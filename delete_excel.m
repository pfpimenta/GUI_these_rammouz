%------------------------------------------------------------%
%---------Réinitialisation du fichier Excel : Solution-------%

% Effacer la feuille solution du fichier Excel 
% Appelée lorsque l'utilisateur lance une autre simulation avec le même
% fichier Excel

% Méthode : Ecrire un vide '' dans les cases de la feuille 
%xlswrite(f1,{''},'Solution','b3:b3')

ligne = ['b6:f6','b7:f7']; % Compteur de case 
for i = 1:5:size(ligne,2)
    xlswrite(f1,{'','','','',''},'Solution',ligne(i:i+4)) % Ecrire dans un vide '' dans les cases
end
xlswrite(f1,{'Configuration du nœud'},'Solution','a8:f8')

ligne = ['a9:f9  ','a10:f10','a11:f11','a12:f12','a13:f13','a14:f14','a15:f15','a16:f16','a17:f17','a18:f18','a19:f19','a20:f20','a21:f21','a22:f22'];
for i = 1:7:size(ligne,2)
    xlswrite(f1,{'','','','','',''},'Solution',ligne(i:i+6))
end
