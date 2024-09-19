% Dette skriptet plottar funksjonen 1/(1-x) 
% saman med Taylor-polynoma for n=1 opp til 
% ein Nmax omkring x=1.
% Nmax er input, hardkoda i starten

% Maksimal grad av Taylor-polynom
Nmax=15;

% Vektor med x-verdiar - og grenser på aksane
x=-2:1e-2:.99;
V= [-2 1 -0.1 7];

% Plottar funksjonen
plot(x, 1./(1-x),'k-', 'linewidth', 2);
axis(V)
hold on
grid on
pause

% Taylor-polynom av grad 0;
P=x.^0;
% Plottar Taylor-polynoma
for k=1:(Nmax+1)
  plot(x, P,'--', 'linewidth',1.5)
  title(['n=',num2str(k-1)])
  pause
  % Oppdaterar polynomet med neste ledd
  P=P + x.^k;
end

hold off