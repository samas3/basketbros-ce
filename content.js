const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.type === 'childList') {
            mutation.addedNodes.forEach((node) => {
                if (node.tagName === 'SCRIPT' && node.src.match(/BasketBros.js/)) {
                    var script = document.createElement('script');
                    script.src = chrome.runtime.getURL('custom.js');
                    node.parentElement.appendChild(script);
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