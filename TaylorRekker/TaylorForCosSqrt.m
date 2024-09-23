% Skript som plottar Taylor-polynoma, opp til 
% ein bestemt orden, for funksjonen
% f(x) = cos (sqrt(x)) omkring x=0.
% Den maksimale ordenen til funksjonen er input
%
% Her er det nokre subtilitetar ....

% Gir maksimal orden
Nmax=15;

% Funksjonen
funk=@(x) cos(sqrt(x));

% Vektor med x-verdiar
x_funk=0:1e-2:50*pi;
x=-5*pi:1e-2:50*pi;

% Intervall på y-aksen
ymin = -1.2;
ymax = 5;


% Initerar polynomet
P=0*x;
an=1;

% Startar plot
figure(1)
plot(x_funk,funk(x_funk),'k-','linewidth',2)
axis([min(x) max(x) ymin ymax])
grid on
pause
for n=0:Nmax
  an=(-1)^round(n)/factorial(2*n);
  P=P+an*x.^n;
  plot(x_funk,funk(x_funk),'k-','linewidth',2)
  grid on
  hold on
  plot(x,P,'r--','linewidth',2)
  hold off
  axis([min(x) max(x) ymin ymax])
  title(['n=',num2str(n)])
  pause
end
hold off