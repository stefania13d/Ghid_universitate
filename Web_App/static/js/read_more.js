document.addEventListener('DOMContentLoaded', () => {
    const readMoreBtn = document.getElementById('read-more-btn');
    const hiddenContent = document.getElementById('hidden-content');
  
    readMoreBtn.addEventListener('click', () => {
      if (hiddenContent.style.display === 'none') {
        hiddenContent.style.display = 'block';
        readMoreBtn.innerHTML = 'Read Less';
      } else {
        hiddenContent.style.display = 'none';
        readMoreBtn.innerHTML = 'About University';
      }
    });
  });