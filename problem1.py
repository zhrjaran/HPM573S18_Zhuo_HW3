class Patient:
    """ base class """

    def __init__(self, name):
        self.name = name
        """
        :param name: name of this node
        :param discharge: discharge of this node
        """

    def discharge(self):
        """ abstract method to be overridden in derived classes"""
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.charge = 1000

    def discharge(self):

        print(self.name, type(self))


class HospitalizedPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.charge = 2000

    def discharge(self):

        print(self.name, type(self))


class Hospital:

    def __init__(self):
        self.patients = []
        self.cost=0

    def admit(self, patient):
        num_patient=len(patient)
        for i in range(num_patient):
            self.patients.append(patient[i])

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.charge

    def get_total_cost(self):
        return self.cost


Patient1 = EmergencyPatient("John")
Patient2 = HospitalizedPatient("Sam")
Patient3 = HospitalizedPatient("Alice")
Patient4 = EmergencyPatient("Catherine")
Patient5 = EmergencyPatient("Becky")

print(Patient1.discharge())

myHospital = Hospital()
myHospital.admit([Patient1, Patient2, Patient3, Patient4, Patient5])
myHospital.discharge_all()
myHospital.get_total_cost()
print(myHospital.get_total_cost())


