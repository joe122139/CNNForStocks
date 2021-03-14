setlocal EnableDelayedExpansion
@echo off
set win=%1
set n_dim=%2
for /f %%i in (symbols.txt) do (
    set ticker=%%i
    python run_binary_preprocessing.py !ticker! %win% %n_dim%
    python generatedata.py dataset %win%_%n_dim%/!ticker! dataset_!ticker!_%win%_%n_dim%
)
echo python myDeepCNN.py -i dataset/dataset_%%s_%win%_%n_dim% -e 50 -d %n_dim% -b 8 -o outputresult.txt -t list -l symbols.txt
python myDeepCNN.py -i dataset/dataset_%%s_%win%_%n_dim% -e 50 -d %n_dim% -b 8 -o outputresult.txt -t list -l symbols.txt
