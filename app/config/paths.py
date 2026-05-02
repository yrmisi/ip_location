from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent

MAP_HTML_DIR: Path = BASE_DIR / "static" / "maps"

ENVS_DIR: Path = BASE_DIR / "config" / "envs"
