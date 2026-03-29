def generate_report(topic, content):
    report = f"""
==============================
        COVER PAGE
==============================
Title: {topic}
Author: Autonomous Research Agent

==============================
        INTRODUCTION
==============================
{content[:500]}

==============================
        KEY FINDINGS
==============================
- Extracted insights from research

==============================
        CHALLENGES
==============================
- Data reliability
- Bias in AI models

==============================
        FUTURE SCOPE
==============================
- More automation
- Better accuracy

==============================
        CONCLUSION
==============================
AI-driven research agents can automate knowledge discovery efficiently.
"""
    return report