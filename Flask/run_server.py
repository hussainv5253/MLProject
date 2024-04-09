import subprocess

gunicorn_executable = "C:\\Users\\mattd\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\Scripts\\gunicorn.exe"

# Define the command to run Gunicorn
gunicorn_command = [
    gunicorn_executable,
    "-b",
    "127.0.0.1:8000",
    "power_forecasting_app:app"  # Adjust this according to your Flask app module and app instance
]

subprocess.run(gunicorn_command, check=True)
