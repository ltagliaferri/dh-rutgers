# How to Add Images and Links in Eleventy Markdown

This guide will walk you through adding images and hyperlinks into your Eleventy static site, based off of the [eleventy-academic-template](https://github.com/ltagliaferri/eleventy-academic-template).

## Adding an image

The format for adding an image in markdown is as follows:

```
![descriptive (alt) text](path or link to image)
```

So, if I had an image of a laptop — `laptop.jpg` — in the `/docs/assets/images/`, the format of this in markdown would be written like this:

```
![Laptop photo](/docs/assets/images/)
```

And on the page it would look like this: 

![Laptop photo](https://raw.githubusercontent.com/ltagliaferri/dh-rutgers-2022/main/src/img/laptop.jpg)

The `Laptop photo` text is alternative (or "alt") text, which renders when the image cannot render or otherwise be fetched. This is also useful text for accessibility as those who cannot see the image will be able to access the text through a screen reader, etc.

Since we are working on the web, images do not need to be in very high quality (as they need to be in print), so you can compress your images prior to adding them to the site, to save bandwidth and enable your site to be speedier and more accesible to those with less access to high-speed internet. One way to get your images compressed is to use [https://tinypng.com](https://tinypng.com), on this side you can drag and drop images and then download the compressed version of the same image.

_Photo by [Kari Shea](https://unsplash.com/@karishea?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/laptop?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_.

## Adding links

Adding links in markdown takes the following format:

```
[text you want to appear](URL you want to link to]
```

So, if you want to link to the New York Public Library website, your link will be written like this:

```
[New York Public Library](https://www.nypl.org/)
```

This will be rendered on the page like this:

[New York Public Library](https://www.nypl.org/)

In a blog post, you may have a longer sentence, the format will remain the same:

```
To learn more, you may visit the [New York Public Library](https://www.nypl.org).
```

> To learn more, you may visit the [New York Public Library](https://www.nypl.org).

You can set up links throughout your Eleventy site; in blog posts, your About page, your CV page, and more. 
