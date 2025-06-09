def evaluate_model(model, test_dataset):
    results = model.evaluate(test_dataset)
    print(f"Test Loss: {results[0]}")
    print(f"Test Accuracy: {results[1]}")