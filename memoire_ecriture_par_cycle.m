%-----------------------------------------------------%
%----------------Consommation m�moire-----------------%

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction �criture-------------------%

% R�ception de l'instruction correspondant � l'�criture  
a=b;
b = a + round (memoire_op_code/timestep);

% Consommation mode actif
for i=a:b 
    memoire_courant(i) = memoire_conso_active;
end

% Ecriture des donn�es 
t = cycle_byte_data*t_data;
a = b ; 
b = a + round (t/timestep);
% Consommation mode �criture 
for i=a:b 
    memoire_courant(i) = memoire_conso_ecriture;
end

