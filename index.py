import os

# Define your personal info
name = "Your Name"
description = "Your Description"
links = [
    {"name": "GitHub", "url": "https://github.com/your-username"},
    {"name": "Twitter", "url": "https://twitter.com/your-twitter-handle"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/your-linkedin-profile"},
]

# Define the Neon Live theme
theme = """
<!DOCTYPE html>
<html>
<head>
    <title>{name}</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/neon/2.2.0/neon.min.css">
    <style>
        body {{
            background-color: #212121;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
        }}
        .container {{
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #333333;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .links {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .links li {{
            margin-bottom: 10px;
        }}
        .links a {{
            color: #66CCCC;
            text-decoration: none;
        }}
        .links a:hover {{
            color: #CCCCCC;
        }}
    </style>
</head>
<body>
    <div class="
