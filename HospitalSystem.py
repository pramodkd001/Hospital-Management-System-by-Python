class Patient:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.bill_amount = 0

    def update_bill(self, amount):
        self.bill_amount += amount

    def display_info(self):
        print("Name:", self.name)
        print("Contact:", self.contact)
        print("Bill Amount:", self.bill_amount)


class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, name, contact):
        patient = Patient(name, contact)
        self.patients[name] = patient
        print("Patient", name, "added successfully.")

    def update_bill(self, name, amount):
        if name in self.patients:
            self.patients[name].update_bill(amount)
            print("Bill for patient", name, "updated successfully.")
        else:
            print("Patient", name, "not found.")

    def display_patient_info(self, name):
        if name in self.patients:
            self.patients[name].display_info()
        else:
            print("Patient", name, "not found.")


def main():
    hospital = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Update Bill")
        print("3. Display Patient Info")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient's name: ")
            contact = input("Enter patient's contact information: ")
            hospital.add_patient(name, contact)
        elif choice == '2':
            name = input("Enter patient's name: ")
            amount = float(input("Enter bill amount to update: "))
            hospital.update_bill(name, amount)
        elif choice == '3':
            name = input("Enter patient's name: ")
            hospital.display_patient_info(name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
