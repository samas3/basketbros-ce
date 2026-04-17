var head = document.getElementsByTagName('head')[0];
var style = document.createElement('link'); 
style.rel = 'stylesheet';
style.type = 'text/css';
style.href = chrome.runtime.getURL('style.css');
var script = document.createElement('script');
script.src = chrome.runtime.getURL('util.js');
head.appendChild(script);
head.appendChild(style);

const versionMark = document.createElement('div');
const version = chrome.runtime.getManifest().version;
versionMark.className = 'version-mark';
versionMark.textContent = `BCE v${version}`;
document.body.appendChild(versionMark);

function createDialog(options = {}) {
    const { title = '对话框', width = 400, height = 300, onClose = null } = options;

    const overlay = document.createElement('div');
    overlay.className = 'dialog-overlay';

    const dialog = document.createElement('div');
    dialog.className = 'dialog';
    dialog.style.width = `${width}px`;
    dialog.style.height = `${height}px`;

    const header = document.createElement('div');
    header.className = 'dialog-header';

    const titleSpan = document.createElement('span');
    titleSpan.className = 'dialog-title';
    titleSpan.textContent = title;

    const closeBtn = document.createElement('button');
    closeBtn.className = 'dialog-close';
    closeBtn.textContent = '×';
    closeBtn.onclick = () => {
        if (onClose) onClose();
        overlay.remove();
    };

    header.appendChild(titleSpan);
    header.appendChild(closeBtn);

    const content = document.createElement('div');
    content.className = 'dialog-content';

    dialog.appendChild(header);
    dialog.appendChild(content);
    overlay.appendChild(dialog);
    document.body.appendChild(overlay);

    return {
        overlay,
        dialog,
        content,
        close: () => overlay.remove()
    };
}