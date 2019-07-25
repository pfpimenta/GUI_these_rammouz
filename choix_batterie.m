%-----------------------------------------------------%
%-------------Choix d'un source d'énergie-------------%

% Calcul de la consommation du noeud tout au long du monitoring
c = 0; % Résultat de recherche : 0 -> source d'énergie convenable non trouvée
       %                         1 -> source d'énergie convenable non trouvée
conso = fonction_consommation_jour (nb_composant, trajet,n_jours,periode_transmission (1), periode_mesure(1), frequence_cpu (1), puissance_rf_tx(1), adc_nb_echantillons(1));

%-----------------------------------------------------%
% Parcourir les différentes batteries par ordre croissant de capacités
% Calcul de l'autonomie assurée par chacune
% Arrêt lorsque l'autonomie désirée est atteinte

for i = 1 : size (capacite_batterie,2)    
    duree_de_vie = capacite_batterie(i)/(conso); % Calcul de l'autonomie
    if (duree_de_vie>autonomie)
        c=1; % Résultat de recherche positif
        break
    end
end

%-----------------------------------------------------%
if (c==1) % Résultat de recherche positif
    capacite_batterie(i)
    % Ecriture dans le fichier Excel
    xlswrite('D_test.xlsx',{'Source d''énergie'},'Solution','a9:a9')
    xlswrite ('D_test.xlsx',capacite_batterie(i),'Solution','b9:b9')
    xlswrite('D_test.xlsx',{'µAh'},'Solution','c9:c9')
else % Résultat de recherche négatif
    xlswrite ('D_test.xlsx',{'Pas de batteries convenable'},'Solution','b9:b9')
end