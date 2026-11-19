# Raw Data Documentation & Provenance

## Survey on Digital Learning Tools Usage Among College Students

### 1. Data Collection Details
- **Methodology**: Primary data collection via structured online survey (Google Forms).
- **Target Population**: College undergraduate and postgraduate students.
- **Collection Window**: August 21, 2026 – September 7, 2026.
- **Geographic Focus**: Ahmednagar (Ahilyanagar), Maharashtra, India (centered at New Arts, Commerce and Science College, Autonomous).
- **Sample Size ($N$)**: 69 verified responses across 22 recorded attributes.

### 2. File Manifest
- `survey_data_raw.xlsx`: Original survey response matrix in Microsoft Excel format.
- `survey_data_raw.csv`: Raw survey response matrix in UTF-8 CSV format.

### 3. Data Privacy & Ethical Compliance (PII Redaction)
In strict accordance with academic ethics and data privacy standards (GDPR / Data Protection principles):
- All respondent full names have been replaced with anonymous identifiers (`Respondent_01` through `Respondent_69`).
- Timestamp, course, age, and academic answers remain 100% authentic and unmodified.
- No email addresses, phone numbers, or private student IDs were published.

### 4. Raw Attributes Overview
Each response contains:
1. `sno`: Response index (1 to 69).
2. `submitted_time`: Form submission timestamp.
3. `name`: De-identified participant code.
4. `age`: Participant age (range 18–26).
5. `gender`: Gender identity (Male, Female, Other).
6. `year_of_study`: Academic stream and year.
7. `uses_tools`: Digital learning tool adoption status (Yes / No).
8. `tools_used`: Pipe-delimited list of digital platforms utilized.
9. `frequency`: Usage frequency level.
10. `time_per_day`: Daily study time spent on tools.
11. `helpfulness`: Perceived academic utility.
12. `main_benefit`: Primary perceived learning benefits (multi-select).
13. `biggest_advantage`: Single most valued advantage.
14. `problem_faced`: Major friction point or barrier encountered.
15. `device`: Primary hardware platform used.
16. `access_location`: Primary study environment.
17. `most_useful_tools`: Specific tools rated as highest value (multi-select).
18. `accuracy_rating`: Trust and reliability perception.
19. `overall_experience`: Holistic satisfaction rating.
20. `costlier_learning_type`: Mode of learning perceived as more expensive.
21. `cost_comparison`: Perception of digital tool cost vs. traditional offline education.
22. `ai_purpose`: Primary academic workflow supported by AI tools.
