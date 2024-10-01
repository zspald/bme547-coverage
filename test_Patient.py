from Patient import Patient


def test_Patient_init():
    name = 'Zac'
    p = Patient('Zac')
    assert p.name == 'Zac'
    assert p.heartrates == []
    assert p.threshold == 120


def test_Patient_add_heartrate_data():
    p = Patient('Zac')
    heartrates = [100, 110, 120, 130, 140]
    p.add_heartrate_data(heartrates)
    assert p.heartrates == [heartrates]


def test_Patient_heartrates_above_threshold():
    p = Patient('Zac')
    heartrates = [100, 110, 120, 130, 140] + [0]*45
    p.add_heartrate_data(heartrates)
    n, msg = p.heartrates_above_threshold()
    assert n == 2
    assert msg == "Success"
