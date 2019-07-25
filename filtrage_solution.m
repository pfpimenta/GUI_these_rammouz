%---------------------------------------------------------------------%
%---------Filtrage des solutions de configurations �lectronique-------%
% Si le nombre de solutions obtenu est superieur � 10
% On r�tressit l'intervalle de consommation acceptable

N = size (i1,2); % Nombre de solutions 

while (N>10) % Tant que les solutions sont plus nombreuses que 10
    marge_reduite = (max(delta_c)-min(delta_c))/2; % R�duire l'intervalle de consommation (la marge) 
    
    x = find (delta_c>marge_reduite); % Filtrer les solutions 
    
    delta_c (x) = []; 
    p(x) = [];
    t(x) =[];
    f(x) = [];
    rf(x) = [];
    adc(x) = [];
    
    N = size (delta_c,2); % Nombre de solutions apr�s filtrage 
    
end

