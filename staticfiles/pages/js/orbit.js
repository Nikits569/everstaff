(function () {
  'use strict';

  var DESKTOP_QUERY = '(min-width: 901px)';
  var BASE_RING_RATIO = 0.33;   // node ring radius as a fraction of container size
  var PILL_GAP = 46;            // px between the node ring and the pill labels
  var NODE_COLORS = ['#16b892', '#3d63d6'];

  function debounce(fn, wait) {
    var timer;
    return function () {
      clearTimeout(timer);
      timer = setTimeout(fn, wait);
    };
  }

  function layoutOrbit(container) {
    var list = container.querySelector('.orbit-items');
    var nodesLayer = container.querySelector('.orbit-nodes');
    if (!list) return;

    var items = Array.prototype.slice.call(list.children);
    var count = items.length;

    if (nodesLayer) nodesLayer.innerHTML = '';

    var isDesktop = window.matchMedia(DESKTOP_QUERY).matches;

    if (!isDesktop || count === 0) {
      items.forEach(function (item) {
        item.style.left = '';
        item.style.top = '';
      });
      return;
    }

    var size = container.clientWidth;
    if (!size) return;

    var cx = size / 2;
    var cy = size / 2;

    // as more items get added later, nudge the ring out a bit so pills
    // keep breathing room instead of overlapping
    var extra = Math.max(0, count - 8) * (size * 0.012);
    var ringRadius = size * BASE_RING_RATIO;
    var pillRadius = ringRadius + PILL_GAP + extra;

    items.forEach(function (item, i) {
      var angle = (i / count) * Math.PI * 2 - Math.PI / 2;

      var nodeX = cx + ringRadius * Math.cos(angle);
      var nodeY = cy + ringRadius * Math.sin(angle);
      var pillX = cx + pillRadius * Math.cos(angle);
      var pillY = cy + pillRadius * Math.sin(angle);

      item.style.left = (pillX / size * 100) + '%';
      item.style.top = (pillY / size * 100) + '%';

      if (nodesLayer) {
        var color = NODE_COLORS[i % NODE_COLORS.length];
        var node = document.createElement('span');
        node.className = 'orbit-node';
        node.style.left = (nodeX / size * 100) + '%';
        node.style.top = (nodeY / size * 100) + '%';
        node.style.background = color;
        node.style.boxShadow = '0 0 0 4px ' + color + '22';
        nodesLayer.appendChild(node);

        item.addEventListener('mouseenter', function () { node.classList.add('active'); });
        item.addEventListener('mouseleave', function () { node.classList.remove('active'); });
        item.addEventListener('focus', function () { node.classList.add('active'); });
        item.addEventListener('blur', function () { node.classList.remove('active'); });
      }
    });
  }

  function init() {
    var orbits = document.querySelectorAll('[data-orbit]');
    if (!orbits.length) return;

    orbits.forEach(layoutOrbit);

    var relayout = debounce(function () {
      orbits.forEach(layoutOrbit);
    }, 150);

    window.addEventListener('resize', relayout);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();