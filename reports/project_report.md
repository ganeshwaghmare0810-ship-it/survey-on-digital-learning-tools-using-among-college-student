# Field Project Report: Survey on Digital Learning Tools Usage Among College Students

**A Quantitative Data Analysis Report — Python (Pandas, NumPy, Matplotlib & Seaborn)**

---

**Student Name:** Waghmare Ganesh Jalindar  
**Class / Degree:** B.Sc. (Data Science) — Second Year (SY) | Roll No./PRN: 81  
**Department:** Department of Data Science, CASAS  
**Institution:** New Arts, Commerce and Science College, Ahmednagar (Autonomous)  
**Academic Mentor:** Prof. Arjana Shaikh  
**Head of Department:** Prof. Arun D. Gangarde  
**Survey Dataset:** `survey_data.csv` (69 Verified Responses, 22 Fields)  
**Date of Submission:** September 2026  

---

## Step 1 — Introduction

Digital technology has become an indispensable pillar of modern higher education. Contemporary college students increasingly integrate digital learning platforms—including Google Classroom, YouTube video tutorials, cloud learning environments, mobile educational apps, web conferencing suites, and cutting-edge Generative Artificial Intelligence (AI) assistants such as ChatGPT and Google Gemini—into their daily academic routines.

These platforms provide students with unprecedented access to educational repositories, asynchronous flexible learning schedules, accelerated information retrieval, and interactive pedagogies. Nevertheless, rapid digital adoption introduces complex friction points, including digital distraction, technical downtime, internet dependency, cognitive overload, and paywalled educational resources.

This project delivers an end-to-end empirical study investigating how college students engage with digital learning tools: their adoption rates, frequency and duration of use, platform preferences, perceived helpfulness, cost perceptions, and academic hurdles. Primary data from 69 student respondents was captured via a 20-question survey instrument and analyzed using Python (`pandas`, `numpy`, `matplotlib`, `seaborn`) alongside Microsoft Power BI.

---

## Step 2 — Problem Statement

While digital and AI-driven tools are widely discussed, empirical clarity is lacking regarding actual collegiate usage patterns, qualitative impact, and financial perceptions in regional Indian educational ecosystems. This investigation answers six primary research questions:

1. Which digital learning tools and AI applications are most widely adopted by college students?
2. What is the typical frequency and daily duration of digital educational engagement?
3. What primary academic workflows motivate students to leverage digital platforms?
4. Do students perceive measurable improvements in understanding and academic performance?
5. How does perceived accuracy and reliability impact overall student satisfaction?
6. What infrastructural and economic obstacles impede seamless digital study?

---

## Step 3 — Objectives of the Study

- **Objective 1:** Identify digital learning tools and AI platforms commonly utilized by undergraduate and postgraduate students.
- **Objective 2:** Measure the frequency and daily time allocation dedicated to digital learning.
- **Objective 3:** Categorize the dominant academic workflows (e.g. concept comprehension, coding assistance, exam preparation).
- **Objective 4:** Evaluate student perceptions regarding tool helpfulness and information reliability.
- **Objective 5:** Assess overall student satisfaction and compute statistical drivers of learning experience.
- **Objective 6:** Uncover key infrastructural, financial, and pedagogical friction points.
- **Objective 7:** Formulate actionable, data-driven recommendations for collegiate institutions and edtech designers.

---

## Step 4 — Scope of the Study

The study encompasses collegiate students residing primarily in Ahilyanagar (Ahmednagar district, Maharashtra), examining their usage of:
- **Video & Tutorial Platforms:** YouTube educational channels and recorded lectures.
- **Learning Management Systems (LMS):** Google Classroom and institutional portals.
- **Video Conferencing suites:** Google Meet, Zoom.
- **Generative AI & LLM Assistants:** OpenAI ChatGPT, Google Gemini, Anthropic Claude, Perplexity.
- **Skill & Language Platforms:** Coursera, Duolingo, Udemy.
- **Hardware & Environment:** Smartphones, laptops, tablets, desktops; study from home, campus, hostels, and libraries.

---

## Step 5 — Research Methodology

### 5.1 Research Design
A descriptive, non-experimental quantitative survey research design was adopted to record authentic, self-reported academic behaviors.

### 5.2 Data Collection Protocol
Primary data was captured through a structured Google Form administered between **August 21, 2026, and September 7, 2026**. The instrument comprised 20 questions capturing 22 variables across demographics, platform adoption, time commitment, benefits, trust, device access, and economics.

### 5.3 Target Population & Sampling Framework
The sampling frame comprised undergraduate and postgraduate college students. Non-probability convenience sampling yielded **69 validated responses**, with strong representation across Data Science and Computer Science degree tracks.

### 5.4 Analytical Toolchain
- **Data Manipulation:** Python `pandas` (v2.x) and `numpy` (v1.x).
- **Data Visualization:** `matplotlib` (v3.x) and `seaborn` (v0.12+).
- **Interactive BI:** Microsoft Power BI Desktop for dimensional modeling, slicers, and KPI tracking.
- **Statistical Procedures:** Univariate frequency analysis, multi-select decomposition, bivariate cross-tabulation, and Pearson product-moment correlation analysis ($r$).

---

## Step 6 — Data Cleaning & Quality Assurance

To ensure data integrity, the raw survey export was processed through a systematic six-stage cleaning protocol:
1. **Header Normalization:** Whitespace stripped and verbose survey questions mapped to concise programmatic keys (e.g., `"7. How frequently do you use digital learning tools?"` $\rightarrow$ `frequency`).
2. **PII Protection & De-identification:** The respondent `name` attribute was decoupled from the analytical dataframe (`df_analysis`) to preserve participant privacy under GDPR/academic research ethics.
3. **Categorical Normalization:** Form-generated artifacts such as `"SY Data science (others)"` were sanitized to `"SY Data science"`.
4. **Missing Value Audit:** Complete-case analysis verified **zero missing entries** across all 22 columns ($N = 69$).
5. **Deduplication Audit:** Rows 55 and 56 shared identical categorical responses submitted in rapid succession; both were retained as legitimate coincident survey submissions within a discrete Likert framework.
6. **Multi-Select Unpacking:** Delimited multi-select strings (separated by `"|"`) were decomposed via a custom parsing routine to calculate exact multi-response frequencies.
7. **Ordinal Likert Encoding:** Mapped ordinal responses into integer scales (1 to 5) for correlation modeling:
   - Frequency: Rarely (1) $\rightarrow$ Daily (5)
   - Helpfulness: Slightly helpful (1) $\rightarrow$ Extremely helpful (4)
   - Accuracy Trust: Very inaccurate (1) $\rightarrow$ Highly accurate (5)
   - Overall Experience: Very Poor (1) $\rightarrow$ Excellent (5)

---

## Step 7 — Demographic Profile of Respondents

- **Age Distribution:** Mean age is **19.93 years** ($\pm 1.87$ SD, Median: 19.0, Range: 18–26). The distribution demonstrates that 84.1% of participants are between 18 and 21 years old.
- **Gender Breakdown:** Male: **66.7% (46)**, Female: **31.9% (22)**, Other: **1.4% (1)**.
- **Academic Programs:** The sample is anchored by Second Year (SY) B.Sc. Data Science students (**31 respondents, 44.9%**), followed by SY Computer Science (**9, 13.0%**) and TY Computer Science (**8, 11.6%**). The remaining 30.5% spans 17 programs including BCA, MCA, Cyber Security, Cloud Computing, and Engineering.

---

## Step 8 — Digital Tool Usage Patterns & Study Habits

- **Tool Adoption Rate:** **94.2% (65 of 69)** actively utilize digital learning tools for their collegiate curriculum; only 5.8% (4) report non-usage.
- **Usage Frequency:** Near-daily habitual usage is the norm: **59.4% (41)** use tools **Daily**, and **20.3% (14)** use them **4–6 days per week**. Combined, **79.7%** utilize digital learning tools on an almost daily basis.
- **Daily Time Allocation:**
  - 1–2 hours: **31.9% (22)**
  - 30 minutes – 1 hour: **30.4% (21)**
  - More than 3 hours: **17.4% (12)**
  - Less than 30 minutes: **15.9% (11)**
  - 2–3 hours: **4.3% (3)**

---

## Step 9 — Digital Tool Ecosystem & Utility Rankings

### Multi-Select Tool Usage Breakdown
Students were asked to check all tools utilized during their academic studies:
1. **YouTube:** **47 mentions (68.1%)** — universal platform for concept tutorials and recorded lectures.
2. **ChatGPT / AI Tools:** **47 mentions (68.1%)** — tied for first place with YouTube, proving AI is now a mainstream educational pillar.
3. **Google Classroom:** **27 mentions (39.1%)** — primary administrative and assignment delivery LMS.
4. **Cloud-Based Tools:** **18 mentions (26.1%)** — cloud development, IDEs, and storage.
5. **Google Meet:** **16 mentions (23.2%)** — real-time academic lectures and peer study.
6. **Educational Mobile Apps:** **16 mentions (23.2%)** — specialized subject applications.
7. **Zoom:** **13 mentions (18.8%)** — remote workshops and webinars.
8. **Duolingo:** **10 mentions (14.5%)** — language acquisition.
9. **Coursera:** **8 mentions (11.6%)** — certified MOOC coursework.

### Tools Rated as Most Academically Useful
When asked to isolate the single most impactful learning tools:
- **ChatGPT:** **55 mentions (79.7%)** — overwhelming preference for conversational AI assistance.
- **Google Gemini:** **17 mentions (24.6%)** — strong secondary multimodal AI tool.
- **Cloud-based AI Tools:** **15 mentions (21.7%)**.
- **Perplexity / Other:** **6 mentions (8.7%)**.

---

## Step 10 — Perceived Usefulness, Academic Benefits & Advantages

- **Perceived Helpfulness:**
  - Very Helpful: **55.1% (38)**
  - Extremely Helpful: **15.9% (11)**
  - Moderately Helpful: **15.9% (11)**
  - Slightly Helpful: **13.0% (9)**
  - *Cumulative Positive Perception:* **71.0%** rate tools as Very or Extremely helpful.
- **Primary Reported Benefits (Multi-select):**
  - All-round holistic benefits: **31.9% (22)**
  - Better understanding of complex/difficult topics: **30.4% (21)**
  - Quick access to reference information: **10.1% (7)**
  - Assistance with assignments and project reports: **10.1% (7)**
  - Time savings and skill improvement: **11.6% (8)**
- **Single Biggest Advantage:**
  - "All of the above": **33.3% (23)**
  - Easy and quick access to information: **26.1% (18)**
  - Saves study time: **18.8% (13)**
  - Clear explanations of complex concepts: **13.0% (9)**
  - Asynchronous study flexibility: **7.2% (5)**

---

## Step 11 — Information Reliability, Satisfaction & Infrastructure

- **Perceived Accuracy & Trust:**
  - Highly Accurate: **42.0% (29)**
  - Accurate: **31.9% (22)**
  - Neutral / Moderately Accurate: **18.8% (13)**
  - Inaccurate (Moderately/Very): **7.2% (5)**
  - *Key Finding:* **73.9% of students maintain high baseline confidence** in digital tool accuracy.
- **Overall Experience & Satisfaction:**
  - Excellent: **47.8% (33)**
  - Good: **34.8% (24)**
  - Average: **8.7% (6)**
  - Poor / Very Poor: **8.7% (6)**
  - *Key Finding:* **82.6% express strong satisfaction** with their digital learning experience.
- **Primary Computing Device:**
  - **Smartphone:** **53.6% (37)** — dominant primary device.
  - **Laptop:** **39.1% (27)**.
  - Tablet: **4.3% (3)**.
  - Desktop: **2.9% (2)**.
- **Primary Access Environment:**
  - **Home:** **55.1% (38)**.
  - **College Campus:** **33.3% (23)**.
  - Hostel & Campus Library: **11.6% (8)**.

---

## Step 12 — Friction Points, Educational Economics & Generative AI

- **Major Obstacles Encountered:**
  - **Paid / Limited Features (Paywalls):** **59.4% (41)** — the decisive #1 barrier.
  - **Internet Connectivity Issues:** **24.6% (17)** — mobile data limits and fluctuating Wi-Fi.
  - Incorrect or Misleading Information (Hallucinations): **8.7% (6)**.
  - Privacy and Data Security Concerns: **7.2% (5)**.
- **Perceived Cost: Digital vs. Offline Learning:**
  - Much more expensive: **26.1% (18)**
  - Slightly more expensive: **26.1% (18)**
  - *Combined:* **52.2% consider digital learning more costly** due to required hardware, recurring mobile data packs, and subscription fees.
  - Almost the same: **21.7% (15)**
  - Slightly / Much cheaper: **26.1% (18)**
- **Which Mode is Costlier Overall?**
  - Digital Learning Tools: **34.8% (24)**
  - Offline Traditional Learning: **33.3% (23)**
  - Depends on Course / Institution: **29.0% (20)**
  - Both cost the same: **2.9% (2)**
- **Core Academic Workflows for Generative AI:**
  - **Clearing Doubts & Complex Theoretical Concepts:** **40.6% (28)**
  - **Coding, Programming & Debugging Assistance:** **37.7% (26)**
  - Preparing Academic Assignments & Project Reports: **11.6% (8)**
  - Translation & Language/Grammar Editing: **7.2% (5)**
  - Step-by-Step Mathematical & Statistical Solutions: **2.9% (2)**

---

## Step 13 — Cross-Tabulation & Statistical Correlation Analysis

### 13.1 Usage Frequency vs. Perceived Helpfulness Cross-Tabulation
Contingency analysis demonstrates a direct positive relationship:
- Of the **41 daily users**, **28 (68.3%)** rate digital tools as "Very helpful" and **7 (17.1%)** rate them as "Extremely helpful".
- Infrequent users (Once a week / Rarely) cluster predominantly in the "Moderately helpful" and "Slightly helpful" tiers.

### 13.2 Pearson Product-Moment Correlation Matrix ($r$)

| Variable | Age | Usage Frequency | Helpfulness | Accuracy Trust | Overall Experience |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Age** | 1.000 | 0.233 | 0.024 | 0.156 | 0.193 |
| **Usage Frequency** | 0.233 | 1.000 | 0.052 | 0.331 | **0.533** |
| **Helpfulness** | 0.024 | 0.052 | 1.000 | -0.064 | -0.017 |
| **Accuracy Trust** | 0.156 | 0.331 | -0.064 | 1.000 | **0.686** |
| **Overall Experience** | 0.193 | **0.533** | -0.017 | **0.686** | 1.000 |

### Statistical Interpretations:
1. **Accuracy Trust $\leftrightarrow$ Overall Experience ($r = +0.686$, Strong Positive):**  
   Perceived accuracy and reliability is the **single strongest statistical driver** of student satisfaction. When students trust the information generated by digital and AI tools, their overall experience rises dramatically.
2. **Usage Frequency $\leftrightarrow$ Overall Experience ($r = +0.533$, Moderate Positive):**  
   Frequent, habitual daily engagement correlates with higher satisfaction, suggesting positive reinforcement loops.
3. **Usage Frequency $\leftrightarrow$ Accuracy Trust ($r = +0.331$, Moderate Positive):**  
   Students who utilize digital tools frequently develop greater familiarity and trust in the technology's outputs.
4. **Age ($r = +0.193$) & Helpfulness ($r = -0.017$):**  
   Exhibit negligible linear correlation with overall experience, demonstrating that student satisfaction is governed by **trust and habit**, rather than age or broad helpfulness perceptions.

---

## Step 14 — Key Analytical Findings Summary

| Metric / Attribute | Empirical Finding |
|:---|:---|
| **Survey Sample Size ($N$)** | 69 verified student respondents |
| **Average Age** | 19.93 years (Range: 18–26, SD: 1.87) |
| **Digital Tool Adoption Rate** | **94.2% (65 respondents)** |
| **Daily / Near-Daily Engagement** | **79.7% (55 respondents)** |
| **Top Digital Learning Tools** | **YouTube (68.1%) & ChatGPT/AI (68.1%) [Tied #1]** |
| **Tool Rated Most Useful** | **ChatGPT (79.7% of respondents)** |
| **High Perceived Helpfulness** | **71.0%** (Very / Extremely helpful) |
| **High Overall Satisfaction** | **82.6%** (Good / Excellent rating) |
| **Information Accuracy Trust** | **73.9%** (Accurate / Highly accurate) |
| **Dominant Computing Hardware** | **Smartphone: 53.6%**, Laptop: 39.1% |
| **Dominant Study Environment** | **Home: 55.1%**, Campus: 33.3% |
| **#1 Hurdle Encountered** | **Paid / Limited Features (59.4%, 41 respondents)** |
| **#2 Hurdle Encountered** | **Internet Connectivity Issues (24.6%, 17 respondents)** |
| **Top AI Use Case** | **Doubts / Concepts (40.6%) & Coding / Debugging (37.7%)** |
| **Key Statistical Driver** | **Trust in Accuracy $\leftrightarrow$ Experience ($r = +0.686$)** |

---

## Step 15 — Limitations of the Study

1. **Sampling Frame:** Convenience sample ($N = 69$) recruited via Google Forms; while robust for exploratory collegiate analysis, findings may not capture national demographic variation.
2. **Disciplinary Concentration:** Over 60% of respondents belong to Computer Science and Data Science tracks, naturally biasing AI adoption and coding use cases upward relative to humanities or arts students.
3. **Self-Reported Metrics:** Analysis relies on self-reported perceptions, study duration, and satisfaction ratings rather than objective GPA/exam transcript audits.

---

## Step 16 — Conclusion

The *Survey on Digital Learning Tools Usage Among College Students* confirms that digital educational platforms have achieved near-universal penetration (**94.2%**) in modern undergraduate and postgraduate environments. 

Rather than treating AI and video platforms as peripheral study aids, students now treat **YouTube and ChatGPT as foundational pedagogical infrastructure** for self-directed study, concept clarification, and technical programming. Over **82.6%** report positive academic satisfaction, with perceived accuracy emerging as the primary statistical driver ($r = 0.69$).

Crucially, the primary constraints hindering digital learning are **financial and infrastructural, not cognitive or pedagogical**. Paywalls and connectivity limitations restrict access for a substantial majority. Addressing these economic barriers represents the most viable path toward equitable, high-impact digital education.

---

## Step 17 — Strategic Recommendations

1. **Institutional Software Licensing:** Colleges and universities should negotiate campus-wide student licenses or institutional subscriptions for premier AI platforms and developer tooling to eliminate the paywall barrier.
2. **Campus Wi-Fi Infrastructure:** High-speed, high-density Wi-Fi should be expanded across academic blocks, libraries, and hostel study halls to resolve connectivity bottlenecks.
3. **Curricular AI Literacy:** Incorporate dedicated workshops on critical AI evaluation, hallucination detection, prompt engineering, and cross-verification against authoritative peer-reviewed literature.
4. **Mobile-First Pedagogical Design:** Because 53.6% of students rely on smartphones as their primary learning portal, LMS interfaces and institutional resources must be responsive and optimized for mobile access.
