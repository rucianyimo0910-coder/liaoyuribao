# 创建 GitHub 仓库说明

要完成项目的部署，您需要先在 GitHub 上创建一个仓库。

## 步骤 1: 创建新仓库

1. 打开浏览器，访问 https://github.com/new
2. 登录您的 GitHub 账户 (rucianyimo0910-coder)
3. 在 "Repository name" 中输入: `healtherly-daily-report`
4. 选择 "Public" (或 "Private" 如果您希望私有)
5. **不要** 勾选 "Initialize this repository with a README"
6. **不要** 勾选 "Add a main branch protection rule"
7. 点击 "Create repository" 按钮

## 步骤 2: 验证仓库创建

仓库创建后，页面会跳转到仓库主页，URL 应该是：
`https://github.com/rucianyimo0910-coder/healtherly-daily-report`

## 步骤 3: 推送代码

仓库创建完成后，回到终端并运行以下命令来推送代码：

```bash
cd ~/workspace/healtherly-daily-report
git push -u origin main
```

或者运行部署脚本：

```bash
cd ~/workspace/healtherly-daily-report
./setup_and_deploy.sh
```

## 替代方案: 使用 GitHub CLI

如果您安装了 GitHub CLI，也可以使用以下命令创建仓库：

```bash
gh repo create healtherly-daily-report --public --description "身心灵疗愈日报 - 每日正能量内容展示平台"
```

## 注意事项

- 仓库名称必须与上面指定的完全一致
- 不要在创建时初始化 README、.gitignore 或 license，因为我们要推送现有内容
- 确保您的 SSH 密钥 (github_deploy_key) 已添加到您的 GitHub 账户

一旦仓库创建成功，您就可以推送项目代码了！

---

完成这些步骤后，您的身心灵疗愈日报项目就会成功部署到 GitHub！