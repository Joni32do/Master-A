clear k
% ODE15s solution the Reaction Rate Equation for
% the Michaelis-Menten system.
%
% Parameters from Chapter 7 of
% Stochastic Modelling for Systems Biology,
% by Darren J. Wilkinson, Chapman & Hall/CRC, 2006.
%
% Downloadable from
% http://www.maths.strath.ac.uk/˜aas96106/algfiles.html
% along with an extended version that produces graphical output.
tspan = [0 50]; 
yzero = [5e-7; 2e-7; 0; 0];
options = odeset('AbsTol',1e-8);
k.k1 = 1e6; 
k.k2 = 1e-4; 
k.k3 = 0.1;
[t,y] = ode15s(@(t, y) mm_rre_ode(t, y, k),tspan,yzero,options);
y = y';
figure();
plot(t, y(1, :), 'DisplayName', 'substrate')
hold on
plot(t, y(2, :), 'DisplayName', 'enzym')
plot(t, y(3, :), 'DisplayName', 'complex')
plot(t, y(4, :), 'DisplayName', 'product')
title("Reaction Rate Equation")
legend();
hold off


