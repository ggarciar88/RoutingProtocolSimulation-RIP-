```text
                             _           ___   ___  
                            (_)         / _ \ / _ \   not©          not©          not©          not©          not©          not©          not©          not©          not©
   __ _ __ _ __ _ _ __ ___ _ __ _ _  __| (_) | (_) |       not©          not©          not©          not©          not©          not©          not©          not©          not©    
  / _` |/ _` |/ _` | '__/ __| |/ _` |   > _ < > _ <              not©          not©          not©          not©          not©          not©          not©          not©          not©     
 | (_| | (_| | (_| | |  ( __| | (_| | || (_) | (_) |
  \__, |\__, |\__,_|_|\_ ___|_|\__,_|_| \___/ \___/                 
   __/ | __/ |                                       
  |___/ |___/                                        
     

@ggarciar88  // RoutingProtocolSimulation-RIP
______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Routing Protocol Simulation (RIP)
______________________________________________________________________________________________________________________________________________________________________________________________________________________

This project simulates a simplified routing protocol (RIP - Routing Information Protocol) using Python threads and data structures.
Each node represents a router, maintaining a routing table and exchanging information with its neighbors.

## Features

- Threaded simulation of network routers
- Periodic routing table exchange (distance-vector algorithm)
- Automatic convergence to shortest paths
- Simple command-line output of routing tables

## File Structure

- `main.py`: Main simulation file

## How It Works

Each node:
- Has direct neighbors with associated costs
- Sends its routing table to neighbors
- Updates its table based on received tables (using RIP logic)
- Prints its final routing table after convergence

## Sample Topology

          A
         / \
        B---C
         \ /
          D

## How to Run

1. Install Python 3
2. Run the following script on the bash:

       python3 main.py


You will see each node’s routing table printed after simulation.

## Future Improvements

- Support for OSPF (link-state)
- BGP simulation (with autonomous systems and policies)
- GUI or web interface for visualization

## License

This project is open-source and free to use for educational and personal learning purposes.
Released under the MIT License (view LICENSE file).




