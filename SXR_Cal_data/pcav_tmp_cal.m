% pcav_tmp_cal.m
% 09/01/2021
% charliex@slac.stanford.edu (C. Xu)
% Reading in phase cavity calibration files

clear all; close all;

a = dir('*Ch8*');
for i = 1:length(a)
    % b = strsplit(a(i).name, '.');
    % c(i,:) = b(1);
    c(i,:) = a(i).name;
end
ba = strsplit(c(1,:),'.');
bb = char(ba(1));
bc = bb(9:end);
% data_table = readtable('Ch8_data_20201023_113100.txt', 'Delimiter', ' ');
data_table = readtable(['Ch8_data' bc '.txt'], 'Delimiter', ' ');
wf_length  = table2array(data_table(1,4));
% raw_wf = zeros(height(data_table), wf_length);
wf_ts  = ceil(seconds(table2array(data_table(:,3))))';
raw_wf = table2array(data_table(:,5:end));
% figure();
% plot(raw_array(1,:));
% grid on
size(raw_wf)

time_table = readtable(['Time1' bc '.txt'], 'Delimiter', ' ');
time_size = size(time_table)
target_var = 12;
raw_time  = table2array(time_table(:,12))';
time_ts = ceil(seconds(table2array(time_table(:,11))))';
% figure();
% plot(raw_time);
% grid on

fs = 357e6;
L = length(raw_wf(1,:));

NFFT = 2^(nextpow2(L)+5);
Y = fft(raw_wf(:,:), NFFT, 2)/L;
f = (fs/2)*(linspace(0,1,NFFT/2));

data_f_amp = 2 * abs(Y(:,1:NFFT/2));
data_f_dB  = 20*log10(data_f_amp);
[~,cav_f_ind] = max(data_f_dB(:,:),[],2);
cav_f = f(cav_f_ind);

% figure();
% plot(cav_f); grid on

figure();
for i = 1:time_size(1)
    plot(f,data_f_dB(i,:)); hold on
end
hold off; grid on;

for i = 2:length(a)
    ba = strsplit(c(i,:),'.');
    bb = char(ba(1));
    bc = bb(9:end);
    % data_table = readtable('Ch8_data_20201023_113100.txt', 'Delimiter', ' ');
    data_table = readtable(['Ch8_data' bc '.txt'], 'Delimiter', ' ');
    raw_wf = table2array(data_table(:,5:end));
    wf_ts1 = ceil(seconds(table2array(data_table(:,3))))';
    wf_ts  = [wf_ts wf_ts1];
    % figure();
    % plot(raw_array(1,:));
    % grid on
    size(raw_wf)
    L = length(raw_wf(1,:));

    NFFT = 2^(nextpow2(L)+5);
    Y = fft(raw_wf(:,:), NFFT, 2)/L;
    f = (fs/2)*(linspace(0,1,NFFT/2));

    data_f_amp = 2 * abs(Y(:,1:NFFT/2));
    data_f_dB  = 20*log10(data_f_amp);
    [~,cav_f_ind] = max(data_f_dB(:,:),[],2);
    cav_f1 = f(cav_f_ind);
    cav_f = [cav_f cav_f1];

    time_table = readtable(['Time1' bc '.txt'], 'Delimiter', ' ');
    time_size = size(time_table)
    target_var = 12;
    raw_time1  = table2array(time_table(:,12))';
    raw_time = [raw_time raw_time1];
    time_ts1 = ceil(seconds(table2array(time_table(:,11))))';
    time_ts  = [time_ts time_ts1];

    % figure();
    % plot(cav_f); grid on

    % figure();
    % for i = 1:time_size(1)
    %     plot(f,data_f_dB(i,:)); hold on
    % end
    % hold off; grid on;
end
bad_shot = (cav_f == 0);
cav_f(bad_shot) = [];
wf_ts(bad_shot) = [];
figure();plot(cav_f); grid on
size(cav_f)
size(raw_time)
cav_f(2,:) = cav_f(1,:);
cav_f(1,:) = wf_ts(1,:) - (wf_ts(1,1));
raw_time(2,:) = raw_time(1,:);
raw_time(1,:) = time_ts(1,:)-time_ts(1,1);
figure(); plot(cav_f(1,:),cav_f(2,:)/(1e6)); grid on
xlabel("time (s)"); set(get(gca, 'YLabel'), 'String', 'Frequency(MHz)');

[sorted_cav_f(1,:),sorted_cav_f(2,:)] = sort(cav_f(2,:));

time_match = zeros(1,length(raw_time));
for i = 1:length(raw_time)
    if 
    if cav_f(1,i) == raw_time(1,i)
        time_match(1,i) = i;
    end
end

% testf = 85e6;
% T = 0:(1/fs):L*(1/fs);
% testw = sin(2*pi*testf*T);
% Y1 = fft(testw, NFFT)/L;
% data_f1_amp = 2 * abs(Y1(1,1:NFFT/2));
% data_f1_dB  = 20*log10(data_f1_amp);
% figure();
% plot(f,data_f1_dB); grid on