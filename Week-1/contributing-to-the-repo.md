# Contributing to this repository

The benefit of GitHub is that we can use it to collaborate on code together, so we will want to contribute to the parent, or upstream, repository. 

[![Introduction to GitHub](https://img.youtube.com/vi/0lEtVpdYbQ4/0.jpg)](hhttps://youtu.be/0lEtVpdYbQ4 "Introduction to GitHub")

If you click on the image above, you can review a video walkthrough of the process described below. 

## Step 1 — Making a fork

As we are not all listed as collaborators on the repository yet, we will need to fork the project. We can do this by navigating to the repository we want to fork — [https://github.com/ltagliaferri/dh-rutgers](https://github.com/ltagliaferri/dh-rutgers) — and clicking the **Fork** button on the top right corner of the page.

Forking a repository means we are making a copy of the upstream parent repository that we can then work off of to either contribte to the main project or to create our own project based on the main one. This ensures that we don't make any changes to the main project, so that all the changes we make are safely contained. While this may not be a big issue when we are working only with text files, this can become very complex when working with code. 

Once GitHub is done forking the repository for us, we should have a copy of the repository and be at the URL of https://github.com/**YourUsername**/dh-rutgers.

## Step 2 — Opening the forked repository in GitHub Desktop

Next, you'll want to open your forked repository in your GitHub Desktop application. You can do this by clicking on the green **Code** button at the top of your forked repository and selecting _Open with GitHub Desktop_ in the dropdown menu.

Once you click, GitHub Desktop should open with your forked repository loaded in. At this point, no changes should be made, but you are ready to make them!

## Step 3 — Make a change in the repo

In order to make a change to the repository, you'll open VS Code to first create a file. Open VS Code and then go to the **File** menu and then click on **Open...** in order to open the local version of the repository. When we use the term "local" we mean that it is on the computer we are currently working on. This is different from the GitHub copy, which lives on GitHub servers.

You will need to select the path for the repository. It is likely under your username, then **Documents** then **GitHub** then **dh-rutgers**. 

Once you select **dh-rutgers** you should have the filesystem visible on the left-hand side of VS Code.

Now you can highlight the **Blog** directory (by clicking on it) and then you can click on the icon for adding a new file, which looks like a piece of paper (or file) and a plus sign. You can alternately highlight the Blog directory and select the **File** menu and then clicking on **New File** in the dropdown.

You should next create a name for your new file. It can be anything you would like that is unique to the other filenames in the folder. It is recommended that you don't use spaces in the filename as it will make it more challenging to work with these files when you are programming. You can use camelCase, hyphens, or underscores. Additionally, you will want to use a `.md` extension to your file so that the computer knows we are writing a file in Markdown. Markdown enables us to format plaintext files that will show up as formatted on GitHub. Your file may be named `your-name.md`, for example. 

Now, you will want to add some text to the file. you can do something like the following just to try it out:

```
# My blog post

Here is my blog post about the public humanities...
```

The first line uses a hashtag (`#`) symbol to tell GitHub to render this as a title.

At this point, save the file and move back to GitHub Desktop.

## Step 4 — Commit and push the change

Within GitHub Desktop, you should notice that there is a change. It should be that `your-name.md` was added to the local copy of the forked repository and that there were some contents added to the file.

You are now ready to write a commit message. You can do this on the lower lefthand corner of the window. You can type "Add your-name.md" in the text input field that says `Summary (required)`. Once you do that, you can click the button **Commit to main**. This means you will be committing your change to the Git staging area, before you push it to the copy of your code on GitHub. 