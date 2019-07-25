%-----------------------------------------------------%
%---------Code pour le logiciel de conception---------%
% Analyse des variables et lancement de la fonction de r�solution
% appropri�e

%-----------------------------------------------------%
% Choix de l'algorithme d'optimisation convenable suivant les donn�es 

% Initialisation des variables de calcul
a0 = prod (nb_composant); % si a0 = 1, les composants du noeud sont pr�d�finis, sinon, un choix de composants est requis
a1 = size (capacite_batterie,2);  % nombre de batteries disponibles 

% Nombre de possibilit�s pour les variables � optimiser 
a2 = size (periode_mesure,2); % P�riode de mesure
a3 = size (periode_transmission,2); % P�riode de transmission 
a4 = size (frequence_cpu,2); % Fr�quence CPU 
a5 = size (puissance_rf_tx,2); % Puissance de transmission RF
a6 = size (adc_nb_echantillons,2); % Fr�quence d'�chantillonnage 

% Routine de vie du patient 
a7 = size (trajet,2);
% Autonomie du noeud 
a8 = size (autonomie,2);

erreur = 0;

%-----------------------------------------------------%
% Cas 1 : Calcul de l'autonomie d'un noeud donn� 
if ((a0*a1*a2*a3*a4*a5*a6==1) && (size(trajet,2) ~=0) && (size(autonomie,2) ==0))
    
    if ((nb ==1)&&(synchronisation==1)) % si noeud unique + algorithme pour la r�duction de la consommation 
        fonction_configuration_reseau (periode_mesure(1),periode_transmission(1));
    end
    conso = fonction_consommation_jour ( nb_composant, trajet, n_jours, periode_transmission (1), periode_mesure (1), frequence_cpu(1), puissance_rf_tx(1),adc_nb_echantillons (1));
    autonomie = capacite_batterie(1)/(conso * 24);
    
    % Ecriture de la solution dans le fichier Excel 
    xlswrite(fichier_out,{'Autonomie'},'Solution','a9:a9')
    xlswrite (fichier_out,autonomie,'Solution','b9:b9')
    xlswrite(fichier_out,{'jours'},'Solution','c9:c9')

%-----------------------------------------------------%    
% Cas 2 : Calcul de la dur�e de d�connexion quotidienne tol�r�e     
elseif ((a0*a1*a2*a3*a4*a5*a6==1) && (size(trajet,2) ==0) && (size(autonomie,2) ~=0)&&(nb==1))
    
    deconnexion_toleree;
    
%-----------------------------------------------------%
% Cas 3 : Choix d'une source d'�nergie convenable    
elseif ((a0*a2*a3*a4*a5*a6==1) && (a1>1) &&(size(trajet,2) ~=0) && (size(autonomie,2) ~=0)) 
    
    if ((nb ==1)&&(synchronisation==1))
        fonction_configuration_reseau (periode_mesure(1),periode_transmission(1));
    end
    choix_batterie;
    
%-----------------------------------------------------%
% Cas 4 : Optimisation de l'architecture �lectronique 
elseif ((a0*a2*a3*a4*a5~=1) && (size(trajet,2) ~=0) && (size(autonomie,2) ~=0))
    
    optimisation ;
    
%-----------------------------------------------------%
% Cas 5 : Calcul de la consommation du noeud (pas de source d'�nergie
% d�finie)
elseif ((a0*a2*a3*a4*a5*a6==1) && (a1==0) &&(size(trajet,2) ~=0) && (size(autonomie,2) ==0))
    
    if ((nb ==1)&&(synchronisation==1))
        fonction_configuration_reseau (periode_mesure(1),periode_transmission(1));
    end
   conso = fonction_consommation_jour ( nb_composant, trajet, n_jours, periode_transmission (1), periode_mesure (1), frequence_cpu(1), puissance_rf_tx(1),adc_nb_echantillons (1));
   
   % Ecriture de la solution dans le fichier Excel 
   xlswrite(fichier_out,{'Consommation'},'Solution','a9:a9')
   xlswrite (fichier_out,conso,'Solution','b9:b9')
   xlswrite(fichier_out,{'�A'},'Solution','c9:c9')

%-----------------------------------------------------%
% Si le probl�me n'admet pas de solution 
else 
    
    xlswrite(fichier_out,{'Les donn�es en entr�es sont insuffisantes pour envisager une configuration'},'Solution','a8:f8')
    erreur = 1;
end

%-----------------------------------------------------%
% Ecrire le temps de connexion autoris� dans le cas d'un noeud unique
% adoptant l'algorithme pour la r�duction de la consommation du BLE
if ((nb==1)&&(synchronisation ==1)&& (erreur==0))
    load ('initialisation','time_cntd')
    xlswrite(fichier_out,time_cntd/1000,'Solution','b6:b6')
end
    