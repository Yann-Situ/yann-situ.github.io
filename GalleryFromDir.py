#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import html
import os


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

ART_DIR = Path("images/art")
GALLERY_DIR = Path("_gallery")

CATEGORY = "visual"

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".avif",
}


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def is_image(path: Path) -> bool:
    """Return True if the file has a supported image extension."""
    return path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS


def creation_date(path: Path) -> str:
    """
    Get the filesystem creation date.

    On macOS/Windows, st_ctime is normally the creation time.
    On Linux, it may instead represent metadata-change time.
    """
    timestamp = path.stat().st_ctime
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def jekyll_path(path: Path) -> str:
    """
    Convert a local Path to a URL suitable for Jekyll.
    """
    return "/" + path.as_posix().lstrip("/")

from PIL import Image

def create_thumbnail(image_path: Path, output_path: Path):
    """Create a resized JPEG thumbnail."""

    with Image.open(image_path) as image:
        image = image.convert("RGB")

        # Don't enlarge small images
        image.thumbnail((800, 800), Image.Resampling.LANCZOS)

        image.save(
            output_path,
            "JPEG",
            quality=85,
            optimize=True
        )


def generate_post(directory: Path, images: list[Path]) -> str:
    """Generate the Markdown content for one gallery post."""

    dir_name = directory.name

    thumbnail_path = directory / "thumbnail.jpg"

    if not thumbnail_path.exists():
        create_thumbnail(images[0], thumbnail_path)

    # Creation date of the thumbnail
    date = creation_date(images[0])

    # Gallery HTML
    image_html = []

    for image in images:
        if image != thumbnail_path:
            image_url = jekyll_path(image)
            alt = html.escape(image.stem.replace("-", " ").replace("_", " "))

            image_html.append(
            f'''<figure class="gallery-image">
  <img
    src="{image_url}"
    alt="{alt}"
    loading="lazy">
</figure>'''
            )

    images_html = "\n\n".join(image_html)

    return f"""---
title: {dir_name}
layout: splash-title
collection: gallery
category: {CATEGORY}
permalink: /gallery/{dir_name}
thumbnail: {thumbnail_path}
date: {date}
columns: 2
---

<div class="gallery-post columns-{{{{ page.columns | default: 2 }}}}">
{images_html}
</div>
"""


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():
    if not ART_DIR.exists():
        print(f"Error: directory does not exist: {ART_DIR}")
        return

    # Create _gallery if necessary
    GALLERY_DIR.mkdir(parents=True, exist_ok=True)

    directories = sorted(
        path for path in ART_DIR.iterdir()
        if path.is_dir()
    )

    if not directories:
        print(f"No directories found in {ART_DIR}")
        return

    for directory in directories:

        images = sorted(
            path for path in directory.iterdir()
            if is_image(path)
        )

        if not images:
            print(f"Skipping {directory}: no images found")
            continue

        output_file = GALLERY_DIR / f"{directory.name}.md"

        content = generate_post(directory, images)

        output_file.write_text(
            content,
            encoding="utf-8"
        )

        print(
            f"Created {output_file} "
            f"({len(images)} image(s))"
        )


if __name__ == "__main__":
    main()
