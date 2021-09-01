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