---
name: "git-commit"
description: "Git代码提交工具。当用户输入'提交代码'、'git commit'、'提交到git'或需要将代码提交到版本库时调用。自动处理Git初始化、暂存、提交等操作。"
---

# Git Commit 技能

Git代码提交工具，用于管理Git仓库的日常操作。

## 功能

- 初始化Git仓库（如果尚未初始化）
- 检查Git状态
- 添加文件到暂存区
- 创建提交
- 创建.gitignore文件
- 提交代码到本地仓库

## 使用场景

当用户输入以下触发词时自动调用：
- "提交代码"
- "git commit"
- "提交到git"
- "代码提交"
- "commit"
- "git提交"

## 工作流程

### 1. 检查Git仓库状态

```bash
git status
```

如果项目没有初始化Git仓库，询问用户是否需要初始化。

### 2. 创建.gitignore（如需要）

常见忽略内容：

```
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
dist/
build/
.pytest_cache/
.coverage
*.log
.DS_Store
node_modules/
.env
```

### 3. 暂存文件

```bash
git add .
```

或指定文件：

```bash
git add <file_path>
```

### 4. 创建提交

使用有意义的提交信息，遵循约定式提交规范：

- `feat:` 新功能
- `fix:` 修复bug
- `docs:` 文档更新
- `style:` 代码格式（不影响功能）
- `refactor:` 重构
- `perf:` 性能优化
- `test:` 测试相关
- `chore:` 构建/工具变更

示例：

```bash
git commit -m "feat: 添加用户登录功能"
```

## 约定式提交格式

提交信息格式：`type: description`

| Type | Description |
|------|-------------|
| feat | 新功能 |
| fix | 修复bug |
| docs | 文档变更 |
| style | 代码格式（不影响功能） |
| refactor | 重构（既不是修复也不是新功能） |
| perf | 性能优化 |
| test | 测试相关 |
| chore | 构建/工具变更 |

## 示例

**用户输入**：`提交代码`

**执行流程**：
1. 检查git status
2. 如果没有.gitignore，创建并添加
3. git add .
4. git commit -m "chore: 更新代码"
5. 显示提交结果

**用户输入**：`提交代码 -m "feat: 添加发票识别模块"`

**执行流程**：
1. 检查git status
2. git add .
3. git commit -m "feat: 添加发票识别模块"
4. 显示提交结果

## 注意事项

- 提交前先检查git status确认要提交的文件
- 使用描述性的提交信息
- 遵循约定式提交规范
- 确保.gitignore正确配置，避免提交不需要的文件
- 如果有敏感信息（如API密钥、密码），不要提交
