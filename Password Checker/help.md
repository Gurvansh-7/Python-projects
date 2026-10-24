Password Checker

A Python-based password strength checker implemented in three different ways to demonstrate different input handling techniques and libraries.

Files =>

1. password_checker_basic.py
Simple password checker using Python's built-in input() function.
Easy to understand and beginner-friendly.
Recommended for learning the core password validation logic.

2. password_checker_msvcrt.py
Password checker using the msvcrt module.
Hides typed characters while entering passwords.
Works only on Windows.
Created for learning low-level keyboard input handling.
Not portable to Linux or macOS.

3. password_checker_prompt_toolkit.py
Password checker using the prompt_toolkit library.
Provides a modern terminal input experience.
Supports password masking and advanced terminal features.
Works across multiple platforms.
Recommended for real-world terminal applications.

Features =>

Minimum length validation
Uppercase letter check
Lowercase letter check
Number check
Special character check
Password strength feedback