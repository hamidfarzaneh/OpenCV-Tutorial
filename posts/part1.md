---
layout: default
title: Another page
description: This is just another page
---

### Abstract
In this part , we are going to talk about how to read an image from a file, options for reading the image 
in case of its type , and the ways of how can we show it on the screen.

### Including the necessary dependencies
First of all ,we have to include the packages needed to get the opencv good to go. 
The first one is actually the `opencv` itself which is the `cv2` demonstrated in the code, then the `numpy` that is used to handle numpy array (we will discuss about it later).
{% highlight python %}
import cv2
import numpy
{% endhighlight %}

### Load our image
Now we have to open our desired image, we use the following image.
<figure>
  <img src="/assets/images/picture.png" alt="OpenCV" class="center">
</figure>

{% highlight python %}
img = cv2.imread('picture.png' , cv2.IMREAD_GRAYSCALE)
{% endhighlight %}

we can load our image using `imread` function. it loads the image specified by the first argument ( in our case , `picture.png`). The second argument specifies the format in what we want the image. This may be :
* IMREAD_UNCHANGED : loads the image as is (including the alpha channel if present) , this is a integer value which is -1 in python and a negative number in C++

* IMREAD_GRAYSCALE : loads the image as an intensity one. this is like converting the image to a gray version of it. integer value of this argument is 0

* IMREAD_COLOR : loads the image in the BGR format (blue , green , red). Integer value of this argument is 1 in python, and a positive number in C++.

For testing purposes , we create three images in all of the discussed formats and try to show all of them in seperated windows.

{% highlight python %}
unchanged_image = cv2.imread('picture.png' , -1)    # it's like using cv2.IMREAD_UNCHANGED
gray_image =      cv2.imread('picture.png' , 0 )    # it's like using cv2.IMREAD_GRAYSCALE
bgr_image =       cv2.imread('picture.png' , 1 )    # it's like using cv2.IMREAD_COLOR
{% endhighlight %}

### Show The Images

Now that we have stored the images, we try to show them on the screen. We can either use the `cv2` library itself or `matplotlib`.
{%highlight python %}
cv2.imshow('unchanged' , unchanged_image)
cv2.imshow('gray' , gray_image)
cv2.imshow('bgr' , bgr_image)
{% endhighlight %}

But if you run this code, you see that nothing appears on the screen, actually the window will open and then closes before you see it. we should make it to wait until a specific action (in our case , pressing a button) happens.

{%highlight python %}
cv2.waitKey(0)
cv2.destroyAllWindows()
{% endhighlight %}

the `waitKey` function will wait until a key is pressed and the `destoryAllWindows` function will closes all windows that are opened by cv2.

<figure>
  <img src="/assets/images/output1.png" alt="OpenCV" class="center">
</figure>

[back](./)
