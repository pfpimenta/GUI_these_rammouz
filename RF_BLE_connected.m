%-----------------------------------------------------%
%-------------Consommation protocole BLE--------------%
%----------------Mode connecté------------------------%

% Ttemps de connexion 
D = round(time_cntd/timestep); 

while (1)   % Evènement de connexion
            % Répetition de cet évènement chaque intervalle de signalisation
    % Réveil
    % Durée du reveil  120 us
    t_wake_up = 0.12;
    m(j)= m(j-1)+round(t_wake_up/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j=j+1;
    
    % Consommation pendant le réveil = 6 mA
    for i=l:n
        rf_courant(i)= 6000 ;
    end
    
    if (n==N) % Si le temps de simulation se termine
        break ;
    end
    
    % Phase de preprocessing : 500 us
    t_preprocessing = 0.5;
    m(j) = m(j-1)+round(t_preprocessing/timestep);
    n = min (m(j),N);
    l =m(j-1);
    j=j+1;
    
    % Consommation en mode actif  
    for i=l:n
        rf_courant(i)=rf_conso_actif;
    end
    
    if (n==N) % Si le temps de simulation se termine
        break ;
    end
    
    % Phase pre tx : 120 us
    t_pre_tx = 0.1;
    m(j)=m(j-1)+round(t_pre_tx/timestep);
    n = min (m(j),N);
    l =m(j-1);
    j=j+1;
    
    % Consommation pre_rx : 10 mA
    for i = l:n
        rf_courant(i)=rf_conso_actif;
    end
    
    if (n==N)
        break ;
    end
    
    % Réception du packet du master : 350 us
    t_packet = 0.35;
    m(j)=m(j-1)+round(t_packet/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j = j+1;
    
    % Consommation mode Rx
    for i = l:n
        rf_courant(i)=rf_conso_rx;
    end
    
    if (n==N)
        break ;
    end
    
    % Transition Rx à Tx 150 us
    t_tx_to_rx = 0.15;
    m(j)=m(j-1)+round(t_tx_to_rx/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j = j+1;
    
    % Consommation mode actif 
    for i = l:n
        rf_courant(i)=rf_conso_actif;
    end
    
    if (n==N)
        break ;
    end
    
    % Réception du paquet de maintenance de la connexion 
    t_packet = 0.15 ;
    m(j)=m(j-1)+round(t_packet/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j = j+1;
    
    % Consommation Tx
    for i = l:n
        rf_courant(i)=rf_conso_tx;
    end
    if (n==N)
        break ;
    end
    
    % Phase post processing : 800 us
    t_post_processing = 0.8;
    m(j)=m(j-1)+round(t_post_processing/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j = j+1;
    
    % Consommation mode actif
    for i = l:n
        rf_courant(i)=rf_conso_actif;
    end
    
    if (n==N)
        break ;
    end
    
    % Attendre l'intervalle de connexion
    m(j)= m(j-5)+round(t_conninterval/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j=j+1;
    
    % Consommation mode PM2
    for i = l:n
        rf_courant(i)=rf_conso_sleep;
    end
    
    if (n==N)
        break ;
    end
    
    if (n>D) % Test si on a dépassé le temps de connexion définie
        break;
    end 
end

% Réception des données du processeur par UART 

t_debut = cpu_lpm3_active + capteur_su + temps_mes + adc_duree + t_traitement;

if (t_debut<time_cntd)
    % Réveil 
    a = round (t_debut/timestep);
    b = a +round (t_wake_up/timestep);
    
    % Consommation réveil
    for i=a:b
        rf_courant (i) = 6000;
    end
    
    % Module BLE en mode actif 
    t_actif = 5;
    a = b;
    b = a +round (t_actif/timestep);
    for i =a:b
        rf_courant (i) = rf_conso_actif;
    end
    
    % Passage en PM2
    a = b ;
    b = a +round(t_wake_up/timestep);
    
    % Consommation réveil
    for i = a:b
        rf_courant  (i)= 6000;
    end
    
    % Quantité de données à transmettre
    total_byte_data = (n_coupure+1)*cycle_byte_data ;
    
    while (total_byte_data)  % Tant qu'il reste des données non transmises
        % Transmission d'un paquet
        for i=b:N
            if (rf_courant(i)==rf_conso_tx)
                break;
            end
        end
        
        if (i>=N)
            break;
        else
            b=i;
        end
        
        % Calcul du temps de transmission du paquet
        if (total_byte_data > 20) % s'il reste plus d'un paquet 
            t_packet = 0.252 + 0.02 ;
            total_byte_data = total_byte_data - 20 ;
        else
            t_packet = 0.252 + total_byte_data*1e-3 ;
            total_byte_data = 0 ;
        end
        
        a = b ;
        b = a + round (t_packet/timestep);
        b = min (b,N);
        
        if (b>D) % Si on dépasse le temps de connexion autorisé
            break;
        end
        
        for i = a:b
            rf_courant  (i)= rf_conso_tx;
        end
        b=b+1;
    end
end
  
