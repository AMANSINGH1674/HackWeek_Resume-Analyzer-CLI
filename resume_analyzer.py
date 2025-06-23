import re
from pathlib import Path
import streamlit as st
import tempfile

try:
    import fitz  # PyMuPDF
except ImportError:
    st.error("Error: PyMuPDF not installed. Run: pip install PyMuPDF")
    st.stop()


class ResumeAnalyzer:
    def __init__(self):
        # Comprehensive skill keywords database
        self.skill_categories = {
            'Programming Languages': [
                'python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby', 'go', 
                'rust', 'swift', 'kotlin', 'typescript', 'scala', 'r', 'matlab',
                'perl', 'shell', 'bash', 'powershell'
            ],
            'Web Technologies': [
                'html', 'css', 'react', 'angular', 'vue', 'node.js', 'nodejs',
                'express', 'django', 'flask', 'laravel', 'spring', 'asp.net',
                'jquery', 'bootstrap', 'sass', 'less', 'webpack', 'rest api',
                'graphql', 'soap'
            ],
            'Databases': [
                'sql', 'mysql', 'postgresql', 'mongodb', 'sqlite', 'oracle',
                'redis', 'elasticsearch', 'cassandra', 'dynamodb', 'neo4j',
                'mariadb', 'sql server'
            ],
            'Cloud & DevOps': [
                'aws', 'azure', 'gcp', 'google cloud', 'docker', 'kubernetes',
                'jenkins', 'git', 'github', 'gitlab', 'ci/cd', 'terraform',
                'ansible', 'chef', 'puppet', 'vagrant', 'linux', 'unix'
            ],
            'Data Science & ML': [
                'machine learning', 'deep learning', 'tensorflow', 'pytorch',
                'scikit-learn', 'pandas', 'numpy', 'matplotlib', 'seaborn',
                'jupyter', 'data analysis', 'statistics', 'nlp', 'computer vision',
                'ai', 'artificial intelligence', 'neural networks'
            ],
            'Mobile Development': [
                'ios', 'android', 'react native', 'flutter', 'xamarin',
                'swift', 'objective-c', 'kotlin', 'java'
            ],
            'Tools & Frameworks': [
                'visual studio', 'intellij', 'eclipse', 'sublime', 'vim',
                'postman', 'jira', 'confluence', 'slack', 'trello', 'agile',
                'scrum', 'kanban'
            ]
        }
        
        # Industry-specific keywords
        self.industry_keywords = {
            'Software Engineering': [
                'software development', 'full stack', 'backend', 'frontend',
                'microservices', 'api development', 'code review', 'debugging',
                'testing', 'unit testing', 'integration testing'
            ],
            'Data Science': [
                'data mining', 'predictive modeling', 'statistical analysis',
                'data visualization', 'big data', 'etl', 'data pipeline',
                'business intelligence', 'analytics'
            ],
            'DevOps': [
                'infrastructure', 'deployment', 'monitoring', 'automation',
                'scalability', 'performance optimization', 'security'
            ]
        }

    def extract_text_from_pdf(self, pdf_path):
        """Extract text content from PDF file."""
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text.lower()  # Convert to lowercase for matching
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
            return ""

    def analyze_skills(self, text):
        """Analyze text for skill mentions and count occurrences."""
        skill_counts = {}
        total_mentions = 0
        
        for category, skills in self.skill_categories.items():
            category_counts = {}
            for skill in skills:
                # Use word boundaries for accurate matching
                pattern = r'\b' + re.escape(skill.lower()) + r'\b'
                matches = len(re.findall(pattern, text))
                if matches > 0:
                    category_counts[skill] = matches
                    total_mentions += matches
            
            if category_counts:
                skill_counts[category] = category_counts
        
        return skill_counts, total_mentions

    def generate_suggestions(self, found_skills, text):
        """Generate improvement suggestions based on missing keywords."""
        suggestions = []
        
        # Check for missing high-demand skills
        missing_critical = []
        critical_skills = [
            'python', 'sql', 'git', 'javascript', 'react', 'aws', 'docker',
            'machine learning', 'data analysis', 'agile'
        ]
        
        for skill in critical_skills:
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if not re.search(pattern, text):
                missing_critical.append(skill)
        
        if missing_critical:
            suggestions.append({
                'type': 'Missing Critical Skills',
                'description': f"Consider adding these high-demand skills: {', '.join(missing_critical[:5])}"
            })
        
        # Check skill diversity
        categories_found = len(found_skills)
        if categories_found < 3:
            suggestions.append({
                'type': 'Skill Diversity',
                'description': 'Expand skill categories. Include more diverse technical skills.'
            })
        
        # Check for specific improvements
        if 'cloud' not in text and 'aws' not in text and 'azure' not in text:
            suggestions.append({
                'type': 'Cloud Skills',
                'description': 'Add cloud platform experience (AWS, Azure, GCP)'
            })
        
        if 'test' not in text:
            suggestions.append({
                'type': 'Testing Skills',
                'description': 'Mention testing experience (unit testing, integration testing)'
            })
        
        # Soft skills check
        soft_skills = ['leadership', 'communication', 'teamwork', 'problem solving']
        found_soft = [skill for skill in soft_skills if skill in text]
        if len(found_soft) < 2:
            suggestions.append({
                'type': 'Soft Skills',
                'description': 'Include more soft skills (leadership, communication, teamwork)'
            })
        
        return suggestions

    def skill_score(self, skill_counts):
        unique_skills_found = sum(len(skills) for skills in skill_counts.values())
        return min(100, (unique_skills_found / 30) * 100)  # Cap at 100%

def main():
    st.title("Resume Analyzer (Advanced)")
    st.write("Upload your resume in PDF format to analyze key skill mentions and get improvement suggestions.")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        analyzer = ResumeAnalyzer()
        text = analyzer.extract_text_from_pdf(tmp_path)
        if not text:
            st.error("Could not extract text from PDF.")
            return
        skill_counts, total_mentions = analyzer.analyze_skills(text)
        suggestions = analyzer.generate_suggestions(skill_counts, text)
        skill_score = analyzer.skill_score(skill_counts)

        st.subheader("Skill Analysis Report")
        st.write(f"**Total Skill Mentions:** {total_mentions}")
        st.write(f"**Skill Categories Found:** {len(skill_counts)}")
        st.write(f"**Skill Coverage Score:** {skill_score:.1f}%")

        if skill_counts:
            for category, skills in skill_counts.items():
                st.markdown(f"**{category}**")
                for skill, count in sorted(skills.items(), key=lambda x: x[1], reverse=True):
                    st.write(f"- {skill.title()}: {count} mention{'s' if count > 1 else ''}")
        else:
            st.info("No technical skills found in the resume.")

        st.subheader("Improvement Suggestions")
        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                st.write(f"{i}. **{suggestion['type']}**: {suggestion['description']}")
        else:
            st.success("Excellent! No major improvements needed.")

if __name__ == "__main__":
    main()