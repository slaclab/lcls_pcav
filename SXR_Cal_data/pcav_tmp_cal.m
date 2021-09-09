% pcav_tmp_cal.m
% 09/01/2021
% charliex@slac.stanford.edu (C. Xu)
% Reading in phase cavity calibration files

clear all; close all;
data_table = readtable('Ch1_data_20201023_113100.txt', 'Delimiter', ' ');
data_table = removevars(data_table, {'Var1', 'Var2', 'Var3', 'Var4'});
raw_array  = table2array(data_table);
figure();
plot(raw_array(1,:));
grid on

time_table = readtable('Time0_20201023_113100.txt', 'Delimiter', ' ');
time_size = size(time_table)
target_var = 12;
for i = 1:target_var-1
    time_table = removevars(time_table, ['Var' num2str(i)]);
end
for i = 0:(time_size(2)-target_var-1)
    time_table = removevars(time_table, ['Var' num2str(time_size(2)-i)]);
end
raw_time  = table2array(time_table);
figure();
plot(raw_time);
grid on


fs = 357e6;
L = length(raw_array(1,:));

NFFT = 2^nextpow2(L);
Y = fft(raw_array(:,:), NFFT, 2)/L;
f = (fs/2)*(linspace(0,1,NFFT/2));

data_f_amp = 2 * abs(Y(:,1:NFFT/2));
data_f_dB  = 20*log10(data_f_amp);
[~,cav_f_ind] = max(data_f_dB,[],2);
cav_f = f(cav_f_ind);
figure();
plot(cav_f); grid on

figure();
for i = 1:time_size(1)
    plot(f,data_f_dB(i,:)); hold on
end
hold off; grid on;


% testf = 85e6;
% T = 0:(1/fs):L*(1/fs);
% testw = sin(2*pi*testf*T);
% Y1 = fft(testw, NFFT)/L;
% data_f1_amp = 2 * abs(Y1(1,1:NFFT/2));
% data_f1_dB  = 20*log10(data_f1_amp);
% figure();
% plot(f,data_f1_dB); grid on