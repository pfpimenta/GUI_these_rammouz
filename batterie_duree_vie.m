%-----------------------------------------------------%
%----------------Consommation moyenne-----------------%

% Consommation totale instantannée pendant la durée de simulation 
total_courant = capteur_courant+ adc_courant+ processeur_courant+ memoire_courant+ rf_courant;

% Consommation moyenne sur la durée de simulation
moyenne_courant = mean (total_courant);

%-----------------------------------------------------%
%----------------Consommation du module RF------------%

% Consommation moyenne sur un évènement de signalisation 
moyenne_adv = ((t_adv_interval-3.45)*rf_conso_sleep + 2.1 * rf_conso_actif + 0.9 * rf_conso_tx + 0.45*rf_conso_rx)/t_adv_interval;
% Consommation moyenne sur un évènement de connexion 
moyenne_cntd=  ((t_conninterval - 2.2)*rf_conso_sleep + 1.7 * rf_conso_actif + 0.15 * rf_conso_tx + 0.35*rf_conso_rx)/t_conninterval;

% Consommation du module RF sur toute la période de mesure 
if (cnx_req>=0)  % Mode connecté 
    if (time_cntd>temps_sim)
        moyenne_courant_rf = (moyenne_cntd * (time_cntd - temps_sim) + rf_conso_sleep_2 * (T-time_cntd - temps_sim))/(T-temps_sim);
    else 
        moyenne_courant_rf = rf_conso_sleep_2;
    end
elseif (cnx_req==-1) % Mode signalisation 
     if (time_adv>temps_sim)
        moyenne_courant_rf = (moyenne_adv * (time_adv - temps_sim) + rf_conso_sleep_2 * (T-time_adv - temps_sim))/(T-temps_sim);
     else 
        moyenne_courant_rf = rf_conso_sleep_2;
     end
elseif (cnx_req==-2) % Mode PM3
    moyenne_courant_rf =rf_conso_sleep_2;
end


%-----------------------------------------------------%
%-------------Consommation moyenne du noeud-----------%
% Consommation moyenne du noeud sur la période de mesure 
moyenne_courant = [moyenne_courant * temps_sim + (total_courant(N)- rf_courant(N) + moyenne_courant_rf)*(T-temps_sim)]/T;
    