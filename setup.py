from setuptools import setup, find_packages
import os

# Check if OpenCV is installed and raise an error if it is not
# but don't do this if the ReadTheDocs systems tries to install
# the library, as that is configured to mock cv2 anyways

long_description = """A library for image augmentation in machine learning experiments, particularly convolutional neural networks.
Supports augmentation of images and keypoints/landmarks in a variety of different ways."""

setup(
    name="imgaug",
    version="0.2.4",
    author="Alexander Jung",
    author_email="kontakt@ajung.name",
    url="https://github.com/aleju/imgaug",
    download_url="https://github.com/aleju/imgaug/archive/0.2.4.tar.gz",
    install_requires=["scipy", "scikit-image>=0.11.0", "numpy>=1.7.0", "six"],
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="Image augmentation library for machine learning",
    long_description=long_description,
    keywords=["augmentation", "image", "deep learning", "neural network", "machine learning"]
)
