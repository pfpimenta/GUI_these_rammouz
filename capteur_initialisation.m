%-----------------------------------------------------%
%----------------------Capteur------------------------%
%-----------Initialisation des param�tres-------------%

% Temps de mesure 
 temps_mes = capteur_init (1,composant(1)) ; 

% Transitions  
capteur_su = capteur_init (2,composant(1)); % Temps de d�marrage 
capteur_sd = capteur_init (3,composant(1)); % Temps d'extinction 

% % Consommation pendant les diff�rents modes de fonctionnement 
capteur_conso_active = capteur_init (4,composant(1));  % mode actif
capteur_conso_shut_down = capteur_init (5,composant(1)); % mode dormant

clear capteur_init