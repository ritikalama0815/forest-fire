def train_model(model, train_dataset, val_dataset, epochs=20):

    history = model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=epochs
    )
    return history