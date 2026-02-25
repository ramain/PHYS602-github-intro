# PHYS602 — Introduction to GitHub

Welcome! This repository is a hands-on introduction to git and GitHub for PHYS602 students.

---

## Everyone: Basic Exercise

Add your name to the participants list and open a pull request.
Full instructions are in [CONTRIBUTING.md](CONTRIBUTING.md).

Find the right file for your last name:

| File | Last names |
|------|-----------|
| [participants_a-f.md](participants_a-f.md) | A – F |
| [participants_g-l.md](participants_g-l.md) | G – L |
| [participants_m-r.md](participants_m-r.md) | M – R |
| [participants_s-z.md](participants_s-z.md) | S – Z |

> **Tip:** If two students with last names in the same range submit pull requests at the same time,
> you may encounter a merge conflict. That's intentional — resolving it is part of the exercise!

---

## Advanced Exercises

Already comfortable with the basics? Try one of the exercises on the branches below.
Check out the branch, read `EXERCISE.md`, and follow the instructions.

```bash
git fetch origin
git checkout exercise/merge-conflict-1   # replace with the branch you want
cat EXERCISE.md
```

Three independent versions of each exercise are available so multiple students
can work simultaneously without stepping on each other.

| Branch | Topic | Key commands |
|--------|-------|-------------|
| `exercise/merge-conflict-1` … `-3` | Resolve a merge conflict | `git merge`, `git add`, `git commit` |
| `exercise/messy-commits-1` … `-3` | Clean up a messy commit history | `git log --oneline`, `git rebase -i` |
| `exercise/add-gitignore-1` … `-3` | Untrack accidentally committed files | `git rm --cached`, `.gitignore` |
| `exercise/broken-history-1` … `-3` | Recover "lost" commits | `git reflog`, `git reset` |
