class Clinic:
    def __init__(self):
        self.patients_list = []

    def show_waiting_count(self):
        print(f"現在の待ち人数: {len(self.patients_list)}人")
        
    def reserve(self, patient :Patient):
        if self._check_reserved(patient):
            print(f"{patient.name}さんはすでに予約済みです")
        else:
            self.patients_list.append(patient)
            print(f"{patient.name}さんの予約を受け付けました")
            
    def diagnosis(self, patient_id = None):
        patient = None
        if patient_id is None:
            if len(self.patients_list) > 0:
                patient = self.patients_list[0]
                
        else:
            for p in self.patients_list:
                if p.patient_id == patient_id:
                    patient = p
                    
        if patient is None:
            print("診察する患者がいません")
        else:
            print(f"{patient.name}さん、{patient.symptom}ですね。")
            
            print(f"診察終わりました。お大事に。")
            
            self.patients_list.remove(patient)
            
    def _check_reserved(self, patient :Patient):
        for p in self.patients_list:
            if p.patient_id == patient.patient_id:
                return True
        return False