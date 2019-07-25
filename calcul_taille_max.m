%---------------------------------------------------------------------%
%---------Calcul de la taille maximale de donn�es � transmettre-------%
% Fonction pour calculer la taille maximale de donn�es � transmettre pendant
% la journ�e en fonction de la routine de vie du patient

function taille_max = calcul_taille_max( e0, e1, e2, e3)

%-----------------------------------------------------%
%------------Lecture des entr�es de la fonction-------% 

trajet = e0 ; % Routine de vie du patient 

connexion = e1; % P�riode de transmission

duree_cycle= e2; % P�riode de mesure 

n_bytes = e3; % Nombre d'octets par mesure (en fonction du codage)

n_cycles = 24 * 60/duree_cycle; % Nombre de mesures par jour 

%-----------------------------------------------------%
%---------------------- Trajet -----------------------%
% D�termination de l'�tat du r�seau pour chaque mesure  

% Initialisation du vecteur CR qui correspond � l'�tat du r�seau 
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
% Etablissement du nombre de mesures non transmises � chaque instant en
% fonction de l'�tat de la connexion r�seau

% Initialisation du vecteur coupure 
coupure = zeros (1,n_cycles); 

% 1) Calcul de la premi�re valeur de la journ�e (apr�s minuit) 
if (size(coupure,2)==1)
    if (CR(1)<0)
        coupure (1) = 1;
    else 
        coupure (1) = 0;
    end
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

% 2) Calcul du reste des valeurs du vecteur coupure 
for i=2:n_cycles 
    if ((CR(i)<0)&&(CR(i-1)<0))
            coupure (i) = coupure (i-1)+1; 
    end
    if ((CR(i)==1)&&(CR(i-1)<0))
            coupure (i) = coupure (i-1)+1; 
    end
end 
end

% La dur�e maximale de coupure du r�seau
coupure_max = max (coupure);

% La taille maximale de donn�es produites � transmettre
taille_max = max ( coupure_max * n_bytes, n_bytes) ;

end

