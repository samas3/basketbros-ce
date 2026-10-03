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

const dict = {
    'zh': {

    },
    'en': {
        'or': 'OR',
        'quarter': 'QUARTER',
        'locked': 'LOCKED',
        'strengths': 'STRENGTHS',
        'weaknesses': 'WEAKNESSES',
        'skills': 'SKILLS',
        'play_now': 'Play Now!',
        '2p': '2 PLAYERS SAME PC',
        'boss_challenge': 'BOSS CHALLENGE',
        'online_vs_friends': 'ONLINE VS FRIENDS',
        'host': 'HOST',
        'join': 'JOIN',
        'server': 'Server:',
        "WE": "US California",
        "EA": "US Atlanta",
        "EU": "EU Frankfurt",
        "AS": "AS Seoul",
        "AU": "AU Sydney",
        "MW": "US Chicago",
        "DA": "US Dallas",
        "NY": "US New Jersey",
        'privacy_policy': 'Privacy Policy',
        'terms_of_service': 'Terms of Service',
        'copyright': ' Blue Wizard Digital',
        'control_panel': 'Control Panel',
        'cpu_guy': 'CPU Guy: ',
        'boss': 'Boss: ',
        'you': 'You: ',
        'human_guy': 'Human Guy: ',
        'choose_baller': 'CHOOSE YOUR BALLER',
        'ready': ' Ready!',
        'left_side': 'LEFT SIDE: ',
        'right_side': 'RIGHT SIDE: ',
        'connecting': 'Connecting to server.',
        'connected': 'Connected, waiting for opponent!',
        'join_code': 'Join Code:',
        'tip': 'Tip: Press ENTER to chat during games!',
        'enter_game_code': 'Enter Game Code',
        'game_paused': 'Game Paused',
        'copy': 'Copy',
        'okay': 'Okay!',
        'stay': 'Stay',
        'quit': 'Quit',
        'exit': 'Exit',
        
    }
}