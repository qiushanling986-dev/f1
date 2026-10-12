# F1 Live Hub

面向 F1 车迷的中文响应式赛事网站。黑红主题，支持 2020 年至当前年份的赛事日历、车手和车队积分、正赛结果、下一站倒计时。

## 快速运行（Windows）

安装 Python 后，在项目目录打开终端：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

访问 http://127.0.0.1:5000 。关闭终端即可停止服务。

也可以不安装 Flask：运行 `python -m http.server 8000 --directory dist` 后访问 http://localhost:8000 。

## 功能与数据

- 选择赛季；查看完整赛程及本地时区发车时间。
- 下一站倒计时，无发车时间时明确提示。
- 车手、车队积分榜，前五名概览与完整表格。
- 每站正赛赛果，未发布结果时显示空状态。
- 页面打开时每 5 分钟刷新，支持手动刷新。
- 网络失败时显示错误，不使用虚构积分或比赛数据。

数据直接来自 [Jolpica F1](https://github.com/jolpica/jolpica-f1) 的 Ergast 兼容 API，浏览器需要联网并可访问 api.jolpi.ca。积分与赛果存在数据源发布延迟；这是赛事信息网站，不提供比赛中实时计时。尚未包含排位结果、遥测或实时追踪。

## 项目结构

- `dist/index.html`：页面结构
- `dist/style.css`：响应式主题
- `dist/app.js`：接口请求、表格、倒计时与导航
- `app.py`：可选 Flask 本地入口
- `tests/test_app.py`：路由验证

## GitHub 发布

创建一个空仓库，把本项目文件上传即可。`dist` 可直接部署到静态托管；GitHub Pages 可用仓库内的工作流发布。Python 入口用于本地学习，无需公开服务器。

## 验证

```bash
python -m unittest discover -s tests
node --check dist/app.js
```

## 许可与声明

项目代码采用 MIT 许可。数据权利与使用要求由数据提供方决定，代码许可不覆盖第三方数据。本站为独立车迷项目，与 Formula 1 或 FIA 无关联。
