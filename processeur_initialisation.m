%-----------------------------------------------------%
%------------------------Processeur-------------------%
%-----------Initialisation des paramètres-------------%

% Transitions entre les différents modes 
cpu_lpm0_active = processeur_init (1,composant(3)); % Sommeil -> actif
cpu_active_lpm0 = processeur_init (2,composant(3)); % Actif -> Sommeil
cpu_lpm3_active = processeur_init (3,composant(3)); % Dormant -> actif
cpu_active_lpm3 = processeur_init (4,composant(3)); % Actif -> dormant

%Tableau de fréquence de traitement avec les consommation en mode sommeil
%correspondantes
tableau_frequence = p_sup_processeur; 
tableau_consommation_active = processeur_init (5:4+size(p_sup_processeur,1),composant(3));
tableau_consommation_lpm0 = processeur_init (5+size(p_sup_processeur,1):4+2*size(p_sup_processeur,1),composant(3));

% Fréquence de traitement
i = find (tableau_frequence == cpu_f);

%Consommation selon le mode 
cpu_conso_active = tableau_consommation_active (i) ; % Mode actif 
cpu_conso_lpm0 = tableau_consommation_lpm0 (i) ; % Mode sommeil 
cpu_conso_lpm3 = processeur_init (size(processeur_init,1),composant(3)); % Mode dormant

clear ('processeur_init','p_sup_processeur')

% Temps de traitement : Instructions de l'agorithme de traitement 
nb_instructions = 4e3+ 5*nb_ech; 
t_instructions = (nb_instructions / cpu_f)* 1e-3; 

% Temps de lecture des données stockées non transmises
if (cnx_req<0)  % S'il reste des données à lire 
t_lecture = 0;
else
t_lecture= memoire_op_code + n_coupure*t_data;
end 

% Temps d'effacement effacer la mémoire 
if (block_erase) % Si mémoire pleine 
    t_erase = memoire_op_code+t_block_erase;
else
    t_erase = 0 ;
end

% Temps d'écriture des données produites  
if (ecriture_par_cycle)|| (cnx_req<0) % Si connexion non établie ou si strategie d'écriture de toutes les données
    t_ecriture = memoire_op_code + t_data;  
else
    t_ecriture = 0 ;
end

% Temps de traitement correspondant
t_traitement= t_instructions+ t_lecture + t_ecriture+t_erase;