%-----------------------------------------------------%
%----------------Consommation processeur--------------%
% "processeur_courant" est la consommation instantannée en fonction de "temps"

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

% Mode dormant jusqu'à la fin du cycle
for i=n:N
processeur_courant (i) = cpu_conso_lpm3;
end 

%-----------------------------------------------------%
%----------Simulation des accès mémoire---------------%
% Réveil de la mémoire 
if (n_coupure)||(ecriture_par_cycle)||(cnx_req <0)||(block_erase) % Si accès mémoire
     
    % Transmission de l'instruction correspondant au réveil 
    t = cpu_lpm3_active + capteur_su + temps_mes + adc_duree + t_instructions; 
    a = 1 + round (t/timestep); 
    t = memoire_op_code;
    b = a + round (t/timestep);
    
    % Consommation de la mémoire = consommation en mode actif
    for i=a:b
        memoire_courant (i) = memoire_conso_active ;
    end
    
    
    % transition de la mémoire dormant -> actif 
    a = b; 
    t = memoire_shut_down_active;
    b = a + round (t/timestep);
    
    % Consommation de la mémoire = consommation en mode actif
    for i=a:b
        memoire_courant (i) = memoire_conso_active ;
    end
end

% Lecture des données
if ((n_coupure) && (cnx_req>=0))  % S'il reste des données non transmise dans la mémoire
    memoire_lecture;
end

% Effacement d'un bloc ou plus de la mémoire
if(block_erase) % Si la mémoire est pleine
    memoire_erase;
end

% Ecriture d'une mesure dans la mémoire
if (ecriture_par_cycle)||(cnx_req <0)
    memoire_ecriture_par_cycle;
end


% Passage de la mémoire en mode dormant
if (n_coupure)||(ecriture_par_cycle)||(cnx_req <0)||(block_erase) % si accès mémoire
    a = b;
    % Transmission de l'instruction correspondant au réveil
    t = memoire_op_code ;
    b = a + round (t/timestep);
    for i=a:b
    memoire_courant (i) = memoire_conso_active ;
    end
    % Transition de la mémoire du mode actif -> dormant
    a = b; 
    t = memoire_active_shut_down;
    b = a + round (t/timestep);
    
    % Consommation de la mémoire = consommation en mode attente
    for i=a:b
        memoire_courant (i) = memoire_conso_stand_by ;
    end
end
