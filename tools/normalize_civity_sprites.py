"""Normalise the first BRTrains3 Civity spritesheets.

The legacy sheets contain rows that are reused by several consist profiles. BRBuild's
allocator consumes rows in profile/livery order, so this script expands those shared
rows into that order while retaining the legacy 8-view template geometry.
"""
from pathlib import Path
import shutil
import sys

from PIL import Image

BRBUILD = Path(sys.argv[1])
PROJECT = Path(sys.argv[2])
sys.path.insert(0, str(BRBUILD))

from Sprites.PalettedImage import PalettedImage  # noqa: E402
from Sprites.SpritesheetExtractor import SpritesheetExtractor  # noqa: E402
from Templates.TemplateLoaderNML import TemplateLoaderNML  # noqa: E402
from Templates.SpritesheetLegacyConverter import SpritesheetLegacyConverter  # noqa: E402

palette = PalettedImage.load_palette(str(BRBUILD / "Sprites/ttd-newgrf-dos.gpl"))
definitions = TemplateLoaderNML().read_folder(str(BRBUILD / "Templates"))
converter = SpritesheetLegacyConverter(definitions, palette)

sources = {
    "BR195Civity": ([13, 39, 13, 65, 39], None),
    "BR196Civity": ([13, 39, 91, 117, 13, 65, 65, 39, 91, 143, 143, 117], "split_gap"),
    "BR197Civity": ([13, 38, 13, 63, 38], None),
}

for vehicle, (wanted_rows, fix) in sources.items():
    folder = PROJECT / "src/vehicles" / vehicle
    target = folder / f"{vehicle}.png"
    source = folder / "legacy_source.png"
    if not source.exists():
        shutil.copy2(target, source)

    image_path = source
    if fix == "split_gap":
        image = Image.open(source).convert("P")
        image.putpalette(palette)
        # The WMR front row has two adjacent views without the legacy 1px gutter.
        fixed = Image.new("P", (image.width + 1, image.height), color=255)
        fixed.putpalette(palette)
        fixed.paste(image.crop((0, 0, 131, image.height)), (0, 0))
        fixed.paste(image.crop((131, 0, image.width, image.height)), (132, 0))
        fixed_path = folder / "legacy_fixed.png"
        fixed.save(fixed_path)
        image_path = fixed_path

    extractor = SpritesheetExtractor(str(image_path), palette)
    rows = extractor.extract_spritesets()
    by_y = {row.y: row for row in rows}
    selected = [by_y[y] for y in wanted_rows]
    cleaned = converter._rebuild_clean_sheet(extractor, selected)
    cleaned.save(target)
    print(f"{vehicle}: wrote {len(selected)} ordered vehicle rows to {target}")
