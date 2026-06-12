/**
 * frame.js — Wraps page content in an iPhone 15 Pro frame.
 * Injects app.css, builds the device shell, adds status-bar
 * icons, and handles responsive viewport scaling.
 */
(function () {
  /* ── 0. Global navigation helper ── */
  window.navigateTo = function(url) {
    window.location.href = url;
  };

  var isDesktop = window.innerWidth > 768;

  /* ── 1. Prevent flash (only on desktop) ── */
  if (isDesktop) {
    var s = document.createElement('style');
    s.textContent = 'body{background:#fff!important;margin:0}';
    document.head.appendChild(s);
  }

  /* ── 2. Inject app.css ── */
  var appCss = document.createElement('link');
  appCss.rel = 'stylesheet';
  appCss.href = 'app.css';
  document.head.appendChild(appCss);

  function wrap() {
    if (!isDesktop) return;
    if (document.querySelector('.phone-device')) return;
    document.body.classList.remove('bg-[#1C1B1F]');

    /* Gather non-script/style children */
    var kids = [];
    var nodes = document.body.childNodes;
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      if (n.nodeType === 1) {
        var t = n.tagName.toUpperCase();
        if (t === 'SCRIPT' || t === 'STYLE' || t === 'LINK') continue;
      }
      kids.push(n);
    }

    /* Build device */
    var device = document.createElement('div');
    device.className = 'phone-device';

    /* Side buttons */
    ['phone-btn-power', 'phone-btn-silent', 'phone-btn-volup', 'phone-btn-voldn'].forEach(function (cls) {
      var btn = document.createElement('div');
      btn.className = cls;
      device.appendChild(btn);
    });

    var screen = document.createElement('div');
    screen.className = 'phone-screen';

    /* Dynamic Island */
    var island = document.createElement('div');
    island.className = 'phone-island';
    screen.appendChild(island);

    /* Home indicator pill */
    var pill = document.createElement('div');
    pill.className = 'phone-pill';
    screen.appendChild(pill);

    /* Status bar — right side icons (signal, wifi, battery) */
    var statusRight = document.createElement('div');
    statusRight.className = 'phone-status-right';
    statusRight.innerHTML = '<svg width="68" height="12" viewBox="0 0 68 12" fill="none" xmlns="http://www.w3.org/2000/svg">' +
      /* Signal bars */
      '<rect x="0" y="7" width="3" height="5" rx="0.5" fill="white" opacity="0.4"/>' +
      '<rect x="4.5" y="5" width="3" height="7" rx="0.5" fill="white" opacity="0.6"/>' +
      '<rect x="9" y="3" width="3" height="9" rx="0.5" fill="white" opacity="0.8"/>' +
      '<rect x="13.5" y="0" width="3" height="12" rx="0.5" fill="white"/>' +
      /* WiFi */
      '<path d="M25 5.5C27.2 3.5 30.8 3.5 33 5.5" stroke="white" stroke-width="1.2" stroke-linecap="round" opacity="0.5"/>' +
      '<path d="M26.5 7.5C28 6 30 6 31.5 7.5" stroke="white" stroke-width="1.2" stroke-linecap="round"/>' +
      '<circle cx="29" cy="10" r="1" fill="white"/>' +
      /* Battery */
      '<rect x="42" y="1" width="22" height="10" rx="2.5" stroke="white" stroke-width="1" fill="none" opacity="0.35"/>' +
      '<rect x="64" y="4" width="1.5" height="4" rx="0.75" fill="white" opacity="0.4"/>' +
      '<rect x="44" y="3" width="16" height="6" rx="1.5" fill="white"/>' +
      '</svg>';
    screen.appendChild(statusRight);

    /* Scroll wrapper */
    var scroll = document.createElement('div');
    scroll.className = 'phone-screen-scroll';

    kids.forEach(function (child) { scroll.appendChild(child); });

    screen.appendChild(scroll);
    device.appendChild(screen);
    document.body.insertBefore(device, document.body.firstChild);

    /* ── Responsive scaling ── */
    function fitToViewport() {
      var deviceW = 401;
      var deviceH = 860;
      var padX = 60, padY = 60;
      var availW = window.innerWidth - padX;
      var availH = window.innerHeight - padY;
      var scaleW = availW / deviceW;
      var scaleH = availH / deviceH;
      var scale = Math.min(scaleW, scaleH, 1);
      device.style.transform = 'scale(' + scale + ')';
    }

    fitToViewport();
    window.addEventListener('resize', fitToViewport);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wrap);
  } else {
    wrap();
  }
})();
