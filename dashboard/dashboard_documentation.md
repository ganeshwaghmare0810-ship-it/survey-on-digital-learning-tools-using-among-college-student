# Power BI Dashboard Architecture & Visual Documentation

**Project Title:** Survey on Digital Learning Tools Usage Among College Students  
**Report File:** `digital_learning_tools_dashboard.pbix`  
**Canvas Resolution:** 1280 x 720 (16:9 Widescreen)  
**Target Audience:** Academic Evaluators, University Administrators, EdTech Product Managers, Recruiters  

---

## 1. Executive Summary & Dashboard Architecture

The Power BI dashboard provides an interactive, visual interface to explore primary empirical survey data from 69 college students regarding their adoption, usage habits, device access, perceived benefits, economic impressions, and generative AI utilization in higher education.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Power BI Report Architecture                    │
├───────────────────────────────────┬────────────────────────────────────┤
│   Page 1: Demographics & Usage    │  Page 2: Perception, Cost & AI     │
├───────────────────────────────────┼────────────────────────────────────┤
│ • KPI Cards (Respondents, Age)    │ • KPI Cards (Satisfaction, Trust)  │
│ • Slicers (Age, Gender, Device)   │ • Slicers (Age, Gender, Device)    │
│ • Age & Gender Distributions      │ • Multi-select Tools Ecosystem     │
│ • Tool Adoption (Yes/No Pie)      │ • Most Useful AI Tools             │
│ • Usage Frequency & Study Hours   │ • Biggest Advantages Reported      │
│ • Perceived Helpfulness & Rating  │ • Problems Faced (Paywalls/Data)   │
│ • Primary Learning Devices        │ • Relative Cost Perception         │
│ • Digital vs. Offline Cost Ratio  │ • Primary AI Academic Use Cases    │
└───────────────────────────────────┴────────────────────────────────────┘
```

The underlying data model connects directly to the survey responses dataset (`Sheet1`, 69 rows, 22 fields). Both pages leverage custom, high-tech dark/slate UI canvas templates created specifically to demarcate visual cards, slicers, and chart containers.

---

## 2. Page 1 — Demographics & Digital Tool Usage Patterns

### Page Overview
Page 1 sets the foundational context of the sample: who the respondents are, how extensively they adopt digital learning tools, how often they use them, how long they study, and what hardware they rely on.

| Visual # | Visual Type | Original Title in PBIX | Cleaned / Recommended Title | Data Fields Mapped | Insight / Takeaway |
|:---:|:---|:---|:---|:---|:---|
| **V-01** | Textbox | *Survey on Digital Learning Tools...* | **Survey on Digital Learning Tools Usage** | Header Banner | Report branding & institutional title banner. |
| **V-02** | Card | *(No title)* | **Total Survey Respondents** | `Count(Sheet1.sno)` | **69 respondents** participated in the study. |
| **V-03** | Card | *(No title)* | **Average Participant Age** | `Average(Sheet1.age)` *(Note: original used Sum)* | Average respondent age is **19.93 years** (range: 18–26). |
| **V-04** | Slicer | *(No title)* | **Filter by Age** | `Sheet1.age` | Interactive single/multi-value filter for age brackets (18–26). |
| **V-05** | Slicer | *(No title)* | **Filter by Gender** | `Sheet1.gender` | Interactive slice by Male, Female, Other. |
| **V-06** | Slicer | *(No title)* | **Filter by Hardware Device** | `Sheet1.device` | Slices report by Smartphone, Laptop, Tablet, Desktop. |
| **V-07** | Column Chart | *Age Distibution of Respondents* | **Age Distribution of Respondents** | X: `Sheet1.age`<br>Y: `Count(Sheet1.sno)` | Concentrated heavily at ages 18, 19, and 20 (undergraduate core). |
| **V-08** | Pie Chart | *Gender Distribution* | **Gender Breakdown** | Legend: `gender`<br>Values: `Count(sno)` | **66.7% Male (46)**, **31.9% Female (22)**, **1.4% Other (1)**. |
| **V-09** | Pie Chart | *Do You Use Digital Learning tools?* | **Digital Tool Adoption Rate** | Legend: `uses_tools`<br>Values: `Count(sno)` | **94.2% (65)** answered Yes; only 5.8% (4) do not use digital tools. |
| **V-10** | Clustered Column | *(No title)* | **Respondents by Academic Program** | X: `year_of_study`<br>Y: `Count(sno)` | Highest volume from **SY Data Science (31)** and CS programs. |
| **V-11** | Clustered Column | *(No title)* | **Usage Frequency Distribution** | X: `frequency`<br>Y: `Count(sno)` | **Daily usage leads with 41 students (59.4%)**, followed by 4–6 days (14). |
| **V-12** | Clustered Column | *Time Spent on digilat learning tools per day* | **Daily Time Dedicated to Digital Study** | X: `time_per_day`<br>Y: `Count(sno)` | Dominant bands: **1–2 hours (22)** and **30 mins–1 hour (21)**. |
| **V-13** | Clustered Column | *Percelved Helpfulness of Digital :earning Tools* | **Perceived Academic Helpfulness** | X: `helpfulness`<br>Y: `Count(sno)` | **Very Helpful (38)** and Extremely Helpful (11) represent 71.0%. |
| **V-14** | Clustered Bar | *Main Benefits Reported* | **Reported Academic Benefits** | Y: `main_benefit`<br>X: `Count(sno)` | **All-round benefit (22)** and **Better understanding (21)** lead. |
| **V-15** | Clustered Column | *Overall Experience Rating* | **Overall Satisfaction Rating** | X: `overall_experience`<br>Y: `Count(sno)` | **82.6% positive:** 33 Excellent, 24 Good, 6 Average, 6 Poor/Very Poor. |
| **V-16** | Pie Chart | *Primary Devise used for Digital Learning* | **Primary Computing Hardware** | Legend: `device`<br>Values: `Count(sno)` | **Smartphone: 53.6% (37)**, Laptop: 39.1% (27), Tablet/Desktop: 7.2%. |
| **V-17** | Pie Chart | *Parcelved cost of Digital vs Offline Learning* | **Cost Perception (Digital vs. Offline)** | Legend: `cost_comparison`<br>Values: `Count(sno)` | 52.2% consider digital more expensive; 26.1% consider it cheaper. |

---

## 3. Page 2 — Perception, Affordability & Generative AI Impact

### Page Overview
Page 2 investigates deeper academic mechanics: tool preferences, multi-select usage, cross-tabulation of frequency vs. helpfulness, key friction points (paywalls, connectivity), cost drivers, and the explosive adoption of Generative AI.

| Visual # | Visual Type | Original Title in PBIX | Cleaned / Recommended Title | Data Fields Mapped | Insight / Takeaway |
|:---:|:---|:---|:---|:---|:---|
| **V-18** | Textbox | *Survey on Digital Learning Tools...* | **Survey on Digital Learning Tools — Deep Dive** | Header Banner | Section title and navigation header. |
| **V-19** | Card | *(No title)* | **Total Survey Sample** | `Count(Sheet1.sno)` | 69 student records evaluated. |
| **V-20** | Card | *(No title)* | **Adoption Index** | `Count(Sheet1.sno)` | High adoption baseline (94.2%). |
| **V-21** | Slicer | *(No title)* | **Filter by Age** | `Sheet1.age` | Cross-page filtering continuity. |
| **V-22** | Slicer | *(No title)* | **Filter by Gender** | `Sheet1.gender` | Cross-page filtering continuity. |
| **V-23** | Slicer | *(No title)* | **Filter by Device** | `Sheet1.device` | Cross-page filtering continuity. |
| **V-24** | Clustered Bar | *Digital learning tools used* | **Digital Learning Platforms Ecosystem** | Y: `tools_used`<br>X: `Count(sno)` | **YouTube (47)** and **ChatGPT/AI (47)** tie for #1; Google Classroom (27). |
| **V-25** | Clustered Bar | *Tools Considered Most Useful(Mostly-use)* | **Tools Rated as Most Useful** | Y: `most_useful_tools`<br>X: `Count(sno)` | **ChatGPT dominates decisively (55 mentions, 79.7%)**, followed by Gemini. |
| **V-26** | Clustered Bar | *Biggest Advantages of Digital Learning Tools* | **Single Greatest Advantage Identified** | Y: `biggest_advantage`<br>X: `Count(sno)` | All of the above (23), Quick Information (18), Time-saving (13). |
| **V-27** | Clustered Column | *Primary Location of Access* | **Primary Study Location** | X: `access_location`<br>Y: `Count(sno)` | **Home (38 respondents, 55.1%)** and **College (23 respondents, 33.3%)**. |
| **V-28** | Clustered Bar | *Problem Faced while using Digital Learning Tools* | **Key Hurdles & Friction Points** | Y: `problem_faced`<br>X: `Count(sno)` | **Paid/Limited Features is #1 barrier (41, 59.4%)**, Internet lag (17, 24.6%). |
| **V-29** | Clustered Bar | *Wthch type of learning is seen as more coustly* | **Perception: Which Learning Mode is Costlier?** | Y: `costlier_learning_type`<br>X: `Count(sno)` | Split three ways: Digital (24), Offline (23), Depends on Course (20). |
| **V-30** | Clustered Bar | *Primary Purpose of using AI Tools* | **Core Academic Purposes of Generative AI** | Y: `ai_purpose`<br>X: `Count(sno)` | **Clearing complex doubts (28, 40.6%)** & **Coding/debugging (26, 37.7%)**. |
| **V-31** | Clustered Column | *Usage Frequency vs Perceived Helpfulness* | **Frequency vs. Perceived Helpfulness Crosstab** | X: `frequency`<br>Y: `Count(sno)`<br>Legend: `helpfulness` | Demonstrates that daily users report the highest concentration of "Very Helpful". |

---

## 4. Professional DAX Measure Suite (Best Practice Recommendations)

In the original report, several visuals utilize default aggregations on integer columns (such as `Sum(Sheet1.sno)` or `Sum(Sheet1.age)`). In enterprise Power BI deployments, explicit DAX measures ensure mathematical correctness, consistent drill-downs, and clean formatting.

The following DAX measures should be added to an explicit `_Measures` table in the PBIX file:

```dax
// =====================================================================
// Core Sample & Adoption Measures
// =====================================================================

Total Respondents = 
COUNTROWS('Sheet1')

Average Age = 
ROUND(AVERAGE('Sheet1'[age]), 2)

Active Digital Tool Users = 
CALCULATE(
    COUNTROWS('Sheet1'),
    'Sheet1'[uses_tools] = "Yes"
)

Digital Tool Adoption Rate = 
DIVIDE([Active Digital Tool Users], [Total Respondents], 0)

// =====================================================================
// Usage Frequency & Time Dedication Measures
// =====================================================================

Daily Users = 
CALCULATE(
    COUNTROWS('Sheet1'),
    'Sheet1'[frequency] = "Daily"
)

Daily Usage Rate = 
DIVIDE([Daily Users], [Total Respondents], 0)

Intensive Users (2+ Hours Daily) = 
CALCULATE(
    COUNTROWS('Sheet1'),
    'Sheet1'[time_per_day] IN {"1-2 hours", "2-3 hours", "More than 3 hours"}
)

// =====================================================================
// Experience, Helpfulness & Trust Metrics
// =====================================================================

High Helpfulness Count = 
CALCULATE(
    COUNTROWS('Sheet1'),
    'Sheet1'[helpfulness] IN {"Very helpful", "Extremely helpful"}
)

High Helpfulness Rate = 
DIVIDE([High Helpfulness Count], [Total Respondents], 0)

Satisfied Students (Good / Excellent) = 
CALCULATE(
    COUNTROWS('Sheet1'),
    'Sheet1'[overall_experience] IN {"Good", "Excellent"}
)

Student Satisfaction Rate = 
DIVIDE([Satisfied Students (Good / Excellent)], [Total Respondents], 0)

High Trust Count (Accurate / Highly Accurate) = 
CALCULATE(
    COUNTROWS('Sheet1'),
    'Sheet1'[accuracy_rating] IN {"Accurate", "Highly accurate"}
)

Trust Rate = 
DIVIDE([High Trust Count (Accurate / Highly Accurate)], [Total Respondents], 0)

// =====================================================================
// Friction Points & Device Access
// =====================================================================

Paywall Friction Count = 
CALCULATE(
    COUNTROWS('Sheet1'),
    'Sheet1'[problem_faced] = "Paid/Limited features"
)

Paywall Friction Rate = 
DIVIDE([Paywall Friction Count], [Total Respondents], 0)

Smartphone Dominance Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('Sheet1'), 'Sheet1'[device] = "Smartphone"),
    [Total Respondents],
    0
)
```

---

## 5. UI/UX Audit & Typographical Recommendations

During inspection of the original `Report/Layout` JSON, minor typographical errors were identified in visual titles. These should be polished for production client presentations:

1. **Page 1 - Visual 7:** `"Age Distibution of Respondents"` → Change to `"Age Distribution of Respondents"`
2. **Page 1 - Visual 12:** `"Time Spent on digilat learning tools per day"` → Change to `"Time Spent on Digital Learning Tools per Day"`
3. **Page 1 - Visual 13:** `"Percelved Helpfulness of Digital :earning Tools"` → Change to `"Perceived Helpfulness of Digital Learning Tools"`
4. **Page 1 - Visual 16:** `"Primary Devise used for Digital Learning"` → Change to `"Primary Device Used for Digital Learning"`
5. **Page 1 - Visual 17:** `"Parcelved cost of Digital vs Offline Learning"` → Change to `"Perceived Cost of Digital vs. Offline Learning"`
6. **Page 2 - Visual 29:** `"Wthch type of learning is seen as more coustly"` → Change to `"Which Type of Learning is Seen as More Costly?"`
7. **Page 2 - Visual 31:** `"Tools Considered Most Useful(Mostly-use)"` → Change to `"Tools Considered Most Useful (Multi-select)"`

---

## 6. How to Open and Refresh the Power BI Dashboard

1. **Prerequisites:** Ensure **Microsoft Power BI Desktop** (Free) is installed on Windows.
2. **Open File:** Double-click `dashboard/digital_learning_tools_dashboard.pbix`.
3. **Data Source Verification:**
   - Go to `Home` > `Transform Data` > `Data Source Settings`.
   - The data source points to the Excel worksheet. If moved, point it to `data/processed/survey_data_cleaned.xlsx` or `data/raw/survey_data_raw.xlsx`.
4. **Apply DAX Measures:** Paste the measures from Section 4 above into the model for optimal enterprise reporting.
5. **Export Visuals:** In Power BI Desktop, navigate to `File` > `Export` > `Export to PDF` or use Windows Snipping Tool (`Win + Shift + S`) to capture refreshed high-resolution screenshots.
