import pygame
import math
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Texto Estilizado con Pygame")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fuente para el texto
font = pygame.font.Font(None, 150)  # Letras grandes, ajusta según necesites
text = "TU_NOMBRE_AQUÍ"  # Reemplaza con el nombre o texto que quieras
text_surfaces = [font.render(char, True, WHITE) for char in text]  # Renderizar cada letra individualmente
text_rects = []  # Lista para almacenar las posiciones de las letras

# Calcular posiciones iniciales para centrar el texto
total_width = sum(surface.get_width() for surface in text_surfaces) + (len(text) - 1) * 10  # Espacio entre letras
start_x = (WIDTH - total_width) // 2
current_x = start_x

for surface in text_surfaces:
    rect = surface.get_rect()
    rect.x = current_x
    rect.centery = HEIGHT // 2  # Centrar verticalmente
    text_rects.append(rect)
    current_x += rect.width + 10  # Espacio de 10 píxeles entre letras

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Obtener la posición del cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Dibujar cada letra con efecto de borde dinámico
    for i, (surface, rect) in enumerate(zip(text_surfaces, text_rects)):
        # Calcular centro de la letra
        char_center_x = rect.centerx
        char_center_y = rect.centery

        # Calcular distancia entre el cursor y el centro de la letra
        dx = mouse_x - char_center_x
        dy = mouse_y - char_center_y
        distance = math.sqrt(dx * dx + dy * dy)

        # Si el cursor está dentro de un radio de 10 píxeles, aplicar borde luminoso
        if distance <= 10:
            # Generar un color aleatorio para el borde
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            border_color = (r, g, b)
        else:
            border_color = WHITE  # Borde blanco opaco por defecto

        # Dibujar el borde (simulando -webkit-text-stroke)
        border_surface = pygame.Surface((rect.width + 4, rect.height + 4), pygame.SRCALPHA)
        pygame.draw.rect(border_surface, border_color, (0, 0, rect.width + 4, rect.height + 4), 2)  # Borde de 2 píxeles
        screen.blit(border_surface, (rect.x - 2, rect.y - 2))
        # Dibujar la letra encima del borde
        screen.blit(surface, rect.topleft)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS

# Cerrar Pygame
pygame.quit()