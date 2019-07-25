%-----------------------------------------------------%
%-------Lecture d'une donnée d'un fichier Excel-------%
% Lecture de la donnée et conversion de l'unité vers les unités adoptés en
% simulation

function result = fonction_excel_read (file, sheet, range )
[n,m] = xlsread (file, sheet, range); % Instruction Matlab pour la lecture à partir du fichier Excel
nb_modules = size (n,2);

% Conversion d'unité 
for i = 1:size (n,1)
    
    for j=1:size (n,2)
        
        if (strcmp (m(i), 's')) % Analyse de l'unité introduite par l'utilisateur
            n(i,j) = n(i,j)*1000; % Conversion de la valeur du paramètre vers l'unité convenable
        end
        if (strcmp (m(i), 'µs'))
            n(i,j) = n(i,j)*1e-3;
        end
        if (strcmp (m(i), 'mA'))
            n(i,j) = n(i,j)*1e3;
        end 
        if (strcmp (m(i), 'A'))
            n(i,j) = n(i,j)*1e6;
        end 
        if (strcmp (m(i), 'ko'))
            n(i,j) = n(i,j)*1e3;
        end 
         if (strcmp (m(i), 'Mo'))
            n(i,j) = n(i,j)*1e6;
         end 
        if (strcmp (sheet, 'Composants') )
            if (strcmp (m(i), 'kHz'))
                n(i,j) = n(i,j)*1e-3;
            end
            if (strcmp (m(i), 'Hz'))
                n(i,j) = n(i,j)*1e-6;
            end
        end 
    end 
end 
result = n ; % Retour du paramètre
end


