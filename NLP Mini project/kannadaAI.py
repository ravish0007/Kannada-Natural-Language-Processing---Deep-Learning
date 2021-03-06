from __future__ import division #used to calculate probability division, without this division relults in 0

#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#
#from __future__ import division #used to calculate probability division, without this division relults in 0

sample_memo = '''
ಕರ್ನಾಟಕದ ಹೊಸಜಿಲ್ಲೆ ರಾಮನಗರಕ್ಕೆ ಸೇರಿದ ಒಂದು ಪಟ್ಟಣ. ಇದೇ ಹೆಸರಿನ ತಾಲ್ಲೂಕಿನ ಆಡಳಿತ ಕೇಂದ್ರ. ಹಿಂದೆ ಬೆಂಗಳೂರು ಜಿಲ್ಲೆಗೆ ಸೇರಿತು. 23.08.07ರಿಂದ ರಾಮನಗರ ಜಿಲ್ಲೆಗೆ ಸೇರಿತು. ಉ.ಅ. 12ಂ 33' ಮತ್ತು ಪು.ರೇ. 77ಂ 29' ನಲ್ಲಿ ಅರ್ಕಾವತಿ ನದಿಯ ಬಲದಂಡೆಯ ಮೇಲೆ, ಉತ್ತರ ದಕ್ಷಿಣವಾಗಿ ಹಬ್ಬಿದೆ. ಬೆಂಗಳೂರು-ಮಳವಳ್ಳಿ ರಸ್ತೆಯಲ್ಲಿರುವ ಈ ಪಟ್ಟಣ ಬೆಂಗಳೂರಿನ ದಕ್ಷಿಣಕ್ಕೆ 58 ಕಿಮೀ ದೂರದಲ್ಲಿದೆ. ರಾಮನಗರ ರೈಲ್ವೆ ನಿಲ್ದಾಣಕ್ಕೆ ಇಲ್ಲಿಂದ 27 ಕಿಮೀ ಅಂತರವಿದೆ. ಪಟ್ಟಣದ ಜನಸಂಖ್ಯೆ 47,047 (2001). 1974ರ ವರೆಗೂ ಇದಕ್ಕೆ ಕಾನಕಾನಹಳ್ಳಿ ಎಂಬ ಹೆಸರಿತ್ತು. ಕಾನಕಾನನೆಂಬವ ಇಲ್ಲಿ ಒಂದು ಸಣ್ಣ ಕೋಟೆ ಕಟ್ಟಿಕೊಂಡಿದ್ದರಿಂದ ಇದಕ್ಕೆ ಈ ಹೆಸರು ಬಂತೆಂದು ಹೇಳಲಾಗಿದೆ. ಕಾನಿಕಾರ್ನ ಹಳ್ಳಿ ಎಂಬುದು ಮೂಲನಾಮವೆಂದೂ ಕಾಣಿಕಾರ್ (ನೆಲದೊಡೆಯ) ಎಂಬುದರಿಂದ ಈ ಹೆಸರು ಬಂತೆಂದೂ ಇಲ್ಲಿಯ ಜನ ತಿಳಿದು ಕೊಂಡಿದ್ದಾರೆಂದೂ ಆದರೆ ವಾಸ್ತವವಾಗಿ ಇದು ಕನ್ಯಾ-ಕರ್ಣ (ಭವಾನಿಯ ಕಿವಿ) ಎಂದಿರಬೇಕೆಂದೂ ಬುಕಾನನ್ ಅಭಿಪ್ರಾಯಪಟ್ಟಿದ್ದಾನೆ. 13ನೆಯ ಶತಮಾನದ ಶಾಸನವೊಂದರಲ್ಲಿ ಇದರ ಹೆಸರು ಕಾಣಿಕಾರಹಳ್ಳಿ. ಈಗ ಇದರ ಹೆಸರು ಕನಕಪುರ ಎಂದಿರುವುದರಿಂದ ಹಳೆಯ ಹೆಸರನ್ನು ಕುರಿತ ವಾದ ಅಷ್ಟಾಗಿ ಮುಖ್ಯವಲ್ಲ.

ಕನಕಪುರದಲ್ಲಿರುವ ಕೋಟೆಯನ್ನು ಕಟ್ಟಿಸಿದಾತ ಚನ್ನಪಟ್ಟಣದ ಪಾಳೆಗಾರನಾಗಿದ್ದ ಜಗದೇವರಾಯ ಎಂದು ಹೇಳಲಾಗಿದೆ. ಆತ ಇಲ್ಲಿದ್ದ ಸಣ್ಣ ಕೋಟೆಯ ಸ್ಥಳದಲ್ಲಿ ಇದನ್ನು ಕಟ್ಟಿಸಿದ. 1630ರಲ್ಲಿ ಇದನ್ನು ಮೈಸೂರಿನ ಚಾಮರಾಜ ಗೆದ್ದುಕೊಂಡ. ಇಲ್ಲಿ ಜೀರ್ಣವಾದ ರಂಗನಾಥ ದೇವಾಲಯವಿದೆ. ಶ್ರೀರಂಗಪಟ್ಟಣದ ಕಡೆಗೆ ನುಗ್ಗಿಬರುತ್ತಿದ್ದ ಬ್ರಿಟಿಷ್ ಸೇನೆಗೆ ಠಾವು ದೊರೆಯದಿರಲೆಂಬ ಉದ್ದೇಶದಿಂದ ಟಿಪ್ಪುಸುಲ್ತಾನ ಎರಡು ಸಾರಿ ಈ ಪಟ್ಟಣವನ್ನು ಹಾಳುಗೆಡವಿದ. ಅನಂತರ ಬಹುಕಾಲ ಕೋಟೆಯೊಳಗಡೆಯಲ್ಲಿ ಹುಲಿಯೇ ಮುಂತಾದ ದುಷ್ಟಮೃಗಗಳು ಸೇರಿಕೊಂಡು ಮನುಷ್ಯರನ್ನೂ ದನಕರುಗಳನ್ನೂ ಎತ್ತಿಕೊಂಡು ಹೋಗುತ್ತಿದ್ದುವು.

ಹಸಿರು ಹೊದೆದ ಬೆಟ್ಟಗಳ ನಡುವೆ ಮಲಗಿರುವ ಕನಕಪುರ ಒಂದು ರಮ್ಯಪ್ರದೇಶ. ಅರ್ಕಾವತಿಯ ದಂಡೆಯ ಮೇಲೆ ಹಬ್ಬಿದ ತೆಂಗಿನ ಮರಗಳ ಸಾಲು ಈ ಪಟ್ಟಣಕ್ಕೆ ಹಸುರು ಕುಚ್ಚಿನ ಅಂಚು ಕಟ್ಟಿದಂತಿದೆ. ಶಿವಸಮುದ್ರ ಮತ್ತು ಶಿಂಷಾಗಳಿಂದ ಬರುವ ವಿದ್ಯುತ್ ಕನಕಪುರದಿಂದ ಮುಂದೆ ರಾಮನಗರ, ಬೆಂಗಳೂರು, ಕೋಲಾರದ ಚಿನ್ನದ ಗಣಿ ಮುಂತಾದ ಎಡೆಗಳಿಗೆ ಸಾಗುತ್ತದೆ. ರೇಷ್ಮೆ ಬಿತ್ತನೆ ಕೋಠಿಗಳೂ ರೇಷ್ಮೆಗೂಡಿನಿಂದ ನೂಲು ಸುತ್ತುವ ಕಾರ್ಖಾನೆಯೂ (ಫಿಲೇಚರ್ಸ್‌) ಇಲ್ಲುಂಟು. ಶಾಲಾ ಕಾಲೇಜೂ ಇವೆ. ಪ್ರತಿ ಗುರುವಾರವೂ ಇಲ್ಲಿ ನಡೆಯುವ ಸಂತೆ ಸುತ್ತೆಲ್ಲ ಪ್ರಸಿದ್ಧ.

ಕನಕಪುರ ತಾಲ್ಲೂಕು ರಾಮನಗರ ಜಿಲ್ಲೆಯ ಅತ್ಯಂತ ದಕ್ಷಿಣದಲ್ಲಿದೆ. ಎಲೆಯಾಕಾರದ, ಕಾವೇರಿ ಜಲಾನಯನ ಭೂಮಿಯ ಪುರ್ವಭಾಗದಲ್ಲಿರುವ ಈ ತಾಲ್ಲೂಕಿನ ಪುರ್ವದಲ್ಲಿ ತಮಿಳುನಾಡಿನ ಸೇಲಂ ಜಿಲ್ಲೆ, ಈಶಾನ್ಯದಲ್ಲಿ ಆನೆಕಲ್ ತಾಲ್ಲೂಕು, ಉತ್ತರದಲ್ಲಿ ದಕ್ಷಿಣ ಬೆಂಗಳೂರು ತಾಲ್ಲೂಕು, ವಾಯವ್ಯದಲ್ಲಿ ರಾಮನಗರ ತಾಲ್ಲೂಕು, ಪಶ್ಚಿಮದಲ್ಲಿ ಚನ್ನಪಟ್ಟಣ ಮತ್ತು ಮಳವಳ್ಳಿ ತಾಲ್ಲೂಕುಗಳು, ದಕ್ಷಿಣದಲ್ಲಿ ಕಾವೇರಿ ನದಿ, ಅದರ ಬೆನ್ನಿಗೇ ಕೊಳ್ಳೆಗಾಲ ತಾಲ್ಲೂಕು ಇವೆ. ವಿಸ್ತೀರ್ಣ 161,460 ಚ ಕಿಮೀ. ಇದು ಇಡೀ ಜಿಲ್ಲೆಯಲ್ಲೇ ಅತ್ಯಂತ ದೊಡ್ಡ ತಾಲ್ಲೂಕು. ನೆಲಮಂಗಲದ ಪಶ್ಚಿಮದ ಕಡೆಯಿಂದ ಬರುವ ಶಿಲಾಬೆಟ್ಟಗಳು ಮಾಗಡಿ, ರಾಮನಗರ ತಾಲೂಕುಗಳನ್ನು ಹಾಯ್ದು, ಈ ತಾಲ್ಲೂಕನ್ನು ಉತ್ತರಭಾಗದಿಂದ ಪ್ರವೇಶಿಸಿ, ಪುರ್ವ, ಪಶ್ಚಿಮ ಮತ್ತು ದಕ್ಷಿಣ ಅಂಚಿನಲ್ಲಿ ಕವಚದಂತೆ ಒತ್ತಾಗಿ ಹಬ್ಬಿವೆ. ಉತ್ತರದಿಂದ ದಕ್ಷಿಣದ ಕಾವೇರಿ ಕಣಿವೆಯ ಕಡೆಗೆ ನೆಲ ಇಳಿಜಾರಾಗಿದೆ. ಪಶ್ಚಿಮದಲ್ಲಿ ಬಾಣಂತಿ ಮಾರಿಬೆಟ್ಟ (104 ಕಿಮೀ), ಭೀಮಕಂಡಿ, ಕಡಕಲ್, ಮುದವಾಡ ಮತ್ತು ನರಸಿಂಹದೇವರ ಬೆಟ್ಟಗಳೂ ಆಗ್ನೇಯದಲ್ಲಿ ದೇವರಬೆಟ್ಟ, ಕೊಪ್ಪಬೆಟ್ಟ (860 ಮೀ), ಬರೀಕಲ್ಲು ಬೆಟ್ಟಗಳೂ ಪುರ್ವದಲ್ಲಿ ಬಿಳೀಕಲ್ಲು ಬೆಟ್ಟ, ಗುಲಕಲ್ ಬೆಟ್ಟಗಳೂ ನೈಋತ್ಯದಲ್ಲಿ ಪತ್ರಧಾರಿದೇವ ಇತ್ಯಾದಿ ಬೆಟ್ಟಗಳೂ ಉತ್ತರದಲ್ಲಿ ಗಂಗಾಧರನ ಬೆಟ್ಟವೂ ಇವೆ. ತಾಲ್ಲೂಕಿನ ನೈಋತ್ಯ ಭಾಗದಲ್ಲಿ ಚಾರ್ನಕೈಟ್ ಶಿಲಾಪದರಗಳಿವೆ. ಉಳಿದ ಕಡೆಗಳಲ್ಲಿರುವುದು ಬೆಣಚುಕಲ್ಲಿನ ಶಿಲೆಗಳು. ರಾಮನಗರದ ಕಣಶಿಲಾ (ಗ್ರಾನೈಟ್) ಸಮುದಾಯ ಕನಕಪುರದಿಂದ ಪ್ರಾರಂಭವಾಗಿ ಉತ್ತರದಲ್ಲಿ ರಾಮನಗರದ ಕಡೆಗೆ ಹರಡಿದೆ. ಈ ಶಿಲೆಗಳದು ಗೋಳಾಕೃತಿ. ಚಾರ್ನಕೈಟ್ನಂತಿರುವ ಡೈಕ್ ಮತ್ತು ಹಾರ್ನ್‌ಬ್ಲೆಂಡ್ ಶಿಲೆಗಳು ಹಾರೋಹಳ್ಳಿಗೆ ವಾಯವ್ಯದಲ್ಲಿವೆ. ಸಾಲಹುಣಿಸೆ ಮತ್ತು ಮರಳವಾಡಿ ಬಳಿ ಪದ್ಮರಾಗ ಶಿಲೆ ಉಂಟು.

ತಾಲ್ಲೂಕಿನ ದಕ್ಷಿಣದಲ್ಲಿ ತ್ರಿಭುಜಾಕೃತಿಯ ಪ್ರದೇಶದಲ್ಲಿರುವುದು ಎರೆಮಣ್ಣು, ಉಳಿದ ಕಡೆಗಳಲ್ಲಿ ಅಗ್ನಿಶಿಲೆಯಿಂದಾದ, ಹಗುರ ರಚನೆಯುಳ್ಳ ಕೆಂಪು ಮಣ್ಣಿದೆ.

ಕಾವೇರಿಯ ಉಪನದಿಯಾದ ಅರ್ಕಾವತಿ ವಾಯವ್ಯದಿಂದ ಪ್ರವೇಶಿಸಿ, ತಾಲ್ಲೂಕಿನ ಮಧ್ಯದಲ್ಲಿ ಉತ್ತರ-ದಕ್ಷಿಣವಾಗಿ ಹರಿದು, ಸಂಗಮದ ಬಳಿ ಕಾವೇರಿಯನ್ನು ಸೇರುತ್ತದೆ. ಅರ್ಕಾವತಿಗೆ ಎರಡೂ ಕಡೆಗಳಿಂದ ಬಂದು ಸೇರುವ ನದಿಗಳೂ ಹೊಳೆಗಳೂ ಅನೇಕ. ವೃಷಭಾವತಿ ನದಿ ಈ ತಾಲ್ಲೂಕನ್ನು ಪ್ರವೇಶಿಸುವಾಗಲೇ ಮುದುವಾಡಿಯ ಬಳಿ ಅರ್ಕಾವತಿಯನ್ನು ಸೇರುತ್ತದೆ. ಈಶಾನ್ಯದ ಕಡೆಯಿಂದ ಹರಿದು ಬರುವ ಅಂತರಗಂಗೆ, ಬಸವನ ಹೊಳೆ, ಕೂಟ್ಲೆ ಹೊಳೆಗಳು ಒಂದುಗೂಡಿ ಅರ್ಕಾವತಿಯನ್ನು ಸೇರುವುದು ಕನಕಪುರದ ಬಳಿ. ಆಗ್ನೇಯ ಎಲ್ಲೆಯವರೆಗೂ ದೊಡ್ಡ ಹೊಳೆ ಹರಿದು ಬಂದು ಸಂಗಮದ ಎದುರು ದಂಡೆಯಲ್ಲಿ ಮಾಹಳ್ಳಿಯ ಬಳಿ ಅರ್ಕಾವತಿಯನ್ನು ಕೂಡಿಕೊಳ್ಳುತ್ತದೆ. ಪಶ್ವಿಮದ ಕಡೆಯಿಂದ ಉಯ್ಯಂ ಬಳ್ಳಿ-ಕಬ್ಬಾಳ ರಸ್ತೆಗೆ ಸಮಾನಾಂತರವಾಗಿ ಹರಿದು ಅರ್ಕಾವತಿಯನ್ನು ಸೇರುವುದೇ ಬಂಡಿಹಳ್ಳ. ಮೇಯಿಂದ ನವೆಂಬರ್ವರೆಗೆ ನೈಋತ್ಯ ಮಾರುತಗಳಿಂದ ಇಲ್ಲಿ 70-75 ಸೆಂಮೀ ಮಳೆಯಾಗುತ್ತದೆ. (ಕನಕಪುರ 75 ಸೆಂಮೀ, ಕೋಡಿಹಳ್ಳಿ 71 ಸೆಂಮೀ, ಸಾತನೂರು 75 ಸೆಂಮೀ). ಬೆಂಗಳೂರು ಜಿಲ್ಲೆಯಲ್ಲಿ ಒಂದೇ ದಿನದಲ್ಲಿ ಅತ್ಯಂತ ಹೆಚ್ಚಿನ ಮಳೆ ಆದದ್ದೆಂದರೆ ಕನಕಪುರದಲ್ಲಿ-1897ರ ಸೆಪ್ಟೆಂಬರ್ 22ರಂದು (22.5 ಸೆಂಮೀ).

ಬೆಟ್ಟದ ಕಾಡುಗಳಿಂದ ಕೂಡಿದ ಈ ತಾಲ್ಲೂಕಿನಲ್ಲಿ ಸರ್ಕಾರಸಂರಕ್ಷಿತ ಅರಣ್ಯಗಳು ಅನೇಕ ಉಂಟು. ದಕ್ಷಿಣದಲ್ಲಿ ಚಿಲಂದವಾಡಿ, ಆಗ್ನೇಯದಲ್ಲಿ ಮೂಗೂರು, ಪಶ್ಚಿಮದಲ್ಲಿ ಕಬ್ಬಾಳ. ತಲ್ಲೂರು ಮತ್ತು ಬಾಣಂತಿಮಾರಿ, ಪುರ್ವದಲ್ಲಿ ಬಿಳಿಕೆರೆ ಮತ್ತು ಈಶಾನ್ಯದಲ್ಲಿ ರಾಗಿಹಳ್ಳಿಗಳಲ್ಲಿ ಸಂರಕ್ಷಿತ ಕಾಡುಗಳಿವೆ. ಕನಕಪುರದ ಸುತ್ತಮುತ್ತ ತೇಗ, ಹೊನ್ನೆ, ಬೀಟೆ, ಕಮ್ಮಾರ ಮುಂತಾದ ಮರಗಳುಂಟು. ಶ್ರೀಗಂಧದ ಮರಗಳೂ ತಕ್ಕಮಟ್ಟಿಗೆ ಬೆಳೆಯುತ್ತವೆ.

ಉತ್ತರ ಮತ್ತು ಮಧ್ಯಭಾಗಗಳಲ್ಲಿ ನದಿ-ಹೊಳೆಗಳ ದಡಗಳಲ್ಲಿ ವ್ಯವಸಾಯ ಸಾಧ್ಯ. ಅರ್ಕಾವತಿ ನದೀಬಂiÀÄಲು ಮುಖ್ಯವಾದದ್ದು.ಒಟ್ಟು ಬೇಸಾಯದ ನೆಲ 70,106 ಹೆ. ಜಿಲ್ಲೆಯಲ್ಲಿ ಬೇಸಾಯಕ್ಕೊಳಗಾಗಿರುವ ನೆಲದಲ್ಲಿ 1/6 ಭಾಗ ಇಲ್ಲಿದೆ. ಆಹಾರ ಧಾನ್ಯಗಳನ್ನು ಬೆಳೆಯುವ ಪ್ರದೇಶ 45,622 ಹೆ. (61.72%), ತೋಟಗಾರಿಕೆ ಪ್ರದೇಶ (1,88 ಹೆ (2.54%), ವಾಣಿಜ್ಯ ಬೆಳೆ ಬೆಳೆಯುವ ಪ್ರದೇಶ 25,256 ಹೆ. (34.17%), ನೀರಾವರಿಗೊಳಪಟ್ಟ ಪ್ರದೇಶ 10,828 ಹೆ. (15.45%), ಬತ್ತ, ರಾಗಿ, ಹಿಪ್ಪನೇರಳೆ, ಅವರೆ, ತೆಂಗು, ಹರಳು, ಹುಣಿಸೆ, ಕುಂಬಳಕಾಯಿ ಇತರ ಮುಖ್ಯ ಬೆಳಸುಗಳು. ನೀರಾವರಿ ಅನುಕೂಲವಿದ್ದರೆ ಈ ತಾಲ್ಲೂಕಿನಲ್ಲಿ ಇನ್ನೂ ಹೆಚ್ಚು ಫಸಲು ತೆಗೆಯಬಹುದು. ಕನಕಪುರದ ದಕ್ಷಿಣಕ್ಕೆ 12 ಕಿಮೀ ಮೈಲಿ ದೂರದಲ್ಲಿರುವ 25 ಲಕ್ಷ ರೂ ವೆಚ್ಚದ ಸಾತನೂರು ಯೋಜನೆ ಮಧ್ಯಮ ತರಗತಿಯ ನೀರಾವರಿ ಯೋಜನೆಗಳಲ್ಲೊಂದು. ಇದರ ಆಯಕಟ್ಟಿನಿಂದ 4047 ಹೆ. ನೆಲ ನೀರಾವರಿಗೆ ಒಳಪಡುತ್ತದೆ. ಮೇಕೆದಾಟು ವಿದ್ಯುತ್ ಯೋಜನೆಯೂ ಪರಿಶೀಲನೆ ಯಲ್ಲಿದೆ. ಈ ತಾಲ್ಲೂಕಿನಲ್ಲಿ ನೂರಕ್ಕೂ ಹೆಚ್ಚು ಕೆರೆಗಳಿವೆ. ಇವು ಬಹುತೇಕ ಸಣ್ಣವು.

ತಾಲ್ಲೂಕಿನ ವಾಯವ್ಯ ಭಾಗದಲ್ಲಿ ಪದ್ಮರಾಗವೂ ಹಾರೋಶಿವರದ ಪಶ್ಚಿಮದಲ್ಲಿ ಕಬ್ಬಿಣದ ಅದಿರೂ ದೊರೆಯುತ್ತವೆ. ರೈಲುಮಾರ್ಗವಿಲ್ಲದ ಈ ತಾಲ್ಲೂಕಿನಲ್ಲಿ ರಸ್ತೆಗಳು ತಕ್ಕಮಟ್ಟಿಗೆ ಅಭಿವೃದ್ಧಿ ಹೊಂದಿವೆಯೆನ್ನಬಹುದು. ಒಟ್ಟು ರಸ್ತೆ ಉದ್ದ 748 ಕಿಮೀ ಸುಧಾರಿತ ರಸ್ತೆಗಳೆ ಹೆಚ್ಚು. ಕನಕಪುರ ಪಟ್ಟಣ ಇವುಗಳ ಕೇಂದ್ರ. ಬೆಂಗಳೂರು-ಮಳವಳ್ಳಿ-ಮೈಸೂರು ರಸ್ತೆ ಇದರ ಮುಖಾಂತರ ಹಾದುಹೋಗುತ್ತದೆ. ಹಲಗೂರು-ಕನಕಪುರ, ಚನ್ನಪಟ್ಟಣ-ಹಸನಹಳ್ಳಿ, ರಾಮನಗರ-ಕನಕಪುರ, ಚನ್ನಪಟ್ಟಣ-ಕನಕಪುರ ಇವು ಇತರ ರಸ್ತೆಗಳು. ಸು. 7291 ಟೆಲಿಪೋನ್ ಸಂಪರ್ಕ ಹಾಗೂ 58 ಅಂಚೆ ಕಛೇರಿಗಳಿವೆ.

ಹಾರೋಹಳ್ಳಿ, ಕನಕಪುರ, ಮರಳವಾಡಿ, ಕೋಡಿಹಳ್ಳಿ, ಸಾತನೂರು, ಉಯ್ಯಂಬಳ್ಳಿ-ಇವು ಈ ತಾಲ್ಲೂಕಿನ ಹೋಬಳಿಗಳು. ಒಟ್ಟು ಹಳ್ಳಿಗಳ ಸಂಖ್ಯೆ 229, ಜನಸಂಖ್ಯೆ 1951ರಲ್ಲಿ 1,68,789 ಇದ್ದುದು 1961ರಲ್ಲಿ 1,98,053 ಆಯಿತು. ತಾಲ್ಲೂಕಿನ ಜನಸಂಖ್ಯೆ 3,37,208 (2001). ಸರಾಸರಿ ಸಾಕ್ಷರತೆ ಶೇ. 50, ನಗರ ಜನಸಂಖ್ಯೆ : 47,060. (ಕೆ.ಆರ್.ಆರ್. )
ಕರ್ನಾಟಕ ಪಠ್ಯಪುಸ್ತಕಗಳು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಲಭ್ಯವಿವೆ ಇಲ್ಲಿ ಕ್ಲಿಕ್ ಮಾಡಿ. ದ್ರಾವಿಡ ಭಾಷೆಗಳಲ್ಲಿ ಪ್ರಾಮುಖ್ಯವುಳ್ಳ ಭಾಷೆಯೂ ಭಾರತದ 
ಪುರಾತನವಾದ ಭಾಷೆಗಳಲ್ಲಿ ಒಂದೂ ಆಗಿರುವ ಕನ್ನಡ ಭಾಷೆಯನ್ನು ಅದರ 
ವಿವಿಧ ರೂಪಗಳಲ್ಲಿ ಸುಮಾರು ೪೫ ದಶಲಕ್ಷ ಜನರು ಆಡು ನುಡಿಯಾಗಿ ಬಳಸುತ್ತಲಿದ್ದಾರೆ. ಕನ್ನಡ ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಆಡಳಿತ ಭಾಷೆ.
ಜಗತ್ತಿನಲ್ಲಿ ಅತ್ಯಂತ ಹೆಚ್ಚು ಮಂದಿ ಮಾತನಾಡುವ ಭಾಷೆಯೆಂಬ ನೆಲೆಯಲ್ಲಿ ಇಪ್ಪತೊಂಬತ್ತನೆಯ ಸ್ಥಾನ ಕನ್ನಡಕ್ಕಿದೆ. ೨೦೧೧ರ ಜನಗಣತಿಯ 
 ಜಗತ್ತಿನಲ್ಲಿ ೬.೪ ಕೋಟಿ ಜನಗಳು ಕನ್ನಡ ಮಾತನಾಡುತ್ತಾರೆ ಎಂದು ತಿಳಿದುಬಂದಿದೆ. ಇವರಲ್ಲಿ ೫.೫ ಕೋಟಿ ಜನಗಳ ಮಾತೃಭಾಷೆ ಕನ್ನಡವಾಗಿದೆ. 
 ಬ್ರಾಹ್ಮಿ ಲಿಪಿಯಿಂದ ರೂಪುಗೊಂಡ ಕನ್ನಡ ಲಿಪಿಯನ್ನು ಉಪಯೋಗಿಸಿ ಕನ್ನಡ ಭಾಷೆಯನ್ನು ಬರೆಯಲಾಗುತ್ತದೆ. ಕನ್ನಡ ಬರಹದ ಮಾದರಿಗಳಿಗೆ 
 ಸಾವಿರದ ಐನೂರು ವರುಷಗಳ ಚರಿತ್ರೆಯಿದೆ. ಕ್ರಿ.ಶ. ಆರನೆಯ ಶತಮಾನದ ಪಶ್ಚಿಮ ಗಂಗ ಸಾಮ್ರಾಜ್ಯದ ಕಾಲದಲ್ಲಿ ಮತ್ತು ಒಂಬತ್ತನೆಯ 
 ಶತಮಾನದ ರಾಷ್ಟ್ರಕೂಟ ಸಾಮ್ರಾಜ್ಯದ ಕಾಲದಲ್ಲಿ ಹಳಗನ್ನಡ ಸಾಹಿತ್ಯ ಅತ್ಯಂತ ಹೆಚ್ಚಿನ ಹೆಚ್ಚಿನ ರಾಜಾಶ್ರಯ ಪಡೆಯಿತು. ಅದಲ್ಲದೆ 
 ಸಾವಿರ ವರುಷಗಳ ಸಾಹಿತ್ಯ ಪರಂಪರೆ ಕನ್ನಡಕ್ಕಿದೆ. ವಿನೋಬಾ ಭಾವೆ ಕನ್ನಡ ಲಿಪಿಯನ್ನು ಲಿಪಿಗಳ ರಾಣಿಯೆಂದು ಹೊಗಳಿದ್ದಾರೆ.
 ಕನ್ನಡದಲ್ಲಿ ಸಂಸ್ಕೃತದ ಪ್ರಭಾವ ಅಸಾಧಾರಣವಾದುದು. ಪ್ರಾಕೃತ, ಪಾಳಿ ಮುಂತಾದ ಭಾಷೆಗಳ ಪ್ರಭಾವವೂ ಕನ್ನಡಕ್ಕಿದೆ. ಕ್ರಿ.ಪೂ ಮೂರನೆಯ 
 ಶತಮಾನಕ್ಕೂ ಮುನ್ನವೇ ಕನ್ನಡ ಭಾಷೆಯನ್ನು ಮೌಖಿಕ ಪರಂಪರೆಯ ಭಾಷೆಯಾಗಿ ರೂಪುಗೊಂಡಿತ್ತೆಂಬುದಕ್ಕೂ ಪ್ರಾಕೃತ ಭಾಷೆಯಲ್ಲಿಯೂ ತಮಿಳು ಭಾಷೆಯಲ್ಲಿಯೂ 
 ಬರೆಯಲ್ಪಟ್ಟ ಶಾಸನಗಳಲ್ಲಿ ಕನ್ನಡದ ಶಬ್ದಗಳು ಬಳಕೆಯಾಗಿವೆಯೆಂದೂ ಇತಿಹಾಸ ತಜ್ಞ ಐರಾವತಂ ಮಹಾದೇವನ್ ಸಾಬೀತುಪಡಿಸಿದ್ದಾರೆ. ಆ ಸಂಶೋಧನೆಯ
 ಪ್ರಕಾರ ಕನ್ನಡ ಭಾಷೆಯನ್ನು ಅಗಾಧ ಪ್ರಮಾಣದ ಜನತೆ ಮಾತನಾಡುತ್ತಿದ್ದ ಭಾಷೆಯಾಗಿದ್ದಿತೆಂದೂ ತಿಳಿದುಬಂದಿದೆ
 ಣಿಚ್ಚವು ಹೊಸದಾಗಿರುವಂಕಾಕ್ಷರ ದಚ್ಚುಗಳೊಳಗೊಂಬತ್ತು
ಣೊಚ್ಚಿತ್ತು ಬಿನ್ನತ್ತಾಗಿರುತರುವಂಕದ ಅಚ್ಚಕಾವ್ಯಕೆ ಸೊನ್ನೆಯಾದಿಮ್

ನುಣುಪಾದ ಸೊನ್ನೆಯ ಮಧ್ಯದೊಳ್ ಕೂಡಿಸೆ ಗಣಿತರ್ಗೆ ಲೆಕ್ಕವ ತರುವ
ಅಣಿಯಾದ ಸೊನ್ನೆಗೆ ಮಣಿಯುತ ನಾನೀಗ ಗುಣಕರ್ಗೆ ಭೂವಲಯವನು

ವರುಷಭಾರತದೊಳು ಬೆಳಗುವೆತ್ತಿಹ ಕಾವ್ಯ ಕರುನಾಡ ಜನರಿಗನಾದಿ
ಅರುಹನಾಗಮದೊಂದಿಗೆ ನಯ ಬರುವಂತೆ ವರಕಾವ್ಯವನ್ನು ಕನ್ನದಿಪೆ

ಪುರ ಜಿನನಾಥ ತನ್ನಂಕದೊಳ್ ಬ್ರಾಹ್ಮಿಗೆ ಅರವತ್ನಾಲ್ಕಕ್ಷರವಿತ್ತ
ವರಕುವರಿಯರು ಸೌಂದರಿಗೆ ಒಂಬತ್ತನು ಕರುಣಿಸಿದನು ಸೊನ್ನೆ ಸಹಿತ

ಕನ್ನಡದೊಂದೆರಳ್ ಮೂರುನಾಲ್ಕೈದಾರು ಮುನ್ನ ಏಳೆಂಟೊಂಬತೆಂಬ
ಉನ್ನತವಾದಂಕ ಸೊನ್ನೆಯಿಂ ಹುಟ್ಟಿತೆಂದೆನ್ನುವುದನು ಕಲಿಸಿದನು

ಸರ್ವಜ್ಞದೇವನು ಸರ್ವಾಂಗದಿಂ ಪೇಳ್ದ ಸರ್ವಸ್ವ ಭಾಷೆಯ ಸರಣಿಗೆ
ಸಕಲವ ಕರ್ಮಾಟದಣುರೂಪ ಹೊಂದುತ ಪ್ರಕಟದ ಓಂದರೋಳ್ ಅಡಗಿ

ಹದಿನೆಂಟು ಭಾಷೆಯ ಮಹಾಭಾಷೆಯಾಗಲು ಬದಿಯ ಭಾಷೆಗಳೇಳುನೂರು
ಹೃದಯದೊಳಡಗಿಸಿ ಕರ್ಮಾಟ ಲಿಪಿಯಾಗಿ ಹುದುಗಿದಂಕ ಭೂವಲಯ

ಪರಭಾಷೆಗಳೆಲ್ಲ ಸಂಯೋಗವಾಗಲು ಸರಸ ಶಬ್ದಾಗಮ ಹುಟ್ಟಿ
ಸರವದು ಮಾಲೆಯಾದತಿಶಯ ಹಾರದ ಸರಸ್ವತಿ ಕೊರಳ ಆಭರಣ
ಭಾರತದ ರಾಜ್ಯಗಳ ರಚನೆ ಮಾನದಂಡಗಳು ಭಾಷೆ [ ಮತ್ತು ರಾಜಕಾರಣಿಗಳು ಈ ದಿನಗಳಲ್ಲಿ ! ] . ಭಾರತ 1950 ರಲ್ಲಿ ಭಾಷಾವಾರು ಪ್ರಾಂತ್ಯಗಳು ರೂಪುಗೊಂಡವು ಅದೇ ವರ್ಷದ ಗಣರಾಜ್ಯವಾದ . ಮೈಸೂರು ರಾಜ್ಯವನ್ನು ದಕ್ಷಿಣ ಭಾರತದಲ್ಲಿ ಅಂತಹ ರಾಜ್ಯವಾಗಿದೆ .ಮೈಸೂರು ರಾಜ್ಯದ ರಾಜರ ಆಳ್ವಿಕೆಯ ಪ್ರದೇಶಗಳಾಗಿದ್ದವು. ಈಗಿನ ಉತ್ತರ ಕರ್ನಾಟಕ ಮತ್ತು ಹೈದರಾಬಾದ್ ಕರ್ನಾಟಕ ಎಂದು ಹಲವಾರು ಜಿಲ್ಲೆಗಳಿಗೆ , ಹೊಸ ರಾಜ್ಯದಲ್ಲಿ ಕರಗಿದ. ಮೈಸೂರು ರಾಜ್ಯದ ಹೆಸರು ನವೆಂಬರ್ 1 , 1973 ರಂದು ಕರ್ನಾಟಕ ಬದಲಾಯಿಸಲಾಯಿತು .

ರಾಜ್ಯದ ಕೊನೆಯಲ್ಲಿ ದೇವರಾಜ ಅರಸು ನಂತರ ಮುಖ್ಯಮಂತ್ರಿ ಈ ಹೆಗ್ಗುರುತು ನಿರ್ಧಾರ ತೆಗೆದುಕೊಂಡಿತು . ಅಧಿಕೃತವಾಗಿ ಹೊಸ ರಾಜ್ಯದ ನವೆಂಬರ್ 1 ರಂದು ಉದಯಿಸಿತು, ಮತ್ತು ಈ ದಿನವನ್ನು ರಾಜ್ಯದಲ್ಲಿ ಪ್ರತಿ ವರ್ಷ ರಾಜ್ಯೋತ್ಸವವಾಗಿ ಆಚರಿಸಲಾಗುತ್ತದೆ . ಈ ಜನಪ್ರಿಯವಾಗಿ ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ಅಥವಾ ಕರ್ನಾಟಕ ರಾಜ್ಯೋತ್ಸವ ಕರೆಯಲಾಗುತ್ತದೆ .

ಆರಂಭದಲ್ಲಿ ಹೆಸರು ಬದಲಾವಣೆ ಎಲ್ಲಾ ಮೂಲಕ ಅವರುಗಳಿಗೆ ಉತ್ತೇಜನ ನೀಡಲಾಯಿತು ಮಾಡಲಾಯಿತು . ಹೆಸರು ಕನ್ನಡ ಮತ್ತು ಕರ್ನಾಟಕದ ಏಕತೆಯ ಪ್ರಜ್ಞೆ ಬಡಿದೆಬ್ಬಿಸಿತು . ಆದರೆ ಕಳೆದ ಕೆಲವು ವರ್ಷಗಳಲ್ಲಿ ಇದು ಉತ್ಸಾಹ ಎಲ್ಲಾ ಆದರೆ ಅಲ್ಪಾಯುಷ್ಯದ ಯೂಫೋರಿಯಾ ಎಂದು ಎಲ್ಲಾ ಸಮಂಜಸ ಅನುಮಾನಗಳನ್ನು ಮೀರಿ ಸಾಬೀತಾಯಿತು ಇದೆ .

ಕರ್ನಾಟಕ ಆಹ್ಲಾದಕರ ಮನಸ್ಥಿತಿ ಇರುತ್ತದೆ ನವೆಂಬರ್ 1 ಬಂದು . ಈ ದಿನ ಸರ್ಕಾರಿ ರಜಾ. ಕೆಲವೇ ಕನ್ನಡ ಪಠಣ ಬೀದಿಗಳಲ್ಲಿ ಮತ್ತು ಸಮುದಾಯ ಕೇಂದ್ರಗಳಲ್ಲಿ ಔಟ್ ಎಂದು . ಜನರು ಒಂದು ರಜಾ ಉಡುಗೊರೆ ಅನುಭವಿಸುವಿರಿ . ಅಗತ್ಯವಾಗಿ ಕರ್ನಾಟಕ ತಂಪಾದ ಮತ್ತು ಶಾಂತಿಯುತ ಅರ್ಥವಲ್ಲ . ರಾಜ್ಯದ ವರ್ಣ ಸಾಕ್ಷಿಯಾಗಿವೆ ಮತ್ತು ಸಮಾಜದ ಒಂದು ಭಾಗ ಈಗ ತದನಂತರ ಜರೆಯುತ್ತಾನೆ ಮಾಡಲಾಗಿದೆ . ಕಾರಣ: ಕನ್ನಡ ಮತ್ತು ತಮಿಳು , ತೆಲುಗು ಮತ್ತು ಹಿಂದಿ ಇತರ ಭಾಷೆಗಳ ಪ್ರಾಬಲ್ಯ ಬಳಸಿಕೊಂಡು ಜನರ ಸಂಖ್ಯೆಯನ್ನು ಅಭಾವವಿರುವ .

ಸರ್ಕಾರ ಸಾಕಷ್ಟು ಇರಿಸಿಕೊಳ್ಳಲು . ಇದು ಸಹ ಒಂದು ಸಮಿತಿ ಕನ್ನಡ Kavalu ಸಮಿತಿ ( ಕನ್ನಡ ವಾಚ್ ಡಾಗ್ ) ಎಂಬ ರೂಪುಗೊಂಡ 1993 ರಲ್ಲಿ ಕನ್ನಡ ಜಾಗೃತಿ ವರ್ಷ ವೀಕ್ಷಿಸಲು ಕರೆ ನೀಡಿದರು .

ನಾಯಿ ವೀಕ್ಷಿಸುತ್ತಿದ್ದಾರೆ? ಯಾವುದೇ ಭಾಷೆ ನಿಜವಾದ ಪ್ರೇಮಿಗಳು ವಿಷಾದಿಸುತ್ತಾನೆ. ನಾವು ಯಾವುದೇ ನಮಗೆ ವೀಕ್ಷಿಸಲು ಬಯಸುವುದಿಲ್ಲ , ನಾವು ನಮ್ಮ ಸ್ವಂತ ರೀತಿಯಲ್ಲಿ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ ... ಉಳಿದ ಹೇಳುತ್ತಾರೆ .

ರಾಜ್ಯ ಸರ್ಕಾರವು ರಾಜ್ಯೋತ್ಸವ ಪ್ರಶಸ್ತಿ ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಕೊಡುಗೆ ಜನರಿಗೆ ನೀಡಲಾಗುತ್ತದೆ ಇದು ಪ್ರತಿ ವರ್ಷ , ಪ್ರಕಟಿಸಿತು .
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split() #strip removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns.

words_to_guess = ["ahead","could"]

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    print ("Provided word is '{}' with distance of '{}'.".format(word,distance))
    
    word_location = []
    #check if the given word is in the sample_text
    if (word in sample):
    #Run through the list of splits, searching for word and give the count/location of the preceding word
        for i,word_data in enumerate(data_list):
            if word_data == word:
                #word_location = i; #will provide data one below another
                word_location.append(i)  #this will return an array
        print ("The given word exists in the sample text, lets proceed!!!")
    else:
        print ("The given word does not exist in the sample text!!!")
        
    #print word_location
    
    from collections import Counter
    next_words = []
    for next_index in range(len(word_location)):
        next_word_data = data_list[word_location[next_index] + distance]
        next_words.append(next_word_data)
        next_index-=1
    # count the number of time a word has been repeated
    next_counts = Counter(next_words)
    #print "Next word {}".format(next_counts)
    
    #conver into dataframe simply for easy access
    import pandas as pd 
    import numpy as np
    my_dic = pd.DataFrame(next_counts, index=[0]).T
    print my_dic
    
    #print my_dic[column_number][row_number] -> 0 and 0 pprovides 1st element
    #print my_dic[0][0]

    #probability of each word calculation, prob = number of times of that word/total    
    #for next_index in range(len(word_location)):
    #prob = (my_dic[0][0])/total_number_of_words  #single column, so 0
    #print "Repetation count is {}".format(my_dic[0][0])
    #print "Total number of words is {}".format(total_number_of_words)
    #print "Probability is {}".format(prob)
    
    total = my_dic.sum(axis=0)
    sum_column = total[0]
    print "sum is {}".format(sum_column)
    
    total_number_of_words = len(my_dic)   
    total_prob = 0
    Probability_of_each_word = []    
    for prob_next_index in range(total_number_of_words):
        prob = (my_dic[0][prob_next_index])/sum_column
        Probability_of_each_word.append(prob)    
        total_prob = total_prob + prob
        prob_next_index-=1  
    print "Probability of each word is {}" .format(Probability_of_each_word)
    print "Total probability should be 1.0 and it is {}".format(total_prob)
    
    
    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.
    
    best_prob = max(Probability_of_each_word)
    best_prob_location = Probability_of_each_word.index(best_prob)
    best_probable_word = (my_dic.index[best_prob_location])
    #type(best_probable_word)
    print "'{}' has best probability of {}".format(best_probable_word,best_prob)
    best_probable_word = str(best_probable_word)
    return (best_probable_word)
    
#print LaterWords(sample_memo,"gonna",1)
#print LaterWords(sample_memo,"ahead",1)
#print LaterWords(sample_memo,"ahead",2)
#print LaterWords(sample_memo,"could",1)
#print LaterWords(sample_memo,"could",2)
#print LaterWords(sample_memo,"be",1)

print LaterWords(sample_memo,"ಕನ್ನಡ",1)
print LaterWords(sample_memo,"ಜನರು",1)
print LaterWords(sample_memo,"ಕಾವೇರಿ",1)
#Yeah, I'm gonna need you to go ahead and come complain about this. 
#Oh, and if you could be/just go and sit at the kids' table, that'd be great 
