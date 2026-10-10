% Skriptet plottar og spelar av ein tone med ei innhyllingskurve
% (ein envelope).

% Grunnfrekvens:
f = 440;

% Sampling rate (44.1 kHz) - antal punkt per sekund
Fs = 44100;

% Vidda av innhyllingskurva (i sekund)
Width = 0.25;

Npkt = 250000;                   % Bestemmer talet på punkt
Tmax=Npkt/Fs;                       % Lengda i sekund
dt=Tmax/(Npkt-1);                   % Tidssteg
T=0:dt:Tmax;                        % Vektor med tidspunkt
Envelope = 1./(exp(15*((abs(T-Tmax/2)-Width)))+1);
y = Envelope.*sin(2*pi*f*T);

%
% Spelar av tonen
%
hplayer = audioplayer(y, Fs);
play(hplayer);

%
% Lagar plott av lyden - i tid
%
figure(1)
plot(T, y)
hold on
plot(T, Envelope, 'r-')
plot(T, -Envelope, 'r-')
hold off
xlabel('Tid i sekund')
ylabel('Signal')

%
% For å sjå på frekvensfordelinga: Fourieromvenging (FFT)
%
Y = fft(y,Npkt);                    % Lydsignalet i frekvens
F = ((0:1/Npkt:1-1/Npkt)*Fs).';     % Vektor med frekvensane
magnitudeY = abs(Y);                % Styrken på FFT-signalet

%
% Lagar plott av lyden - i frekvens
%
figure(3)
plot(F(1:floor(Npkt/2)), magnitudeY(1:floor(Npkt/2)))
V = axis;
axis([f-10 f+10 V(3) V(4)])
xlabel('Frekvens in Hz')            % Set tekst på aksane
ylabel('Signalstyrke')