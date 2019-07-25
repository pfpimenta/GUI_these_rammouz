%-----------------------------------------------------%
%--------Lecture de la feuille Excel "composants"-----------%


% Coordonnées du fichier Excel en question 
f = fichier_in;

% Initialisation du nombre de composants
nb_composant = [];


%-----------------------------------------------------%
%--------Lecture des paramètres des composants--------%
%-----------------------------------------------------%
% Capteur 
% Nom de la worksheet 
s = 'Composants';
a = ['c6:m6  ','c8:m9  ', 'c12:m13'];
capteur_init = [] ;
% Lecture et sauvegarde dans la matrice capteur_init
for i = 1 : 7: size (a,2)
    n = fonction_excel_read (f, s, a(i:i+6));
    capteur_init = [capteur_init;n];
end


% Nombre de modules commerciaux disponibles pour les élements du circuit
% sous la forme [capteur ADC Processeur Mémoire ModuleRF]
nb_composant = [nb_composant;size(capteur_init,2)];

%-----------------------------------------------------%
% ADC 
a = ['c20:m20','c22:m23', 'c26:m28'];
adc_init = [] ;
n = [];

% Lecture et sauvegarde dans la matrice adc_init
for i = 1 : 7: size (a,2)
    n = fonction_excel_read (f, s, a(i:i+6)); % Fonction de lecture 
    adc_init = [adc_init;n];
end

nb_composant = [nb_composant;size(adc_init,2)];

%-----------------------------------------------------%
% Processeur
a = ['c35:m38', 'c41:m50','c51:m60','c61:m61' ];
processeur_init = [] ;
n = []; 
% Lecture et sauvegarde dans la matrice processeur_init
for i = 1 : 7: size (a,2)
    n = fonction_excel_read (f, s, a(i:i+6));
    processeur_init = [processeur_init;n];
end

nb_composant = [nb_composant;size(processeur_init,2)];

[n,m] = xlsread (f,s,'a41:b50');
p_sup_processeur = [];
if (size(n,1)~=0)
    p_sup_processeur = [p_sup_processeur ; n];
end


%-----------------------------------------------------%
% Mémoire
a = ['c68:m76', 'c78:m81','c84:m89' ];
memoire_init = [] ;
n = []; 
% Lecture et sauvegarde dans la matrice memoire_init
for i = 1 : 7: size (a,2)
    n = fonction_excel_read (f, s, a(i:i+6));
    memoire_init = [memoire_init;n];
end

nb_composant = [nb_composant;size(memoire_init,2)];

%-----------------------------------------------------%
%module RF
a = ['c97:m98  ','c100:m103', 'c106:m115','c116:m119' ];
module_rf_init = [] ;
n = []; 
% Lecture et sauvegarde dans la matrice module_rf_init
for i = 1 : 9: size (a,2)
    n = fonction_excel_read (f, s, a(i:i+8));
    module_rf_init = [module_rf_init;n];
end

nb_composant = [nb_composant;size(module_rf_init,2)];

[n,m] = xlsread (f,s,'a106:b115');
p_sup_module_rf = [];
if (size(n,1)~=0)
    p_sup_module_rf = [p_sup_module_rf;n];
end


% Sauvegarde des données lues dans une libraire
save ('initialisation', 'capteur_init', 'adc_init','processeur_init', 'p_sup_processeur', 'memoire_init','module_rf_init', 'p_sup_module_rf', 'nb_composant','fichier_in','fichier_out')
clear all 