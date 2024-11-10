from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self): 
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content) #toml
    
    # get the name, description and dependencies
        project_name = data.get("tool", {}).get("poetry", {}).get("name", "Unknown name")
        description = data.get("tool", {}).get("poetry", {}).get("description", "No description")
        license_info = data.get("tool", {}).get("poetry", {}).get("license", "No license")
        authors = data.get("tool", {}).get("poetry", {}).get("authors", [])
        dependencies = list(data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())
        
        print("Authors:", authors)
        return Project(project_name, description, license_info, authors, dependencies, dev_dependencies)