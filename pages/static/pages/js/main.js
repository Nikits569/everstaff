document.addEventListener('DOMContentLoaded', function () {

  /* ---- "Детальніше" expandable text blocks ---- */
  document.querySelectorAll('[data-expand-toggle]').forEach(function (btn) {
    var targetId = btn.getAttribute('data-expand-toggle');
    var panel = document.getElementById(targetId);
    if (!panel) return;

    btn.addEventListener('click', function () {
      var isOpen = btn.getAttribute('aria-expanded') === 'true';
      if (isOpen) {
        panel.style.maxHeight = '0px';
        btn.setAttribute('aria-expanded', 'false');
      } else {
        panel.style.maxHeight = panel.scrollHeight + 'px';
        btn.setAttribute('aria-expanded', 'true');
      }
      var labelMore = btn.getAttribute('data-label-more');
      var labelLess = btn.getAttribute('data-label-less');
      if (labelMore && labelLess) {
        var span = btn.querySelector('span');
        if (span) span.textContent = isOpen ? labelMore : labelLess;
      }
    });
  });

  /* recalc open panels on resize so max-height stays correct */
  window.addEventListener('resize', function () {
    document.querySelectorAll('[data-expand-toggle][aria-expanded="true"]').forEach(function (btn) {
      var panel = document.getElementById(btn.getAttribute('data-expand-toggle'));
      if (panel) panel.style.maxHeight = panel.scrollHeight + 'px';
    });
  });

  /* ---- Mobile menu toggle (isolated full-screen overlay) ---- */
  var navToggle = document.querySelector('.nav-toggle');
  var mobileMenu = document.getElementById('mobile-menu');
  var mobileMenuClose = document.getElementById('mobile-menu-close');

  function openMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.add('open');
    document.body.classList.add('menu-open');
    if (navToggle) navToggle.setAttribute('aria-expanded', 'true');
  }
  function closeMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.remove('open');
    document.body.classList.remove('menu-open');
    if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
  }

  if (navToggle && mobileMenu) {
    navToggle.addEventListener('click', function () {
      if (mobileMenu.classList.contains('open')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });
    if (mobileMenuClose) mobileMenuClose.addEventListener('click', closeMobileMenu);
    mobileMenu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMobileMenu);
    });
    // close on resize back to desktop width
    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) closeMobileMenu();
    });
  }

  /* ---- Language switcher (visual only — no i18n logic, wired up server-side) ---- */
  document.querySelectorAll('.lang-switch').forEach(function (el) {
    var trigger = el.querySelector('button');
    if (!trigger) return;
    trigger.addEventListener('click', function (e) {
      e.stopPropagation();
      var isOpen = el.getAttribute('data-open') === 'true';
      document.querySelectorAll('.lang-switch').forEach(function (o) { o.setAttribute('data-open', 'false'); });
      el.setAttribute('data-open', isOpen ? 'false' : 'true');
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.lang-switch').forEach(function (o) { o.setAttribute('data-open', 'false'); });
  });

  /* ---- Toast messages: manual close + cleanup after auto-hide animation ---- */
  document.querySelectorAll('.toast-message').forEach(function (toast) {
    var closeBtn = toast.querySelector('.toast-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', function () { toast.remove(); });
    }
    toast.addEventListener('animationend', function (e) {
      if (e.animationName === 'toast-out') toast.remove();
    });
  });

  /* ---- Header shadow / state on scroll (subtle) ---- */
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      header.style.boxShadow = window.scrollY > 8 ? '0 12px 30px -22px rgba(16,26,51,.35)' : 'none';
    });
  }
});
