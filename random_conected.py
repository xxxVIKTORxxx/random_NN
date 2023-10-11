import numpy as np
import pandas as pd
from random import randint

#defining random size of neuralnet
num_neurons = randint(10, 25)
print(f'Number of neurons: {num_neurons}')

#forming a sequence of neurons
neurons_chain = {}
for neuron in range(num_neurons):
    neurons_chain["neuron_{0}".format(neuron)] = []
#checker
print(neurons_chain)
print(f'Lenght check: {len(neurons_chain)}')


#building a random connections between the neurons
for neuron_key in neurons_chain:

    for another_neuron_key in neurons_chain:
        connect = randint(1,2)
        if connect == 1:
            neurons_chain[neuron_key].append(another_neuron_key)
        else:
            pass
#checking
for neuron_key in neurons_chain:
    print(f'Connections of {neuron_key} :\n {neurons_chain[neuron_key]}')


#adding weitghts to conenctions
neurons_chain_W = {}
for neuron_key in neurons_chain:
    neuron_connection_weights = []
    for neurons_connection in neurons_chain[neuron_key]:
        conenction_weight = np.random.uniform()
        to_append = [neurons_connection, conenction_weight]
        neuron_connection_weights.append(to_append)
        neurons_chain_W[neuron_key] = neuron_connection_weights
#CHECKER
print('AFTER WEIGHTS')
for neuron_key in neurons_chain_W:
    print(f'Connections of {neuron_key} :\n {neurons_chain_W[neuron_key]}')

#randomizing input and output neurons amount
input_neurons = randint( int((len(neurons_chain.keys())/3)*0.33), int(len(neurons_chain.keys())/3) )
output_neurons = randint( int((len(neurons_chain.keys())/3)*0.33), int(len(neurons_chain.keys())/3) )
print(f'input neurons amount: {input_neurons}; output neurons amount: {output_neurons}')

