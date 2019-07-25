%-----------------------------------------------------%
%----------------Consommation module RF---------------%
% "rf_courant" est la consommation instantannée en fonction de "temps"


switch option % Test pour déterminer le protocle de communication adopté 
    case 1 % protocole BLE
        RF_BLE; % Lancement du code pour la simulation de la consommation du module
    
end