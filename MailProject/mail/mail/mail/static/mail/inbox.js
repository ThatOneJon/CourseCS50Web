document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
    load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.addEventListener("submit", () => {
  fetch('/emails',{
    method: 'POST',
    body: JSON.stringify({
      recipients : "jon@doe.com",
      subject : document.getElementById("compose-subject").value,
      body : document.getElementById("compose-body").value
    })
  })
  .then(response => response.json())
  .then(result => {
    // Print result
    console.log(result);
}) });
}



function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  fetch('/emails/inbox')
  .then(response => response.json())
  .then(emails =>{

    console.log(emails);

    emails.forEach( obj=> {
    const u = document.getElementById("emails-view");
    let i = document.createElement("li");
    i.innerHTML = `ID: ${obj.id} - Sender: ${obj.sender} - Subject: ${obj.subject} - FROM: ${obj.timestamp}`;
    u.appendChild(i);
    })
  });



  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


  
}