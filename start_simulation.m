%---------------------------------------------------------------%
%-------- Start simulation from simulation_params.m ------------%
%---------------------------------------------------------------%
% To be used with the GUI_these_rammouz graphical user interface
% (July 2019, Pedro FOLETTO PIMENTA)
%---------------------------------------------------------------%

clc % Effacer les textes affiches dans la fen�tre de commande
clear all % Effacer les variables

disp("Starting simulation with the parameters from simulation_params.m")

% load parameters from a .mat file
% load('C:\Users\pimenta\Desktop\Codes_these_Ramzy\Code Matlab\simulation_params.mat') %TODO
load simulation_params
% load initialisation

if (strcmp (routine, 'Non connu')) % Trajet non connu, � optimiser 
    trajet = [];
elseif (strcmp (routine, 'Al�atoire')) % Trajet al�atoire, � g�n�rer avec la fonction Matlab 
    trajet = fonction_generation_trajet( 30 );
else    % predefini, a lire, et a convertir en minutes
    % TODO
    trajet = []; % A CHANGER !
%     [n,m] = xlsread (f, s, 'b42:e45');
%     trajet = [];
%     for i =1:size (n,2)
%         trajet = [trajet, n(i,1),n(i,3)];
%     end
%     trajet = trajet *1440;
end


% correct missing parameters
fichier_out = 'Data_input.xlsx';% TEMPORAIRE
memoire_init = memoire_init.'; % change columns for rows

% demarrer simulation
logiciel;

% save results in a .mat file
% save ('results','duree_de_connexion','consommation') % TODO
