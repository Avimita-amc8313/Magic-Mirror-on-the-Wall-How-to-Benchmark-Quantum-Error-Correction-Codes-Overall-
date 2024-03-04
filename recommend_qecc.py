import json
import sympy as sp
import math

def load_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def calculate_average_error(depErr, gateErr, readErr):
    return (3 * float(gateErr) + 2 * float(depErr) + float(readErr)) / 6

def filter_qeccs(user_input, qeccs, debug_mode=False):  # Add debug_mode argument
    filtered_qeccs = []
    
    for situation in user_input['situations']:
        if debug_mode:
            print(f"\nProcessing {situation['situation']}")

        # Filter 1: Error type / error protection
        step1 = [qecc for qecc in qeccs if situation['errType'] in qecc['error protection']]
        if debug_mode:
            print("After filter 1 (error type):", [q['name'] for q in step1])

        # Filter 2: qType / realization
        step2 = [qecc for qecc in step1 if situation['qType'] in qecc['realization']]
        if debug_mode:
            print("After filter 2 (qType):", [q['name'] for q in step2])

        # Filter 3: Consider all if qOrig is 1, otherwise only those with scalability as 'yes'
        if situation['qOrig'] == "1":
            step3 = step2
        else:
            step3 = [qecc for qecc in step2 if qecc['scalability'] == 'yes']
        if debug_mode:
            print("After filter 3 (scalability):", [q['name'] for q in step3])

        # Corrected Filter 3a: Adjust the logic for transversal gates based on multiQGate
        if situation['multiQGate'] == 'yes':
            step3a = [qecc for qecc in step3 if qecc['transversal gate'] != 'none']
        else:
            step3a = step3

        if int(situation['qOrig']) > 2:
            step3a = [qecc for qecc in step3a if qecc['name'].lower() != 'steane']

        if debug_mode:
            print("After filter 3a (transversal gate and Steane exclusion):", [q['name'] for q in step3a])

        # Filter 4: Average error below threshold
        step4 = [qecc for qecc in step3a if calculate_average_error(situation['depErr'], situation['gateErr'], situation['readErr']) < float(qecc['error threshold'])]
        if debug_mode:
            print("After filter 4 (average error):", [q['name'] for q in step4])

        filtered_qeccs.extend(step4)  # This is the list after all filtering steps

        # Filter 5, 6, 7: Sort by complexity, transversal, and decoding
        step5_6_7 = sorted(step4, key=lambda q: (int(q['complexity']), int(q['transversal gate'] if q['transversal gate'].isdigit() else 999), -int(q['decoding'])))

        # Filter 8: Calculate max distance
        for qecc in step5_6_7:
            qecc['max_distance'] = calculate_max_distance(qecc['qubit overhead'], int(situation['maxSpare'])/int(situation['qOrig']))
        
       
        print("After sorting and max distance calculation for",situation['situation'],":", [(q['name'], q['max_distance']) for q in step5_6_7])

        filtered_qeccs.extend(step5_6_7)  # This is the list after all filtering and sorting steps

    return filtered_qeccs

# The rest of the main function remains unchanged.

def calculate_max_distance(qubit_overhead, maxQAvail):
    # If qubit overhead is a number, return None (no calculation needed)
    if qubit_overhead.isdigit():
        return None
    # If qubit overhead is a formula, solve for d
    else:
        d = sp.symbols('d')
        formula = qubit_overhead.replace('^', '**')
        try:
            solutions = sp.solve(formula + '- {}'.format(maxQAvail), d)
            if solutions:
                max_d = max([sol.evalf() for sol in solutions if sol.is_real])
                return int(max_d)  # Convert max_d to an integer
        except Exception as e:
            print(f"Error solving {formula}: {e}")
    return None


def main():
    user_input = load_json('user_input/user_input.json')
    qeccs = load_json('QECCs/qecc_with_parameters.json')['QECCs']
    
    # Enrich QECCs with their names for easier identification in prints
    enriched_qeccs = []
    for qecc in qeccs:
        for name, properties in qecc.items():
            enriched_qeccs.append({"name": name, **properties})
    
    filtered_qeccs = filter_qeccs(user_input, enriched_qeccs, debug_mode=False)  # Pass debug_mode=True
    # Further processing can be done with filtered_qeccs if needed

main()
