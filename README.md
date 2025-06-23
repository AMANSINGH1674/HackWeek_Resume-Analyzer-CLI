# Resume Analyzer CLI & Web App

A Python tool to analyze PDF resumes for key technical skills and provide improvement suggestions. Use it as a command-line tool or a Streamlit web app.

## Features
- Extracts text from PDF resumes
- Detects and counts mentions of a wide range of tech skills
- Categorizes skills (Programming, Web, Cloud, Data Science, etc.)
- Suggests improvements based on missing or underrepresented keywords
- Provides a skill coverage score
- Usable via CLI or Streamlit web interface

## Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/AMANSINGH1674/HackWeek_Resume-Analyzer-CLI.git
   cd HackWeek_Resume-Analyzer-CLI
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)
Run the analyzer on a PDF resume:
```sh
python resume_analyzer.py path/to/your_resume.pdf
```

### Streamlit Web App
Launch the web interface:
```sh
streamlit run resume_analyzer.py
```
Then open the provided local URL in your browser, upload a PDF, and view the analysis.

## Example Output
- Skill mentions by category
- Suggestions for missing skills
- Skill coverage score

## Requirements
- Python 3.7+
- PyMuPDF
- Streamlit

## License
MIT 