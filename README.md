# Talk to Me — Chatbot Prototype

A small interactive rule-based chatbot built in Python for LING 498 – Computational Methods in Linguistics. The project explores how basic Natural Language Processing (NLP) techniques can simulate short conversations without relying on large language models.

## Features

- Detects simple intents such as greetings, thanks, and goodbyes
- Uses NLTK for tokenization and lemmatization
- Performs rule-based intent detection through keyword matching
- Generates randomized responses to reduce repetition
- Stores basic user information (name, age, favourite colour)
- Records conversation history and exports it to a text file
- Includes a free chat mode for continuous interaction
- Supports optional dialogue experiments

## Technologies Used

- Python 3
- NLTK (Natural Language Toolkit)
- Standard Python libraries (`random`)

## NLP concepts

- Tokenization
- Lemmatization
- Lexical preprocessing
- Rule-based intent detection
- Pattern matching

## What I Practiced

- Dictionaries
- Lists
- Functions
- Loops
- Conditional statements
- User input validation
- Rule-based conversational design
- Lexical preprocessing with NLTK
- Conversation logging

## Project Structure 

- TalkToMe.py
- experiments.py
- conversation_logs.txt
- README.md

## Running the Project

Install NLTK

If running for the first time, download the following resources:

- nltk.download("punkt")
- nltk.download("wordnet")
- nltk.download("omw-1.4")

## Project Status

This project is an educational prototype developed for an undergraduate Computational Linguistics course. It demonstrates how rule-based conversational agents operate using basic NLP techniques.

## Future Improvements

- Expand the intent library
- Improve the conversation log system
- Add sentiment analysis
- Integrate part-of-speech tagging or named entity recognition
