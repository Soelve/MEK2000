% Dette skriptet lagar ein tone.
% Den plottar han og spelar han av - 
% for ulike spektrum, som blir hardkoda.
% Amplitude og frekvens blir også hardkoda.

% Grunnfrekvens
Frek = 440;
w = 2*pi*Frek;  % Vinkelfrekvens

% Bestemmer spektrumet
% Nokre litt tilfeldige verdiar
Spectrum = [1 .3 .1 .1 .1 .1 .05 .05];
% Vektor med n-verdiar
nn = 1:20;
% Alternerande, sakte avtakande (sagtann)
%Spectrum = (-1).^nn./nn;
% Frå eksempel med funksjon som liknar på sinus:
%Spectrum = 5./(2*nn+1).^3;
% Rein sinus
%Spectrum = [1];
L = length(Spectrum);

% Tida det varer - i sekund
TimeSec = 4;
% Amplitude
Amp = .2;

% Samplefrekvens
Fs = 44100;
% Vektor med tidspunkt
t = linspace(0, TimeSec, TimeSec*Fs);

% Miksar overtonar og lagar lydsignal
F = 0*t;            % Set F til null
for n = 1:L
  F = F + Spectrum(n)*sin(n*w*t);   % Legg til - komponent for komp.
end

% Justere amplitude
F = Amp*F;

% Legge til støy?
Noise = 0*rand(1,TimeSec*Fs);
F = F + Noise;

% Plottar lyden
figure(2)
subplot(2,1,1)
bar([1:L]*w/2/pi, Spectrum)
xlabel('Frekvens [Hz]')
subplot(2,1,2)
plot(t(1:1000), F(1:1000))
xlabel('Tid [s]')
ylabel('Amplitude')
set(gca, 'fontsize', 12)

% Spelar av lyden
hplayer = audioplayer(F, Fs);
play(hplayer);
