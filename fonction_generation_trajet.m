%-----------------------------------------------------%
%-------------G�n�ration de trajet al�atoire----------%

function  trajet_minutes = fonction_generation_trajet( precision )

%-----------------------------------------------------%
%------------Lecture des entr�es de la fonction-------% 
% On d�finit la pr�cision comme �tant la dur�e minimale de coupure r�seau (exprim�e en minutes) 
N = 24 * 60 / precision ; % Nombre de cycles 

%-----------------------------------------------------%
% Initialisation des variables de calcul 
A = rand (N,1); % Vecteur al�atoire entre 0 et 1 
A = round (A); % Transformation de ce vecteur en un vecteur al�atoire de 0 (non �tablie) et 1 (�tablie) 
compteur = 1 ;
j = 1 ;
i = 1 ;

%-----------------------------------------------------%
% Etablissement du trajet � partir du vecteur A
while (i <= N)
    if ((A(i)==0)&&(compteur==1))
        trajet (j)=i;
        compteur =2;
        j = j+1 ;
    end
    if ((A(i)==1)&&(compteur==2))
        trajet (j)=i;
        compteur =1;
        j = j+1 ;
    end
    if (A(N) ==0)
        trajet (j) = N+1;
    end
    i=i+1;
end
trajet = trajet -1 ;

trajet = trajet * precision /60; % Trajet en heure 

trajet_minutes = trajet * 60; % Trajet en minutes � la sortie 

end

