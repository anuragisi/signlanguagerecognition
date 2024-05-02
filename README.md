# Sign Language Recognition

This documentation has been updated after a long hiatus, so anticipate that the literature and versions mentioned herein are likely outdated or obsolete. The author conducted this research as part of a B.Tech dissertation from January 2016 to June 2016. Some of the records were subsequently documented and published here.

This is the latest working code of the sign language recognition system which enables us to recognise the symbols as characters easily as we have done researched over the algorithms to try to get the best results in a simple and best way.We have used python 2.7 with OpenCV 3.0 Library.

Let us assume that you have installed opencv 3.0 and python 2.7 correctly.
Then run it as simple as running a python program.

If any error happens let us know,then we will feel happy to help you.

# Gesture Recognition
<p>Gesture recognition is a topic in computer science and language technology with the goal of interpreting human gesture via mathematical algorithms.</p>

<ul>Hardware Tools used in Gesture Recognition:
  <li>1. Wired gloves</li>
  <li>2. Depth-aware cameras</li>
  <li>3. Stereo cameras</li>
  <li>4. Controller-based gestures</li>
  <li>5. Single camera</li>
</ul>

<p>In our project we have implemented sign language recognition on a single camera.</p>

# Algorithms
<ul>Broadly speaking there are 2 different approaches in gesture recognition:
  <li><ul>3D model-based algorithms:
      <li>Volumetric model</li>
      <li>Skeletal models</li></ul>
  </li>
    <li><ul>Appearance-based models:
      <li>Deformable 2D templates.</li>
      <li>Image sequences</li></ul>
  </li>
</ul>

# Methodology
<ul>
<li>Working Environment</li>  
<li>Tools - OpenCV 3.0, Python 2.7</li>
<li>Environment – IDLE (Integrated Development Environment) which is the basic Platform for python.</li>
<li>Experiment Platform - Linux based platform (e.g. Ubuntu 15.10 is a Debian-based Linux Operating System)</li>
</ul>

<samp>
  <img width="472" alt="image" src="https://github.com/anuragprasad95/signlanguagerecognition/assets/3609255/2a5ad89f-bf87-437d-9e70-b734ecfc1dbc">
</samp>

# Implementation
<ul>
  <li>Acquire the image</li>
  <li>Acquiring frames in real time</li>
  <li><ul>Image Preprocessing
    <li>Morphological Transforms</li>
    <li>Blurring</li>
    <li>Thresholding</li>
  </ul>
  </li>
  <li>Extract the largest contour</li>
  <li>Detect hand gesture by finding the defects in a hull</li>
  <li>Contour shape matching algo run</li>
  <li>Printing the Alphabet <samp><img width="463" alt="image" src="https://github.com/anuragprasad95/signlanguagerecognition/assets/3609255/49f263a7-696d-4ee1-a604-044043450323">
</samp></li>
</ul>

# Conclusion
<ul>
<li>Indian Sign Language using object detection and recognition through computer vision was a partly successful one.</li>
<li>The question of perfection is another quest to deal in the days to come.</li>
<li>The hand gesture detection and recognition were the main topic and problem that were dealt
with.</li>
</ul>

# Reference
<ul>
  <li>[1] R. Gopalan and B. Dariush, “Towards a Vision Based Hand Gesture Interface for Robotic Grasping”, The IEEE/RSJ International Conference on Intelligent Robots and Systems, October 11-15, 2009, St. Louis, USA, pp. 1452-1459.</li>

<li>[2] T. Kapuscinski and M. Wysocki, “Hand Gesture Recognition for Man-Machine interaction”, Second Workshop on Robot Motion and Control, October 18-20, 2001, pp. 91-96.</li>

<li>[3] D. Y. Huang, W. C. Hu, and S. H. Chang, “Vision-based Hand Gesture Recognition Using PCA+Gabor Filters and SVM”, IEEE Fifth International Conference on Intelligent Information Hiding and Multimedia Signal Processing, 2009, pp. 1-4.</li>

<li>[4] C. Yu, X. Wang, H. Huang, J. Shen, and K. Wu, “Vision-Based Hand Gesture Recognition Using Combinational Features”, IEEE Sixth International Conference on Intelligent Information Hiding and Multimedia Signal Processing, 2010, pp. 543-546.</li>

<li>[5] J. L. Raheja, K. Das, and A. Chaudhury, “An Efficient Real Time Method of Fingertip Detection”, International Conference on Trends in Industrial Measurements and automation (TIMA), 2011, pp. 447-450.</li>

<li>[6] Manigandan M. and I. M Jackin, “Wireless Vision based Mobile Robot control using Hand Gesture Recognition through Perceptual Color Space”, IEEE International Conference on Advances in Computer Engineering, 2010, pp. 95-99.</li>

<li>[7] A. S. Ghotkar, R. Khatal, S. Khupase, S. Asati, and M. Hadap, “Hand Gesture Recognition for Indian Sign Language”, IEEE International Conference on Computer Communication and Informatics (ICCCI), Jan. 10-12, 2012, Coimbatore, India.</li>

<li>[8] I. G. Incertis, J. G. G. Bermejo, and E.Z. Casanova, “Hand Gesture Recognition for Deaf People Interfacing”, The 18th International Conference on Pattern Recognition (ICPR), 2006.</li>

<li>[9] J. Rekha, J. Bhattacharya, and S. Majumder, “Shape, Texture and Local Movement Hand Gesture Features for Indian Sign Language Recognition”, IEEE, 2011,pp. 30-35.</li>

<li>[10] L. K. Lee, S. Y. An, and S. Y. Oh, “Robust Fingertip Extraction with Improved Skin Color Segmentation for Finger Gesture Recognition in Human-Robot Interaction”, WCCI 2012 IEEE World Congress on Computational Intelligence, June, 10-15, 2012, Brisbane, Australia.</li>

<li>[11] S. K. Yewale and P. K. Bharne, “Hand Gesture Recognition Using Different Algorithms Based on Artificial Neural Network”, IEEE, 2011, pp. 287-292.</li>

<li>[12] Y. Fang, K. Wang, J. Cheng, and H. Lu, “A Real-Time Hand Gesture Recognition Method”, IEEE ICME, 2007, pp. 995-998.</li>

<li>[13] S. Saengsri, V. Niennattrakul, and C.A. Ratanamahatana, “TFRS: Thai Finger-Spelling Sign Language Recognition System”, IEEE, 2012, pp. 457-462.</li>

<li>[14] J. H. Kim, N. D. Thang, and T. S. Kim, “3-D Hand Motion Tracking and Gesture Recognition Using a Data Glove”, IEEE International Symposium on Industrial Electronics (ISIE), July 5-8, 2009, Seoul Olympic Parktel, Seoul , Korea, pp. 1013-1018.</li>

<li>[15] J. Weissmann and R. Salomon, “Gesture Recognition for Virtual Reality Applications Using Data Gloves and Neural Networks”, IEEE, 1999, pp. 2043-2046.</li>

<li>[16] W. W. Kong and S. Ranganath, “Sign Language Phoneme Transcription with PCA-based Representation”, The 9th International Conference on Information and Communications Security(ICICS), 2007, China.</li>

<li>[17] M. V. Lamar, S. Bhuiyan, and A. Iwata, “Hand Alphabet Recognition Using Morphological PCA and Neural Networks”, IEEE, 1999, pp. 2839-2844.</li>

<li>[18] O. B. Henia and S. Bouakaz, “3D Hand Model Animation with a New Data-Driven Method”, Workshop on Digital Media and Digital Content Management (IEEE Computer Society), 2011, pp. 72-76.</li>

<li>[19] M. Pahlevanzadeh, M. Vafadoost, and M. Shahnazi, “Sign Language Recognition”, IEEE, 2007.</li>

<li>[20] J. B. Kim, K. H. Park, W. C. Bang, and Z. Z. Bien, “Continuous Gesture Recognition System for Korean Sign Language based on Fuzzy Logic and Hidden Markov Model”, IEEE, 2002, pp. 1574-1579.</li>

</ul>

Contact us at :
Email - er.anuragprasad@gmail.com
