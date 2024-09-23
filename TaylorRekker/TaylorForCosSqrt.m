% Skript som plottar Taylor-polynoma, opp til 
% ein bestemt orden, for funksjonen
% f(x) = cos (sqrt(x)) omkring x=0.
% Den maksimale ordenen til funksjonen er input

% Gir maksimal orden
Nmax=15;

% Funksjonen
funk=@(x) cos(sqrt(x));

% Vektor med x-verdiar
x=0:1e-2:50*pi;

% Initerar polynomet
P=0*x;
an=1;

% Startar plot
figure(1)
plot(x,funk(x),'k-','linewidth',2)
axis([min(x) max(x) -1.2 1.2])
grid on
pause
for n=0:Nmax
  an=(-1)^round(n)/factorial(2*n);
  P=P+an*x.^n;
  plot(x,funk(x),'k-','linewidth',2)
  grid on
  hold on
  plot(x,P,'r--','linewidth',2)
  hold off
  axis([min(x) max(x) -1.2 1.2])
  title(['n=',num2str(n)])
  pause
end
hold off