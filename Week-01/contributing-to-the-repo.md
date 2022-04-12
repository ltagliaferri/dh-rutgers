# Contributing to this repository

The benefit of GitHub is that we can use it to collaborate on code together, so we will want to contribute to the parent, or upstream, repository. 

[![Introduction to GitHub](https://img.youtube.com/vi/0lEtVpdYbQ4/0.jpg)](https://youtu.be/0lEtVpdYbQ4 "Introduction to GitHub")

If you click on the image above, you can review a video walkthrough of the process described below. 

## Step 1 — Making a fork

As we are not all listed as collaborators on the repository yet, we will need to fork the project. We can do this by navigating to the repository we want to fork — [https://github.com/ltagliaferri/dh-rutgers](https://github.com/ltagliaferri/dh-rutgers) — and clicking the **Fork** button on the top right corner of the page.

Forking a repository means we are making a copy of the upstream parent repository that we can then work off of to either contribte to the main project or to create our own project based on the main one. This ensures that we don't make any changes to the main project and that all of our changes are safely contained. While this may not be a big issue when we are working only with text files, this can become very complex when working with code. 

Once GitHub is done forking the repository for us, we should have a copy of the repository and be at the URL of https://github.com/**YourUsername**/dh-rutgers.

## Step 2 — Opening the forked repository in GitHub Desktop

Next, you'll want to open your forked repository in your GitHub Desktop application. You can do this by clicking on the green **Code** button at the top of your forked repository and selecting _Open with GitHub Desktop_ in the dropdown menu.

Once you click on this, GitHub Desktop should open with your forked repository loaded in. You will also have a copy of the repository on your computer. At this point, no changes should be displayed in GitHub Desktop, but you are now ready to make them!

## Step 3 — Make a change in the repo

In order to make a change to the repository, you'll open VS Code to first create a file. Open VS Code and then go to the **File** menu and then click on **Open...** . When we use the term "local" we mean that it is on the computer we are currently working on. This is different from the GitHub copy, which lives on GitHub servers.

You will need to select the path for the repository. It is likely under your username, then **Documents**, then **GitHub**, then **dh-rutgers**. 

Once you select **dh-rutgers** you should have the filesystem visible on the left-hand side of VS Code.

Now you can highlight the **Blog** directory (by clicking on it) and then you can click on the icon for adding a new file, which looks like a piece of paper (or file) and a plus sign. You can alternately highlight the **Blog** directory and select the **File** menu and then click on **New File** in the dropdown.

You should next create a name for your new file. It can be anything you would like that is unique to the other filenames in the folder. It is recommended that you don't use spaces in the filename as it will make it more challenging to work with these files when you are programming. You can use camelCase, hyphens, or underscores. Additionally, you will want to use a `.md` extension to your file so that the computer knows we are writing a file in Markdown. Markdown enables us to format plaintext files that will show up as formatted on GitHub. Your file may be named `your-name.md`, for example. 

Now, you will want to add some text to the file. You can do something like the following just to try it out:

```
# My blog post

Here is my blog post about the public humanities...
```

The first line uses a hashtag (`#`) symbol to tell GitHub to render this as a title.

At this point, save the file and move back to GitHub Desktop.

## Step 4 — Commit and push the change

Within GitHub Desktop, you should notice that there is a change: `your-name.md` was added to the local copy of the forked repository and there were some contents added to the file.

You are now ready to write a commit message. You can do this on the lower lefthand corner of the window. You can type "Add your-name.md" in the text input field that says `Summary (required)`. Once you do that, you can click the button **Commit to main**. This means you will be committing your change to the Git staging area, before you push it to the copy of your code on GitHub. 

Once you commit the code, you should see that there is now the option to push your code to GitHub. There will be a **Push origin** button with an up arrow at the top of the GitHub Desktop window, as well as a blue banner that also has a **Push origin** button. You can click either of these buttons as they do the same thing. Once you click **Push origin** the commit will live on GitHub within your forked repository. 

## Step 5 — Open a pull request

A pull request is a way to ask the maintainer of the upstream / parent project to _pull_ our contribution into the larger project. 

Once your change was made to the GitHub version of your forked repository, and is available at the https://github.com/**YourUsername**/dh-rutgers URL, you should have a banner on the main page of the repo that says you are one commit ahead of the upstream project (that is the one at https://github.com/ltagliaferri/dh-rutgers) and that you can now **Contribute** to the project. Click on **Contribute**, then click on **Open pull request**. Now, you will be able to inspect the changes you have made. You can optionally modify your commit message that you wrote in GitHub Desktop and can also add a description. 

Once you are satisfied with your changes, you can click the green button that reads **Create pull request**. This is the final step of the pull request, and now that pull request will be visible on the upsteam main project.

At this point, the maintainer will be able to pull in the pull request or else make another comment on that request. 