%-----------------------------------------------------%
%-------------Consommation ADC instantannée-----------%
% "adc_courant" est un vecteur pour la représentation de la consommation instantannée en fonction de "temps"

%-----------------------------------------------------%
%-------Initialisation des variables de calcul--------%
m = []; % Les dates de début et de fin d'une fonctionnalité sont illustrés dans m sous la forme d'indices dans le vecteur "temps" 
j=1; % compteur  
m(j)=1; 
j=j+1;

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-------Fonction conversion analogique numérique------%

% Mode dormant  
t_shut_down = cpu_lpm3_active + capteur_su; %temps passé pendant ce mode  
m(j)= m(j-1)+round (t_shut_down/timestep); % Indice de la date de fin du mode dormant 
n = m(j); % Indice de la date de fin du mode dormant 
l = m(j-1); % Indice de la date du début du mode dormant 
j=j+1;

% Mise de la consommation de l'ADC sous sa valeur en mode dormant pendant
% le temps passé dans ce mode
for i=l:n
    adc_courant (i) = adc_conso_shut_down ;
end 

% Echantillonage et conversion analogique numérique de chaque échantillon  
for k=1: (nb_ech-1)   % pour chaque échantillon 
    % Conversion analogique numérique
    t_conversion = adc_duree;  
    m(j)= m(j-1)+round (t_conversion/timestep);
    n = m(j);
    l = m(j-1);
    j=j+1;
    
    % Consommation pendant la conversion 
    for i=l:n
        adc_courant (i) = adc_conso + adc_conso_conversion;
    end 
    
    % Mode actif entre deux échantillons 
    t_inter_echantillons = adc_periode - adc_duree; % Durée écoulée entre deux échantillons
    m(j)= m(j-1)+round (t_inter_echantillons/timestep);
    n = m(j);
    l = m(j-1);
    j=j+1;
    
    % Consommation mode actif
    for i=l:n
        adc_courant (i) = adc_conso ;
    end 
end 

% Conversion du dernier échantillon
t_conversion = adc_duree;
m(j)= m(j-1)+round (t_conversion/timestep);
n = m(j);
l = m(j-1);
j=j+1;
% Consommation pendant la conversion
for i=l:n
    adc_courant (i) = adc_conso + adc_conso_conversion;
end 

% Mode Dormant jusqu'à la fin du cycle 
for i=n:N
adc_courant (i) = adc_conso_shut_down;
end 
