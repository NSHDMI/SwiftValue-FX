# SwiftValue

A lightweight and responsive desktop currency converter built with Python and Tkinter. 
It uses real-time data from the ExchangeRate-API to provide accurate conversion between 150+ world currencies.

---

## Features

* Real-time Rates: Fetches the latest exchange rates via API.
* Multi-threading: The UI remains responsive during network requests (no freezing).
* Smart UI: Clean dark-themed interface with keyboard shortcuts (Enter to convert).
* Safety: Uses environment variables to protect sensitive API keys.

---
## Preview
![photo_2026-01-31_20-35-57](https://github.com/user-attachments/assets/bf3197cb-fd66-4a15-a5df-df582cc89f39)
---
## Installation

1.  Clone the repository:
  ```
  git clone [https://github.com/NSHDMI/Applications-Exchange.git](https://github.com/NSHDMI/Applications-Exchange.git)

  cd Applications-Exchange
  ```

4.  Install dependencies:
        ```pip install -r requirements.txt```
    

5.  Set up the API key:
    * Get a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/).
    * Create a .env file in the project root.
    * Add the following line:
                ```EXCHANGE_API_KEY=your_actual_key_here```
        

6.  Run the application:
        ```python Exchange.py```
    

---

## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-gray?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-orange?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

---

## License

This project is open-source and distributed under the MIT License.  
You are free to use, modify, and distribute it.

---

## Contributing

Pull requests and suggestions are welcome!  
If you find a bug or have an idea for improvement, feel free to open an issue.

Developed by [NSHDMI](https://github.com/NSHDMI)
