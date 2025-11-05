// 网页放大镜 - Content Script
(function() {
  'use strict';

  // 放大镜配置
  const config = {
    magnifierSize: 200,      // 放大镜直径
    zoomLevel: 2,            // 放大倍数
    borderWidth: 3,          // 边框宽度
    isActive: false          // 放大镜是否激活
  };

  // 放大镜元素
  let magnifier = null;
  let magnifierLens = null;

  // 创建放大镜元素
  function createMagnifier() {
    // 创建放大镜容器
    magnifier = document.createElement('div');
    magnifier.id = 'page-magnifier';
    magnifier.style.cssText = `
      position: fixed;
      width: ${config.magnifierSize}px;
      height: ${config.magnifierSize}px;
      border-radius: 50%;
      border: ${config.borderWidth}px solid #333;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(0, 0, 0, 0.1);
      pointer-events: none;
      z-index: 2147483647;
      display: none;
      overflow: hidden;
      background: white;
    `;

    // 创建放大镜内容容器（用于显示放大的页面内容）
    magnifierLens = document.createElement('div');
    magnifierLens.id = 'page-magnifier-lens';
    magnifierLens.style.cssText = `
      position: absolute;
      width: 100%;
      height: 100%;
      transform-origin: 0 0;
    `;

    magnifier.appendChild(magnifierLens);
    document.body.appendChild(magnifier);
  }

  // 移除放大镜
  function removeMagnifier() {
    if (magnifier && magnifier.parentNode) {
      magnifier.parentNode.removeChild(magnifier);
      magnifier = null;
      magnifierLens = null;
    }
  }

  // 更新放大镜位置和内容
  function updateMagnifier(e) {
    if (!config.isActive || !magnifier || !magnifierLens) return;

    const mouseX = e.clientX;
    const mouseY = e.clientY;

    // 设置放大镜位置（中心跟随鼠标）
    const magnifierX = mouseX - config.magnifierSize / 2;
    const magnifierY = mouseY - config.magnifierSize / 2;

    magnifier.style.left = magnifierX + 'px';
    magnifier.style.top = magnifierY + 'px';
    magnifier.style.display = 'block';

    // 计算要放大的源区域大小
    const sourceSize = config.magnifierSize / config.zoomLevel;

    // 计算源区域的左上角位置（鼠标为中心）
    const sourceX = mouseX - sourceSize / 2;
    const sourceY = mouseY - sourceSize / 2;

    // 使用 transform 来实现放大效果
    // 1. 缩放页面内容
    // 2. 平移使得鼠标位置的内容显示在放大镜中心
    const translateX = -sourceX * config.zoomLevel;
    const translateY = -sourceY * config.zoomLevel;

    magnifierLens.style.transform = `scale(${config.zoomLevel}) translate(${translateX / config.zoomLevel}px, ${translateY / config.zoomLevel}px)`;

    // 复制页面内容到放大镜中
    updateLensContent();
  }

  // 更新放大镜镜头内容
  let lastUpdateTime = 0;
  const updateInterval = 50; // 限制更新频率为20fps，避免性能问题

  function updateLensContent() {
    const now = Date.now();
    if (now - lastUpdateTime < updateInterval) {
      return;
    }
    lastUpdateTime = now;

    // 清空之前的内容
    if (magnifierLens.children.length === 0) {
      // 创建一个克隆的文档内容
      // 我们使用一个技巧：通过CSS来显示页面的镜像
      const clonedContent = document.body.cloneNode(true);

      // 移除克隆内容中的放大镜元素，避免递归
      const magnifierClone = clonedContent.querySelector('#page-magnifier');
      if (magnifierClone) {
        magnifierClone.remove();
      }

      // 清空lens并添加克隆内容
      magnifierLens.innerHTML = '';
      magnifierLens.appendChild(clonedContent);
    }
  }

  // 使用更高效的方法：通过背景层克隆实现
  function createMagnifierEfficient() {
    // 创建放大镜容器
    magnifier = document.createElement('div');
    magnifier.id = 'page-magnifier';

    // 创建用于显示放大内容的iframe（更好的隔离）
    const magnifierContent = document.createElement('div');
    magnifierContent.className = 'magnifier-content';

    magnifier.appendChild(magnifierContent);
    document.body.appendChild(magnifier);

    magnifierLens = magnifierContent;
  }

  // 使用CSS实现的高效放大镜更新
  function updateMagnifierEfficient(e) {
    if (!config.isActive || !magnifier) return;

    const mouseX = e.clientX;
    const mouseY = e.clientY;

    // 放大镜位置
    magnifier.style.left = (mouseX - config.magnifierSize / 2) + 'px';
    magnifier.style.top = (mouseY - config.magnifierSize / 2) + 'px';
    magnifier.style.display = 'block';

    // 计算背景位置
    const zoom = config.zoomLevel;
    const bgX = -mouseX * zoom + config.magnifierSize / 2;
    const bgY = -mouseY * zoom + config.magnifierSize / 2;

    // 更新放大镜样式
    magnifier.style.cssText = `
      position: fixed;
      left: ${mouseX - config.magnifierSize / 2}px;
      top: ${mouseY - config.magnifierSize / 2}px;
      width: ${config.magnifierSize}px;
      height: ${config.magnifierSize}px;
      border-radius: 50%;
      border: ${config.borderWidth}px solid #333;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(255, 255, 255, 0.1);
      pointer-events: none;
      z-index: 2147483647;
      display: block;
      overflow: hidden;
      background: white;
      background-image: var(--page-screenshot);
      background-position: ${bgX}px ${bgY}px;
      background-size: ${document.documentElement.scrollWidth * zoom}px ${document.documentElement.scrollHeight * zoom}px;
      background-repeat: no-repeat;
    `;
  }

  // 重新实现：使用绝对定位和缩放
  function createMagnifierV2() {
    // 创建放大镜外层容器
    magnifier = document.createElement('div');
    magnifier.id = 'page-magnifier';

    // 创建内层容器，用于放大内容
    magnifierLens = document.createElement('div');
    magnifierLens.id = 'page-magnifier-lens';

    magnifier.appendChild(magnifierLens);

    // 添加到body，但不是body的子元素，而是添加到html
    // 这样可以避免一些样式继承问题
    if (document.body) {
      document.body.appendChild(magnifier);
    } else {
      document.documentElement.appendChild(magnifier);
    }

    // 应用样式
    updateMagnifierStyles();
  }

  // 更新放大镜样式
  function updateMagnifierStyles() {
    if (!magnifier) return;

    magnifier.style.cssText = `
      position: fixed;
      width: ${config.magnifierSize}px;
      height: ${config.magnifierSize}px;
      border-radius: 50%;
      border: ${config.borderWidth}px solid #333;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.5), inset 0 0 8px rgba(255, 255, 255, 0.2);
      pointer-events: none;
      z-index: 2147483647;
      display: none;
      overflow: hidden;
      background: white;
    `;

    if (magnifierLens) {
      magnifierLens.style.cssText = `
        position: absolute;
        left: 0;
        top: 0;
        width: 100vw;
        height: 100vh;
        transform-origin: 0 0;
        pointer-events: none;
      `;
    }
  }

  // 更新放大镜 V2
  function updateMagnifierV2(e) {
    if (!config.isActive || !magnifier || !magnifierLens) return;

    const mouseX = e.clientX;
    const mouseY = e.clientY;

    // 放大镜位置
    magnifier.style.left = (mouseX - config.magnifierSize / 2) + 'px';
    magnifier.style.top = (mouseY - config.magnifierSize / 2) + 'px';
    magnifier.style.display = 'block';

    // 计算缩放和平移
    const zoom = config.zoomLevel;

    // 计算需要平移的距离，使得鼠标位置显示在放大镜中心
    const translateX = -mouseX * zoom + config.magnifierSize / 2;
    const translateY = -mouseY * zoom + config.magnifierSize / 2;

    // 应用变换
    magnifierLens.style.transform = `scale(${zoom}) translate(${translateX / zoom}px, ${translateY / zoom}px)`;

    // 同步页面内容
    syncPageContent();
  }

  // 同步页面内容到放大镜
  function syncPageContent() {
    if (!magnifierLens) return;

    // 只在第一次或内容改变时更新
    if (magnifierLens.children.length === 0 || needsUpdate) {
      requestAnimationFrame(() => {
        // 克隆整个HTML元素
        const htmlClone = document.documentElement.cloneNode(true);

        // 移除克隆中的放大镜本身
        const magnifierInClone = htmlClone.querySelector('#page-magnifier');
        if (magnifierInClone) {
          magnifierInClone.remove();
        }

        // 移除克隆中的script标签，避免执行
        const scripts = htmlClone.querySelectorAll('script');
        scripts.forEach(script => script.remove());

        // 清空并添加新内容
        magnifierLens.innerHTML = '';

        // 只克隆body内容
        const bodyClone = htmlClone.querySelector('body');
        if (bodyClone) {
          // 移除body clone中的放大镜
          const magInBody = bodyClone.querySelector('#page-magnifier');
          if (magInBody) {
            magInBody.remove();
          }

          magnifierLens.appendChild(bodyClone);
        }

        needsUpdate = false;
      });
    }
  }

  let needsUpdate = true;

  // 激活放大镜
  function activateMagnifier() {
    if (!magnifier) {
      createMagnifierV2();
    }
    config.isActive = true;
    needsUpdate = true; // 标记需要更新内容
    if (magnifier) {
      magnifier.style.display = 'block';
    }
  }

  // 停用放大镜
  function deactivateMagnifier() {
    config.isActive = false;
    if (magnifier) {
      magnifier.style.display = 'none';
    }
  }

  // 切换放大镜状态
  function toggleMagnifier() {
    if (config.isActive) {
      deactivateMagnifier();
    } else {
      activateMagnifier();
    }
    return config.isActive;
  }

  // 监听鼠标移动事件
  document.addEventListener('mousemove', updateMagnifierV2);

  // 监听页面变化，标记需要更新
  const observer = new MutationObserver(() => {
    if (config.isActive) {
      needsUpdate = true;
    }
  });

  // 开始观察DOM变化
  if (document.body) {
    observer.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true,
      characterData: true
    });
  }

  // 监听来自popup的消息
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'toggleMagnifier') {
      const isActive = toggleMagnifier();
      sendResponse({ isActive: isActive });
    } else if (request.action === 'getMagnifierState') {
      sendResponse({ isActive: config.isActive });
    } else if (request.action === 'setZoomLevel') {
      config.zoomLevel = request.zoomLevel;
      sendResponse({ success: true });
    } else if (request.action === 'setMagnifierSize') {
      config.magnifierSize = request.size;
      if (magnifier) {
        updateMagnifierStyles();
      }
      sendResponse({ success: true });
    }
    return true; // 保持消息通道开启
  });

  // 键盘快捷键：按 Alt+M 切换放大镜
  document.addEventListener('keydown', (e) => {
    if (e.altKey && e.key === 'm') {
      e.preventDefault();
      toggleMagnifier();
    }
  });

  console.log('网页放大镜已加载！按 Alt+M 或点击扩展图标来切换放大镜。');
})();
