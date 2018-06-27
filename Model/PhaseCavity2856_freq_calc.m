% Calculating new LCLS I Phase cavity reasonate frequency 
% 2856MHz RF cards are not compatible with 2805MHz reasonate frequency
% ADC CLK - 357MHz, RF frequency 476MHz
% Keeping the IF/ADC CLK ratio the same as the 2600MHz LCLS 2 style to 
% minimize the algorithm change

clear all; clc;
% format compact
% 2600MHz result from Steve
Fcav2600 = 2600e6 - 4.64e6;
Fcav2600 = 2600e6 - 5* 13e6/14
Fadc2600 = 351e6    % ADC sampling frequency
Flo2600  = 2600e6 - 5/21*Fadc2600 % LO frequency
Fif2600  = Fcav2600 - Flo2600
if2adc_r = Fif2600/Fadc2600

Fadc2856 = 357e6    % ADC clk for 2856MHz board
Fif2856  = Fadc2856 * if2adc_r  % Calculating IF frequency base on ADC clk and ratio
Fif2856_og = 85e6;
Flo2856  = 2856e6 - Fif2856_og;
Fcav2856 = Flo2856 + Fif2856 % New cavity frequency