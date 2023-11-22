%% Two-Segment arm model


% Parameters

% Upper arm
l1 = 0.335;
d1 = 0.146;
m1 = 2.1;
I1 = 0.024;

% Lower arm
l2 = 0.263;
d2 = 0.179;
m2 = 1.65;
I2 = 0.025;

% Forces

g = 9.81;

% Simulation Parameters
t0 = 0;
T = 5;
dt = 0.001;
t = t0:dt:T;
N = floor(T/dt);

% Stiffness Matrix
M11 = @(q) m1*d1^2 + m2*(l1^2 + d2^2 + 2*l1*d2*cos(q(2)) ) + I1 + I2;
M12 = @(q) m2*(l1*d2*cos(q(2)) + d2^2) + I2;
M22 = @(q) d2^2*m2 + I2;

M = @(q) [M11(q), M12(q); ...
          M12(q), M22(q)];



% Generalized Corriolis

C1 = @(q, qdot) -l1*d2*m2*sin(q(2))*(2*qdot(1)*qdot(2) -qdot(2)^2) ...
      + g*(cos(q(1)-pi/2))*(m1*d1 + m2*l1) ...
      - g*cos(q(1)+q(2)-pi/2)*(m2*d2);
C2 =  @(q, qdot) -qdot(1)*qdot(2)*(m2*l1*sin(q(2))) ...
         +m2*l1*qdot(1)*d2*(qdot(1)+qdot(2))*sin(q(2)) ...
         +m2*g*d2*cos(q(1)+q(2)-pi/2);

C = @(q, qdot) [C1(q, qdot); ...
                C2(q, qdot)];


%% Updated Matrix

% Matrix M 
M11 = @(q) m1*d1^2 + m2*( l1^2 + d2^2 + 2*l1*d2*cos(q(2))) + I1 + I2;
M12 = @(q) m2*(d2^2 + l1*d2*cos(q(2))) + I2;
M21 = @(q) m2*(d2^2 + l1*d2*cos(q(2))) + I2;
M22 = @(q) m2*d2^2 + I2;

M = @(q) [M11(q), M12(q); ...
          M21(q), M22(q)]; 

% Matrix C
C1 = @(q, qdot) -l1*d2*m2*sin(q(2))*(2*qdot(1)*qdot(2) + qdot(2)^2) ...
      + g*(cos(q(1)-pi/2))*(m1*d1 + m2*l1) ...
      + g*cos(q(1)+q(2)-pi/2)*(m2*d2);
C2 =  @(q, qdot) -qdot(1)*qdot(2)*(m2*l1*d2*sin(q(2))) ...
         +m2*l1*qdot(1)*d2*(qdot(1)+qdot(2))*sin(q(2)) ...
         +m2*g*d2*cos(q(1)+q(2)-pi/2);

C = @(q, qdot) [C1(q, qdot); ...
                C2(q, qdot)];


%% Initial values

% Case 1
q0 = [0; 0]
qdot0 = [0; 0]
u0 = [0; 0]
% 
% % Case 2
q0 = [0.35; 0]
qdot0 = [0; 0]
u0 = [0; 0]
% 
% Case 3
% q0 = [0; 0]
% qdot0 = [0; 0]
% u0 = [2.0; 0]

% % Case 4
% q0 = [pi/2; pi/8];
% qdot0 = [0; 0];
% u0 = [1; 1];


%% Simulation Loop
q = zeros(2, N+1);
qdot = zeros(2, N+1);
qddot = zeros(2, N+1);


q(:,1) = q0;
qdot(:,1) = qdot0;
u = u0;

for i = 1:N
    qddot(:, i) = M(q(:,i))\(u - C(q(:,i), qdot(:,i)) );
    qdot(:, i+1) = qdot(:, i) + dt * qddot(:, i);
    q(:, i+1) = q(:, i) + dt * qdot(:, i);
end


%% Plotting
figure(1)
plot(t, q(1, :))
hold on
plot(t, q(2, :))
legend("Upper Arm Angle", "Lower Arm Angle")
hold off


%% Animation
x1 = @(q) l1 * cos(q(1) - pi/2);
y1 = @(q) l1 * sin(q(1) - pi/2);
x2 = @(q) l1 * cos(q(1) - pi/2) + l2 * cos(q(1) -pi/2 + q(2));
y2 = @(q) l1 * sin(q(1) - pi/2) + l2 * sin(q(1) -pi/2 + q(2));

figure(2)

for i=1:10:N
    plot([0, x1(q(:, i)), x2(q(:, i))], [0, y1(q(:, i)), y2(q(:, i))])
    hold on
    scatter([0, x1(q(:, i)), x2(q(:, i))], [0, y1(q(:, i)), y2(q(:, i))],'filled')
    hold off
    axis([-0.5, 0.5, -0.8, 0.2])
    pause(dt)
    drawnow
end


%% Test
q0 = [0; 0]
qdot0 = [1; 1]
u0 = [0; 0]

M(q0)
C(q0, qdot0)

