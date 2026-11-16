""" Module to manage user configuration settings. """
test_settings = {
    "Theme": "dark",
    "Notifications": "enabled",
    "Volume": "high"
}
#To add setting:
def add_setting(settings, key,value):
    key, value = key.lower(), value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value    
    return f"Setting '{key}' added with value '{value}'. successfully!"

#To update setting:
def update_setting(settings, key, value):
    key, value = key.lower(), value.lower()
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    settings[key] = value
    return f"Setting '{key}' updated to value '{value}'. successfully!"

#To delete setting:
def delete_setting(settings, key):
    key = key.lower()
    if key not in settings:
        return "Setting not found!"
    del settings[key]
    return f"Setting '{key}' deleted successfully!"

#To view setting:
def view_setting(settings):
    if not settings:
        return "No settings available."
    lines = [f"{key.capitalize()}: {value}" for key, value in settings.items()]
    return "Current User Settings:\n" + "\n".join(lines)


print(add_setting({'theme': 'light'}, 'THEME', 'dark'))
print(add_setting({'theme': 'light'}, 'volume', 'high'))
print(update_setting({'theme': 'light'}, 'theme', 'dark'))
print(update_setting({'theme': 'light'}, 'volume', 'high'))
print(delete_setting({'theme': 'light'}, 'theme')) 
print(view_setting(test_settings))    