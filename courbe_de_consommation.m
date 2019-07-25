%-----------------------------------------------------%
%--------------Courbes de consommation----------------%
% Tracé des courbes de consommations instantannées sur la durée de
% simulation

% Capteur
subplot (2,3,1) 
plot (temps,capteur_courant)

% ADC
subplot (2,3,2)
plot (temps, adc_courant)

% Processeur 
subplot (2,3,3)
plot (temps,processeur_courant)

% Mémoire 
subplot (2,3,4)
plot (temps,rf_courant)

% Module RF
subplot (2,3,5)
plot (temps,memoire_courant)

% Courant total
subplot (2,3,6)
plot (temps,total_courant)