import tkinter as tk
from tkinter import messagebox

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Survey App")
        
        # Create A GUi Elements
        self.name_label = tk.Label(root, text="Name: ")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.age_label = tk.Label(root, text="Age: ")
        self.age_label.pack()
        
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()
        
        self.satisfaction_label = tk.Label(root, text="How Satisfied Are You With Our Service? ")
        self.satisfaction_label.pack()
        
        self.satisfaction_var = tk.StringVar(root)
        self.satisfaction_var.set("Very Satisfied")
        
        self.satisfaction_option = tk.OptionMenu(root, self.satisfaction_var, "Very Satisfied", "Satisfied", "Neutral", "Unsatisfied", "Very Unsatisfied")
        self.satisfaction_option.pack()
        
        self.submit_button = tk.Button(root, text="Submit", command = self.submit_survey)
        self.submit_button.pack()
        
        self.survey_result = []
        
    def submit_survey(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        satisfaction = self.satisfaction_var.get()
            
        if name and age:
            try:
                age = int(age)
                self.survey_result.append({
                    "Name": name,
                    "Age": age,
                    "Satisfaction": satisfaction
                    })

                messagebox.showinfo("Survey App", "Thank you for submitting the survey")
                    
                self.name_entry.delete(0, tk.END)
                self.age_entry.delete(0, tk.END)
                self.satisfaction_var.set("Very Satisfied")
                    
            except ValueError:
                messagebox.showerror("Survey App", "Invalid Age, Please Enter A Number.")
        else:
            messagebox.showerror("Survey App", "Please Fill Out The Fields.")
        
        
        print(self.survey_result)
        
if __name__=="__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.geometry("300x400")
    root.mainloop()