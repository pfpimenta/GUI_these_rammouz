%-----------------------------------------------------%
%----------------Configuration du r�seau--------------%
% R�partition des intervalles de temps sur les noeuds de capteurs

function fonction_configuration_reseau(periode_mesure,periode_transmission )

% Param�tres de la connexion BLE
load ('initialisation','module_rf_init','taille_data','trajet','nb','data_max','noeud','fichier_out')
connection_interval = module_rf_init (1, 1) ;
clear module_rf_init

% Intervalle de r�ception de chaque paquet
reception_paquet = 2*connection_interval;

%-----------------------------------------------------%
% Calcul du PGCD des temps de transmission - unit� de base
unite_base = periode_transmission (1);
for k = 2:length(periode_transmission)
    unite_base = gcd (unite_base,periode_transmission(k));
end
unite_base = unite_base *60 * 1e3;

% Calcul de la quantit� maximale de donn�es produites
for i=1:nb
    taille_max (i) = calcul_taille_max (trajet, periode_transmission (i), periode_mesure (i), taille_data(i));
    cntd_time (i) = taille_max (i)*reception_paquet/20 ; % Dur�e n�cessaire pour la transmission de ces donn�es
end

% On suppose 2 secondes pour l'�tablissement de la connexion BLE
% Calcul des intervalles de temps de chaque noeud
cntd_time = 2000 + cntd_time;
somme = sum (cntd_time);
cntd_time = cntd_time - 2000;

%-----------------------------------------------------%
% D�but de l'algorithme dichotomique
diviseur = 2; % Compteur d'unit� de base

% Cas d'un noeud unique
if ((somme<unite_base)&&(nb==1)) % Test si la somme des intervalles de temps est inf�rieure � l'unit� de base
    time_cntd = cntd_time +2000;
    
end

while (somme > unite_base) % Tant que la somme des intervalles de temps est sup�rieure � l'unit�de base,
    % on r�partit la transmission sur une unit� de base suppl�mentaire
    
    cntd_time_2=cntd_time/diviseur;
    cntd_time_3 = ceil (cntd_time_2/reception_paquet)*reception_paquet;
    somme = sum (cntd_time_3+2000);
    if (somme > unite_base) % Si la somme est sup�rieure � l'unit� de base
        diviseur = diviseur+1; % on r�partit la transmission sur une unit� de base suppl�mentaire
    end
end

% Cas d'un noeud unique
if ((somme<unite_base)&&(nb==1))
    if (time_cntd>unite_base)
        time_cntd = cntd_time_3 +2000;
       
    end
end

% Cas d'un r�seau de plusieurs noeuds
if (nb>1)
    % Deuxi�me partie de l'algorithme dichotomique : augmenter le temps de
    % connexion attribu� � chaque noeud progressivement en vue de r�duire les d�lais de
    % transmission tout en respectant l'unit� de base
    while (diviseur >1)
        for i = 1 :nb
            if (cntd_time_3(i)>= cntd_time (i))
                cntd_time_3(i) = ceil (cntd_time (i)/reception_paquet)*reception_paquet;
            else
                a = cntd_time_2 (i);
                a = a * diviseur/(diviseur-1) ;
                a = ceil (a/reception_paquet)*reception_paquet;
                cntd_time_3 (i) = a ;
                somme = sum (cntd_time_3);
                if (somme > unite_base)
                    cntd_time_3(i)= ceil (cntd_time_2(i)/reception_paquet)*reception_paquet;
                end
            end
        end
        diviseur = diviseur-1;
    end
    delai_transmission = ceil (cntd_time ./ cntd_time_3);
    cntd_time_3;
  
    %-----------------------------------------------------%    
    % Ecriture de la configuration du r�seau dans le fichier Excel
    xlswrite(fichier_out,(cntd_time_3+2000)/1000,'Solution','b6:f6')
    xlswrite(fichier_out,delai_transmission,'Solution','b7:f7')
    
    %-----------------------------------------------------%
    % Configuration du noeud d'int�r�t (� optimiser)
    % Intervalle de temps attribu�
    time_cntd = cntd_time_3 (noeud)+2000;
    % Taille maximale pouvant �tre transmise  dans l'intervalle de temps attribu�
    data_max = (time_cntd-2000) * 20 / (reception_paquet*taille_data(noeud)) -1;
    % Codage de l'information
    taille_data = taille_data(noeud);
    % Intervalle de mesure
    periode_mesure = periode_mesure (noeud);
    % Intervalle de transmission
    periode_transmission = periode_transmission (noeud);
end    


%-----------------------------------------------------%
% Sauvegarde de l'information
save ('initialisation','periode_mesure', 'periode_transmission','taille_data','data_max','time_cntd','-append')

end

