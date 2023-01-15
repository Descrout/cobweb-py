from cobweb.matris import Matrix
import cobweb.activations as activations
import json

class Cobweb:
    def __init__(self, input, output, learning_rate = 0.1, output_activation = "sigmoid"):
        self.layer_sizes = [input, output]
        self.weights = [Matrix(output, input)]
        self.biases = [Matrix(output, 1)]
        self.activations = [output_activation]
        self.learning_rate = learning_rate

    def insert_before_last(arr, el):
        return [*arr[:-1], el, arr[-1]]

    def add_layer(self, neuron_count, activation = "sigmoid"):
        self.activations = Cobweb.insert_before_last(self.activations, activation)
        self.biases = Cobweb.insert_before_last(self.biases, Matrix(neuron_count, 1))
        self.layer_sizes = Cobweb.insert_before_last(self.layer_sizes, neuron_count)
        self.weights = [Matrix(shape[0], shape[1]) for shape in self.shapes()]

    def shapes(self):
        return [(a,b) for a,b in zip(self.layer_sizes[1:], self.layer_sizes[:-1])]

    def predict(self,a):
        a = Matrix.From1DList(a)
        for i, (w,b) in enumerate(zip(self.weights, self.biases)):
            a = w.matmul(a) + b
            a.map(activations.get(self.activations[i]).func)
        return a.flatten()
    
    def layer_values(self, a):
        values = [Matrix.From1DList(a)]
        for i, (w,b) in enumerate(zip(self.weights, self.biases)):
            x = w.matmul(values[-1]) + b
            x.map(activations.get(self.activations[i]).func)
            values.append(x)
        return values
    
    def train(self, input_list, target_list):
        layers = self.layer_values(input_list)
        targets = Matrix.From1DList(target_list)

        latest_errors = targets - layers[-1]
        for i in range(len(layers) - 1, 0, -1):
            gradients = Matrix.Map(layers[i], activations.get(self.activations[i - 1]).dfunc)
            gradients.mul(latest_errors)
            gradients.mul(self.learning_rate)

            layer_before_t = layers[i - 1].transpose()
            deltas = gradients.matmul(layer_before_t)
            self.weights[i - 1].add(deltas)
            self.biases[i - 1].add(gradients)

            latest_errors = self.weights[i - 1].transpose().matmul(latest_errors)

    def save(self, filename):
        save_dict = {
            "layer_sizes": self.layer_sizes,
            "activations" : self.activations,
            "learning_rate" : self.learning_rate,
            "weights": [],
            "biases": [],
        }

        for w in self.weights:
            save_dict["weights"].append(w.__dict__)

        for b in self.biases:
            save_dict["biases"].append(b.__dict__)

        with open( filename , "w" ) as write:
            json.dump( save_dict , write )
    
    @staticmethod
    def load(filename):
        nn = Cobweb(1, 1)

        with open( filename , "r" ) as read:
            data = json.load(read)

            nn.layer_sizes = data["layer_sizes"]
            nn.learning_rate = data["learning_rate"]
            nn.activations = data["activations"]
            
            weights = data["weights"]
            nn.weights.clear()
            for weight in weights:
                nn.weights.append(Matrix.From2DList(weight["data"]))

            biases = data["biases"]
            nn.biases.clear()
            for bias in biases:
                nn.biases.append(Matrix.From2DList(bias["data"]))

        return nn