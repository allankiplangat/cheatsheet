# ROLE OF FEATURES IN MACHINE LEARNING:

- [Role of features in machine learning](#role-of-features-in-machine-learning)
  - [Features and Labels in Machine Learning](#features-and-labels-in-machine-learning)

## Features and Labels in Machine Learning

- A machine learning algorithm is an algorithm that is able to learn from data
- Works with a huge maze of data, finds patterns and make intelligent decisions

#### Types of machine learning problems

- **Classification** (Classifying instances) used to predict classes or cateories
- **Regression** (predicting a continuous numeric value)
- **Clustering** (Finding logical groupings or patterns existing in data)
- **Dimensionality Reduction** (Extracting latent features from the data)

#### Terminology

- **Input: Feature Vector** The input into an ML algorithm (The X variables)
- **Output: Label**
- **X Variables** The attributes that the ML algorithm focuses on are called **features**
- **Vector/list** Each data point of such features
- **Y-variables** The attributes that the ML algorithm tries to predict (**labels**)
- Types of labels
  - Categorical (Classification)
  - Continuous (regression)

#### The Machine Learning Workflow

![alt text](</machine learning/mlpipeline.png>)

- **Selecting and Extracting Features** Raw data, prepare data, cleaned data (time consuming step) and all encompases feature engineering
-

## Feature Engineering

- Engineering the features so that we get the best out of the model
- Block and tacle work
- Bespoke - specific to:
  - Problem
  - Data

## Scope of Feature Engineering

- **Feature Selection** - Selecting the most relevant features for the models
- **Feature Learning** - Using supervised or unsupervised techniques to learn latent features that exist in the data
- **Feature Extraction** - Involves transformation or reorientation of our input features into fundamentally transformed derived features (unrecognisable) and cant be interpreted
- **Feature Combination** - Might have raw granular feature in your data can e combine to get a more meaningful feature with more predictive power
- **Dimensionality reduction** - Reducing the complexity of the input data reorienting data in new axis which better represent the data

#### Feature Selection

- Choosing the best subset from within an existing set of features (x-variables), without substantially transforming them
  > **Use Case**
  > Many X-variables most of which contain little information some of which are very meaningful Meaningful variables are independent of each other

#### Categories of feature selection techniques

- **Filter Methods** Applying statistical techniques to select the most relevant features e.g chi square analysis anova analysis, mutual information
- **Embedded Methods** Building a machine learning method that assigns importance to the different features and selects most important features
  - Relevant features selected by training a machine learning model i.e Lasso regression, decision trees
- **Wrapper Methods** (Lie between Filter and embedded) training a number of differeent candidates on a subset of features anc choose the subset of features that produces the est model
  - Build candidate models by selecting feature subsets - choose the subset which gives the best model

#### Feature Learning

- Rely on ML algorithms rather than human experts to learn the best representations of complex data such as images and videos. (Also known as **Representation Learning**)

  > **Supervised Feature Learning**
  > Features are learnt using labeled data e. Neural networks, They greatly reduce need for expert judgment

- **Traditional ML-based systems** rely on experts to decide what features to pay attention to.
- **Representation** ML-based system figure out by themselves what features to pay attention to e.g Neural Networks

> **Unsupervised Feature Learning**

- Features need to be learned in absence of labeled corpus
  - Clustering
  - Dictionary learning for image data (Learns sparse representation of dense features)
  - Autoencoders (To extranct latent significant representation of the data) - for Neural networks

#### Feature Extraction

- You might have machine learning models that cant work directly with raw features which works well with derived features
- Differs from feature selection in that input features are fundamentally transformed into derived features, which are often unrecognizable and hard to interpret
  - Image descriptors for images
  - Principal components for matrices
  - Tf-Idf for documents
  - Feature extraction usually also leads to dimensionality reduction
  - Explicit objective is to re-express feature in a "better" form
  - Not to reduce number of X columns

#### Feature Combination

- The raw data you might be working with might have very granular information which might not have much predictive power
- Aggregates and brings features together to get a feature with more predictive power
- Some features naturally work better when considered togeter
- Original feature might be raw or too granular
- Bringing features together might improve the predictive power of features

#### Dimentionality Reduction

- Apply pre-processing algorithms to reduce complexity of raw features (To reduce curse of dimentionality)
- Specifically aim to reduce number of input features
- Excess number of features leads to severe problems
  - Curse of Dimensionality (Problems visualizing data, poor quality overfitted models- well in training and poor in the real world)
- Dimensionality reduction explicitly aim to solve curse of Dimensionality while preserving much information as possible
- Form of unsupervised learning
- Based on data you are working with you might use. - **Linear Data** - Principle component analysis(PCA) - **Non Linear data** - Manifold Learnig - **Latent Semantic Analysis** - Working with text dat - **Autoencoding** - images

#### Training, Test and Validation Data

- Data used to train a model cannot be used to evaluate a model (model has seen all instances of the training data)
- If you evaluate your model on the training data the model gives a great score that doesnt mean its a good model,
- The model may have memorized training instances
- Model robustness cannot be measured on instances it has seen before
- Test set can be used to choose the best candidate model
- Model evaluation on instances the model has not seen during training
- **Evaluation can be biased**
- When you use the same instances the test set to pick the best candidate model, it can lead to a kind of overfitting

> **Overfitting on Test Set** choosing best candidate model on the Test Set leads to tis overfitting. Occurs when data is split into just two sets: Train and Test

#### Cross-validation (Singular Cross-validation)

![alt text](</machine learning/cross-validation.png>)

- Carve out a separate validation set of data points; use this to evaluate different candidate models. Data now split into 3 sets: Training, validation and test.
- Hold out 2 subsets of the original data, validation data and test data
- Train data to produce candidate models - validation data to evaluate models
- Test data applied to the selected model to provide an unbiased evaluation to the final model
- Now can have multiple candidate models, and select the est one - **Hyperparameter Tuning**
- For N candidate models, run N training and N validation processes but just 1 test process
- The models performance on the validation set is incorporated into the model itself and this may introduce bias

#### K-fold Cross-Validation

- For each candidate model, repeatedly train and validate using different subsets of training data.
- Much more computationally intensive , but very robust -does not waste data
  ![alt text](</machine learning/kfold1.png>)
  ![alt text](</machine learning/kfold2.png>)
  ![alt text](</machine learning/kfold3.png>)
