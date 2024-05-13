import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.1"     

REPONAME = "MLops-classification"
USER_NAME = "visanthoxd"
SRC_REPO = "classifier"
AUTHOR_EMAIL = "visanthoxd@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for MLops classifier app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/visanth-oxd/MLops-classification",
    project_urls={
        "Bug Tracker": f"https://github.com/visanth-oxd/MLops-classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)    
