# Magic Mirror on the Wall, How to Benchmark Quantum Error Correction Codes, Overall ?

## Description

We present an adaptive QECC recommendation tool, a versatile framework that evaluates user-defined scenario characteristics to suggest a range of Quantum Error Correcting Codes (QECCs), ordered from most to least fitting, and provides the maximum achievable distance for each. This tool is designed to be evergreen, allowing for the inclusion of additional QECCs and the swift modification of their parameters without necessitating significant overhauls to the system. This ensures the framework's adaptability and relevance in the rapidly evolving quantum computing landscape. For instance, should a QECC that has not been previously realized on trapped-ion qubits later achieve this milestone, the framework can easily accommodate this new information.

Gate errors are the most weighted due to their extensive impact on the quantum system, followed by depolarizing and readout errors. Since all quantum errors can be categorized as Pauli errors, scenarios considering 'all-Pauli' errors are deemed most realistic. This flexibility aids in the versatility and characterization of QECCs. Each QECC includes a set of qubit types on which it has been implemented as one of its parameters. The 'simulation' type is consistently applied across all QECCs to accommodate those not yet realized in specific scenarios, ensuring that simulated implementations are considered for every QECC. The framework aims to optimize for reduced complexity in overall operations and lattice surgery, while enhancing the code distance and the availability of decoding algorithms. It generates a ranked list of QECCs from most to least suitable based on these considerations, along with the maximum achievable code distance for each QECC, determined by the user’s available qubits for error correction and the qubits in the original circuit.

This project is based on the methodologies described in the paper, Magic Mirror on the Wall, How to Benchmark Quantum Error Correction Codes, Overall ? (https://arxiv.org/abs/2402.11105).

## Packages Needed

The project requires the following Python packages:

- json
- sympy
- math

You can install these packages using pip.

## How to Run?

Begin by adding a user input in `user_input/user_input.json` and then execute `recommend_qecc.py` to get QECC recommendations. This script has an inbuilt `debug_mode` which, when activated, allows users to observe the filtration process of QECCs step by step until only the final recommendations are left. For a demonstration of how to run this process, refer to `running_process.ipynb`.

## Example User Input

The framework evaluates scenarios based on five key factors: the qubit type being used, the available number of qubits for error correction within the system, the count of qubits in the circuit requiring correction, the presence of multi-qubit gates in the circuit, and the types and rates of physical errors encountered (including Pauli errors like bit-flip, phase-flip, or all-Pauli, as well as depolarizing, gate, and readout errors).

```
{
    "situation": "scenario1",
    "qType": "superconducting",
    "maxSpare": "100",
    "qOrig": "1",
    "multiQGate": "no",
    "errType": "bit-flip",
    "depErr": "1E-4",
    "gateErr": "1E-3",
    "readErr": "1E-2"
}
```
Detailed description of this user_input file can be found in `doc/documentation.md`.

## Extending the Project

As of now the framework considers 8 QECCs: quantum repetition code, Shor code, Steane code, Toric code, Surface code, Bacon-Shor code, 3D color code and Heavy-hexagon code. The framework is designed to seamlessly integrate additional QECCs and to effortlessly update existing parameters. Whether a QECC is realized on a new qubit type previously unaccounted for, or if there's an improvement in its error threshold, these changes can be rapidly incorporated. This adaptability ensures the framework remains current with advancements in the field. All reference QECCs can be found in `QECCs/qecc_with_parameters.json`. Detailed description of this reference file can be found in `doc/documentation.md`.

An example QECC:

```
{
    "HeavyHexagon": {
        "qubit overhead": "((5*d^2-2*d-1)/2)",
        "error threshold": "0.045",
        "error protection": ["bit-flip", "phase-flip", "all-pauli"],
        "decoding": "3",
        "transversal gate": "3",
        "scalability": "yes",
        "realization": ["simulation", "superconducting"],
        "complexity": "6"
    }
}
```

## Cite This Work

```
@article{chatterjee2024magic,
  title={Magic Mirror on the Wall, How to Benchmark Quantum Error Correction Codes, Overall?},
  author={Chatterjee, Avimita and others},
  journal={arXiv preprint arXiv:2402.11105},
  year={2024}
}
```

## Contact

For any questions or inquiries about this project, please contact:

Name: Avimita Chatterjee
Email: amc8313@psu.edu