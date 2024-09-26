# TEST REPO

## Overview

Welcome to the **TEST REPO**! This repository contains various tools and resources designed for testing and experimentation.

## TEST LAB

The **TEST LAB** section includes a Docker container specifically set up for conducting various attack simulations. This environment is ideal for security professionals and enthusiasts looking to explore and understand different types of attacks in a controlled setting.

### Getting Started

To get started with the TEST LAB, follow these steps:

1. **Clone the Repository:**

```bash
git clone https://github.com/pascalnehlsen/test-repo.git
cd test-repo
```

2. **Build the Docker Container**:

```bash
docker build -t test-lab .
```

3. **Run the Docker Container**:

```bash
docker run -it test-lab
```

## Fake Metadata

The **FAKE METADATA** tool allows users to read and modify PDF metadata easily. This small utility is perfect for users looking to change the metadata of their PDF files for testing or organizational purposes.

### Features

- Read PDF metadata
- Modify PDF metadata
- User-friendly interface

### Usage

1. **Clone the Repository:**

```bash
git clone https://github.com/pascalnehlsen/test-repo.git
cd test-repo
```

2. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Tool**:

```bash
python fake_metadata.py <path_to_pdf>
```
