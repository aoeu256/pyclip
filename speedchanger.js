var speedRate = 1.25; // 保存当前视频速度的变量
var savedSpeed = 1.25;

document.addEventListener('keydown', function(event) {
    if (event.key === '`') { // 检查是否按下了反引号键
        const videos = document.querySelectorAll('video'); // 获取页面中的所有视频元素
        videos.forEach(video => {
            if (!video.paused) { // 检查视频是否正在播放
                savedSpeed = video.playbackRate; // 将当前视频速度保存在变量中
                video.playbackRate = 5; // 将视频速度设置为5倍速
            }
        });
    }
});

document.addEventListener('keyup', function(event) {
    if (event.key === '`') { // 检查是否释放了反引号键
        const videos = document.querySelectorAll('video'); // 获取页面中的所有视频元素
        videos.forEach(video => {
            if (!video.paused) { // 检查视频是否正在播放
                video.playbackRate = speedRate; // 将视频速度恢复为保存的速度
            }
        });
    }
});