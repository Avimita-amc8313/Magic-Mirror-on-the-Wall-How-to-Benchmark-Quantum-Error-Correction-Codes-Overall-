# Description of the user input and QECC reference json files

## user_input/user_input.json

"situation": Name of the scenario,

"qType": type of qubit being used,

"maxSpare": number of qubits available in the system that can be used for error correction,

"qOrig": number of qubits in the original circuit that needs to be corrected,

"multiQGate": is there a multi-qubit gate? --> yes or no,

"errType": type of error that needs to be corrected --> bit-flip, phase-flip or all-pauli,

"depErr": depolarizing error rate,

"gateErr": gate error rate,

"readErr": readout error rate


## QECCs/qecc_with_parameters.json

"QECC_name": {
          "qubit overhead": qubit overhead as a numeric value or as a function of distance, d,

          "error threshold": the error threshold of the QECC,

          "error protection": type of error the QECC gives protection from --> ["bit-flip", "phase-flip",  "all-pauli"],

          "decoding": number of decoding algorithms available to be used for the QECC,

          "transversal gate": none or the complexity of the transversal gate usual employed by the QECC --> ,clifford gates: 1, teleportation: 2 or lattice surgery: 3

          "scalability": if the QECC is scalable or not --> yes or no,

          "realization": the type of qubits the QECC has been realized on --> ["simulation", "superconducting", "trapped-ion", "liquid-state-nmr", "nv-diamond", "optical-system",      "rydberg-atom", "ising-anyons"],

          "complexity": rate of complexity of the QECC --> very low: 1, low: 2, medium: 3, high: 4, very high: 5 or extremely high: 6 
        }