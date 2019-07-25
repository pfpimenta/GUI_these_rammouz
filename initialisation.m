%-----------------------------------------------------%
%-------------------Simulation------------------------%
%-----------Initialisation des paramètres-------------%

% Temps de simulation
temps_sim = 2e3;

%-------------------Noeud-----------------------------%
%-----------Initialisation des paramètres-------------%

% Conversion de la période de mesure en ms
% nombre de mesures / nombre de minutes
mesure = 1;
T =(minutes*60)/ mesure*(1e3);

% Nombre d'octets de données par cycle de mesure 
cycle_byte_data = taille_data ;

%-----------------------------------------------------%
%-------------------Composants------------------------%
%-----------Initialisation des paramètres-------------%

% Capteur 
capteur_initialisation; 

% ADC 
adc_initialisation;

% Mémoire 
memoire_initialisation;

% Processeur 
processeur_initialisation;

% Module radiofréquence 
RF_initialisation;

