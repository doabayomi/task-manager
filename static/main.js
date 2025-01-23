import './css/main.css';
import * as riot from 'riot';

const page = document.body.getAttribute('data-page');

switch (page) {
  
  case 'login':
    import('@components/authentication/login-form.riot').then((module) => {
      riot.register('app', module.default);
      riot.mount('app');
    }).catch((error) => {
      console.error('Error loading page:', error)
    })
    break;

  case 'register':
    import('@components/authentication/register-form.riot').then((module) => {
      riot.register('app', module.default);
      riot.mount('app');
    }).catch((error) => {
      console.error('Error loading page:', error)
    })
    break;
  
  // As many pages as needed we can just export the components to it.
  default:
    break;
}
