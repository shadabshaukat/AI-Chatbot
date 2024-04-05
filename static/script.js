function formatMessage(message) {
    // Simple heuristic to detect code blocks
    if (message.startsWith('```') && message.endsWith('```')) {
        return `<pre>${message.slice(3, -3)}</pre>`;
    }
    return message;
}

async function sendMessage() {
    const inputElement = document.getElementById('input');
    const message = inputElement.value;
    inputElement.value = ''; // Clear the input field

    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    });

    if (!response.ok) {
        alert('Error from server: ' + await response.text());
        return;
    }

    const data = await response.json();
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
    messagesDiv.innerHTML += `<div><strong>Bot:</strong> ${formatMessage(data.response)}</div>`;
}

function formatMessage(message) {
    return message;  // Keep this simple for now, consider syntax highlighting for future improvements
}

function clearChat() {
    document.getElementById('messages').innerHTML = '';
}

async function sendMessage() {
    const inputElement = document.getElementById('input');
    const message = inputElement.value;
    inputElement.value = ''; // Clear the input field

    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    });

    if (!response.ok) {
        alert('Error from server: ' + await response.text());
        return;
    }

    const data = await response.json();
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
    messagesDiv.innerHTML += `<div><strong>Bot:</strong> ${formatMessage(data.response)}</div>`;
}

