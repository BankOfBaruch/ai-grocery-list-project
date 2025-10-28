# Grocery Analyzer: Diabetic Dietary Advisor

## Project Overview

This project is a Python-based script designed to analyze grocery items and their nutritional values against dietary guidelines for diabetics. It leverages the **Gemini 2.5 Pro API** to provide detailed, item-specific feedback on whether a food item is diabetic-friendly and the reasoning behind the recommendation.

This project showcases skills in data processing, API integration, and leveraging large language models (LLMs) for specialized analysis.

## Key Features

* **CSV Data Ingestion:** Reads and processes a structured CSV file (`Grocery_List.csv`) containing nutritional information (Calories, Carbohydrates, Sugar, etc.).
* **Gemini API Integration:** Dynamically generates prompts for the Gemini 2.5 Pro model, sending nutritional data for analysis.
* **Diabetic Suitability Analysis:** The Gemini model provides a definitive "Yes" or "No" verdict on the item's diabetic friendliness, along with a detailed explanation (Source 4, 5).
* **Structured Output:** Parses the AI's response to extract the verdict and reasoning for clear, itemized output (Source 7).

## Technology Stack

* **Language:** Python 3
* **Libraries:** `csv`, `google-genai` (for the Gemini API), `pandas` (optional, but good for data manipulation)
* **API:** Google Gemini 2.5 Pro (Model: `gemini-2.5-pro-preview-03-25`) (Source 6)
* **Data Format:** CSV

## ⚙️ How to Run the Script

### Prerequisites

1.  **Python:** Ensure you have Python 3.x installed.
2.  **API Key:** Obtain a Gemini API key from Google AI Studio.

### Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/Grocery-Analyzer.git](https://github.com/YourUsername/Grocery-Analyzer.git)
    cd Grocery-Analyzer
    ```

2.  **Install Dependencies:**
    ```bash
    pip install google-genai
    # (If you add any libraries like pandas later, install them here)
    ```

3.  **Set Your API Key:**
    The script currently hardcodes the API key for demonstration purposes (Source 1).

    *To run the current script:* **Replace the placeholder key** in `grocery_analyzer.py` with your actual API key:
    ```python
    genai.configure(api_key="YOUR_ACTUAL_GEMINI_API_KEY_HERE")
    ```
     **For production use, you should set your API key as an environment variable.**
    # macOS / Linux
    ```bash
    export GEMINI_API_KEY="your_api_key_here"

    # Windows (PowerShell)
    $env:GEMINI_API_KEY = "your_api_key_here"


4.  **Execute the Script:**
    ```bash
    python grocery_analyzer.py
    ```

### Expected Output

The script will iterate through each item in the `Grocery_List.csv` and print the AI's analysis:

example:

Item: Ramen Noodles Diabetic Friendly?: No Reasoning: [Gemini's detailed explanation on why the item is not recommended for diabetics]
Item: Apple Diabetic Friendly?: Yes Reasoning: [Gemini's detailed explanation on why the item is recommended for diabetics]
... and so on for all items.