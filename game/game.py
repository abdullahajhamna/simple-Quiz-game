
import time
def documentation():
    print("""
this porgram test your knowledge
you may ask, konwledge? abdout what?
and we will tell you it's about The greatest series in history "The Office" 
""")
    
t = 3
def countdown():
    global t
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        t -= 1
    print('OK start the Quiz')  # Add some spaces to overwrite any leftover characters

