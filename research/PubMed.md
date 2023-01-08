# 1.) Research
Research articles relating to patient no-show appointments.


## Articles:
- [Patient No-Show Prediction: A Systematic Literature Review](https://pubmed.ncbi.nlm.nih.gov/33286447/)
- [Predicting Patient No-show Behavior: a Study in a Bariatric Clinic](https://pubmed.ncbi.nlm.nih.gov/30209668/)
- [Factors associated with patient no-show rates in an academic otolaryngology practice](https://pubmed.ncbi.nlm.nih.gov/28815608/)
- [Factors Associated with Increased Risk of Patient No-Show in Telehealth and Traditional Surgery Clinics](https://pubmed.ncbi.nlm.nih.gov/32891797/)


## Insight:
### Patient No-Show Prediction: A Systematic Literature Review
This study reviewed 41 different articles, 82% of which were publishing in the last 10 years.  In terms of developing a prediction model, linear regression was the most widely used appearing in 30 of the articles.  In about half of the studies, the following variables were recorded to affect no-shows: **age, gender, insurance, distance, weekday, visit time and lead time**.  **Previous no show appointments** was also a contributor in determining if the action would repeat.  Other variables such as **race, marital status and visit type** were also recorded.  The study states that the use of EHRs will be critical in the future with data collection in order to allow for increased accuracy in prediction models for determining if a patient will be a no show.  
___


### Predicting Patient No-show Behavior: a Study in a Bariatric Clinic
This study conducted a retrospective review of a little over 13 thousand records for about 2660 bariatric patients in Brazil, specifically Rio de Janeiro.  The study quickly lists a few variables that are utilized in prediction no shows.  This includes the following: socio-demographic data, clinical characteristics, appointment information, features of environment, features of the __health professional__, age, gender, race, socioeconomic status, martial status, lead time, previous no show history, datetime of appointment, symptoms, type of appointment, form of payment, and distance to clinic.  Out of the listed variables, there are a few that stood out as the most important to be reviewed: **appointment characteristics** (*lead time, appointment type, datetime of appt, payment methods, prior no show, number of previous appts*), **patient demographics** (*age, gender, race, etc*) & **specialized characteristics** (*healthcare specialty, distance from clinic-residence*).  The study discovered that **women were more likely to no show** when compared to men.  Patients with **private insurance were also likely to no show**.  This is due to the high costs associated with paying medical expenses.  Patients were also seen to **no show after surgery for follow-up with specialties**.  The median age of the patients in this study was 40.  The statistical model utilized in the study was a multiple logistic regression, specializing in lead time, the datetime of the appointment, previous no show history, number of previous appointments and type of appointment.  According to a reduced multiple model, patient no shows were twice as likely to occur during the times of 4:31pm - 6:30pm.  Patients who scheduled between 10:30am - 4:30pm were more likely to show.  Additionaly, appointments made from December - February were most likely to show.  Patients with a lower history of previous overall appointments were more likely to show.  **Age, gender, and weekday were determined __NOT__ to be significant predictors**.  Increased no shows were associated with appointments later in the day (4:30pm or later), post-surgery appointments, high lead-time, no show history, travel time was between 20 - 50km from residence - clinic and other specialities outside of bariatric surgery.  The highest no show age range was between 30 - 44 years old while the highest to show was 59+ year old patients.  Statistical percentage of no show variables are displayed in the results of the study and should be referred to.  
___


### Factors associated with patient no-show rates in an academic otolaryngology practice
This study conducted a retrospective review of all Otolaryngology patients medical charts associated with the University of Kentucky between February 1st, 2015 to January 30th, 2016.  The study obtained information from outpatient EMRs, Allscripts EHR, billing systems and Appscripts practice management system.  It was also noted that all patients received an automated phonecall reminder for their appointment 2-3 days prior.  In the one year study, 4,551 patients out of 22,759 were no shows.  The major contributing variables from this study includes **satellite clinics, new patient visits, younger age groups, and patients on Medicaid**.  Those listed variables were vital in no shows.  Certain **specialities** in Otolaryngology were also listed as increased risk of no shows. 
___


### Factors Associated with Increased Risk of Patient No-Show in Telehealth and Traditional Surgery Clinics
This study conducted a retrospective cohort study of return and postoperative visits from January 2018 to March 2020 from a single tertiary care center.  In the study, 812 patients out of 12,359 were listed as no shows.  A few variables listed to have an effect on no shows includes **race, marital status and clinic specialties** were initially listed.  From the variables, those of African American background were more likely to no show.  Patients who were single or separated were also prone to become no shows.  One thing that was noted, was the fact that eClinic visits (telehealth) increased the odds of no shows.  This study utilized a multivariable logiistic regression to identify patient and clinical factors associated with no shows.  The model displayed that **geographic location did __NOT__ play a siginificant role** in determining no shows.  It was also discussed that **race is associated with technological access**, thus **limiting the options of access to care** (telehealth).  This **increased the no shows for people of color**.  Lastly, single or separated individuals were more likely to no show due to the lack of support.  The study showed that married patients have an increased level of support to attend their appointments from pressure from their spouce.  Thus, **married invdividuals were likely to show to their appointment compared to single or separated**.  
___

## Notable findings:
Across the four articles, there are several repeat variables as well as variables that contradict each other.  From these articles though, I was able to gather a better hold on what variables to look for that are more likely to sway patients towards a no show.  Here are the variables:
1. Patient demographics (age, race, sex, marital status)
2. Datetime of appointment
3. Lead time of appointment
4. Type of visit (routine v. specialty)
5. Previous history (no shows, previous appointments)

One thing I am suprised to see is the debate between the geographic location between the residence and the clinic.  Two studies stated that the distance did play a factor in determining no shows, while one study stated it did not play a role.  The last study did not specifically state the geographic distance, but rather touched on the satellite clinics outside the main care center.  This may not be a determinance of distance, but rather a mentality of better care from a larger centralized center.  

Insurance and payment method is also a key player in these studies; however, that type of information is not currently provided in the dataset.  I may look into the zipcodes of the patients provided on the dataset and look at the county or state and try to assimilate the number or percentage of individuals in those areas who have either private insurance or state/federal insurance such as Medicare/Medicaid (as applicable)