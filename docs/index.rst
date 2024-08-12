.. Brainfuck Art documentation master file, created by
   sphinx-quickstart on Sat Aug 11 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Brainfuck Art's documentation!
==========================================



.. image:: https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue
   :alt: Python Versions

.. image:: https://github.com/pablomm/brainfuck-art/actions/workflows/tests.yml/badge.svg
   :alt: Test Status

.. image:: https://readthedocs.org/projects/brainfuck-art/badge/?version=latest
    :target: https://brainfuck-art.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://img.shields.io/pypi/v/brainfuck_art.svg
   :target: https://pypi.org/project/brainfuck_art/
   :alt: PyPI version

      

**Brainfuck Art** is a Python library developed as a hobby project for generating images with hidden Brainfuck code. Inspired by `htmlfuck <https://github.com/pablomm/htmlfuck>`_, the library provides functionality to encode text into Brainfuck, convert images to ASCII art, and export the output in HTML, SVG, or PDF formats.

.. image:: https://raw.githubusercontent.com/pablomm/brainfuck-art/main/docs/assets/coffee.svg
   :alt: Coffee Example
   :target: https://raw.githubusercontent.com/pablomm/brainfuck-art/main/docs/assets/coffee.svg



Example
-------

You can download this example as a PDF: `Coffee PDF <https://github.com/pablomm/brainfuck-art/blob/main/docs/assets/coffee.pdf?raw=True>`_. Copy the content (Ctrl+A) and paste it into a Brainfuck interpreter like `this one <https://copy.sh/brainfuck/>`_ to recover the hidden content.


Features
--------

- **Text to Brainfuck**: Convert any text into Brainfuck code.
- **ASCII Art Generation**: Transform images into color blocks.
- **Multiple Output Formats**: Export your creations as HTML, SVG, or PDF.
- **Command-Line Interface (CLI)**: Generate and export art from the terminal.
- **Python API**: Integrate Brainfuck Art into your Python projects with ease.

Installation
------------

To install Brainfuck Art, ensure you have Python 3.9 or higher, and run:

.. code-block:: bash

   pip install brainfuck_art

Command-Line Usage
------------------

You can use Brainfuck Art directly from the command line to create art with hidden Brainfuck code:

.. code-block:: bash

   # Download the example image
   curl -L -o coffee.png https://github.com/pablomm/brainfuck-art/blob/main/docs/assets/coffee.png\?raw\=true

   # Generate Art with hidden text
   brainfuck-art coffee.png -t "I love coffee" -o "coffee.pdf" -W 100 -H 100

Main Options
------------

- `-t`, `--text`: Text to encode as Brainfuck code.
- `-o`, `--output`: The output file name (with extension).
- `-W`, `--width`: Width of the output in characters.
- `-H`, `--height`: Height of the output in characters.
- `-f`, `--filetype`: File type for output (html, svg, pdf).

Python API Usage
----------------

You can also use Brainfuck Art as a Python package to programmatically generate Brainfuck code, interpret it, and create visual art.

Generate Brainfuck Code
-----------------------

.. code-block:: python

   from brainfuck_art import text_to_bf

   code = text_to_bf("brainfuck")
   print(code)

Example output:

.. code-block:: none

   '>+++++++[>++++++++++++++<-]>.<++++[>++++<-]>.<++++[>----<-]>-.++++++++.+++++.--------.+++++++++++++++.<+++[>------<-]>.++++++++.'

Execute Brainfuck Code
----------------------

.. code-block:: python

   from brainfuck_art import execute_bf

   output, tape = execute_bf(code)
   print(output)  # Outputs: brainfuck

Generate ASCII Art with Hidden Text
-----------------------------------

.. code-block:: python

   from brainfuck_art import image_to_matrix, save_matrix_to_svg

   text = "I love coffee"
   text_matrix, color_matrix = image_to_matrix("coffee.png", text=text)
   save_matrix_to_svg(text_matrix, color_matrix, output_file="coffee.svg")

You can also save the output in PDF or HTML formats using the same approach.

License
-------

Brainfuck Art is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

