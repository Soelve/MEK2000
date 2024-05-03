% Skript som plottar Taylor-polynoma, opp til 
% ein bestemt orden, for funksjonen
% f(x) = e^x omkring x=0.
% Den maksimale ordenen til funksjonen er input

% Gir maksimal orden
Nmax=10;

% Funksjonen
funk=@(x) exp(x);

% Vektor med x-verdiar
x=-2:1e-2:2;

% Initerar polynomet
P=0*x;
an=1;

% Startar plot
figure(1)
plot(x,funk(x),'k-','linewidth',2)
  axis([min(x) max(x) 0 8])
grid on
pause
for n=0:Nmax
  an=1/factorial(n);
  P=P+an*x.^n;
  plot(x,funk(x),'k-','linewidth',2)
  grid on
  hold on
  plot(x,P,'r--','linewidth',2)
  hold off
  axis([min(x) max(x) 0 8])
  title(['n=',num2str(n)])
  pause
end
hold off
