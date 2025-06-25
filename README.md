# Resume Analyzer CLI & Web App

**Try it instantly online:** [resumeanalyzercli-aman.streamlit.app](https://resumeanalyzercli-aman.streamlit.app/)

A Python tool to analyze PDF resumes for key technical skills and provide improvement suggestions. Use it as a command-line tool, a Streamlit web app locally, or try it online.

## Features
- Extracts text from PDF resumes
- Detects and counts mentions of a wide range of tech skills
- Categorizes skills (Programming, Web, Cloud, Data Science, etc.)
- Suggests improvements based on missing or underrepresented keywords
- Provides a skill coverage score
- Usable via CLI, Streamlit web interface, or online

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

### Online (Recommended)
No installation needed! Just visit:
[https://resumeanalyzercli-aman.streamlit.app/](https://resumeanalyzercli-aman.streamlit.app/)

### Command-Line Interface (CLI)
Run the analyzer on a PDF resume:
```sh
python resume_analyzer_cli.py "/path/to/your resume.pdf"
```

- Make sure to wrap the file path in quotes if it contains spaces.
- The CLI will print skill mentions, categories, score, and suggestions directly to your terminal.

### Streamlit Web App (Local)
Launch the web interface locally:
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