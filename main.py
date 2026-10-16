import flet as ft
from flet.app.app import app

def main(page: ft.Page):
    page.title = "Audio PoC"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Register audio control in overlay
    audio = ft.Audio(
        src="finish.mp3",
        autoplay=False,
    )
    page.overlay.append(audio)

    def play_sound(e):
        audio.play()

    page.add(
        ft.ElevatedButton(
            text="Play Finish",
            icon=ft.Icons.PLAY_ARROW,
            on_click=play_sound,
        )
    )

if __name__ == "__main__":
    app(target=main, assets_dir="assets")
