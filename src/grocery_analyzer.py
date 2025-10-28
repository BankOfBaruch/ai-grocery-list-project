import csv
import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="YOUR_ACTUAL_GEMINI_API_KEY_HERE")

# Define the file path for the grocery list CSV
filePath = ("PATH_TO_YOUR_GROCERY_LIST_CSV_FILE")


def readCsvData(filePath):
    """
    Reads data from a CSV file and returns it as a list of dictionaries.

    Args:
        filePath (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the CSV.
              Keys are column headers, and values are the corresponding row values.
    """
    with open(filePath, 'r', newline='') as file:
        # Create a DictReader object to read the CSV as dictionaries
        reader = csv.DictReader(file)
        # Convert each row to a dictionary and return as a list
        return [dict(row) for row in reader]


def promptGenerator(groceryList):
    promptList = []

    for item in groceryList:
        # Create a structured string with nutritional info
        item_info = "\n".join(
            # creates a string that contains the key and value of each item in the dictionary
            [f"{key}: {value}" for key, value in item.items()])

        prompt = {
            "Prompt": f"Based on the following food item and nutritional info, "
            f"is it diabetic friendly? Give a definite 'yes' or 'no' response "
            f"and provide reasoning in 200 words or less.\n\n{item_info}"
        }
        promptList.append(prompt)  # adds the prompt to the list

    return promptList


def getGeminiResponse(promptList):
    model = genai.GenerativeModel(
        "gemini-2.5-pro-preview-03-25")  # specifies the model to use

    responses = []
    for prompt in promptList:
        # sends the prompt to the model
        response = model.generate_content(prompt["Prompt"])
        responses.append(response.text)  # adds the response to the list

    return responses


def parseGeminiResponse(response):
  
    lines = response.split("\n")  # splits the response into lines
    verdict = "Unknown"  # sets the default value
    reasoning = ""  # sets the default value

    for line in lines:
        if "Yes" in line or "No" in line:
            verdict = line.strip()  # sets the verdict to the line that contains yes or no
        else:
            reasoning += line + " "  # adds the line to the reasoning string

    return verdict, reasoning.strip()  # returns the verdict and reasoning


def main():
    """
    Main function to orchestrate the grocery item analysis.
    Reads the grocery list, generates prompts, gets responses from Gemini,
    parses the responses, and prints the results.
    """
    groceryList = readCsvData(filePath)  # reads the csv file
    groceryPrompt = promptGenerator(groceryList)  # creates the prompt list

    # gets the responses from gemini
    responses = getGeminiResponse(groceryPrompt)

    # loops through the items and responses
    for item, response in zip(groceryList, responses):
        verdict, reasoning = parseGeminiResponse(
            response)  # parses the response
        print(f"Item: {item['Item']}")  # prints the item name
        print(f"Diabetic Friendly?: {verdict}")  # prints the verdict
        print(f"Reasoning: {reasoning}")  # prints the reasoning
        print("-" * 50)  # prints a line to separate the items


if __name__ == "__main__":
    main()
