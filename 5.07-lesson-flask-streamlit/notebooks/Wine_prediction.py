{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "08caed09-f8ff-4597-89ce-7fa676c3a784",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.datasets import load_wine\n",
    "from sklearn.model_selection import train_test_split, cross_val_score\n",
    "from sklearn.linear_model import LinearRegression, LogisticRegression\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "import streamlit as st\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7bc5e6d0-59f8-42b3-bb8d-c69736dc4338",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = load_wine()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8c09d824-8c1a-445d-b7b6-0a1245fe0521",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'.. _wine_dataset:\\n\\nWine recognition dataset\\n------------------------\\n\\n**Data Set Characteristics:**\\n\\n    :Number of Instances: 178 (50 in each of three classes)\\n    :Number of Attributes: 13 numeric, predictive attributes and the class\\n    :Attribute Information:\\n \\t\\t- Alcohol\\n \\t\\t- Malic acid\\n \\t\\t- Ash\\n\\t\\t- Alcalinity of ash  \\n \\t\\t- Magnesium\\n\\t\\t- Total phenols\\n \\t\\t- Flavanoids\\n \\t\\t- Nonflavanoid phenols\\n \\t\\t- Proanthocyanins\\n\\t\\t- Color intensity\\n \\t\\t- Hue\\n \\t\\t- OD280/OD315 of diluted wines\\n \\t\\t- Proline\\n\\n    - class:\\n            - class_0\\n            - class_1\\n            - class_2\\n\\t\\t\\n    :Summary Statistics:\\n    \\n    ============================= ==== ===== ======= =====\\n                                   Min   Max   Mean     SD\\n    ============================= ==== ===== ======= =====\\n    Alcohol:                      11.0  14.8    13.0   0.8\\n    Malic Acid:                   0.74  5.80    2.34  1.12\\n    Ash:                          1.36  3.23    2.36  0.27\\n    Alcalinity of Ash:            10.6  30.0    19.5   3.3\\n    Magnesium:                    70.0 162.0    99.7  14.3\\n    Total Phenols:                0.98  3.88    2.29  0.63\\n    Flavanoids:                   0.34  5.08    2.03  1.00\\n    Nonflavanoid Phenols:         0.13  0.66    0.36  0.12\\n    Proanthocyanins:              0.41  3.58    1.59  0.57\\n    Colour Intensity:              1.3  13.0     5.1   2.3\\n    Hue:                          0.48  1.71    0.96  0.23\\n    OD280/OD315 of diluted wines: 1.27  4.00    2.61  0.71\\n    Proline:                       278  1680     746   315\\n    ============================= ==== ===== ======= =====\\n\\n    :Missing Attribute Values: None\\n    :Class Distribution: class_0 (59), class_1 (71), class_2 (48)\\n    :Creator: R.A. Fisher\\n    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\\n    :Date: July, 1988\\n\\nThis is a copy of UCI ML Wine recognition datasets.\\nhttps://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data\\n\\nThe data is the results of a chemical analysis of wines grown in the same\\nregion in Italy by three different cultivators. There are thirteen different\\nmeasurements taken for different constituents found in the three types of\\nwine.\\n\\nOriginal Owners: \\n\\nForina, M. et al, PARVUS - \\nAn Extendible Package for Data Exploration, Classification and Correlation. \\nInstitute of Pharmaceutical and Food Analysis and Technologies,\\nVia Brigata Salerno, 16147 Genoa, Italy.\\n\\nCitation:\\n\\nLichman, M. (2013). UCI Machine Learning Repository\\n[https://archive.ics.uci.edu/ml]. Irvine, CA: University of California,\\nSchool of Information and Computer Science. \\n\\n.. topic:: References\\n\\n  (1) S. Aeberhard, D. Coomans and O. de Vel, \\n  Comparison of Classifiers in High Dimensional Settings, \\n  Tech. Rep. no. 92-02, (1992), Dept. of Computer Science and Dept. of  \\n  Mathematics and Statistics, James Cook University of North Queensland. \\n  (Also submitted to Technometrics). \\n\\n  The data was used with many others for comparing various \\n  classifiers. The classes are separable, though only RDA \\n  has achieved 100% correct classification. \\n  (RDA : 100%, QDA 99.4%, LDA 98.9%, 1NN 96.1% (z-transformed data)) \\n  (All results using the leave-one-out technique) \\n\\n  (2) S. Aeberhard, D. Coomans and O. de Vel, \\n  \"THE CLASSIFICATION PERFORMANCE OF RDA\" \\n  Tech. Rep. no. 92-01, (1992), Dept. of Computer Science and Dept. of \\n  Mathematics and Statistics, James Cook University of North Queensland. \\n  (Also submitted to Journal of Chemometrics).\\n'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wine.DESCR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fcfce698-ea94-4b66-a122-07134367deb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "wine = pd.DataFrame(data.data, columns=data.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "399bde08-ef98-4ee6-9cbd-6aceba257393",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>alcohol</th>\n",
       "      <th>malic_acid</th>\n",
       "      <th>ash</th>\n",
       "      <th>alcalinity_of_ash</th>\n",
       "      <th>magnesium</th>\n",
       "      <th>total_phenols</th>\n",
       "      <th>flavanoids</th>\n",
       "      <th>nonflavanoid_phenols</th>\n",
       "      <th>proanthocyanins</th>\n",
       "      <th>color_intensity</th>\n",
       "      <th>hue</th>\n",
       "      <th>od280/od315_of_diluted_wines</th>\n",
       "      <th>proline</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>14.23</td>\n",
       "      <td>1.71</td>\n",
       "      <td>2.43</td>\n",
       "      <td>15.6</td>\n",
       "      <td>127.0</td>\n",
       "      <td>2.80</td>\n",
       "      <td>3.06</td>\n",
       "      <td>0.28</td>\n",
       "      <td>2.29</td>\n",
       "      <td>5.64</td>\n",
       "      <td>1.04</td>\n",
       "      <td>3.92</td>\n",
       "      <td>1065.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>13.20</td>\n",
       "      <td>1.78</td>\n",
       "      <td>2.14</td>\n",
       "      <td>11.2</td>\n",
       "      <td>100.0</td>\n",
       "      <td>2.65</td>\n",
       "      <td>2.76</td>\n",
       "      <td>0.26</td>\n",
       "      <td>1.28</td>\n",
       "      <td>4.38</td>\n",
       "      <td>1.05</td>\n",
       "      <td>3.40</td>\n",
       "      <td>1050.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13.16</td>\n",
       "      <td>2.36</td>\n",
       "      <td>2.67</td>\n",
       "      <td>18.6</td>\n",
       "      <td>101.0</td>\n",
       "      <td>2.80</td>\n",
       "      <td>3.24</td>\n",
       "      <td>0.30</td>\n",
       "      <td>2.81</td>\n",
       "      <td>5.68</td>\n",
       "      <td>1.03</td>\n",
       "      <td>3.17</td>\n",
       "      <td>1185.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>14.37</td>\n",
       "      <td>1.95</td>\n",
       "      <td>2.50</td>\n",
       "      <td>16.8</td>\n",
       "      <td>113.0</td>\n",
       "      <td>3.85</td>\n",
       "      <td>3.49</td>\n",
       "      <td>0.24</td>\n",
       "      <td>2.18</td>\n",
       "      <td>7.80</td>\n",
       "      <td>0.86</td>\n",
       "      <td>3.45</td>\n",
       "      <td>1480.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>13.24</td>\n",
       "      <td>2.59</td>\n",
       "      <td>2.87</td>\n",
       "      <td>21.0</td>\n",
       "      <td>118.0</td>\n",
       "      <td>2.80</td>\n",
       "      <td>2.69</td>\n",
       "      <td>0.39</td>\n",
       "      <td>1.82</td>\n",
       "      <td>4.32</td>\n",
       "      <td>1.04</td>\n",
       "      <td>2.93</td>\n",
       "      <td>735.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   alcohol  malic_acid   ash  alcalinity_of_ash  magnesium  total_phenols  \\\n",
       "0    14.23        1.71  2.43               15.6      127.0           2.80   \n",
       "1    13.20        1.78  2.14               11.2      100.0           2.65   \n",
       "2    13.16        2.36  2.67               18.6      101.0           2.80   \n",
       "3    14.37        1.95  2.50               16.8      113.0           3.85   \n",
       "4    13.24        2.59  2.87               21.0      118.0           2.80   \n",
       "\n",
       "   flavanoids  nonflavanoid_phenols  proanthocyanins  color_intensity   hue  \\\n",
       "0        3.06                  0.28             2.29             5.64  1.04   \n",
       "1        2.76                  0.26             1.28             4.38  1.05   \n",
       "2        3.24                  0.30             2.81             5.68  1.03   \n",
       "3        3.49                  0.24             2.18             7.80  0.86   \n",
       "4        2.69                  0.39             1.82             4.32  1.04   \n",
       "\n",
       "   od280/od315_of_diluted_wines  proline  \n",
       "0                          3.92   1065.0  \n",
       "1                          3.40   1050.0  \n",
       "2                          3.17   1185.0  \n",
       "3                          3.45   1480.0  \n",
       "4                          2.93    735.0  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wine.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "4e88bbfb-125b-454c-bfe9-c30ffd3c4890",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.scatterplot(x=wine['alcohol'], y = wine['color_intensity']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1386113e-e13e-4751-8071-72c60d729c2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x7ff29d321400>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 2340x2340 with 182 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(wine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "f8ba5efb-5557-4d04-aa90-bee22c8ffbe1",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = wine.drop(columns=['alcohol', 'ash', 'malic_acid', 'hue', 'proanthocyanins', 'od280/od315_of_diluted_wines'])\n",
    "y = wine['alcohol']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "ca55939b-6905-4d93-8631-3011b08356d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 2022)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "91d51188-6bea-40a0-9024-e9b015bbb916",
   "metadata": {},
   "outputs": [],
   "source": [
    "lr = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "a2f488e8-cd25-4f89-8911-11d40a84fd80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lr.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "9f2ca4e0-3584-45ae-8cd5-37c7503a6c5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.47680293690090414"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cross_val_score(lr, X_train, y_train).mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "a81286a9-5d25-4e8a-878a-42f751586144",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_preds = lr.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "29b4ecc3-218b-4b4b-8085-f6e875451e87",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/jonathanbeltran/opt/miniconda3/lib/python3.9/site-packages/seaborn/_decorators.py:36: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='alcohol'>"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.scatterplot(y_test , y_preds )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "e5dc8894-9be1-4c4f-95ff-222857f84b6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"Simple Linear Regression on Wine Data set\")\n",
    "st.text(\"What is a strong predictor for alcohol content in your fav wine?\")\n",
    "\n",
    "\n",
    "page = st.sidebar.selectbox('Select a page', ('About', 'The Model'))\n",
    "\n",
    "if page == 'About':\n",
    "    st.write(\"We used the wine data set to see what featues contribute to a wine's alcohol content\")\n",
    "\n",
    "if page == 'The Model':\n",
    "    st.write(\"Below you'll find a plot of our alcohol content for predicted and actual values\")\n",
    "    sns.scatterplot(y_test , y_preds )\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47df13ce-bc56-4516-ba2a-aebfa34a09db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}