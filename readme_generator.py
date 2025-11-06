#!/usr/bin/env python3
"""
README Generator
A tool to generate a basic README.md template for your project.
Usage: python readme_generator.py <project_name>
"""

import sys
import os

def generate_readme(project_name):
    """Generate a basic README content."""
    readme_content = f"""# {project_name}

A brief description of what {project_name} does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
# Installation instructions
```

## Usage

```python
# Example usage
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""
    return readme_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python readme_generator.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    readme_content = generate_readme(project_name)

    filename = "README.md"
    if os.path.exists(filename):
        overwrite = input(f"{filename} already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("Aborted.")
            return

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"Generated {filename} for project '{project_name}'")

if __name__ == "__main__":
    main()