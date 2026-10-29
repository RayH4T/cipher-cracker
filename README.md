# Cipher Cracker

A Python-based brute-force tool for numeric Caesar-style ciphers.

## Features

- Brute-Force Decryption.
- Numeric Cipher Support.
- Test all 26 possible alphabet shifts.
- Colored terminal interface and loading animation.

## Project Structure

| File | Description |
| --- | --- |
| `ray_cracker.py` | Tests all 26 possible shifts. |

## Requirements

- Python 3
- Kali Linux, macOS, or another compatible terminal

## Installation

Clone the repository:

```bash
git clone https://github.com/RayH4T/cipher-cracker.git
cd ray-cracker
```

## Usage

Run Cipher Cracker:

```bash
python3 ray_cracker.py
```
1. Enter the numeric cipher code number you get from ray cipher tool.
2. Wait for the loading animation to finish.
3. Review the 26 possible decryption results.
4. Check the green-highlighted Shift results.
   
## Example

Input:

```text
15-12-19-19-22-0-4-22-25-19-11
```

Output:

```text
WHO IS RAY
```

## How It Works

Cipher Crack performs a brute-force search by trying every possible alphabet shift and displaying the resulting text for each candidate.

## Disclaimer

This project is for educational purposes only. It is not secure encryption and should not be used to protect confidential information.

## Author

RAYH4T

## License

No license has been specified yet.
