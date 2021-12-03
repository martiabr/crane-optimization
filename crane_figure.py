import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib.patches import Arc

def get_angle_plot(line1, line2, offset=1, color=None, origin=(0, 0), 
                   len_x_axis = 1, len_y_axis = 1):
    l1xy = line1.get_xydata()
    
    # Angle between line1 and x-axis
    y1 = l1xy[1][1] - l1xy[0][1]
    x1 = l1xy[1][0] - l1xy[0][0]
    # Allows you to use this in different quadrants
    angle1 = np.degrees(np.arctan2(y1, x1))
    
    l2xy = line2.get_xydata()
    
    # Angle between line2 and x-axis
    y2 = l2xy[1][1] - l2xy[0][1]
    x2 = l2xy[1][0] - l2xy[0][0]
    angle2 = np.degrees(np.arctan2(y2, x2))
    
    theta1 = min(angle1, angle2)
    theta2 = max(angle1, angle2)
    
    angle = theta2 - theta1
    
    if color is None:
        color = line1.get_color() # Uses the color of line 1 if color parameter is not passed.
    
    return Arc(origin, len_x_axis*offset, len_y_axis*offset, 0, 
               theta1, theta2, color=color, 
               label = r'${:.4}^\circ$'.format(float(angle)))

r_0 = -0.5
r_end = 0.5
theta_0 = 0.4
l = 1.0
rect_height = 0.15
beam_height = 0.05
radius = 750

fig, ax = plt.subplots(figsize=(6,4))

line_1, = ax.plot([-1.2,1.2], [0,0], 'k--', alpha=0.7, lw=1.5)
rect_1 = ax.add_patch(Rectangle((0 - 1, 0 - 0.5*beam_height), 2, beam_height, facecolor='firebrick', edgecolor='k', lw=2))
rect_2 = ax.add_patch(Rectangle((r_0 - 0.2, 0.0 - 0.5*rect_height), 0.4, rect_height, facecolor='indianred', edgecolor='k', lw=2))

x_pendulum = r_0 + l * np.sin(theta_0)
y_pendulum = -l * np.cos(theta_0)
line_2, = ax.plot([r_0, x_pendulum], [0, y_pendulum], '-o', c='k', lw=3, ms=6)
point_1 = ax.scatter(x_pendulum, y_pendulum, s=radius, facecolors='darkorange', edgecolors='k', lw=2)

ax.scatter(r_0, -l, s=30, facecolor='firebrick', zorder=5)
ax.text(r_0, -l-0.1, 'Start', horizontalalignment='center')
ax.scatter(r_end, -l, s=30, facecolor='firebrick', zorder=5)
ax.text(r_end, -l-0.1, 'Target', horizontalalignment='center')

line_3, = ax.plot([-0.5, -0.5], [0,-1], 'k--', alpha=0.7, lw=1.5)
line_4, = ax.plot([0.5, 0.5], [-1,0], 'k--', alpha=0.7, lw=1.5)

angle_plot = get_angle_plot(line_3, line_2, offset=0.6, origin=[-0.5,0])
ax.add_patch(angle_plot)

ax.text(r_0, rect_height/2 + 0.05, r'$r$', horizontalalignment='center')
ax.text(-0.43, -0.4, r'$\theta$', horizontalalignment='center')

plt.axis('equal')
plt.xlim([-1, 1])
plt.ylim([-1.35, 0.35])
plt.savefig('crane_fig.png', dpi=400, bbox_inches='tight')

plt.show()
