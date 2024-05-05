
<h1 align="center">EASY LOCAL RAG</h1>

<p align="center">
	<img src="https://img.shields.io/github/license/skyonya/easy_local_rag?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/skyonya/easy_local_rag?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/skyonya/easy_local_rag?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/skyonya/easy_local_rag?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/LangChain-blue?style=flat">
   <img alt="Static Badge" src="https://img.shields.io/badge/ChromaDB-blue?style=flat">
<img alt="Static Badge" src="https://img.shields.io/badge/SentenceTransformers-blue?style=flat">



</p>
<hr>

##  Quick Links

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

> - [ Overview](#overview)
> - [ Features](#features)
> - [ Repository Structure](#repository-structure)
> - [ Modules](#modules)
> - [ Getting Started](#getting-started)
>   - [ Installation](#installation)
>   - [ Running ](#running)
> - [ Project Roadmap](#project-roadmap)
> - [ Contributing](#contributing)
> - [ License](#license)
</details>

---


##  Overview

easy_local_rag is a Python project designed to create a local question-answer system with RAG (Retrieval Augmented Generation) and LLM (Large Language Model)

document vectorization, similarity search, and model-based answer generation

---

##  Features

- **Document Processing**: Includes functions for loading and splitting documents into smaller chunks for efficient processing.


- **Vector Store Management**: Facilitates the creation, loading, and access of a vector store using Chroma library and SentenceTransformer embeddings.


- **Answer Generation with RAG (Retrieval Augmented Generation)**: Utilizes an external API (Ollama) to generate bot recommendations based on user input and relevant documents.


- **Interactive Question-Answer Loop**: Allows users to input questions, performs similarity search against the document vector store, generates answers using the model, and provides responses to user queries.

---

##  Repository Structure

```sh
└── /
    ├── LICENSE
    ├── README.md
    ├── model_answer.py
    ├── requirements.txt
    ├── split_docs_tools.py
    ├── start_model.py
    ├── tools.py
    └── vectorstore_tools.py
```

---


##  Modules

<details closed><summary>Modules</summary>

| File                                         | Summary                                                                                                                                                                                                                                            |
| ---                                          |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [tools.py](tools.py)                         | The module provides a set of utility functions for common tasks related to file system operations and performance measurement.                                                                                                                     |
| [model_answer.py](model_answer.py)           | Bot generating recommendations based on user input and relevant documents using the Ollama API. It constructs prompts based on the input parameters, sends requests to the API endpoint for text generation, and returns the generated bot answer. |
| [vectorstore_tools.py](vectorstore_tools.py) | The module contains functions for creating, loading, and accessing a vector store using the Chroma library and SentenceTransformer embeddings. It provides utility functions to manage document embeddings and vector store persistence.           |
| [start_model.py](start_model.py)             | The module serves as an entry point for initiating a question-answer system utilizing a document vector store and a model for generating answers. It provides settings for specifying document paths, model names, and embedding models, and it orchestrates the interaction between the vector store and the answer generation model.                                                                                                                                                                                                                                                   |
| [split_docs_tools.py](split_docs_tools.py)   | The module provides functions for loading and splitting documents into smaller chunks. It utilizes text loaders and splitters from the LangChain community library to handle document processing efficiently.                                                                                                                                                                                                                                                   |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.10.6 or newer`

###  Installation

1. Clone the  repository:

```sh
git clone https://github.com/skyonya/easy_local_rag/
```

2. Change to the project directory:

```sh
cd easy_local_rag
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running 

1. Run model in Ollama:

```sh
ollama run mistral
```

2. Use the following command to run :

```sh
python start_model.py
```

---

##  Project Roadmap

- [X] `► Split documents into chunks`
- [X] `► Conversion text chunks to embeddings`
- [X] `► Save and load embeddings to vector db`
- [X] `► Semantic search in vector db`
- [X] `► Generating answer with relevant document from db`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/skyonya/easy_local_rag/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/skyonya/easy_local_rag/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/skyonya/easy_local_rag/issues)**: Submit bugs found or log feature requests.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/skyonya/easy_local_rag/
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [MIT](https://github.com/Skyonya/easy_local_rag/blob/main/LICENSE) License. For more details, refer to the [MIT](https://github.com/Skyonya/easy_local_rag/blob/main/LICENSE) file.

---

[**Return**](#quick-links)

---
