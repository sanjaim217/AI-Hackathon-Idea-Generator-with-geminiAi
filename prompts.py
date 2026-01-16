def hackathon_prompt(domain, level, users):
    return f"""
Generate a unique hackathon project idea.

Domain: {domain}
Difficulty Level: {level}
Target Users: {users}

Include:
1. Project Title
2. Problem Statement
3. Proposed Solution
4. Key Features
5. Tech Stack
6. Innovation Factor
"""
