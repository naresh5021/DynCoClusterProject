
# DynCoCluster: A Dynamic Parallel Co-Clustering Framework for Scalable Recommendation Systems

DynCoCluster is a scalable and efficient deep learning-based recommendation framework built on a parallel co-clustering algorithm. It addresses the key limitations of traditional collaborative filtering and matrix factorization approaches by integrating dynamic clustering, feature engineering, and deep learning modules. The project is designed to perform well across large-scale datasets like Amazon Product Reviews and aims to deliver high recommendation accuracy, precision, and computational efficiency.

## 🔍 Key Features

- Dynamic Parallel Co-Clustering Engine
- Feature Engineering Module with TF-IDF and Sentiment Scoring
- Scalable Preprocessing Pipeline
- Model Evaluation and Benchmarking (MAP, Precision, F1-Score)
- Integrated with Visualization and Ablation Studies

## 📁 Project Structure

```
DynCoClusterProject/
│
├── data_loader/           # Scripts for loading and preprocessing dataset
│   └── preprocess.py
│
├── feature_engineering/   # Feature extraction and transformation
│   └── feature_extractor.py
│
├── model/                 # Core implementation of DynCoCluster model
│   └── dyncocluster.py
│
├── evaluation/            # Evaluation metrics and comparison functions
│   └── evaluator.py
│
├── visualizations/        # All EDA and result visualization scripts
│   └── plot_generator.py
│
├── main.py                # Entry point to run the full pipeline
├── config.py              # Hyperparameters and settings
└── requirements.txt       # Python dependencies
```

## 🚀 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DynCoCluster.git
   cd DynCoCluster
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main pipeline:
   ```bash
   python main.py
   ```

## 🧪 Dataset

The project uses the [Amazon Product Reviews dataset](https://nijianmo.github.io/amazon/index.html) with ~100,000+ reviews. The dataset includes review text, rating, product category, and user metadata.

## 📈 Results

- Precision: 92.3%
- Recall: 90.8%
- F1-Score: 91.5%
- MAP: 89.2%
- Execution Time: 45s

## 📚 Citation

If you use this framework in your research, please cite the following:

```
@article{your2025dyncocluster,
  title={DynCoCluster: A Dynamic Parallel Co-Clustering Framework for Scalable Recommendation Systems},
  author={J. Naresh Kumar et al.},
  journal={To Appear in SCI Journal},
  year={2025}
}
```

## 📬 Contact

For questions or contributions, please contact naresh5021@gmail.com.
