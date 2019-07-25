%-----------------------------------------------------%
%-------------Consommation ADC instantann�e-----------%
% "adc_courant" est un vecteur pour la repr�sentation de la consommation instantann�e en fonction de "temps"

%-----------------------------------------------------%
%-------Initialisation des variables de calcul--------%
m = []; % Les dates de d�but et de fin d'une fonctionnalit� sont illustr�s dans m sous la forme d'indices dans le vecteur "temps" 
j=1; % compteur  
m(j)=1; 
j=j+1;

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-------Fonction conversion analogique num�rique------%

% Mode dormant  
t_shut_down = cpu_lpm3_active + capteur_su; %temps pass� pendant ce mode  
m(j)= m(j-1)+round (t_shut_down/timestep); % Indice de la date de fin du mode dormant 
n = m(j); % Indice de la date de fin du mode dormant 
l = m(j-1); % Indice de la date du d�but du mode dormant 
j=j+1;

% Mise de la consommation de l'ADC sous sa valeur en mode dormant pendant
% le temps pass� dans ce mode
for i=l:n
    adc_courant (i) = adc_conso_shut_down ;
end 

% Echantillonage et conversion analogique num�rique de chaque �chantillon  
for k=1: (nb_ech-1)   % pour chaque �chantillon 
    % Conversion analogique num�rique
    t_conversion = adc_duree;  
    m(j)= m(j-1)+round (t_conversion/timestep);
    n = m(j);
    l = m(j-1);
    j=j+1;
    
    % Consommation pendant la conversion 
    for i=l:n
        adc_courant (i) = adc_conso + adc_conso_conversion;
    end 
    
    % Mode actif entre deux �chantillons 
    t_inter_echantillons = adc_periode - adc_duree; % Dur�e �coul�e entre deux �chantillons
    m(j)= m(j-1)+round (t_inter_echantillons/timestep);
    n = m(j);
    l = m(j-1);
    j=j+1;
    
    % Consommation mode actif
    for i=l:n
        adc_courant (i) = adc_conso ;
    end 
end 

% Conversion du dernier �chantillon
t_conversion = adc_duree;
m(j)= m(j-1)+round (t_conversion/timestep);
n = m(j);
l = m(j-1);
j=j+1;
% Consommation pendant la conversion
for i=l:n
    adc_courant (i) = adc_conso + adc_conso_conversion;
end 

% Mode Dormant jusqu'� la fin du cycle 
for i=n:N
adc_courant (i) = adc_conso_shut_down;
end 
