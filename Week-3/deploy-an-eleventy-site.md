# Deploy an Eleventy Site

[![Deploy an Eleventy Site](https://img.youtube.com/vi/d7HDAbkJR7Y/0.jpg)](https://www.youtube.com/watch?v=d7HDAbkJR7Y "Deploy an Eleventy Site")

If you click on the image above, you can review a video walkthrough of the process. 

Run the following command to generate keys:

```
ssh-keygen -t rsa -b 4096 -C "$(git config user.email)" -f gh-pages -N ""
```

Ensure that you copy and paste the above command exactly and run it in the Terminal within the repository we're using. 