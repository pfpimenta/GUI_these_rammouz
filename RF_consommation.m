%-----------------------------------------------------%
%----------------Consommation module RF---------------%
% "rf_courant" est la consommation instantann�e en fonction de "temps"


switch option % Test pour d�terminer le protocle de communication adopt� 
    case 1 % protocole BLE
        RF_BLE; % Lancement du code pour la simulation de la consommation du module
    
end