from setuptools import setup, find_packages

with open("./LinkedinScraping/readme.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="linkedin_scraping",
    version="0.0.1",
    author="edA",
    author_email="edandradef@gmail.com",
    description="coleta dados de vagas para analise e faz conexeos",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
)