# Cobweb


| <img src="./logo.png" width="256" height="256">  | Inefficient but easy to understand neural network library. <br>Cobweb has been made from scratch. <br>It doesn't use any external library. <br>(not even numpy 😱) |
| ------------- | ------------- |


### Create a neural network
```python
from cobweb import Cobweb
# inputs, outputs
nn = Cobweb(3, 4)
nn.add_layer(8)
nn.add_layer(16, activation="tanh") #default = sigmoid 

# Fully connected layers:
# 3 -> 8 -> 16 -> 4
```

### Training (Backpropagation)
```python
# inputs, label
nn.train([0.6, 0.88, 0.36], [1, 0, 0, 0])
```

### Make a prediction
```python
guess = nn.predict([0.6, 0.88, 0.36])
print(guess)
```

### Save and Load Model
```python
# Save
nn.save("filename.json")
# Load
loaded_nn = Cobweb.load("filename.json")
```

You can checkout ``cobweb/matris.py`` for the handmade matrix math class.
