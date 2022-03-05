/* 
  Principal javascript to use 
*/

import { changeBackground } from './helpers/utils.js';


// defautl background to use
var backgroundSrcDefault = '/static/img/brazil-image.jpg'


// buttons for change the background
const backgroundButtons = document.querySelectorAll('.background-button');


// setting the initial background
const srcImage = localStorage.getItem('background-image')
if (srcImage != null || srcImage != '') {
  changeBackground(srcImage)
} else {
  changeBackground(backgroundSrcDefault)
}

backgroundButtons.forEach((button) => {
  button.addEventListener('click', () => {
    // change the backgound
    const srcImage = button.childNodes[1].getAttribute('src');
    localStorage.setItem('background-image', srcImage)
    changeBackground(srcImage);
  })
})