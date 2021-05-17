#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib.error
import urllib.parse
import json


# import easygui as g
300776290

def get_all_hotSong():  # 获取热歌榜所有歌曲名称和id
    url = 'http://music.163.com/discover/toplist?id=3778678'  # 网易云云音乐热歌榜url
    url1 = 'http://music.163.com/song/media/outer/url?id=436514312.mp3'
    header = {  # 请求头部
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36 '
    }
    request = urllib.request.Request(url=url, headers=header)
    html = urllib.request.urlopen(request).read().decode('utf8')  # 打开url
    html = str(html)  # 转换成str
    pat1 = r'<ul class="f-hide"><li><a href="/song\?id=\d*?">.*</a></li></ul>'  # 进行第一次筛选的正则表达式
    result = re.compile(pat1).findall(html)  # 用正则表达式进行筛选
    result = result[0]  # 获取tuple的第一个元素

    pat2 = r'<li><a href="/song\?id=\d*?">(.*?)</a></li>'  # 进行歌名筛选的正则表达式
    pat3 = r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'  # 进行歌ID筛选的正则表达式
    hot_song_name = re.compile(pat2).findall(result)  # 获取所有热门歌曲名称
    hot_song_id = re.compile(pat3).findall(result)  # 获取所有热门歌曲对应的Id

    return hot_song_name, hot_song_id


def get_hotComments(hot_song_name, hot_song_id):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + hot_song_id + '?csrf_token='  # 歌评url
    header = {  # 请求头部
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    # post请求表单数据
    data = {
        'params': 'zC7fzWBKxxsm6TZ3PiRjd056g9iGHtbtc8vjTpBXshKIboaPnUyAXKze+KNi9QiEz/IieyRnZfNztp7yvTFyBXOlVQP/JdYNZw2+GRQDg7grOR2ZjroqoOU2z0TNhy+qDHKSV8ZXOnxUF93w3DA51ADDQHB0IngL+v6N8KthdVZeZBe0d3EsUFS8ZJltNRUJ',
        'encSecKey': '4801507e42c326dfc6b50539395a4fe417594f7cf122cf3d061d1447372ba3aa804541a8ae3b3811c081eb0f2b71827850af59af411a10a1795f7a16a5189d163bc9f67b3d1907f5e6fac652f7ef66e5a1f12d6949be851fcf4f39a0c2379580a040dc53b306d5c807bf313cc0e8f39bf7d35de691c497cda1d436b808549acc'}
    postdata = urllib.parse.urlencode(data).encode('utf8')  # 进行编码
    request = urllib.request.Request(url, headers=header, data=postdata)
    reponse = urllib.request.urlopen(request).read().decode('utf8')
    json_dict = json.loads(reponse)  # 获取json
    hot_commit = json_dict['hotComments']  # 获取json中的热门评论

    num = 0
    # fhandle = open('./song_comments', 'a')  # 写入文件
    fhandle = open('song_comment.txt', 'a', encoding='UTF8')  # 写入文件
    fhandle.write('唐国毅编译\n')
    fhandle.write(hot_song_name + ':' + '\n')

    for item in hot_commit:
        num += 1
        fhandle.write(str(num) + '.' + item['content'] + '\n')
    fhandle.write('\n==============================================\n\n')
    fhandle.close()


def cut1():  # 把歌曲文件单独分割保存模块
    song_name_tem = 'none'  # 避免未声明先引用情况
    f = open('song_comment.txt', encoding='UTF-8')
    song_lyric = []
    for each_line in f:
        if each_line[:6] != '======':
            if ':' in each_line:
                (song_name_tem, none1) = each_line.split(':', 1)
                song_lyric.extend(each_line)
                # print(type(song_name_tem))
            else:
                song_lyric.extend(each_line)
        else:
            song_name = str(song_name_tem) + '.txt'
            song_lyric_file = open(song_name, 'w', encoding='UTF-8')
            song_lyric_file.writelines(song_lyric)
            song_lyric = []
    f.close()


def star_fun(input_num):  # 执行最开始爬的大文件
    num = 0
    # while num < len(hot_song_name):  # 保存所有热歌榜中的热评
    while num < input_num:
        print('正在抓取第%d首歌曲热评...' % (num + 1))
        get_hotComments(hot_song_name[num], hot_song_id[num])
        print('第%d首歌曲热评抓取成功' % (num + 1))
        num += 1


def cut():
    fhandle = open('./song_comment.txt', 'a', encoding='UTF8')  # 写入文件
    fhandle.write('唐国毅编译')
    global hot_song_name, hot_song_id
    hot_song_name, hot_song_id = get_all_hotSong()  # 获取热歌榜所有歌曲名称和id

    list_1 = list(range(1, 201))
    str_1 = str(list_1)
    input_str = input('你想获取多少热歌榜单的歌曲热评（请输入1-200的整数）：')  # 输入需要爬多少歌曲
    while (input_str.isdigit() != True) or (input_str not in str_1):
        input_str = input('请再次输入1-200的整数，是1-200整数喔！：')
    input_num = int(input_str)

    input_cut1 = input('是否需要把歌曲文件单独分割保存当前文件夹下（Y/N）:')
    cut1_str = ['Y', 'N', 'y', 'n']
    while input_cut1 not in cut1_str:
        input_cut1 = input('请勿输入其他字符！是否需要把歌曲文件单独分割保存（Y/N）:')
    if input_cut1 == 'Y' or input_cut1 == 'y':
        star_fun(input_num)
        cut1()
    elif input_cut1 == 'N' or input_cut1 == 'n':
        star_fun(input_num)####


cut()#开始运行
