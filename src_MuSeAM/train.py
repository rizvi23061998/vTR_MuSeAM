from model import nn_model
import time
import sys

# get dictionary from text file
def train(file_name):
    dict = {}
    with open(file_name) as f:
        for line in f:
        #    print(line)
           (key, val) = line.split()
           dict[key] = val

    # change string values to integer values
    dict["filters"] = int(dict["filters"])
    dict["kernel_size"] = int(dict["kernel_size"])
    dict["epochs"] = int(dict["epochs"])
    dict["batch_size"] = int(dict["batch_size"])
    dict["alpha"] = int(dict["alpha"])
    

    return dict

def main(argv = None):
    if argv is None:
        argv = sys.argv

        argumentfile = argv[1]
        arguments = []
        with open(argumentfile,'r') as f:
            for line in f:
                arguments.append(line.rstrip('\n'))

        print(arguments)
        #input args
        parameter_file = arguments[0]
        #e.g. parameter1.txt
        fasta_file = arguments[1]
        #e.g. sequences.fa
        readout_file = arguments[2]
        #e.g. wt_readout.dat
        
    ## excute the code
    start_time = time.time()

    dict = train(parameter_file)

    nn_model(fasta_file, readout_file, filters=dict["filters"], kernel_size=dict["kernel_size"], pool_type=dict["pool_type"], regularizer=dict["regularizer"],
            activation_type=dict["activation_type"], epochs=dict["epochs"], batch_size=dict["batch_size"],alpha=dict["alpha"])

    # reports time consumed during execution (secs)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())

#train('parameter1.txt')
