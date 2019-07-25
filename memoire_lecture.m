%-----------------------------------------------------%
%----------------Consommation mémoire-----------------%

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction lecture--------------------%

% Réception de l'instruction correspondant à la lecture 
a=b;
b = a + round (memoire_op_code/timestep);

% Consommation mode actif
for i=a:b 
    memoire_courant(i) = memoire_conso_active;
end

% Lecture des données 
t = n_coupure*t_data;
a = b; 
b = a + round (t/timestep);

% Consommation mode lecture 
for i=a:b 
    memoire_courant(i) = memoire_conso_lecture;
end

