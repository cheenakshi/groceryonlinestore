window.addEventListener('DOMContentLoaded', () => {
    debugger
    const userData = JSON.parse(localStorage.getItem("userData"));
    const userDropdown = document.getElementById('userDropdown');
    const loginIcon = document.getElementById('loginIcon');
    const usernameSpan = document.getElementById('username');
    const userOptions = document.getElementById('userOptions');

    if (userData && userData.userName) {
       usernameSpan.textContent = userData.userName;
       loginIcon.style.display = 'none'; // Hide login icon
       userDropdown.style.display = 'flex'; // Show username dropdown
    } else {
       userDropdown.style.display = 'none'; // Hide username dropdoFwn
       loginIcon.style.display = 'flex'; // Show login icon
    }


 });

 function handleOptionChange(event) {
    debugger
       const selectedOption = event.target.innerText;
       if (selectedOption === 'Profile') {
          window.location.href = '/ui/profile.html';
       } else if (selectedOption === 'Logout') {
          localStorage.removeItem("userData");
          window.location.href = "/ui/home.html";
       }
    }