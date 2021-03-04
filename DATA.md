# Classify multilingual emotional speech audio by valence
---

## Application
Emotion recognition is an important part of natural language understanding. Conversational agents accepting voice input have already been deployed in many contexts such as healthcare [[1]](#1) or customer service [[2]](#2) where empathic responses improve the quality of services provided. A crosslingually or multilingually trained classifier can be especially useful when little training data is available for a particular target language [[3]](#3).

[[4]](#4) combined five corpora (German, Italian, and English variants) and attained F1 scores between 89% and 98% and corresponding accuracy scores between 92% and 98% for valence classification. Using a model trained on English and French data, [[3]](#3) achieved an unweighted average recall of 61.73% (English) and 49.33% (French) for valence. [[5]](#5) trained a model on English, German, Italian, and Urdu to obtain an unweighted average recall score of 70.98% for binary (negative and non-negative) valence classification in Urdu. Others have developed multilingual speech emotion recognition systems to classify utterances into affective categories (e.g., happy, sad, angry, neutral, etc.) [[6]](#6)–[[9]](#9). This project builds on prior research by incorporating a broader set of multilingual data: nine English datasets and ten non-English datasets in eight other languages.

## Data
English audio samples with emotion labels are publicly available from the [Carnegie Mellon University Let’s Go Spoken Dialogue Corpus](https://www.ultes.eu/ressources/lego-spoken-dialogue-corpus/) [[10]](#10)–[[11]](#11), [Crowd-sourced Emotional Multimodal Actors Dataset](https://github.com/CheyneyComputerScience/CREMA-D) [[12]](#12)–[[13]](#13), the [Electromagnetic Articulography Database](https://span.usc.edu/owncloud/index.php/s/RTttck1EJ6Vcoyu) [[14]](#14), the [Emotional Voices Database](https://mega.nz/folder/KBp32apT#gLIgyWf9iQ-yqnWFUFuUHg) [[15]](#15), the [JL-Corpus](https://www.kaggle.com/tli725/jl-corpus) [[16]](#16), the [Ryerson Audio-Visual Database of Emotional Speech and Song](https://zenodo.org/record/1188976) [[17]](#17), the [Surrey Audio-Visual Expressed Emotion Database](http://personal.ee.surrey.ac.uk/Personal/P.Jackson/SAVEE/Download.html) [[18]](#18), the [Toronto Emotional Speech Set](https://dataverse.scholarsportal.info/dataset.xhtml?persistentId=doi%3A10.5683%2FSP2%2FE8H2MF) [[19]](#19), and the [Variably Intense Vocalizations of Affect and Emotion Corpus](https://zenodo.org/record/4066235) [[20]](#20).

Most of the English-language datasets are of North American English. The Surrey Audio-Visual Expressed Emotion Database [[18]](#18) is of British English and the JL Corpus [[16]](#16) is of New Zealand English; the Crowd-sourced Emotional Multimodal Actors Dataset [[12]](#12)–[[13]](#13) consists of a variety of other English accents. Although not a full dataset, [[21]](#21) provides six samples (two each of positive, negative, and neutral valence) in Australian English.

Similar spoken corpora with emotion labels are freely available for Arabic ([Arabic Natural Audio Dataset](https://www.kaggle.com/suso172/arabic-natural-audio-dataset)) [[21]](#21), Canadian French ([Canadian French Emotional Speech Database](https://www.gel.usherbrooke.ca/audio/cafe.htm)) [[22]](#22), Estonian ([Estonian Emotional Speech Corpus](https://metashare.ut.ee/repository/download/4d42d7a8463411e2a6e4005056b40024a19021a316b54b7fb707757d43d1a889/)) [[23]](#23), French ([French Emotional Speech Database - Oréau](https://zenodo.org/record/4405783)) [[24]](#24), German ([Berlin Database of Emotional Speech](https://www.kaggle.com/piyushagni5/berlin-database-of-emotional-speech-emodb)) [[25]](#25), Greek ([Acted Emotional Speech Dynamic Database](https://mega.nz/folder/0ShVXY7C#-73kVoK05OjTPEA95UUvMw)) [[26]](#26)–[[27]](#27), Persian ([Sharif Emotional Speech Database](https://github.com/mansourehk/ShEMO)) [[28]](#28), and Urdu ([Urdu Language Speech Dataset](https://www.kaggle.com/bitlord/urdu-language-speech-dataset)) [[6]](#6).

I obtained labeled datasets for Turkish ([BAUM-1](https://archive.ics.uci.edu/ml/datasets/BAUM-1) [[28]](#28) and [BAUM-2](https://archive.ics.uci.edu/ml/datasets/BAUM-2)) [[29]](#29) as well, but the end-user license agreements do not allow for distribution in any way, so they are not uploaded to this project's repository. The same was true of the Surrey Audio-Visual Expressed Emotion Database [[18]](#18).

I considered several other datasets [##], but many of these required an active academic affiliation, were paywalled, or were otherwise inaccessible.

Each dataset was created with different methods, but they share common features that make them suitable for this project:
1. Public or free-use non-commercial access.
1. Audio data per record of natural human speech at the word or utterance level from a single speaker. These were variously obtained from participant elicitation [#], trained actors [#], or television media samples [#]. Some were also associated with video content (not used for this project) [#].
1. A valence classification of either positive, negative, or neutral per record. Each dataset utilized some kind(s) of human verification for these labels. Some were accompanied by intensity ratings [#] or categorical emotion labels [#]; these features were not used for this project.
1. Demonstrated academic or practical application in some context (e.g., conference or journal publication, Kaggle, etc.).
1. Gender for all samples?

(SAVEE, emodb, ravdess is actors
urdu, meld is tv media

## Datasets
* English
  * [CREMA-D](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/CREMA-D) | Crowd-sourced Emotional Multimodal Actors Dataset [[12]](#12)–[[13]](#13)
  * [dzafic](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/dzafic) | Six samples from [[21]](#21)
  * [Emotional_EMA](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/Emotional_EMA) | Electromagnetic Articulography Database [[14]](#14)
  * [EmoV-DB_sorted](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/EmoV-DB_sorted) | Emotional Voices Database [[15]](#15)
  * [enterface_db](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/enterface_db) | name [[]](#)
  * [jl-corpus](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/jl-corpus) | JL-Corpus [[16]](#16)
  * [LEGOv2](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/LEGOv2) | Carnegie Mellon University Let’s Go Spoken Dialogue Corpus [[10]](#10)–[[11]](#11)
  * [ravdess](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/ravdess) | Ryerson Audio-Visual Database of Emotional Speech and Song [[17]](#17)
  * [savee](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/savee) | Surrey Audio-Visual Expressed Emotion Database [[18]](#18)
  * [tess](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/tess) | Toronto Emotional Speech Set [[19]](#19)
  * [vivae](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/vivae) | Variably Intense Vocalizations of Affect and Emotion Corpus [[20]](#20)
* Non-English
  * BAUM-1
  * [aesdd](https://www.github.com/michen00/potential_project_data/tree/main/multilingual_speech_valence_class/aesdd) | Acted Emotional Speech Dynamic Database (Greek) [[26]](#26)–[[27]](#27)
  * [anad](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/anad) | Arabic Natural Audio Dataset [[21]](#21)
  * [cafe](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/cafe) | Canadian French Emotional Speech Database [[22]](#22)
  * [ekorpus](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/ekorpus) | Estonian Emotional Speech Corpus [[23]](#23)
  * [EmoDB](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/EmoDB) | Berlin Database of Emotional Speech (German) [[25]](#25)
  * [oreau2](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/oreau2) | French Emotional Speech Database - Oréau [[24]](#24)
  * [ShEMO](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/ShEMO) | Sharif Emotional Speech Database (Persian) [[28]](#28)
  * [urdu](https://github.com/michen00/multilingual_speech_valence_classification/tree/main/datasets/urdu) | Urdu Language Speech Dataset [[5]](#5)

## References

<span aria-hidden="true"><h6><sub><sup><sub><sup>1</sup></sub></sup></sub></h6></span>

1. L. Laranjo, A. G. Dunn, H. Y. Tong, A. B. Kocaballi, J. Chen, R. Bashir, D. Surian, B. Gallego, F. Magrabi, A. Y. S. Lau, and E. Coiera, "Conversational agents in healthcare: A systematic review," *J. Amer. Med. Inform. Assoc.,* vol. 25, no. 9, pp. 1248–1258, Jul. 11, 2018, doi: https://doi.org/10.1093/jamia/ocy072.

<span aria-hidden="true"><h6><sub><sup><sub><sup>2</sup></sub></sup></sub></h6></span>

2. U. Gnewuch, S. Morana, and A. Maedche, "Towards designing cooperative and social conversational agents for customer service," in *Proc. 38th Int. Conf. Inf. Syst.,* Seoul, South Korea, Dec. 10–13, 2017. Accessed: Mar. 3, 2021. [Online]. Available: https://chatbotresearch.com/wp-content/uploads/2018/06/icis2017.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>3</sup></sub></sup></sub></h6></span>

3. M. Neumann and N. T. Vu, "Cross-lingual and multilingual speech emotion recognition on English and French," in *Proc. IEEE Int. Conf. Acoust., Speech, and Signal Process.,* Calgary, Alberta, Canada, Apr. 15–20, 2018, pp. 5769–5773. doi: https://doi.org/10.1109/ICASSP.2018.8462162.

<span aria-hidden="true"><h6><sub><sup><sub><sup>4</sup></sub></sup></sub></h6></span>

4. K. Zvarevashe and O. O. Olugbara, "Recognition of cross-language acoustic emotional valence using stacked ensemble learning," *Algorithms,* vol. 13, no. 10, p. 246, Sep. 27, 2020, doi: https://doi.org/10.3390/a13100246.

<span aria-hidden="true"><h6><sub><sup><sub><sup>5</sup></sub></sup></sub></h6></span>

5. S. Latif, A. Qayyum, M. Usman, and J. Qadir, "Cross lingual speech emotion recognition: Urdu vs. Western languages," 2020, *arXiv:1812.10411*. Accessed Feb. 10, 2021. [Online]. Available: https://arxiv.org/pdf/1812.10411.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>6</sup></sub></sup></sub></h6></span>

6. R. Elbarougy and M. Akagi, "Cross-lingual speech emotion recognition system based on a three-layer model for human perception," in *2013 Asia-Pacific Signal and Inf. Process. Assoc. Annu. Summit and Conf.,* Kaohsiung, Taiwan, Oct. 29–Nov. 1, 2013, pp. 1-10. doi: https://doi.org/10.1109/APSIPA.2013.6694137.

<span aria-hidden="true"><h6><sub><sup><sub><sup>7</sup></sub></sup></sub></h6></span>

7. P. Heracleous and A. Yoneyama, "A comprehensive study on bilingual and multilingual speech emotion recognition using a two-pass classification scheme," *PLos ONE,* vol. 14, no. 8, p. e0220386, Aug. 15, 2019, doi: https://doi.org/10.1371/journal.pone.0220386.

<span aria-hidden="true"><h6><sub><sup><sub><sup>8</sup></sub></sup></sub></h6></span>

8. X. Li and M. Akagi, "Multilingual speech emotion recognition system based on a three-layer model," in *Proc. Interspeech,* San Francisco, CA, USA, Sep. 8–12, 2016, pp. 3608–3612. doi: https://doi.org/10.21437/Interspeech.2016-645.

<span aria-hidden="true"><h6><sub><sup><sub><sup>9</sup></sub></sup></sub></h6></span>

9. X. Li and M. Akagi, "Improving multilingual speech emotion recognition by combining acoustic features in a three-layer model," *Speech Communication,* vol. 110, pp. 1–12, Jul. 2019, doi: https://doi.org/10.1016/j.specom.2019.04.004.

<span aria-hidden="true"><h6><sub><sup><sub><sup>10</sup></sub></sup></sub></h6></span>

10. A. Schmitt, S. Ultes, and W. Minker, "A parameterized and annotated spoken dialog corpus of the CMU Let’s Go bus information system," in *Int. Conf. Lang. Resour. and Eval.,* Istanbul, Turkey, May 2012, pp. 3369–3373. Accessed: Feb. 8, 2021. Available: http://www.lrec-conf.org/proceedings/lrec2012/pdf/333_Paper.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>11</sup></sub></sup></sub></h6></span>

11. S. Ultes, A. Schmitt, M. J. P. Sánchez, and W. Minker, "Analysis of an extended interaction quality corpus," in *Natural Language Dialog Systems and Intelligent Assistants,* G. G. Lee, H. K. Kim, M. Jeong, and J.-H. Kim, Eds., Cham, Switzerland: Springer Int. Publishing, 2015, pp. 41–52. doi: https://doi.org/10.1007/978-3-319-19291-8_4.

<span aria-hidden="true"><h6><sub><sup><sub><sup>12</sup></sub></sup></sub></h6></span>

12. H. Cao, D. G. Cooper, M. K. Keutmann, R. C. Gur, A. Nenkova, and R. Verma, "CREMA-D: Crowd-sourced Emotional Multimodal Actors Dataset," *IEEE Trans. Affect Comput.,* vol. 5, no. 4, pp. 377–390, Oct./Dec. 2014, doi: https://doi.org/10.1109/TAFFC.2014.2336244.

<span aria-hidden="true"><h6><sub><sup><sub><sup>13</sup></sub></sup></sub></h6></span>

13. M. K. Keutmann, S. L. Moore, A. Savitt, and R. C. Gur, "Generating an item pool for translational social cognition research: Methodology and initial validation," *Behav. Res. Methods,* vol. 47, no. 1, pp. 228–234, Mar. 2015, doi: https://doi.org/10.3758/s13428-014-0464-0.

<span aria-hidden="true"><h6><sub><sup><sub><sup>14</sup></sub></sup></sub></h6></span>

14. S. Lee, S. Yildirim, A. Kazemzadeh, and S. S. Narayanan, "An articulatory study of emotional speech production," in *Proc. InterSpeech,* Lisbon, Portugal, Sep. 4–8, 2005, pp. 497–500. Accessed: Feb. 8, 2021. [Online.] Available: https://sail.usc.edu/ema_web/LeeInterSpeech2005.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>15</sup></sub></sup></sub></h6></span>

15. A. Adigwe, N. Tits, K. El Haddad, S. Ostadabbas, and T. Dutoit, "The Emotional Voices Database: Towards controlling the emotion dimension in voice generation systems," 2018, *arXiv:1806.09514*. Accessed: Feb. 8, 2021. [Online]. Available: https://arxiv.org/pdf/1806.09514.pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>16</sup></sub></sup></sub></h6></span>

16. J. James, L. Tian, and C. Watson, "An open source emotional speech corpus for human robot interaction applications," in *Proc. Interspeech,* Hyderabad, India, Sep. 2–6, 2018, pp. 2768–2772. doi: https://doi.org/10.21437/Interspeech.2018-1349.

<span aria-hidden="true"><h6><sub><sup><sub><sup>17</sup></sub></sup></sub></h6></span>

17. S. R. Livingstone and F. A. Russo, "The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS): A dynamic, multimodal set of facial and vocal expressions in North American English," *PLoS ONE,* vol. 13, no. 5, p. e0196391, May 16, 2018, doi: https://doi.org/10.1371/journal.pone.0196391.

<span aria-hidden="true"><h6><sub><sup><sub><sup>18</sup></sub></sup></sub></h6></span>

18. S. Haq and P. J. B. Jackson, "Multimodal emotion recognition," in *Machine Audition: Principles, Algorithms and Systems,* W. Wang, Ed., IGI Global Press, Jul. 2010, pp. 398–423. doi: https://doi.org/10.4018/978-1-61520-919-4.

<span aria-hidden="true"><h6><sub><sup><sub><sup>19</sup></sub></sup></sub></h6></span>

19. M. K. Pichora-Fuller and K. Dupuis, *Toronto Emotional Speech Set (TESS). V1.* 2020. Distributed by Scholars Portal Dataverse. Accessed: Feb. 8, 2021. doi: https://doi.org/10.5683/SP2/E8H2MF.

<span aria-hidden="true"><h6><sub><sup><sub><sup>20</sup></sub></sup></sub></h6></span>

20. N. Holz, P. Larrouy-Maestri, and D. Poeppel, *The Variably Intense Vocalizations of Affect and Emotion Corpus (VIVAE). V1.* Oct. 5, 2020. Distributed by Zenodo. Accessed: Feb. 8, 2021. [Dataset]. doi: https://doi.org/10.5281/zenodo.4066235.

<span aria-hidden="true"><h6><sub><sup><sub><sup>21</sup></sub></sup></sub></h6></span>

21. I. Dzafic, *Example emotion videos used in investigation of emotion perception in schizophrenia.* 2017. Distributed by the University of Queensland. Accessed: Mar. 3, 2021. [Online]. doi: https://doi.org/10.14264/uql.2017.120.

!!!

<span aria-hidden="true"><h6><sub><sup><sub><sup>21</sup></sub></sup></sub></h6></span>

21. S. Klaylat, *Arabic Natural Audio Dataset Automatic Emotion Recognition. V11.* Dec. 1, 2017. Distributed by Kaggle. Accessed: Feb. 8, 2021. [Online]. Available: https://www.kaggle.com/suso172/arabic-natural-audio-dataset/version/11

<span aria-hidden="true"><h6><sub><sup><sub><sup>22</sup></sub></sup></sub></h6></span>

22. O. Lahaie and P. Gournay, *Canadian French Emotional Speech Database. V1.1.* 2017. Distributed by Groupe de Recherche sur la Parole et l'Audio. Accessed: Feb. 8, 2021. [Online]. Available: https://www.gel.usherbrooke.ca/audio/cafe.htm

<span aria-hidden="true"><h6><sub><sup><sub><sup>23</sup></sub></sup></sub></h6></span>

23. H. Pajupuu, *Eesti Emotsionaalse Kõne Korpus. V5.* Jun. 12, 2012. Distributed by Center of Estonian Language Resources. Accessed: Feb. 9, 2021. [Online]. doi: https://doi.org/10.15155/EKI.000A.

<span aria-hidden="true"><h6><sub><sup><sub><sup>24</sup></sub></sup></sub></h6></span>

24. L. Kerkeni, C. Cleder, Y. Serrestou, and K. Raoff, *French Emotional Speech Database - Oréau. V2.* Dec. 31, 2020. Distributed by Zenodo. Accessed: Feb. 9, 2021. [Dataset]. doi: https://doi.org/10.5281/zenodo.4405783.

<span aria-hidden="true"><h6><sub><sup><sub><sup>25</sup></sub></sup></sub></h6></span>

25. F. Burkhardt, A. Paeschke, M. Rolfes, W. Sendlmeier, and B. Weiss, "A database of German emotional speech," in *Proc. InterSpeech,* Lisbon, Portugal, Sep. 4–8, 2005. Accessed: Feb. 9, 2021. [Online]. Available: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.130.8506&rep=rep1&type=pdf

<span aria-hidden="true"><h6><sub><sup><sub><sup>26</sup></sub></sup></sub></h6></span>

26. N. Vryzas, R. Kotsakis, A. Liatsou, C. A. Dimoulas, and G. Kalliris, "Speech emotion recognition for performance interaction," *J. Audio Eng. Soc.,* vol. 66, no. 6, pp. 457–467, Jun. 2018, doi: https://doi.org/10.17743/jaes.2018.0036.

<span aria-hidden="true"><h6><sub><sup><sub><sup>27</sup></sub></sup></sub></h6></span>

27. N. Vryzas, M. Matsiola, R. Kotsakis, C. Dimoulas, and G. Kalliris, "Subjective evaluation of a speech emotion recognition interaction framework," in *Proc. Audio Mostly 2018 Sound Immersion and Emotion,* North Wales, United Kingdom, Sep. 12–14, 2018, p. 34. Accessed: Feb. 9, 2021. doi: https://doi.org/10.1145/3243274.3243294.

<span aria-hidden="true"><h6><sub><sup><sub><sup>28</sup></sub></sup></sub></h6></span>

28. O. M. Nezami, P. J. Lou, and M. Karami, "ShEMO: A large-scale validated database for Persian speech emotion detection," *Lang. Resour. and Eval.,* vol. 53, no. 1, pp. 1–16, Oct. 8, 2018, doi: https://doi.org/10.1007/s10579-018-9427-x.

<span aria-hidden="true"><h6><sub><sup><sub><sup>29</sup></sub></sup></sub></h6></span>

29. S. Zhalehpour, O. Onder, Z. Akhtar, and C. E. Erdem, "BAUM-1: A spontaneous audio-visual face database of affective and mental states," *IEEE Trans.  Affect. Comput.,* vol. 8, no. 3, pp. 300–313, Jul./Sep. 2017, doi: https:/doi.org/10.1109/TAFFC.2016.2553038.

<span aria-hidden="true"><h6><sub><sup><sub><sup>30</sup></sub></sup></sub></h6></span>

30. C. E. Erdem, C. Turan, Z. Aydin, "BAUM-2: A multilingual audio-visual affective face database," *Multimedia Tools and Applications,* vol. 74, no. 18, pp. 7429–7459, May 9, 2015, doi: https://doi.org/10.1007/s11042-014-1986-2.

add meld
add enterface_db
