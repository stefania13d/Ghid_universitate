document.addEventListener('DOMContentLoaded', () => {
    const readMoreBtn = document.getElementById('read-more-btn');
    const hiddenContent = document.getElementById('hidden-content');
    const welcomeMessage = document.getElementById('welcome-message'); // get a reference to the welcome message
  
        readMoreBtn.addEventListener('click', () => {
          if (hiddenContent.style.display === 'none') {
            hiddenContent.style.display = 'block';
            readMoreBtn.innerHTML = '<< Afișează mai puțin';
            welcomeMessage.style.display = 'none'; // hide the welcome message
            readMoreBtn.classList.add('show-less'); // add the class
            
          } else {
            hiddenContent.style.display = 'none';
            readMoreBtn.innerHTML = 'Vezi mai multe >>';
            welcomeMessage.style.display = 'block'; // show the welcome message
            readMoreBtn.classList.remove('show-less'); // remove the class
          }
        });
    });
