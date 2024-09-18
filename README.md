<h1>MySQL Database Connection in VS Code</h1>
<br>
This guide explains how to set up and connect a MySQL database to VS Code for local development. With this setup, you can manage databases, run queries, and view results seamlessly within the VS Code environment.
<br>
<br>
<strong>Prerequisites:</strong>
<br>
Before starting, ensure the following tools are installed:
<br>
<ul>
  <li>Visual Studio Code (VS Code)</li>
  <li>MySQL Server</li>
  <li>MySQL Extension for VS Code</li>
  <li>MySQL credentials (username, password, and port)</li>
</ul>
<h1>Setup Instructions:</h1>
<h2>Step 1: Install MySQL Extension in VS Code:</h2>
<br>
<p>
  1) SQLTools  
  <br>
  2)SQLTools MySQL/MariaDB
    <br>
  <strong>(Both by Matheus Teixeira)</strong>
    <br>
</p>
 <h2>Step 2: Create a New MySQL User and Grant Privileges</h2>
    <p>Once you are logged in to your MySQL server as the root user or an admin with appropriate privileges, it is recommended to create a new user for your application or development work.
      This ensures security and limits access to specific databases and operations. Here's how you can do it:</p>
    <ol>
        <li>Login to your MySQL server using the following command:
            <pre><code>mysql -u root -p</code></pre>
        </li>
        <li>Once logged in, create a new user by running the following SQL query. Replace <code>username</code> and <code>password</code> with your desired values:
                    <pre><code>CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';</code></pre>
         </li>
        <li>Next, grant all necessary privileges to the new user on a specific database (e.g., `my_database`). This gives the user permission to perform certain actions within that database:
            <pre><code>GRANT ALL PRIVILEGES ON my_database.* TO 'username'@'localhost';</code></pre>
        </li>
        <li>Apply the changes by running:
            <pre><code>FLUSH PRIVILEGES;</code></pre>
        </li>
        <li>Verify the user has been created and has access to the database by logging in as the new user:
            <pre><code>mysql -u username -p</code></pre>
        </li>
    </ol>
    <h2>Why Create a New User and Grant Specific Privileges?</h2>
    <p>Creating a new MySQL user instead of using the root user for application or development purposes enhances security. By limiting the user's privileges to only the necessary databases and actions (such as SELECT, INSERT, UPDATE, etc.), you reduce the risk of accidental or malicious changes to critical system databases. Additionally, it is a good practice to use a dedicated user for each application to maintain better control and auditing of database activities.</p>
       <h2>Step 3: Pull the Repository and Update MySQL Credentials in <code>app.py</code></h2>
    <p>Now that your MySQL database is set up and your user has the appropriate privileges, the final step is to pull the project repository and configure the database connection in the application.</p>
    <ol>
        <li>Open your terminal and navigate to the directory where you want to clone the repository.</li>
        <li>Use the following command to pull the repository:
            <pre><code>git clone https://github.com/your-repository-link.git</code></pre>
        </li>
        <li>Once cloned, open the repository in your preferred code editor (such as VS Code).</li>
        <li>Locate the <code>app.py</code> file, which contains the database connection logic. You will find lines where MySQL credentials are set (typically in a connection string or function).</li>
        <li>Replace the placeholder credentials with your actual MySQL credentials, which you set up in the previous steps:
            <pre><code>
DATABASE_CONFIG = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'my_database',
}
            </code></pre>
        </li>
        <li>Save the changes, and you're ready to go! You can now run the application, and it will connect to your MySQL database using your credentials.</li>
    </ol>
<br>
<br>
  <h1 style="fontsize:30px;">THANK YOU</h1>




