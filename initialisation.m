%-----------------------------------------------------%
%-------------------Simulation------------------------%
%-----------Initialisation des param�tres-------------%

% Temps de simulation
temps_sim = 2e3;

%-------------------Noeud-----------------------------%
%-----------Initialisation des param�tres-------------%

% Conversion de la p�riode de mesure en ms
% nombre de mesures / nombre de minutes
mesure = 1;
T =(minutes*60)/ mesure*(1e3);

% Nombre d'octets de donn�es par cycle de mesure 
cycle_byte_data = taille_data ;

%-----------------------------------------------------%
%-------------------Composants------------------------%
%-----------Initialisation des param�tres-------------%

% Capteur 
capteur_initialisation; 

% ADC 
adc_initialisation;

% M�moire 
memoire_initialisation;

% Processeur 
processeur_initialisation;

% Module radiofr�quence 
RF_initialisation;

