# Project Methodology & Research Design

**Project Title:** Survey on Digital Learning Tools Usage Among College Students  
**Degree Track:** B.Sc. (Data Science) — Field Project under NEP 2020  
**Department:** Department of Data Science, CASAS  
**Institution:** New Arts, Commerce and Science College, Ahmednagar (Autonomous)  

---

## 1. Research Framework

```
┌────────────────────────────────────────────────────────────────────────┐
│                        End-to-End Research Lifecycle                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    1. Problem Formulation          ▼
    ├── Literature review & classroom observation
    └── Definition of 6 research questions & 7 core objectives
                                    │
    2. Survey Instrument Design     ▼
    ├── Google Forms design: 20 questions across 5 sections
    └── Pilot testing & response validation
                                    │
    3. Primary Data Collection      ▼
    ├── Non-probability convenience sampling (N = 69)
    └── Active collection window: Aug 21 – Sept 7, 2026
                                    │
    4. Data Engineering & Cleansing ▼
    ├── Column renaming & whitespace sanitization
    ├── PII redaction (name decoupling)
    ├── Deduplication audit & missing value verification
    └── Multi-select pipe ("|") decomposition
                                    │
    5. Quantitative Analytics       ▼
    ├── Descriptive statistics & univariate distributions
    ├── Ordinal Likert mapping (1 to 5 scale)
    ├── Bivariate cross-tabulations
    └── Pearson product-moment correlation analysis (r)
                                    │
    6. Visualization & Reporting    ▼
    ├── 21 High-resolution Matplotlib/Seaborn figures
    ├── 2-Page interactive Microsoft Power BI Dashboard
    └── Formal Academic Thesis & GitHub Portfolio Repository
```

---

## 2. Research Design & Sampling Strategy

### Research Design
A non-experimental, descriptive cross-sectional survey research design was implemented. Descriptive research is optimal for establishing baseline frequencies, behavioral patterns, and qualitative evaluations within a defined student community.

### Target Population & Study Area
- **Geographic Area:** Ahmednagar (officially Ahilyanagar), Maharashtra, India.
- **Institutional Context:** New Arts, Commerce and Science College (Autonomous), managed by the Ahmednagar Jilha Maratha Vidya Prasarak Samaj (AJMVP Samaj, est. 1970). Affiliated to Savitribai Phule Pune University.
- **Population:** Undergraduate and postgraduate college students enrolled in computer science, data science, and allied collegiate disciplines.

### Sampling Technique
- **Method:** Non-probability convenience and snowball sampling administered via digital channels (college communication groups, student WhatsApp networks).
- **Sample Size ($N$):** **69 validated student responses** containing complete, non-null submissions across all 22 survey parameters.

---

## 3. Data Collection Instrument

Primary empirical data was captured via a structured Google Form containing **20 formal questions** categorized into five thematic modules:

1. **Section A: Personal & Demographic Profile**
   - Full Name (captured for academic verification; redacted during public analysis).
   - Age (integer, in completed years).
   - Gender (Male, Female, Other).
   - Academic Class / Year of Study (e.g. SY Data Science, SY Computer Science).
2. **Section B: Digital Learning Tool Usage & Study Habits**
   - General adoption (Yes / No).
   - Specific platforms utilized (Multi-select: YouTube, ChatGPT, Google Classroom, Zoom, etc.).
   - Frequency of use (Daily, 4–6 days/week, 2–3 days/week, Once a week, Rarely).
   - Daily time commitment (<30 mins, 30m–1h, 1–2h, 2–3h, >3h).
3. **Section C: Academic Value, Perceived Benefits & Information Trust**
   - Specific tool considered most useful (ChatGPT, Gemini, etc.).
   - Perceived academic helpfulness (4-point Likert scale).
   - Multi-select reported benefits (conceptual understanding, time saving, exam preparation).
   - Single greatest advantage.
   - Information accuracy & reliability trust (5-point Likert scale).
   - Holistic satisfaction / overall experience rating (5-point Likert scale).
4. **Section D: Infrastructure, Barriers & Educational Economics**
   - Primary hardware platform (Smartphone, Laptop, Tablet, Desktop).
   - Primary study location (Home, College, Hostel, Library).
   - Primary problem or obstacle faced (Paywalls, Connectivity, Inaccuracy, Privacy).
   - Relative cost perception: Digital vs. Offline learning.
   - Overall perception of which learning mode is costlier.
5. **Section E: Generative Artificial Intelligence (AI) Workflows**
   - Primary functional use case for leveraging AI tools in collegiate coursework.

---

## 4. Data Preprocessing & Cleaning Protocol

The exported raw survey matrix was subjected to a seven-step data preparation pipeline:

1. **Header Sanitization:** Verbose survey questions were converted to lowercase snake_case identifiers (`time_per_day`, `problem_faced`, `ai_purpose`).
2. **Privacy Redaction (PII):** Participant names were decoupled from the analysis dataframe (`df_analysis`) and stored in a de-identified format (`Respondent_01` to `Respondent_69`) in compliance with GDPR and university research ethics.
3. **String Stripping:** Whitespace artifacts and trailing form tags (e.g. `"(others)"`) were programmatically stripped using regular expressions.
4. **Completeness Check:** Audited with `df.isna().sum()`. The survey instrument enforced mandatory fields, yielding **100% complete records** ($0$ null values).
5. **Deduplication Check:** Rows 55 and 56 contained identical responses submitted within the same minute. Following rigorous methodology, both records were preserved as distinct respondents because in a short Likert survey, identical answers between classmates are statistically expected.
6. **Multi-Select Array Unpacking:** Pipe-delimited strings (`"Youtube | Zoom | ChatGPT/AI tools"`) were parsed and aggregated via a frequency accumulator to generate true multi-response distributions.
7. **Ordinal Score Transformation:** Mapped qualitative Likert variables to numerical integers (1 to 5) to enable Pearson product-moment correlation calculations.

---

## 5. Statistical & Analytical Techniques

1. **Univariate Descriptive Statistics:** Frequency counts, percentages, means, medians, standard deviations, and range calculations.
2. **Multi-Response Frequency Analysis:** Multi-select categorical decomposition to establish penetration percentages relative to sample size ($N = 69$).
3. **Bivariate Cross-Tabulation:** Two-way contingency matrices (e.g., Frequency vs. Perceived Helpfulness) to evaluate interaction patterns.
4. **Pearson Product-Moment Correlation Analysis ($r$):**
   $$r = \frac{\sum (X - \bar{X})(Y - \bar{Y})}{\sqrt{\sum (X - \bar{X})^2 \sum (Y - \bar{Y})^2}}$$
   Quantifying linear relationships across Age, Usage Frequency, Helpfulness, Information Trust, and Overall Satisfaction.
5. **Interactive Business Intelligence:** Power BI dimensional modeling, slicer integration, and interactive visual reporting.
