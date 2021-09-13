% data2txt.m
% 09/09/21
% charliex@slac.stanford.edu (C.Xu)
% Convert the .data extention to .txt for import to matlab

blah = dir('*.data');
L = length(blah);
for i = 1:L
    a = blah(i).name;
    b = strsplit(a,'.');
    fn = [char(b(1)) '.txt'];
    movefile(a, fn)
end

% clear all
% a = dir('*Ch1*')
% a.name
% for i = 1:11
%     % b = strsplit(a(i).name, '.');
%     % c(i,:) = b(1);
%     c(i,:) = a(i).name;
% end