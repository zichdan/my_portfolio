// PYTHON DJANGO CODE FOR THE CONTACT FORM -------------BUT STRICTLY COMMENTED TO AVOID UNAVOIDABLE ERRORS ON THE CONTACT PAGE 



// // <!-- Include the reCAPTCHA script if needed -->
// (function () {
//   "use strict";

//   let forms = document.querySelectorAll('.php-email-form');

//   forms.forEach(function(e) {
//     e.addEventListener('submit', function(event) {
//       event.preventDefault();

//       let thisForm = this;

//       let action = thisForm.getAttribute('action');
//       let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');
//       let loadingElement = thisForm.querySelector('.loading');
//       let errorMessageElement = thisForm.querySelector('.error-message');
//       let sentMessageElement = thisForm.querySelector('.sent-message');

//       if (!action) {
//         displayError(thisForm, 'The form action property is not set!');
//         return;
//       }

//       loadingElement.classList.add('d-block');
//       errorMessageElement.classList.remove('d-block');
//       sentMessageElement.classList.remove('d-block');

//       let formData = new FormData(thisForm);

//       if (recaptcha) {
//         if (typeof grecaptcha !== "undefined") {
//           grecaptcha.ready(function() {
//             try {
//               grecaptcha.execute(recaptcha, {action: 'php_email_form_submit'})
//               .then(token => {
//                 formData.set('recaptcha-response', token);
//                 php_email_form_submit(thisForm, action, formData, loadingElement, errorMessageElement, sentMessageElement);
//               });
//             } catch(error) {
//               displayError(thisForm, error);
//             }
//           });
//         } else {
//           displayError(thisForm, 'The reCaptcha javascript API url is not loaded!');
//         }
//       } else {
//         php_email_form_submit(thisForm, action, formData, loadingElement, errorMessageElement, sentMessageElement);
//       }
//     });
//   });

//   function php_email_form_submit(thisForm, action, formData, loadingElement, errorMessageElement, sentMessageElement) {
//     fetch(action, {
//       method: 'POST',
//       body: formData,
//       headers: {'X-Requested-With': 'XMLHttpRequest'}
//     })
//     .then(response => {
//       if (response.ok) {
//         return response.text();
//       } else {
//         throw new Error(`${response.status} ${response.statusText} ${response.url}`);
//       }
//     })
//     .then(data => {
//       loadingElement.classList.remove('d-block');
//       if (data.trim() == 'success') {
//         sentMessageElement.classList.add('d-block');
//         thisForm.reset();
//       } else {
//         throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action);
//       }
//     })
//     .catch((error) => {
//       displayError(thisForm, error);
//     });
//   }

//   function displayError(thisForm, error) {
//     let errorMessageElement = thisForm.querySelector('.error-message');
//     let loadingElement = thisForm.querySelector('.loading');
    
//     loadingElement.classList.remove('d-block');
//     errorMessageElement.innerHTML = error;
//     errorMessageElement.classList.add('d-block');
//   }
// })();






















// jAVASCRIPT CODE FOR PHP CONTACT FORM -------------BUT STRICTLY COMMENTED TO AVOID UNAVOIDABLE ERRORS ON THE CONTACT PAGE 


// /**
// * PHP Email Form Validation - v3.6
// * URL: https://bootstrapmade.com/php-email-form/
// * Author: BootstrapMade.com
// */
// (function () {
//   "use strict";

//   let forms = document.querySelectorAll('.php-email-form');

//   forms.forEach( function(e) {
//     e.addEventListener('submit', function(event) {
//       event.preventDefault();

//       let thisForm = this;

//       let action = thisForm.getAttribute('action');
//       let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');
      
//       if( ! action ) {
//         displayError(thisForm, 'The form action property is not set!');
//         return;
//       }
//       thisForm.querySelector('.loading').classList.add('d-block');
//       thisForm.querySelector('.error-message').classList.remove('d-block');
//       thisForm.querySelector('.sent-message').classList.remove('d-block');

//       let formData = new FormData( thisForm );

//       if ( recaptcha ) {
//         if(typeof grecaptcha !== "undefined" ) {
//           grecaptcha.ready(function() {
//             try {
//               grecaptcha.execute(recaptcha, {action: 'php_email_form_submit'})
//               .then(token => {
//                 formData.set('recaptcha-response', token);
//                 php_email_form_submit(thisForm, action, formData);
//               })
//             } catch(error) {
//               displayError(thisForm, error);
//             }
//           });
//         } else {
//           displayError(thisForm, 'The reCaptcha javascript API url is not loaded!')
//         }
//       } else {
//         php_email_form_submit(thisForm, action, formData);
//       }
//     });
//   });

//   function php_email_form_submit(thisForm, action, formData) {
//     fetch(action, {
//       method: 'POST',
//       body: formData,
//       headers: {'X-Requested-With': 'XMLHttpRequest'}
//     })
//     .then(response => {
//       if( response.ok ) {
//         return response.text();
//       } else {
//         throw new Error(`${response.status} ${response.statusText} ${response.url}`); 
//       }
//     })
//     .then(data => {
//       thisForm.querySelector('.loading').classList.remove('d-block');
//       if (data.trim() == 'OK') {
//         thisForm.querySelector('.sent-message').classList.add('d-block');
//         thisForm.reset(); 
//       } else {
//         throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action); 
//       }
//     })
//     .catch((error) => {
//       displayError(thisForm, error);
//     });
//   }

//   function displayError(thisForm, error) {
//     thisForm.querySelector('.loading').classList.remove('d-block');
//     thisForm.querySelector('.error-message').innerHTML = error;
//     thisForm.querySelector('.error-message').classList.add('d-block');
//   }

// })();
