// Popup 控制脚本
document.addEventListener('DOMContentLoaded', function() {
  const toggleBtn = document.getElementById('toggleBtn');
  const zoomSlider = document.getElementById('zoomSlider');
  const sizeSlider = document.getElementById('sizeSlider');
  const zoomValue = document.getElementById('zoomValue');
  const sizeValue = document.getElementById('sizeValue');
  const statusDiv = document.getElementById('status');

  // 更新UI状态
  function updateUI(isActive) {
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

  // 向当前标签页发送消息
  function sendMessageToCurrentTab(message, callback) {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      if (tabs[0]) {
        chrome.tabs.sendMessage(tabs[0].id, message, callback);
      }
    });
  }

  // 获取当前放大镜状态
  sendMessageToCurrentTab({ action: 'getMagnifierState' }, function(response) {
    if (response) {
      updateUI(response.isActive);
    }
  });

  // 切换放大镜按钮
  toggleBtn.addEventListener('click', function() {
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
