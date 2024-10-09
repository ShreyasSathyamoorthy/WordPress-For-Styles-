def script(html_content):
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Replicated Page</title>
    <style>
        p.example-class {
            color: red;
            font-size: 50px;
        }
    
        .highlight {
            background-color: rgba(255, 255, 0, 0.5);
        }
        #modal {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            z-index: 1000;
            display: none; /* Initially hidden */
        }
        #modalContent {
            text-align: center;
        }
        #modal:before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: -1; /* Behind the modal */
            display: none; /* This won't be used, as we manage visibility with JS */
        }
    </style>
    <script>
        let tagName = "";
        let textContent = "";
        let className = "";
        let htmlTag = ""; // Define htmlTag to store the outer HTML

        document.addEventListener('mouseover', function(event) {
            const target = event.target;
            target.classList.add('highlight');
        });

        document.addEventListener('mouseout', function(event) {
            const target = event.target;
            target.classList.remove('highlight');
        });

        document.addEventListener('contextmenu', function(event) {
            event.preventDefault();
            const element = event.target;

            // Store the HTML tag in the global variable
            htmlTag = element.outerHTML; 
            className = element.className; // Capture the class name
            textContent = element.textContent; // Capture the text content
            tagName = element.tagName; // Capture the tag name
            
            const modal = document.querySelector('#modal');
            if (modal) {
                modal.style.display = 'block'; // Show the modal
            }

            // Send the information to the server
            fetch('/right-click', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ tag: htmlTag, class: className, text: textContent })
            })
            .then(response => {
                if (!response.ok) {
                    console.error('Network response was not ok');
                }
            })
            .catch(error => console.error('There was a problem with the fetch operation:', error));
        });

        function closeModal() {
            const modal = document.querySelector('#modal');
            if (modal) {
                modal.style.display = 'none'; // Hide the modal
            }
        }

        function submitInputs() {
            const username = document.querySelector('input[name="username"]').value;
            console.log('Username submitted:', username);
            
            // Send the username and the HTML tag to the backend
            fetch('/submit-username', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username: username, tag: tagName, class: className, text: textContent }) // Send username and captured data
            })
            .then(response => {
                if (!response.ok) {
                    console.error('Network response was not ok');
                } else {
                    console.log('Username and HTML tag successfully submitted');
                    closeModal(); // Close the modal after successful submission
                    location.reload(); // Reload the page after submission
                }
            })
            .catch(error => console.error('There was a problem with the fetch operation:', error));
        }
    </script>
</head>
<body>
    <div id="modal">
        <div id="modalContent">
            <h2>Right Click Detected!</h2>
            <div id="input-container">
                <input type="text" name="username" placeholder="Enter your username">
            </div>
            <button onclick="submitInputs()">Submit</button>
            <button onclick="closeModal()">Close</button>
        </div>
    </div>
    ''' + str(html_content)+'''
</body>
</html>
'''
