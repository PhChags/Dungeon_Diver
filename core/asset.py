from pathlib import Path

from vendor.pplay.sprite import Sprite
from vendor.pplay.gameimage import GameImage

_base_path = f"{Path(__file__).resolve().parent}/../assets"


def resolve_sprite(asset_name: str) -> Sprite:
    """
    Resolves an absolute asset name to a Sprite instance
    """
    return Sprite(f"{_base_path}/{asset_name}")


def resolve_game_image(asset_name: str) -> GameImage:
    """
    Resolves an absolute asset name to a GameImage instance
    """
    return GameImage(f"{_base_path}/{asset_name}")
