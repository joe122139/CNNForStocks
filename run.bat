set win=%2
set n_dim=%3
set ticker=%1
python run_binary_preprocessing.py %ticker% %win% %n_dim%
python generatedata.py dataset %win%_%n_dim%/%ticker% dataset_%ticker%_%win%_%n_dim%
python myDeepCNN.py -i dataset/dataset_%ticker%_%win%_%n_dim% -e 100 -d %n_dim% -b 8 -o outputresult_%ticker%.txt
