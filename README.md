# DotSense: A 3D-Printed Refreshable Text-to-Braille Translator Device

DotSense is a physical text-to-Braille translation device designed to make digital and printed text accessible through touch. The system combines a Python-based application with an ESP32-controlled mechanism that raises and lowers Braille dots using four servo motors.

The device uses a 3D-printed enclosure and a cam-based mechanism to create **two refreshable Braille cells**. The enclosure and mechanical design files are not included in this repository.

## Publication

This project is published on IEEE Xplore: [Paper](https://ieeexplore.ieee.org/abstract/document/11253646/)
Please refer to the publication for the project's research context and further technical details.

## Repository Structure

```text
DotSense/
├── App/
│   └── Python application and text-processing components
└── ESP32/
    └── ESP32 firmware and servo-control components
```

### `App/`

Contains the application, developed with [Flet](https://flet.dev/), and the text-processing components used to prepare content for Braille translation.

Technologies and libraries include:

- **Flet**: application interface.
- **pdfplumber**: text extraction from PDF documents.
- **pytesseract**: OCR (optical character recognition) for extracting text from images or scanned documents, when supported by the application workflow.

### `ESP32/`

Contains the ESP32-side code responsible for controlling the physical device. The ESP32 coordinates **four servo motors operating in parallel** to actuate the cam mechanism and display the Braille patterns on the two cells.

## How It Works

At a high level, the system follows this workflow:

1. **Input text:** The user provides text through the application or a supported document.
2. **Text extraction:** The application extracts text from supported PDFs and, where applicable, scanned or image-based content using OCR.
3. **Text-to-Braille conversion:** The text is prepared as Braille patterns for physical output.
4. **Device control:** The application communicates the required output to the ESP32.
5. **Tactile display:** The ESP32 controls the servo motors and cam mechanism to raise the corresponding dots on the two Braille cells. The user reads the output by touch, and the cells can be refreshed to display subsequent patterns.

## Hardware Overview

- ESP32 microcontroller.
- Four servo motors, controlled in parallel.
- Cam-based mechanism for actuating the Braille dots.
- Two refreshable Braille cells.
- 3D-printed enclosure.

The 3D-printable enclosure and mechanical files are not included in this repository.

## Requirements

The application is Python-based and uses Flet, pdfplumber, and pytesseract. Additional dependencies may be required by the current source code.

- Python
- Flet
- pdfplumber
- pytesseract
- Tesseract OCR engine

## Project Scope and Limitations

- DotSense is a prototype for tactile text-to-Braille output.
- The display consists of two refreshable Braille cells.
- The 3D-printed enclosure and mechanical design files are not distributed in this repository.
- OCR results can vary depending on document quality, layout, and image clarity.


## Citation

If you use or discuss this project in academic work, please cite the associated publication:
- [IEEE Xplore publication](https://ieeexplore.ieee.org/abstract/document/11253646/)
