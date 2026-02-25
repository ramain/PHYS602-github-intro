# Contributing — Basic Exercise

Follow these steps to add your name to the participants list and open a pull request.
This covers the core git workflow you will use constantly as a researcher.

---

## Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-ORG/PHYS602-github-intro.git
cd PHYS602-github-intro
```

---

## Step 2: Create a new branch

Always make changes on a branch, not directly on `main`.
Name your branch `add/firstname-lastname` (use your real name, all lowercase, hyphen-separated).

```bash
git checkout -b add/robert-main
```

Verify you are on your new branch:

```bash
git branch
# * add/robert-main
#   main
```

---

## Step 3: Add your name

Open the participants file that matches your last name:

| File | Last names |
|------|-----------|
| `participants_a-f.md` | A – F |
| `participants_g-l.md` | G – L |
| `participants_m-r.md` | M – R |
| `participants_s-z.md` | S – Z |

Add a row to the table at the bottom with your name and a short research description
(10 words or fewer). Use the existing rows as a template:

```markdown
| Robert Main | Mapping stellar winds in massive binary systems |
```

Save the file.

---

## Step 4: Stage and commit your change

```bash
git add participants_m-r.md        # use the file you actually edited
git status                         # confirm only your file is staged
git commit -m "Add Robert Main to participants"
```

A good commit message is short and describes *what* changed, not *how*.

---

## Step 5: Push your branch to GitHub

```bash
git push origin add/robert-main
```

If this is your first push, git may print a longer command — just copy and run it.

---

## Step 6: Open a pull request

1. Go to the repository on GitHub.
2. You should see a banner: **"Compare & pull request"** — click it.
   (If not, click **Pull requests → New pull request** and select your branch.)
3. Set the base branch to `main`.
4. Give your PR a clear title, e.g. `Add Robert Main to participants`.
5. Click **Create pull request**.

That's it! A maintainer will review and merge your PR.

---

## Troubleshooting

**My push was rejected:**
Someone else merged a change to `main` while you were working.
Pull the latest changes and rebase your branch on top:

```bash
git fetch origin
git rebase origin/main
git push origin add/robert-main
```

**I got a merge conflict:**
Open the file with conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`),
decide which lines to keep (or keep both), remove the markers, then:

```bash
git add participants_m-r.md
git commit
```
