# gittricks

Git(Hub) tips and tricks playground.

## Tasks

### Exercise 1: Rebasing, amend and force-push

#### 1.1 set up

- clone the repo
- make a new branch
- add a new file with some random content
- commit and push
- make a pull request

#### 1.2 amemd

- oh, you forgot to something or want to edit the commit message:
- (make another small edit to your file)
- use `git amend` to attach to the last commit.

#### 1.3 rebase and force-push

- in the meantime the main-branch has another commit: you need to rebase onto main! 
- push to your feature branch:
  - rejected! you need to force push because your commit changed.
- force-push your rebased and ammended feature branch
- Done.

### Exercise 2: Interactive rebasing

- edit `file1.py`, e.g., change the for-loop to a list comprehension.
- commit 
- push to your remote feature branch
- rebase onto `main`
- resolve the conflict following the instructions in the terminal
- force-push to your remote feature branch
- Done.

### Exercise 3: Selective adding

- on your feature branch, edit `file1.py` in two different lines, adding comments or random stuff.
- use `git -p add` to add the two edits in the file as two different commits.

### Exercise 4: Cherry-picking

- on your feature branch copy the commit hash, use `git log` to see the history.
- switch to `main`
- cherry-pick your feature branch commit onto to `main`

