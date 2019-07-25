%-----------------------------------------------------%
%----------------Consommation m�moire-----------------%

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction lecture--------------------%

% R�ception de l'instruction correspondant � la lecture 
a=b;
b = a + round (memoire_op_code/timestep);

% Consommation mode actif
for i=a:b 
    memoire_courant(i) = memoire_conso_active;
end

% Lecture des donn�es 
t = n_coupure*t_data;
a = b; 
b = a + round (t/timestep);

% Consommation mode lecture 
for i=a:b 
    memoire_courant(i) = memoire_conso_lecture;
end

