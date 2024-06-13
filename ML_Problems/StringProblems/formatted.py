import textwrap

def display_formatted_text(text, width=50):
  
    wrapped_text = textwrap.fill(text, width=width)
    
  
    print(wrapped_text)


text = """
Python is a widely used high-level programming language for
general-purpose programming, created by Guido van Rossum 

"""


display_formatted_text(text)
