---
layout: page
permalink: /teaching/
title: teaching
description: Seven open courses, all running in your browser.
nav: true
nav_order: 2
---

Each course stands on its own and builds every idea by hand before handing it to a library. The notebooks open in Google Colab with one click, so there is nothing to install. The first two courses start from a first line of Python. The other five assume you can already program.

- [**From Python to Deep Learning and Fine-Tuning**](#deep-learning): for those heading towards machine learning and AI.
- [**From Zero to Data Structures and Algorithms in Python**](#data-structures): a practice-first route through programming fundamentals, algorithms, and data structures.
- [**From Words to Meaning: Natural Language Processing in Python**](#nlp): how machines read, search, translate and summarise text, from counting words to retrieval-augmented generation.
- [**From Questions to Answers: Classic Datasets, Fully Explored**](#classic-datasets): complete exploratory analyses of the classic datasets of data science, already run and commented, from the first question to a baseline model.
- [**From One Table to a Cluster: Working with Data at Scale**](#data-at-scale): SQL, data warehouses, NoSQL, Spark and streaming, and how to tell when you need them.
- [**From Papers to Practice: Landmark Deep Learning Architectures**](#landmark-architectures): the networks that shaped deep learning, from the perceptron to the Transformer, each explained from its original paper, built in PyTorch and trained.
- [**From Random Moves to Winning Agents: Reinforcement Learning with Games**](#reinforcement-learning): agents that learn by trial and error, from slot machines to Snake, a lunar lander and self-play, with videos of the agents you train.

Want to write your own code alongside the notebooks? <a href="https://colab.research.google.com/#create=true" target="_blank">Open a blank Colab notebook</a>.

---

## From Python to Deep Learning and Fine-Tuning
{: #deep-learning}

A complete, self-contained course that takes you from a first line of Python to fine-tuning a modern Transformer model. The notebooks run directly in the browser via Google Colab: nothing to install.

Each concept is first explained in depth, then implemented by hand, and only then handed to a library. That order is deliberate: it is what turns these systems from black boxes into things you genuinely understand.

---

### Module A: Python Foundations

| # | Notebook | |
|---|----------|---|
| 1 | Hello World and Python Fundamentals: variables, types, input/output | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/01_hello_world_basics.ipynb" target="_blank">Open in Colab</a> |
| 2 | Control Flow and Functions: decisions, loops, writing your own functions | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/02_control_flow_functions.ipynb" target="_blank">Open in Colab</a> |
| 3 | Data Structures: lists, dictionaries, sets, and comprehensions | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/03_data_structures.ipynb" target="_blank">Open in Colab</a> |
| 4 | Modular Code and OOP: modules, classes, and inheritance | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/04_modules_oop.ipynb" target="_blank">Open in Colab</a> |

### Module B: Scientific Python

| # | Notebook | |
|---|----------|---|
| 5 | NumPy: arrays, vectorisation, and the linear algebra behind ML | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/05_numpy.ipynb" target="_blank">Open in Colab</a> |
| 6 | Pandas: loading, cleaning, and exploring real data | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/06_pandas.ipynb" target="_blank">Open in Colab</a> |
| 7 | Data Visualisation: turning numbers into insight | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/07_visualization.ipynb" target="_blank">Open in Colab</a> |

### Module C: Machine Learning

| # | Notebook | |
|---|----------|---|
| 8 | ML Concepts and Workflow: core ideas, overfitting, and evaluation metrics | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/08_ml_concepts.ipynb" target="_blank">Open in Colab</a> |
| 9 | Regression: first models and gradient descent by hand | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/09_regression.ipynb" target="_blank">Open in Colab</a> |
| 10 | Classification: logistic regression, decision trees, and evaluation | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/10_classification.ipynb" target="_blank">Open in Colab</a> |
| 11 | Beyond the Basics: scaling, cross-validation, ensembles, clustering, PCA | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/11_advanced_ml.ipynb" target="_blank">Open in Colab</a> |

### Module D: Deep Learning

| # | Notebook | |
|---|----------|---|
| 12 | From ML to Neural Networks: build a network from scratch in NumPy | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/12_neural_networks_intro.ipynb" target="_blank">Open in Colab</a> |
| 13 | Backpropagation and Training: how networks learn; introduction to PyTorch | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/13_backprop_pytorch.ipynb" target="_blank">Open in Colab</a> |
| 14 | Convolutional Neural Networks: deep learning for images | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/14_cnns.ipynb" target="_blank">Open in Colab</a> |
| 15 | Sequence Models and Attention: text, time series, and the road to Transformers | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/15_sequence_models_attention.ipynb" target="_blank">Open in Colab</a> |

### Module E: Transformers and Fine-Tuning

| # | Notebook | |
|---|----------|---|
| 16 | The Transformer Architecture: self-attention explained in detail | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/16_transformers.ipynb" target="_blank">Open in Colab</a> |
| 17 | Pretrained Models and Transfer Learning: standing on the shoulders of giants | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/17_pretrained_transfer.ipynb" target="_blank">Open in Colab</a> |
| 18 | Fine-Tuning a Model: adapt a state-of-the-art model to your own data | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-hello-world-to-ai/18_fine_tuning.ipynb" target="_blank">Open in Colab</a> |

---

## From Zero to Data Structures and Algorithms in Python
{: #data-structures}

A complete, practice-first course that takes you from a first line of Python to building your own stacks, linked lists, hash tables and search trees. It assumes no programming experience. The notebooks run directly in the browser via Google Colab: nothing to install.

Each concept is first explained in plain words, then shown in small worked examples, and then practised: the 18 notebooks contain more than 140 exercises, each with a hidden solution. Every claim about speed is measured rather than asserted, with timing experiments you run yourself.

---

### Module A: Python from Zero

| # | Notebook | |
|---|----------|---|
| 1 | First Steps in Python: printing, variables, types, arithmetic, input | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/01_first_steps.ipynb" target="_blank">Open in Colab</a> |
| 2 | Making Decisions: if / elif / else, comparisons, logical operators | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/02_making_decisions.ipynb" target="_blank">Open in Colab</a> |
| 3 | Loops: for, while, range, accumulators, nested loops | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/03_loops.ipynb" target="_blank">Open in Colab</a> |
| 4 | Functions: parameters, return values, defaults, scope | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/04_functions.ipynb" target="_blank">Open in Colab</a> |
| 5 | Lists, Strings and Dictionaries: the everyday containers | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/05_lists_strings_dicts.ipynb" target="_blank">Open in Colab</a> |
| 6 | Writing Robust Programs: validating input, handling errors, solving problems step by step | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/06_robust_programs.ipynb" target="_blank">Open in Colab</a> |
| 7 | Classes and Objects: bundling data and behaviour, inheritance | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/07_classes_objects.ipynb" target="_blank">Open in Colab</a> |

### Module B: Mini Projects

| # | Notebook | |
|---|----------|---|
| 8 | Games of Chance: the random module, Guess the Number, Rock–Paper–Scissors | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/08_games_of_chance.ipynb" target="_blank">Open in Colab</a> |
| 9 | A To-Do List Application: designing a program from functions, saving to a file | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/09_todo_list.ipynb" target="_blank">Open in Colab</a> |
| 10 | An ATM as a State Machine: organising a program around its states | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/10_atm_state_machine.ipynb" target="_blank">Open in Colab</a> |

### Module C: Algorithms and Complexity

| # | Notebook | |
|---|----------|---|
| 11 | Big O Notation: measuring how code scales, with real timing experiments | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/11_big_o.ipynb" target="_blank">Open in Colab</a> |
| 12 | Recursion: functions that call themselves, the call stack, memoisation | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/12_recursion.ipynb" target="_blank">Open in Colab</a> |
| 13 | Searching: linear search and binary search | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/13_searching.ipynb" target="_blank">Open in Colab</a> |
| 14 | Sorting: bubble, selection, insertion and merge sort, compared on the clock | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/14_sorting.ipynb" target="_blank">Open in Colab</a> |

### Module D: Data Structures

| # | Notebook | |
|---|----------|---|
| 15 | Stacks and Queues: last-in-first-out and first-in-first-out | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/15_stacks_queues.ipynb" target="_blank">Open in Colab</a> |
| 16 | Linked Lists: nodes and references, built by hand | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/16_linked_lists.ipynb" target="_blank">Open in Colab</a> |
| 17 | Hash Tables: how dictionaries find things instantly | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/17_hash_tables.ipynb" target="_blank">Open in Colab</a> |
| 18 | Trees and Binary Search Trees: hierarchical data and fast ordered lookup | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-zero-to-data-structures/18_trees_bst.ipynb" target="_blank">Open in Colab</a> |

---

## From Words to Meaning: Natural Language Processing in Python
{: #nlp}

A complete course on how machines work with human language, from a single string of characters to systems that search, translate, summarise and answer questions. It assumes you can already program in Python. The notebooks run directly in the browser via Google Colab: nothing to install.

One question runs through all 18 notebooks: how do we turn text into numbers without losing what it means? Each idea is first explained in plain words, then built by hand in a few lines of Python, and only then handed to a library. Every method is measured against a simple baseline, and the result is reported even when the simple method wins.

The course does not repeat the foundations of machine learning and neural networks. Those are covered in [From Python to Deep Learning and Fine-Tuning](#deep-learning), and the notebooks here point to the exact notebook there whenever they rely on it.

---

### Module A: Text as Data

| # | Notebook | |
|---|----------|---|
| 1 | Text as Data: characters, Unicode, counting words, Zipf's law | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/01_text_as_data.ipynb" target="_blank">Open in Colab</a> |
| 2 | Regular Expressions: describing patterns in text, cleaning messy data | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/02_regular_expressions.ipynb" target="_blank">Open in Colab</a> |
| 3 | Tokenisation and Normalisation: tokens, stop words, stemming, lemmatisation | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/03_tokenisation_normalisation.ipynb" target="_blank">Open in Colab</a> |

### Module B: The Structure of Language

| # | Notebook | |
|---|----------|---|
| 4 | Formal Languages and Automata: finite automata by hand, the Chomsky hierarchy | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/04_formal_languages_automata.ipynb" target="_blank">Open in Colab</a> |
| 5 | Grammars and Parsing: context-free grammars, parse trees, ambiguity, CKY | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/05_grammars_parsing.ipynb" target="_blank">Open in Colab</a> |
| 6 | Part-of-Speech Tagging and Named Entities: a hidden Markov model and the Viterbi algorithm | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/06_pos_tagging_named_entities.ipynb" target="_blank">Open in Colab</a> |

### Module C: Counting Words

| # | Notebook | |
|---|----------|---|
| 7 | N-gram Language Models: predicting the next word, smoothing, perplexity | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/07_ngram_language_models.ipynb" target="_blank">Open in Colab</a> |
| 8 | Bag of Words, TF-IDF and Search: documents as vectors, a small search engine | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/08_bag_of_words_tfidf_search.ipynb" target="_blank">Open in Colab</a> |
| 9 | Text Classification with Naive Bayes: a classifier built from word counts | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/09_text_classification_naive_bayes.ipynb" target="_blank">Open in Colab</a> |

### Module D: Meaning as Vectors

| # | Notebook | |
|---|----------|---|
| 10 | Word Embeddings: co-occurrence, PPMI, Word2Vec by hand, analogies | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/10_word_embeddings.ipynb" target="_blank">Open in Colab</a> |
| 11 | Topic Modelling: discovering themes in an unlabelled collection | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/11_topic_modelling.ipynb" target="_blank">Open in Colab</a> |

### Module E: Neural Networks for Text

| # | Notebook | |
|---|----------|---|
| 12 | LSTMs and Text Generation: gates, memory, a character-level language model | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/12_lstms_text_generation.ipynb" target="_blank">Open in Colab</a> |
| 13 | Sequence-to-Sequence Models and Translation: encoder, decoder, the BLEU score | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/13_seq2seq_translation.ipynb" target="_blank">Open in Colab</a> |
| 14 | Convolutions over Text: phrase detectors that learn | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/14_convolutions_over_text.ipynb" target="_blank">Open in Colab</a> |

### Module F: Language Models in Practice

| # | Notebook | |
|---|----------|---|
| 15 | Subword Tokenisation and Decoding: byte-pair encoding by hand, temperature, top-p, beam search | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/15_subword_tokenisation_decoding.ipynb" target="_blank">Open in Colab</a> |
| 16 | Text from the Web: collecting text properly and responsibly | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/16_text_from_the_web.ipynb" target="_blank">Open in Colab</a> |
| 17 | Summarisation: extractive and abstractive methods, the ROUGE score | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/17_summarisation.ipynb" target="_blank">Open in Colab</a> |
| 18 | Semantic Search and Retrieval-Augmented Generation: finding by meaning, answering from sources | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-words-to-meaning/18_semantic_search_rag.ipynb" target="_blank">Open in Colab</a> |

---

## From Questions to Answers: Classic Datasets, Fully Explored
{: #classic-datasets}

A course of complete exploratory data analyses (EDA) of the classic datasets of data science. Each notebook starts from one question, loads the data straight from a public URL, and follows the same route: a first look, missing values, one variable at a time, pairs of variables and confounders, feature engineering, baseline models judged against common sense, and a written answer to the question. It assumes basic Python and a first contact with pandas.

The notebooks are saved **already run**: every table and chart is visible on opening, and each result is followed by a comment that explains what it shows, so a notebook can be read or presented without waiting for any code. Running it again in Colab takes about a minute. Every notebook ends with a *Going further* section for experienced students, with techniques used in the best public analyses of the same data: leak-free pipelines, fairness constraints, bootstrap intervals, lag features for time data and t-SNE maps.

The course does not re-teach pandas, plotting or machine learning, which are in [From Python to Deep Learning and Fine-Tuning](#deep-learning). It shows how those tools are used together to answer a question.

---

| # | Dataset and question | |
|---|----------|---|
| 1 | Titanic: who survived, and why? Missing values, two-way tables, a confounder, titles from names, baselines and overfitting | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/01_titanic.ipynb" target="_blank">Open in Colab</a> |
| 2 | Palmer Penguins: which species is this? Pair plots, Simpson's paradox, scaling, k-means against the true labels | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/02_penguins.ipynb" target="_blank">Open in Colab</a> |
| 3 | House Prices: what makes a house expensive? 80 columns, missing or "none", a log target, outliers, regression in dollars | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/03_house_prices.ipynb" target="_blank">Open in Colab</a> |
| 4 | Adult Census Income: who earns more, and is the model fair? Disguised missing values, unbalanced classes, thresholds, fairness | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/04_adult_income.ipynb" target="_blank">Open in Colab</a> |
| 5 | Heart Disease: can routine tests flag a sick heart? Codes as categories, selection bias, small data, the cost of a missed case | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/05_heart_disease.ipynb" target="_blank">Open in Colab</a> |
| 6 | Wine Quality: can chemistry predict taste? Duplicates and leakage, human scores, predictions pulled to the middle | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/06_wine_quality.ipynb" target="_blank">Open in Colab</a> |
| 7 | Bike Sharing: when do people ride? Daily and seasonal rhythms, gaps in time, honest time splits, seasonal baselines | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/07_bike_sharing.ipynb" target="_blank">Open in Colab</a> |
| 8 | Fashion-MNIST: what does a computer see in a picture? Images as tables, average images, PCA, raw-pixel baselines | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-questions-to-answers/08_fashion_mnist.ipynb" target="_blank">Open in Colab</a> |

---

## From One Table to a Cluster: Working with Data at Scale
{: #data-at-scale}

A complete course on what happens to data once there is a lot of it: SQL and indexes, data warehouses, columnar files, NoSQL, MapReduce, Spark, streaming and the cloud. It assumes you can already program in Python, and no knowledge of databases. The notebooks run directly in the browser via Google Colab: nothing to install.

One question runs through the first 12 notebooks: what changes when the data no longer fits? In one table, in the time a query has, in memory, on one machine, and finally in time itself. Each idea is first explained in plain words, then built by hand in a few lines of Python, and only then handed to a professional tool. Every claim about speed or size is measured, including the cases where the simple approach beats the heavy machinery. The six notebooks of the last module take one real data warehouse, Microsoft's AdventureWorks sample, through every idea of the course.

The course does not repeat what the others cover. Working with tables in pandas and machine learning are in [From Python to Deep Learning and Fine-Tuning](#deep-learning). Big O, binary search, hash tables and trees are in [From Zero to Data Structures and Algorithms in Python](#data-structures).

---

### Module A: Data at Rest

| # | Notebook | |
|---|----------|---|
| 1 | Tables and SQL: the relational model, keys, first queries, transactions | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/01_tables_and_sql.ipynb" target="_blank">Open in Colab</a> |
| 2 | Joins and Aggregation: combining tables, grouping, window functions | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/02_joins_and_aggregation.ipynb" target="_blank">Open in Colab</a> |
| 3 | Indexes and Query Plans: why some queries are instant and others crawl | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/03_indexes_and_query_plans.ipynb" target="_blank">Open in Colab</a> |
| 4 | Data Warehouses: facts, dimensions and the star schema | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/04_data_warehouses.ipynb" target="_blank">Open in Colab</a> |

### Module B: Beyond Tables

| # | Notebook | |
|---|----------|---|
| 5 | Files and Formats: rows against columns, CSV against Parquet | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/05_files_and_formats.ipynb" target="_blank">Open in Colab</a> |
| 6 | NoSQL: documents, key-value stores, sharding, replication and the CAP theorem | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/06_nosql.ipynb" target="_blank">Open in Colab</a> |

### Module C: Too Big for One Machine

| # | Notebook | |
|---|----------|---|
| 7 | Larger than Memory: streaming through data that does not fit | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/07_larger_than_memory.ipynb" target="_blank">Open in Colab</a> |
| 8 | MapReduce by Hand: divide, map, shuffle, reduce | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/08_mapreduce_by_hand.ipynb" target="_blank">Open in Colab</a> |
| 9 | Spark, RDDs and DataFrames: a cluster engine in your notebook | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/09_spark_rdds_dataframes.ipynb" target="_blank">Open in Colab</a> |
| 10 | Spark SQL and Pipelines: and when a cluster is the wrong tool | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/10_spark_sql_pipelines.ipynb" target="_blank">Open in Colab</a> |

### Module D: Data in Motion and in the Cloud

| # | Notebook | |
|---|----------|---|
| 11 | Streaming: windows, late data and answers that are never final | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/11_streaming.ipynb" target="_blank">Open in Colab</a> |
| 12 | The Cloud and an End-to-End Pipeline: counting the cost, putting it all together | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/12_cloud_and_pipeline.ipynb" target="_blank">Open in Colab</a> |

### Module E: A Real Warehouse, End to End

| # | Notebook | |
|---|----------|---|
| 13 | Meet a Real Warehouse: an inventory, the grain, missing values, keys and personal data | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/13_meet_a_real_warehouse.ipynb" target="_blank">Open in Colab</a> |
| 14 | Building the Warehouse: enforced keys, views, indexes and summary tables | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/14_building_the_warehouse.ipynb" target="_blank">Open in Colab</a> |
| 15 | From Warehouse to Documents: the same sales as MongoDB documents, and what each shape costs | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/15_warehouse_to_documents.ipynb" target="_blank">Open in Colab</a> |
| 16 | Exploring the Data with Spark: an exploratory data analysis that brings back only answers | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/16_exploring_with_spark.ipynb" target="_blank">Open in Colab</a> |
| 17 | Machine Learning with Spark MLlib: pipelines, honest evaluation, leakage and customer segments | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/17_spark_mllib.ipynb" target="_blank">Open in Colab</a> |
| 18 | Measuring Scale: pandas, SQLite and Spark on growing data, and when one machine is enough | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-one-table-to-a-cluster/18_measuring_scale.ipynb" target="_blank">Open in Colab</a> |

---

## From Papers to Practice: Landmark Deep Learning Architectures
{: #landmark-architectures}

A course on the architectures that shaped deep learning. Each notebook starts from one or two landmark papers, linked in full, explains the problem they solved in plain words, builds the architecture in PyTorch, and trains it at a scale that fits a laptop or a free Colab session. Every claim of the paper is put to a small experiment: a perceptron that cannot learn XOR, a 32-layer network that is worse than an 8-layer one until shortcuts are added, an RNN that forgets after 50 steps, an encoder whose accuracy collapses with sentence length until attention is added.

The notebooks are saved **already run**, with every result commented, so they can be read or presented without waiting. Each one opens with a box on **training time and limitations**: how long the training took, what was scaled down compared with the paper, and why the numbers differ. Very large models (AlexNet, VGG, ResNet-50) are not retrained; their official pretrained weights are loaded instead. New architectures are added one notebook at a time.

The course assumes the foundations of neural networks and PyTorch, which are taught in [From Python to Deep Learning and Fine-Tuning](#deep-learning).

---

| # | Architecture and papers | |
|---|----------|---|
| 1 | The Perceptron and the MLP: Rosenblatt (1958), Minsky and Papert (1969), backpropagation (1986). XOR and hidden representations | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/01_perceptron_and_mlp.ipynb" target="_blank">Open in Colab</a> |
| 2 | LeNet-5: LeCun et al. (1998). Convolutions, shared weights and pooling on handwritten digits, and robustness to shifts | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/02_lenet5.ipynb" target="_blank">Open in Colab</a> |
| 3 | AlexNet and VGG: Krizhevsky et al. (2012), Simonyan and Zisserman (2014). ReLU, depth with 3 × 3 filters, pretrained ImageNet models | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/03_alexnet_and_vgg.ipynb" target="_blank">Open in Colab</a> |
| 4 | ResNet: He et al. (2015). The degradation problem reproduced, and the residual shortcut that fixes it | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/04_resnet.ipynb" target="_blank">Open in Colab</a> |
| 5 | LSTM: Hochreiter and Schmidhuber (1997). Vanishing gradients through time, measured on the adding problem | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/05_lstm.ipynb" target="_blank">Open in Colab</a> |
| 6 | Sequence to Sequence and Attention: Sutskever et al., Cho et al., Bahdanau et al. (2014). The bottleneck and attention maps | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/06_seq2seq_attention.ipynb" target="_blank">Open in Colab</a> |
| 7 | The Transformer: Vaswani et al. (2017). Self-attention, multi-head attention and positional encoding written by hand | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/07_transformer.ipynb" target="_blank">Open in Colab</a> |
| 8 | Autoencoders and VAEs: Hinton and Salakhutdinov (2006), Kingma and Welling (2013). Compression, latent spaces and new digits | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/08_autoencoder_vae.ipynb" target="_blank">Open in Colab</a> |
| 9 | Generative Adversarial Networks: Goodfellow et al. (2014), DCGAN (2015). A forger against a detective, quality and variety | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-papers-to-practice/09_gan.ipynb" target="_blank">Open in Colab</a> |

---

## From Random Moves to Winning Agents: Reinforcement Learning with Games
{: #reinforcement-learning}

A complete course on agents that learn by trial and error. Nobody shows them the right answer: they act, receive a reward, and work out for themselves how to get more of it. Every idea is taught with a game, from a row of slot machines to Snake, a lunar lander, Flappy Bird and Connect Four, and in almost every notebook you watch a video of the agent you have just trained. The notebooks run in Google Colab without a GPU.

Each method is first explained in plain words, then written by hand in a few lines of Python, and only then taken from a library: Q-learning, deep Q-networks, policy gradients, PPO, tree search and self-play. Results in this field vary a great deal from one run to the next, so the course measures before it claims, and says so when an experiment shows no clear difference.

The course assumes you can program in Python. From Module C on the agents are neural networks in PyTorch, which are covered in [From Python to Deep Learning and Fine-Tuning](#deep-learning). Most cells finish in seconds. A few train an agent for some minutes, and the notebook says so beforehand.

---

### Module A: Foundations

| # | Notebook | |
|---|----------|---|
| 1 | Learning by Trial and Error: slot machines, estimating values, exploring and exploiting | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/01_trial_and_error.ipynb" target="_blank">Open in Colab</a> |
| 2 | Worlds, States and Rewards: environments, returns, policies, the Gymnasium library | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/02_worlds_states_rewards.ipynb" target="_blank">Open in Colab</a> |
| 3 | Planning with the Bellman Equations: value functions, policy iteration, value iteration | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/03_planning_bellman.ipynb" target="_blank">Open in Colab</a> |
| 4 | Learning from Complete Episodes: Monte Carlo methods, Blackjack learned from wins and losses | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/04_learning_from_episodes.ipynb" target="_blank">Open in Colab</a> |

### Module B: Learning with a Table

| # | Notebook | |
|---|----------|---|
| 5 | Learning Step by Step: SARSA and Q-learning, on-policy and off-policy | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/05_sarsa_and_q_learning.ipynb" target="_blank">Open in Colab</a> |
| 6 | Building Snake: a game of our own as an environment, observations and rewards | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/06_building_snake.ipynb" target="_blank">Open in Colab</a> |
| 7 | A Snake That Learns: Q-learning on Snake, exploration, reward hacking, the limits of tables | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/07_a_snake_that_learns.ipynb" target="_blank">Open in Colab</a> |

### Module C: Deep Value-Based Learning

| # | Notebook | |
|---|----------|---|
| 8 | When the Table Is Too Big: a network as Q-function, and why it is unstable | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/08_when_the_table_is_too_big.ipynb" target="_blank">Open in Colab</a> |
| 9 | Deep Q-Networks: experience replay, target networks, landing a spacecraft | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/09_deep_q_networks.ipynb" target="_blank">Open in Colab</a> |
| 10 | Better Deep Q-Networks: Double DQN, dueling networks, prioritised replay, Flappy Bird | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/10_better_deep_q_networks.ipynb" target="_blank">Open in Colab</a> |
| 11 | Learning from Pixels: convolutional agents, frame stacking, Atari, the Pokémon Red project | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/11_learning_from_pixels.ipynb" target="_blank">Open in Colab</a> |

### Module D: Policy-Based Learning

| # | Notebook | |
|---|----------|---|
| 12 | Policy Gradients: policy networks, REINFORCE, baselines | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/12_policy_gradients.ipynb" target="_blank">Open in Colab</a> |
| 13 | Actor-Critic Methods: advantages, a critic, generalised advantage estimation, A2C | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/13_actor_critic.ipynb" target="_blank">Open in Colab</a> |
| 14 | Proximal Policy Optimisation: the clipped objective, by hand and from a library | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/14_proximal_policy_optimisation.ipynb" target="_blank">Open in Colab</a> |
| 15 | Continuous Actions: Gaussian policies, swinging up a pendulum, off-policy control with SAC | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/15_continuous_actions.ipynb" target="_blank">Open in Colab</a> |

### Module E: Beyond a Single Agent

| # | Notebook | |
|---|----------|---|
| 16 | Planning and Tree Search: Dyna-Q, minimax, Monte Carlo tree search, the idea of AlphaZero | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/16_planning_and_tree_search.ipynb" target="_blank">Open in Colab</a> |
| 17 | Opponents and Self-Play: self-play, games without a best move, a monster-battle tournament | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/17_opponents_and_self_play.ipynb" target="_blank">Open in Colab</a> |
| 18 | Reinforcement Learning in Practice: seeds and confidence intervals, reward design, your own project | <a href="https://colab.research.google.com/github/giannis00/giannis00.github.io/blob/main/assets/jupyter/from-random-moves-to-winning-agents/18_rl_in_practice.ipynb" target="_blank">Open in Colab</a> |
