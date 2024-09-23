% Skript som plottar Taylor-polynoma, opp til 
% ein bestemt orden, for funksjonen
% f(x) = sqrt(x) omkring x=1.
% Den maksimale ordenen til funksjonen er input.

% Gir maksimal orden
Nmax = 25;

% Funksjonen
funk=@(x) sqrt(x);

% Vektor med x-verdiar
x=0:1e-2:3;

% Intervall på y-aksen
ymin = -0.1;
ymax = 3;

% Initerar polynomet og koeffisienten i potensrekka
P=0*x;
teljar = 1;
nemnar = 1;

% Startar plot
figure(1)
plot(x,funk(x),'k-','linewidth',2)
axis([min(x) max(x) ymin ymax])
grid on
pause

% Første to polynom
% n = 0
P = teljar/nemnar * (x-1).^0;
plot(x,funk(x),'k-','linewidth',2)
grid on
hold on
plot(x,P,'r--','linewidth',2)
hold off
axis([min(x) max(x) ymin ymax])
title(['n=',num2str(n)])
pause

% n = 1
nemnar = 2;
P = P + teljar/nemnar * (x-1).^1;
plot(x,funk(x),'k-','linewidth',2)
grid on
hold on
plot(x,P,'r--','linewidth',2)
hold off
axis([min(x) max(x) ymin ymax])
title(['n=',num2str(n)])
pause

% Loopar over resten
for n=2:Nmax
  teljar = teljar*(2*n-3);
  nemnar = nemnar*(2*n);
  P=P + (-1)^(n+1)*teljar/nemnar*(x-1).^n;
  plot(x,funk(x),'k-','linewidth',2)
  grid on
  hold on
  plot(x,P,'r--','linewidth',2)
  hold off
  axis([min(x) max(x) ymin ymax])
  title(['n=',num2str(n)])
  pause
end
hold off