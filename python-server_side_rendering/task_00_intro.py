from os.path import exists

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("template must be a string and not {type(template).__name__}")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not isinstance(attendees, list):
        print("attendees must be a list of dictionaries and not {type(attendees).__name__}")
        return
    if len(attendees) < 0:
        print("No data provided, no output files generated.")
        return
    if not attendees:
        print("Attendees cannot be empty")
        return
    
    for elem, attendee in enumerate(attendees, start=1):
        text = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key) or 'N/A'
            text = text.replace(f"{{{key}}}", value)
            
        if not exists(f"output_{elem}.txt"):
            with open(f"output_{elem}.txt", "w", encoding="utf-8") as file:
                file.write(text)
        else:
            print("File already exists")
         