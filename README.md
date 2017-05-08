# Calculate SEM Images Stats


<p>
<center>
<sup><strong>
<h1>
Analysis of SEM Images of Steel
</h1>
</strong></sup>
</center>
</p>

<p>
<ul>

<li style="float: left; display: inline">
<a href="https://travis-ci.org/wd15/sem-image-stats" target="_blank">
<img src="https://api.travis-ci.org/wd15/sem-image-stats.svg"
alt="Travis CI">
</a>
</li>

<li style="float: left; display: inline">
<a href="https://github.com/wd15/sem-images-stats/blob/master/LICENSE.md" target="_blank">
<img src="https://img.shields.io/badge/license-mit-blue.svg"
alt="Travis CI">
</a>
</li>

</ul>
</p>
<br>

### Overview

The goal of this work is to analyze images of steel from SEM. The initial data set consists of 9 images. The first step in the work (comprising this notebook) is to categorize the microstructure in each image. A number of analysis steps are required including

 - cropping the images,
 - extracting meta-data embedded in the images,
 - thresholding the images to increase contrast,
 - classifying the pixels in the image as a given phase,
 - classifying the inter lammelar spacing in one of the phases,
 - obtaining statistics about the microstructure such as the volume fraction, spacing and shape.

### Git LFS

The image files are stored in Git using Git Large File Storage. This is an exploratory attempt at using Git LFS. Future work with very large volumes of data will require a public server with Git LFS deployed as the current work uses GitHub as the Git LFS server, which only allows 2GB of data storage for each user.

### Toolz

This analysis uses [Toolz](http://toolz.readthedocs.io/en/latest/) to explore the use of functional programming for data pipelines in Python. It seems to make the code a lot cleaner with less intermediate variables, which seems to be an advantage especially when evaluating cells in the notebook. Overall, it is currently unclear how much of benefit this approach provides. It does seem to obfuscate some of the code for non-functional programmers. Hopefully, it will help with parallel processing of the data pipelines using Dask in the future.

### Reproducible

The notebook is tested on Travis CI so the computational environment can be built by following the steps in `.travis.yml`.

### Notebook

The main notebook is [index.ipynb](./index.ipynb).