%-----------------------------------------------------%
%--------Interface Utilisateur dans Matlab------------%

%-----------------------------------------------------%
% Effacer la fenêtre de commande
clc
% Effacer les variables 
clear all

%-----------------------------------------------------%
fprintf ('Bonjour\n')
% Affichage 
a= input ('Choisir parmi les options suivantes :\n1: Créer un projet\n2: Ouvrir un projet\n');
% Nouveau projet ou un existant 
if (a==1)
    b = input ('Un fichier Template sera ouvert.\nRemplir la fiche Composants par les informations relatives aux composants.\nRemplir la fiche Problème par le problème de conception à résoudre.\nSaisir Entrer pour procéder')
    if (size (b,1)==0)
        winopen ('Data_input.xlsx')
    end
    fprintf ('Une fois les données remplies, Sauvegarder le fichier sous un autre nom, ce nom constituera le nom du projet créé.\n')
    f = input ('Saisir le nom du fichier.\n','s');
    g = input ('Saisir Entrer pour lancer la simulation.\n');
else 
    b = [];
    fprintf ('Choisir le projet à ouvrir parmi:')
    d = dir('*.xlsx'); % Affichage des fichiers Excel existant (les projets) 
    % Faire corresponde à chaque fichier un numéro permettant à
    % l'utilisateur de le choisir 
    for i=size(d,2)
        c = d(i).name;
        c = c(1:end-5);
        if (strcmp(c,'Data_input')==0)
            b = [b,i]; 
            fprintf ('\n1:%s',c)
        else
            b = [b,0];
        end
    end
    e = input('\n');
    e = find (b==e); % Identification du fichier selon la saisie de l'utilisateur 
    f = d(e).name ;
    f = f (1:end-5);
    
    fprintf ('Désirez-vous effectuer des changements au niveau de l''initialisation des composants ou du problème?\nRépondez par oui ou non')
    % Oui ou Non, toute autre saisie n'est pas acceptable
    c = input ('\n','s');
    erreur = 1;
    while (erreur)
        if (strcmp(c,'oui'))
            winopen (d(e).name)
            erreur = 0;
            g = input ('Une fois la saisie terminée, sauvegarder et fermer le fichier.\nSaisir Entrer pour lancer la simulation.\n');
        elseif (strcmp(c,'non'))
            erreur = 0;
            g = input ('Saisir Entrer pour lancer la simulation.\n');
        else 
            c = input ('Saisir oui ou non pour répondre à la question.\n','s') ;
        end
    end
    
    f1 = strcat(f,'.xlsx');
    % Effacer la solution si l'on manipule un fichier existant
    delete_excel;
end

% Initialisation des noms des fichiers
fichier_in = f;
fichier_out = strcat(f,'.xlsx');
clear ('a','b','c','d','e','erreur','f','f1','g','i','ligne')

% Lecture des entrées à partir du fichier Excel 
Excel_init;
probleme_init;

% Lancement de la simulation
if (nb>1)
    fonction_configuration_reseau (periode_mesure, periode_transmission);
    load initialisation
    time_cntd;
    periode_mesure;
    periode_transmission;
end


logiciel;
display ('Simulation terminée. Ouverture du fichier')
winopen (fichier_out)

