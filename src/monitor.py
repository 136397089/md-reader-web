# -*- coding: utf-8 -*-
# monitor.py

import threading
import logging
import resource
import time

# 资源监控线程
class MonitorThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.running = True
        
    def run(self):
        logging.info("资源监控线程已启动")
        while self.running:
            try:
                # 获取内存使用情况 (RSS)
                usage = resource.getrusage(resource.RUSAGE_SELF)
                memory_mb = usage.ru_maxrss / 1024  # Linux下单位是KB
                
                # 获取当前活跃线程数
                thread_count = threading.active_count()
                
                logging.info(f"系统状态 - 内存: {memory_mb:.2f}MB, 线程数: {thread_count}")
                
                # 每60秒记录一次
                time.sleep(60)
            except Exception as e:
                logging.error(f"监控线程异常: {e}")
                time.sleep(60)
