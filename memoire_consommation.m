%-----------------------------------------------------%
%----------------Consommation m�moire-----------------%
% "memoire_courant" est la consommation instantann�e en fonction de "temps"

% Initialisation de la consommation de la m�moire � sa valeur en mode
% dormant
% Elle sera modifi�e lors de l'appel des fonction de lecture, �criture,
% effacement
for i=1:N 
    memoire_courant(i) = memoire_conso_shut_down;
end