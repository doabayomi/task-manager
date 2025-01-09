import './css/main.css';
import * as riot from 'riot';

document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.getAttribute('data-page');

  switch (page) {
    case 'home':
      import('@components/pages/home.riot').then((module) => {
        // Mount the component to the '#app' div
        riot.mount('#app', module.default); // Ensure module.default is usec.
      });
      break;
    
    case 'login':
      import('@components/pages/login-form.riot').then((module) => {
        riot.mount('#app', module.default)
      })
      riot.mount('#app', Home);
    
    // As many pages as needed we can just export the components to it.
    default:
      break;
  }
})
