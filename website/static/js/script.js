'use strict';

/**
 * navbar toggle
 */

const overlay = document.querySelector("[data-overlay]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const navElemArr = [navOpenBtn, navCloseBtn, overlay];

const navToggleEvent = function (elem) {
  for (let i = 0; i < elem.length; i++) {
    elem[i].addEventListener("click", function () {
      navbar.classList.toggle("active");
      overlay.classList.toggle("active");
    });
  }
}

navToggleEvent(navElemArr);
navToggleEvent(navLinks);



/**
 * header sticky & go to top
 */

const header = document.querySelector("[data-header]");
const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {

  if (window.scrollY >= 200) {
    header.classList.add("active");
    goTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    goTopBtn.classList.remove("active");
  }

});

AOS.init({ delay: 200, offset: 100, duration: 500 });

// For emailing
async function send_email(subject, msg) {
  let message = "Hi, someone tried to contact you from your website. Here are the details\n\n" + msg + "\n\nRegards,\nYour Website"
  const response = await fetch(window.location.origin + "/contact", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ subject, message })
  });
  return await response.json();
}

async function get_message(subject) {

  const { value: formValues } = await Swal.fire({
    title: 'Enter user details',
    html:
      '<center>' +
      '<label for="swal-input1">Enter name</label>' +
      '<input id="swal-input1" type="name" class="swal2-input">' +
      '<label for="swal-input2">Enter email</label>' +
      '<input id="swal-input2" type="email" class="swal2-input">' +
      '<label for="swal-input3">Enter phone</label>' +
      '<input id="swal-input3" type="number" class="swal2-input">' +
      '<label for="swal-input4">Enter message</label>' +
      '<textarea id="swal-input4" class="swal2-textarea" placeholder="Type your message here..." id="swal2-input"></textarea>' +
      '<center>',
    focusConfirm: false,
    confirmButtonText: 'submit',
    confirmButtonColor: '#3085d6',
    didClose: () => {
      Swal.showLoading();
    },
    preConfirm: () => {
      const name = document.getElementById('swal-input1').value
      const email = document.getElementById('swal-input2').value
      const phone = document.getElementById('swal-input3').value
      const message = document.getElementById('swal-input4').value
      const nameRegex = /^[a-zA-Z\s]+$/
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      const phoneRegex = /^\d{10}$/
      if (!nameRegex.test(name)) {
        Swal.showValidationMessage('Please enter a valid name')
      } else if (!emailRegex.test(email)) {
        Swal.showValidationMessage('Please enter a valid email address')
      } else if (!phoneRegex.test(phone)) {
        Swal.showValidationMessage('Please enter a valid phone number')
      } else {
        return [name, email, phone, message]
      }
    }
  }).then(async (result) => {
    if (result.value) {
      const [name, email, phone, message] = result.value
          const msg = "Name: " + name + "\nEmail: " + email + "\nPhone: " + phone + "\nMessage: " + message
          send_email(subject , msg).then((data) => {
            if (data.status == "success") {
              Swal.fire({
                icon: 'success',
                title: 'Your message has been sent',
                text: 'We will get back to you shortly',
                confirmButtonText: 'Ok'
              })
            } else {
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Something went wrong',
                confirmButtonText: 'Ok'
              })
            }
          })
    }
  });
}

const contactus = document.getElementById('contactus');
const enquire = document.getElementById("enquire");
if (enquire) {
  enquire.addEventListener("click", () => {
    const package_name = document.getElementById('packname').textContent;
    get_message("Someone is Enquirying about " + package_name);
  });
}
contactus.addEventListener("click", () => {
  get_message("Someone Tried to contact you from your website");
});