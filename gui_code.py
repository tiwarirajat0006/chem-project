import tkinter as tk
from tkinter import ttk, messagebox
import statistics

class StandardDeviationCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Deviation Calculator")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 14, 'bold'))
        style.configure('Result.TLabel', font=('Arial', 11))
        
        # Title
        title = ttk.Label(root, text="Standard Deviation Calculator", style='Title.TLabel')
        title.pack(pady=15)
        
        # Input frame
        input_frame = ttk.LabelFrame(root, text="Enter Data", padding=10)
        input_frame.pack(padx=20, pady=10, fill='x')
        
        # Instructions
        instructions = ttk.Label(input_frame, 
                                text="Enter numbers separated by commas or spaces:",
                                font=('Arial', 9))
        instructions.pack(anchor='w')
        
        # Text entry
        self.data_entry = tk.Text(input_frame, height=5, width=50, font=('Arial', 10))
        self.data_entry.pack(pady=10)
        
        # Sample data button
        sample_btn = ttk.Button(input_frame, text="Load Sample Data",command=self.load_sample)
        sample_btn.pack()
        
        # Buttons frame
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)
        
        calculate_btn = ttk.Button(btn_frame, text="Calculate", command=self.calculate, width=15)
        calculate_btn.grid(row=0, column=0, padx=5)
        
        clear_btn = ttk.Button(btn_frame, text="Clear", command=self.clear, width=15)
        clear_btn.grid(row=0, column=1, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(root, text="Results", padding=10)
        results_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Results labels
        self.count_label = ttk.Label(results_frame, text="Count: -", style='Result.TLabel')
        self.count_label.pack(anchor='w', pady=3)
        
        self.mean_label = ttk.Label(results_frame, text="Mean: -", style='Result.TLabel')
        self.mean_label.pack(anchor='w', pady=3)
        
        self.variance_label = ttk.Label(results_frame, text="Variance: -", style='Result.TLabel')
        self.variance_label.pack(anchor='w', pady=3)
        
        self.std_pop_label = ttk.Label(results_frame, text="Population Std Dev (σ): -", style='Result.TLabel')
        self.std_pop_label.pack(anchor='w', pady=3)
        
        self.std_sample_label = ttk.Label(results_frame, text="Sample Std Dev (s): -", style='Result.TLabel')
        self.std_sample_label.pack(anchor='w', pady=3)
        
    def load_sample(self):
        sample_data = "12, 15, 18, 20, 22, 25, 28, 30"
        self.data_entry.delete('1.0', tk.END)
        self.data_entry.insert('1.0', sample_data)
        
    def calculate(self):
        try:
            # Get text and parse numbers
            text = self.data_entry.get('1.0', tk.END).strip()
            
            if not text:
                messagebox.showwarning("Warning", "Please enter some numbers!")
                return
            
            # Replace commas with spaces and split
            text = text.replace(',', ' ')
            numbers = [float(x) for x in text.split() if x]
            
            if len(numbers) < 2:
                messagebox.showwarning("Warning", "Please enter at least 2 numbers!")
                return
            
            # Calculate statistics
            count = len(numbers)
            mean = statistics.mean(numbers)
            variance = statistics.variance(numbers)
            std_sample = statistics.stdev(numbers)
            std_pop = statistics.pstdev(numbers)
            
            # Update labels
            self.count_label.config(text=f"Count: {count}")
            self.mean_label.config(text=f"Mean: {mean:.4f}")
            self.variance_label.config(text=f"Variance: {variance:.4f}")
            self.std_pop_label.config(text=f"Population Std Dev (σ): {std_pop:.4f}")
            self.std_sample_label.config(text=f"Sample Std Dev (s): {std_sample:.4f}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid numbers only.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def clear(self):
        self.data_entry.delete('1.0', tk.END)
        self.count_label.config(text="Count: -")
        self.mean_label.config(text="Mean: -")
        self.variance_label.config(text="Variance: -")
        self.std_pop_label.config(text="Population Std Dev (σ): -")
        self.std_sample_label.config(text="Sample Std Dev (s): -")

if __name__ == "__main__":
    root = tk.Tk()
    app = StandardDeviationCalculator(root)
    root.mainloop()
