import pandas as pd
import os

data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'}
]
df = pd.DataFrame(data)

# Define the OneDrive path correctly (fix the error)
onelake_path = r"C:\Users\kuose\OneLake - Microsoft\global-IT-DEV\selena_lakehouse.Lakehouse\Files"  # 替換為實際的 OneLake 上傳端點
target_folder = os.path.join(onelake_path, 'test_folder')  # Use os.path.join to build the full path
csv_filename = os.path.join(target_folder, 'test_data.csv')  # File name with today's date (May 15, 2025)

# Ensure the folder exists
os.makedirs(target_folder, exist_ok=True)

# Save CSV to the OneDrive folder
df.to_csv(csv_filename, index=False, encoding='utf-8')
# Print confirmation message
print(f"CSV saved to {csv_filename}")