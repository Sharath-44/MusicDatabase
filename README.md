# Melody Vault - Music Database

Melody Vault is a music database project built using MySQL, Flask, and HTML. It allows users to create playlists, add songs to them, and offers features like public and private playlists, user settings, and search functionality.

## Features

- **User Authentication:**
  - Users can register, log in, and log out.
  - Passwords are securely hashed and stored.

- **Playlist Management:**
  - Create and manage playlists.
  - Add songs to playlists.
  - Public and private playlist options available.

- **User Settings:**
  - Change username.
  - Modify playlist names.

- **Search Functionality:**
  - Search for songs and playlists.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/sharath-44/melody-vault.git
    ```

2. **Database Setup:**
    - Run the database migrations:
    ```bash
    python sqlsetup.py
    ```

4. **Run the Application:**
    ```bash
    python app.py
    ```

## Usage

1. **Register/Login:**
    - Access the application through the browser and register/login with your credentials.

2. **Create a Playlist:**
    - Once logged in, navigate to the "Create Playlist" section to create a new playlist.

3. **Add Songs:**
    - After creating a playlist, add songs to it from the available database.

4. **Public/Private Playlists:**
    - Choose between public and private visibility for your playlists.

5. **User Settings:**
    - Change your username or modify playlist names in the "Settings" section.

6. **Search:**
    - Utilize the search functionality to find specific songs or playlists.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or create a pull request.

