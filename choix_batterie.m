%-----------------------------------------------------%
%-------------Choix d'un source d'�nergie-------------%

% Calcul de la consommation du noeud tout au long du monitoring
c = 0; % R�sultat de recherche : 0 -> source d'�nergie convenable non trouv�e
       %                         1 -> source d'�nergie convenable non trouv�e
conso = fonction_consommation_jour (nb_composant, trajet,n_jours,periode_transmission (1), periode_mesure(1), frequence_cpu (1), puissance_rf_tx(1), adc_nb_echantillons(1));

%-----------------------------------------------------%
% Parcourir les diff�rentes batteries par ordre croissant de capacit�s
% Calcul de l'autonomie assur�e par chacune
% Arr�t lorsque l'autonomie d�sir�e est atteinte

for i = 1 : size (capacite_batterie,2)    
    duree_de_vie = capacite_batterie(i)/(conso); % Calcul de l'autonomie
    if (duree_de_vie>autonomie)
        c=1; % R�sultat de recherche positif
        break
    end
end

%-----------------------------------------------------%
if (c==1) % R�sultat de recherche positif
    capacite_batterie(i)
    % Ecriture dans le fichier Excel
    xlswrite('D_test.xlsx',{'Source d''�nergie'},'Solution','a9:a9')
    xlswrite ('D_test.xlsx',capacite_batterie(i),'Solution','b9:b9')
    xlswrite('D_test.xlsx',{'�Ah'},'Solution','c9:c9')
else % R�sultat de recherche n�gatif
    xlswrite ('D_test.xlsx',{'Pas de batteries convenable'},'Solution','b9:b9')
end