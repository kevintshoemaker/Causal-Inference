---
title: "NRES 701A: Causal Inference and Analysis"
subtitle: "Course Syllabus, Spring 2027 (DRAFT v2)"
---

> **Draft, subject to change.** This is a preliminary syllabus to help students decide whether to enroll.
> The readings, schedule and assignment details will probably change before the semester starts.

|  |  |
|------------------|------------------------------------------------------------------|
| **Instructors** | Kevin Shoemaker (kevinshoemaker@unr.edu) and Todd Steury (tsteury@unr.edu), Dept. of Natural Resources & Environmental Science |
| **Meeting time and place** | [Day and time to be announced], [room to be announced]. One meeting per week. |
| **Credits and grading** | 2 credits, letter grade |
| **Office hours** | [To be announced], or by appointment |
| **Background** | One regression-level statistics course is recommended but not required. No prior training in causal inference, philosophy or R is assumed. |

# Course description

How do we know that one thing causes another? What would it take to show that a decline in a wildlife
population was driven by habitat loss rather than climate, that deer abundance in the past was driven by
people rather than by climate, or that more species make an ecosystem more productive or stable? What can
we conclude from observational data when an experiment is impossible? And what changes when the system we
study has feedback, networks and many interacting parts?

This course introduces the modern tools of causal inference and shows how to apply them to research in
ecology, natural resources, anthropology, archaeology and related fields. We start with the core ideas:
the "ladder of causation," counterfactuals, and causal diagrams (directed acyclic graphs, or DAGs). We
then work through the main strategies for estimating causal effects: experiments, quasi-experimental
designs, structural equation models and time-series methods. Throughout, we read and critique published
papers, both those that use formal causal methods and those that make causal claims without them.

The course is open to graduate students from any department. The centerpiece is an individual project:
each student builds and refines a well-reasoned causal diagram of their own study system, one that can
guide the design and analysis of their thesis or dissertation research.

# Course format

Each weekly meeting has three parts:

1. **Lecture and discussion (20 to 25 minutes),** led by Kevin or Todd, introducing the week's concepts.
2. **Paper discussion,** centered on the week's readings. Students help lead these discussions (see
   "Paper discussion leadership" below).
3. **Hands-on exercise,** a short problem set or DAG workshop done in small groups in class. Exercises can
   be done with pencil and paper; some include optional R extensions.

# Student learning outcomes

Students who succeed in this course will be able to:

1. Distinguish associational, interventional and counterfactual questions (the ladder of causation) and
   say which one a given study answers.
2. Draw a causal diagram (DAG) for a question in their own field, and use it to identify confounders,
   colliders and mediators and to choose an adjustment set.
3. Explain the assumptions behind experiments, quasi-experimental designs, structural equation models and
   time-series causal methods, and judge when each is credible for a given study system.
4. Read a published paper critically for the causal claim it makes, the evidence offered, and the
   assumptions stated and unstated.
5. Describe how feedback, network structure and scale complicate causal reasoning, and where acyclic
   graphs stop being adequate.
6. Communicate a causal argument clearly in discussion, in a presentation and in writing.

# Texts and readings

**Required text:** Pearl, J., and D. Mackenzie (2018) *The Book of Why: The New Science of Cause and
Effect.* Basic Books. We read four chapters (Introduction and Chapters 1, 4 and 7); the rest is
recommended.

**Readings on WebCampus:** most weekly reading consists of journal articles, posted on WebCampus. Each week
has at most two required readings, usually one that frames the concepts and one applied paper.

**Recommended books (not required):** Pearl, Glymour and Jewell, *Causal Inference in Statistics: A Primer*
(Wiley, 2016); Huntington-Klein, *The Effect* (free online); Cunningham, *Causal Inference: The Mixtape*
(free online); Shipley, *Cause and Correlation in Biology*, 2nd ed. (Cambridge, 2016); McElreath,
*Statistical Rethinking*, 2nd ed. (CRC Press, 2020).

# Course requirements

| Component | Points |
|------------------------------------------------------------|----------|
| Participation and weekly reading responses | 20 |
| In-class exercises | 10 |
| Paper discussion leadership | 10 |
| "Causal claims in the wild" critique | 15 |
| Causal DAG project: initial DAG (Week 5) | 10 |
| Causal DAG project: revised DAG and peer review (Week 10) | 5 |
| Causal DAG project: final presentation (Week 15) | 10 |
| Causal DAG project: final write-up (finals week) | 20 |
| **Total** | **100** |

**Participation and weekly reading responses (20 points).** Come to class having done the reading and
ready to discuss it. By noon on the day of class, post a short response (about 150 words) on WebCampus:
one point you found important and one question you want to discuss. Your two lowest response scores are
dropped.

**In-class exercises (10 points).** Each week's hands-on exercise is graded for good-faith completion.
Your two lowest scores are dropped.

**Paper discussion leadership (10 points).** Each student (in pairs, if enrollment is large) helps lead
the discussion of one week's applied paper. Leaders give a short summary of the paper's causal claim and
evidence, and bring three discussion questions. Sign-up is in Week 1.

**"Causal claims in the wild" critique (15 points; due Week 8).** Find a published paper in your field
that makes a causal claim (for example, "X drives Y" or "X caused the decline") without using formal causal
inference methods. In about 1,000 words: state the claim and which rung of the ladder of causation it
reaches; draw the DAG the authors implicitly assume; identify likely confounders, colliders or selection
effects; judge whether the conclusion follows; and describe what design or analysis would have supported
the claim. Choose your paper by Week 4.

**Causal DAG project (45 points total).** Over the semester you will build a well-reasoned causal diagram
of your own study system, aimed at a causal question in your thesis or dissertation research. Students
without a thesis system yet may choose a well-studied system from the literature, with instructor
approval.

- *Initial DAG (Week 5):* a DAG for your system and focal causal question, with one or two sentences
  justifying each arrow.
- *Revised DAG and peer review (Week 10):* an updated DAG that incorporates what you learned in Weeks 6
  to 9, plus written feedback on a classmate's DAG.
- *Final presentation (Week 15):* an 8 to 10 minute presentation of your DAG and its implications.
- *Final write-up (due finals week, 1,500 to 2,000 words):* your final DAG; the justification and
  assumptions behind it; the adjustment set(s) for your focal question; testable implications; a
  discussion of feedback or unmeasured variables the DAG may miss; and the study design and analysis you
  would use to estimate your causal effect.

# Grading scale

The UNR Graduate School requires a grade of C or better for a course to count toward a graduate degree,
so C is the lowest passing grade in this course.

| Grade | Points |
|---|---|
| A | 93–100 |
| A− | 90–92 |
| B+ | 87–89 |
| B | 83–86 |
| B− | 80–82 |
| C+ | 77–79 |
| C | 73–76 |
| F | Below 73 |

# Weekly schedule

Reading should be completed before the class for which it is listed. Spring break and university holidays
are not shown; dates will be added once the meeting time is set. Readings marked "BoW" are from *The Book
of Why*; all others are on WebCampus.

| Week | Topic and in-class exercise | Required reading | Due |
|-----|--------------------------------------------------|-------------------------|---------------|
| 1 | **Why causality?** Seeing, doing and imagining: the ladder of causation. *Exercise:* place published claims from your field on the ladder. | BoW Introduction and Ch. 1 | Sign up for discussion week |
| 2 | **What is a cause?** Counterfactuals, interventions and potential outcomes; description vs. prediction vs. causal inference. *Exercise:* potential-outcomes tables. | Woodward (SEP), selected sections; Hernán et al. 2019 | Reading responses begin |
| 3 | **DAGs and confounding.** Reading a causal graph; paths, forks, chains and confounders. *Exercise:* draw DAGs; intro to dagitty. | BoW Ch. 4; Arif & MacNeil 2022 | |
| 4 | **Colliders, the back-door criterion and the do-operator.** Adjustment sets; when "controlling for" a variable makes things worse. *Exercise:* simulate confounding and collider bias. | BoW Ch. 7 | Choose "claims in the wild" paper |
| 5 | **DAG workshop.** Building a DAG for your own system. *Exercise:* small-group critique of initial DAGs. | Laubach et al. 2021 | **Initial DAG** |
| 6 | **Experiments.** What randomization and BACI designs do and do not guarantee. *Exercise:* find the hidden assumptions in a field experiment. | Kimmel et al. 2021 | |
| 7 | **Quasi-experiments.** Matching, difference-in-differences, regression discontinuity and instrumental variables. *Exercise:* difference-in-differences with a toy dataset. | Butsic et al. 2017; Watson et al. 2025 | |
| 8 | **Unobserved confounding and panel data.** Fixed effects and repeated observations. *Exercise:* simulate omitted-variable bias. | Byrnes & Dee 2025; Dee et al. 2023 | **"Claims in the wild" critique** |
| 9 | **Path analysis and structural equation models.** Testing a causal model against data; d-separation in practice. *Exercise:* fit and test a simple path model. | Grace & Irvine 2020; Cole et al. 2024 | |
| 10 | **Time series and dynamical systems.** Granger causality and convergent cross mapping: what does each test? *Exercise:* apply both to simulated predator–prey data. | Sugihara et al. 2012; Barraquand et al. 2021 | **Revised DAG and peer review** |
| 11 | **Complexity and stability: cause or statistical artifact?** The diversity–stability debate. *Exercise:* structured debate. | Tilman et al. 1998; Doak et al. 1998 | |
| 12 | **Feedback, networks and systems thinking.** Why DAGs are acyclic, and what to do about feedback. *Exercise:* unroll a feedback loop through time. | Flannery 1968; M. Salmon 1978 | |
| 13 | **Synthesis: from DAG to study design.** Choosing an approach for your own question. *Exercise:* draft an analysis plan for your DAG. | Siegel & Dee 2025 | |
| 14 | **Project workshop.** | None | |
| 15 | **Final presentations.** | None | **Presentation**; write-up due finals week |

# Readings by week

**Week 1.** Pearl, J., and D. Mackenzie (2018) *The Book of Why: The New Science of Cause and Effect.*
Basic Books. Introduction and Ch. 1.

**Week 2.** Woodward, J. Causation and manipulability. *Stanford Encyclopedia of Philosophy.* (Free
online.) — Hernán, M. A., J. Hsu, and B. Healy (2019) A second chance to get causal inference right: A
classification of data science tasks. *Chance* 32(1).

**Week 3.** Pearl and Mackenzie (2018), Ch. 4. — Arif, S., and M. A. MacNeil (2022) Applying the
structural causal model framework for observational causal inference in ecology. *Ecological
Monographs.*

**Week 4.** Pearl and Mackenzie (2018), Ch. 7.

**Week 5.** Laubach, Z. M., E. J. Murray, K. L. Hoke, R. J. Safran, and W. Perng (2021) A biologist's
guide to model selection and causal inference. *Proceedings of the Royal Society B* 288.

**Week 6.** Kimmel, K., L. E. Dee, M. L. Avolio, and P. J. Ferraro (2021) Causal assumptions and causal
inference in ecological experiments. *Trends in Ecology & Evolution* 36(12).
doi:10.1016/j.tree.2021.08.008

**Week 7.** Butsic, V., D. J. Lewis, V. C. Radeloff, M. Baumann, and T. Kuemmerle (2017)
Quasi-experimental methods enable stronger inferences from observational data in ecology. *Basic and
Applied Ecology* 19: 1–10. — Watson, E. J., D. J. Glass, and L. C. Petito (2025) Toward new directions
in human biology: A roadmap for anthropological causal inference with observational data. *American
Journal of Human Biology.* doi:10.1002/ajhb.70149

**Week 8.** Byrnes, J. E. K., and L. E. Dee (2025) Causal inference with observational data and
unobserved confounding variables. *Ecology Letters* 28: e70023. doi:10.1111/ele.70023 (open access) —
Dee, L. E., et al. (2023) Clarifying the effect of biodiversity on productivity in natural ecosystems with
longitudinal data and methods for causal inference. *Nature Communications* 14: 2607.
doi:10.1038/s41467-023-37194-5 (open access)

**Week 9.** Grace, J. B., and K. M. Irvine (2020) Scientist's guide to developing explanatory statistical
models using causal analysis principles. *Ecology* 101(4): e02962. doi:10.1002/ecy.2962 — Cole, K. E.,
M. Moffatt, B. F. Codding, and J. M. Broughton (2024) Human settlement density, not late Holocene climate
change, influenced Artiodactyla species abundance in northeastern California faunal assemblages.
*Quaternary International* 689–690: 43–54. doi:10.1016/j.quaint.2023.10.006

**Week 10.** Sugihara, G., R. May, H. Ye, C. Hsieh, E. Deyle, M. Fogarty, and S. Munch (2012) Detecting
causality in complex ecosystems. *Science* 338. — Barraquand, F., C. Picoche, M. Detto, and F. Hartig
(2021) Inferring species interactions using Granger causality and convergent cross mapping. *Theoretical
Ecology* 14(1): 87–105.

**Week 11.** Tilman, D., C. L. Lehman, and C. E. Bristow (1998) Diversity-stability relationships:
Statistical inevitability or ecological consequence? *American Naturalist* 151. — Doak, D. F., et al.
(1998) The statistical inevitability of stability-diversity relationships in community ecology.
*American Naturalist* 151.

**Week 12.** Flannery, K. V. (1968) Archaeological systems theory and early Mesoamerica. In B. J. Meggers
(ed.), *Anthropological Archaeology in the Americas*, pp. 67–87. Anthropological Society of Washington.
— Salmon, M. H. (1978) What can systems theory do for archaeology? *American Antiquity* 43: 174–183.

**Week 13.** Siegel, K., and L. E. Dee (2025) Foundations and future directions for causal inference in
ecological research. *Ecology Letters* 28. doi:10.1111/ele.70053

## Suggested readings (not required)

- Pearl and Mackenzie (2018), the remaining chapters (especially Ch. 5, the smoking debate; Ch. 6,
  paradoxes; Ch. 8, counterfactuals; and Ch. 9, mediation).
- Bulbulia, J. A. (2024) Methods in causal inference. Part 1: Causal diagrams and confounding.
  *Evolutionary Human Sciences* 6.
- Cardillo, M., and E. Carranza (2025) Applying statistical and causal modeling to interpret thermal
  alteration in observational lithic data. *Peer Community Journal* 5: e88.
- Deffner, D., J. M. Rohrer, and R. McElreath (2022) A causal framework for cross-cultural
  generalizability. *Advances in Methods and Practices in Psychological Science* 5(3).
- Ferraro, P. J., and M. M. Hanauer (2014) Advances in measuring the environmental and social impacts of
  environmental programs. *Annual Review of Environment and Resources* 39.
- Grace, J. B., et al. (2016) Integrative modelling reveals mechanisms linking productivity and plant
  species richness. *Nature* 529.
- Holland, P. W. (1986) Statistics and causal inference. *Journal of the American Statistical
  Association* 81.
- May, R. M. (1972) Will a large complex system be stable? *Nature* 238.
- McElreath, R. (2020) *Statistical Rethinking*, 2nd ed. CRC Press. Ch. 6.
- Bateson, G. (1972) *Steps to an Ecology of Mind.* University of Chicago Press. Selected essays.
- Tainter, J. A. (1988) *The Collapse of Complex Societies.* Cambridge University Press. Ch. 4.

# Classroom policies

**Attendance.** Attendance is expected. Because the course depends on discussion and in-class exercises,
please tell us in advance if you must miss a meeting.

**Late assignments.** Submit assignments on WebCampus by the start of class on the due date. If you know
you will miss a class, you may turn work in early. Contact us before the due date if you need an
extension.

**Email.** You should expect a response within 24 hours on weekdays. Emails sent after 5 PM on Friday
will usually be answered on Monday. For complex questions, please come to office hours.

**Use of artificial intelligence (AI).** [Policy to be finalized by the instructors before the semester
starts.]

# University policies

**Americans with Disabilities Act.** Any student with a disability needing academic adjustments or
accommodations is requested to speak with the instructors or the Disability Resource Center (Pennington
Achievement Center Suite 230) as soon as possible to arrange for appropriate accommodations.

**Academic dishonesty and plagiarism.** All students must abide by UNR academic standards outlined in the
Student Code of Conduct (https://www.unr.edu/student-conduct/university-policies/student-code-of-conduct).
Plagiarism includes knowingly "submitting the language, ideas, thoughts or work of another as one's own;
or assisting in the act of plagiarism by allowing one's work to be used in this fashion." Penalties can
be severe, up to and including expulsion from the university. Guidance on avoiding plagiarism:
https://library.unr.edu/help/quick-how-tos/avoiding-plagiarism.

**Classroom civility.** UNR supports the principle of freedom of expression for both faculty and
students, and respects the rights of faculty to teach and students to learn. Maintaining these rights
requires classroom conditions that do not impede learning. Disruptive behavior may be subject to
disciplinary action under the Student Code of Conduct.

**Student privacy.** In compliance with the Family Educational Rights and Privacy Act (FERPA), the
University of Nevada, Reno maintains the strictest confidentiality of your records.

**Audio and video recording.** Surreptitious or covert video-taping of class or unauthorized audio
recording of class is prohibited by law and by Board of Regents policy. This class may be recorded only
with the written permission of the instructors. To accommodate students with disabilities, some students
may be given permission to record class; your comments in class may therefore be recorded.

**Equal opportunity and Title IX.** The University of Nevada, Reno is committed to providing a safe
learning and work environment for all. If you believe you have experienced discrimination, sexual
harassment, sexual assault, domestic/dating violence, or stalking, whether on or off campus, or need
information related to immigration concerns, please contact the University's Equal Opportunity & Title IX
office at 775-784-1547. For more information, visit https://www.unr.edu/equal-opportunity-title-ix.

**Failure to comply with policy.** In accordance with section 6,502 of the University Administrative
Manual, a student may receive academic and disciplinary sanctions for failure to comply with policy,
including this syllabus, for failure to comply with the directions of a University official, or for
disruptive behavior in the classroom.

**Academic success services.** Your student fees cover usage of the Math Center (775-784-4422), the
Tutoring Center (775-784-6801), and the University Writing and Speaking Center (775-784-6030). These
centers support your classroom learning; it is your responsibility to take advantage of their services.
