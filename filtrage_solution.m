%---------------------------------------------------------------------%
%---------Filtrage des solutions de configurations électronique-------%
% Si le nombre de solutions obtenu est superieur à 10
% On rétressit l'intervalle de consommation acceptable

N = size (i1,2); % Nombre de solutions 

while (N>10) % Tant que les solutions sont plus nombreuses que 10
    marge_reduite = (max(delta_c)-min(delta_c))/2; % Réduire l'intervalle de consommation (la marge) 
    
    x = find (delta_c>marge_reduite); % Filtrer les solutions 
    
    delta_c (x) = []; 
    p(x) = [];
    t(x) =[];
    f(x) = [];
    rf(x) = [];
    adc(x) = [];
    
    N = size (delta_c,2); % Nombre de solutions après filtrage 
    
end

