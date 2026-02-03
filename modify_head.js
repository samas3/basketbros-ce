var head = document.getElementsByTagName('head')[0];
var style = document.createElement('link'); 
style.rel = 'stylesheet';
style.type = 'text/css';
style.href = chrome.runtime.getURL('style.css');
head.appendChild(style);