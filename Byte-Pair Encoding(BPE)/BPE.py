import kagglehub

# Download latest version
path = kagglehub.dataset_download("aliakay8/penn-treebank-dataset")

print("Path to dataset files:", path)