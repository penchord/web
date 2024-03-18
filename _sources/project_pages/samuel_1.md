# Stroke Audit Machine Learning (SAMueL)

> *“Your decision to treat or not treat … That’s the difficult part. That’s the grey area where everyone does a different thing.”* — Stroke Consultant during interviews for SAMueL-1

## Summary

Stroke is a common cause of adult disability. Expert opinion is that about one in five patients should receive clot-busting drugs ('thrombolysis') to break up the blood clot that is causing their stroke. At the moment only about one in nine patients actually receive this treatment in the UK. There is a lot of variation between hospitals, which means that the same patient might receive different treatment in different hospitals. A new treatment is mechanical removal of larger clots ('thrombectomy'). At the moment only about 1 in 30 patients receive this treatment, when it is thought about 1 in 7 patients could be suitable. Though thrombectomy is suitable for fewer patients than thrombolysis, it generally has a larger beneficial effect.

The key aim of the SAMueL work is to understand between-hospital variation in provision of thrombolysis and thrombectomy, the consequences of that variation on patient outcomes and use of NHS resources, and how unwarranted variation may be reduced, patient outcomes improved, and NHS resource use optimised.

The figure below shows the pathway we are looking at, and the questions we are are asking. We use *clinical pathway simulation* to model the flow of patients through the emergency stroke pathway, so we can ask questions about what improvement in outcomes could be achieved by improving patient flow. We use machine learning to understand variation in decision to treat, so we can ask questions about what improvement in outcomes could be achieved by improving consistency around clinical decision-making.

![](./images/samuel_pathway.png)

We tailor our modelling to process-speeds and decisions-to-treat at each hospital, and also base the models on hospital's own patient populations. This allows us to provide a realistic idea of what thrombolysis or thrombectomy use could be at each hospital, rather than providing the same target to all hospitals regardless of local patient population demographics.

In SAMueL-1 we developed the methods for understanding what are the main causes of variation in use of thrombolysis between hospitals: how much difference is due to processes (like how quickly a patient is scanned), how much is due to differences in patient populations, and how much difference is due to different decision-making by doctors. By applying these methods we found that the majority of between-hospital variation comes from hospital processes and decision-making, and not from differences in local populations. We also found that thrombolysis rates could reasonably be nearly doubled, but that each hospital should have its own target, taking into account the characteristics of the local population.

In SAMueL-2 we extended the methodology to include explainable machine learning to understand how patient features and hospital ID affect choice to give thrombolysis. We found that the odds of the same patient receiving thrombolysis varied by more than 10 fold between hospitals. We also built explainable machine learning models to predict outcome with and without thrombolysis, and demonstrated that the benefit from thrombolysis in practice closely matches that found in the clinical trials.

We are currently exploring developing this work to include use of thrombectomy as well as thrombolysis.

## Funding

HDR-UK British Heart Foundation Stroke Data Science Catalyst: BHF_SC001 £21k. What are the long-term consequences of stroke on the patient and to the NHS, and what contributes to variation? April - December 2024.

NIHR Health Services and Delivery Research Reference NIHR134326: £589K Stroke Audit Machine Learning (SAMueL-2). April 2022 to July 2024. [link](https://fundingawards.nihr.ac.uk/award/NIHR134326)

NIHR HS&DR Project: 17/99/89: £330K Use of simulation and machine learning to identify key levers for maximising the disability benefit of intravenous thrombolysis in acute stroke pathways. Feb 2019 - August 2021 [link](https://fundingawards.nihr.ac.uk/award/17/99/89)

## Patient and carer involvement

We have a very engaged patient and carer involvement group. They have helped shape our work in important ways:

* They have constantly encouraged the project to focus most on improving patient outcomes.
* They provide a critical audience for developing and testing ways to explain complex machine learning methods in easily understandable ways.
* They help the project prioritise what to communicate from the project's extensive work.


## Project web sites (with Python code)

[SAMueL-1 online book of all work](https://samuel-book.github.io/samuel-1/introduction/intro.html)

[Explainable machine learning to understand variation in thrombolysis practice](https://samuel-book.github.io/samuel_shap_paper_1/introduction/intro.html)

## Publications

### Peer reviewed papers

Pearn, K, Allen, M., Laws, A., Monks, T., Everson, R. and James, M. (2023). What Would Other Emergency Stroke Teams Do? Using Explainable Machine Learning to Understand Variation in Thrombolysis Practice. European Stroke Journal 8 (4): 956–65. [link](https://doi.org/10.1177/23969873231189040)

James, C., Allen, M,. James, M., Everson, R. (2023) Using machine learning and clinical registry data to uncover variation in clinical decision making. Intelligence-Based Medicine. 7, 100098. doi: https://doi.org/10.1016/j.ibmed.2023.100098. [link](https://www.sciencedirect.com/science/article/pii/S2666521223000121)

Allen, M. James, C., Frost,J., Liabo, K., Pearn, K., Monks, T., Everson, R., Stein, K. and James, M.  (2022). Use of Clinical Pathway Simulation and Machine Learning to Identify Key Levers for Maximizing the Benefit of Intravenous Thrombolysis in Acute Stroke.  Stroke. 2022;53:2758–2767 DOI 10.1161/STROKEAHA.121.038454. [link](https://www.ahajournals.org/doi/10.1161/STROKEAHA.121.038454) 

Allen, M., James, C., Frost, J. Liabo, K., Pearn, K., Monks, T., Zhelev, Z., Logan, S., Everson, R., James, M., Stein, K. (2022). Using simulation and machine learning to maximise the benefit of intravenous thrombolysis in acute stroke in England and Wales: the SAMueL modelling and qualitative study. Health and Social Care Delivery Research. 2022 Oct 21;10(31):1–148. DOI: 10.3310/GVZL5699 [link](https://pubmed.ncbi.nlm.nih.gov/36302070/) Accompanying online book: Available online at: [link](https://samuel-book.github.io/samuel-1/). DOI: 10.5281/zenodo.5078131.

*Stroke* editorial on SAMueL-1 work: [link](https://www.ahajournals.org/doi/10.1161/STROKEAHA.122.039954)

Allen, M., Pearn, K., Monks, T., Bray, B., Everson, R., Salmon, A., James, M. and Stein, K. (2019) Can clinical audits be enhanced by pathway simulation and machine learning? An example from the acute stroke pathway. BMJ Open 2019;9:e028296. doi:10.1136/bmjopen-2018-028296 [link](https://bmjopen.bmj.com/content/9/9/e028296)

### Conference presentations

Pearn, K., Allen, M., Laws, A., Everson, R. & James, M. (2023). What would other emergency stroke teams do? Using explainable machine learning to understand variation in thrombolysis practice. European Stroke Organisation Conference. Zenodo. [https://doi.org/10.5281/zenodo.7878306](https://doi.org/10.5281/zenodo.7878306)

Pearn, K., Allen, M., Laws, A., Everson, R. & James, M. (2023). WHAT WOULD OTHER EMERGENCY STROKE TEAMS DO? Using explainable machine learning to understand variation in thrombolysis (clot-busting) practice. AI UK 2023 (Turing Institute), London, UK. Zenodo. [https://doi.org/10.5281/zenodo.7759059](https://doi.org/10.5281/zenodo.7759059)

## Quotes

Noreen Kamal, editor of *Stroke*:

> 'Both machine learning and simulation modeling provide an exciting new frontier for acute stroke research. These SAMueL approaches can provide insight for process improvements that will result in better patient outcomes'

Dr. Richard Francis, Head of Research, Stroke Association:

> 'We are very concerned by thrombolysis rates in England. Thrombolysis rates stagnated at around 11-12% since 2013, and recently fell below 11% for the first time in a decade. There is also considerable variation across the country. These figures are unacceptable. Big data and machine learning approaches like those used in this study give us hope. They offer exciting possibilities for improving stroke services. We are also pleased to see the researchers looking at what might be helpful for individual hospitals.'

Prof. Chris Price, Professor of Stroke and Applied Research, Newcastle University: 

> 'These results are relevant both to individual clinicians and to systems. For instance, clinicians may focus more on establishing stroke onset time to make better treatment decisions. Services could set the target rate for thrombolysis at a level based upon evidence.The research could lead to changes in local service assessments and targets. It will also feed into other research I am supporting about emergency pathways of care for stroke.'

Dr. Jehath Syed, Clinical Pharmacist and Researcher, JSS Academy of Higher Education & Research, Mysuru: 

> 'Congratulations to the authors for this exhaustive work. It is the first of its kind and definitely adds value to the literature and practice. These findings will lead to further improvements to the healthcare system.'

Holly Maguire, Advanced Nurse Practitioner for stroke, Mid Cheshire Hospital Trust:

> 'I co-ordinate acute stroke training locally, and believe that some of these results will influence practice nationally. Simulation training is becoming more widely used with positive results across healthcare learning. Applying this learning to acute stroke treatment is an excellent advance. Providing robust training for emergency service provision is notoriously difficult. Prompt diagnosis and treatment is paramount and it can be difficult to provide services alongside training. The need to wait for someone to present with a particular condition can also make training a lengthy process. Simulation training could allow  standardised and robust training to be provided nationally, which would reduce intra-hospital variation.'

Ailsa Brotherton, Improvement Director, National Improvement Board

> 'Dear Martin (James). I just wanted to drop you a *Thank You* email for visiting our Trust today (to present the SAMueL work) with your colleagues; your presentation was superb, so inspirational in terms of the difference we can make for the patients who are not currently receiving thrombolysis; a great illustration of how we compare in our decision making to the ‘premier’ hospitals.....I think this is amazing work with huge clinical benefit.'

David Hargroves, National Clinical Director for Stroke Medicine – NHS England

> 'Dear Martin, thank you so much for your excellent talk and contribution to the whole 'Thrombolysis in Acute Stroke Collaborate' (TASC) day yesterday.  We are delighted with the collaboration with you and your colleagues from the SAMuel research group. I have real hopes that we will be able to start to make significant inroads to improving thombolysis rates.'


## Web App

The [SAMueL Web App](https://stroke-predictions.streamlit.app/) allows individual hospitals to analyse their own emergency stroke system, and compare it to other hospitals by using a number of different analyses. Each hospital can see:

* Descriptive statistics of their stroke patient population and clinical pathway process speeds.
* How thrombolysis use and clinical benefit may be improved by:
    1. Increasing pathway speed
    2. Increasing the proportion of patients whose stroke onset time is determined.
    3. Adopting similar thrombolysis decision-making to *benchmark* hospitals.
* Predictions of thrombolysis decisions for individual patients (the user sets the patient characteristics and see how likely they are to give thrombolysis, and see what other hospitals would do).
* Likely population outcomes depending on time to thrombolysis and thrombectomy
* A health economics model of patient life expectancy, quality of life years, and the NHS healthcare costs of stroke, depending on discharge disability, age, and gender.

## NIHR highlighting of project

* [NIHR Highlight 1](https://evidence.nihr.ac.uk/alert/increasing-thrombolysis-use-after-stroke-lessons-from-machine-learning/)

* [NIHR Highlight 2](https://evidence.nihr.ac.uk/collection/improving-stroke-services-lessons-from-research/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/B2Q6ak4iELE?si=vYcXTF71rD8hW9Yw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## HDR-UK Award

In 2024 the SAMueL team were given a [HDR-UK Reproducibility Award](https://www.hdruk.ac.uk/wp-content/uploads/2024/02/HDRUK-Awards-2024-Brochure.pdf) for the transparency of the project code and for making the models accessible to stroke teams through the Web App

## Use of work

* Key output from SAMueL, such as bespoke thrombolysis targets for each hospital, will be introduced into national SSNAP audit reports later in 2024.

* SAMueL-1 is cited by the most recent national clinical guidelines for stroke care (Royal College of Physicians 2023), in support of the potential for improving thrombolysis rates: [National Clinical Guideline for Stroke for the UK and Ireland](https://www.strokeguideline.org/)

* SAMueL is forming part of an NHS-England led initiative to improve thrombolysis use in England. This is the TASC (Thrombolysis in Acute Stroke Collaboration) team and has launched in October 2023. Teams have access to analysis of their thrombolysis pathways and decision-making through the [SAMueL Web App](https://stroke-predictions.streamlit.app/)

* The [2024 National Stroke Audit review](https://www.strokeaudit.org/Documents/National/Clinical/Apr2022Mar2023/Apr2022Mar2023-AnnualReport.aspx) cites SAMueL work on potential to improve thrombolysis use.

## Code repositories

[SAMueL-1 Project (online code book)](https://samuel-book.github.io/samuel-1/introduction/intro.html)

[Explainable machine learning for thrombolysis use](https://github.com/samuel-book/samuel_shap_paper_1)

[Stroke unit demographics](https://github.com/samuel-book/stroke_unit_demographics)

[Streamlit web application](https://github.com/samuel-book/streamlit_combo_stroke)

[Machine learning examples with synthetic data](https://github.com/samuel-book/samuel_examples)

## People

**Modelling and machine learning**: Michael Allen, Kerry Pearn, Anna Laws, Charlotte James, Tom Monks, Richard Everson

**Clinical leadership**: Martin James

**Health economics**: Peter McMeekin

**Qualitative research**: Julia Frost, Rachel Jarvis, Keira Pratt-Boyden, Iain Lang, Cathy Pope

**Patient and carer involvement group**: Leon Farmer, Lauren Asare, Penny Thompson, John Williams, Ian and Nicky Hancock, David Burgess, Simon Douglas

**Clinical/management advice**: Ken Stein, Stuart Logan
