import os
import subprocess
import winreg as reg
from typing import List

class HyperCenter:
    def __init__(self):
        self.startup_reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"

    def list_startup_programs(self) -> List[str]:
        """List all programs that are set to run at startup."""
        programs = []
        try:
            with reg.OpenKey(reg.HKEY_CURRENT_USER, self.startup_reg_key, 0, reg.KEY_READ) as key:
                count_subkeys = reg.QueryInfoKey(key)[1]
                for i in range(count_subkeys):
                    program = reg.EnumValue(key, i)
                    programs.append((program[0], program[1]))
        except WindowsError as e:
            print(f"Failed to list startup programs: {e}")
        return programs

    def disable_startup_program(self, program_name: str) -> bool:
        """Disable a specified startup program."""
        try:
            with reg.OpenKey(reg.HKEY_CURRENT_USER, self.startup_reg_key, 0, reg.KEY_ALL_ACCESS) as key:
                reg.DeleteValue(key, program_name)
            print(f"Disabled startup program: {program_name}")
            return True
        except FileNotFoundError:
            print(f"Program '{program_name}' not found in startup list.")
        except WindowsError as e:
            print(f"Error disabling program '{program_name}': {e}")
        return False

    def enable_startup_program(self, program_name: str, program_path: str) -> bool:
        """Enable a specified program to run at startup."""
        try:
            with reg.OpenKey(reg.HKEY_CURRENT_USER, self.startup_reg_key, 0, reg.KEY_SET_VALUE) as key:
                reg.SetValueEx(key, program_name, 0, reg.REG_SZ, program_path)
            print(f"Enabled startup program: {program_name}")
            return True
        except WindowsError as e:
            print(f"Error enabling program '{program_name}': {e}")
        return False

    def optimize_startup(self):
        """Optimize startup by disabling unnecessary programs."""
        print("Listing current startup programs...")
        programs = self.list_startup_programs()
        if not programs:
            print("No startup programs found.")
            return

        print("Current startup programs:")
        for name, path in programs:
            print(f"  {name}: {path}")

        to_disable = input("Enter the names of programs to disable (comma separated): ").split(',')
        to_disable = [name.strip() for name in to_disable]

        for program_name in to_disable:
            self.disable_startup_program(program_name)

if __name__ == "__main__":
    hyper_center = HyperCenter()
    hyper_center.optimize_startup()