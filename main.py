from website import create_app

app = create_app()

# Don't run on import
if __name__ == '__main__':
    app.run(debug=True)