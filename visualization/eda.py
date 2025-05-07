import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()