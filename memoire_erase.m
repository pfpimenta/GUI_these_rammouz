%-----------------------------------------------------%
%----------------Consommation m�moire-----------------%

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction effacement-----------------%

% R�ception de l'instruction correspondant � l'effacement
a=b;
b = a + round (memoire_op_code/timestep);

%Consommation mode actif
for i=a:b 
    memoire_courant(i) = memoire_conso_active;
end

% Effacement du bloc 
a=b;
b = a + round (t_block_erase/timestep);

% Consommation mode effacement
for i=a:b 
    memoire_courant(i) = memoire_conso_erase;
end
