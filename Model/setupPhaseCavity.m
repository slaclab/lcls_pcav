%script setupPhaseCavity
format compact

qbeam = 100e-12  %beam charge, typ 100 pC
Frf = 1300e6

Fcav = 2600e6 - 5* 13e6/14

wcav = 2*pi*Fcav; 
Qcav = 6060
Cav = tf([wcav/Qcav    0], [1  wcav/Qcav  wcav^2]) %cavity filter response

Fbp = Fcav, wbp = 2*pi*Fbp; Qbp = 3; % bandpass filter
BPrf = tf([wbp/Qbp  0], [1  wbp/Qbp wbp^2])  % RF bandpass filter response
%Flo = 2516.4285e6% LO Frequency

Flp = 1e9, wlp = 2 *pi*Flp; %Mixer IF Lowpass filter
LPif = tf( wlp^2, [ 1 wlp/.707 wlp^2])

Fadc = 351e6    %ADC sampling frequency
Flo = 2*Frf - 5/21*Fadc % LO frequency

Fif = Fcav - Flo; wif = 2*pi*Fif; Qif = 4.2% Mixer If filter
BPif = tf([wif/Qif  0], [1  wif/Qif wif^2])  % RF bandpass filter response

Idark = 400e-9    % Dark current, taken to be max allowed by Gun PRD
qdark = Idark/Flo %dark current charge per RF bucket (for sturcture dark current
Fgun = 185.7143e6   %Gun RF = 1300/7

%Plot transfer functions
bopt = bodeoptions;
bopt.FreqUnits = 'MHz';
bopt.PhaseVisible = 'on';
figure(1), close(1), figure(1)
bodeplot(Cav, BPrf, wcav + 2*pi*(-20e6:0.2e6:20e6), bopt); grid on
title('Cavity & RF Input Filter Responses')

figure(2)
bodeplot(LPif, bopt); grid on
title('IF Lowpass Filter Response')

figure(3)
bodeplot(BPif, bopt)
grid on
title('IF Bandpass Filter Response')