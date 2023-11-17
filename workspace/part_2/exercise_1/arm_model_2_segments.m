%% Two-Segment arm model

% Symbolic





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
dt = 0.01;
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


M = @(q) [m1*d1^2+I1+m2*l1^2+m2*l1*d2*cos(q(2))+m2*d2^2+I2, m2*l1*d2*cos(q(2))+m2*d2^2+I2;
    m2*l1*d2*cos(q(2))+m2*d2^2+I2, m2*d2^2+I2];
C = @(q,qdot) [g*(m1*d1*cos(q(1))+m2*l1*cos(q(1))+m2*d2*cos(q(1)+q(2)))-l1*d2*qdot(1)*sin(q(2))*qdot(2)-l1*d2*qdot(2)^2*sin(q(2));
    g*m2*d2*cos(q(1)+q(2))-m2*l1*d2*qdot(1)* sin(q(2))* qdot(2)+m2*l1*d2*qdot(1)*(qdot(1)+qdot(2))*sin(q(2))];


%% Initial values

% Case 1
q0 = [0; 0]
qdot0 = [0; 0]
u0 = [0; 0]
% 
% Case 2
% q0 = [0.35; 0]
% qdot0 = [0; 0]
% u0 = [0; 0]
% 
% % Case 3
% q0 = [-pi/2; 0]
% qdot0 = [0; 0]
% u0 = [2.0; 0]


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
hold on
for i=1:N
    plot([0, x1(q(:, i)), x2(q(:, i))], [0, y1(q(:, i)), y2(q(:, i))])
    axis([-0.5, 0.5, -0.5, 0.5])
    drawnow
    pause(dt)
end
hold off
% % Create the figure
% figure;
% hLine = plot(t, y1); % Plot the initial data
% hold on;
% hLine2 = plot(t, y2);
% hold off;
% 
% % Add a slider
% slider = uicontrol('Style', 'slider', 'Min', 1, 'Max', length(t), 'Value', 1, 'Position', [10 50 300 20]);
% addlistener(slider, 'Value', 'PostSet', @(~,~) updatePlot(hLine, hLine2, t, slider));
% 
% % Function to update the plot based on the slider value
% function updatePlot(line1, line2, time, slider)
%     val = round(get(slider, 'Value')); % Get the slider value
%     set(line1, 'XData', [0, x1(q(:, i)), x2(q(:, i))], 'YData', [0, y1(q(:, i)), y2(q(:, i))]; % Update first plot
%     set(line2, 'XData', time(1:val), 'YData', cos(time(1:val))); % Update second plot
%     drawnow;
% end
% 
% for i=1:N+1
%     
% end
% 
% [0, x1(q(:, i)), x2(q(:, i))]
% [0, y1(q(:, i)), y2(q(:, i))]


%% Test
q0 = [0; 0]
qdot0 = [1; 1]
u0 = [0; 0]

M(q0)
C(q0, qdot0)

