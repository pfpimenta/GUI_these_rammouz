%-----------------------------------------------------%
%---------------Module radiofréquence-----------------%
%-----------Initialisation du protocole---------------%

option = 1 ; % Protocole Bluetooth Low Energy 
             % Ajouter d'autres options pour d'autres protocoles 

             
%-----------------------------------------------------%
%----------------Module radiofréquence----------------%
%-----------Initialisation des paramètres-------------%

switch option % Test pour déterminer le protocle de communication adopté 
    case 1 % protocole Bluetooth Low Energy 
        
        % Paramètres du protocole 
        t_conninterval = module_rf_init (1,composant(5)) ; % Intervalle de connexion 
        t_adv_interval = module_rf_init (2,composant(5))  ; % Intervalle de signalisation 
        
        % Temps de signalisation et temps de connexion
        time_adv = time_cntd; 
        if (time_cntd ==-1)
            time_cntd = T; % connexion permanente - pendant toute la période 
            time_adv = T ; % signalisation permanente - pendant toute la période
        end
        
        % Temps pour l'établissement de la connexion
        time_cnting = 1e3; % temps pour l'établissement de la connexion 
        
        % Tableau des différentes puissances de transmission
        tableau_puissance_rf_tx = p_sup_module_rf;
        % Tableau des consommation en mode tx en fonction des différentes puissances de transmission
        tableau_consommation_rf_tx = module_rf_init (7:6+size(p_sup_module_rf,1),composant(5));
        
        % Consommation en mode tx en fonction de la puissance de
        % transmission définie
        i = find (tableau_puissance_rf_tx == rf_puissance);
        rf_conso_tx = tableau_consommation_rf_tx (i) ;
        
        % Consommation pendant les autres modes de fonctionnement 
        rf_conso_rx = module_rf_init (7+size(p_sup_module_rf,1),composant(5)); % Consommation en mode Rx
        rf_conso_actif = module_rf_init (8+size(p_sup_module_rf,1),composant(5)); % Consommation en mode actif 
        rf_conso_sleep = module_rf_init (9+size(p_sup_module_rf,1),composant(5)) ; % Consommation en mode PM2
        rf_conso_sleep_2 = module_rf_init (10+size(p_sup_module_rf,1),composant(5)) ; % Consommation en mode PM3
            
end