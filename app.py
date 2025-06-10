from scripts.load_data import load_dataset
from scripts.preprocess import preprocess_dataset
from scripts.model import create_model
from scripts.train import train_model
from scripts.evaluate import evaluate_model
from scripts.predict import predict_image

train_dataset = load_dataset('dataset/train')
test_dataset = load_dataset('dataset/test')
val_dataset = load_dataset('dataset/val')


train_dataset = preprocess_dataset(train_dataset)
test_dataset = preprocess_dataset(test_dataset)
val_dataset = preprocess_dataset(val_dataset)

model = create_model()
#train on train dataset, test on val dataset and train the model 20 times over the dataset
history = train_model(model, train_dataset, val_dataset, epochs=20)

evaluate_model(model, test_dataset)
print("Model training and evaluation completed.")

print(predict_image(model, 'sample_fire.jpg'))
