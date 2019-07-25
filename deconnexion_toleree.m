%-----------------------------------------------------%
%---------Calcul de la d�connexion tol�r�e------------%

% Fichier pour �crire la solution
load ('initialisation', 'fichier_out')
%-----------------------------------------------------%
% Limite de la consommation 
conso_desiree = capacite_batterie(1)/(autonomie)

%-----------------------------------------------------%
% Initialisation des variables de calcul
trajet = [0 5*periode_transmission(1)];
conso = 0 ;

%-----------------------------------------------------%
% Premi�re Phase de l'algorithme dichotomique
while (1)
    
    
    % Pour un noeud adoptant l'algorithme � basse consommation, le
    % changement du trajet implique un changement de la dur�e de connexion autoris�e
    if ((nb ==1)&&(synchronisation==1))
        save ('initialisation','trajet','-append')
        fonction_configuration_reseau (periode_mesure(1),periode_transmission(1)); % Calcul de la dur�e de connexion
    end
    
    % Calcul de la consommation pour ce trajet
    conso = fonction_consommation_jour ( composant, trajet, 1, periode_transmission (1), periode_mesure(1), frequence_cpu(1), puissance_rf_tx (1), adc_nb_echantillons (1));
    if (conso<conso_desiree) % Comparaison � la consommation limite pour respecter l'autonomie
        trajet (2) = trajet (2) - 5 * periode_transmission (1);
        break;
    else
        trajet (2) = trajet (2) + 5 * periode_transmission (1);
    end
end

% Deuxi�me phase de l'algorithme dichotomique
while (1)
    
    % Pour un noeud adoptant l'algorithme � basse consommation, le
    % changement du trajet implique un changement de la dur�e de connexion autoris�e   
    if ((nb ==1)&&(synchronisation==1))
        save ('initialisation','trajet','-append')
        fonction_configuration_reseau (periode_mesure(1),periode_transmission(1)); % Calcul de la dur�e de connexion
    end
    
    % Calcul de la consommation pour ce trajet
    conso = fonction_consommation_jour (composant, trajet, 1, periode_transmission(1), periode_mesure(1), frequence_cpu(1), puissance_rf_tx (1), adc_nb_echantillons (1));
    if (conso<conso_desiree) % Comparaison � la consommation limite pour respecter l'autonomie
        
        break;
    else
        trajet (2) = trajet (2) +  periode_transmission (1);
    end
end

%-----------------------------------------------------%
% D�connexion tol�r�e
coupure_toleree = trajet (2) - trajet (1);

%-----------------------------------------------------%
% Ecriture dans le fichier Excel
xlswrite('D_test.xlsx',{'Dur�e de d�connexion tol�r�e'},'Solution','a9:a9')

if (coupure_toleree>0)
    xlswrite (fichier_out,coupure_toleree,'Solution','b9:b9')
    xlswrite(fichier_out,{'minutes'},'Solution','c9:c9')
else
    coupure_toleree = 0;
    xlswrite(fichier_out,coupure_toleree,'Solution','b9:b9')
end

trajet = []
save ('initialisation','trajet','-append')

