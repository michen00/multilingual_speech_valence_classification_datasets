Updated at Nov. 5th 2011

<< Contact >>
If you have any question or comments, please do not hesitate and contact us.
Jangwon Kim: jangwon@usc.edu

<< General description >>
This Electromagnetic Articulography (EMA) database includes articulatory motions recorded by an EMA system.
Talkers produced simulated (acted) emotional speech.
A set of 10 sentences was commonly used for speech recording of a male (AB) and two females (JN, LS), who are native speakers of American English.
On top of the 10 sentences, there are 4 additional sentences used for recording by only AB.
Each sentence was produced five times for four different emotions, such as neutrality, anger, sadness and happiness.
In totol, AB produced 280 utterances (14 sentences x 5 repetitions x 4 emotions), and JR and JN produced 200 utterances (10 sentences x 5 repetitions x 4 emotions).
Each utterance was digitalized in 12-bit amplitude resolution with 16kHz sampling rate.
Speech was recorded simultaneously by the EMA system so that speech and corresponding articulatory movements are aligned in time.

The list of 14 sentences are as following.
(1) Your grandmother is on the phone
(2) The doctor made the scar foam with antiseptic
(3) Don't compare me to your father
(4) That made being deaf tantamount to isolation
(5) I hear the echo of voices and the sound of shoes
(6) They think the company and I will have a long future
(7) The doctor made the scar. Foam antiseptic didn't help
(8) I am talking about the same picture you showed me
(9) That dress looks like it comes from Asia
(10) It's hard being very deaf. Tantamount to isolation
(11) I don't know how she could miss this opportunity
(12) Toby and George stole the game
(13) Hold your breath and combine all the ingredients in a large bowl
(14) They vetoed his proposal instantly

The sentences from (1) to (10) were used for all three speakers, and the sentences from (11) to (14) were used for only AB.

The EMA system samples articulatory data at 200Hz and acoustic data at 16kHz.
Each sensor trajectory in the x-direction (forward-backward (horizontal) direction) and in the y-direction (vertical direction) with respect to the system coordinate in recorded by the EMA system.
The corrections for head movement and rotation to the occlusal plane were performed so that the x-axis is parallel to the speaker's occlusal plane.
The position values of TT, Jaw and LL were already smoothed by a 9th order Butterworth filter of cutoff friquency 10Hz.
Finally, the origin of the coordinate system was translated to the upper maxilla reference position.
Each sensor trajectory signal was then differentiated to obtain velocity values, which were smoothed a 9th order Butterworth filter of cutoff friquency 15Hz.
Accelaration values were computed in the same fashion with velocity values.
Those values were saved in *.mat files.
(Lee, S. et. al. Interspeech 2005)



<< Reference >>
You may use below paper as a reference of this EMA database.
Sungbok Lee, Serdar Yildirim, Abe Kazemzadeh, Shrikanth Narayanan
Lee, S., Yildirim, S., Kazemzadeh, A. and Narayanan, S., ``An Articulatory study of emotional speech production.'' Interspeech, Lisbon, Portugal, pp. 497-500, 2005.



<< Description of *.mat files >>
The information in *.mat files is following
(1) speech waveform (sampling rate of audio: 16kHz)
(2) reference marks movement measurements of nose
(3) articulatory movement measurements values of tongue tip (TT), Jaw (jaw or lower incisor) and lower lip (LL). There are also reference measurements, but you may ignore that.



<< How to access data >>
You can access to articulatory data using common MATLAB grammar for structure format data.
Here are Some examples of accessing to the articulatory or audio data in MATLAB

load('rot_4emo_ab_angry_01_001.mat') // Load data in the file rot_4emo_ab_angry_01_001.mat
rot_4emo_ab_angry_01_001(1,1).NAME // read the name of structure (1,1)
audio = rot_4emo_ab_angry_01_001(1,1).SIGNAL // read the signal in the structure (1,1) and save the values in a variable 'audio'
ttSIGNAL = rot_4emo_ab_angry_01_001(1,4).SIGNAL // read the TT movement measurements (position values) and save the values in a variable 'ttSIGNAL'
ttVEL = rot_4emo_ab_angry_01_001(1,4).VEL // read the TT velocity values and save them in a variable 'ttVEL'
ttACCEL = rot_4emo_ab_angry_01_001(1,4).ACCEL // read the TT accelation values and save them in a variable 'ttACCEL'



<< Evaluations by listeners >>
1. The total number of utterances satisfying both (1) high agreement (high evaluation scores (3 or 4)) and (2) successful recording (no missing or bad mat file) for 10 common sentences are as following.
AB: 153, JN: 173, LS: 177

2. The list of the file names which are corrupted or unsuccessfully recorded is following.
AB: mat file for ab_neutral_37_046 is missing due to corruption while collecting the data.
JN: mat file for jn_happy_33 is bad.
JN: mat file for jn_neutral_04 is bad.
JN: mat file for jn_neutral_21 is bad.
LS: mat file for ls_happy_40 is bad.

3. There are two kinds of evaluations. One is for categorical emotion (used in 1. above), and the other is for VAD (valence, activation and dominance).
DocumentationEma.txt and EvaluatorData.txt are evaluation files for VAD.
DocumentationEma.txt contains the raw evaluation results and their mean.
EvaluatorData.txt contains the information of each evaluator for VAD evaluation.



<< Q&A >>
Please read below Q&A carefully before you use this database.

Q1: One 'neutral' file '4emo_ab_neutral_37_046.mat' is missing for ab under "ab/Matfiles".
A1: yes.  Some corrupted mat files are excluded. That's one of them.

Q2: What is "matname(1,4).SIGNAL" for? I mean the one with the name "max".
A2: I think you meant matname(1,3).SIGNAL, not matname(1,4).SIGNAL. matname(1,3) is for maxilary point.
Maxilary and nose markers were used for calibrating the head position.
The movement of the three other articulators, (tongue tip, lower lip, jaw), are relative to the head position.

Q3: How to name the .mat file? e.g. rot_4emo_ab_angry_37_041.mat. What's '041'?
A3: 041 is just data recording index number. 37 should be used when you find its sentence number.
For example, The sentence number of *ab_anger_37* is 7, which is "The doctor made the scar. Foam antiseptic didn't help."

Q4: The reference(Lee, 2005, INTERSPEECH) only talked about one male speaker, it seems that more tasks were done after this publication (e.g. 2 more female speakers, listening test by 4 listeners). So any more document or paper for this?
A4: Same recording and post-processing methods were used for the other data of female speakers'. The only difference is the number of sentences: 14 for AB and 10 for JN and LS.

Q5: For the emotion label file ('/HumanEval/best_xxx_files.txt'), i supposed that the first column is the sound file name, col2-5 is happy, angry, sad, and neutral, is this correct? Then what the 6th column is for? "none of the four emotions" ?
A5: The last column is "Others." There were 5 categories (happy, angry, sad, neutral and others) that listeners could choose as a best-representative emotion for each audio clip. Any emotion other than happy, angry, sad and neutral belongs to 'others.' For example, a listener chooses "others" when he/she feel "surprise" as the most representative emotion for an audio clip.

Q6: What does each column in 'all_sentlevel.matlab.txt' mean? BTW, the number of files for each speaker is AB 153, JN 173, LS 177,,,confused again...why...
A6: Column 1: speaker, Column 2: speaker id (AB:1, JN:2, LS:3), Column 3: mat file name, Column 4: sentence number, Column 5: target emotion (used for speaker), 
Column 6: target emotion index (neutrality: 1, anger: 2, sadness: 3, happiness: 4), Column 7: starting point of speech in the audio mat file (in matname(1,1).SIGNAL)
Column 8: ending point of speech

The total number of utterances satisfying a condition, high agreement between listeners' evaluation results (3 or 4) and target emotion for 10 COMMON SENTENCES, are 154 for AB, 176 for JN, 177 for LS. The 503 utterances in total are those in the all_sentlevel.matlab.txt file.
In above utterances, 1 mat file for AB and 3 mat files for JN are corrupted or missing. One corrupted mat file in LS data did not get high emotion evaluation score from listeners. So, AB has 153 (154-1), JN has 173 (176-3), and LS has 177 (177-0, since corrupted mat file does not belong to the utterance of high emotion evaluation score).



