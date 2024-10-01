from Patient import Patient


db = []


def load_heartrate_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data


def parse_patient_data(data):
    pt_info = []
    for line in data:
        pt_info.append(line.strip())
        if line.strip() == 'END':
            add_pt_to_db(pt_info)
            pt_info = []


def add_pt_to_db(patient_info):
    name, type, heartrates = patient_info[0], patient_info[1], patient_info[2]
    heartrates = [float(x) for x in heartrates.split(',')]
    heartrates = convert_heartrates(heartrates, type)
    patient = Patient(name)
    patient.add_heartrate_data(heartrates)
    db.append(patient)


def convert_heartrates(heartrates, type):
    if type == 'BPS':
        conv_heartrates = [x * 60 for x in heartrates]
    elif type == 'BPM':
        conv_heartrates = heartrates
    else:
        raise ValueError("Invalid type")
    return conv_heartrates


def calculate_heartrate_stats():
    n_above_threshold = []
    for pt in db:
        n_above_curr, msg = pt.heartrates_above_threshold()
        n_above_threshold.append(n_above_curr)
    return n_above_threshold


def display_results(above_threshold_data):
    print("Number of heartrates above threshold for each patient:")
    for i, pt in enumerate(db):
        print(f"{pt.name}: {above_threshold_data[i]}")


def main():
    data = load_heartrate_data('heartrate_data.txt')
    parse_patient_data(data)
    above_threshold_data = calculate_heartrate_stats()
    display_results(above_threshold_data)

if __name__ == "__main__":
    main()
