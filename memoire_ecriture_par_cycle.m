%-----------------------------------------------------%
%----------------Consommation mémoire-----------------%

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction écriture-------------------%

% Réception de l'instruction correspondant à l'écriture  
a=b;
b = a + round (memoire_op_code/timestep);

% Consommation mode actif
for i=a:b 
    memoire_courant(i) = memoire_conso_active;
end

% Ecriture des données 
t = cycle_byte_data*t_data;
a = b ; 
b = a + round (t/timestep);
% Consommation mode écriture 
for i=a:b 
    memoire_courant(i) = memoire_conso_ecriture;
end

