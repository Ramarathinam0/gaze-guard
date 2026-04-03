from setuptools import setup, find_packages  # type: ignore

setup(
    name="gaze-guard",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python"
    ],
    author="Your Name",
    description="AI attention detection library using camera"
)