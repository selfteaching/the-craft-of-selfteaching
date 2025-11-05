// Popup 控制脚本
document.addEventListener('DOMContentLoaded', function() {
  const toggleBtn = document.getElementById('toggleBtn');
  const zoomSlider = document.getElementById('zoomSlider');
  const sizeSlider = document.getElementById('sizeSlider');
  const zoomValue = document.getElementById('zoomValue');
  const sizeValue = document.getElementById('sizeValue');
  const statusDiv = document.getElementById('status');

  let contentScriptReady = false;

  // 更新UI状态
  function updateUI(isActive, message) {
    if (message) {
      statusDiv.textContent = message;
      statusDiv.className = 'status inactive';
      toggleBtn.disabled = true;
      return;
    }

    toggleBtn.disabled = false;
    if (isActive) {
      toggleBtn.textContent = '关闭放大镜';
      toggleBtn.classList.add('active');
      statusDiv.textContent = '状态：已激活';
      statusDiv.className = 'status active';
    } else {
      toggleBtn.textContent = '启动放大镜';
      toggleBtn.classList.remove('active');
      statusDiv.textContent = '状态：未激活';
      statusDiv.className = 'status inactive';
    }
  }

  // 检查页面URL是否支持content script
  function isValidPage(url) {
    if (!url) return false;
    // Chrome 扩展无法在这些页面上运行
    const invalidProtocols = ['chrome://', 'chrome-extension://', 'edge://', 'about:', 'view-source:'];
    return !invalidProtocols.some(protocol => url.startsWith(protocol));
  }

  // 向当前标签页发送消息（带错误处理）
  function sendMessageToCurrentTab(message, callback) {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      if (!tabs[0]) {
        console.error('没有找到活动标签页');
        if (callback) callback(null);
        return;
      }

      const tab = tabs[0];

      // 检查是否是有效的页面
      if (!isValidPage(tab.url)) {
        console.warn('当前页面不支持扩展:', tab.url);
        updateUI(false, '此页面不支持扩展');
        if (callback) callback(null);
        return;
      }

      // 发送消息
      chrome.tabs.sendMessage(tab.id, message, function(response) {
        // 检查是否有错误
        if (chrome.runtime.lastError) {
          console.error('消息发送错误:', chrome.runtime.lastError.message);

          // 如果是连接错误，尝试注入脚本
          if (chrome.runtime.lastError.message.includes('Receiving end does not exist')) {
            console.log('Content script 未加载，尝试刷新页面或重新加载扩展');
            updateUI(false, '请刷新页面后重试');
            contentScriptReady = false;
          }

          if (callback) callback(null);
          return;
        }

        // 成功接收到响应
        contentScriptReady = true;
        if (callback) callback(response);
      });
    });
  }

  // 初始化：获取当前放大镜状态
  function initialize() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      if (!tabs[0]) return;

      // 检查页面类型
      if (!isValidPage(tabs[0].url)) {
        updateUI(false, '此页面不支持扩展');
        return;
      }

      // 尝试获取状态
      sendMessageToCurrentTab({ action: 'getMagnifierState' }, function(response) {
        if (response) {
          updateUI(response.isActive);
          contentScriptReady = true;
        } else {
          updateUI(false, '等待页面加载...');
          // 延迟重试
          setTimeout(function() {
            sendMessageToCurrentTab({ action: 'getMagnifierState' }, function(response) {
              if (response) {
                updateUI(response.isActive);
                contentScriptReady = true;
              } else {
                updateUI(false, '请刷新页面后重试');
              }
            });
          }, 500);
        }
      });
    });
  }

  // 启动初始化
  initialize();

  // 切换放大镜按钮
  toggleBtn.addEventListener('click', function() {
    if (!contentScriptReady) {
      updateUI(false, '请刷新页面后重试');
      return;
    }

    sendMessageToCurrentTab({ action: 'toggleMagnifier' }, function(response) {
      if (response) {
        updateUI(response.isActive);
      }
    });
  });

  // 放大倍数滑块
  zoomSlider.addEventListener('input', function() {
    const value = parseFloat(this.value);
    zoomValue.textContent = value + 'x';
  });

  zoomSlider.addEventListener('change', function() {
    const value = parseFloat(this.value);
    if (!contentScriptReady) return;

    sendMessageToCurrentTab({
      action: 'setZoomLevel',
      zoomLevel: value
    }, function(response) {
      if (response && response.success) {
        console.log('放大倍数已更新:', value);
      }
    });
  });

  // 放大镜大小滑块
  sizeSlider.addEventListener('input', function() {
    const value = parseInt(this.value);
    sizeValue.textContent = value + 'px';
  });

  sizeSlider.addEventListener('change', function() {
    const value = parseInt(this.value);
    if (!contentScriptReady) return;

    sendMessageToCurrentTab({
      action: 'setMagnifierSize',
      size: value
    }, function(response) {
      if (response && response.success) {
        console.log('放大镜大小已更新:', value);
      }
    });
  });

  // 监听来自content script的状态更新
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'magnifierStateChanged') {
      updateUI(request.isActive);
    }
  });
});
