const versionMark = document.createElement('div');
const version = chrome.runtime.getManifest().version;
versionMark.className = 'version-mark';
versionMark.textContent = `BCE v${version}`;
document.body.appendChild(versionMark);