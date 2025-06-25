import argparse
from resume_analyzer import ResumeAnalyzer
import sys


def main():
    parser = argparse.ArgumentParser(description="Resume Analyzer CLI - Analyze your resume PDF for key skills and suggestions.")
    parser.add_argument('pdf', type=str, help='Path to your resume PDF file')
    args = parser.parse_args()

    analyzer = ResumeAnalyzer()
    text = analyzer.extract_text_from_pdf(args.pdf)
    if not text:
        print("[ERROR] Could not extract text from PDF.")
        sys.exit(1)
    skill_counts, total_mentions = analyzer.analyze_skills(text)
    suggestions = analyzer.generate_suggestions(skill_counts, text)
    skill_score = analyzer.skill_score(skill_counts)

    print("\n=== Skill Analysis Report ===")
    print(f"Total Skill Mentions: {total_mentions}")
    print(f"Skill Categories Found: {len(skill_counts)}")
    print(f"Skill Coverage Score: {skill_score:.1f}%\n")

    if skill_counts:
        for category, skills in skill_counts.items():
            print(f"[{category}]")
            for skill, count in sorted(skills.items(), key=lambda x: x[1], reverse=True):
                print(f"  - {skill.title()}: {count} mention{'s' if count > 1 else ''}")
            print()
    else:
        print("No technical skills found in the resume.\n")

    print("=== Improvement Suggestions ===")
    if suggestions:
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion['type']}: {suggestion['description']}")
    else:
        print("Excellent! No major improvements needed.")

if __name__ == "__main__":
    main() 