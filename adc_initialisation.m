%-----------------------------------------------------%
%----------Convertisseur Analogique Numérique---------%
%-----------Initialisation des paramètres-------------%

% Durée de la conversion 
adc_duree = adc_init (1,composant(2));

% Transitions   
adc_su = adc_init (2,composant(2));  % Temps de démarrage 
adc_sd = adc_init (3,composant(2));  % Temps d'extinction 

% Période d'échantillonnage 
adc_periode = temps_mes /(nb_ech-1);
adc_periode = round (adc_periode*1e3)/(1e3);

% Consommation pendant les différents modes de fonctionnement 
adc_conso=adc_init (4,composant(2)); % Mode actif 
adc_conso_conversion = adc_init (5,composant(2)) ; % Conversion 
adc_conso_shut_down = adc_init(6,composant(2)); % Mode dormant

clear adc_init
