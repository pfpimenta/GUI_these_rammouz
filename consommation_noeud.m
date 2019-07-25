%-----------------------------------------------------%
%--------Consommation noeud sur un cycle--------------%
% Script pour visualiser et tester les courbes de consommation

clear all 
clc 
load ('initialisation', 'capteur_init', 'adc_init','processeur_init', 'p_sup_processeur', 'memoire_init','module_rf_init', 'p_sup_module_rf','taille_data','time_cntd') 

%-----------------------------------------------------%
%-------------Initialisation des variables------------%  

taille_data = 2; % Taille des données 

time_cntd = 1.5e3; % Temps de connexion autorisé

composant = [1 1 1 1 1]; % Vecteurs des composants sous la forme [ capteur adc processeur memoire moduleRF]

cnx_req = 1;  % Etat de la connexion à la station de base : 
              %             -2 pas de transmission
              %             -1 mode signalisation
              %             0 établissement de la connexion
              %             1 mode connecté

n_coupure = 0; % Nombre de mesures à transmettre 

ecriture_par_cycle =0; % Strategie de sauvegarde de données :
                       % 0 : Ecriture si transmission échouée
                       % 1 : Ecriture de toute l'information 

block_erase =0; % Effacement de la mémoire si = 1

minutes = 1; % Intervalle de mesure en minutes

cpu_f = 8; % Fréquence CPU en MHz

nb_ech = 10; % Fréquence d'échantillonnage en Hz

rf_puissance = 15; % Puissance RF

taille_data = 2; % Taille des données 

time_cntd = 1.5e3; % Temps de connexion autorisé


%-----------------------------------------------------%
%-----Initialisation des paramètres de simulation-----% 

initialisation; % Initialisation des entrées de simulation 

temps = (0:1e-2:temps_sim); % Définition de l'axe de temps 
N=size(temps,2);
timestep = temps (2)-temps(1); % Définition du pas pour parcourir l'axe de temps

%-----------------------------------------------------%
%------------Simulation de la Consommation------------% 
% Etablissement des consommations instantannées des composants 
capteur_consommation ;
adc_consommation ; 
memoire_consommation;
processeur_consommation;
RF_consommation; 

% Calcul de la consommation moyenne sur la période de mesure
batterie_duree_vie;

% Tracé les courbes de consommation 
courbe_de_consommation;

