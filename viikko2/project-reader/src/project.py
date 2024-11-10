class Project:
    def __init__(self, name, description, license_info, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license_info = license_info
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
    
    def _stringify_authors(self, authors):
        return ", ".join(authors) if len(authors) > 0 else "-"

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license_info or '-'}"
            f"\n\nAuthors:{self._stringify_authors(self.authors)}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
