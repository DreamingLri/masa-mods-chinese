# masa-mods-chinese
一个`masa mods`的汉化资源包，包括 `itemscroller` `litematica` `malilib` `minihud` `tweakeroo` `syncmatica` `litematica-printer`模组的汉化

[![Crowdin](https://badges.crowdin.net/masa-mod-chinese/localized.svg)](https://crowdin.com)

原作者: 

[醉梦巅峰](mailto:893136473@qq.com) - [B站](https://space.bilibili.com/13205801) 

[新兵Sinbing](https://github.com/Sinbing) - [B站](https://space.bilibili.com/1446187)

## 简介

> [!IMPORTANT]
> 本汉化为个人汉化版本，并非官方汉化

由于醉梦巅峰不再进行`masa mods`1.21版本之后的汉化，本人进行了原本汉化的重构，以适应 1.21 [Sakura Ryoko](https://github.com/sakura-ryoko) 版本的`masa mods`

如果您想查看醉梦巅峰1.20.1版本的汉化，请点击[这里](https://github.com/DreamingLri/masa-mods-chinese/tree/1.20)

> [!WARNING]  
> 本汉化包只适配了1.21 [Sakura Ryoko](https://github.com/sakura-ryoko) **最新版本**的`masa mods`，并不能保证此汉化包能够正常应用在低于1.21的mod中
> 
> 有汉化错误多半是因为您没有更新模组和汉化包到最新版（

## 如何使用

从[Release](https://github.com/DreamingLri/masa-mods-chinese/releases)下载最新版本汉化包，之后将汉化包放入`resourcepacks`文件夹中即可使用，记得在资源包里面启用这个（

> [!NOTE]
> `masa-mod-chinese.zip`是含有中英文对照的翻译格式
>
> `masa-mod-chinese-new.zip`是只含有中文的翻译格式，非常适合搭配[tweakermore](https://github.com/Fallen-Breath/tweakermore)模组的`applyTweakerMoreOptionLabelGlobally`功能使用

如果您想体验**最新**~~最不稳定~~的汉化更新：

1. 将本项目clone到本地 - `git clone https://github.com/DreamingLri/masa-mods-chinese.git`
2. pip安装`hjson`包 - `pip install hjson`
3. 运行`generate.py`文件即可获得资源包 - `python generate.py`
4. 运行`rename.py`即可重命名资源包 - `python rename.py`

## Release版本说明

`1.1.x` 为修改翻译错误或新增翻译内容的小更新

`1.x.1` 为正常翻译的更新，通常为更换翻译格式或进行大范围翻新

`x.1.1` 为跟随mc大版本更新的大更新(例如1.20、1.21)

## 结语

感谢 [醉梦巅峰](mailto:893136473@qq.com) 和 [新兵Sinbing](https://github.com/Sinbing) 对masa mods汉化的贡献

如果您发现任何汉化错误，欢迎提交[issue](https://github.com/DreamingLri/masa-mods-chinese/issues/new)