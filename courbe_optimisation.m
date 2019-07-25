%-----------------------------------------------------%
%--------------Courbe d'optimisation------------------%

% Afficher la courbe de d'optimisation (comment on s'approche de la
% solution optimale

% Effacer les figures provenant d'un traitement antérieur
clf; 

% Tracé de la figure 
i1 = (1:1:size(delta_c,2));
plot (i1,delta_c)
xlabel ('Itération');
ylabel ('Ecart de consommation');

