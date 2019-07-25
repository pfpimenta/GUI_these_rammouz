%-----------------------------------------------------%
%----------------Consommation mémoire-----------------%
% "memoire_courant" est la consommation instantannée en fonction de "temps"

% Initialisation de la consommation de la mémoire à sa valeur en mode
% dormant
% Elle sera modifiée lors de l'appel des fonction de lecture, écriture,
% effacement
for i=1:N 
    memoire_courant(i) = memoire_conso_shut_down;
end