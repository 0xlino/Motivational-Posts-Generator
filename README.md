# Motivational Posts Generator Python

#### Avoid using the tool to spam or create undesirable content on the internet.

## Overview

This Python script provides functionality to overlay quotes on images, along with additional features like applying a tint to the image, adding a trademark or logo, and resizing images. It's designed to create visually appealing quote images, suitable for sharing on social media or other platforms.

## Features

- **Random Quote Selection:** Extracts a random quote from a provided text file.
- **Image Checking:** Determines whether a file is an image (supports JPG, PNG, JPEG).
- **Trademark Placement:** Adds a trademark text inside the image.
- **Tint Application:** Applies a color tint to the image.
- **Logo Placement:** Supports adding a logo image to the quote image.
- **Quote Placement:** Offers two options for placing quotes - at the top or in the center of the image.
- **Final Image Creation:** Combines all features to build the final image with a quote, optionally including a logo and trademark.

## Usage

1. **Prepare Input Files:**
   - Place image files in `in/raw`.
   - Add quotes in `in/quotes.txt`.
   - Store logos in `in/author_images` with author names as filenames.

2. **Configuration:**
   - Set the path for input and output directories.
   - Customize fonts and sizes as needed.

3. **Running the Script:**
   - Execute the script.
   - Choose to generate all combinations or specific pairings of images and quotes.
   - Opt to include a trademark/logo as desired.

4. **Output:**
   - Final images are saved in the `out` directory.
   - Each image is named using a combination of quote and image identifiers.

## Dependencies

- Python 3.x
- PIL (Python Imaging Library)

## Notes

- The script is intended for positive and creative use.
- Avoid using the tool to spam or create undesirable content on the internet.
---