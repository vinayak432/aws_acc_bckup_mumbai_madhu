import json

# Step 1: Read the JSON file
with open("spring-core.json", "r") as file:
    data = json.load(file)

# Step 2: Access top-level package
spring_core = data["org.springframework:spring-core"]

# Step 3: Loop through each version
for version_key, details in spring_core.items():

    print("\n==============================")
    print("Version Key:", version_key)
    print("==============================")

    # Step 4: Access individual elements
    print("Version:", details["Version"])
    print("Unique Package Name:", details["UniquePackageName"])
    print("Master Package Name:", details["MasterPackageName"])
    print("Programming Language:", details["ProgrammingLanguage"])
    print("License:", details["License"])
    print("Build Command:", details["BuildCmd"])
    print("Target Package Name:", details["TargetPackageName"])
    print("Source Type:", details["SourceType"])
    print("Force Build:", details["ForceBuild"])
    print("Dependency Build:", details["DependencyBuild"])
    print("Fetch Online:", details["FetchOnline"])
    print("Unit Test Command:", details["UnitTestCommand"])
    print("Build Directory:", details["BuildDirectory"])
    print("Use Patch:", details["UsePatch"])

    # Step 5: Access list (Dependencies)
    print("Dependencies:")
    for dep in details["Dependencies"]:
        print(" -", dep)

    # Step 6: Access nested object (Environment)
    environment = details["Environment"]
    print("Environment:")
    print(" Maven:", environment["maven"])
    print(" Java:", environment["java"])
    print(" Gradle:", environment["gradle"])
    print(" SBT:", environment["sbt"])
    print(" Ant:", environment["ant"])

    # Step 7: Access URL
    print("POM URL:", details["PomUrl"])

