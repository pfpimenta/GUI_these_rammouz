%-----------------------------------------------------%
%-------------Consommation protocole BLE--------------%

%-----------------------------------------------------%
%-------Initialisation des variables de calcul--------% 
m = [];
j=1;
m(j)=1;
j=j+1;

%-----------------------------------------------------%
%----------Simulation de la consommation--------------%
%-----------------Fonction transmission---------------%

% Mise de la consommation en mode dormant 
for i = 1 :N
        rf_courant (i) =  rf_conso_sleep_2;
end

% Test sur le mode de fonctionnement : signalisation, connecté, etc.

if (cnx_req == -1)  % Mode signalisation 
    C = N+1;
    RF_BLE_advertising;
    
elseif (cnx_req==0) % Etablissement de la connexion 
    RF_BLE_connecting ;
    
elseif (cnx_req ==1) % Mode connecté
    RF_BLE_connected ;
end 

