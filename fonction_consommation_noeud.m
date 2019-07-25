%-----------------------------------------------------%
%---------Consommation noeud sur un cycle-------------%
% Fonction utilis�e pour le calcul de la consommation sur un cycle

function moyenne_courant = fonction_consommation_noeud(e0,e1,e2,e3,e4,e5,e6,e7,e8 )

load ('initialisation', 'capteur_init', 'adc_init','processeur_init', 'p_sup_processeur', 'memoire_init','module_rf_init', 'p_sup_module_rf','taille_data','time_cntd') 

%-----------------------------------------------------%
%------------Lecture des entr�es de la fonction-------% 

composant = e0; % Vecteurs des composants sous la forme [ capteur adc processeur memoire moduleRF]

cnx_req = e1; % Etat de la connexion � la station de base : 
              %             -2 pas de transmission
              %             -1 mode signalisation
              %             0 �tablissement de la connexion
              %             1 mode connect�
              
n_coupure = e2 ; % Nombre de mesures � transmettre

ecriture_par_cycle =e3; % Strategie de sauvegarde de donn�es :
                       % 0 : Ecriture si transmission �chou�e
                       % 1 : Ecriture de toute l'information
                       
block_erase =e4; % Effacement de la m�moire si = 1

minutes = e5; % Intervalle de mesure en minutes

cpu_f = e6 ; % Fr�quence CPU en MHz

rf_puissance = e7; % Puissance RF

nb_ech = e8; % Fr�quence d'�chantillonnage en Hz


%-----------------------------------------------------%
%-----Initialisation des param�tres de simulation-----% 

initialisation; % Initialisation des entr�es de simulation

temps = (0:1e-3:temps_sim); % D�finition de l'axe de temps 
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


end

