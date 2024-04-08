import tkinter as tk
from tkinter import messagebox

from main import decrypted_message, encrypted_message


# Define a function to handle encryption and decryption
def handle_encryption():
  message = f"""Location: {location_txt.get()}
      Callsign and Radio Frequency: {callsign_radio_freq_txt.get()}
      Number of Patients: {number_of_patients_txt.get()}
      Special Equipment Needed: {special_equipment_need_txt.get()}
      Number of Patient Type: {number_of_patient_type_txt.get()}
      Security at Pickup Site: {security_pickup_site_txt.get()}
      Site Marking: {site_marking_txt.get()}
      Patient Nationality: {patient_nationality_txt.get()}
      NBC Contamination: {nbc_contamination_txt.get()}"""
  encrypted_msg = encrypted_message(message)
  messagebox.showinfo("Encrypted Message", encrypted_msg.decode())


def handle_decryption(encrypted_msg):
  decrypted_msg = decrypted_message(encrypted_msg)
  messagebox.showinfo("Decrypted Message", decrypted_msg)


# Create the main application window
root = tk.Tk()
root.title("Nine Line Report")

# Create input entry field
location_txt = tk.Entry(root, width=50)
callsign_radio_freq_txt = tk.Entry(root, width=50)
number_of_patients_txt = tk.Entry(root, width=50)
special_equipment_need_txt = tk.Entry(root, width=50)
number_of_patient_type_txt = tk.Entry(root, width=50)
security_pickup_site_txt = tk.Entry(root, width=50)
site_marking_txt = tk.Entry(root, width=50)
patient_nationality_txt = tk.Entry(root, width=50)
nbc_contamination_txt = tk.Entry(root, width=50)

location_txt.pack(pady=10)
callsign_radio_freq_txt.pack(pady=10)
number_of_patients_txt.pack(pady=10)
special_equipment_need_txt.pack(pady=10)
number_of_patient_type_txt.pack(pady=10)
security_pickup_site_txt.pack(pady=10)
site_marking_txt.pack(pady=10)
patient_nationality_txt.pack(pady=10)
nbc_contamination_txt.pack(pady=10)

# Create Encrypt buttons
encrypt_button = tk.Button(root,
                           text="Send Encrypted Message",
                           command=handle_encryption)
encrypt_button.pack(pady=5)

# Start the GUI main loop
root.mainloop()
