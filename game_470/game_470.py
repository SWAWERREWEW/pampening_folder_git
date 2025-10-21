import pygame
import _other_470.const
import _other_470.objects
import _other_470.scenes.gameover
import _other_470.scenes.menu
import _other_470.scenes.gamestart
import _other_470.scenes.gamewin

def main():
    # Запуск игры
    while _other_470.const.run:
        # Тормозим время
        clock = pygame.time.Clock()

        # Сценарий меню игры
        if _other_470.const.game_status == _other_470.const.scene1:
            _other_470.scenes.menu.menu()

        # Сценарий начало игры
        elif _other_470.const.game_status == _other_470.const.scene2:
            _other_470.scenes.gamestart.gamestart()

        # Сценарий проигрыш
        elif _other_470.const.game_status == _other_470.const.scene3:
            _other_470.scenes.gameover.gameover()

        # Сценарий выиграш
        elif _other_470.const.game_status == _other_470.const.scene4:
            _other_470.scenes.gamewin.gamewin()

        # Обновление экрана
        pygame.display.update()

        # Отслеживание особых событий
        for event in pygame.event.get():
            # Выход из игры
            if event.type == pygame.QUIT:
                _other_470.const.run = False
                pygame.quit()
                exit()

        # Установка значения кадров в секунду
        clock.tick(_other_470.const.fps)


if __name__ == "__main__":
    main()