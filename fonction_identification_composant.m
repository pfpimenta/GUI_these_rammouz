%-----------------------------------------------------%
%-----------Identifiation d'un module-----------------%
% Lorsqu'un module commercial est appel� dans la feuille "Probl�me", cette fonction 
% permet de l'identifier et de lui faire correspondre ses caract�ristiques 

function id = fonction_identification_composant( composant, file, sheet, range)

a = cell2mat(composant); 

if (isnan(a))  % Pas de modules choisis
    id = 0;
else
    if (isnumeric(a))     % Si valeur num�rique
        a = mat2str (a);  % Transformer en texte 
    end
    
    [n,m,r] = xlsread (file,sheet,range);
    
    for i=1:size(r,2)
        c = cell2mat (r(i));
        if (isnumeric(c))
            c = mat2str(c);
        end
        if (strcmp (c,a))
            break;
        end
    end
    id = i; % Identificateur permettant de rep�rer les caract�ristiques du composant
    
    
end
end

