import subprocess
import tempfile
import os
import sys

class CodeChecker:
    def __init__(self, language):
        self.language = language

    def _create_temp_file(self, suffix, code, dir=None):
        #suffs = {'python': 'py', 'java': 'java', 'c++': 'cpp', 'golang': 'go'}
        """Create a temporary file with the given code and return its name."""
        temp_file = tempfile.NamedTemporaryFile(suffix='.py', delete=False)
        temp_file.write(code.encode())
        temp_file.flush()
        temp_file.close()  # Explicitly close the temporary file
        # print(f"Temporary file created: {temp_file.name}")
        return temp_file.name

    def _run_command(self, command, cwd=None):
        """Run a command in subprocess and return (success, output)."""
        try:
            if cwd:
                print(f"Changing directory to: {cwd}")
                os.chdir(cwd)
            # print(f"Running command: {' '.join(command)} in {cwd or 'current directory'}")
            result = subprocess.run(command, capture_output=True, text=True)
            # print(f"Command output: {result.stdout}\nCommand error: {result.stderr}")
            return result.returncode == 0, result.stdout + result.stderr  # Combine stdout and stderr for full output
        except Exception as e:
            return False, str(e)

    def check_syntax(self, code):
        temp_file_name = self._create_temp_file(self.language, code, dir=os.getcwd())
        success, output = self._run_command([self.language, temp_file_name])
        os.unlink(temp_file_name)  # Now unlink the temporary file by its name
        return success, output

    def check_style_and_formatting(self, code):
        temp_file_name = self._create_temp_file(self.language, code, dir=os.getcwd())
        if self.language == 'python':
            command = ['pylint', '--disable=all', '--enable=C,R,W,E', temp_file_name]
        elif self.language == 'java':
            command = ['java', '-jar', 'checkstyle-8.41-all.jar', '-c', '/google_checks.xml', temp_file_name]
        else:
            raise ValueError(f"Unsupported language: {self.language}")

        success, output = self._run_command(command, cwd=os.path.dirname(temp_file_name))
        os.unlink(temp_file_name)
        return success, output

    def check_semantics(self, code):
        temp_file_name = self._create_temp_file(self.language, code, dir=os.getcwd())
        if self.language == 'python':
            command = ['pytest', temp_file_name]
        elif self.language == 'java':
            command = ['mvn', 'test']
        else:
            raise ValueError(f"Unsupported language: {self.language}")

        success, output = self._run_command(command, cwd=os.path.dirname(temp_file_name))
        os.unlink(temp_file_name)
        return success, output

    def check_coverage(self, code, tests):
        temp_file_name = self._create_temp_file(self.language, code, dir=os.getcwd())
        test_file_name = self._create_temp_file("test_" + self.language, tests, dir=os.getcwd())
        temp_dir = os.path.dirname(temp_file_name)  # Directory where temp files are created

        if self.language == 'python':
            command = ['coverage', 'run', '--source=.', '-m', 'pytest', test_file_name]
            coverage_command = ['coverage', 'report']
        elif self.language == 'java':
            command = ['mvn', 'clean', 'test', 'jacoco:report']
            coverage_command = None  # Implement Java coverage command if necessary
        else:
            raise ValueError(f"Unsupported language: {self.language}")

        success, output = self._run_command(command, cwd=temp_dir)
        if success and coverage_command:
            success, coverage_output = self._run_command(coverage_command, cwd=temp_dir)
            output += coverage_output  # Combine the outputs
        os.unlink(temp_file_name)
        os.unlink(test_file_name)
        return success, output

    def check_best_practices(self, code):
        temp_file_name = self._create_temp_file("." + self.language, code, dir=os.getcwd())
        if self.language == 'python':
            command = ['pylint', '--disable=all', '--enable=C,R,W,E', temp_file_name]
        elif self.language == 'java':
            command = ['pmd', '-d', temp_file_name, '-R', 'rulesets/java/quickstart.xml', '-f', 'text']
        else:
            raise ValueError(f"Unsupported language: {self.language}")

        success, output = self._run_command(command, cwd=os.path.dirname(temp_file_name))
        os.unlink(temp_file_name)
        return success, output

# Пример использования:
f1 = open("programs/code_example.py", "r")
code_snippet = ''.join(f1.readlines())
f1.close()

python_checker = CodeChecker('python')
syntax_ok, syntax_output = python_checker.check_syntax(code_snippet)
if syntax_ok:
    print("Syntax is correct.")
else:
    print("Syntax errors found:", syntax_output)

style_ok, style_output = python_checker.check_style_and_formatting(code_snippet)
if style_ok:
    print("Style is correct.")
else:
    print("Style errors found:", style_output)

semantics_ok, semantics_output = python_checker.check_semantics(code_snippet)
if semantics_ok:
    print("Semantics are correct.")
else:
    print("Semantic errors found:", semantics_output)

# Assume we have test cases
# f2 = open("C:/workspace/Yandex_SHAR/practice/babushka.py", "r")
# tests_snippet = ''.join(f2.readlines())
# f2.close()

# test_cases = code_snippet + '\n' + tests_snippet
# print(test_cases)

# coverage_ok, coverage_output = python_checker.check_coverage(code_snippet, test_cases)
# if coverage_ok:
#     print("Test coverage is adequate.")
# else:
#     print("Test coverage errors found:", coverage_output)

best_practices_ok, best_practices_output = python_checker.check_best_practices(code_snippet)
if best_practices_ok:
    print("Best practices are followed.")
else:
    print("Best practices errors found:", best_practices_output)
