%-----------------------------------------------------%
%----------------Choix des composants-----------------%
% Fonction pour le choix des modules les plus économes en énergie

function choix = fonction_choix_composant( e0, e1, e2, e3, e4 )

%-----------------------------------------------------%
%------------Lecture des entrées de la fonction-------% 

nombre_composant = e0; % Nombre de modules disponibles pour chaque élement du circuit 

% les entrées e1->e4 correspondent aux entrées e5->e8 de la
% fonction_consommation_neoud

%-----------------------------------------------------%
% Initialisation du choix 
choix = [1 1 1 1 1];

%-----------------------------------------------------%
% Calcul en deux grandes étapes
% 1) Calcul de la consommation du noeud en changeant à chaque fois un module 
% 2) Recherche du minimum 

for i = 1:(size(nombre_composant,2)) % Pour chaque élement du circuit 
    if (nombre_composant (i)>1) % Si un choix est à faire 
        for i1=1:nombre_composant (i) % Parcourir les modules commerciaux
           
            choix (i)= i1 ;
            consommation (i1)= fonction_consommation_noeud(choix,1,0,0,0,e1,e2,e3,e4); % Calcul de la consommation
        end
        i1 = find (consommation == min(consommation));
        choix (i)= i1;
    end
end

end

