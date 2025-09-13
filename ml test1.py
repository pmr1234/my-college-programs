import pandas as pd

# Function to read CSV and calculate statistics
def calculate_statistics(file_path):
    # Load data from CSV
    df = pd.read_csv(file_path)
    print(df)
    # Calculate statistics
    mode_emp_id = df['Emp ID'].mode()[0]
    mean_salary = df['Emp Salary'].mean()
    median_salary = df['Emp Salary'].median()
    mode_salary = df['Emp Salary'].mode()[0]
    variance_salary = df['Emp Salary'].var()
    std_deviation_salary = df['Emp Salary'].std()
    
    
    # Display results
    print(f"Mean Salary: {mean_salary}")
    print(f"Median Salary: {median_salary}")
    print(f"Mode Salary: {mode_salary}")
    print(f"Variance of Salary: {variance_salary}")
    print(f"Standard Deviation of Salary: {std_deviation_salary}")
    print(f"Mode Emp ID: {mode_emp_id}")
    # Save statistics to a new CSV
    stats = {
        "Mean Salary": [mean_salary],
        "Median Salary": [median_salary],
        "Mode Salary": [mode_salary],
        "Variance": [variance_salary],
        "Standard Deviation": [std_deviation_salary],
        "Mode Emp ID": [mode_emp_id]
    }
    pd.DataFrame(stats).to_csv('salary_statistics.csv', index=False)

# Main execution
if __name__ == "__main__":
    calculate_statistics('employee_data.csv')
