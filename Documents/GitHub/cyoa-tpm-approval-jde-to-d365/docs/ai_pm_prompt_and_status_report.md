# 📋 AI-Engineered Project Management Prompt & Executive Status Report

## 🔧 AI Prompt: Executive Project Status Report Generator

Use this AI prompt to generate concise, executive-level status reports that synthesize the best of Lean Six Sigma, PMI AIPMP, Scrum Product Ownership, and Agile reporting practices.

---

### 🔍 Prompt:

> You are an AI assistant supporting a Project Manager overseeing a cross-functional team. Generate a concise, executive-level project status report that synthesizes Lean Six Sigma, PMI AIPMP, Scrum Alliance Product Owner priorities, and Agile methodologies. The report should:
>
> 1. Summarize key project objectives in a results-driven format.
> 2. Update current status across:
>    - Schedule (planned vs. actual milestones)
>    - Budget (variance and burn rate insights)
>    - Deliverables (completion, quality, and stakeholder satisfaction)
> 3. Highlight the top 3 accomplishments this period using success metrics or customer impact.
> 4. Identify the top 3 concerns or impediments, including root cause insights or recommended mitigations.
> 5. Provide actionable insights for executives or clients, including:
>    - High-level recommendations
>    - Key decision points
>    - Change requests or risk alerts
>
> The tone should be confident, data-informed, and stakeholder-aware, tailored for a [INSERT AUDIENCE TYPE] audience. Ensure use of visual indicators (e.g., RAG status, burn-down charts, milestone timelines) and Lean efficiency metrics like DPMO, cycle time, and VoC alignment. Use Agile terminology where appropriate (e.g., epics, velocity, WIP limits).
>
> **Before generation, confirm the following inputs:**
> - Main project objectives:
> - Current status (schedule, budget, deliverables):
> - Top 3 accomplishments:
> - Top 3 concerns:
> - Audience type:

---

## 📈 Executive Status Report (Sample Output)

### 🧭 Project Overview
**Project Name:** JDE to D365 TPM Approval System  
**Objective:** Streamline Total Preventive Maintenance approvals by migrating legacy JDE workflows into Microsoft Dynamics 365.  
**Success Criteria:** Reduce manual cycle time by 40%, align 90%+ of TPM workflows to D365, and deliver UAT-ready MVP by Week 6.

---

### 📊 Status Snapshot

| Metric             | Status       | Commentary                                     |
|--------------------|--------------|------------------------------------------------|
| **Schedule**       | 🟡 At Risk   | Sprint 2 delayed by 3 days due to API auth.   |
| **Budget**         | 🟢 On Track  | Burn rate 92% aligned with planned threshold. |
| **Deliverables**   | 🟢 On Track  | MVP Feature Set v1 complete; QA in progress.  |

---

### ✅ Top 3 Accomplishments

1. **Delivered MVP Workflow Engine:** Covers 4 TPM approval paths, reducing cycle time by ~32%.  
2. **Integrated with Azure AD Auth:** Secure SSO built for maintenance engineers.  
3. **First UAT Walkthrough Complete:** 92% stakeholder satisfaction (VoC survey results).

---

### 🚧 Top 3 Concerns / Impediments

1. **API Rate Limiting with D365:** Mitigation: Shift batch sync jobs to midnight runs.  
2. **Non-standard TPM Workflows (30% cases):** Root cause: Legacy manual overrides. Decision needed: Standardize or support edge logic?  
3. **Scrum Velocity Dip in Sprint 2:** Due to team resource reshuffle. Mitigation: Pull WIP limit to 3 and increase pair programming sessions.

---

### 📌 Actionable Insights for Executives

- 🧭 **Recommendation:** Prioritize standardization of TPM workflows — high ROI on simplification.  
- 🚨 **Risk Alert:** Delays in external approval schema could affect regulatory compliance window.  
- 🧠 **Decision Needed:** Should we move forward with dual workflow logic or phase out legacy overrides?

---

### 📊 Visuals

- 📈 Burndown charts and cycle time trendlines available in `/visuals/sprint-insights.png`
- ✅ Lean Metrics Tracked: DPMO, Sprint WIP, Net Promoter Score (UAT), Feature Rework %

---

_This AI prompt and report template was generated and refined using OpenAI's GPT-4 turbo, engineered by [Erwin Maurice McDonald](https://github.com/emcdo411)._

