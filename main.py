#!/usr/bin/env python3.5
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # make this False in production
