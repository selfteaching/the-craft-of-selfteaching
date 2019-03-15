# Github进行fork后如何与原仓库同步

实在是……有太多人同时在帮忙修订错别字或优化 `the-craft-of-selfteaching` 了。如果你在提交 pull request 后，得到老师回复说：“重新fork”，其实是你遇到一个问题：

> 在你fork之后，但 xiaolai 的仓库已经更新了；但 github 不会自动帮你把 xiaolai 的仓库 同步给你 fork 后的仓库。导致你提交pull request时的版本和 xiaolai 的版本不一致。

于是，你需要与原仓库同步。以下是傻瓜版操作步骤：

1、进入到本地仓库的目录，以下所有操作，都在你本地仓库的目录下操作。

比如我fork并clone到本地的目录为`/from-liujuanjuan-the-craft-of-selfteaching`

![image](https://user-images.githubusercontent.com/31027645/54422899-6938e880-474a-11e9-8768-27ac24673e28.png)


2、执行命令 `git remote -v` 查看你的远程仓库的路径：

![image](https://user-images.githubusercontent.com/31027645/54422975-95ed0000-474a-11e9-96bf-1018d6bc06f2.png)

3、执行命令 `git remote add upstream https://github.com/selfteaching/the-craft-of-selfteaching.git` 把 xiaolai 的仓库设置为你的上游代码库

这个命令执行后，没有任何返回信息；所以再次执行命令 `git remote -v` 检查是否成功

![image](https://user-images.githubusercontent.com/31027645/54423107-d8aed800-474a-11e9-9ab8-7bb901181283.png)

4、执行命令 `git fetch upstream` 抓取 xiaolai 原仓库的更新：

5、执行命令 `git checkout master` 切换到 master 分支：

6、执行命令 `git merge upsteam/master` 合并远程的master分支：

此时，你的本地仓库已经抓取到原仓库的修订了。但这将面临几种情况：

- 你的本地没有做过修改：OK，啥事儿也没有
- 你的本地做过修改，但幸运的是，与抓取到的原仓库修订没有冲突，那你本地修改仍被保留
- 你的本地做过修改，但糟糕的是，与原仓库修订产生了冲突……小心为妙，那还是删掉你fork的仓库，重新fork，重新clone到你的本地吧

7、把你本地仓库向你github上fork的仓库推送修改

执行命令 `git status` 检查哪些文件有变化

执行命令 `git add -A` 或者 `git add filename`添加所有或逐个添加

执行命令 `git commit -m "你的备注"` 提交

执行命令 `git push origin master` 把本地仓库推送到github上你fork的仓库

8、在你fork的仓库创建 pull request 



