const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);

scrollToBottom();
const chatSocket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/'
  + roomName
  + '/'
);

chatSocket.onopen = function(e) {
  console.log('WebSocket connection opened');
}

chatSocket.onclose = function(e) {
  console.log('WebSocket connection closed');
}

chatSocket.onerror = function(error) {
  console.error('WebSocket Error:', error);
}
chatSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);

  if (data.message) {
    // Append the new message directly to the chat container

    appendNewMessage(data.username, data.message,data.profile_pic, data.timestamp );
  } else {
    alert('The message was empty!');
  }

  scrollToBottom();
};

$('#chat-message-input').focus();
$('#chat-message-input').on('keyup', function(e) {
  if (e.keyCode === 13) {
    e.preventDefault();
    $('#chat-message-submit').click();
  }
});

$('#chat-message-submit').on('click', function(e) {
  e.preventDefault();

  const messageInputDom = $('#chat-message-input');
  const message = messageInputDom.val();

  console.log({
    'message': message,
    'username': userName,
    'room': roomName
  });

  chatSocket.send(JSON.stringify({
    'message': message,
    'username': userName,
    'room': roomName,
  }));

  $('#chat-message-input').focus();
  messageInputDom.val('');
  return false;
});

function scrollToBottom() {
  let objDiv = document.getElementById('chat-messages');
  objDiv.scrollTop = objDiv.scrollHeight;
}

function appendNewMessage(username, message,profile_pic,timestamp) {
  // Create the HTML for a new chat message
  const messageHTML = `
    <div id="chat-message" class="chat-message" data-username="${username}">
      <div class="profile-image">
        <img src="${profile_pic}" alt="" class="profile-image" />
      </div>
      <div class="message-content">
        <div class="message-header">
          <span class="username"><b>${username}</b></span>
          <span class="timestamp">${timestamp}</span>
        </div>
        <div class="message-body">
          ${message}
        </div>
      </div>
    </div>
  `;

  // Append the new message to the chat container
  $("#chat-messages").append(messageHTML);
}

