# Data Dictionary: Digital Learning Tools Survey Dataset

**Dataset Name:** `survey_data_cleaned.csv` / `survey_data_raw.xlsx`  
**Total Observations ($N$):** 69 Validated Student Records  
**Total Attributes:** 22 Survey Attributes + 4 Derived Numerical Score Metrics  
**Collection Date:** August 21, 2026 – September 7, 2026  

---

## 1. Demographic & Identification Attributes

| Variable | Column Header in Raw Form | Data Type | Scale | Allowed Values / Categories | Description |
|:---|:---|:---:|:---:|:---|:---|
| `sno` | `S.NO` | Integer | Identifier | `1` to `69` | Unique serial response identifier. |
| `submitted_time` | `Submitted Time` | DateTime | Temporal | `YYYY-MM-DD HH:MM:SS` | Form submission timestamp. |
| `name` | `1. Full Name` | String | Identifier | `Respondent_01` – `Respondent_69` | De-identified student code (real names removed for PII protection). |
| `age` | `2. Age` | Integer | Ratio | `18` to `26` | Participant age in completed years. |
| `gender` | `3. Gender` | String | Nominal | `Male`, `Female`, `Other` | Self-reported gender identity. |
| `year_of_study` | `4. Year of study` | String | Nominal | `SY Data science`, `SY computer science`, `TY computer science`, `TY Data science`, `FY Data science`, `FY computer science`, `Other` | Academic course, discipline, and standing year. |

---

## 2. Adoption & Study Habit Attributes

| Variable | Column Header in Raw Form | Data Type | Scale | Allowed Values / Categories | Description |
|:---|:---|:---:|:---:|:---|:---|
| `uses_tools` | `5. Do you use digital learning tools for your studies?` | String | Binary | `Yes`, `No` | General adoption status of digital educational platforms. |
| `tools_used` | `6. Which digital learning tools do you use?` | String | Nominal (Multi-select) | `Youtube`, `ChatGPT/AI tools`, `Google Classroom`, `Cloude`, `Education apps`, `Google Meet`, `Zoom`, `Duolingo`, `Coursera`, `Udemy` | Digital platforms used (pipe-delimited `"\|"` multi-response). |
| `frequency` | `7. How frequently do you use digital learning tools?` | String | Ordinal | `Daily`, `4-6 days a week`, `2-3 days a week`, `Once a week`, `Rarely` | Frequency level of digital tool usage. |
| `time_per_day` | `8. how much time do you spend using digital learning tools for academic purposes per day?` | String | Ordinal | `Less than 30 minutes`, `30 minutes -1 hours`, `1-2 hours`, `2-3 hours`, `More than 3 hours` | Daily time allocation dedicated to digital study. |

---

## 3. Academic Value, Perceived Benefits & Information Trust

| Variable | Column Header in Raw Form | Data Type | Scale | Allowed Values / Categories | Description |
|:---|:---|:---:|:---:|:---|:---|
| `most_useful_tools` | `15. Which digital learning tools do you consider most useful for your academic learning?` | String | Nominal (Multi-select) | `ChatGPT`, `Gemini`, `cloude`, `Perplexity`, `perfectly` | Specific platforms perceived as delivering the highest academic utility. |
| `helpfulness` | `9. How much do digital learning tools help you in your studies` | String | Ordinal | `slightly helpful`, `Moderately helpful`, `Very helpful`, `Extremely helpful` | Perceived qualitative helpfulness for academic coursework. |
| `main_benefit` | `10. What is the main benefits you get from digital learning tools?` | String | Nominal (Multi-select) | `All`, `Better understanding of difficult topics`, `Helps in assignment/project`, `Quick Access to information`, `Save time`, `improve technical/learning skills`, `Important exam preparation`, `provides additional study material` | Primary academic benefits experienced by the student. |
| `biggest_advantage` | `11. what do you consider the biggest advantage of digital learning tools` | String | Nominal | `All of the above`, `Easy and quick Access to information`, `Save time`, `Easy explanation of difficult concept`, `Flexibility to study anytime and anywhere`, `Easy revision through recorded lectures` | Single most decisive advantage identified. |
| `accuracy_rating` | `16. How accurate and reliable do you find the information provided by digital learning tools?` | String | Ordinal | `Highly accurate`, `Accurate`, `Neutral / Moderately accurate`, `Moderately inaccurate`, `Very inaccurate` | Perceived accuracy and reliability of digital & AI information. |
| `overall_experience` | `17. How would you rate your overall experience with digital learning tools for your academic studies?` | String | Ordinal | `Excellent`, `Good`, `Average`, `Poor`, `Very Poor` | Holistic satisfaction and quality rating of digital learning. |

---

## 4. Hardware Infrastructure, Access & Educational Economics

| Variable | Column Header in Raw Form | Data Type | Scale | Allowed Values / Categories | Description |
|:---|:---|:---:|:---:|:---|:---|
| `device` | `13. What device do you mainly use for digital learning?` | String | Nominal | `Smartphone`, `Laptop`, `Tablet`, `Desktop` | Primary hardware computing platform used for study. |
| `access_location` | `14. Where do mainly access digital learning tools?` | String | Nominal | `Home`, `College`, `Hostel`, `Library` | Primary physical environment where digital tools are accessed. |
| `problem_faced` | `12. what problem do you face while using digital learning tools?` | String | Nominal | `Paid/Limited features`, `Internet connectivity issues`, `incorrect or misleading information`, `Privacy concerns` | Primary obstacle, friction point, or barrier encountered. |
| `cost_comparison` | `19. Compared to offline learning, how do you find the cost of digital learning tools?` | String | Ordinal | `Much more expensive`, `Slightly more expensive`, `Almost the same`, `Slightly cheaper`, `Much cheaper` | Perceived cost of digital tools relative to traditional offline schooling. |
| `costlier_learning_type` | `18. Which type of learning do you think is more costly?` | String | Nominal | `Digital Learning Tools`, `Offline Learning`, `Depends on the course/institute`, `Both cost almost the same` | Evaluation of which educational mode represents the greater expense. |
| `ai_purpose` | `20. What is your primary purpose for using AI tools?` | String | Nominal | `Clearing doubts and complex concepts`, `Coding / Programming debugging and help`, `Preparing assignments and project reports`, `Translation and grammar correction`, `Understanding math and statistical step-by-step solutions` | Dominant functional academic use case for AI assistants. |

---

## 5. Derived Numeric Score Metrics (Encoded for Correlation Analysis)

| Variable | Source Attribute | Mapping Formula | Min / Max | Analytical Purpose |
|:---|:---|:---|:---:|:---|
| `freq_score` | `frequency` | Rarely = 1, Once a week = 2, 2-3 days a week = 3, 4-6 days a week = 4, Daily = 5 | 1 to 5 | Quantifies frequency for Pearson correlation. |
| `help_score` | `helpfulness` | slightly helpful = 1, Moderately helpful = 2, Very helpful = 3, Extremely helpful = 4 | 1 to 4 | Quantifies perceived academic helpfulness. |
| `acc_score` | `accuracy_rating` | Very inaccurate = 1, Moderately inaccurate = 2, Neutral = 3, Accurate = 4, Highly accurate = 5 | 1 to 5 | Quantifies student trust in information accuracy. |
| `exp_score` | `overall_experience` | Very Poor = 1, Poor = 2, Average = 3, Good = 4, Excellent = 5 | 1 to 5 | Quantifies holistic student satisfaction. |
