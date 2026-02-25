# PHYS602 — Introduction to GitHub

This repository is meant as a hands-on introduction to git and GitHub for PHYS602 students.

## Basic Exercise

Add your name to the participants list and open a pull request.
Full instructions are in [CONTRIBUTING.md](CONTRIBUTING.md).

Find the right file for your last name:

| File | Last names |
|------|-----------|
| [participants_a-f.md](participants_a-f.md) | A – F |
| [participants_g-l.md](participants_g-l.md) | G – L |
| [participants_m-r.md](participants_m-r.md) | M – R |
| [participants_s-z.md](participants_s-z.md) | S – Z |

> If two students with last names in the same range submit pull requests at the same time,
> you may encounter a merge conflict. That's intentional — resolving it is part of the exercise!

## Advanced Exercises

If you are more experienced in git/github, the above may be too easy.  There are some optional
branches below which have some common git/github problems.

```bash
git fetch origin
git checkout exercise/merge-conflict-1   # replace with the branch you want
cat EXERCISE.md
```

Three independent versions of each exercise are available so multiple students
can work simultaneously without stepping on each other.

| Branch | Topic | Key commands |
|--------|-------|-------------|
| `merge-conflict-1` … `-3` | Resolve a merge conflict | `git merge`, `git add`, `git commit` |
| `messy-commits-1` … `-3` | Clean up a messy commit history | `git log --oneline`, `git rebase -i` |
| `add-gitignore-1` … `-3` | Untrack accidentally committed files | `git rm --cached`, `.gitignore` |
| `broken-history-1` … `-3` | Recover "lost" commits | `git reflog`, `git reset` |

Other useful topics to learn:
- Creating / resolving an issue
- Adding a large file using github LFS
- Continuous Integration