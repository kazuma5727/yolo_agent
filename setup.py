from setuptools import find_packages, setup

import yolo_agent

# mypackage.__version__ を取得する
version = yolo_agent.__version__

requirements = []
with open("requirements.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        requirements.append(line)

setup(
    name="yolo_agent",
    version=version,
    packages=find_packages(),
    install_requires=requirements,
)
