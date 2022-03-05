/**
 * Some utils functions to use.
 */


/**
 * 
 * @param {string} newBackgroundSrc The new background src to set
 */
export function changeBackground(newBackgroundSrc) {
  // getting the body and set the new background
  const body = document.getElementsByTagName('body')
  body[0].setAttribute('style', `background-image: url('${newBackgroundSrc}');`)
}