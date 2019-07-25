%-----------------------------------------------------%
%-------------Consommation protocole BLE--------------%
%----------------Mode signalisation-------------------%

% Temps de signalisation 
D =  round(time_adv/timestep); 

while (1) % Signalisation sur trois canaux dans un évènement de signalisation 
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
    
    %Phase de preprocessing : 500 us
    t_preprocessing = 0.5;
    m(j) = m(j-1)+round(t_preprocessing/timestep);
    n = min (m(j),N);
    l =m(j-1);
    j=j+1;
    
    % Consommation en mode actif  
    for i=l:n
        rf_courant(i)=rf_conso_actif;
    end
    
    if (n==N)
        break ;
    end
    
    % Phase pre tx : 120 us
    t_pre_tx = 0.12;
    m(j)=m(j-1)+round(t_pre_tx/timestep);
    n = min (m(j),N);
    l =m(j-1);
    j=j+1;
    
    % Consommation pre_tx : 10 mA
    for i = l:n
        rf_courant(i)=10000;
    end
    
    if (n==N)
        break ;
    end
    
    % Evènement de signalisation 
    for adv_channel=1:3 % pour chaque canal de signalisation 
        % Transmission d'un paquet de signalisation : 300 us 
        t_tx_adv = 0.3;
        m(j)=m(j-1)+round(t_tx_adv/timestep);
        n = min (m(j),N);
        l = m(j-1);
        j = j+1;
        
        % Consommation mode Tx
        for i = l:n
            rf_courant(i)=rf_conso_tx;
        end
        
        if ((n==N)||(n>C))
            break ;
        end
        
        % Transition entre Tx et Rx 150 us
        t_tx_to_rx = 0.15;
        m(j)=m(j-1)+t_tx_to_rx/timestep;
        n = min (m(j),N);
        l = m(j-1);
        j = j+1;
        
        % Consommation pendant cette transition  
        for i = l:n
            rf_courant(i)=rf_conso_actif;
        end
        
        if (n==N)
            break ;
        end
        
       % Ecoute sur le canal : 115 us
        t_rx_adv = 0.15;
        m(j)=m(j-1)+round(t_rx_adv/timestep);
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
        
        if (adv_channel<3)
            % Attente inter-canal : 150 us
            t_inter_channel = 0.15;
            m(j)=m(j-1)+round(t_inter_channel/timestep);
            n = min (m(j),N);
            l = m(j-1);
            j = j+1;
            
            % Consommation i%consommation inter canal : mode actif
            for i = l:n
                rf_courant(i)= rf_conso_actif;
            end
        end
        
        if (n==N)
            break ;
        end
    end
    
    if (n>C) % Test si la connexion s'est établie
        break;
    end 
    
    % Phase post processing : 800 us
    t_post_processing = 0.8;
    m(j)=m(j-1)+round(t_post_processing/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j = j+1;
    
    % Consommation post processing : mode actif 
    for i = l:n
        rf_courant(i)=rf_conso_actif;
    end
    
    if (n==N)
        break ;
    end
    
    
    % Mode PM2 pendant l'intervalle de signalisation 
    m(j)=m(j-13)+round(t_adv_interval/timestep);
    n = min (m(j),N);
    l = m(j-1);
    j = j+1;
    
    % Consommation mode PM2
    for i = l:n
        rf_courant(i)=rf_conso_sleep;
    end
    if (n==N)
        break ;
    end
    if (n>D) % Test si on a dépassé le temps de signalisation définie
        break; 
    end
end
