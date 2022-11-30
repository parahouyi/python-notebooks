## adb commands
### start an activity
adb shell am start com.hypergryph.arknights/com.u8.sdk.U8UnityContext
### close an activity
adb shell am force-stop com.hypergryph.arknights
### adb tab, swipe
subprocess.Popen('adb shell am start com.hypergryph.arknights/com.u8.sdk.U8UnityContext', shell=True).wait()
adb shell input tap x y
adb shell input swipe x1 y1 x2 y2
adb shell input text "insert%stext%shere"              %s表示空格

1.手机USB线连接到PC端，并打开手机USB调试；
2.在CMD窗口输入:adb tcpip 5555；
3.可以断开USB数据线与PC端的连接；
4.在CMD窗口再输入:adb connect ip:5555 ,即可与PC端进行远程连接啦

python programming
import os
import subprocess
import time

一、ADB 简介

1什么是 ADB?

ADB 全称为 Android Debug Bridge，起到调试桥的作用，是一个客户端-服务器端程序。其中客户端是用来操作的电脑，服务端是 Android 设备。ADB 也是 Android SDK 中的一个工具，可以直接操作管理 Android 模拟器或者真实的 Android 设备。

2为什么要用 ADB?

ADB 可以直接操作管理手机模拟器或者真实的手机设备(如华为手机)。它的主要功能有：

运行设备的 shell(命令行)

管理模拟器或设备的端口映射

计算机和设备之间上传/下载文件

可以对设备的应用进行卸载安装等

在 App 遇到 ANR/Crash 等 bug 时，可以通过 ADB 来抓取日志

简而言之，ADB 就是连接 Android 手机与 PC 端的桥梁，可以让用户在电脑上对手机进行全面的操作！

二、ADB 命令详解

1基本指令
命令	adb version
含义	显示 adb 版本
操作	
命令	adb help
含义	帮助信息，查看 adb 所支持的所有命令
操作	
命令	adb start-server
含义	启动 adb 服务
操作	
命令	adb kill-server
含义	关闭 adb 服务
操作	
命令	adb devices
含义	用来查看当前连接的设备，已连接的设备会显示出来
操作	
命令	adb connect 设备号
含义	用来连接设备
操作	

2权限指令
命令	adb root
含义	获取 Android 管理员（root 用户）的权限
操作	
命令	adb shell
含义	登录设备-shell，这个命令将登录设备的 shell(内核)，登录 shell 后可以使用 cd、ls、rm 等 Linux 命令
操作	
命令	adb remount
含义	获取 System 分区可写权限，需要 root 后才能有这个权限
操作	

3apk 操作指令
命令	adb shell pm list packages
含义	显示所有包名
操作	
命令	adb shell pm list packages –s
含义	显示系统应用包名
操作	
命令	adb shell pm list packages -3
含义	显示第三方应用包名
操作	
命令	adb install <apk 文件路径 >
含义	将本地 apk 软件安装到设备上
操作	
命令	adb uninstall <apk 包名 >
含义	将设备上的 apk 卸载
操作	

4文件操作指令
命令	adb push < 本地路径 > < 手机端路径 >
含义	把本地的文件或文件夹复制到设备（手机）
操作	
命令	adb pull < 手机端文件 > < 本地路径 >
含义	把设备（手机）的文件或文件夹复制到本地
操作	

5日志操作指令
命令	adb logcat -v time > D:\logs\logcat.log
含义	输出实时日志并保存在本地文件，通过 Ctrl+C 来停止。抓取日志的步骤：先输入命令启动日志，然后操作 App，复现 bug，再 ctrl+c 停止日志，分析本地保存的文件
操作	
命令	adb bugreport >D:\logs\ bugreport.log
含义	输入指令后开始抓取 Log，不需要按 Ctrl+C 来停止，会自动化停止 Log 打印，并将日志文件保存在本地。抓取日志的步骤：主要抓取执行命令时往前 10 分钟左右的日志信息，所以在出现 bug 后立即采用此方法才有效，问题出现时间太长不建议使用此方法
操作	

6系统操作指令
命令	adb shell getprop ro.product.model
含义	获取设备型号
操作	
命令	adb shell getprop ro.build.version.release
含义	获取设备 Android 系统版本
操作	
命令	adb get-serialno
含义	获取设备的序列号（设备号）
操作	
命令	adb shell wm size
含义	获取设备屏幕分辨率
操作	
命令	adb shell screencap -p /sdcard/mms.png
含义	屏幕截图
操作	
命令	adb pull /sdcard/mms.png D:\app
含义	将截图导出到本地
操作	

adb shell dumpsys activity |find "mFocusedActivity" 查看前台应用包名，适用于 Android 7.0 以下，必须先启动 app

 

adb shell dumpsys activity |find "mResumedActivity" 查看前台应用包名，适用于 Android 8.0 以上，必须先启动 app


    dumpsys:
    dumpsys命令可以提供非常多的系统信息。可以通过adb shell service list来查看dumpsys能提供查询信息的服务，常用的有：

服务	类名	功能
activity	ActivityManagerService	AMS相关信息
package	PackageManagerService	PMS相关信息
window	WindowManagerService	WMS相关信息
input	InputManagerService	IMS相关信息
power	PowerManagerService	PMS相关信息
procstats	ProcessStatsService	进程统计
battery	BatteryService	电池信息
alarm	AlarmManagerService	闹钟信息
meminfo	MemBinder	内存

