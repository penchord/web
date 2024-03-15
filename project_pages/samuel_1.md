# Stroke Audit Machine Learning (SAMueL)

> *“Your decision to treat or not treat … That’s the difficult part. That’s the grey area where everyone does a different thing.”* — Stroke Consultant during interviews for SAMueL-1

## Summary

Stroke is a common cause of adult disability. Expert opinion is that about one in five patients should receive clot-busting drugs ('thrombolysis') to break up the blood clot that is causing their stroke. At the moment only about one in nine patients actually receive this treatment in the UK. There is a lot of variation between hospitals, which means that the same patient might receive different treatment in different hospitals.

In SAMueL-1 we developed the methods for understanding what are the main causes of variation between hospitals: How much difference is due to processes (like how quickly a patient is scanned), how much is due to differences in patient populations, and how much difference is due to different decision-making by doctors. By applying these methods we found that thrombolysis rates could reasonable be doubled, but that each hospital should have its own target, taking into account the characteristics of the local population.

In SAMueL-2 we extended the methodology to include explainable machine learning how patient features and hospital ID affect choice to give thrombolysis. We also built explainable machine learning models to predict outcome with and without thrombolysis, and demonstrated that the benefit from thrombolysis in practice closely matches that found in the clinical trials.

## Funding

NIHR HS&DR Project: 17/99/89: £330K Use of simulation and machine learning to identify key levers for maximising the disability benefit of intravenous thrombolysis in acute stroke pathways. Feb 2019 - August 2021 [link](https://fundingawards.nihr.ac.uk/award/17/99/89)

NIHR Health Services and Delivery Research Reference NIHR134326: £589K Stroke Audit Machine Learning (SAMueL-2). April 2022 to March 2024. [link](https://fundingawards.nihr.ac.uk/award/NIHR134326)

## Project web sites (with Python code)

[SAMueL-1 online book of all work](https://samuel-book.github.io/samuel-1/introduction/intro.html)

[Explainable machine learning to understand variation in thrombolysis practice](https://samuel-book.github.io/samuel_shap_paper_1/introduction/intro.html)

## Publications

Pearn, K, Allen, M., Laws, A., Monks, T., Everson, R. and James, M. (2023). What Would Other Emergency Stroke Teams Do? Using Explainable Machine Learning to Understand Variation in Thrombolysis Practice. European Stroke Journal 8 (4): 956–65. [link](https://doi.org/10.1177/23969873231189040)

James, C., Allen, M,. James, M., Everson, R. (2023) Using machine learning and clinical registry data to uncover variation in clinical decision making. Intelligence-Based Medicine. 7, 100098. doi: https://doi.org/10.1016/j.ibmed.2023.100098. [link](https://www.sciencedirect.com/science/article/pii/S2666521223000121)

Allen, M. James, C., Frost,J., Liabo, K., Pearn, K., Monks, T., Everson, R., Stein, K. and James, M.  (2022). Use of Clinical Pathway Simulation and Machine Learning to Identify Key Levers for Maximizing the Benefit of Intravenous Thrombolysis in Acute Stroke.  Stroke. 2022;53:2758–2767 DOI 10.1161/STROKEAHA.121.038454. [link](https://www.ahajournals.org/doi/10.1161/STROKEAHA.121.038454) 

Allen, M., James, C., Frost, J. Liabo, K., Pearn, K., Monks, T., Zhelev, Z., Logan, S., Everson, R., James, M., Stein, K. (2022). Using simulation and machine learning to maximise the benefit of intravenous thrombolysis in acute stroke in England and Wales: the SAMueL modelling and qualitative study. Health and Social Care Delivery Research. 2022 Oct 21;10(31):1–148. DOI: 10.3310/GVZL5699 [link](https://pubmed.ncbi.nlm.nih.gov/36302070/) Accompanying online book: Available online at: [link](https://samuel-book.github.io/samuel-1/). DOI: 10.5281/zenodo.5078131.

*Stroke* editorial on SAMueL-1 work: [link](https://www.ahajournals.org/doi/10.1161/STROKEAHA.122.039954)

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

## Web App

[SAMueL Web App](https://stroke-predictions.streamlit.app/)

## NIHR highlighting of project

* [NIHR Highlight 1](https://evidence.nihr.ac.uk/alert/increasing-thrombolysis-use-after-stroke-lessons-from-machine-learning/)

* [NIHR Highlight 2](https://evidence.nihr.ac.uk/collection/improving-stroke-services-lessons-from-research/)

* [YouTube (Prof Martin James)](https://www.youtube.com/watch?v=B2Q6ak4iELE)

## HDR-UK Award

In 2024 the SAMueL team were given a [HDR-UK Reproducibility Award](https://www.hdruk.ac.uk/wp-content/uploads/2024/02/HDRUK-Awards-2024-Brochure.pdf) for the transparency of the project code and for making the models accessible to stroke teams through the Web App

## Use of work

* SAMueL-1 is cited by the most recent national clinical guidelines for stroke care (Royal College of Physicians 2023), in support of the potential for improving thrombolysis rates: [National Clinical Guideline for Stroke for the UK and Ireland](https://www.strokeguideline.org/)

* SAMueL is forming part of an NHS-England led initiative to improve thrombolysis use in England. This is the TASC (Thrombolysis in Acute Stroke Collaboration) team and has launched in October 2023. Teams have access to analysis of their thrombolysis pathways and decision-making through the [SAMueL Web App](https://stroke-predictions.streamlit.app/)

* The [2024 National Stroke Audit review](https://www.strokeaudit.org/Documents/National/Clinical/Apr2022Mar2023/Apr2022Mar2023-AnnualReport.aspx) cites SAMueL work on potential to improve thrombolysis use.





