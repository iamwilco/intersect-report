/* ══════════════════════════════════════════════════════════════
   INTERSECT COMMITTEE REPORTS — Frontend Engine
   Handles data loading, filtering, charts, and interactivity.
   ══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── Utility ── */
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

  /* ════════════════════════════════════════
     PROMISE TRACKER — Filter + Count
     ════════════════════════════════════════ */
  window.filterTable = function filterTable(status) {
    const table = $('#tracker');
    if (!table) return;

    const rows = $$('tbody tr', table);
    let visible = 0;

    rows.forEach(row => {
      if (status === 'all' || row.dataset.status === status) {
        row.classList.remove('hidden');
        visible++;
      } else {
        row.classList.add('hidden');
      }
    });

    // Update button states
    $$('.filter-btn').forEach(btn => btn.classList.remove('active'));
    const activeBtn = $(`#btn-${status}`);
    if (activeBtn) activeBtn.classList.add('active');

    // Update count
    const countLabel = $('#count-label');
    if (countLabel) countLabel.textContent = `Showing ${visible} items`;
  };

  /* ════════════════════════════════════════
     ANIMATED COUNTERS — Stat strips
     ════════════════════════════════════════ */
  function animateCounters() {
    const counters = $$('[data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = parseInt(el.dataset.count, 10);
        if (isNaN(target)) return;

        const duration = 800;
        const start = performance.now();
        const initial = 0;

        function tick(now) {
          const elapsed = now - start;
          const progress = Math.min(elapsed / duration, 1);
          // Ease out cubic
          const eased = 1 - Math.pow(1 - progress, 3);
          const current = Math.round(initial + (target - initial) * eased);
          el.textContent = current;
          if (progress < 1) requestAnimationFrame(tick);
        }

        requestAnimationFrame(tick);
        observer.unobserve(el);
      });
    }, { threshold: 0.3 });

    counters.forEach(el => observer.observe(el));
  }

  /* ════════════════════════════════════════
     PROGRESS RING — SVG donut
     ════════════════════════════════════════ */
  function initProgressRings() {
    $$('.progress-ring').forEach(svg => {
      const fg = $('.ring-fg', svg);
      if (!fg) return;
      const r = parseFloat(fg.getAttribute('r'));
      const circumference = 2 * Math.PI * r;
      const pct = parseFloat(svg.dataset.percent) || 0;

      fg.style.strokeDasharray = circumference;
      fg.style.strokeDashoffset = circumference;

      // Animate on scroll
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          const offset = circumference - (pct / 100) * circumference;
          fg.style.strokeDashoffset = offset;
          observer.unobserve(svg);
        });
      }, { threshold: 0.3 });

      observer.observe(svg);
    });
  }

  /* ════════════════════════════════════════
     STAGGER ANIMATIONS — Fade-in on scroll
     ════════════════════════════════════════ */
  function initScrollAnimations() {
    const elements = $$('.fade-in-on-scroll');
    if (!elements.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    elements.forEach(el => observer.observe(el));
  }

  /* ════════════════════════════════════════
     ATTENDANCE BAR ANIMATION
     ════════════════════════════════════════ */
  function initAttendanceBars() {
    const bars = $$('.att-bar');
    if (!bars.length) return;

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const bar = entry.target;
        const targetWidth = bar.dataset.width || bar.style.width;
        bar.style.width = '0%';
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            bar.style.width = targetWidth;
          });
        });
        observer.unobserve(bar);
      });
    }, { threshold: 0.2 });

    bars.forEach(bar => {
      bar.dataset.width = bar.style.width;
      observer.observe(bar);
    });
  }

  /* ════════════════════════════════════════
     TABLE SORT — Click column headers
     ════════════════════════════════════════ */
  function initSortableTables() {
    $$('table[data-sortable]').forEach(table => {
      const headers = $$('th', table);
      headers.forEach((th, colIdx) => {
        th.style.cursor = 'pointer';
        th.title = 'Click to sort';
        let ascending = true;

        th.addEventListener('click', () => {
          const tbody = $('tbody', table);
          const rows = $$('tr', tbody);

          rows.sort((a, b) => {
            const aText = a.children[colIdx]?.textContent?.trim() || '';
            const bText = b.children[colIdx]?.textContent?.trim() || '';

            // Try numeric
            const aNum = parseFloat(aText.replace(/[^0-9.-]/g, ''));
            const bNum = parseFloat(bText.replace(/[^0-9.-]/g, ''));
            if (!isNaN(aNum) && !isNaN(bNum)) {
              return ascending ? aNum - bNum : bNum - aNum;
            }
            return ascending
              ? aText.localeCompare(bText)
              : bText.localeCompare(aText);
          });

          rows.forEach(row => tbody.appendChild(row));
          ascending = !ascending;

          // Visual indicator
          headers.forEach(h => h.dataset.sort = '');
          th.dataset.sort = ascending ? 'desc' : 'asc';
        });
      });
    });
  }

  /* ════════════════════════════════════════
     SMOOTH NAV HIGHLIGHT
     ════════════════════════════════════════ */
  function highlightCurrentNav() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    $$('.masthead-nav a').forEach(link => {
      const href = link.getAttribute('href');
      if (href === currentPage) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  /* ════════════════════════════════════════
     KEYBOARD SHORTCUTS
     ════════════════════════════════════════ */
  function initKeyboardNav() {
    document.addEventListener('keydown', e => {
      // Left/Right arrow for nav between reports
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

      const navLinks = $$('.masthead-nav a');
      const currentIdx = navLinks.findIndex(a => a.classList.contains('active'));

      if (e.key === 'ArrowLeft' && currentIdx > 0) {
        e.preventDefault();
        navLinks[currentIdx - 1].click();
      } else if (e.key === 'ArrowRight' && currentIdx < navLinks.length - 1) {
        e.preventDefault();
        navLinks[currentIdx + 1].click();
      }
    });
  }

  /* ════════════════════════════════════════
     DATA LOADING — For dynamic committee pages
     ════════════════════════════════════════ */
  window.loadCommitteeData = async function (committeeId) {
    try {
      const resp = await fetch(`data/${committeeId.toLowerCase()}.json`);
      if (!resp.ok) return null;
      return await resp.json();
    } catch {
      return null;
    }
  };

  window.loadIndex = async function () {
    try {
      const resp = await fetch('data/index.json');
      if (!resp.ok) return null;
      return await resp.json();
    } catch {
      return null;
    }
  };

  /* ════════════════════════════════════════
     MARKDOWN RENDERER — Minimal for report sections
     ════════════════════════════════════════ */
  window.renderMarkdown = function (text) {
    if (!text) return '';
    return text
      // Headers
      .replace(/^### (.+)$/gm, '<h3>$1</h3>')
      .replace(/^## (.+)$/gm, '<h2>$1</h2>')
      // Bold
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      // Italic
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      // Lists
      .replace(/^- (.+)$/gm, '<li>$1</li>')
      .replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>')
      // Horizontal rules
      .replace(/^---$/gm, '<hr>')
      // Paragraphs (lines not already wrapped)
      .replace(/^(?!<[hulo]|<li|<hr)(.+)$/gm, '<p>$1</p>')
      // Clean up
      .replace(/<\/ul>\s*<ul>/g, '')
      .replace(/\n{3,}/g, '\n\n');
  };

  /* ════════════════════════════════════════
     TOOLTIP — Lightweight hover tooltips
     ════════════════════════════════════════ */
  function initTooltips() {
    let tip = document.createElement('div');
    tip.className = 'tooltip';
    tip.style.cssText = `
      position: fixed; z-index: 999; pointer-events: none;
      background: var(--ink); color: var(--paper); font-family: var(--mono);
      font-size: 11px; padding: 4px 10px; border-radius: 3px;
      opacity: 0; transition: opacity 0.15s;
      white-space: nowrap; max-width: 300px;
    `;
    document.body.appendChild(tip);

    document.addEventListener('mouseover', e => {
      const target = e.target.closest('[title]');
      if (!target) return;
      const text = target.getAttribute('title');
      if (!text) return;
      target.dataset.tooltipText = text;
      target.removeAttribute('title');
      tip.textContent = text;
      tip.style.opacity = '1';
    });

    document.addEventListener('mousemove', e => {
      if (tip.style.opacity === '0') return;
      tip.style.left = (e.clientX + 12) + 'px';
      tip.style.top = (e.clientY - 28) + 'px';
    });

    document.addEventListener('mouseout', e => {
      const target = e.target.closest('[data-tooltip-text]');
      if (!target) return;
      target.setAttribute('title', target.dataset.tooltipText);
      delete target.dataset.tooltipText;
      tip.style.opacity = '0';
    });
  }

  /* ════════════════════════════════════════
     INIT
     ════════════════════════════════════════ */
  function init() {
    highlightCurrentNav();
    animateCounters();
    initProgressRings();
    initScrollAnimations();
    initAttendanceBars();
    initSortableTables();
    initKeyboardNav();
    initTooltips();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
