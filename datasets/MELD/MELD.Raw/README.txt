           

MELD: Multimodal EmotionLines Dataset for Emotion Recognition in Multiparty Conversation
                         			                               
Version 1.0

September 30th, 2018
                                
Soujanya Poria‡, Devamanyu HazarikaΦ, Navonil Majumder†, Gautam Naik‡, Erik Cambria‡, Rada Mihalcea*
‡School of Computer Science and Engineering, Nanyang Technological Univerisity, Singapore
†Centro de Investigacion en Computacion, Instituto Politecnico Nacional, Mexico ´
ΦSchool of Computing, National University of Singapore, Singapore
*Computer Science & Engineering, University of Michigan, Ann Arbor, USA

sporia@ntu.edu.sg, hazarika@comp.nus.edu.sg, navo@nlp.cic.ipn.mx,
gautam@sentic.net, cambria@ntu.edu.sg, mihalcea@umich.edu
									

CONTENTS
1. Introduction
2. Purpose
3. Dataset Creation
4. Paper
5. Raw Data
6. Description of the .csv files
7. Citation


=======================
1. Introduction

Multimodal EmotionLines Dataset (MELD) has been created by enhancing and extending EmotionLines dataset. MELD contains the same dialogue instances available in EmotionLines, but it also encompasses audio and visual modality along with text. MELD has more than 1300 dialogues and 13000 utterances from Friends TV series. Multiple speakers participated in the dialogues. Each utterance in a dialogue has been labeled by any of these seven emotions -- Anger, Disgust, Sadness, Joy, Neutral, Surprise and Fear. MELD also has sentiment (positive, negative and neutral) annotation for each utterance.

Please visit https://affective-meld.github.io for more details.

=======================
2. Purpose

Multimodal data analysis exploits information from multiple-parallel data channels for decision making. With the rapid growth of AI, multimodal emotion recognition has gained a major research interest, primarily due to its potential applications in many challenging tasks, such as dialogue generation, multimodal interaction etc. A conversational emotion recognition system can be used to generate appropriate responses by analyzing user emotions. Although there are numerous works carried out on multimodal emotion recognition, only a very few actually focus on understanding emotions in conversations. However, their work is limited only to dyadic conversation understanding and thus not scalable to emotion recognition in multi-party conversations having more than two participants. EmotionLines can be used as a resource for emotion recognition for text only, as it does not include data from other modalities such as visual and audio. At the same time, it should be noted that there is no multimodal multi-party conversational dataset available for emotion recognition research. In this work, we have extended, improved, and further developed the EmotionLines dataset for the multimodal scenario. Emotion recognition in sequential turns has several challenges and contex understanding is one of them. The emotion change and emotion flow in the sequence of turns in a dialogue make accurate context modeling a difficult task. In this dataset, as we have access to the multimodal data sources for each dialogue, we hypothesize that it will improve the context modeling thus benefiting the overall emotion recognition performance.  This dataset can also be used to develop a multimodal affective dialogue system. 

=======================
3. Dataset Creation

The first step deals with finding the timestamp of every utterance in each of the dialogues present in the EmotionLines dataset. To accomplish this, we crawled through the subtitle files of all the episodes which contains the beginning and the end timestamp of the utterances. This process enabled us to obtain season ID, episode ID, and timestamp of each utterance in the episode. We put two constraints whilst obtaining the timestamps: (a) timestamps of the utterances in a dialogue must be in increasing order, (b) all the utterances in a dialogue have to belong to the same episode and scene.
Constraining with these two conditions revealed that in EmotionLines, a few dialogues consist of multiple natural dialogues. We filtered out those cases from the dataset. Because of this error correction step, in our case, we have the different number of dialogues as compare to the EmotionLines. After obtaining the timestamp of each utterance, we extracted their corresponding audio-visual clips from the source episode. Separately, we also took out the audio content from those video clips. Finally, the dataset contains visual, audio, and textual modality for each dialogue.

=======================
4. Paper

The paper explaining this dataset can be found - https://github.com/SenticNet/MELD/blob/master/MELD.pdf

=======================
5. Raw data

Please visit https://affective-meld.github.io to download the raw data. The data is stored in .mp4 format and can be found in the XXX.tar.gz files.

=======================
6. Description of the .csv files

Column Specification
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Column Name  | Description                                                                                                                              |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Sr No.       | Serial numbers of the utterances mainly for referencing the utterances in case of different versions or multiple copies with different   |
|              | subsets.                                                                                                                                 |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Utterance    | Individual utterances from EmotionLines as a string.                                                                                     |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Speaker      | Name of the speaker associated with the utterance.                                                                                       |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Emotion      | The emotion (neutral, joy, sadness, anger, surprise, fear, disgust) expressed by the speaker in the utterance.                           |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Sentiment    | The sentiment (positive, neutral, negative) expressed by the speaker in the utterance.                                                   |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Dialogue_ID  | The index of the dialogue starting from 0.                                                                                               |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Utterance_ID | The index of the particular utterance in the dialogue starting from 0.                                                                   |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Season       | The season no. of Friends TV Show to which a particular utterance belongs.                                                               |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Episode      | The episode no. of Friends TV Show in a particular season to which the utterance belongs.                                                |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| StartTime    | The starting time of the utterance in the given episode in the format 'hh:mm:ss,ms'.                                                     |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+
| EndTime      | The ending time of the utterance in the given episode in the format 'hh:mm:ss,ms'.                                                       |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------+

The files
- train_sent_emo.csv - contains the utterances in the training set along with Sentiment and Emotion labels.
- dev_sent_emo.csv - contains the utterances in the dev set along with Sentiment and Emotion labels.
- test_sent_emo.csv - contains the utterances in the test set along with Sentiment and Emotion labels.

=======================
7. Citation

Please cite the following papers if you find this dataset useful in your research

S. Poria, D. Hazarika, N. Majumder, G. Naik, E. Cambria, R. Mihalcea. Multimodal EmotionLines: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversation. (2018)

Chen, S.Y., Hsu, C.C., Kuo, C.C. and Ku, L.W. EmotionLines: An Emotion Corpus of Multi-Party Conversations. arXiv preprint arXiv:1802.08379 (2018).

