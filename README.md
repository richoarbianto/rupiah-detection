
# Rupiah Detection with Speech-to-Text Project

This project is an application designed to detect Rupiah banknotes, specifically aimed at aiding individuals with visual impairments. The program uses computer vision to detect the banknote denomination and then converts the detected value into speech.

## Features

- **Rupiah Banknote Detection**: Utilizes a machine learning model to recognize the banknote's denomination.
- **Text-to-Speech Conversion**: After detecting the denomination, the program announces it aloud via text-to-speech.
- **Easy to Use**: Simply run the script, and automatic detection begins.

## Requirements

- Tested with Python 3.11.x
- Required libraries are listed in `requirements.txt`

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/richoarbianto/rupiah-detection
   ```
2. Navigate to the project directory.
   ```bash
   cd rupiah-detection
   ```
3. Install all dependencies listed in `requirements.txt`.
   ```bash
   pip3 install -r requirements.txt
   ```

## Running the Program

After installation, you can start the program with the following command:
```bash
python3 main.py
```

The program will automatically begin detecting any recognized banknotes seen by the camera and will announce the denomination.

## Contribution

Contributions are highly welcome for improvements or new features. Please feel free to submit a pull request or start a discussion if you have ideas for development.

## License

This project is licensed under the [MIT License](LICENSE).

---

We hope this application assists visually impaired individuals in easily identifying Rupiah banknotes.
