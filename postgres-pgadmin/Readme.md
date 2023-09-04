## Usage

1. Clone this repository to your local machine or create a new directory for your project.

2. Create the following directories in the same location as your `docker-compose.yml` file:

    - `pg_local_storage` for PostgreSQL data persistence.
    - `pgadmin_local_storage` for pgAdmin data persistence.

3. Modify the `docker-compose.yml` file if necessary to customize the PostgreSQL and pgAdmin configuration.

4. Start the containers using Docker Compose:


- The `-d` flag runs the containers in the background.

5. Access the following services in your web browser:

- **PostgreSQL**: [http://localhost:5432](http://localhost:5432)
    - **Username**: `dev_user`
    - **Password**: `dev-password`

- **pgAdmin**: [http://localhost:8888](http://localhost:8888)
    - **Email**: `dev-user@dummy.com`
    - **Password**: `dev-password`
