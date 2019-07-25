%-----------------------------------------------------%
%---------------Dimensionnement du noeud--------------%
% Choix de composant, de sources d'énergie et de configuration électronique

% Classification des périodes de transmission par ordre décroissant 
periode_mesure = sort(periode_mesure,'descend');

% Cas d'un capteur unique connecté en permanence (mesure et transmission
% confondue)
if ((nb==1)&& (synchronisation ==1)&& (size(periode_mesure,2)>1))
    periode_transmission = periode_mesure;
end

%-----------------------------------------------------%
%Etape 1
%Choix des composants selon leur consommation en courant


% Cas d'un noeud unique adoptant l'algorithme pour la réduction
% de la consommation BLE
% Génération de la durée de connexion autorisée correspondante
if ((nb ==1)&&(synchronisation==1))
    fonction_configuration_reseau (periode_mesure(1),periode_mesure(1));
    load ('initialisation','time_cntd')
    
end

% Choix des composants constitutifs du noeud 
composant = fonction_choix_composant (nb_composant, periode_mesure(1),frequence_cpu(1),puissance_rf_tx(1),adc_nb_echantillons (1));

%-----------------------------------------------------%
% Etape 2 
% Choix d'une source d'énergie et configuration électronique 
i0 = 1 ;
while (i0<=size(capacite_batterie,2))
        
        conso_desiree = capacite_batterie(i0)/(autonomie) % consommation maximale à respecter pour la batterie en question
        
        % Marge acceptable sur la consommation désiré (en microampères)
        marge = 0.1*conso_desiree ;
        
        % Algorithme de recherche exhaustive pour les valeurs prises par
        % la configuration électronique du noeud 
        k=1;
        c(k)=0;
        for i1=1:size(periode_transmission,2)
            
            % Cas d'un noeud unique adoptant l'algorithme pour la réduction
            % de la consommation BLE
            % Il faut optimiser la valeur de la période de transmission 
            % Il faut d'abord établir les différentes possibilités 
            if ((nb ==1)&&(synchronisation ==1)&&(size(periode_mesure,2)>1))
                periode_mesure = 1: periode_transmission (i1);
                periode_mesure = periode_mesure (rem(periode_transmission(i1),periode_mesure)==0);
                periode_mesure = sort (periode_mesure,'descend');
                periode_mesure = periode_mesure (periode_mesure>=min(periode_transmission));
            end
            
            % Cas d'un noeud connecté en permanence : mesure et
            % transmission confondue
            if ((nb ==1)&&(synchronisation ==0))
                 periode_mesure = periode_transmission (i1);
             end
            
            for i2 = 1 :size (periode_mesure,2)
                
                % Cas d'un noeud unique adoptant l'algorithme pour la réduction
                % de la consommation BLE
                % Génération de la durée de connexion autorisée correspondante
                if ((nb ==1)&&(synchronisation==1))
                    fonction_configuration_reseau (periode_mesure(i2),periode_transmission(i1));
                    load ('initialisation','time_cntd')
                    
                end
                for i3=1:size(frequence_cpu,2)
                    
                    for i4=1:size(puissance_rf_tx,2)
                        
                        for i5=1:size(adc_nb_echantillons,2)
                            
                          % Calcul de la consommation pendant la durée du
                          % monitoring
                          a = fonction_consommation_optimisation (composant, trajet,n_jours, conso_desiree,marge, periode_transmission(i1), periode_mesure(i2), frequence_cpu (i3), puissance_rf_tx(i4), adc_nb_echantillons(i5)); 
                          if (a<=conso_desiree) 
                              tracker =0;
                              if ((a>=(conso_desiree-marge))) % Si la consommation appartient au domaine de solutions acceptables
                                                              % Sauvegarde des valeurs dans des vecteurs spécifiques  
                                  if (k==1)
                                      c (k) = a ; % Consommation moyenne
                                      f (k) = frequence_cpu (i3); % Fréquence CPU
                                      p (k) = periode_mesure(i2); % Période de mesure 
                                      t (k) = periode_transmission (i1); % Période de transmission 
                                      rf (k) = puissance_rf_tx (i4); % Puissance RF
                                      adc (k) = adc_nb_echantillons (i5); % Fréquence d'échantillonnage
                                  else
                                      if (abs(a-c(k-1))<1e-3) % Deux solutions ayant la même consommation, on conserve la plus performante
                                          k=k-1;
                                          c(k)=a ;
                                          f (k) = frequence_cpu (i3);
                                          p (k) = periode_mesure(i2);
                                          t (k) = periode_transmission (i1);
                                          rf (k) = puissance_rf_tx (i4);
                                          adc (k) = adc_nb_echantillons (i5);

                                      else
                                          c (k) = a ; 
                                          f (k) = frequence_cpu (i3);
                                          p (k) = periode_mesure(i2);
                                          t (k) = periode_transmission (i1);
                                          rf (k) = puissance_rf_tx (i4);
                                          adc (k) = adc_nb_echantillons (i5);

                                      end
                                  end

                                  k=k+1;
                              end
                          else
                              tracker = 1; % Suivi du critère d'arrêt
                            break;
                          end
                          
                        end

                        if ((i5==1)&&(tracker==1))
                            break; % arrêt de la recherche sans parcourir les autres valeurs
                        end
                        
                        
                    end

                    if ((i4==1)&&(tracker==1))
                            break; % arrêt de la recherche sans parcourir les autres valeurs
                    end
                end

                    if ((i3==1)&&(tracker==1))
                            break; % arrêt de la recherche sans parcourir les autres valeurs
                    end
                    
            end

                    if ((i2==1)&&(tracker==1))
                            break; % arrêt de la recherche sans parcourir les autres valeurs
                    end
        end
          

            if ((i1==1)&&(i2==1)&&(i3==1)&&(i4==1))
                i0 = i0+1; % si pas de solutions, on augmente la capacité de la batterie 

            else
                
                break;
            end
            
end
    
%-----------------------------------------------------%
% Si pas de solutions selon les critères données
if (k==1)
    if (i0== (size(capacite_batterie,2)+1))
         display ('Pas de solutions. Il faut augmenter la capacité de la batterie.')
    else
         display ('Pas de solutions. Il faut augmenter la marge.')
    end
    break;
end

%-----------------------------------------------------%
% Etape 3 
% Filtrer les solutions si elle sont nombreuses 
 delta_c = conso_desiree - c ; % Ecart de consommation 
 N = size (delta_c,2) ;  % Nombre de solutions 
 filtrage_solution ; % Filtrage de ces solutions si elles sont nombreuses

%-----------------------------------------------------%
% Etape 4
% Afficher la courbe d'optimiation
courbe_optimisation ; 

% sauvegarder les valeurs dans un vecteur 
save ('opti_output2','i1','delta_c','p','t','f','rf' ,'adc')

%-----------------------------------------------------%
% Etape 5
% Filtrer les solutions selon les préférences de l'utilisateur 
filtrage_preferences ; 