function yprime = mm_rre_ode(t,y,k)
    % MM_RRE Michaelis-Menten Reaction Rate Equation
    yprime = zeros(4,1);
    yprime(1) = -k.k1*y(1)*y(2) + k.k2*y(3);
    yprime(2) = -k.k1*y(1)*y(2) + (k.k2+k.k3)*y(3);
    yprime(3) = k.k1*y(1)*y(2) - (k.k2+k.k3)*y(3);
    yprime(4) = k.k3*y(3);
end