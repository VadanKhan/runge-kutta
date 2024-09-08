## Scripts

1. **q_switch_laser.py**: Solves a system of two differential equations related to Q-switched laser pulses.
2. **rk4_example.py**: Solves a single differential equation as an example.

## Requirements

- Python 3.7+
- NumPy
- Matplotlib
- Poetry (for dependency management and virtual environment setup)

## Setup Instructions

1. **Clone the repository:**

    ```
   git clone <repository_url>
   cd <repository_directory>
    ```

2. **Install Poetry:** Follow the instructions on the Poetry website to install Poetry.

3. **Configure Poetry to create virtual environments in the project directory:**
    ```
   poetry config virtualenvs.in-project true
    ```

4. **Install dependencies and create a virtual environment:**
    ```
   poetry install
    ```
   This will install the required dependencies and create a virtual environment within the repository.

5. **Activate the virtual environment:**
    ```
   poetry shell
    ```
## Running the Scripts

1. **Run the main script:**
    ```
   python q_switch_laser.py
    ```
   This script solves the system of differential equations and plots the results.

2. **Run the example script:**
    ```
   python rk4_example.py
    ```
   This script solves a single differential equation and plots the results.

## Notes

- Ensure that you have activated the virtual environment before running the scripts.
- Modify the initial conditions and parameters in the scripts as needed to explore different scenarios.
