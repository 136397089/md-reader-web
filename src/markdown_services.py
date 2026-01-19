# -*- coding: utf-8 -*-
# markdown_services.py

import os
import re
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.util import AtomicString
import xml.etree.ElementTree as etree

def process_markdown_images(html_content, file_path):
    """处理Markdown中的图片链接，转换为安全的API链接"""
    if not file_path:
        return html_content
    
    # 获取文件所在目录
    file_dir = os.path.dirname(file_path)
    
    # 匹配img标签
    img_pattern = r'<img([^>]*?)src=[\'"](.*?)[\'"]([^>]*?)>'
    
    def replace_img(match):
        pre_attrs = match.group(1)
        src = match.group(2)
        post_attrs = match.group(3)
        
        # 跳过网络图片和data:协议图片
        if src.startswith(('http://', 'https://', 'data:')):
            return match.group(0)
        
        # 跳过绝对路径
        if src.startswith('/'):
            return match.group(0)
        
        # 构建相对于Markdown文件的图片路径
        if file_dir:
            image_path = os.path.join(file_dir, src).replace('\\', '/')
        else:
            image_path = src
        
        # 构建新的API链接
        new_src = f'/api/image?path={image_path}'
        
        return f'<img{pre_attrs}src="{new_src}"{post_attrs}>'
    
    return re.sub(img_pattern, replace_img, html_content)


class MathInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('span')
        el.text = AtomicString(f"${m.group(1)}$")
        el.set('class', 'math-inline')
        return el, m.start(0), m.end(0)

class MathBlockProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('div')
        el.text = AtomicString(f"$${m.group(1)}$$")
        el.set('class', 'math-display')
        return el, m.start(0), m.end(0)

class MathExtension(Extension):
    def extendMarkdown(self, md):
        # 优先级设置：
        # backtick (代码块) 是 175
        # escape (转义) 是 180
        # 我们设置为 < 175，确保代码块先被处理
        
        # 块级公式 $$...$$
        # 使用[\s\S]匹配任意字符包括换行符
        md.inlinePatterns.register(MathBlockProcessor(r'\$\$([\s\S]+?)\$\$', md), 'math_block', 174)
        
        # 行内公式 $...$
        md.inlinePatterns.register(MathInlineProcessor(r'(?<!\\)\$(?!\$)([\s\S]+?)(?<!\\)\$', md), 'math_inline', 173)
