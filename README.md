# Gondi Wordnet

[![Website](https://img.shields.io/badge/Website-Live-brightgreen)](https://gondi-wordnet.onrender.com/)
[![Language](https://img.shields.io/badge/Language-Gondi-blue)](https://en.wikipedia.org/wiki/Gondi_language)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-orange)](https://flask.palletsprojects.com/)

A comprehensive digital lexical database and web platform for the Gondi language. This project aims to preserve, promote, and provide a research-oriented resource for Gondi, a South-Central Dravidian language.

## ✨ Creator

This repository and the accompanying web application were conceptualized, designed, and developed by **Rutwik Muley**.

* **GitHub:** `Rutwik-M` https://github.com/Rutwik-M
* **LinkedIn:** `Rutwik Muley` https://www.linkedin.com/in/rutwik-muley-b20707208
* **Portfolio:** `Rutwik Muley` [rutwik-m.is-a.dev](https://rutwik-m.is-a.dev)

---

### **Live Application: [gondi-wordnet.onrender.com](https://gondi-wordnet.onrender.com/)**

<img width="3072" height="2286" alt="screencapture-gondi-wordnet-onrender-2025-08-05-08_35_26" src="https://github.com/user-attachments/assets/96009b40-d8a0-4974-9072-240933525f54" />


---

## 📖 About The Project

A WordNet is a large lexical database where words are grouped into sets of synonyms called *synsets*, each expressing a distinct concept. This project applies that powerful lexicographical structure to the Gondi language.

The Gondi Wordnet serves two main purposes:
1.  **Language Preservation**: To create a lasting, accessible digital archive of the Gondi lexicon.
2.  **Community & Research**: To provide a collaborative tool for linguists, community members, and language learners to explore, contribute to, and analyze the Gondi language.

---

## 🚀 Features

The platform includes a robust set of features for both public users and registered contributors:

* **Comprehensive Search**: An intuitive interface to search for Gondi words and view their meanings, parts of speech, and relations.
* **Multi-Level User System**: Supports different user roles, including administrators and reviewers/contributors with distinct permissions.
* **Contribution Workflow**: Registered users can add new words and propose edits to existing ones.
* **Review & Approval System**: A dedicated interface for administrators or reviewers to approve or reject new submissions and edits, ensuring data quality and accuracy.
* **Transliteration**: Built-in logic to handle different scripts or transliteration schemes.
* **Wordnet Visualization**: A graphical representation of the lexical relationships between words.

---

## 🛠️ Tech Stack

* **Backend**: Python with the **Flask** web framework.
* **Frontend**: HTML, CSS, JavaScript.
* **Database**: PostgreSQL (or similar) for storing user data, words, and review entries.
* **Deployment**: Hosted on **Render**.

---

## 📂 Directory Structure

The repository is organized as follows:

```
└── rutwik-m-gondi-wordnet/
    ├── app.py                  # Main Flask application file (routes, logic)
    ├── config.example.py       # Example configuration file for environment variables
    ├── gondi_proper.json       # Gondi Alphabets JSON for Transliteration Model
    ├── Procfile                # Defines commands for the web server (for deployment)
    ├── requirements.txt        # Python dependencies for pip
    ├── runtime.txt             # Specifies Python runtime for deployment
    ├── transliteration.py      # Module for transliteration logic
    └── templates/              # Directory for all user-facing HTML templates
        ├── add_word.html
        ├── admin.html
        ├── create_user.html
        ├── edit_word.html
        ├── edit_word_review.html
        ├── index.html
        ├── login.html
        ├── login_review.html
        ├── review.html
        ├── review_entries.html
        └── wordnet_visualization.html
```

---

## ⚙️ Getting Started: Local Setup

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/rutwik-m-gondi/rutwik-m-gondi-wordnet.git](https://github.com/rutwik-m-gondi/rutwik-m-gondi-wordnet.git)
    cd rutwik-m-gondi-wordnet
    ```

2.  **Create and activate a virtual environment:**
    * On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure the application:**
    * Create a copy of the example configuration file and name it `config.py`:
        ```sh
        cp config.example.py config.py
        ```
    * Open `config.py` and set the required environment variables, such as a `SECRET_KEY`, your database connection details, and admin credentials.

5.  **Run the application:**
    ```sh
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

## 🤝 Contributing

Contributions are welcome and greatly appreciated. Please fork the repository and open a pull request with your enhancements.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📜 License

This project is distributed under the MIT License. See the `LICENSE` file for more information. (Note: You should add a `LICENSE` file with the MIT License text to your repository).
