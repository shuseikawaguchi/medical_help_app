from Clinic import Clinic
from Patient import Patient


def main():
    myclinic = Clinic()

    patients = [
        ["佐藤", 111, "咳"],
        ["田中", 222, "腹痛"],
        ["鈴木", 333, "鼻水"],
        ["山田", 444, "倦怠感"],
        ["中田", 555, "インフル"],
    ]

    for p in patients:
        name, pid, symptom = p
        patient = Patient(name, pid, symptom)
        myclinic.reserve(patient)

    myclinic.show_waiting_count()

    me = Patient("中田", 555, "インフル")
    myclinic.reserve(me)
    myclinic.show_waiting_count()

    myclinic.diagnosis()
    myclinic.show_waiting_count()

    myclinic.diagnosis(patient_id=555)
    myclinic.show_waiting_count()


if __name__ == "__main__":
    main()