from vendor.pplay.window import *

from core.scene import SceneManager

from scenes.main_menu import MainMenu


def main():
    screen = Window(1280, 720)
    screen.set_title("Dungeon Diver")

    scene_manager = SceneManager(screen)
    scene_manager.show_scene(MainMenu())

    while True:
        if scene_manager.has_no_scenes_to_show():
            break

        scene_manager.tick()

    return


if __name__ == "__main__":
    main()
