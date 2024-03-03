## Gemini SQL Query Retrieval App

The Gemini SQL Query Retrieval App is a Streamlit web application designed to facilitate the generation of SQL queries from English questions. This app leverages the Google Gemini model from `google.generativeai` to convert user-provided questions into SQL commands, allowing for seamless interaction with a SQLite database.

### How It Works

1. Gemini Model Integration:
   - The app integrates the Gemini model using the `genai` library to transform English questions into SQL queries.
   - An API key, stored securely in a `.env` file and loaded using `dotenv`, configures the access to the Gemini model.

2. SQL Query Execution:
   - Upon user input of a question, the app sends this question along with a predefined prompt to the Gemini model.
   - The `get_gemini_response` function fetches the generated SQL query from the model based on the question.
   - This SQL query is then executed on a SQLite database named "student.db" using the `read_sql_query` function.

3. Streamlit User Interface:
   - The Streamlit interface displays a header introducing the app as a "Gemini App To Retrieve SQL Data".
   - Users interact by inputting questions into a text input field and clicking the "Ask the question" button.
   - Upon submission, the app retrieves the SQL query using Gemini, executes it on the database, and displays the resulting data.

### Features

- Question Input: Users can input English questions related to a predefined SQL database structure.
- SQL Query Generation: The Gemini model generates SQL queries based on the user's question.
- Database Interaction: Queries are executed on the SQLite database to retrieve relevant data.
- Streamlit Display: Results are presented in a Streamlit interface, providing an intuitive and interactive user experience.

### Usage

1. Getting Started:
   - Ensure the required Python packages (`transformers`, `sacrebleu`, `py7zr`, `transformers`, `datasets`, `torch`, `pandas`, `matplotlib`, `nltk`, `tqdm`) are installed.
   - Configure the API key for the Gemini model in a `.env` file.

2. Running the App:
   - Execute the script in a Python environment.
   - Access the Streamlit web interface on the specified local server.

### Example

- User Input: "How many students are in the Data Science class?"
- Generated SQL Query: `SELECT COUNT(*) FROM STUDENT WHERE CLASS='Data Science';`
- Result Display: The app displays the count of students in the Data Science class.

The Gemini SQL Query Retrieval App streamlines the process of converting English questions into SQL queries, making database interactions more intuitive and accessible for users.
