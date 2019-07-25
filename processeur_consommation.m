%-----------------------------------------------------%
%----------------Consommation processeur--------------%
% "processeur_courant" est la consommation instantann�e en fonction de "temps"

%-----------------------------------------------------%
%-------Initialisation des variables de calcul--------% 
m = [];
j=1;
m(j)=1;
j=j+1;

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction traitement-----------------%

% Mode actif 
t_actif = cpu_lpm3_active + capteur_su + temps_mes + adc_duree + t_traitement + cpu_active_lpm3; 
m(j)= m(j-1)+round (t_actif/timestep);
n = m(j);
l = m(j-1);
j=j+1;

% Consommation mode actif
for i=l:n
    processeur_courant (i) = cpu_conso_active ;
end 

% Mode dormant jusqu'� la fin du cycle
for i=n:N
processeur_courant (i) = cpu_conso_lpm3;
end 

%-----------------------------------------------------%
%----------Simulation des acc�s m�moire---------------%
% R�veil de la m�moire 
if (n_coupure)||(ecriture_par_cycle)||(cnx_req <0)||(block_erase) % Si acc�s m�moire
     
    % Transmission de l'instruction correspondant au r�veil 
    t = cpu_lpm3_active + capteur_su + temps_mes + adc_duree + t_instructions; 
    a = 1 + round (t/timestep); 
    t = memoire_op_code;
    b = a + round (t/timestep);
    
    % Consommation de la m�moire = consommation en mode actif
    for i=a:b
        memoire_courant (i) = memoire_conso_active ;
    end
    
    
    % transition de la m�moire dormant -> actif 
    a = b; 
    t = memoire_shut_down_active;
    b = a + round (t/timestep);
    
    % Consommation de la m�moire = consommation en mode actif
    for i=a:b
        memoire_courant (i) = memoire_conso_active ;
    end
end

% Lecture des donn�es
if ((n_coupure) && (cnx_req>=0))  % S'il reste des donn�es non transmise dans la m�moire
    memoire_lecture;
end

% Effacement d'un bloc ou plus de la m�moire
if(block_erase) % Si la m�moire est pleine
    memoire_erase;
end

% Ecriture d'une mesure dans la m�moire
if (ecriture_par_cycle)||(cnx_req <0)
    memoire_ecriture_par_cycle;
end


% Passage de la m�moire en mode dormant
if (n_coupure)||(ecriture_par_cycle)||(cnx_req <0)||(block_erase) % si acc�s m�moire
    a = b;
    % Transmission de l'instruction correspondant au r�veil
    t = memoire_op_code ;
    b = a + round (t/timestep);
    for i=a:b
    memoire_courant (i) = memoire_conso_active ;
    end
    % Transition de la m�moire du mode actif -> dormant
    a = b; 
    t = memoire_active_shut_down;
    b = a + round (t/timestep);
    
    % Consommation de la m�moire = consommation en mode attente
    for i=a:b
        memoire_courant (i) = memoire_conso_stand_by ;
    end
end
