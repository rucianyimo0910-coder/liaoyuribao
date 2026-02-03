# 部署指南：身心灵疗愈日报到 GitHub Pages

## 部署步骤

### 1. 创建 GitHub 仓库
1. 登录 GitHub
2. 点击 "New repository"
3. 输入仓库名称（如 `healtherly-daily-report`）
4. 选择 "Public" 或 "Private"
5. 不要勾选 "Initialize this repository with a README"
6. 点击 "Create repository"

### 2. 上传代码
```bash
# 将本地代码推送到新创建的仓库
git remote add origin <your-repository-url>
git branch -M main
git push -u origin main
```

### 3. 启用 GitHub Pages
有两种方式可以部署：

#### 方式一：手动部署（一次性）
1. 进入仓库的 `Settings` 选项卡
2. 在左侧菜单中找到 `Pages`
3. 在 `Source` 部分选择：
   - Branch: `main`
   - Folder: `/root` (或 `/(root)`，取决于你的 GitHub 界面)
4. 点击 `Save`

#### 方式二：自动部署（推荐）
此方式将自动每日更新日报。

1. 确保 `.github/workflows/deploy.yml` 文件存在（项目中已包含）
2. 进入仓库的 `Settings` 选项卡
3. 在左侧菜单中找到 `Pages`
4. 在 `Source` 部分选择：
   - Branch: `gh-pages`
   - Folder: `/(root)`
5. 点击 `Save`

### 4. 配置自动更新
如果选择方式二（自动部署），GitHub Actions 将按计划自动更新日报：

- 编辑 `.github/workflows/deploy.yml` 中的 cron 表达式来更改更新频率
- 当前设置为每天北京时间下午 4 点更新
- cron 表达式: `0 8 * * *` (UTC 时间 8 点 = 北京时间 16 点)

### 5. 查看部署结果
1. 部署完成后，你可以在仓库的 `Settings` -> `Pages` 部分找到访问 URL
2. URL 格式通常是：`https://<your-username>.github.io/<repository-name>/`

## 验证部署

1. 检查 Actions 状态：
   - 进入仓库的 `Actions` 选项卡
   - 确认工作流正在运行且无错误

2. 检查页面：
   - 访问 GitHub Pages URL
   - 确认页面正常显示且内容更新

## 自定义设置

### 更改更新时间
编辑 `.github/workflows/deploy.yml` 中的 cron 表达式：

```yaml
on:
  schedule:
    # 格式: 分 时 日 月 星期
    # 默认: 每天 UTC 8 点 (北京时间下午 4 点)
    - cron: '0 8 * * *'
```

### 添加更多数据源
编辑 `src/generate_report.py` 中的相关函数来添加更多内容源：

- `get_healing_news()` - 疗愈资讯
- `get_mental_health_info()` - 心理健康
- `get_natural_therapy_info()` - 自然疗法
- `get_meditation_info()` - 冥想内容
- `get_recommended_reading()` - 推荐阅读

## 故障排除

### 页面未更新
1. 检查 Actions 是否有错误
2. 确认 `public` 目录下有 `index.html` 文件
3. 验证 GitHub Pages 源设置是否正确

### Actions 运行失败
1. 检查 `.github/workflows/deploy.yml` 语法
2. 确认工作流未被禁用
3. 验证仓库具有适当的权限

### 内容不准确
1. 检查数据源 URL 是否有效
2. 更新 `requirements.txt` 中的依赖包版本
3. 修改抓取逻辑以适应目标网站的变化

## 维护建议

- 定期检查内容源的有效性
- 监控 GitHub Actions 运行状况
- 根据需要更新依赖包
- 按需调整页面样式和布局