import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка окна и иконки
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/m.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения мишени и определение ее размеров
target_img = pygame.image.load("img/target.png")
target_width = 100
target_height = 100

# Установка начальной позиции мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный выбор цвета фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Начальное количество очков
score = 0

# Создание шрифта для отображения текста
font = pygame.font.Font(None, 36)

# Создание объекта Clock для управления частотой обновления экрана
clock = pygame.time.Clock()

# Время игры в секундах и начальное время
game_time = 30
start_time = pygame.time.get_ticks()

# Переменная для управления основным циклом игры
running = True
while running:
    # Очистка экрана и установка цвета фона
    screen.fill(color)

    # Отображение оставшегося времени
    time_remaining = max(0, game_time - (pygame.time.get_ticks() - start_time) // 1000)
    time_text = font.render(f"Time: {time_remaining}", True, (255, 255, 255))
    screen.blit(time_text, (10, 10))

    # Отображение текущего счета
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 50))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по мишени и обновление счета
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отображение мишени
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

    # Проверка времени игры и управление частотой обновления экрана
    if time_remaining == 0:
        running = False
    clock.tick(30)

# Отображение окончательного счета
final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
pygame.display.update()

# Ожидание перед выходом из игры
pygame.time.wait(2000)

# Завершение работы Pygame
pygame.quit()