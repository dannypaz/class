Having trouble remembering to type `source activate dsci6007` before working on a lab?
Try this:

0. make sure you are not in `DSCI6007-student` or any other git repo
1. `git clone https://github.com/chdoig/conda-auto-env`
2. follow the instructions in the README.md
(namely, sourcing conda_auto_env.sh  to `.bash_profile`).
3. cd into `DSCI6007-student`
4. run `source activate dsci6007` (for perhaps the last time)
5. run `conda env export > environment.yml`
6. close your terminal window and open a new one
7. cd into `DSCI6007-student` again and this time
it should automatically activate your conda environment
