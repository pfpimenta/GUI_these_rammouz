%-----------------------------------------------------%
%--------Lecture de la feuille "Problème"-----------%

% Coordonnées du fichier Excel en question 
load ('initialisation','fichier_in','fichier_out');
f = fichier_in;
s = 'Problème'; 

%-----------------------------------------------------%
% Constitution du noeud
% Lecture des composants choisis
[n,m,r] = xlsread (f, s, 'b17:f17');
if ((size(n,2)>0)||(size(m,2)>0))
    
    composant =[];
    a = ['d4:m4  ','d18:m18','d33:m33','d66:m66', 'd95:m95']; % cases à lire
    j =1;
    for i=1:size(r,2)
        % Identification des composants à travers leurs noms
        id = fonction_identification_composant(r(i), fichier_in,'Composants',a(j:j+6));
        j=j+7;
        composant = [composant,id];
    end
    load ('initialisation','nb_composant')
    for i=1:size(composant,2)
        if (composant(i)~=0)
            nb_composant (i)= 1; % Etablissement du vecteur qui montre le nombre de modules disponibles pour chaque 
                                 % élement du circuit
        end
    end
end


%-----------------------------------------------------%
% Configuration électronique 

% Fréquence de traitement : Lecture et conversion d'unité
[n,m] = xlsread (f, s, 'b23:h23');
if (strcmp (m, 'kHz'))
    frequence_cpu = n *1e-3;
elseif (strcmp (m, 'Hz'))
    frequence_cpu = n *1e-6;
else
    frequence_cpu = n ;
end

% Fréquence d'échantillonnage : Lecture et conversion d'unité
[n,m] = xlsread (f, s, 'b24:h24');
if (strcmp (m, 'MHz'))
    adc_nb_echantillons = n *1e6;
elseif (strcmp (m, 'kHz'))
    adc_nb_echantillons = n *1e3;
else
    adc_nb_echantillons = n ;
end

%Puissance de transmission : Lecture et conversion d'unité
[n,m] = xlsread (f, s, 'c25:h25');
puissance_rf_tx =n;

%-----------------------------------------------------%
%Capacité des batteries disponibles : Lecture et conversion d'unité
[n,m] = xlsread (f, s, 'b27:h27');
if (strcmp (m, 'Ah'))
    capacite_batterie = n *1e6;
elseif (strcmp (m, 'mAh'))
    capacite_batterie = n *1e3;
else
    capacite_batterie = n ;
end

%-----------------------------------------------------%
% Autonomie : Lecture et conversion d'unité
[n,m] = xlsread (f, s, 'b31:c31');
if (strcmp (m, 'jours'))
    autonomie = n *24;
else
    autonomie = n ;
end

%-----------------------------------------------------%
% Durée du monitoring  : Lecture et conversion d'unité
[n,m] = xlsread (f, s, 'b35:c35');
n_jours = n;

%-----------------------------------------------------%
% Trajet 
[n,m] = xlsread (f, s, 'b39:b39');
if (strcmp (m, 'Non connu')) % Trajet non connu, à optimiser 
    trajet = [];
elseif (strcmp (m, 'Aléatoire')) % Trajet aléatoire, à générer avec la fonction Matlab 
    trajet = fonction_generation_trajet( 30 );
else    % prédéfini, à lire, et à convertir en minutes
    [n,m] = xlsread (f, s, 'b42:e45');
    trajet = [];
    for i =1:size (n,2)
        trajet = [trajet, n(i,1),n(i,3)];
    end
    trajet = trajet *1440;
end

%-----------------------------------------------------%
% Nombre de noeuds 
[n,m] = xlsread (f, s, 'b3:b3');
nb = n ; 

%-----------------------------------------------------%
% Cas d'un noeud unique 
if (nb == 1) 
    noeud =1 ;
    % Nombre d'octets par mesure
        [n,m] = xlsread (f, s, 'c9:c9');
        taille_data = n;
        
        %Période de mesure
        [n,m] = xlsread (f, s, 'c21:h21');
        periode_mesure = n;
     
        % Algorithme de connexion : continu ou à basse consommation    
    [n,m] = xlsread (f, s, 'b4:b4');
    if (strcmp (m, 'continu'))  % si continu 
        xlswrite(fichier_out,{'Continue'},'Solution','b6:b6')
        periode_transmission = periode_mesure;  % mesure et transmission confondue
        data_max = [] ; % Initialisation de la taille de données maximale à transmettre  
        synchronisation = 0; % connecté en permanence 
        time_cntd = -1; % connecté en permanence 
    else 
        [n,m] = xlsread (f, s, 'c22:h22');
        periode_transmission = n; % Affectation de la valeur correspondante à la période de transmission 
        data_max = []; % Initialisation de la taille de données maximale à transmettre  
        synchronisation =1 ; % Algorithme pour la réduction de la consommation BLE
    end

else  % si plusieurs noeuds 
    [n,m] = xlsread (f, s, 'c7:g9');
    synchronisation = 1; % algorithme pour la réduction de la consommation 
    
    % Lecture des valeurs pour la configuration du réseau 
    periode_mesure = n(1,:); % période de mesure 
    periode_transmission = n(2,:); % période de transmission 
    taille_data = n(3,:); % codage de l'information 
    data_max = []; % Initialisation de la taille de données maximale à transmettre 

    %-----------------------------------------------------%    
    % Noeud d'intérèt, à optimiser
    [n,m,r]= xlsread (f, s, 'b13:b13');
    noeud = fonction_identification_composant(r, fichier_in,'Problème','c6:g6');
end

[n,m] = xlsread (f,s, 'b21:b25');
m{5} = '';

%-----------------------------------------------------%    
% Préférences utilisateur représentés par deux valeurs : min et max 
% une case laissée vide signifie que l'utilisateur n'a pas de contrainte
% sur cette valeur 
% Lecture des données et remplissage des vecteur ub (upper bound) et lb
% (lower bound)

clear a 

[n,k,r] = xlsread (f,s, 'i21:j25');
n = cell2mat (r(:,1));


for i = 1:size(m,1);
    switch i 
        case 1 
            if (isnan(n(i)))
                n (i) = min (periode_mesure);
            end
        case 2 
             if (isnan(n(i)))
                if (size (periode_transmission,2))
                    n (i) = min (periode_transmission);
                else 
                    n (i) = min (periode_mesure);
                end
             end
        case 3 
            if (isnan(n(i)))
                n (i) = min (frequence_cpu);
            end
            if  (strcmp (m(i), 'kHz'))
                n(i) = n(i) *1e-3;
            elseif (strcmp (m(i), 'Hz'))
                n(i) = n(i) *1e-6;
            end
        case 4 
            if (isnan(n(i)))
                n (i) = min (adc_nb_echantillons);
            end
            if  (strcmp (m(i), 'kHz'))
                n(i) = n(i) *1e3;
            elseif (strcmp (m(i), 'MHz'))
                n(i) = n(i) *1e6;
            end
        case 5 
            if (isnan(n(i)))
                n (i) = min (puissance_rf_tx);
            end
    end
end
lb = n ;
% Préférences utilisateur 
[n,k,r] = xlsread (f,s, 'k21:l25');
n = cell2mat (r(:,1));


for i = 1:size(m,1)
    switch i 
        case 1 
            if (isnan(n(i)))
                n (i) = max (periode_mesure);
            end
        case 2 
             if (isnan(n(i)))
                if (size (periode_transmission,2))
                    n (i) = max (periode_transmission);
                else 
                    n (i) = max (periode_mesure);
                end
             end
        case 3 
            if (isnan(n(i)))
                n (i) = max (frequence_cpu);
            end
            if  (strcmp (m(i), 'kHz'))
                n(i) = n(i) *1e-3;
            elseif (strcmp (m(i), 'Hz'))
                n(i) = n(i) *1e-6;
            end
        case 4 
            if (isnan(n(i)))
                n (i) = max (adc_nb_echantillons);
            end
            if  (strcmp (m(i), 'kHz'))
                n(i) = n(i) *1e3;
            elseif (strcmp (m(i), 'MHz'))
                n(i) = n(i) *1e6;
            end
        case 5 
            if (isnan(n(i)))
                n (i) = max (puissance_rf_tx);
            end
    end
end
ub = n;

%-----------------------------------------------------%    
% Sauvegarde des données
save ('initialisation','nb_composant','-append')
clear ('a','f','i','id','j','m','n','r','s')
load initialisation 
save initialisation 