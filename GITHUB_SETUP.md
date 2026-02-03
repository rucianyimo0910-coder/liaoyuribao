# GitHub 推送说明

要将此项目推送到您的 GitHub 账户，请按照以下步骤操作：

## 1. 在 GitHub 上创建新仓库
1. 登录到您的 GitHub 账户
2. 点击 "New repository" 按钮
3. 输入仓库名称，例如 "healtherly-daily-report"
4. 选择 "Public" 或 "Private"
5. 不要勾选 "Initialize this repository with a README"
6. 点击 "Create repository"

## 2. 配置远程仓库
在您的终端中运行以下命令（将下面的 URL 替换为您自己的仓库地址）：

```bash
cd healtherly-daily-report
git remote add origin https://github.com/YOUR_USERNAME/healtherly-daily-report.git
```

## 3. 推送到 GitHub
```bash
git branch -M main
git push -u origin main
```

## 4. 如果需要使用 SSH 方式（推荐）
如果您设置了 SSH 密钥，可以使用：

```bash
git remote set-url origin git@github.com:YOUR_USERNAME/healtherly-daily-report.git
git push -u origin main
```

## 5. 如果您需要使用个人访问令牌
如果 GitHub 不允许密码认证，请创建个人访问令牌并使用它代替密码：

1. 前往 GitHub Settings > Developer settings > Personal access tokens
2. 点击 "Generate new token"
3. 选择适当的权限
4. 使用令牌作为密码进行身份验证

## 注意事项
- 请将 `YOUR_USERNAME` 替换为您的实际 GitHub 用户名
- 如果您尚未配置 Git 凭据助手，每次推送时可能需要输入用户名和密码（或令牌）
- 如果您使用的是私有仓库，请确保您有适当的访问权限

---

完成以上步骤后，您的项目就会成功推送到 GitHub！