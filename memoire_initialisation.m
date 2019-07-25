%-----------------------------------------------------%
%-----------------------M�moire-----------------------%
%-----------Initialisation des param�tres-------------%

% Param�tre de la communication SPI 
memoire_f_SCK = memoire_init (3,composant(4)) ; % Fr�quence
memoire_periode = 1/memoire_f_SCK; % P�riode

% Temps de lecture/�criture 
t_data = memoire_init (5,composant(4)) * cycle_byte_data / memoire_init (4,composant(4)) ; 

% Transitions entre les diff�rents mode 
memoire_op_code = memoire_init (2,composant(4)) * memoire_periode * (1e-3);  % Temps pours la transmission des instructions
memoire_shut_down_active =  memoire_init (10,composant(4)); % transition dormant -> actif 
memoire_active_shut_down =  memoire_init (11,composant(4)); % transition actif -> dormant

% Temps pour effacer une partie ou la totalit� de la m�moire
t_block_erase = memoire_init (9,composant(4)); 

% Consommation pendant les diff�rents modes de fonctionnement
memoire_conso_active =  memoire_init (14,composant(4)); % Mode actif
memoire_conso_ecriture =  memoire_init (15,composant(4)); % Mode �criture
memoire_conso_lecture =  memoire_init (16,composant(4)); % Mode lecture 
memoire_conso_erase =  memoire_init (17,composant(4)); % Mode effacement 
memoire_conso_stand_by =  memoire_init (18,composant(4));  % Mode attente 
memoire_conso_shut_down =  memoire_init (19,composant(4)); % Mode dormant

clear memoire_init