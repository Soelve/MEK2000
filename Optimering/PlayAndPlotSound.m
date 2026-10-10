% Skriptet les inn ei lydfil i wav-format og plottar lyden - både
% i tid og i frekvens. Lyden blir også spelt av
% Antal samplingar per sekund er gitt i linje 7 og namnet på lydfila
% er itt i linje 12 (hardkoda).

% Sampling rate (44.1 kHz) - antal punkt per sekund
Fs = 44100;

%
% Les inn lydfil
%
%load chirp.mat
%load handel.mat
load gong.mat

y=y(:,1);                           % Reduserar det til eitt signal (mono)
Npkt = length(y);                   % Bestemmer talet på punkt
Tmax=Npkt/Fs;                       % Lengda i sekund
dt=Tmax/(Npkt-1);                   % Tidssteg
T=0:dt:Tmax;                        % Vektor med tidspunkt

%
% Spelar av musikken
%
hplayer = audioplayer(y, Fs);
play(hplayer);

%
% Lagar plott av lyden - i tid
%
figure(1)
plot(T,y)
xlabel('Tid i sekund')
ylabel('Signal')

%
% For å sjå på frekvensfordelinga: Fourieromvenging (FFT)
%
Y = fft(y,Npkt);                    % Lydsignalet i frekvens
F = ((0:1/Npkt:1-1/Npkt)*Fs).';     % Vektor med frekvensane
magnitudeY = abs(Y);                % Styrken på FFT-signalet
phaseY = unwrap(angle(Y));          % Fasen til FFT-signalet

%
% Lagar plott av lyden - i frekvens
%
figure(2)
subplot(2,1,1)                      % Deler plottet i to
plot(F(1:floor(Npkt/2))/1e3,log(magnitudeY(1:floor(Npkt/2))))
xlabel('Frekvens i kHz')            % Set tekst på aksane
ylabel('Signal i dB')
title('Signalstyrke')
subplot(2,1,2)                      % Nytt underplott
plot(F(1:floor(Npkt/2))/1e3,phaseY(1:floor(Npkt/2)))
xlabel('Frekvens i kHz')            % Set tekst på aksane
ylabel('Fasen til signalet')