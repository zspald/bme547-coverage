import pytest
from heartrate_analysis import db


def test_add_pt_to_db():
    from heartrate_analysis import add_pt_to_db
    data = ['Zac', 'BPM', '100,110,120,130,140']
    add_pt_to_db(data)
    assert len(db) == 1
    assert db[0].name == 'Zac'
    assert db[0].heartrates == [[100, 110, 120, 130, 140]]
    db.clear()


def test_parse_patient_data():
    from heartrate_analysis import parse_patient_data
    data = ['Zac\n', 'BPM\n', '100,110,120,130,140\n', 'END\n', 'Zac2\n',
            'BPS\n', '1.67,2.33,1.83,2.17,2.0\n', 'END\n']
    parse_patient_data(data)
    assert len(db) == 2
    assert db[0].name == 'Zac'
    assert db[1].name == 'Zac2'
    assert db[0].heartrates == [[100, 110, 120, 130, 140]]
    assert db[1].heartrates[0] == pytest.approx([100.2, 139.8, 109.8, 130.2,
                                                 120.0])
    db.clear()


def test_calculate_heartrate_stats():
    from heartrate_analysis import calculate_heartrate_stats
    from Patient import Patient
    db.append(Patient('Zac'))
    db[0].add_heartrate_data([100, 110, 120, 130, 140] + [0]*45)
    db.append(Patient('Zac2'))
    db[1].add_heartrate_data([150, 140, 121, 130, 119] + [0]*45)
    n_above_threshold = calculate_heartrate_stats()
    assert n_above_threshold == [2, 4]
    db.clear()
