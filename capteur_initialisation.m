%-----------------------------------------------------%
%----------------------Capteur------------------------%
%-----------Initialisation des paramètres-------------%

% Temps de mesure 
 temps_mes = capteur_init (1,composant(1)) ; 

% Transitions  
capteur_su = capteur_init (2,composant(1)); % Temps de démarrage 
capteur_sd = capteur_init (3,composant(1)); % Temps d'extinction 

% % Consommation pendant les différents modes de fonctionnement 
capteur_conso_active = capteur_init (4,composant(1));  % mode actif
capteur_conso_shut_down = capteur_init (5,composant(1)); % mode dormant

clear capteur_init