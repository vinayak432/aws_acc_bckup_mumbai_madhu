import json

# Read the JSON file
with open("org.springframework_spring-core.json", "r") as file:
    data = json.load(file)

# Access top-level key
spring_core = data["org.springframework:spring-core"]

# Access a specific version
version_5326 = spring_core["5.3.26"]

# Access individual elements
print("Version:", version_5326["Version"])
print("Unique Package Name:", version_5326["UniquePackageName"])
print("Programming Language:", version_5326["ProgrammingLanguage"])
print("License:", version_5326["License"])
print("Build Command:", version_5326["BuildCmd"])

# Access list (Dependencies)
print("Dependencies:")
for dep in version_5326["Dependencies"]:
    print("-", dep)

# Access nested object (Environment)
environment = version_5326["Environment"]
print("Environment Details:")
print("Java Version:", environment["java"])
print("Maven:", environment["maven"])
print("Gradle:", environment["gradle"])

