import csv

# Kontaktų klasė, skirta laikyti vieno kontakto informaciją
class Contact:
    def __init__(self, name, phone, email):
        # Inicializuojamos kontakto savybės
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        # Grąžina formatuotą kontakto informaciją kaip tekstą
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Kontaktų knygos klasė, skirta tvarkyti kontaktų sąrašą
class ContactBook:
    def __init__(self):
        # Inicializuojamas tuščias kontaktų sąrašas
        self.contacts = []

    # Metodas pridėti kontaktą į sąrašą
    def add_contact(self, contact):
        self.contacts.append(contact)

    # Metodas pašalinti kontaktą pagal vardą
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)

    # Metodas ieškoti kontakto pagal vardą
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    # Metodas parodyti visus kontaktus
    def display_contact(self):
        for contact in self.contacts:
            print(contact)

    # Metodas išsaugoti kontaktus į failą
    def save_to_file(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            # Įrašomas kiekvienas kontaktas kaip atskira eilutė
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.email])
        print(f"Contacts saved to {filename}.")

    # Metodas užkrauti kontaktus iš failo
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                # Kiekviena eilutė įrašoma kaip kontaktas
                self.contacts = [Contact(row[0], row[1], row[2]) for row in reader]
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")

# Pagrindinė funkcija su sąsaja naudotojui
def main():
    # Sukuriamas naujas kontaktų knygos objektas
    contact_book = ContactBook()

    while True:
        # Meniu pasirinkimams
        print("\nKontaktu knygos meniu:")
        print("1. Pridėti kontaktą")
        print("2. Ištrinti kontaktą")
        print("3. Ieškoti kontakto")
        print("4. Rodyti visus kontaktus")
        print("5. Išsaugoti kontaktus į failą")
        print("6. Užkrauti kontaktus iš failo")
        print("7. Baigti programą")

        choice = input("Iveskite pasirinkima: ")

        if choice == "1":
            # Pridėti naują kontaktą
            name = input("Suveskite varda: ")
            phone = input("Suveskite telefono numeri: ")
            email = input("Suveskite elektronini pašta: ")
            contact = Contact(name, phone, email) # Sukuriamas naujas kontaktas
            contact_book.add_contact(contact)
            print("Kontaktas pridėtas.")

        elif choice == "2":
            # Ištrinti kontaktą pagal vardą
            name = input("Iveskite kontakta kuri norite ištrinti: ")
            contact_book.delete_contact(name)
            print("Kontaktas ištrintas.")

        elif choice == "3":
            # Ieškoti kontakto pagal vardą
            name = input("Iveskite kontakta kuri norite rasti: ")
            contact = contact_book.search_contact(name)
            if contact:
                print("Kontaktas rastas:")
                print(contact)
            else:
                print("Kontaktas nerastas.")

        elif choice == "4":
            # Rodyti visus kontaktus
            print("\nVisi kontaktai:")
            contact_book.display_contact()

        elif choice == "5":
            # Išsaugoti kontaktus į failą
            filename = input("Iveskite failo pavadinimą: ")
            contact_book.save_to_file(filename)

        elif choice == "6":
            # Uzkrauti kontaktus iš failo
            filename = input("Iveskite failo pavadinimą: ")
            contact_book.load_from_file(filename)

        elif choice == "7":
            # Išeiti iš programos
            print(" ")
            break

        else:
            # Pranešimas apie neteisingą pasirinkimą
            print("Bandykite iš naujo.")

# Pagrindinis programos paleidimas
if __name__ == "__main__":
    main()