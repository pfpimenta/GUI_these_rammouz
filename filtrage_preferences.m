%--------------------------------------------------------%
%--Filtrage des solutions de configuration �lectronique---%
% Filtrer les solutions de l'optimisation en fonction des pr�f�rences utilisateurs  

load opti_output2 
% Initialisation des cases pour �crire dans le fichier Excel
ligne = ['a9:f9  ','a10:f10','a11:f11','a12:f12','a13:f13','a14:f14','a15:f15','a16:f16','a17:f17','a18:f18','a19:f19','a20:f20','a21:f21','a22:f22'];

% Appel des pr�f�rences utilisateur (sauvegard�s dans deux vecteurs ub - upper bound et lb - lower bound )
% Selon la forme [fr�quence_mesure fr�quence_cpu puissance_rf fr�quence_adc]
load ('initialisation', 'ub','lb','fichier_out')
ub ([4 5])= ub ([5 4]);
lb ([4 5])= lb ([5 4]);


%--------------------------------------------------------%
% Filtrage des valeurs pour chaque param�tre  : 
% Pour chaque param�tre, on rel�ve l'indice de la solution qui est conforme
% aux pr�f�rences utilisateurs 
% L'intersection de ces solutions forme l'ensemble des solutions conformes
% aux pr�f�rences utilisateurs

% Fr�quence de transmission 
x1 = find (t>= lb(1));
x2 = find (t<= ub(1));
x = intersect(x1,x2);

% Fr�quencede de mesure
y1 = find (p>=lb(2));
y2 = find (p<=ub(2));
y = intersect (y1,y2);

% Fr�quence CPU
z1 = find (f>=lb(3));
z2 = find (f <=ub(3));
z = intersect (z1,z2);

% Puissance RF
v1 = find (rf >=lb(4));
v2 = find (rf <= ub(4));
v = intersect (v1,v2);

% Fr�quence d'�chantillonnage
w1 = find (adc >=lb(5));
w2 = find (adc <= ub(5));
w = intersect (w1,w2);

% Intersection de toutes les solutions 
x = intersect (x,y);
x = intersect (x,w);
z = intersect (z,v);
x = intersect (x,z);
c_ligne = 1; % Compteur de lignes dans Excel

% Ecriture de la solution dans le fichier Excel 
xlswrite(fichier_out,{'','P�riode de mesure (min)','P�riode de transmission (min)','Fr�quence de traitement (MHz)','Puissance de transmission','Fr�quence d''�chantillonnage (Hz)'},'Solution',ligne(c_ligne:c_ligne+6))
c_ligne = c_ligne+7; 

% Ecriture des solutions conformes 
xlswrite(fichier_out,{'Solutions conformes aux pr�f�rences utilisateur','','','','',''},'Solution',ligne(c_ligne:c_ligne+6));
c_ligne = c_ligne+7; 
N = size (x,2);
if (N==0) % Si pas de solutions coformes 
    c_ligne=c_ligne+7
else
    
    
    for i=1:N
        j = x(N+1-i);
        
        xlswrite(fichier_out,{'',p(j),t(j),f(j),rf(j),adc(j)},'Solution',ligne(c_ligne:c_ligne+6))
        c_ligne=c_ligne+7;
    end
    
    % Elimination des solutions conformes du vecteurs de toutes les
    % solutions 
    % A pr�sent, il ne reste que les solutions non conformes 
    t(x) =[];
    p(x) = [];
    f(x) = [];
    rf(x) = [];
    adc(x) = [];

end

%--------------------------------------------------------%
% Ecriture des solutions non conformes dans le fichier Excel 
% et impression sur l'�cran
xlswrite(fichier_out,{'Solutions non conformes aux pr�f�rences utilisateur','','','','',''},'Solution',ligne(c_ligne:c_ligne+6))
c_ligne=c_ligne+7;

for i = 1 :size (p,2)
    xlswrite(fichier_out,{'',p(i),t(i),f(i),rf(i),adc(i)},'Solution',ligne(c_ligne:c_ligne+6))
    c_ligne=c_ligne+7;

end

    