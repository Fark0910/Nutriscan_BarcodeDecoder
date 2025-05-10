# NutriScan Barcode Decoder

NutriScan Barcode Decoder is a Python-based backend module designed to receive barcode images from the ESP32-CAM device, decode them, and retrieve detailed product information using external APIs. This module plays a crucial role in determining the nutritional suitability of scanned food items.

---

## 📦 Repository Contents

- `main.py` – Core script handling image reception, barcode decoding, and API communication.
- `start.sh` – Shell script to initiate the backend server.
- `requirement.txt` – Lists all Python dependencies required for the project.
- `.gitignore` – Specifies files and directories to be ignored by Git.

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Libraries & Tools:**
  - `Dynamsoft Barcode Reader` – For accurate barcode decoding from images.
  - `requests` – To handle HTTP requests to external APIs.
  - `Flask` or `FastAPI` (assumed) – For setting up the backend server.
- **Deployment:** Can be hosted on platforms like Render or Heroku for seamless integration with the ESP32-CAM device.

---
# NutriScan Barcode Decoder

🔗 **Live API Endpoint:** [https://barcodedecoder.onrender.com](https://barcodedecoder.onrender.com)

## 🔧 Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Fark0910/Nutriscan_BarcodeDecoder.git
   cd Nutriscan_BarcodeDecoder
