%-----------------------------------------------------%
%-------------Consommation protocole BLE--------------%
%----------Etablissement de la connexion--------------%


% Temps d'établissement de la connexion
C = round(time_cnting/timestep);

% Mode signalisation jusqu'à l'établissement de la connexion
RF_BLE_advertising;

% Transition du mode Tx au mode Rx
t_tx_to_rx = 0.15;
m(j)=m(j-1)+t_tx_to_rx/timestep;
n = min (m(j),N);
l = m(j-1);
j = j+1;
%consommation tx_to_rx
for i = l:n
    rf_courant(i)=rf_conso_actif;
end

% Reception de la requête de connexion : 300 us
t_rx_cnx_req = 0.3;
m(j)=m(j-1)+round(t_rx_cnx_req/timestep);
n = m(j);
l = m(j-1);
j = j+1;
% Consommation mode Rx
for i = l:n
    rf_courant(i)=rf_conso_rx;
end

% Phase post processing time : us
t_post_processing = 0.8;
m(j)=m(j-1)+round(t_post_processing/timestep);
n = min (m(j),N);
l = m(j-1);
j = j+1;

% Consommation post processing : mode actif
for i = l:n
    rf_courant(i)=rf_conso_actif;
end


% Attente d'un interval de temps
% 1.25 ms <t< windowsize + windowoffset
% Exemple 10 ms
t_wait_con = 10;
m(j)=m(j-1)+round(t_wait_con/timestep);
n = m(j);
l = m(j-1);
j = j+1;
%consommation PM2
for i = l:n
    rf_courant(i)=rf_conso_sleep;
end

% Passage en mode connecté
RF_BLE_connected ;


 
