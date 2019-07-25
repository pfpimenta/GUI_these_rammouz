%-----------------------------------------------------%
%---------Consommation noeud : durée monitoring-------%
% Fonction utilisée pour calculer la consommation du noeud sur la période
% de monitoring

function conso_moyenne = fonction_consommation_jour(e0 ,e1, e2, e3, e4, e5, e6,e7)

%-----------------------------------------------------%
%------------Lecture des entrées de la fonction-------% 

% Composants choisis 
composant = e0 ; 

% Trajet de la personne en minutes
trajet = e1;

% Durée du processus de monitoring 
n_jours = e2 ; 


% Quantité de données maximale pouvant être transmise pendant la durée de connexion
% autorisée
load ('initialisation','data_max')

% Configuration électronique 
connexion = e3 ; % Période de transmission 
var1 = e4 ; % Période de mesure
var2 = e5 ; % fréquence CPU
var3 = e6; % puissance de transmission du module RF 
var4 = e7; % nombre d'échantillons pour l'ADC
 

% Caractéristiques de la mémoire 
% Permet de déterminer la stratégie adoptée pour la mémorisation des données
load ('initialisation','memoire_init')
memoire_taille = memoire_init(1,composant(4)); % Taille totale de la mémoire 
memoire_bloc = memoire_init (8,composant(4)) ;  % Taille à effacer lorsque la mémoire est pleine
memoire_erase = 0 ; % Mémoire vide
clear memoire_init

% Taille des données obtenues par mesure 
load ('initialisation','taille_data')
n_bytes_cycle = taille_data;

% Période de mesure ou durée du cycle  
duree_cycle = var1;

% Nombre de mesures par jour 
n_cycles = 24 * 60/duree_cycle;

%-----------------------------------------------------%
%---------------------- Trajet -----------------------%
% Determination de l'état du réseau pour chaque mesure  

% Initialisation du vecteur CR qui correspond à l'état du réseau 
CR = ones (1,n_cycles);
CR = CR *(-2); 

% Calcul des instants de mesures et de transmission
date_mesure = (0:duree_cycle:24*60 - duree_cycle);
date_connexion = (0:connexion:24*60-connexion);

% Etablissement du vecteur CR en fonction du trajet 
for i = 1: size (date_mesure,2)
    for j = 1 : size(date_connexion,2)
        if (date_mesure (i) == date_connexion (j))
            CR (i)=1;
        end
    end
end

for i = 1: size (date_mesure,2)
    for j = 1 : 2 : size(trajet,2)
        if ((date_mesure (i) >= trajet (j))&& (date_mesure(i) < trajet (j+1))) & (CR(i)==1)
            CR (i)=-1;
        
        end  
    end 
end

%-----------------------------------------------------%
% Etablissement du nombre de mesures non transmises à chaque instant en
% fonction de l'état de la connexion réseau

% Initialisation du vecteur coupure 
coupure = zeros (1,n_cycles);

% 1) Calcul de la première valeur de la journée (après minuit)
if (size(coupure,2)==1)
    if (CR(1)<0)
        coupure (1) = 1;
    else 
        coupure (1) = 0;
    end
    fprintf ('a')
else
if (CR(1)<0)
    i = n_cycles;
    while (1)
        if (CR(i)<0)
            i=i-1; 
        else
            break;
        end 
    end
    coupure (1) = n_cycles - i;
end

% 2) Le reste des valeurs du vecteur coupure 
for i=2:n_cycles 
    if ((CR(i)<0)&&(CR(i-1)<0))
            coupure (i) = coupure (i-1)+1; 
    end
    if ((CR(i)==1)&&(CR(i-1)<0))
            coupure (i) = coupure (i-1)+1; 
    end
end 
end 
if (size (data_max,2)>0)
    a = 0 ;
    for i =1:n_cycles
        if (CR(i)==1)
            coupure (i) = coupure (i) + a ;
            if (coupure (i) > data_max)

                a = coupure (i) -data_max ;
                coupure (i) = data_max ;
            else 
                a=0;
            end 
        end 
    end
    if ( a~=0)
        fprintf ('error')
    end
end



% La durée maximale de coupure du réseau
coupure_max = max (coupure);

% Le nombre de cycle de reprise de connexion 
j= 1 ;
for i=1:n_cycles 
    if ((CR(i)==1)&&(coupure(i)~=0))
        j=j+1;
    end
end
n_cycles_reprise = j-1 ;


%----------------------------------------------------------%
% Etablissement de l'approche utilisé pour la mémorisation %
data_total = n_cycles * n_jours * n_bytes_cycle ;  % Calcul de la taille de données générée pendant le monitoring
if (memoire_taille >= data_total)
    memorisation_par_cycle = 1 ;
else
    memorisation_par_cycle = 0 ;
end 

%----------------------------------------------------------%
%--------------- Simplification du calcul -----------------%
%----------------------------------------------------------%

% Consommation pour un cycle avec une connection établie avec une mesure à
% transmettre 
coupure_normal = connexion/duree_cycle-1;
conso_normal = fonction_consommation_noeud (composant, 1,connexion/duree_cycle-1, memorisation_par_cycle,0, var1, var2, var3, var4);

% Consommation pendant les cycles de coupure réseau 
conso_coupure = fonction_consommation_noeud (composant,-1,0, memorisation_par_cycle,0,var1, var2, var3, var4);

% Consommation pendant les cycles de mesures sans transmission 
 conso_mesure = fonction_consommation_noeud (composant,-2,0, memorisation_par_cycle,0,var1, var2, var3, var4);

% Consommation pendant les cycles de reprise de connection 
j= 1 ;
post_coupure = [];
for i=1:n_cycles 
    if ((CR(i)==1)&&(coupure(i)~=0)&&coupure(i)~= coupure_normal)
        m = find (post_coupure == coupure(i));
        if ( size (m,2) == 0)
           
            post_coupure (j) = coupure (i);
            conso_post_coupure (j) = fonction_consommation_noeud (composant, 1,coupure(i), memorisation_par_cycle,0,var1, var2,var3, var4);
            j=j+1;
        end
        m = [];
    end
end

%----------------------------------------------------------%
%------------------------ Calcul --------------------------%
% Iteration sur les jours du monitoring
% Lorsque les conditions du fonctionnement sont identiques aux conditions
% de calcul précédent, la valeur est directement affecté à l'instant 
% Si non la fonction de calcul sur un cycle est appelée avec les entrées
% correspondantes

% Initialisation des variables de calcul 
taille_donnee = 0 ; % Taille de données écrites dans la mémoire 
k = 1;

for j=1:n_jours % Boucle sur les jours du monitoring 
    
    for i=1:n_cycles % Boucle sur les cycles pendant un jour
        
        if ((CR(i)==1)&&(coupure(i)==coupure_normal)&&(memoire_erase==0))
            conso(i)=conso_normal; % Cycle avec connexion établie 
        elseif ((CR(i)==-1)&&(memoire_erase==0))
            conso(i) = conso_coupure ; % Cycle avec connexion non établie
        elseif ((CR(i)==-2)&&(memoire_erase==0))
            conso(i) = conso_mesure; % Cycle de mesure sans transmission 
        elseif ((CR(i)==1)&&(coupure(i)~=0)&& (coupure(i)~= coupure_normal)&&(memoire_erase==0))
            k = find (post_coupure == coupure(i)); % Cycle de reprise de connexion 
            conso(i)= conso_post_coupure (k);
        else
            conso(i) = fonction_consommation_noeud (composant, CR(i),coupure(i), memorisation_par_cycle,memoire_erase, var1, var2, var3, var4);
            memoire_erase=0; % Cas différent des cas précalculés
        end
        
        % Evolution de l'usage mémoire
        if ((CR(i)< 0))
            taille_donnee = taille_donnee + n_bytes_cycle; % Taille de données écrites
        end
 
        if ((taille_donnee + n_bytes_cycle) > memoire_taille) % Test si la partie vide de la mémoire est remplie
            memoire_erase = 1; % Mémoire pleine -> effacer la mémoire 
            memoire_taille = memoire_bloc + memoire_taille - taille_donnee;  % Taille de la mémoire initialisée à la taille effacée
            taille_donnee = 0 ; % Usage mémoire = 0
        end
    end
    conso_jour(j)= mean (conso); % Vecteur des consommations moyennes pendant chaque jour 
     
end

conso_moyenne = mean (conso_jour); % Valeur de la consommation moyenne sur toute la durée du monitoring


end

