#!/usr/bin/env python3
"""
生成 Chrome 扩展图标
使用 PIL (Pillow) 库创建放大镜图标
"""

try:
    from PIL import Image, ImageDraw
    import os

    def create_magnifier_icon(size):
        """创建放大镜图标"""
        # 创建带透明背景的图像
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # 计算尺寸
        padding = size // 8
        lens_size = size - 2 * padding

        # 放大镜圆形部分
        circle_left = padding
        circle_top = padding
        circle_right = padding + lens_size * 0.6
        circle_bottom = padding + lens_size * 0.6

        # 绘制外圆（边框）
        draw.ellipse(
            [circle_left, circle_top, circle_right, circle_bottom],
            outline=(102, 126, 234, 255),
            width=max(2, size // 32),
            fill=(255, 255, 255, 200)
        )

        # 绘制内圆
        inner_padding = size // 16
        draw.ellipse(
            [circle_left + inner_padding, circle_top + inner_padding,
             circle_right - inner_padding, circle_bottom - inner_padding],
            outline=(102, 126, 234, 180),
            width=max(1, size // 48)
        )

        # 绘制手柄
        handle_width = max(3, size // 16)
        handle_start_x = circle_right - size // 8
        handle_start_y = circle_bottom - size // 8
        handle_end_x = size - padding
        handle_end_y = size - padding

        draw.line(
            [handle_start_x, handle_start_y, handle_end_x, handle_end_y],
            fill=(102, 126, 234, 255),
            width=handle_width
        )

        # 绘制手柄末端的圆形装饰
        handle_circle_size = handle_width * 1.5
        draw.ellipse(
            [handle_end_x - handle_circle_size // 2,
             handle_end_y - handle_circle_size // 2,
             handle_end_x + handle_circle_size // 2,
             handle_end_y + handle_circle_size // 2],
            fill=(118, 75, 162, 255)
        )

        return img

    # 创建 icons 目录
    icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
    os.makedirs(icons_dir, exist_ok=True)

    # 生成不同尺寸的图标
    sizes = [16, 48, 128]
    for size in sizes:
        icon = create_magnifier_icon(size)
        icon_path = os.path.join(icons_dir, f'icon{size}.png')
        icon.save(icon_path, 'PNG')
        print(f'已生成图标: {icon_path}')

    print('\n所有图标生成完成！')

except ImportError:
    print('错误: 需要安装 Pillow 库')
    print('请运行: pip install Pillow')
    print('\n或者，你可以手动创建以下尺寸的图标:')
    print('- icons/icon16.png (16x16)')
    print('- icons/icon48.png (48x48)')
    print('- icons/icon128.png (128x128)')
