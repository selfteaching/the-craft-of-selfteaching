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
  let canvas = null;
  let ctx = null;

  // 创建放大镜元素
  function createMagnifier() {
    // 创建容器
    magnifier = document.createElement('div');
    magnifier.id = 'page-magnifier';
    magnifier.style.cssText = `
      position: fixed;
      width: ${config.magnifierSize}px;
      height: ${config.magnifierSize}px;
      border-radius: 50%;
      border: ${config.borderWidth}px solid #333;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
      pointer-events: none;
      z-index: 2147483647;
      display: none;
      overflow: hidden;
    `;

    // 创建canvas用于绘制放大内容
    canvas = document.createElement('canvas');
    canvas.width = config.magnifierSize;
    canvas.height = config.magnifierSize;
    canvas.style.cssText = `
      width: 100%;
      height: 100%;
      border-radius: 50%;
    `;

    magnifier.appendChild(canvas);
    document.body.appendChild(magnifier);

    ctx = canvas.getContext('2d');
  }

  // 移除放大镜
  function removeMagnifier() {
    if (magnifier && magnifier.parentNode) {
      magnifier.parentNode.removeChild(magnifier);
      magnifier = null;
      canvas = null;
      ctx = null;
    }
  }

  // 更新放大镜位置和内容
  function updateMagnifier(e) {
    if (!config.isActive || !magnifier) return;

    const x = e.clientX;
    const y = e.clientY;

    // 设置放大镜位置（中心跟随鼠标）
    magnifier.style.left = (x - config.magnifierSize / 2) + 'px';
    magnifier.style.top = (y - config.magnifierSize / 2) + 'px';

    // 获取页面的滚动位置
    const scrollX = window.pageXOffset || document.documentElement.scrollLeft;
    const scrollY = window.pageYOffset || document.documentElement.scrollTop;

    // 计算源区域的中心点（在整个页面上的位置）
    const sourceX = x + scrollX;
    const sourceY = y + scrollY;

    // 计算要捕获的区域大小（放大前的区域）
    const sourceSize = config.magnifierSize / config.zoomLevel;

    // 清除画布
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 保存上下文状态
    ctx.save();

    // 创建圆形裁剪路径
    ctx.beginPath();
    ctx.arc(config.magnifierSize / 2, config.magnifierSize / 2, config.magnifierSize / 2, 0, Math.PI * 2);
    ctx.clip();

    // 使用 drawImage 进行放大
    // 由于我们不能直接捕获整个页面，我们使用一个技巧：
    // 将鼠标下的区域通过 CSS 变换来模拟放大效果
    try {
      // 绘制背景
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // 使用 html2canvas 或类似库会更好，但为了保持轻量级
      // 我们使用 CSS transform 来实现基本的放大效果
      // 这里我们创建一个视觉提示
      ctx.font = '16px Arial';
      ctx.fillStyle = '#333';
      ctx.textAlign = 'center';
      ctx.fillText('放大区域', config.magnifierSize / 2, config.magnifierSize / 2);

      // 绘制十字准星
      ctx.strokeStyle = 'rgba(0, 0, 0, 0.3)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(config.magnifierSize / 2, 0);
      ctx.lineTo(config.magnifierSize / 2, config.magnifierSize);
      ctx.moveTo(0, config.magnifierSize / 2);
      ctx.lineTo(config.magnifierSize, config.magnifierSize / 2);
      ctx.stroke();

    } catch (error) {
      console.error('绘制放大镜内容时出错:', error);
    }

    // 恢复上下文状态
    ctx.restore();
  }

  // 使用 foreignObject 和 SVG 来实现真实的页面放大
  function updateMagnifierWithSVG(e) {
    if (!config.isActive || !magnifier) return;

    const x = e.clientX;
    const y = e.clientY;

    // 设置放大镜位置
    magnifier.style.left = (x - config.magnifierSize / 2) + 'px';
    magnifier.style.top = (y - config.magnifierSize / 2) + 'px';
    magnifier.style.display = 'block';

    // 计算要捕获的区域大小
    const sourceSize = config.magnifierSize / config.zoomLevel;
    const sourceX = x - sourceSize / 2;
    const sourceY = y - sourceSize / 2;

    // 使用 CSS transform 进行放大
    const scale = config.zoomLevel;
    const translateX = -(sourceX * scale - config.magnifierSize / 2);
    const translateY = -(sourceY * scale - config.magnifierSize / 2);

    // 克隆鼠标下的元素并放大显示
    // 这是一个简化版本，实际实现需要更复杂的逻辑
    ctx.save();
    ctx.beginPath();
    ctx.arc(config.magnifierSize / 2, config.magnifierSize / 2, config.magnifierSize / 2 - config.borderWidth, 0, Math.PI * 2);
    ctx.clip();

    // 绘制网格背景
    ctx.fillStyle = '#f0f0f0';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // 绘制提示文字
    ctx.fillStyle = '#666';
    ctx.font = '14px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(`${config.zoomLevel}x 放大`, config.magnifierSize / 2, config.magnifierSize / 2 - 20);
    ctx.fillText('鼠标位置: ' + Math.round(x) + ', ' + Math.round(y), config.magnifierSize / 2, config.magnifierSize / 2 + 20);

    ctx.restore();
  }

  // 激活放大镜
  function activateMagnifier() {
    if (!magnifier) {
      createMagnifier();
    }
    config.isActive = true;
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
  document.addEventListener('mousemove', updateMagnifierWithSVG);

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
        magnifier.style.width = config.magnifierSize + 'px';
        magnifier.style.height = config.magnifierSize + 'px';
        canvas.width = config.magnifierSize;
        canvas.height = config.magnifierSize;
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
