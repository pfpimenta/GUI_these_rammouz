%-----------------------------------------------------%
%--------Consommation noeud sur un cycle--------------%
% Script pour visualiser et tester les courbes de consommation

clear all 
clc 
load ('initialisation', 'capteur_init', 'adc_init','processeur_init', 'p_sup_processeur', 'memoire_init','module_rf_init', 'p_sup_module_rf','taille_data','time_cntd') 

%-----------------------------------------------------%
%-------------Initialisation des variables------------%  

taille_data = 2; % Taille des donn�es 

time_cntd = 1.5e3; % Temps de connexion autoris�

composant = [1 1 1 1 1]; % Vecteurs des composants sous la forme [ capteur adc processeur memoire moduleRF]

cnx_req = 1;  % Etat de la connexion � la station de base : 
              %             -2 pas de transmission
              %             -1 mode signalisation
              %             0 �tablissement de la connexion
              %             1 mode connect�

n_coupure = 0; % Nombre de mesures � transmettre 

ecriture_par_cycle =0; % Strategie de sauvegarde de donn�es :
                       % 0 : Ecriture si transmission �chou�e
                       % 1 : Ecriture de toute l'information 

block_erase =0; % Effacement de la m�moire si = 1

minutes = 1; % Intervalle de mesure en minutes

cpu_f = 8; % Fr�quence CPU en MHz

nb_ech = 10; % Fr�quence d'�chantillonnage en Hz

rf_puissance = 15; % Puissance RF

taille_data = 2; % Taille des donn�es 

time_cntd = 1.5e3; % Temps de connexion autoris�


%-----------------------------------------------------%
%-----Initialisation des param�tres de simulation-----% 

initialisation; % Initialisation des entr�es de simulation 

temps = (0:1e-2:temps_sim); % D�finition de l'axe de temps 
N=size(temps,2);
timestep = temps (2)-temps(1); % D�finition du pas pour parcourir l'axe de temps

%-----------------------------------------------------%
%------------Simulation de la Consommation------------% 
% Etablissement des consommations instantann�es des composants 
capteur_consommation ;
adc_consommation ; 
memoire_consommation;
processeur_consommation;
RF_consommation; 

% Calcul de la consommation moyenne sur la p�riode de mesure
batterie_duree_vie;

% Trac� les courbes de consommation 
courbe_de_consommation;

