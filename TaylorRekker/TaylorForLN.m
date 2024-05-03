% Dette skriptet plottar den naturlege
% logaritmefunksjonen saman med Taylor-
% polynoma for n=1 opp til ein Nmax
% omkring x=1.
% Nmax er input, hardkoda i starten

% Maksimal grad av Taylor-polynom
Nmax=20;

% Vektor med x-verdiar - og grenser på aksane
x=0.05:1e-2:3;
V= [0 3 -5 2];

% Plottar funksjonen
plot(x,log(x),'k-','linewidth',2);
axis(V)
hold on
grid on
pause

% Taylor-polynom av grad 1;
P=x-1;
% Plottar Taylor-polynoma
for k=2:Nmax
  plot(x,P,'--','linewidth',1.5)
  title(['n=',num2str(k-1)])
  pause
  Prefaktor=(-1)^(k-1)/k*(x-1).^k;  
  P=P+Prefaktor;
end

hold off