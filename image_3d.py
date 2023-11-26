import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_image(solid_3d, fcolor='cyan'):
    # Criar uma figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1,1,1])
    
    # Adicionar o objeto STL à figura
    solid_mesh = mplot3d.art3d.Poly3DCollection(solid_3d.vectors, edgecolor="k", facecolors=fcolor, linewidths=0.5)
    ax.add_collection3d(solid_mesh)
    
    # Obter limites para ajustar a escala
    x_limits = solid_3d.x.min(), solid_3d.x.max()
    y_limits = solid_3d.y.min(), solid_3d.y.max()
    z_limits = solid_3d.z.min(), solid_3d.z.max()
    
    # Calcular o centro para ajustar a escala
    x_center = np.mean(x_limits)
    y_center = np.mean(y_limits)
    z_center = np.mean(z_limits)
    
    # Configurar a escala da plotagem
    max_range = np.array([x_limits, y_limits, z_limits]).ptp().max() / 2.0
    mid_x = (x_limits[1] + x_limits[0]) / 2.0
    mid_y = (y_limits[1] + y_limits[0]) / 2.0
    mid_z = (z_limits[1] + z_limits[0]) / 2.0
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    # Adicionar uma iluminação
    ax.azim = 45
    ax.elev = 30
    
    # Adicionar uma grade
    ax.grid(False)
    
    # Ajustar a aparência da figura
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('k')
    ax.yaxis.pane.set_edgecolor('k')
    ax.zaxis.pane.set_edgecolor('k')
    
    # Adicionar rótulos
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
def create_video(solid_3d, video_name, fcolor='cyan'):
    # Criar uma figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1,1,1])
    
    # Adicionar o objeto STL à figura
    solid_mesh = mplot3d.art3d.Poly3DCollection(solid_3d.vectors, edgecolor="k", facecolors=fcolor, linewidths=0.5)
    ax.add_collection3d(solid_mesh)
    
    # Obter limites para ajustar a escala
    x_limits = solid_3d.x.flatten()
    y_limits = solid_3d.y.flatten()
    z_limits = solid_3d.z.flatten()
    
    # Calcular o centro para ajustar a escala
    x_center = np.mean(x_limits)
    y_center = np.mean(y_limits)
    z_center = np.mean(z_limits)
    
    # Configurar a escala da plotagem
    max_range = np.array([x_limits, y_limits, z_limits]).ptp().max() / 2.0
    mid_x = (x_limits.max() + x_limits.min()) / 2.0
    mid_y = (y_limits.max() + y_limits.min()) / 2.0
    mid_z = (z_limits.max() + z_limits.min()) / 2.0
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    # Adicionar uma iluminação
    ax.azim = 45
    ax.elev = 30
    
    # Adicionar uma grade
    ax.grid(False)
    
    # Ajustar a aparência da figura
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('k')
    ax.yaxis.pane.set_edgecolor('k')
    ax.zaxis.pane.set_edgecolor('k')
    
    # Adicionar rótulos
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    # Remover os eixos
    ax.set_axis_off()
    
    # Função de animação para girar o objeto
    def update(frame):
        ax.view_init(elev=10, azim=frame)
    
    # Criar animação
    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
    
    # Salvar animação como arquivo .gif
    ani.save(video_name, writer='pillow', fps=30)