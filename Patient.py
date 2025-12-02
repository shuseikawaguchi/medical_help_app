class Human():
    def __init__(self, name :str):
        self.name = name

class Patient(Human):
    def __init__(self, name :str, patient_id :int, symptom :str):
        super().__init__(name)
        self.patient_id = patient_id
        self.symptom = symptom
        