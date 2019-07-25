%-----------------------------------------------------%
%---------Consommation noeud sur un cycle-------------%
% Fonction utilisée pour le calcul de la consommation sur un cycle

function moyenne_courant = fonction_consommation_noeud(e0,e1,e2,e3,e4,e5,e6,e7,e8 )

load ('initialisation', 'capteur_init', 'adc_init','processeur_init', 'p_sup_processeur', 'memoire_init','module_rf_init', 'p_sup_module_rf','taille_data','time_cntd') 

%-----------------------------------------------------%
%------------Lecture des entrées de la fonction-------% 

composant = e0; % Vecteurs des composants sous la forme [ capteur adc processeur memoire moduleRF]

cnx_req = e1; % Etat de la connexion à la station de base : 
              %             -2 pas de transmission
              %             -1 mode signalisation
              %             0 établissement de la connexion
              %             1 mode connecté
              
n_coupure = e2 ; % Nombre de mesures à transmettre

ecriture_par_cycle =e3; % Strategie de sauvegarde de données :
                       % 0 : Ecriture si transmission échouée
                       % 1 : Ecriture de toute l'information
                       
block_erase =e4; % Effacement de la mémoire si = 1

minutes = e5; % Intervalle de mesure en minutes

cpu_f = e6 ; % Fréquence CPU en MHz

rf_puissance = e7; % Puissance RF

nb_ech = e8; % Fréquence d'échantillonnage en Hz


%-----------------------------------------------------%
%-----Initialisation des paramètres de simulation-----% 

initialisation; % Initialisation des entrées de simulation

temps = (0:1e-3:temps_sim); % Définition de l'axe de temps 
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


end

