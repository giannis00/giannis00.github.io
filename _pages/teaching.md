---
layout: page
permalink: /teaching/
title: teaching
description: Four complete open courses that run in the browser. From Python to deep learning, from zero to data structures and algorithms, from words to meaning in natural language processing, and from one table to a cluster.
nav: true
nav_order: 2
---

Four complete, self-contained courses. Every notebook runs directly in the browser via Google Colab: nothing to install. The first two start from a first line of Python. The other two assume you can already program.

- [**From Python to Deep Learning and Fine-Tuning**](#deep-learning): for those heading towards machine learning and AI.
- [**From Zero to Data Structures and Algorithms in Python**](#data-structures): a practice-first route through programming fundamentals, algorithms, and data structures.
- [**From Words to Meaning: Natural Language Processing in Python**](#nlp): how machines read, search, translate and summarise text, from counting words to retrieval-augmented generation.
- [**From One Table to a Cluster: Working with Data at Scale**](#data-at-scale): SQL, data warehouses, NoSQL, Spark and streaming, and how to tell when you need them.

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

## From One Table to a Cluster: Working with Data at Scale
{: #data-at-scale}

A complete course on what happens to data once there is a lot of it: SQL and indexes, data warehouses, columnar files, NoSQL, MapReduce, Spark, streaming and the cloud. It assumes you can already program in Python, and no knowledge of databases. The notebooks run directly in the browser via Google Colab: nothing to install.

One question runs through all 12 notebooks: what changes when the data no longer fits? In one table, in the time a query has, in memory, on one machine, and finally in time itself. Each idea is first explained in plain words, then built by hand in a few lines of Python, and only then handed to a professional tool. Every claim about speed or size is measured, including the cases where the simple approach beats the heavy machinery.

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
