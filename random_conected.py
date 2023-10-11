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

# assigning input neurons randomly
inputs_set = 0
outputs_set = 0
while inputs_set < input_neurons or outputs_set < output_neurons:
    for neuron_key in neurons_chain_W:
            set_not_set = randint(1,2)
            if set_not_set == 1:
                input_output = randint(1,2)
                if inputs_set < input_neurons:
                    if input_output == 1:
                        neurons_chain_W[neuron_key].append('input_neuron')
                        inputs_set +=1
                        print(f'Neuron {neuron_key} are Input neuron: \n {neurons_chain_W[neuron_key]}')
                elif outputs_set < output_neurons:
                    if input_output == 2:
                        neurons_chain_W[neuron_key].append('output_neuron')
                        outputs_set +=1
                        print(f'Neuron {neuron_key} are Output neuron: \n {neurons_chain_W[neuron_key]}')

