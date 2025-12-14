# Edinburgh Carbon Intelligence

---

# 中文版本

## 项目概述

这是一个交互式网页应用，用于展示爱丁堡墓地的碳储存潜力研究。该项目结合了地理空间数据、环境指标和社会经济数据，通过可视化地图和详细报告呈现研究成果。

---

## 技术栈

| 类别 | 技术 |
|------|------|
| **后端** | Python Flask |
| **数据库** | Oracle Database |
| **前端** | HTML5, CSS3, JavaScript |
| **地图库** | Leaflet.js |
| **样式** | 自定义 CSS（玻璃态设计） |
| **字体** | Google Fonts (Rajdhani, Inter, EB Garamond) |
| **图标** | Font Awesome |

---

## 项目结构

```
deploy-web-2/
│
├── app.py                      # Flask 主应用程序
├── templates/
│   └── map.html                # 前端页面模板
├── data/
│   ├── Cemeteries_35.json      # 墓地 GeoJSON 地理数据
│   └── edinburgh_simd.json     # SIMD 社会剥夺指数数据
├── static/
│   └── report_images/          # 报告图片资源
├── 01_create_tables_clean.sql  # 数据库表创建脚本
├── 02_insert_data.sql          # 数据插入脚本
└── README.md                   # 项目文档
```

---

## 开发流程

### 第一阶段：数据准备

#### 1.1 数据库设计

- 使用 Oracle 数据库存储墓地数据
- 创建 `graveyards` 表，包含以下关键字段：
  - `name` - 墓地名称
  - `area_hectares` - 面积（公顷）
  - `ndvi_mean` - NDVI 植被指数
  - `carbon_per_hectare_validate` - 每公顷碳储量
  - `edi_new_canopy_ndvi` - EDI 环境剥夺指数
  - `simd_decile` - SIMD 社会剥夺十分位数
  - `canopy_percentage` - 树冠覆盖率
  - `agb_total` - 地上生物量总量

#### 1.2 GeoJSON 数据准备

- `Cemeteries_35.json` - 包含35个墓地的地理边界多边形
- `edinburgh_simd.json` - 爱丁堡 SIMD 区域数据用于社会剥夺可视化

---

### 第二阶段：后端开发

#### 2.1 Flask 应用架构

```python
# 核心路由
/                           # 主页
/api/graveyards             # 墓地数据 API
/api/simd                   # SIMD 数据 API
/static/<path:filename>     # 静态文件服务
```

#### 2.2 数据融合逻辑

1. 读取 GeoJSON 文件获取地理边界
2. 连接 Oracle 数据库获取环境指标
3. 通过名称匹配合并数据（支持名称映射）
4. 对未匹配项使用面积匹配算法
5. 注入报告标签（如"生物多样性热点"、"优先区域"等）

---

### 第三阶段：前端开发

#### 3.1 页面结构

- **报告页面** - 学术研究报告展示，包含项目介绍、研究发现、团队信息
- **地图页面** - 交互式地图可视化，支持多种数据视图

#### 3.2 地图功能

| 功能 | 描述 |
|------|------|
| **多层可视化** | 碳储量、EDI、SIMD、NDVI 等多种视图模式 |
| **交互弹窗** | 点击墓地显示详细数据卡片 |
| **搜索过滤** | 按名称搜索墓地 |
| **图例说明** | 动态颜色图例 |
| **数据导出** | 支持数据导出功能 |
| **响应式设计** | 适配移动端显示 |

#### 3.3 UI 设计特点

- 采用 Glassmorphism（玻璃态）设计风格
- 深色主题配合霓虹色彩强调
- 平滑动画过渡效果
- 侧边栏可折叠设计

#### 3.4 颜色编码系统

```css
--neon-blue: #0ea5e9;    /* 高值指标 */
--neon-green: #10b981;   /* 生态指标 */
--neon-red: #ef4444;     /* 优先区域 */
--neon-purple: #8b5cf6;  /* 强调元素 */
--neon-yellow: #f59e0b;  /* 遗产标记 */
```

---

### 第四阶段：数据可视化模式

| 模式 | 数据字段 | 颜色范围 |
|------|----------|----------|
| **碳储量** | carbon_per_hectare | 绿色渐变 |
| **EDI 指数** | edi_new_canopy_ndvi | 蓝色渐变 |
| **SIMD 剥夺** | simd_decile | 红-黄-绿 |
| **NDVI 植被** | ndvi_mean | 绿色渐变 |
| **树冠覆盖** | canopy_percentage | 绿色渐变 |

---

### 第五阶段：报告集成

- 集成学术研究报告内容
- 展示团队成员信息
- 包含关键发现和建议
- 支持图片查看器功能

---

## 运行项目

### 环境要求

```bash
pip install flask oracledb
```

### 启动服务

```bash
python app.py
```

服务将在 `http://localhost:55429` 启动

---

## API 端点

| 端点 | 方法 | 描述 |
|------|------|------|
| `/` | GET | 主页面 |
| `/api/graveyards` | GET | 返回墓地 GeoJSON 数据 |
| `/api/simd` | GET | 返回 SIMD 区域数据 |

---

## 关键指标说明

| 指标 | 说明 |
|------|------|
| **NDVI** | 归一化植被指数，衡量植被健康程度 (0-1) |
| **EDI** | 环境剥夺指数，综合树冠覆盖和 NDVI (0-100) |
| **SIMD** | 苏格兰多重剥夺指数，1=最剥夺，10=最不剥夺 |
| **Carbon** | 每公顷碳储量（吨/公顷） |
| **Canopy** | 树冠覆盖百分比 |
| **AGB** | 地上生物量总量 |

---

## 项目特色

1. **数据驱动** - 基于真实环境监测数据
2. **多维分析** - 结合环境与社会经济指标
3. **交互体验** - 直观的地图交互界面
4. **学术价值** - 服务于大学地理科学研究
5. **响应式设计** - 支持多设备访问

---

## 开发团队

**爱丁堡大学 - 地理科学学院**

---

## 许可证

本项目用于学术研究目的。

---
---
---

# English Version

## Project Overview

An interactive web application showcasing research on carbon storage potential in Edinburgh's graveyards. The project combines geospatial data, environmental metrics, and socioeconomic data through an interactive map and detailed report.

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python Flask |
| **Database** | Oracle Database |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Mapping** | Leaflet.js |
| **Styling** | Custom CSS (Glassmorphism Design) |
| **Fonts** | Google Fonts (Rajdhani, Inter, EB Garamond) |
| **Icons** | Font Awesome |

---

## Project Structure

```
deploy-web-2/
│
├── app.py                      # Main Flask application
├── templates/
│   └── map.html                # Frontend template
├── data/
│   ├── Cemeteries_35.json      # Cemetery GeoJSON data
│   └── edinburgh_simd.json     # SIMD deprivation data
├── static/
│   └── report_images/          # Report images
├── 01_create_tables_clean.sql  # Database table creation script
├── 02_insert_data.sql          # Data insertion script
└── README.md                   # Project documentation
```

---

## Development Process

### Phase 1: Data Preparation

#### 1.1 Database Design

- Oracle database for cemetery data storage
- Created `graveyards` table with key fields:
  - `name` - Cemetery name
  - `area_hectares` - Area in hectares
  - `ndvi_mean` - NDVI vegetation index
  - `carbon_per_hectare_validate` - Carbon storage per hectare
  - `edi_new_canopy_ndvi` - EDI environmental deprivation index
  - `simd_decile` - SIMD social deprivation decile
  - `canopy_percentage` - Canopy coverage percentage
  - `agb_total` - Total above-ground biomass

#### 1.2 GeoJSON Data Preparation

- `Cemeteries_35.json` - Geographic boundary polygons for 35 cemeteries
- `edinburgh_simd.json` - Edinburgh SIMD zone data for deprivation visualization

---

### Phase 2: Backend Development

#### 2.1 Flask Application Architecture

```python
# Core Routes
/                           # Home page
/api/graveyards             # Cemetery data API
/api/simd                   # SIMD data API
/static/<path:filename>     # Static file serving
```

#### 2.2 Data Merging Logic

1. Load GeoJSON file for geographic boundaries
2. Connect to Oracle database for environmental metrics
3. Merge data by name matching (with name mapping support)
4. Use area-based matching for unmatched features
5. Inject report tags (e.g., "Biodiversity Hotspot", "Priority Zone")

---

### Phase 3: Frontend Development

#### 3.1 Page Structure

- **Report Page** - Academic research report display with project intro, findings, team info
- **Map Page** - Interactive map visualization with multiple data views

#### 3.2 Map Features

| Feature | Description |
|---------|-------------|
| **Multi-layer Visualization** | Carbon, EDI, SIMD, NDVI view modes |
| **Interactive Popups** | Click cemetery to show detailed data card |
| **Search & Filter** | Search cemeteries by name |
| **Legend** | Dynamic color legend |
| **Data Export** | Export functionality |
| **Responsive Design** | Mobile-friendly layout |

#### 3.3 UI Design Features

- Glassmorphism design aesthetic
- Dark theme with neon accent colors
- Smooth animation transitions
- Collapsible sidebar design

#### 3.4 Color Coding System

```css
--neon-blue: #0ea5e9;    /* High values */
--neon-green: #10b981;   /* Ecological */
--neon-red: #ef4444;     /* Priority zones */
--neon-purple: #8b5cf6;  /* Accent */
--neon-yellow: #f59e0b;  /* Heritage */
```

---

### Phase 4: Visualization Modes

| Mode | Data Field | Color Range |
|------|------------|-------------|
| **Carbon** | carbon_per_hectare | Green gradient |
| **EDI Index** | edi_new_canopy_ndvi | Blue gradient |
| **SIMD Deprivation** | simd_decile | Red-Yellow-Green |
| **NDVI Vegetation** | ndvi_mean | Green gradient |
| **Canopy Coverage** | canopy_percentage | Green gradient |

---

### Phase 5: Report Integration

- Integrated academic research report content
- Team member information display
- Key findings and recommendations
- Image viewer functionality

---

## Running the Project

### Requirements

```bash
pip install flask oracledb
```

### Start Server

```bash
python app.py
```

Server starts at `http://localhost:55429`

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main page |
| `/api/graveyards` | GET | Returns cemetery GeoJSON data |
| `/api/simd` | GET | Returns SIMD zone data |

---

## Key Metrics Explanation

| Metric | Description |
|--------|-------------|
| **NDVI** | Normalized Difference Vegetation Index, measures vegetation health (0-1) |
| **EDI** | Environmental Deprivation Index, combines canopy and NDVI (0-100) |
| **SIMD** | Scottish Index of Multiple Deprivation, 1=most deprived, 10=least deprived |
| **Carbon** | Carbon storage per hectare (tonnes/hectare) |
| **Canopy** | Tree canopy coverage percentage |
| **AGB** | Total above-ground biomass |

---

## Project Highlights

1. **Data-Driven** - Based on real environmental monitoring data
2. **Multi-Dimensional Analysis** - Combines environmental and socioeconomic indicators
3. **Interactive Experience** - Intuitive map interaction interface
4. **Academic Value** - Serves university geoscience research
5. **Responsive Design** - Supports multi-device access

---

## Development Team

**University of Edinburgh - School of GeoSciences**

---

## License

This project is for academic research purposes.
