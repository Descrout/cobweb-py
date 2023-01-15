from cobweb import Cobweb
import random

xor_rules = [
    {
        "input": [1.0, 1.0],
        "output": [0.0],
    },
    {
        "input": [1.0, 0.0],
        "output": [1.0],
    },
    {
        "input": [0.0, 0.0],
        "output": [0.0],
    },
    {
        "input": [0.0, 1.0],
        "output": [1.0],
    },
]

model_filename = "xor_model.json"

# Uncomment these lines to enable training

# training_data = [random.choice(xor_rules) for _ in range(80_000)]
# epoch = 5

# train_nn = Cobweb(2, 1)
# train_nn.add_layer(3)

# for _ in range(epoch):
#     random.shuffle(training_data)
#     for data in training_data:
#         train_nn.train(data["input"], data["output"])

# train_nn.save(model_filename)

loaded_nn = Cobweb.load(model_filename)

guess = loaded_nn.predict([1.0, 1.0])
print("Should be close to 0 => {}".format(guess))

guess = loaded_nn.predict([0.0, 1.0])
print("Should be close to 1 => {}".format(guess))

guess = loaded_nn.predict([1.0, 0.0])
print("Should be close to 1 => {}".format(guess))

guess = loaded_nn.predict([0.0, 0.0])
print("Should be close to 0 => {}".format(guess))

test_data = [random.choice(xor_rules) for _ in range(1000)]

correct = 0
for data in test_data:
    guess = [round(n) for n in loaded_nn.predict(data["input"])]
    target = data["output"]
    if guess == target:
        correct += 1

print("Accuracy: {}%".format(correct / len(test_data) * 100))