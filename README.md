# Datasets for multilingual speech valence classification

## Introduction
This repo collects datasets with raw audio that can be used for speech emotion recognition, particularly for training a multilingual speech valence classifier.

To the best of my knowledge, all end-user license agreements for these datasets allow for public or free-use non-commercial access; for those that disallow distribution, there are no requirements for active university affiliation or institutional review board approval.

---

## Contents
* [Application](#Application)
* [Data](#Data)
* [Datasets](#Datasets)
* [References](#References)

---

## Application
Emotion recognition is an important part of natural language understanding. Conversational agents accepting voice input have already been deployed in many contexts such as healthcare [[1]](#1) or customer service [[2]](#2) where empathic responses improve the quality of services provided. A cross-lingually or multilingually trained classifier can be especially useful when little training data is available for a particular target language [[3]](#3).

[[4]](#4) combined five corpora (German, Italian, and English variants) and attained F1 scores between 89% and 98% and corresponding accuracy scores between 92% and 98% for valence classification. Using a model trained on English and French data, [[3]](#3) achieved an unweighted average recall of 61.73% (English) and 49.33% (French) for valence. [[5]](#5) trained a model on English, German, Italian, and Urdu to obtain an unweighted average recall score of 70.98% for binary (negative and non-negative) valence classification in Urdu. Others have developed multilingual speech emotion recognition systems to classify utterances into affective categories (e.g., happy, sad, angry, neutral, etc.) [[6]](#6)–[[9]](#9). This repo is part of a project that builds on prior research by unifying a broader set of multilingual data: 12 English datasets, 9 datasets in non-English languages, and 2 datasets providing both English and non-English speech samples for a total of 24 data sources in 9 languages.

## Data
English audio samples with emotion labels were sourced from the [Carnegie Mellon University Let's Go Spoken Dialogue Corpus](https://www.ultes.eu/ressources/lego-spoken-dialogue-corpus/) [[10]](#10)–[[11]](#11), [Crowd-sourced Emotional Multimodal Actors Dataset](https://github.com/CheyneyComputerScience/CREMA-D) [[12]](#12)–[[13]](#13), the [Electromagnetic Articulography Database](https://span.usc.edu/owncloud/index.php/s/RTttck1EJ6Vcoyu) [[14]](#14), the [EmoReact dataset](https://www.behnaznojavan.com/data) [[15]](#15), the [eNTERFACE '05 Audio-Visual Emotion Database](http://www.enterface.net/enterface05/docs/results/databases/project2_database.zip) [[16]](#16), the [JL Corpus](https://www.kaggle.com/tli725/jl-corpus) [[17]](#17), the [Multimodal EmotionLines Dataset](https://affective-meld.github.io/) [[18]](#18)–[[19]](#19), the [Ryerson Audio-Visual Database of Emotional Speech and Song](https://zenodo.org/record/1188976) [[20]](#20), the [Surrey Audio-Visual Expressed Emotion Database](http://personal.ee.surrey.ac.uk/Personal/P.Jackson/SAVEE/Download.html) [[21]](#21), the [Toronto Emotional Speech Set](https://dataverse.scholarsportal.info/dataset.xhtml?persistentId=doi%3A10.5683%2FSP2%2FE8H2MF) [[22]](#22), and the [Variably Intense Vocalizations of Affect and Emotion Corpus](https://zenodo.org/record/4066235) [[23]](#23).

Most of the English-language datasets are of North American English with some dialectic variations. For instance, the Crowd-sourced Emotional Multimodal Actors Dataset [[12]](#12)–[[13]](#13) (amongst others) consists mostly of Mainstream American English recordings but also some samples of non-standard American English while the Toronto Emotional Speech Set [[22]](#22) was elicited from two actresses recruited from the eponymous metropolitan area in Canada.

On the other hand, the Surrey Audio-Visual Expressed Emotion Database [[21]](#21) is of British English and the JL Corpus [[17]](#17) is of New Zealand English. The eNTERFACE '05 Audio-Visual Emotion Database [[16]](#16) consists of English spoken by participants of fourteen nationalities. Although not a full dataset, [[24]](#24) provides six samples (two each of positive, negative, and neutral valence) in Australian English (prepared for investigation of emotion perception in patients with schizophrenia).

Similar spoken corpora with emotion labels were obtained for Arabic ([Egyptian Arabic speech emotion database](https://www.researchgate.net/publication/341001383_EYASE_Database)) [[25]](#25), Estonian ([Estonian Emotional Speech Corpus](https://metashare.ut.ee/repository/download/4d42d7a8463411e2a6e4005056b40024a19021a316b54b7fb707757d43d1a889/)) [[26]](#26), French ([French Emotional Speech Database - Oréau](https://zenodo.org/record/4405783)) [[27]](#27) and Canadian (Québec) French ([Canadian French Emotional Speech Database](https://www.gel.usherbrooke.ca/audio/cafe.htm)) [[28]](#28), German ([Berlin Database of Emotional Speech](https://www.kaggle.com/piyushagni5/berlin-database-of-emotional-speech-emodb)) [[29]](#29), Greek ([Acted Emotional Speech Dynamic Database](https://mega.nz/folder/0ShVXY7C#-73kVoK05OjTPEA95UUvMw)) [[30]](#30)–[[31]](#31), Persian ([Sharif Emotional Speech Database](https://github.com/mansourehk/ShEMO)) [[32]](#32), Turkish ([BAUM-1](https://archive.ics.uci.edu/ml/datasets/BAUM-1)) [[33]](#33), and Urdu ([Urdu Language Speech Dataset](https://www.kaggle.com/bitlord/urdu-language-speech-dataset)) [[5]](#5).

Two datasets contained non-English samples in addition to English samples: [BAUM-2](https://archive.ics.uci.edu/ml/datasets/BAUM-2) (Turkish) [[34]](#34) and the [Emotional Speech Dataset](https://github.com/HLTSingapore/Emotional-Speech-Data) (Mandarin Chinese) [[35]](#35). Although reported to contain Belgian French samples as well, only the English files of the [Emotional Voices Database](https://mega.nz/folder/KBp32apT#gLIgyWf9iQ-yqnWFUFuUHg) [[36]](#36) were available to me.

The end-user license agreements of BAUM-1 [[33]](#33), BAUM-2 [[34]](#34), the EmoReact dataset [[15]](#15), the Egyptian Arabic speech emotion database [[25]](#25) and the Surrey Audio-Visual Expressed Emotion Database [[21]](#21) do not allow for distribution of the datasets, so the raw data were not uploaded to this repository; to use these datasets, you may need to fill out the appropriate end-user license agreements and/or contact the authors. Otherwise, I tried to preserve the directory structure of each dataset and upload them in full, although I compressed some of the larger subdirectories and files that are irrelevant (e.g., video samples when audio-only samples are also available).

I also included additional documentation (e.g., full-text journal articles) where I could along with some notes and Python scripts I used for file organization. (The scripts were written in a 3.9.6 environment, but most Python 3.x versions should be fine.)

Each dataset was created with different methods, but they share common features that made them suitable for this project:
1. Audio data (or video data with audio) of natural human speech at the utterance level from a single speaker. These were variously obtained via spontaneous participant elicitation (e.g., the eNTERFACE '05 Audio-Visual Emotion Database [[16]](#16) or Estonian Emotional Speech Corpus [[26]](#26)), acted speech (e.g., Ryerson Audio-Visual Database of Emotional Speech and Song [[20]](#20) or Acted Emotional Speech Dynamic Database [[30]](#30)–[[31]](#31)), or media samples from telelvision or films (e.g., the Urdu Language Speech Dataset [[5]](#5) or Multimodal EmotionLines Dataset [[18]](#18)–[[19]](#19))).
1. A single unambiguous valence classification per audio sample of either positive, negative, or neutral — explicitly labeled or directly inferable from the conventional valences of emotion categories where supported by the literature on emotion studies. For instance, samples colored with anger, disgust, fear, or sadness would all be considered negatively valenced and joy is considered positively valenced. Because the valence of states like "concentrating" or "sleepy" are more ambiguous, they would not be considered valid labels for this project. Datasets dealing with sentiment but not emotions were omitted from consideration.
1. Demonstrated academic or practical application in some context (e.g., conference or journal publication, Kaggle, etc.).
1. Public or free-use non-commercial access.

Information about speaker gender was available for all datasets as well (although not always explicitly encoded). All speakers in all datasets were adults with the exception of the EmoReact dataset [[15]](#15), which featured children's English, and the Canadian French Emotional Speech Database [[28]](#28) in which one of the actors was under 18 years old at time of recording.

I considered many other datasets such as those listed in [[38]](#38), but most of these did not meet all the above criteria, required an active academic affiliation, were paywalled, or were otherwise inaccessible or unusable.

## Datasets
* English
  * [CREMA-D](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/CREMA-D) | Crowd-sourced Emotional Multimodal Actors Dataset [[12]](#12)–[[13]](#13)
  * [dzafic](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/dzafic) | Six samples from [[24]](#24)
  * [EmoReact_V_1.0](https://www.github.com/michen00/potential_project_data/tree/main/multilingual_speech_valence_class/tree/main/datasets/EmoReact_V_1.0) | EmoReact dataset [[15]](#15)
  * [Emotional_EMA](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/Emotional_EMA) | Electromagnetic Articulography Database [[14]](#14)
  * [EmoV-DB_sorted](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/EmoV-DB_sorted) | Emotional Voices Database [[35]](#35)
  * [enterface_db](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/enterface_db) | eNTERFACE '05 Audio-Visual Emotion Database [[16]](#16)
  * [jl-corpus](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/jl-corpus) | JL Corpus [[17]](#17)
  * [LEGOv2](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/LEGOv2) | Carnegie Mellon University Let’s Go Spoken Dialogue Corpus [[10]](#10)–[[11]](#11)
  * [MELD](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/MELD) | Multimodal EmotionLines Dataset [[18]](#18)–[[19]](#19)
  * [ravdess](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/ravdess) | Ryerson Audio-Visual Database of Emotional Speech and Song [[20]](#20)
  * [savee](https://www.github.com/michen00/potential_project_data/tree/main/multilingual_speech_valence_class/savee) | Surrey Audio-Visual Expressed Emotion Database [[21]](#21)
  * [tess](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/tess) | Toronto Emotional Speech Set [[22]](#22)
  * [vivae](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/vivae) | Variably Intense Vocalizations of Affect and Emotion Corpus [[23]](#23)
* Non-English
  * [aesdd](https://www.github.com/michen00/potential_project_data/tree/main/multilingual_speech_valence_class/tree/main/datasets/aesdd) | Acted Emotional Speech Dynamic Database (Greek) [[30]](#30)–[[31]](#31)
  * [BAUM1](https://www.github.com/michen00/potential_project_data/tree/main/multilingual_speech_valence_class/tree/main/datasets/BAUM1) | (Turkish) [[33]](#33)
  * [BAUM2](https://www.github.com/michen00/potential_project_data/tree/main/multilingual_speech_valence_class/tree/main/datasets/BAUM2) | (Turkish) [[34]](#34)
  * [cafe](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/cafe) | Canadian French Emotional Speech Database [[28]](#29)
  * [ekorpus](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/ekorpus) | Estonian Emotional Speech Corpus [[26]](#26)
  * [EmoDB](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/EmoDB) | Berlin Database of Emotional Speech (German) [[29]](#29)
  * [esd](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/esd) | Emotional Speech Dataset (Mandarin Chinese and English) [[35]](#35)
  * [EYASE](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/EYASE) | Egyptian Arabic speech emotion database [[25]](#25)
  * [oreau2](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/oreau2) | French Emotional Speech Database - Oréau [[27]](#27)
  * [ShEMO](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/ShEMO) | Sharif Emotional Speech Database (Persian) [[33]](#32)
  * [urdu](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/urdu) | Urdu Language Speech Dataset [[5]](#5)

## References

<span aria-hidden="true"><h6><sub><sup><sub><sup>1</sup></sub></sup></sub></h6></span>

1. L. Laranjo, A. G. Dunn, H. Y. Tong, A. B. Kocaballi, J. Chen, R. Bashir, D. Surian, B. Gallego, F. Magrabi, A. Y. S. Lau, and E. Coiera, "Conversational agents in healthcare: A systematic review," *J. Amer. Med. Inform. Assoc.,* vol. 25, no. 9, pp. 1248–1258, Jul. 11, 2018, doi: https://doi.org/10.1093/jamia/ocy072.

<span aria-hidden="true"><h6><sub><sup><sub><sup>2</sup></sub></sup></sub></h6></span>

2. U. Gnewuch, S. Morana, and A. Maedche, "Towards designing cooperative and social conversational agents for customer service," in *Proc. 38th Int. Conf. Inf. Syst.,* Seoul, South Korea, Dec. 10–13, 2017. Accessed: Mar. 3, 2021. [Online]. Available: https://chatbotresearch.com/wp-content/uploads/2018/06/icis2017.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>3</sup></sub></sup></sub></h6></span>

3. M. Neumann and N. T. Vu, "Cross-lingual and multilingual speech emotion recognition on English and French," in *Proc. IEEE Int. Conf. Acoust., Speech, and Signal Process.,* Calgary, AB, Canada, Apr. 15–20, 2018, pp. 5769–5773. doi: https://doi.org/10.1109/ICASSP.2018.8462162.

<span aria-hidden="true"><h6><sub><sup><sub><sup>4</sup></sub></sup></sub></h6></span>

4. K. Zvarevashe and O. O. Olugbara, "Recognition of cross-language acoustic emotional valence using stacked ensemble learning," *Algorithms,* vol. 13, no. 10, p. 246, Sep. 27, 2020, doi: https://doi.org/10.3390/a13100246.

<span aria-hidden="true"><h6><sub><sup><sub><sup>5</sup></sub></sup></sub></h6></span>

5. S. Latif, A. Qayyum, M. Usman, and J. Qadir, "Cross lingual speech emotion recognition: Urdu vs. Western languages," 2020, *arXiv:1812.10411*. Accessed Feb. 10, 2021. [Online]. Available: https://arxiv.org/pdf/1812.10411.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>6</sup></sub></sup></sub></h6></span>

6. R. Elbarougy and M. Akagi, "Cross-lingual speech emotion recognition system based on a three-layer model for human perception," in *2013 Asia-Pacific Signal and Inf. Process. Assoc. Annu. Summit and Conf.,* Kaohsiung, Taiwan, Oct. 29–Nov. 1, 2013, pp. 1-10. doi: https://doi.org/10.1109/APSIPA.2013.6694137.

<span aria-hidden="true"><h6><sub><sup><sub><sup>7</sup></sub></sup></sub></h6></span>

7. P. Heracleous and A. Yoneyama, "A comprehensive study on bilingual and multilingual speech emotion recognition using a two-pass classification scheme," *PLoS ONE,* vol. 14, no. 8, p. e0220386, Aug. 15, 2019, doi: https://doi.org/10.1371/journal.pone.0220386.

<span aria-hidden="true"><h6><sub><sup><sub><sup>8</sup></sub></sup></sub></h6></span>

8. X. Li and M. Akagi, "Multilingual speech emotion recognition system based on a three-layer model," in *Proc. INTERSPEECH 2016,* San Francisco, CA, USA, Sep. 8–12, 2016, pp. 3608–3612. doi: https://doi.org/10.21437/Interspeech.2016-645.

<span aria-hidden="true"><h6><sub><sup><sub><sup>9</sup></sub></sup></sub></h6></span>

9. X. Li and M. Akagi, "Improving multilingual speech emotion recognition by combining acoustic features in a three-layer model," *Speech Communication,* vol. 110, pp. 1–12, Jul. 2019, doi: https://doi.org/10.1016/j.specom.2019.04.004.

<span aria-hidden="true"><h6><sub><sup><sub><sup>10</sup></sub></sup></sub></h6></span>

10. A. Schmitt, S. Ultes, and W. Minker, "A parameterized and annotated spoken dialog corpus of the CMU Let’s Go bus information system," in *Int. Conf. Lang. Resour. and Eval.,* Istanbul, Turkey, May 2012, pp. 3369–3373. Accessed: Feb. 8, 2021. Available: https://www.academia.edu/21586940/A_Parameterized_and_Annotated_Spoken_Dialog_Corpus_of_the_CMU_Lets_Go_Bus_Information_System

<span aria-hidden="true"><h6><sub><sup><sub><sup>11</sup></sub></sup></sub></h6></span>

11. S. Ultes, A. Schmitt, M. J. P. Sánchez, and W. Minker, "Analysis of an extended interaction quality corpus," in *Natural Lang. Dialog Syst. and Intell. Assistants,* G. G. Lee, H. K. Kim, M. Jeong, and J.-H. Kim, Eds., Cham, Switzerland: Springer Int. Publishing, 2015, pp. 41–52. doi: https://doi.org/10.1007/978-3-319-19291-8_4.

<span aria-hidden="true"><h6><sub><sup><sub><sup>12</sup></sub></sup></sub></h6></span>

12. H. Cao, D. G. Cooper, M. K. Keutmann, R. C. Gur, A. Nenkova, and R. Verma, "CREMA-D: Crowd-sourced Emotional Multimodal Actors Dataset," *IEEE Trans. Affect. Comput.,* vol. 5, no. 4, pp. 377–390, Oct./Dec. 2014, doi: https://doi.org/10.1109/TAFFC.2014.2336244.

<span aria-hidden="true"><h6><sub><sup><sub><sup>13</sup></sub></sup></sub></h6></span>

13. M. K. Keutmann, S. L. Moore, A. Savitt, and R. C. Gur, "Generating an item pool for translational social cognition research: Methodology and initial validation," *Behav. Res. Methods,* vol. 47, no. 1, pp. 228–234, Mar. 2015, doi: https://doi.org/10.3758/s13428-014-0464-0.

<span aria-hidden="true"><h6><sub><sup><sub><sup>14</sup></sub></sup></sub></h6></span>

14. S. Lee, S. Yildirim, A. Kazemzadeh, and S. S. Narayanan, "An articulatory study of emotional speech production," in *Proc. INTERSPEECH 2005,* Lisbon, Portugal, Sep. 4–8, 2005, pp. 497–500. Accessed: Feb. 8, 2021. [Online.] Available: https://sail.usc.edu/ema_web/LeeInterSpeech2005.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>15</sup></sub></sup></sub></h6></span>

15. B. Nojavanasghari, T. Baltrušaitis, C. E. Hughes, and L.-P. Morency, "EmoReact: A multimodal approach and dataset for recognizing emotional responses in children," in *Proc. 18th ACM Int. Conf. Multimodal Interaction,* Tokyo, Japan, Nov. 12–16 2016, pp. 137–144. doi: https://doi.org/10.1145/2993148.2993168.

<span aria-hidden="true"><h6><sub><sup><sub><sup>16</sup></sub></sup></sub></h6></span>

16. O. Martin, I. Kotsia, B. Macq, and I. Pitas, "The eNTERFACE '05 Audio-Visual Emotion Database," in *Proc. 22nd Int. Conf. on Data Eng. Workshops,* Atlanta, GA, USA, Apr. 3–7, 2006, p. 8. doi: https://doi.org/10.1109/ICDEW.2006.145.

<span aria-hidden="true"><h6><sub><sup><sub><sup>17</sup></sub></sup></sub></h6></span>

17. J. James, L. Tian, and C. Watson, "An open source emotional speech corpus for human robot interaction applications," in *Proc. INTERSPEECH 2018,* Hyderabad, India, Sep. 2–6, 2018, pp. 2768–2772. doi: https://doi.org/10.21437/Interspeech.2018-1349.

<span aria-hidden="true"><h6><sub><sup><sub><sup>18</sup></sub></sup></sub></h6></span>

18. S.-Y. Chen, C.-C. Hsu, C.-C. Kuo, T.-H. Huang, and L.-W. Ku, "EmotionLines: An emotion corpus of multi-party conversations," 2018, *arXiv:1802.08379v2*. Accessed: Mar. 4, 2021. [Online]. Available: https://arxiv.org/pdf/1802.08379.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>19</sup></sub></sup></sub></h6></span>

19. S. Poria, D. Hazarika, N. Majumder, G. Naik, E. Cambria, and R. Mihalcea, "MELD: A multimodal multi-party dataset for emotion recognition in conversations," 2018, *arXiv:1810.02508v6*. Accessed: Mar. 4, 2021. [Online]. Available: https://arxiv.org/pdf/1810.02508.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>20</sup></sub></sup></sub></h6></span>

20. S. R. Livingstone and F. A. Russo, "The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS): A dynamic, multimodal set of facial and vocal expressions in North American English," *PLoS ONE,* vol. 13, no. 5, p. e0196391, May 16, 2018, doi: https://doi.org/10.1371/journal.pone.0196391.

<span aria-hidden="true"><h6><sub><sup><sub><sup>21</sup></sub></sup></sub></h6></span>

21. S. Haq and P. J. B. Jackson, "Multimodal emotion recognition," in *Machine Audition: Principles, Algorithms and Systems,* W. Wang, Ed., Hershey, PA, USA: IGI Global Press, 2011, pp. 398–423. doi: https://doi.org/10.4018/978-1-61520-919-4.ch017.

<span aria-hidden="true"><h6><sub><sup><sub><sup>22</sup></sub></sup></sub></h6></span>

22. M. K. Pichora-Fuller and K. Dupuis, *Toronto Emotional Speech Set (TESS). V1.* 2020. Distributed by Scholars Portal Dataverse. Accessed: Feb. 8, 2021. doi: https://doi.org/10.5683/SP2/E8H2MF.

<span aria-hidden="true"><h6><sub><sup><sub><sup>23</sup></sub></sup></sub></h6></span>

23. N. Holz, P. Larrouy-Maestri, and D. Poeppel, *The Variably Intense Vocalizations of Affect and Emotion Corpus (VIVAE). V1.* Oct. 5, 2020. Distributed by Zenodo. Accessed: Feb. 8, 2021. [Dataset]. doi: https://doi.org/10.5281/zenodo.4066235.

<span aria-hidden="true"><h6><sub><sup><sub><sup>24</sup></sub></sup></sub></h6></span>

24. I. Dzafic, *Example emotion videos used in investigation of emotion perception in schizophrenia.* 2017. Distributed by the University of Queensland. Accessed: Mar. 3, 2021. [Online]. doi: https://doi.org/10.14264/uql.2017.120.

<span aria-hidden="true"><h6><sub><sup><sub><sup>25</sup></sub></sup></sub></h6></span>

25. L. Abdel-Hamid, "Egyptian Arabic speech emotion recognition using prosodic, spectral, and wavelet features," *Speech Communication,* vol. 122, pp. 19–30, Sep. 2020, doi: https://doi.org/10.1016/j.specom.2020.04.005.

<span aria-hidden="true"><h6><sub><sup><sub><sup>26</sup></sub></sup></sub></h6></span>

26. H. Pajupuu, *Eesti Emotsionaalse Kõne Korpus. V5.* Jun. 12, 2012. Distributed by Center of Estonian Language Resources. Accessed: Feb. 9, 2021. [Online]. doi: https://doi.org/10.15155/EKI.000A.

<span aria-hidden="true"><h6><sub><sup><sub><sup>27</sup></sub></sup></sub></h6></span>

27. L. Kerkeni, C. Cleder, Y. Serrestou, and K. Raoff, *French Emotional Speech Database - Oréau. V2.* Dec. 31, 2020. Distributed by Zenodo. Accessed: Feb. 9, 2021. [Dataset]. doi: https://doi.org/10.5281/zenodo.4405783.

<span aria-hidden="true"><h6><sub><sup><sub><sup>28</sup></sub></sup></sub></h6></span>

28. O. Lahaie and P. Gournay, *Canadian French Emotional Speech Database. V1.1.* 2017. Distributed by Groupe de Recherche sur la Parole et l'Audio. Accessed: Feb. 8, 2021. [Online]. Available: https://www.gel.usherbrooke.ca/audio/cafe.htm

<span aria-hidden="true"><h6><sub><sup><sub><sup>29</sup></sub></sup></sub></h6></span>

29. F. Burkhardt, A. Paeschke, M. Rolfes, W. Sendlmeier, and B. Weiss, "A database of German emotional speech," in *Proc. INTERSPEECH 2005,* Lisbon, Portugal, Sep. 4–8, 2005. Accessed: Feb. 9, 2021. [Online]. Available: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.130.8506&rep=rep1&type=pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>30</sup></sub></sup></sub></h6></span>

30. N. Vryzas, R. Kotsakis, A. Liatsou, C. A. Dimoulas, and G. Kalliris, "Speech emotion recognition for performance interaction," *J. Audio Eng. Soc.,* vol. 66, no. 6, pp. 457–467, Jun. 2018, doi: https://doi.org/10.17743/jaes.2018.0036.

<span aria-hidden="true"><h6><sub><sup><sub><sup>31</sup></sub></sup></sub></h6></span>

31. N. Vryzas, M. Matsiola, R. Kotsakis, C. A. Dimoulas, and G. Kalliris, "Subjective evaluation of a speech emotion recognition interaction framework," in *Proc. Audio Mostly 2018 Sound Immersion and Emotion,* North Wales, United Kingdom, Sep. 12–14, 2018, p. 34. doi: https://doi.org/10.1145/3243274.3243294.

<span aria-hidden="true"><h6><sub><sup><sub><sup>32</sup></sub></sup></sub></h6></span>

32. O. M. Nezami, P. J. Lou, and M. Karami, "ShEMO: A large-scale validated database for Persian speech emotion detection," *Lang. Resour. and Eval.,* vol. 53, no. 1, pp. 1–16, Oct. 8, 2018, doi: https://doi.org/10.1007/s10579-018-9427-x.

<span aria-hidden="true"><h6><sub><sup><sub><sup>33</sup></sub></sup></sub></h6></span>

33. S. Zhalehpour, O. Onder, Z. Akhtar, and C. E. Erdem, "BAUM-1: A spontaneous audio-visual face database of affective and mental states," *IEEE Trans.  Affect. Comput.,* vol. 8, no. 3, pp. 300–313, Jul./Sep. 2017, doi: https://doi.org/10.1109/TAFFC.2016.2553038.

<span aria-hidden="true"><h6><sub><sup><sub><sup>34</sup></sub></sup></sub></h6></span>

34. C. E. Erdem, C. Turan, and Z. Aydin, "BAUM-2: A multilingual audio-visual affective face database," *Multimedia Tools and Applications,* vol. 74, no. 18, pp. 7429–7459, May 9, 2015, doi: https://doi.org/10.1007/s11042-014-1986-2.

<span aria-hidden="true"><h6><sub><sup><sub><sup>35</sup></sub></sup></sub></h6></span>

35. K. Zhou, B. Sisman, R. Liu, and H. Li, "Seen and unseen emotional style transfer for voice conversion with a new emotional speech dataset," 2020, *arXiv:2010.14794v2*. Accessed Mar. 3, 2021. [Online]. Available: https://arxiv.org/pdf/2010.14794.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>36</sup></sub></sup></sub></h6></span>

36. A. Adigwe, N. Tits, K. El Haddad, S. Ostadabbas, and T. Dutoit, "The Emotional Voices Database: Towards controlling the emotion dimension in voice generation systems," 2018, *arXiv:1806.09514*. Accessed: Feb. 8, 2021. [Online]. Available: https://arxiv.org/pdf/1806.09514.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>37</sup></sub></sup></sub></h6></span>

37. M. Noordewier and S. Breugelmans, “On the valence of surprise,” *Cognition and Emotion,* vol. 27, no. 7, pp. 1326–1334, Apr. 2013, doi: https://doi.org/10.1080/02699931.2013.777660.

<span aria-hidden="true"><h6><sub><sup><sub><sup>38</sup></sub></sup></sub></h6></span>

38. A. Malek. "SER-datasets." Github. https://github.com/SuperKogito/SER-datasets (accessed Mar. 4, 2021).
