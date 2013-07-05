var chatRoom= new Firebase('http://dcode.firebaseio.com/chat_room');
document.addEventListener('DOMContentLoaded', function(){
var messageList = document.getElementById('chat-message-list');
var form = document.getElementById('chat-form');
var messageInput = document.getElementById('message-input');
        chatRoom.on('child_added', function(snapshot){
                var li = document.createElement('li');
                li.textContent = snapshot.val().message;
                messageList.appendChild(li);
                messageList.scrollTop = messageList.scrollHeight;
                });

                        form.addEventListener('submit', function(event)){
                        event.preventDefault();
                        chatRoom.push({message:messageInput.value});

                        messageInput.value = '';
                        });

});