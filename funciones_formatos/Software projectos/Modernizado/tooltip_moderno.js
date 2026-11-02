/**
 * Modern Tooltip System
 * Reemplazo moderno de wz_tooltip.js
 * Compatible con: Chrome 80+, Firefox 75+, Safari 13+, Edge 80+
 */

// Constantes para compatibilidad con API antigua
const DELAY = 'DELAY';
const FADEIN = 'FADEIN';
const FADEOUT = 'FADEOUT';
const BGCOLOR = 'BGCOLOR';
const FONTCOLOR = 'FONTCOLOR';
const BORDERCOLOR = 'BORDERCOLOR';
const WIDTH = 'WIDTH';
const STICKY = 'STICKY';
const CLICKCLOSE = 'CLICKCLOSE';
const CLICKSTICKY = 'CLICKSTICKY';
const CLOSEBTN = 'CLOSEBTN';
const TITLE = 'TITLE';
const ABOVE = 'ABOVE';
const LEFT = 'LEFT';
const OFFSETX = 'OFFSETX';
const OFFSETY = 'OFFSETY';
const CENTERMOUSE = 'CENTERMOUSE';
const FOLLOWMOUSE = 'FOLLOWMOUSE';
const DURATION = 'DURATION';

class TooltipManager {
  #config = {
    delay: 100,
    duration: 0,
    fadeIn: 200,
    fadeOut: 150,
    offsetX: 14,
    offsetY: 4,
    followMouse: false,
    centerMouse: true,
    above: false,
    left: false,
    maxWidth: 400,
    padding: '12px 16px',
    borderRadius: '8px',
    backgroundColor: '#1e293b',
    color: '#f8fafc',
    fontSize: '14px',
    fontFamily: 'system-ui, -apple-system, sans-serif',
    boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
    sticky: false,
    clickClose: false,
    clickSticky: true,
    closeButton: true,
    title: '',
    easing: 'cubic-bezier(0.16, 1, 0.3, 1)'
  };

  #tooltip = null;
  #content = null;
  #closeBtn = null;
  #currentTarget = null;
  #isVisible = false;
  #mouseX = 0;
  #mouseY = 0;
  #hideTimeout = null;
  #showTimeout = null;
  #animationFrame = null;

  constructor() {
    this.#init();
  }

  #init() {
    this.#tooltip = document.createElement('div');
    this.#tooltip.className = 'modern-tooltip';
    this.#tooltip.setAttribute('role', 'tooltip');
    this.#tooltip.setAttribute('hidden', '');
    
    this.#tooltip.innerHTML = `
      <div class="tooltip-header">
        <span class="tooltip-title"></span>
        <button class="tooltip-close" aria-label="Cerrar tooltip">×</button>
      </div>
      <div class="tooltip-body"></div>
    `;
    
    this.#content = this.#tooltip.querySelector('.tooltip-body');
    this.#closeBtn = this.#tooltip.querySelector('.tooltip-close');
    
    this.#closeBtn.addEventListener('click', () => this.hide());
    document.addEventListener('mousemove', this.#handleMouseMove.bind(this));
    document.addEventListener('click', this.#handleClick.bind(this), true);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.hide();
    });
    
    document.body.appendChild(this.#tooltip);
    this.#injectStyles();
  }

  #injectStyles() {
    if (document.getElementById('modern-tooltip-styles')) return;
    
    const styles = document.createElement('style');
    styles.id = 'modern-tooltip-styles';
    styles.textContent = `
      .modern-tooltip {
        position: fixed;
        z-index: 9999;
        max-width: min(90vw, 400px);
        background: ${this.#config.backgroundColor};
        color: ${this.#config.color};
        font-family: ${this.#config.fontFamily};
        font-size: ${this.#config.fontSize};
        padding: ${this.#config.padding};
        border-radius: ${this.#config.borderRadius};
        box-shadow: ${this.#config.boxShadow};
        pointer-events: none;
        opacity: 0;
        transform: translateY(8px) scale(0.96);
        transition: 
          opacity ${this.#config.fadeIn}ms ${this.#config.easing},
          transform ${this.#config.fadeIn}ms ${this.#config.easing};
        will-change: transform, opacity;
      }
      
      .modern-tooltip[hidden] {
        display: none !important;
      }
      
      .modern-tooltip.visible {
        opacity: 1;
        transform: translateY(0) scale(1);
        pointer-events: auto;
      }
      
      .modern-tooltip.fading-out {
        opacity: 0;
        transform: translateY(4px) scale(0.98);
        transition-duration: ${this.#config.fadeOut}ms;
      }
      
      .tooltip-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 8px;
        padding-bottom: 8px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
      }
      
      .tooltip-title {
        font-weight: 600;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.025em;
        color: rgba(255,255,255,0.8);
      }
      
      .tooltip-close {
        background: rgba(255,255,255,0.1);
        border: none;
        color: inherit;
        width: 24px;
        height: 24px;
        border-radius: 6px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        line-height: 1;
        transition: background 150ms;
        pointer-events: auto;
      }
      
      .tooltip-close:hover {
        background: rgba(255,255,255,0.2);
      }
      
      .tooltip-body {
        line-height: 1.5;
      }
      
      .tooltip-body p { margin: 0 0 8px 0; }
      .tooltip-body p:last-child { margin-bottom: 0; }
      
      .modern-tooltip.position-above {
        transform-origin: bottom center;
      }
      
      .modern-tooltip.position-left {
        transform-origin: right center;
      }
    `;
    document.head.appendChild(styles);
  }

  show(content, options = {}) {
    if (!content) return;
    
    this.#clearTimeouts();
    
    const opts = { ...this.#config, ...options };
    
    if (this.#isVisible) {
      this.hide();
    }
    
    this.#showTimeout = setTimeout(() => {
      this.#render(content, opts);
    }, opts.delay);
  }

  showFromElement(elementId, options = {}) {
    const element = document.getElementById(elementId);
    if (!element) {
      console.warn(`Elemento #${elementId} no encontrado`);
      return;
    }
    
    const content = element.cloneNode(true);
    content.style.display = 'block';
    content.hidden = false;
    
    this.show(content, { ...options, isHTML: true });
  }

  hide() {
    this.#clearTimeouts();
    
    if (!this.#isVisible || !this.#tooltip) return;
    
    this.#tooltip.classList.remove('visible');
    this.#tooltip.classList.add('fading-out');
    
    this.#hideTimeout = setTimeout(() => {
      this.#tooltip.setAttribute('hidden', '');
      this.#tooltip.classList.remove('fading-out');
      this.#isVisible = false;
      this.#currentTarget = null;
    }, this.#config.fadeOut);
  }

  #render(content, options) {
    this.#content.innerHTML = '';
    
    if (options.isHTML || content instanceof HTMLElement) {
      this.#content.appendChild(content);
    } else {
      this.#content.textContent = content;
    }
    
    const titleEl = this.#tooltip.querySelector('.tooltip-title');
    titleEl.textContent = options.title || '';
    titleEl.style.display = options.title ? 'block' : 'none';
    
    this.#closeBtn.style.display = options.closeButton ? 'flex' : 'none';
    
    this.#tooltip.removeAttribute('hidden');
    this.#tooltip.offsetHeight;
    
    this.#isVisible = true;
    this.#position(options);
    this.#tooltip.classList.add('visible');
    
    if (options.duration > 0) {
      this.#hideTimeout = setTimeout(() => this.hide(), options.duration);
    }
  }

  #position(options) {
    const rect = this.#tooltip.getBoundingClientRect();
    const viewport = {
      width: window.innerWidth,
      height: window.innerHeight
    };
    
    let x = this.#mouseX + options.offsetX;
    let y = this.#mouseY + options.offsetY;
    
    if (options.centerMouse) {
      x = this.#mouseX - (rect.width / 2);
    }
    
    if (options.above || (y + rect.height > viewport.height - 20)) {
      y = this.#mouseY - rect.height - options.offsetY;
      this.#tooltip.classList.add('position-above');
    } else {
      this.#tooltip.classList.remove('position-above');
    }
    
    if (options.left || (x + rect.width > viewport.width - 20)) {
      x = this.#mouseX - rect.width - options.offsetX;
      this.#tooltip.classList.add('position-left');
    } else {
      this.#tooltip.classList.remove('position-left');
    }
    
    x = Math.max(10, Math.min(x, viewport.width - rect.width - 10));
    y = Math.max(10, Math.min(y, viewport.height - rect.height - 10));
    
    this.#tooltip.style.left = `${x}px`;
    this.#tooltip.style.top = `${y}px`;
  }

  #handleMouseMove(e) {
    this.#mouseX = e.clientX;
    this.#mouseY = e.clientY;
    
    if (this.#isVisible && this.#config.followMouse) {
      cancelAnimationFrame(this.#animationFrame);
      this.#animationFrame = requestAnimationFrame(() => {
        this.#position(this.#config);
      });
    }
  }

  #handleClick(e) {
    if (this.#config.clickClose && this.#isVisible && !this.#tooltip.contains(e.target)) {
      this.hide();
    }
    
    if (this.#config.clickSticky && this.#currentTarget === e.target) {
      this.#config.followMouse = false;
    }
  }

  #clearTimeouts() {
    clearTimeout(this.#showTimeout);
    clearTimeout(this.#hideTimeout);
    cancelAnimationFrame(this.#animationFrame);
  }

  destroy() {
    this.#clearTimeouts();
    this.#tooltip?.remove();
    document.getElementById('modern-tooltip-styles')?.remove();
  }
}

// Singleton global
const Tooltip = new TooltipManager();

// Función para parsear argumentos de API antigua
function parseOldArgs(args) {
  const options = {};
  const map = {
    'DELAY': 'delay',
    'FADEIN': 'fadeIn',
    'FADEOUT': 'fadeOut',
    'BGCOLOR': 'backgroundColor',
    'FONTCOLOR': 'color',
    'BORDERCOLOR': 'borderColor',
    'WIDTH': 'maxWidth',
    'STICKY': 'sticky',
    'CLICKCLOSE': 'clickClose',
    'CLICKSTICKY': 'clickSticky',
    'CLOSEBTN': 'closeButton',
    'TITLE': 'title',
    'ABOVE': 'above',
    'LEFT': 'left',
    'OFFSETX': 'offsetX',
    'OFFSETY': 'offsetY',
    'CENTERMOUSE': 'centerMouse',
    'FOLLOWMOUSE': 'followMouse',
    'DURATION': 'duration'
  };
  
  for (let i = 0; i < args.length; i += 2) {
    const key = args[i];
    const value = args[i + 1];
    if (key !== undefined && value !== undefined) {
      const newKey = map[key] || key.toLowerCase();
      options[newKey] = value;
    }
  }
  return options;
}

// API global compatible
window.Tip = (text, ...args) => {
  const options = parseOldArgs(args);
  Tooltip.show(text, options);
};

window.TagToTip = (elementId, ...args) => {
  const options = parseOldArgs(args);
  Tooltip.showFromElement(elementId, options);
};

window.UnTip = () => Tooltip.hide();