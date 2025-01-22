import './css/main.css';
import * as riot from 'riot';

const page = document.body.getAttribute('data-page');

import Dashboard from '@components/dashboard/dashboard.riot';

console.log("dashboard:", Dashboard);

switch (page) {
  
  case 'home':
    import('@components/home.riot').then((module) => {
      riot.register('app', module.default);
      riot.mount('app'); // Mount the component
    }).catch((error) => {
      console.error('Error loading home component:', error);
    });
    break;
  
  case 'login':
    import('@components/authentication/login-form.riot').then((module) => {
      console.log(riot.register('app', module.default));
      riot.mount('app');
    }).catch((error) => {
      console.error('Error loading page:', error)
    })
    break;
  
  case 'dashboard':
    import('@components/dashboard/dashboard.riot').then((module) => {
      console.log("module:", module.default);
      riot.register('app', Dashboard);
      //riot.register('app', module.default);
      riot.mount('app', {}, 'dashboard');
    }).catch((error) => {
      console.error('Error loading dashboard component:', error)
    })
    break;

  // As many pages as needed we can just export the components to it.
  default:
    console.error("the page name is not associted with any component");
}
