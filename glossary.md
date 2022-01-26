# Glossary

We will keep a running glossary of technical terms throughout the semester.

## General computation

### Deploy

Deployment is when code is made available to the intended end users of that code. This includes the initial release of software applications themselves, new features, bug fixes, or security patches. Generally, software is moved from internal servers to public-facing servers during deployment, so that users can have access to that software. In the example of a personal website, you may build it locally on your own computer, and then deploy it to a cloud server when you are ready for users to have access to it. 

---

### Local

The computer we are currently working on. A _local_ copy of a repository is one that exists in our computer's filesystems. 

---

### Markdown

Markdown is a markup language that we can use to create formatted text using a plain-text editor like VS Code. Markdown will be rendered as formatted text on GitHub and static websites.

---

## Git

Git is version control software that is free and open source, and serves as the basis for Git code host platforms like GitHub. It allows for tracking changes across files and is often use for collaboration across software development projects.

---

### Branch

A branch in Git allows you to build off of the main project in a discrete and separate space that will leave the main project untouched until the branch is merged in. Generally, a project's core branch is called the "main" branch, and you can create new branches based on this branch so that the main branch remains clean until you are ready to incorporate those changes (note that you can also build off of other branches if needed). A common recommended practice is to consider anything on the main branch as being deployable for others to use at any time.

You may create a new branch to work on a new feature (that is, to add functionality to a project, like a dark mode version of a webapp), or to fix a bug in the software (something not behaving as expected, or something broken). If you are working within multiple branches at once (say you are building a new feature and also reviewing a colleague's work), you can checkout each branch as needed and all of the changes to the codebase will remain discrete on each branch as though the are separate snapshots.

---

### Clone

A clone of a Git repository is a copy of the repository that remains linked to the original (upstream) repository. If you are working on a team with others, you are more likely to clone the main project. If you are not on a team with others but would like to contribute to the main project, you will more likely fork the repository.

---

### Commit

Committing within the context of a Git repository means that you are recording changes. Depending on what branch you are on and what project you are in, you may be committing directly to the main project. 

---

### Fetch

When you fetch from a remote repository, you are downloading the updates to your local copy. 

---

### Fork

A fork of a Git repository is a copy of the repository that is a completely new copy of that repository. A fork of a repository on GitHub will live under your username and the project name. If you would like to contribute to the main project, you will need to open a request for the maintainers to merge it in. You may also use a fork of a repository in order to create a new project that is based on an already existant one (the one that you forked). 

---

### Pull request

A request that a project accept changes you have made to its code repository; that is, to _pull_ in the changes you have contributed to the code base so that it is available for others.

---

### Push

When you push in Git, you are moving commits you have made to the software to the remote repository. Generally, you are pushing from your local machine to the remote repo. If you are working in a repository you maintain , you may be directly impacting the code in the remote repo. 

---

### Upstream

An upstream repository is a project you have forked from. This is different from an origin repository, which would be your remote fork. 