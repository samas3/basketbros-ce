const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.type === 'childList') {
            mutation.addedNodes.forEach((node) => {
                if (node.tagName === 'SCRIPT' && node.src.match(/BasketBros.js/)) {
                    node.src = chrome.runtime.getURL('BasketBros.js');
                }
            });
        }
    });
});
observer.observe(document.documentElement, {
    childList: true,
    subtree: true,
});