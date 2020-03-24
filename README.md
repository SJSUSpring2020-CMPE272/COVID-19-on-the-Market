# COVID-19 Effect on the Market

# Suggested - Candidate for seizure predictions?

## Project Idea 1

1. Pneumonia Detection

2. 1 million adults seek out medical attention from complications caused by pneumonia every year, and 50,000 die from the disease. In order to treat this, doctors must first determine if pneumonia is present. In order to do that, doctors examine chest x-ray scans to find certain infections in the lungs. This requires ample time for the doctors to check out, and if the doctor is overburdened with dozens of x-rays to examine, it could take a long time for patients to get their results, and seek treatment right away. This project utilizes the help of IBM Watson to create a machine learning model that will learn from images of chest scans that have pneumonia present or not present. From this, doctors can use to assist in diagnosing to speed up the process and efficiency.

3. This is in no way to replace doctors, but to add extra evidence and confidence that their conclusion is correct. With pneumonia being so common throughout all ages, it is important, especially during the season, to confirm every patient who has this sickness. 

4. The project will utilize IBM Watson Image Recognition API to be accompanied with Backend/Front technologies like HTML, CSS, NodeJS, etc.

Dataset: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia


## Project Idea 2

1. Heart Disease Detection

2. About 600,000 Americans die from heart disease each year, which accounts for 
1/4 deaths. Doctors try to diagnose these problems as soon as possible to give proper care to 
patients. Looking at results of blood and other related tests can prolong the time it takes for
A patient to receive treatment. This project should allow for the input of various test data, and determine whether the
person associated with the test has a heart disease or not. Machine learning can be used to create a model based on the given data set. We can also deploy it on the cloud and create a good UI using frontend/backend technologies. 

3. This is for doctors who are usually busy attending to other patients that time for diagnosis becomes
Rather lengthy to perform. Our hope is that an application to speed up the diagnosis processes will allow
For doctors to speed up the time it takes to finalize results so that it would increase the efficiency
Of getting patients treated. Also, a patient can also use this application if they have the results themselves.

4. Machine Learning
   -tensorflow
   -keras
   -pandas

   Kaggle Dataset stored in a database like mySQL/mongo. https://www.kaggle.com/ronitf/heart-disease-uci

   Deployment to AWS EC2.

   Nodejs, HTML, CSS, REST API's


   
   

## Project Idea 3
1. Prediction of Wild Fire causes

2. About 80% of every wildfires are caused by humans. (https://nhmu.utah.edu/sites/default/files/attachments/Wildfire%20FAQs.pdf) Wildfires are devasting to the environment, as many animals and houses are lost. Prevention of the causes of these 
widespread fires are of the upmost priority in preserved wildlife and protecting towns. If investigators could predict what 
was the causes of these fires, it could assist in leading them to the possible culprit. Using Machine Learning on an existing dataset, we can use Tensorflow/Keras to create a model for predicting root causes of wild fires. MySQL databases can store this data , and receive more when fires occur. We can also have a user interface, as well as deployment on a cloud. 

3. The goal of this project is to ultimately prevent these fires from happening in the first place. Given fires occurring in California, Australia, and in the Amazon, the damages are immeasurable. We hope that past data on fire causes would provide some insight on what could have started, and potentially lead to finding culprits responsible.

4. Machine Learning
   -tensorflow
   -keras
   -pandas
   
   
   Kaggle Dataset stored in a database like mySQL/mongo. https://www.kaggle.com/new-york-state/nys-forest-ranger-wildland-fire-reporting

   Deployment to AWS EC2.

   Nodejs, HTML, CSS, REST API's





## Project Idea 4

1. Recipe Suggester

2. Many people have a lot of food just in their pantries or refrigerators and do not know what to do with all the food that they have stored away. People will be able to add the ingredients (either by manually inputting or uploading photos of them) that they own and will be shown suggested recipes based on those ingredients. Users can also refine the results by adding additional constraints such as recipe ratings, time, cost, nutrition, and dietary restrictions.

3. This is to help people figure out what to cook, based on what ingredients they already have. This project can help them empty out their pantries or refrigerators by suggesting recipes that use ingredients that they have, and will also help people become more environmentally friendly by reducing food waste.

4. Machine Learning
   -IBM Watson Visual Recognition
   -tensorflow
   -keras
   -pandas
   
   Kaggle Dataset stored in a database like mySQL/mongo. https://www.kaggle.com/hugodarwood/epirecipes
   
   Deployment to AWS EC2.

   Nodejs, HTML, CSS, REST API's
   
## Project Idea 5
   
1. Student's Assistant
   
2. Some students are not auditory learners. Students go to lecture, get distracted, and only hear a small percentage of what the professor says. This means that not only is the students' time wasted, the professor's time is also wasted since not all of his/her words are being absorbed. The professor's use of his time would be maximized if all students absorbed 100% of his words. One way to achieve this is to use voice-to-text to write down all of the professor's words. We can take this one step further and create an application that. This also helps students with hearing disabilities.
   
   A) creates a full text rendition of the lecture. This would involve 
	   i) sorting the word-for-word content according to which slide they were on (i.e. Slide1 content, Slide2 content, etc.)
	   ii) filtering out unnecessary words like "um" 
      iii) fixing grammar and punctuation to make the content more readable 
	   iv) create paragraphs instead of just having a monologue

   B) Part B of the application would involve the application extracting key facts and presenting a compact summary of the lecture. It       can create lists of topics, identify definitions, and has a search functionality. 
   
3) Having a text version of each lecture allows students to review each lecture effectively and efficiently. Students who are visual learners will appreciate being able to read lectures. The professor will be happy knowing his words are absorbed. 

4) Python Speech Recognition, HTML, CSS, MongoDB, Python, AWS, NodeJS, Machine Learning -tensorflow -keras -pandas
https://www.kaggle.com/rtatman/english-word-frequency 


