import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

data = pd.read_csv("data/Mall_Customers.csv")

features = ["Annual Income (k$)", "Spending Score (1-100)"]

X = data[features]

kmeans = KMeans(n_clusters=5, random_state=42)

data["Cluster"] = kmeans.fit_predict(X)

print(data.head())
#
plt.figure(figsize=(10, 6))

plt.scatter(
    X["Annual Income (k$)"],
    X["Spending Score (1-100)"],
    c=data["Cluster"],
    s=50
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200,
    marker="X",
    label="Cluster Centers"
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("customer_clusters.png", dpi=150)
plt.show()
#
inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertia.append(model.inertia_)
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal K")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("elbow_method.png", dpi=150)
plt.show()