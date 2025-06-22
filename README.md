______________________________________________________________________________________________________________________________________________________________________________________________________________________
# Routing Protocol Simulation (RIP)
______________________________________________________________________________________________________________________________________________________________________________________________________________________

This project simulates a simplified routing protocol (RIP - Routing Information Protocol) using Python threads and data structures. Each node represents a router, maintaining a routing table and exchanging information with its neighbors.

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

Simulation inspired by networking classes and developed for educational purposes.



