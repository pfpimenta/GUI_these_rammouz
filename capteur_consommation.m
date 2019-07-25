%-----------------------------------------------------%
%----------------Consommation capteur-----------------%
% "capteur_courant" est la consommation instantannée en fonction de "temps"

%-----------------------------------------------------%
%-------Initialisation des variables de calcul--------%
m = [];
j=1;
m(j)=1;
j=j+1;

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction mesure---------------------%

% Mode dormant  
t_shut_down = cpu_lpm3_active ; 
m(j)= m(j-1)+round (t_shut_down/timestep);
n = m(j);
l = m(j-1);
j=j+1;

% Consommation en mode dormant
for i=l:n
    capteur_courant (i) = capteur_conso_shut_down ;
end

% Mode actif pendant la phase de mesure
t_active = capteur_su + temps_mes + adc_duree + capteur_sd; 
m(j)= m(j-1)+round (t_active/timestep);
n = m(j);
l = m(j-1);
j=j+1;

% Consommation mode actif
for i=l:n
    capteur_courant(i) = capteur_conso_active ;
end

% Retour au mode dormant jusqu'à la fin du cycle
for i=n:N 
    capteur_courant (i) = capteur_conso_shut_down; 
end

