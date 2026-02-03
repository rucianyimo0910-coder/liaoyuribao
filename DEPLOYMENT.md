# 部署说明

## 本地运行

### 方法一：使用启动脚本（推荐）
```bash
cd healtherly-daily-report
bash start.sh
```

### 方法二：手动运行
```bash
cd healtherly-daily-report
npm install
npx serve ./public
```

### 方法三：使用 live-server（实时刷新）
```bash
cd healtherly-daily-report
npm install -g live-server
live-server ./public --port=3000
```

## 访问应用

启动后，您可以在浏览器中访问 `http://localhost:3000` 来查看应用。

## 部署到生产环境

### 静态托管服务（如 Netlify、Vercel、GitHub Pages）
只需将 `public` 目录中的文件上传到托管服务即可。

### 云服务器部署
1. 将整个项目上传到服务器
2. 安装 Node.js 和 npm
3. 运行 `npm install` 安装依赖
4. 运行 `npx serve ./public` 启动服务
5. （可选）使用 pm2 或 systemd 确保服务持续运行

### Docker 部署
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install -g serve
RUN npm install

COPY public/ ./public/

EXPOSE 3000

CMD ["serve", "-s", "public"]
```

## 生产环境配置建议

- 使用 Nginx 作为反向代理
- 配置 SSL 证书
- 设置适当的缓存策略
- 监控服务状态

## 故障排除

### 端口冲突
如果 3000 端口被占用，可以使用其他端口：
```bash
npx serve -l 3001 ./public
```

### 权限问题
确保有适当的文件读取权限：
```bash
chmod -R 755 ./public
```

### 依赖安装失败
清除 npm 缓存并重试：
```bash
npm cache clean --force
npm install
```

---

🌿 *愿每一个今天都是美好的一天* 🌿