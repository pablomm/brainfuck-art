from typing import Union
import numpy as np
from pathlib import Path

def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color string to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb: tuple) -> str:
    """Convert an RGB tuple to a hex color string."""
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

def luminance(rgb: tuple) -> float:
    """Calculate the luminance of an RGB color."""
    r, g, b = rgb
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def adjust_color_brightness(rgb: tuple, factor: float) -> tuple:
    """
    Adjust the brightness of an RGB color.
    
    :param rgb: The original RGB color as a tuple.
    :param factor: Factor to adjust brightness by (greater than 1 to lighten, between 0 and 1 to darken).
    :return: A new RGB tuple with adjusted brightness.
    """
    return tuple(min(max(int(c * factor), 0), 255) for c in rgb)

def get_contrasting_text_color(hex_color: str, darken_factor: float = 0.7, lighten_factor: float = 1.3) -> str:
    """
    Determine a darker or lighter color for the text based on the background color.
    
    :param hex_color: The hex color string of the background.
    :param darken_factor: Factor to darken the text color if the background is light.
    :param lighten_factor: Factor to lighten the text color if the background is dark.
    :return: A hex color string for the adjusted text color.
    """
    rgb = hex_to_rgb(hex_color)
    lum = luminance(rgb)

    if lum > 128:  # Light background, darken the text
        adjusted_rgb = adjust_color_brightness(rgb, darken_factor)
    else:  # Dark background, lighten the text
        adjusted_rgb = adjust_color_brightness(rgb, lighten_factor)

    return rgb_to_hex(adjusted_rgb)

def save_matrix_to_html(
    text_matrix: np.ndarray,
    color_matrix: np.ndarray,
    output_file: Union[str, Path],
    font_size: int = 10,
    line_height_ratio: float = 1.0,
    darken_factor: float = 0.7,
    lighten_factor: float = 1.3
) -> None:
    """
    Generates an HTML file displaying the text matrix with colors from the color matrix,
    adjusting the text color to be a darker or lighter version of the background color.
    
    :param text_matrix: A 2D NumPy array of characters representing the text.
    :param color_matrix: A 2D NumPy array of hex color strings.
    :param output_file: The file path where the HTML file will be saved.
    :param font_size: The font size to use in the HTML output.
    :param line_height_ratio: The ratio of line-height to font-size to adjust the aspect ratio (default is 1).
    :param darken_factor: Factor to darken the text color if the background is light.
    :param lighten_factor: Factor to lighten the text color if the background is dark.
    """
    output_file = Path(output_file)

    # Start building the HTML content
    html_content = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "<meta charset='UTF-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        "<title>Text and Color Matrix</title>",
        "<style>",
        f".matrix {{ font-family: monospace; font-size: {font_size}px; line-height: {line_height_ratio}; white-space: pre; }}",
        "</style>",
        "</head>",
        "<body>",
        "<div class='matrix'>"
    ]

    for row_idx in range(text_matrix.shape[0]):
        row_html = []
        current_color = None
        buffer = []

        for col_idx in range(text_matrix.shape[1]):
            char = text_matrix[row_idx, col_idx]
            color = color_matrix[row_idx, col_idx]
            text_color = get_contrasting_text_color(color, darken_factor, lighten_factor)

            if color != current_color:
                if buffer:
                    # Flush the buffer for the previous color and text color
                    row_html.append(f"<span style='color:{text_color}; background-color:{current_color}'>{''.join(buffer)}</span>")
                buffer = [char]
                current_color = color
            else:
                buffer.append(char)

        # Flush the last buffer
        if buffer:
            row_html.append(f"<span style='color:{text_color}; background-color:{current_color}'>{''.join(buffer)}</span>")

        html_content.append(''.join(row_html))
        html_content.append("<br>")  # Add a line break after each row

    # Close the HTML tags
    html_content.extend([
        "</div>",
        "</body>",
        "</html>"
    ])

    # Write the HTML content to the output file
    with output_file.open('w') as f:
        f.write(''.join(html_content))

# Example usage:
# text_matrix = np.array([['A', 'B'], ['C', 'D']])
# color_matrix = np.array([['#ff0000', '#00ff00'], ['#0000ff', '#ffff00']])
# save_matrix_to_html(text_matrix, color_matrix, 'output.html')
