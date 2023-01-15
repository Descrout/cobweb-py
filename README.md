# Cobweb

Inefficient but easy to understand neural network library.  
This library has been made from scratch and does not use any library. (not even numpy 😱)

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
# input list, label list
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