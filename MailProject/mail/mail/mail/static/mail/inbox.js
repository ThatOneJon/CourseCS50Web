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
  document.querySelector('#one-mail').style.display = 'none';


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
  document.querySelector('#one-mail').style.display = 'none';
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails =>{

    console.log(emails);

    emails.forEach( obj=> {
    const u = document.getElementById("emails-view");
    let i = document.createElement("div");
    i.innerHTML = `<button class="mail" onclick=viewMail(${obj.id})>ID: ${obj.id} - Sender: ${obj.sender} - Subject: ${obj.subject} - FROM: ${obj.timestamp}</a>`;
    i.style.border = "solid black 2px";
    i.style.marginTop = "10px";

      if(obj.read === true){
        i.style.backgroundColor = "lightgrey";
      }else{
        i.style.backgroundColor = "white";

      }
    u.appendChild(i);

    })
  });

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
}


function viewMail(i){
      fetch(`emails/${i}`)
      .then(response =>response.json())
      .then(data => {
        console.log(data);
   

    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#one-mail').style.display = 'block';

    document.getElementById("sender").innerHTML = `This Mail is from: ${data.sender} <br> to: ${data.recipients}`;
    document.getElementById("subj").innerHTML = data.subject;
    document.getElementById("text").innerHTML = data.body;

    document.getElementById("delete").addEventListener('click', () => {reply_email(data)});        
    document.getElementById("archive").addEventListener('click', event => {archiveMail(data.id)});
    document.getElementById("unArchive").addEventListener('click', event => { 
      fetch(`/emails/${data.id}`, {
        method:"PUT",
        body: JSON.stringify({
        archived: false
        })
      })
      location.reload()
    });
          
  })
}
function archiveMail(j){
  console.log("Does this work?")
fetch(`/emails/${j}`, {
  method:"PUT",
  body: JSON.stringify({
  archived: true
  })
}) 
location.reload()
}


function reply_email(i) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#one-mail').style.display = 'none';


  // Clear out composition fields
  document.querySelector('#compose-recipients').value = i.sender;
  document.querySelector('#compose-subject').value = `RE: ${i.subject}`;
  document.querySelector('#compose-body').value = `${i.sender} wrote this: ${i.body}`;

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