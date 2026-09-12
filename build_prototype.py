# -*- coding: utf-8 -*-
out_path = r'd:\00 云上江西\03 赣政通\需求设计\态势感知\gzt-prototype\index.html'

def write_css_head():
    return '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>态势感知管理系统</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif; font-size: 14px; color: #303133; background: #f5f7fa; line-height: 1.5; }
a { color: #409eff; text-decoration: none; cursor: pointer; }
a:hover { color: #66b1ff; }
.app-container { display: flex; height: 100vh; overflow: hidden; }
.sidebar { width: 220px; background: #001529; flex-shrink: 0; display: flex; flex-direction: column; overflow-y: auto; overflow-x: hidden; }
.sidebar-logo { height: 60px; display: flex; align-items: center; padding: 0 16px; background: #002140; color: #fff; font-size: 16px; font-weight: 600; flex-shrink: 0; }
.sidebar-logo-icon { width: 32px; height: 32px; background: linear-gradient(135deg, #1890ff, #40a9ff); border-radius: 6px; display: flex; align-items: center; justify-content: center; margin-right: 12px; font-size: 14px; }
.sidebar-menu { flex: 1; padding: 8px 0; }
.menu-item { height: 44px; display: flex; align-items: center; padding: 0 20px; color: rgba(255,255,255,.7); cursor: pointer; transition: all .2s; user-select: none; }
.menu-item:hover, .menu-item.open { color: #fff; }
.menu-item.active { background: #1890ff; color: #fff; }
.menu-icon { margin-right: 10px; font-size: 16px; width: 18px; text-align: center; }
.menu-arrow { margin-left: auto; font-size: 12px; transition: transform .2s; }
.menu-item.open .menu-arrow { transform: rotate(180deg); }
.submenu { display: none; background: #000c17; }
.submenu.open { display: block; }
.submenu-item { height: 40px; display: flex; align-items: center; padding: 0 20px 0 48px; color: rgba(255,255,255,.65); cursor: pointer; transition: all .2s; font-size: 13px; }
.submenu-item:hover { color: #fff; }
.submenu-item.active { color: #fff; background: #1890ff; }
.main-wrapper { flex: 1; display: flex; flex-direction: column; overflow: hidden; min-width: 0; }
.header { height: 60px; background: #fff; border-bottom: 1px solid #e4e7ed; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; flex-shrink: 0; }
.breadcrumb { font-size: 14px; color: #606266; }
.crumb-first { color: #303133; }
.crumb-sep { margin: 0 8px; color: #c0c4cc; }
.header-right { display: flex; align-items: center; gap: 20px; }
.header-icon { position: relative; cursor: pointer; font-size: 18px; color: #606266; }
.badge { position: absolute; top: -6px; right: -6px; min-width: 16px; height: 16px; padding: 0 4px; background: #f56c6c; color: #fff; border-radius: 8px; font-size: 11px; line-height: 16px; text-align: center; }
.user-info { display: flex; align-items: center; gap: 8px; cursor: pointer; }
.user-avatar { width: 32px; height: 32px; border-radius: 50%; background: #409eff; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 14px; }
.user-name { color: #606266; }
.content-wrapper { flex: 1; overflow-y: auto; padding: 20px; background: #f5f7fa; }
.page { display: none; }
.page.active { display: block; }
.el-card { background: #fff; border-radius: 4px; border: 1px solid #ebeef5; box-shadow: 0 2px 12px 0 rgba(0,0,0,.04); margin-bottom: 16px; }
.el-card__body { padding: 20px; }
.filter-bar { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 16px; }
.filter-item { display: flex; align-items: center; gap: 8px; }
.filter-item label { color: #606266; font-size: 14px; white-space: nowrap; }
.el-input__inner { height: 32px; line-height: 32px; padding: 0 12px; border: 1px solid #dcdfe6; border-radius: 4px; font-size: 14px; color: #606266; background: #fff; outline: none; transition: border-color .2s; }
.el-input__inner:focus { border-color: #409eff; }
select.el-input__inner { padding-right: 24px; appearance: auto; }
.el-button { display: inline-flex; align-items: center; justify-content: center; height: 32px; padding: 0 16px; border: 1px solid #dcdfe6; border-radius: 4px; background: #fff; color: #606266; font-size: 14px; cursor: pointer; transition: all .2s; white-space: nowrap; }
.el-button:hover { color: #409eff; border-color: #c6e2ff; background: #ecf5ff; }
.el-button--primary { background: #409eff; border-color: #409eff; color: #fff; }
.el-button--primary:hover { background: #66b1ff; border-color: #66b1ff; color: #fff; }
.el-button--success { background: #67c23a; border-color: #67c23a; color: #fff; }
.el-button--success:hover { background: #85ce61; border-color: #85ce61; }
.el-button--danger { color: #f56c6c; border-color: #fbc4c4; background: #fef0f0; }
.el-button--danger:hover { background: #f56c6c; border-color: #f56c6c; color: #fff; }
.el-button--text { border: none; background: transparent; color: #409eff; padding: 0 4px; }
.el-button--text:hover { color: #66b1ff; background: transparent; }
.action-bar { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; flex-wrap: wrap; }
.el-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.el-table th, .el-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid #ebeef5; }
.el-table th { background: #fafafa; color: #909399; font-weight: 600; white-space: nowrap; }
.el-table td { color: #606266; }
.el-table tr:hover td { background: #f5f7fa; }
.el-table .actions { display: flex; gap: 8px; flex-wrap: nowrap; }
.el-switch { display: inline-flex; align-items: center; width: 40px; height: 20px; border-radius: 10px; background: #dcdfe6; cursor: pointer; position: relative; transition: background .2s; }
.el-switch.is-checked { background: #409eff; }
.el-switch__core { width: 16px; height: 16px; border-radius: 50%; background: #fff; position: absolute; left: 2px; transition: left .2s; }
.el-switch.is-checked .el-switch__core { left: 22px; }
.el-pagination { display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 16px; color: #606266; font-size: 13px; }
.el-pagination button { min-width: 28px; height: 28px; padding: 0 6px; border: 1px solid #dcdfe6; background: #fff; border-radius: 4px; cursor: pointer; color: #606266; }
.el-pagination button.is-active { background: #409eff; color: #fff; border-color: #409eff; }
.el-pagination button:disabled { color: #c0c4cc; cursor: not-allowed; }
.el-tabs { margin-bottom: 16px; }
.el-tabs__nav { display: flex; border-bottom: 1px solid #e4e7ed; }
.el-tabs__item { padding: 0 20px; height: 40px; line-height: 40px; color: #303133; cursor: pointer; border-bottom: 2px solid transparent; transition: all .2s; font-size: 14px; white-space: nowrap; }
.el-tabs__item:hover { color: #409eff; }
.el-tabs__item.is-active { color: #409eff; border-bottom-color: #409eff; }
.el-tabs__content { display: none; }
.el-tabs__content.is-active { display: block; }
.el-progress { display: inline-flex; align-items: center; width: 100%; }
.el-progress__bar { flex: 1; height: 8px; background: #ebeef5; border-radius: 4px; overflow: hidden; }
.el-progress__inner { height: 100%; background: #409eff; border-radius: 4px; transition: width .3s; }
.el-progress__text { margin-left: 8px; color: #606266; font-size: 12px; min-width: 35px; }
.el-checkbox { width: 14px; height: 14px; border: 1px solid #dcdfe6; border-radius: 2px; cursor: pointer; display: inline-block; }
.el-checkbox.checked { background: #409eff; border-color: #409eff; position: relative; }
.el-checkbox.checked::after { content: ''; position: absolute; left: 4px; top: 1px; width: 4px; height: 8px; border: solid #fff; border-width: 0 2px 2px 0; transform: rotate(45deg); }
.el-dialog__wrapper { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,.5); z-index: 1000; align-items: center; justify-content: center; }
.el-dialog__wrapper.visible { display: flex; }
.el-dialog { background: #fff; border-radius: 4px; box-shadow: 0 2px 12px 0 rgba(0,0,0,.1); width: 600px; max-width: 90%; max-height: 80vh; display: flex; flex-direction: column; }
.el-dialog__header { padding: 16px 20px; border-bottom: 1px solid #ebeef5; display: flex; align-items: center; justify-content: space-between; }
.el-dialog__title { font-size: 16px; font-weight: 600; color: #303133; }
.el-dialog__headerbtn { background: none; border: none; font-size: 20px; color: #909399; cursor: pointer; }
.el-dialog__body { padding: 20px; overflow-y: auto; flex: 1; }
.el-dialog__footer { padding: 12px 20px; border-top: 1px solid #ebeef5; text-align: right; }
.el-form-item { margin-bottom: 16px; }
.el-form-item__label { display: block; color: #606266; font-size: 14px; margin-bottom: 6px; }
.el-form-item__content .el-input__inner { width: 100%; }
.el-form-item__content textarea.el-input__inner { height: 80px; padding: 8px 12px; resize: vertical; }
.el-checkbox-group { display: flex; flex-wrap: wrap; gap: 12px; }
.el-checkbox-button { display: inline-flex; align-items: center; gap: 4px; padding: 6px 12px; border: 1px solid #dcdfe6; border-radius: 4px; cursor: pointer; color: #606266; font-size: 13px; }
.el-checkbox-button:hover { border-color: #409eff; color: #409eff; }
.el-checkbox-button.is-checked { background: #409eff; border-color: #409eff; color: #fff; }
.transfer-panel { border: 1px solid #e4e7ed; border-radius: 4px; padding: 12px; max-height: 200px; overflow-y: auto; }
.transfer-item { padding: 6px 8px; cursor: pointer; border-radius: 4px; color: #606266; }
.transfer-item:hover { background: #f5f7fa; }
.transfer-item.selected { background: #ecf5ff; color: #409eff; }
.el-message { position: fixed; top: -60px; left: 50%; transform: translateX(-50%); padding: 12px 20px; background: #fff; border-radius: 4px; box-shadow: 0 2px 12px 0 rgba(0,0,0,.1); z-index: 2000; transition: top .3s; border-left: 4px solid #67c23a; min-width: 280px; }
.el-message.show { top: 20px; }
.scroll-x { overflow-x: auto; }
.mt-2 { margin-top: 12px; }
</style>
</head>
<body>
<div class="app-container">
  <aside class="sidebar">
    <div class="sidebar-logo"><div class="sidebar-logo-icon">态</div><span>态势感知管理系统</span></div>
    <nav class="sidebar-menu">
      <div class="menu-item open" data-submenu="data-gov" onclick="toggleSubmenu('data-gov')">
        <span class="menu-icon">▦</span><span>数据治理</span><span class="menu-arrow">▾</span>
      </div>
      <div class="submenu open" id="submenu-data-gov">
        <div class="submenu-item active" data-page="extract-config" onclick="switchPage('extract-config', '数据治理 / 数据转换提取配置')">数据转换提取配置</div>
        <div class="submenu-item" data-page="data-model" onclick="switchPage('data-model', '数据治理 / 数据模型管理')">数据模型管理</div>
        <div class="submenu-item" data-page="data-chart" onclick="switchPage('data-chart', '数据治理 / 数据图表管理')">数据图表管理</div>
        <div class="submenu-item" data-page="data-query" onclick="switchPage('data-query', '数据治理 / 数据查询')">数据查询</div>
        <div class="submenu-item" data-page="data-filter" onclick="switchPage('data-filter', '数据治理 / 数据过滤')">数据过滤</div>
      </div>
      <div class="menu-item" data-submenu="sys-manage" onclick="toggleSubmenu('sys-manage')">
        <span class="menu-icon">⚙</span><span>系统管理</span><span class="menu-arrow">▾</span>
      </div>
      <div class="submenu" id="submenu-sys-manage">
        <div class="submenu-item" data-page="dict" onclick="switchPage('dict', '系统管理 / 字典管理')">字典管理</div>
        <div class="submenu-item" data-page="notice" onclick="switchPage('notice', '系统管理 / 通知公告管理')">通知公告管理</div>
        <div class="submenu-item" data-page="log" onclick="switchPage('log', '系统管理 / 日志管理')">日志管理</div>
        <div class="submenu-item" data-page="param" onclick="switchPage('param', '系统管理 / 参数管理')">参数管理</div>
      </div>
      <div class="menu-item" data-page="integration" onclick="switchPage('integration', '系统对接 / 系统对接管理')">
        <span class="menu-icon">⇄</span><span>系统对接</span>
      </div>
    </nav>
  </aside>
  <div class="main-wrapper">
    <header class="header">
      <div class="header-left">
        <div class="breadcrumb">
          <span class="crumb-first" id="crumb-first">数据治理</span>
          <span class="crumb-sep">/</span>
          <span id="crumb-current">数据转换提取配置</span>
        </div>
      </div>
      <div class="header-right">
        <div class="header-icon">🔔<span class="badge">5</span></div>
        <div class="user-info"><div class="user-avatar">超</div><span class="user-name">超级管理员</span></div>
      </div>
    </header>
    <div class="content-wrapper">
'''

switch_on = '<div class="el-switch is-checked" onclick="this.classList.toggle(\'is-checked\')"><div class="el-switch__core"></div></div>'
switch_off = '<div class="el-switch" onclick="this.classList.toggle(\'is-checked\')"><div class="el-switch__core"></div></div>'
cb = '<span class="el-checkbox" onclick="this.classList.toggle(\'checked\')"></span>'

def progress_html(val):
    return f'<div class="el-progress"><div class="el-progress__bar"><div class="el-progress__inner" style="width:{val}%"></div></div><span class="el-progress__text">{val}%</span></div>'

def pagination_html(total):
    return f'<div class="el-pagination"><span class="el-pagination__total">共 {total} 条</span><button disabled>上一页</button><button class="is-active">1</button><button>2</button><button>3</button><button>下一页</button></div>'

def write_extract_config():
    s = '''<section class="page active" id="page-extract-config">
  <div class="el-card">
    <div class="el-card__body">
      <div class="el-tabs">
        <div class="el-tabs__nav">
          <div class="el-tabs__item is-active" onclick="switchTab(this, 'tab-extract-report')">报表导出配置</div>
          <div class="el-tabs__item" onclick="switchTab(this, 'tab-extract-chart')">图表导出配置</div>
        </div>
      </div>
      <div class="el-tabs__content is-active" id="tab-extract-report">
        <div class="filter-bar">
          <div class="filter-item"><label>模板名称</label><input class="el-input__inner" placeholder="请输入模板名称"></div>
          <div class="filter-item"><label>导出格式</label><select class="el-input__inner"><option>全部</option><option>CSV</option><option>Excel</option><option>PDF</option></select></div>
          <div class="filter-item"><label>状态</label><select class="el-input__inner"><option>全部</option><option>启用</option><option>禁用</option></select></div>
          <button class="el-button el-button--primary" onclick="showToast('查询成功','共找到 24 条模板')">搜索</button>
          <button class="el-button" onclick="showToast('已重置','筛选条件已重置')">重置</button>
        </div>
        <div class="action-bar">
          <button class="el-button el-button--primary" onclick="openDialog('新增报表导出模板','report-add')">+ 新增</button>
          <button class="el-button el-button--danger" onclick="showToast('批量删除成功','已删除选中的模板')">批量删除</button>
          <button class="el-button el-button--success" onclick="showToast('导出成功','已开始导出任务')">导出</button>
          <button class="el-button" onclick="showToast('复制成功','已复制当前模板')">复制</button>
          <button class="el-button" onclick="openDialog('模板版本管理','version')">版本管理</button>
          <button class="el-button" onclick="openDialog('导出预览','preview')">预览</button>
          <button class="el-button" onclick="openDialog('导出历史记录','history')">历史记录</button>
          <button class="el-button" onclick="showToast('刷新成功','已刷新列表')">刷新</button>
        </div>
        <div class="scroll-x">
          <table class="el-table">
            <thead><tr>
              <th>''' + cb + '''</th>
              <th>模板编码</th><th>模板名称</th><th>数据来源</th><th>导出格式</th><th>字段配置</th><th>排序规则</th>
              <th>过滤条件</th><th>分页大小</th><th>是否脱敏</th><th>样式</th><th>状态</th><th>系统通知</th>
              <th>导出进度</th><th>创建时间</th><th>操作</th>
            </tr></thead>
            <tbody>
'''
    report_rows = [
        ('RPT001','月度用户统计报表','用户统计','Excel','按创建时间','1000','2024-01-15','100'),
        ('RPT002','季度待办分析报表','待办统计','CSV','按字段降序','2000','2024-02-10','100'),
        ('RPT003','应用访问明细报表','应用统计','PDF','按访问量降序','500','2024-03-05','100'),
        ('RPT004','行为日志汇总报表','行为统计','Excel','按操作时间','1500','2024-03-20','80'),
        ('RPT005','年度组织架构报表','单位索引','Excel','按单位编码升序','800','2024-04-01','100'),
        ('RPT006','部门活跃度报表','部门索引','CSV','按活跃天数降序','1200','2024-04-15','60'),
        ('RPT007','用户登录明细报表','用户索引','PDF','按登录时间','2000','2024-05-01','100'),
        ('RPT008','待办超时统计报表','待办统计','Excel','按超时天数','1000','2024-05-20','100'),
        ('RPT009','群组消息统计报表','群组索引','CSV','按消息数降序','600','2024-06-01','100'),
        ('RPT010','网络电话记录报表','网络电话索引','Excel','按通话时长','900','2024-06-15','40'),
    ]
    for code,name,source,fmt,sort,page,date,prog in report_rows:
        s += f'''              <tr>
                <td>{cb}</td>
                <td>{code}</td><td>{name}</td><td>{source}</td><td>{fmt}</td>
                <td><span>已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
                <td>{sort}</td>
                <td><span>已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
                <td>{page}</td><td>{switch_on}</td>
                <td><span>已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
                <td>{switch_on}</td><td>{switch_off}</td><td>{progress_html(int(prog))}</td><td>{date}</td>
                <td><div class="actions">
                  <a class="el-button--text" onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a>
                  <a class="el-button--text" onclick="showToast('删除成功')">删除</a>
                  <a class="el-button--text" onclick="showToast('复制成功')">复制</a>
                  <a class="el-button--text" onclick="openDialog('模板版本管理','version')">版本</a>
                  <a class="el-button--text" onclick="openDialog('修改记录','modify-record')">修改记录</a>
                  <a class="el-button--text" onclick="openDialog('导出预览','preview')">预览</a>
                </div></td>
              </tr>
'''
    s += '''            </tbody>
          </table>
        </div>
        ''' + pagination_html(24) + '''
      </div>
      <div class="el-tabs__content" id="tab-extract-chart">
        <div class="filter-bar">
          <div class="filter-item"><label>模板名称</label><input class="el-input__inner" placeholder="请输入模板名称"></div>
          <div class="filter-item"><label>图表类型</label><select class="el-input__inner"><option>全部</option><option>折线图</option><option>柱状图</option><option>饼图</option><option>面积图</option></select></div>
          <div class="filter-item"><label>状态</label><select class="el-input__inner"><option>全部</option><option>启用</option><option>禁用</option></select></div>
          <button class="el-button el-button--primary" onclick="showToast('查询成功','共找到 18 条模板')">搜索</button>
          <button class="el-button" onclick="showToast('已重置','筛选条件已重置')">重置</button>
        </div>
        <div class="action-bar">
          <button class="el-button el-button--primary" onclick="openDialog('新增图表导出模板','chart-add')">+ 新增</button>
          <button class="el-button el-button--danger" onclick="showToast('批量删除成功','已删除选中的模板')">批量删除</button>
          <button class="el-button el-button--success" onclick="showToast('导出成功','已开始导出任务')">导出</button>
          <button class="el-button" onclick="showToast('复制成功','已复制当前模板')">复制</button>
          <button class="el-button" onclick="openDialog('模板版本管理','version')">版本管理</button>
          <button class="el-button" onclick="openDialog('图表组合','chart-combine')">组合</button>
          <button class="el-button" onclick="openDialog('导出预览','preview')">预览</button>
          <button class="el-button" onclick="openDialog('导出历史记录','history')">历史记录</button>
          <button class="el-button" onclick="showToast('刷新成功','已刷新列表')">刷新</button>
        </div>
        <div class="scroll-x">
          <table class="el-table">
            <thead><tr>
              <th>''' + cb + '''</th>
              <th>模板编码</th><th>模板名称</th><th>数据源</th><th>图表类型</th><th>图表组合</th><th>数据表配置</th>
              <th>样式与布局</th><th>交互配置</th><th>导出格式</th><th>分辨率</th><th>是否分页</th>
              <th>是否脱敏</th><th>状态</th><th>系统通知</th><th>导出进度</th><th>创建时间</th><th>操作</th>
            </tr></thead>
            <tbody>
'''
    chart_rows = [
        ('CHT001','用户活跃趋势图','用户统计','折线图','PNG','300dpi','2024-01-10','100'),
        ('CHT002','待办处理时效图','待办统计','柱状图','JPG','150dpi','2024-02-05','100'),
        ('CHT003','应用访问占比图','应用统计','饼图','PDF','300dpi','2024-02-28','100'),
        ('CHT004','行为分布热力图','行为统计','面积图','SVG','150dpi','2024-03-15','80'),
        ('CHT005','单位活跃度对比','单位索引','柱状图','PNG','300dpi','2024-04-08','100'),
        ('CHT006','部门协作关系图','部门索引','饼图','JPG','300dpi','2024-04-22','60'),
        ('CHT007','日程时间分布图','日程索引','折线图','PNG','150dpi','2024-05-12','100'),
        ('CHT008','网络电话时长统计','网络电话索引','柱状图','PDF','300dpi','2024-05-30','40'),
    ]
    combine_texts = ['已组合3个','已组合2个','已组合1个','已组合4个','已组合2个','已组合1个','已组合3个','已组合2个']
    for i,(code,name,source,typ,fmt,res,date,prog) in enumerate(chart_rows):
        s += f'''              <tr>
                <td>{cb}</td>
                <td>{code}</td><td>{name}</td><td>{source}</td><td>{typ}</td>
                <td><span>{combine_texts[i]}</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
                <td><span>已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
                <td><span>已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
                <td><span>已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
                <td>{fmt}</td><td>{res}</td><td>{switch_on}</td><td>{switch_on}</td>
                <td>{switch_on}</td><td>{switch_off}</td><td>{progress_html(int(prog))}</td><td>{date}</td>
                <td><div class="actions">
                  <a class="el-button--text" onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a>
                  <a class="el-button--text" onclick="showToast('删除成功')">删除</a>
                  <a class="el-button--text" onclick="showToast('复制成功')">复制</a>
                  <a class="el-button--text" onclick="openDialog('模板版本管理','version')">版本</a>
                  <a class="el-button--text" onclick="openDialog('修改记录','modify-record')">修改记录</a>
                  <a class="el-button--text" onclick="openDialog('导出预览','preview')">预览</a>
                </div></td>
              </tr>
'''
    s += '''            </tbody>
          </table>
        </div>
        ''' + pagination_html(18) + '''
      </div>
    </div>
  </div>
</section>
'''
    return s

def write_other_modules():
    return '''<section class="page" id="page-data-model">
  <div class="el-card"><div class="el-card__body">
    <div class="el-tabs"><div class="el-tabs__nav">
      <div class="el-tabs__item is-active" onclick="switchTab(this,'tab-model-user')">用户统计模型</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-model-todo')">待办统计模型</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-model-app')">应用统计模型</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-model-behavior')">行为统计模型</div>
    </div></div>
    <div class="el-tabs__content is-active" id="tab-model-user">
      <div class="filter-bar"><div class="filter-item"><label>模型名称</label><input class="el-input__inner" placeholder="请输入模型名称"></div><div class="filter-item"><label>状态</label><select class="el-input__inner"><option>全部</option><option>启用</option><option>禁用</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
      <div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">复制</button><button class="el-button">版本</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button></div>
      <table class="el-table"><thead><tr><th>模型编码</th><th>模型名称</th><th>统计维度</th><th>指标公式</th><th>数据来源</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody>
        <tr><td>MOD001</td><td>用户活跃统计模型</td><td>日/周/月</td><td>COUNT(DISTINCT user_id)</td><td>用户索引</td><td>''' + switch_on + '''</td><td>2024-06-01</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr>
        <tr><td>MOD002</td><td>用户增长统计模型</td><td>月/季度</td><td>新增用户数</td><td>用户索引</td><td>''' + switch_on + '''</td><td>2024-06-02</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr>
      </tbody></table>''' + pagination_html(12) + '''
    </div>
    <div class="el-tabs__content" id="tab-model-todo"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">复制</button><button class="el-button">版本</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>模型编码</th><th>模型名称</th><th>统计维度</th><th>指标公式</th><th>数据来源</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody><tr><td>MOD-T01</td><td>待办处理时效模型</td><td>日/周</td><td>AVG(处理时长)</td><td>待办索引</td><td>''' + switch_on + '''</td><td>2024-06-03</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(8) + '''</div>
    <div class="el-tabs__content" id="tab-model-app"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">复制</button><button class="el-button">版本</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>模型编码</th><th>模型名称</th><th>统计维度</th><th>指标公式</th><th>数据来源</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody><tr><td>MOD-A01</td><td>应用访问统计模型</td><td>日/周/月</td><td>COUNT(app_id)</td><td>应用索引</td><td>''' + switch_on + '''</td><td>2024-06-04</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(6) + '''</div>
    <div class="el-tabs__content" id="tab-model-behavior"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">复制</button><button class="el-button">版本</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>模型编码</th><th>模型名称</th><th>统计维度</th><th>指标公式</th><th>数据来源</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody><tr><td>MOD-B01</td><td>用户行为分析模型</td><td>日/周</td><td>COUNT(behavior_id)</td><td>行为索引</td><td>''' + switch_on + '''</td><td>2024-06-05</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(7) + '''</div>
  </div></div>
</section>

<section class="page" id="page-data-chart">
  <div class="el-card"><div class="el-card__body">
    <div class="el-tabs"><div class="el-tabs__nav">
      <div class="el-tabs__item is-active" onclick="switchTab(this,'tab-chart-user')">用户统计可视化</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-chart-todo')">待办统计可视化</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-chart-app')">应用统计可视化</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-chart-behavior')">行为统计可视化</div>
    </div></div>
    <div class="el-tabs__content is-active" id="tab-chart-user">
      <div class="filter-bar"><div class="filter-item"><label>图表名称</label><input class="el-input__inner" placeholder="请输入图表名称"></div><div class="filter-item"><label>图表类型</label><select class="el-input__inner"><option>全部</option><option>折线图</option><option>柱状图</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
      <div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div>
      <table class="el-table"><thead><tr><th>图表编码</th><th>图表名称</th><th>关联模型</th><th>图表类型</th><th>X轴字段</th><th>Y轴字段</th><th>状态</th><th>创建时间</th><th>操作</th></tr></thead><tbody>
        <tr><td>CH-U01</td><td>用户活跃趋势</td><td>用户活跃统计模型</td><td>折线图</td><td>日期</td><td>活跃用户数</td><td>''' + switch_on + '''</td><td>2024-06-01</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr>
      </tbody></table>''' + pagination_html(8) + '''
    </div>
    <div class="el-tabs__content" id="tab-chart-todo"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>图表编码</th><th>图表名称</th><th>关联模型</th><th>图表类型</th><th>X轴字段</th><th>Y轴字段</th><th>状态</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>CH-T01</td><td>待办处理时效</td><td>待办处理时效模型</td><td>柱状图</td><td>部门</td><td>平均处理时长</td><td>''' + switch_on + '''</td><td>2024-06-02</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(6) + '''</div>
    <div class="el-tabs__content" id="tab-chart-app"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>图表编码</th><th>图表名称</th><th>关联模型</th><th>图表类型</th><th>X轴字段</th><th>Y轴字段</th><th>状态</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>CH-A01</td><td>应用访问占比</td><td>应用访问统计模型</td><td>饼图</td><td>应用名称</td><td>访问量</td><td>''' + switch_on + '''</td><td>2024-06-03</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(7) + '''</div>
    <div class="el-tabs__content" id="tab-chart-behavior"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>图表编码</th><th>图表名称</th><th>关联模型</th><th>图表类型</th><th>X轴字段</th><th>Y轴字段</th><th>状态</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>CH-B01</td><td>行为分布</td><td>用户行为分析模型</td><td>面积图</td><td>小时</td><td>操作次数</td><td>''' + switch_on + '''</td><td>2024-06-04</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(5) + '''</div>
  </div></div>
</section>

<section class="page" id="page-data-query">
  <div class="el-card"><div class="el-card__body">
    <div class="el-tabs"><div class="el-tabs__nav">
      <div class="el-tabs__item is-active" onclick="switchTab(this,'tab-query-unit')">单位索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-dept')">部门索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-user')">用户索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-todo')">待办事项索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-group')">群组索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-phone')">网络电话索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-active')">活跃度索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-schedule')">日程索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-app')">应用索引</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-query-behavior')">行为索引</div>
    </div></div>
    <div class="el-tabs__content is-active" id="tab-query-unit">
      <div class="filter-bar"><div class="filter-item"><label>单位名称</label><input class="el-input__inner" placeholder="请输入单位名称"></div><div class="filter-item"><label>状态</label><select class="el-input__inner"><option>全部</option><option>启用</option><option>禁用</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
      <div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div>
      <table class="el-table"><thead><tr><th>单位编码</th><th>单位名称</th><th>单位级别</th><th>单位类型</th><th>所属区划</th><th>状态</th><th>标签</th><th>更新时间</th><th>操作</th></tr></thead><tbody>
        <tr><td>U001</td><td>江西省人民政府</td><td>省级</td><td>行政机关</td><td>江西省</td><td>''' + switch_on + '''</td><td>核心单位</td><td>2024-06-01</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr>
      </tbody></table>''' + pagination_html(156) + '''
    </div>
    <div class="el-tabs__content" id="tab-query-dept"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>部门编码</th><th>部门名称</th><th>所属单位</th><th>部门层级</th><th>负责人</th><th>状态</th><th>标签</th><th>操作</th></tr></thead><tbody><tr><td>D001</td><td>办公室</td><td>江西省人民政府</td><td>一级</td><td>张三</td><td>''' + switch_on + '''</td><td>综合</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(142) + '''</div>
    <div class="el-tabs__content" id="tab-query-user"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>用户账号</th><th>用户姓名</th><th>所属单位</th><th>所属部门</th><th>手机号</th><th>状态</th><th>标签</th><th>操作</th></tr></thead><tbody><tr><td>zhangsan</td><td>张三</td><td>省政府</td><td>办公室</td><td>138****0001</td><td>''' + switch_on + '''</td><td>管理员</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(128) + '''</div>
    <div class="el-tabs__content" id="tab-query-todo"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>待办编码</th><th>待办标题</th><th>待办类型</th><th>发起人</th><th>处理人</th><th>优先级</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>TD001</td><td>审批请假申请</td><td>审批</td><td>李四</td><td>王五</td><td>高</td><td>''' + switch_on + '''</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(98) + '''</div>
    <div class="el-tabs__content" id="tab-query-group"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>群组ID</th><th>群组名称</th><th>群主</th><th>成员数</th><th>群组类型</th><th>状态</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>G001</td><td>项目协作群</td><td>张三</td><td>25</td><td>工作群</td><td>''' + switch_on + '''</td><td>2024-05-01</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(76) + '''</div>
    <div class="el-tabs__content" id="tab-query-phone"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>通话ID</th><th>主叫</th><th>被叫</th><th>通话时长</th><th>通话类型</th><th>状态</th><th>开始时间</th><th>操作</th></tr></thead><tbody><tr><td>P001</td><td>张三</td><td>李四</td><td>5分30秒</td><td>语音</td><td>''' + switch_on + '''</td><td>2024-06-01 09:30</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(65) + '''</div>
    <div class="el-tabs__content" id="tab-query-active"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>用户/组织</th><th>登录次数</th><th>活跃天数</th><th>最后活跃</th><th>活跃度等级</th><th>操作</th></tr></thead><tbody><tr><td>张三</td><td>128</td><td>22</td><td>2024-06-10</td><td>高</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(88) + '''</div>
    <div class="el-tabs__content" id="tab-query-schedule"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>日程ID</th><th>日程标题</th><th>发起人</th><th>参与人</th><th>开始时间</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>S001</td><td>周例会</td><td>张三</td><td>部门全员</td><td>2024-06-10 09:00</td><td>''' + switch_on + '''</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(72) + '''</div>
    <div class="el-tabs__content" id="tab-query-app"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>应用编码</th><th>应用名称</th><th>应用类型</th><th>访问量</th><th>使用人数</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>APP001</td><td>OA办公</td><td>办公</td><td>15230</td><td>856</td><td>''' + switch_on + '''</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(95) + '''</div>
    <div class="el-tabs__content" id="tab-query-behavior"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">统计</button><button class="el-button">备份</button><button class="el-button">恢复</button><button class="el-button">刷新</button><button class="el-button">预警</button><button class="el-button">版本</button><button class="el-button">自动清理</button></div><table class="el-table"><thead><tr><th>行为ID</th><th>行为类型</th><th>操作人</th><th>操作对象</th><th>操作时间</th><th>IP地址</th><th>操作</th></tr></thead><tbody><tr><td>B001</td><td>登录</td><td>张三</td><td>系统</td><td>2024-06-10 08:30</td><td>10.0.0.1</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(110) + '''</div>
  </div></div>
</section>

<section class="page" id="page-data-filter">
  <div class="el-card"><div class="el-card__body">
    <div class="el-tabs"><div class="el-tabs__nav">
      <div class="el-tabs__item is-active" onclick="switchTab(this,'tab-filter-unit')">单位基本信息过滤</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-filter-dept')">部门基本信息过滤</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-filter-region')">行政区划信息过滤</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-filter-business')">业务条线信息过滤</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-filter-org')">组织架构信息过滤</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-filter-time')">时间范围信息过滤</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-filter-geo')">地理位置信息过滤</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-filter-code')">区域编码信息过滤</div>
    </div></div>
    <div class="el-tabs__content is-active" id="tab-filter-unit">
      <div class="filter-bar"><div class="filter-item"><label>过滤名称</label><input class="el-input__inner" placeholder="请输入过滤名称"></div><div class="filter-item"><label>过滤维度</label><select class="el-input__inner"><option>全部</option><option>单位级别</option><option>单位类型</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
      <div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div>
      <table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody>
        <tr><td>F-U001</td><td>省级单位过滤</td><td>单位级别</td><td>3</td><td>2024-01-01 至 2024-12-31</td><td>张三</td><td>2024-06-01</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr>
      </tbody></table>''' + pagination_html(32) + '''
    </div>
    <div class="el-tabs__content" id="tab-filter-dept"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div><table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>F-D001</td><td>一级部门过滤</td><td>部门层级</td><td>2</td><td>不限</td><td>李四</td><td>2024-06-02</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr></tbody></table>''' + pagination_html(28) + '''</div>
    <div class="el-tabs__content" id="tab-filter-region"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div><table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>F-R001</td><td>南昌市辖区过滤</td><td>行政区划</td><td>5</td><td>不限</td><td>王五</td><td>2024-06-03</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr></tbody></table>''' + pagination_html(25) + '''</div>
    <div class="el-tabs__content" id="tab-filter-business"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div><table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>F-B001</td><td>政务业务条线过滤</td><td>业务条线</td><td>4</td><td>不限</td><td>赵六</td><td>2024-06-04</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr></tbody></table>''' + pagination_html(18) + '''</div>
    <div class="el-tabs__content" id="tab-filter-org"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div><table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>F-O001</td><td>组织架构过滤</td><td>组织架构</td><td>3</td><td>不限</td><td>张三</td><td>2024-06-05</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr></tbody></table>''' + pagination_html(22) + '''</div>
    <div class="el-tabs__content" id="tab-filter-time"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div><table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>F-T001</td><td>近30天数据过滤</td><td>时间范围</td><td>1</td><td>2024-05-11 至 2024-06-10</td><td>李四</td><td>2024-06-06</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr></tbody></table>''' + pagination_html(15) + '''</div>
    <div class="el-tabs__content" id="tab-filter-geo"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div><table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>F-G001</td><td>南昌市地理位置过滤</td><td>地理位置</td><td>2</td><td>不限</td><td>王五</td><td>2024-06-07</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr></tbody></table>''' + pagination_html(12) + '''</div>
    <div class="el-tabs__content" id="tab-filter-code"><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button><button class="el-button">过滤历史</button></div><table class="el-table"><thead><tr><th>过滤编码</th><th>过滤名称</th><th>过滤维度</th><th>条件数量</th><th>时间范围</th><th>创建人</th><th>创建时间</th><th>操作</th></tr></thead><tbody><tr><td>F-C001</td><td>区域编码过滤</td><td>区域编码</td><td>3</td><td>不限</td><td>赵六</td><td>2024-06-08</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a><a class="el-button--text">执行</a></div></td></tr></tbody></table>''' + pagination_html(14) + '''</div>
  </div></div>
</section>

<section class="page" id="page-dict">
  <div class="el-card"><div class="el-card__body">
    <div class="filter-bar"><div class="filter-item"><label>字典名称</label><input class="el-input__inner" placeholder="请输入字典名称"></div><div class="filter-item"><label>字典类型</label><select class="el-input__inner"><option>全部</option><option>系统字典</option><option>业务字典</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
    <div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">导入</button></div>
    <table class="el-table"><thead><tr><th>字典编码</th><th>字典名称</th><th>字典类型</th><th>字典值</th><th>排序</th><th>状态</th><th>备注</th><th>操作</th></tr></thead><tbody>
      <tr><td>DICT001</td><td>用户状态</td><td>系统字典</td><td>启用/禁用/锁定</td><td>1</td><td>''' + switch_on + '''</td><td>用户账号状态</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr>
    </tbody></table>''' + pagination_html(28) + '''
  </div></div>
</section>

<section class="page" id="page-notice">
  <div class="el-card"><div class="el-card__body">
    <div class="filter-bar"><div class="filter-item"><label>标题</label><input class="el-input__inner" placeholder="请输入标题"></div><div class="filter-item"><label>类型</label><select class="el-input__inner"><option>全部</option><option>通知</option><option>公告</option></select></div><div class="filter-item"><label>状态</label><select class="el-input__inner"><option>全部</option><option>已发布</option><option>草稿</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
    <div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">导入</button></div>
    <table class="el-table"><thead><tr><th>公告ID</th><th>标题</th><th>类型</th><th>发布范围</th><th>发布人</th><th>发布时间</th><th>状态</th><th>操作</th></tr></thead><tbody>
      <tr><td>NT001</td><td>系统维护通知</td><td>通知</td><td>全员</td><td>管理员</td><td>2024-06-10 09:00</td><td>''' + switch_on + '''</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr>
    </tbody></table>''' + pagination_html(18) + '''
  </div></div>
</section>

<section class="page" id="page-log">
  <div class="el-card"><div class="el-card__body">
    <div class="el-tabs"><div class="el-tabs__nav">
      <div class="el-tabs__item is-active" onclick="switchTab(this,'tab-op-log')">操作日志</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-login-log')">登录日志</div>
    </div></div>
    <div class="el-tabs__content is-active" id="tab-op-log">
      <div class="filter-bar"><div class="filter-item"><label>操作人</label><input class="el-input__inner" placeholder="请输入操作人"></div><div class="filter-item"><label>操作类型</label><select class="el-input__inner"><option>全部</option><option>新增</option><option>修改</option><option>删除</option></select></div><div class="filter-item"><label>操作模块</label><select class="el-input__inner"><option>全部</option><option>数据报表</option><option>图表配置</option></select></div><div class="filter-item"><label>时间范围</label><input class="el-input__inner" placeholder="开始时间">-<input class="el-input__inner" placeholder="结束时间" style="margin-left:4px"></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
      <div class="action-bar"><button class="el-button el-button--danger">删除</button><button class="el-button el-button--danger">清空</button><button class="el-button el-button--success">导出</button></div>
      <table class="el-table"><thead><tr><th>日志ID</th><th>操作人</th><th>操作类型</th><th>操作模块</th><th>操作内容</th><th>IP地址</th><th>操作时间</th><th>操作</th></tr></thead><tbody>
        <tr><td>LOG001</td><td>张三</td><td>新增</td><td>数据报表</td><td>新增月度用户统计报表模板</td><td>10.0.0.1</td><td>2024-06-10 09:30</td><td><div class="actions"><a class="el-button--text">查看</a><a class="el-button--text">删除</a></div></td></tr>
      </tbody></table>''' + pagination_html(256) + '''
    </div>
    <div class="el-tabs__content" id="tab-login-log">
      <div class="filter-bar"><div class="filter-item"><label>用户名</label><input class="el-input__inner" placeholder="请输入用户名"></div><div class="filter-item"><label>登录状态</label><select class="el-input__inner"><option>全部</option><option>成功</option><option>失败</option></select></div><div class="filter-item"><label>时间范围</label><input class="el-input__inner" placeholder="开始时间">-<input class="el-input__inner" placeholder="结束时间" style="margin-left:4px"></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
      <div class="action-bar"><button class="el-button el-button--danger">删除</button><button class="el-button el-button--danger">清空</button><button class="el-button el-button--success">导出</button><button class="el-button">解锁</button></div>
      <table class="el-table"><thead><tr><th>日志ID</th><th>用户名</th><th>登录IP</th><th>登录地点</th><th>浏览器</th><th>登录状态</th><th>登录时间</th><th>操作</th></tr></thead><tbody>
        <tr><td>LGN001</td><td>张三</td><td>10.0.0.1</td><td>南昌市</td><td>Chrome</td><td>成功</td><td>2024-06-10 08:30</td><td><div class="actions"><a class="el-button--text">查看</a><a class="el-button--text">删除</a></div></td></tr>
      </tbody></table>''' + pagination_html(312) + '''
    </div>
  </div></div>
</section>

<section class="page" id="page-param">
  <div class="el-card"><div class="el-card__body">
    <div class="filter-bar"><div class="filter-item"><label>参数名称</label><input class="el-input__inner" placeholder="请输入参数名称"></div><div class="filter-item"><label>参数编码</label><input class="el-input__inner" placeholder="请输入参数编码"></div><div class="filter-item"><label>状态</label><select class="el-input__inner"><option>全部</option><option>启用</option><option>禁用</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
    <div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">导入</button></div>
    <table class="el-table"><thead><tr><th>参数编码</th><th>参数名称</th><th>参数值</th><th>参数类型</th><th>描述</th><th>状态</th><th>操作</th></tr></thead><tbody>
      <tr><td>PARAM001</td><td>导出文件最大行数</td><td>10000</td><td>数值</td><td>限制单次导出最大记录数</td><td>''' + switch_on + '''</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr>
    </tbody></table>''' + pagination_html(24) + '''
  </div></div>
</section>

<section class="page" id="page-integration">
  <div class="el-card"><div class="el-card__body">
    <div class="el-tabs"><div class="el-tabs__nav">
      <div class="el-tabs__item is-active" onclick="switchTab(this,'tab-int-user')">用户激活数</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-app')">应用强提醒</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-phone')">网络电话</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-sms')">短信强提醒</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-meet')">视频会议</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-vc')">视频电话</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-group')">群聊统计</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-groupcnt')">群聊数</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-chat')">聊天窗口</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-gzt')">赣政通强提醒</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-single')">单聊统计</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-sync')">同步频率配置</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-adapter')">接口适配</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-logtype')">日志分类</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-auth')">权限认证配置</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-analysis')">接口对接分析</div>
      <div class="el-tabs__item" onclick="switchTab(this,'tab-int-apilog')">接口日志</div>
    </div></div>
    <div class="el-tabs__content is-active" id="tab-int-user">
      <div class="filter-bar"><div class="filter-item"><label>时间范围</label><input class="el-input__inner" placeholder="开始时间">-<input class="el-input__inner" placeholder="结束时间" style="margin-left:4px"></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div>
      <div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div>
      <table class="el-table"><thead><tr><th>日期</th><th>激活用户数</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody>
        <tr><td>2024-06-10</td><td>12,580</td><td>+5.2%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr>
      </tbody></table>''' + pagination_html(30) + '''
    </div>
    <div class="el-tabs__content" id="tab-int-app"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>应用名称</th><th>强提醒次数</th><th>触达人数</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>OA办公</td><td>3,256</td><td>2,180</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(28) + '''</div>
    <div class="el-tabs__content" id="tab-int-phone"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>通话次数</th><th>通话时长</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>8,520</td><td>1,250小时</td><td>+3.1%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(25) + '''</div>
    <div class="el-tabs__content" id="tab-int-sms"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>短信条数</th><th>触达人数</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>15,230</td><td>12,580</td><td>+2.8%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(22) + '''</div>
    <div class="el-tabs__content" id="tab-int-meet"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>会议场次</th><th>参会人次</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>320</td><td>4,560</td><td>+8.5%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(20) + '''</div>
    <div class="el-tabs__content" id="tab-int-vc"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>视频通话次数</th><th>通话时长</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>2,150</td><td>320小时</td><td>+1.2%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(18) + '''</div>
    <div class="el-tabs__content" id="tab-int-group"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>群聊消息数</th><th>活跃群数</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>45,230</td><td>380</td><td>+4.6%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(26) + '''</div>
    <div class="el-tabs__content" id="tab-int-groupcnt"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>群组总数</th><th>新增群组</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>1,250</td><td>12</td><td>+1.0%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(24) + '''</div>
    <div class="el-tabs__content" id="tab-int-chat"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>聊天窗口数</th><th>活跃窗口</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>8,560</td><td>3,250</td><td>+2.3%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(21) + '''</div>
    <div class="el-tabs__content" id="tab-int-gzt"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>强提醒次数</th><th>触达人数</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>6,820</td><td>5,430</td><td>+3.7%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(23) + '''</div>
    <div class="el-tabs__content" id="tab-int-single"><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日期</th><th>单聊消息数</th><th>活跃人数</th><th>环比</th><th>状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-06-10</td><td>32,150</td><td>6,820</td><td>+1.8%</td><td>正常</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(27) + '''</div>
    <div class="el-tabs__content" id="tab-int-sync"><div class="filter-bar"><div class="filter-item"><label>配置名称</label><input class="el-input__inner" placeholder="请输入配置名称"></div><div class="filter-item"><label>状态</label><select class="el-input__inner"><option>全部</option><option>启用</option><option>禁用</option></select></div><button class="el-button el-button--primary">搜索</button><button class="el-button">重置</button></div><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>配置编码</th><th>配置名称</th><th>同步频率</th><th>数据范围</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody><tr><td>SYNC001</td><td>用户数据同步</td><td>每5分钟</td><td>全量</td><td>''' + switch_on + '''</td><td>2024-06-10</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(8) + '''</div>
    <div class="el-tabs__content" id="tab-int-adapter"><div class="filter-bar"><div class="filter-item"><label>接口名称</label><input class="el-input__inner" placeholder="请输入接口名称"></div><button class="el-button el-button--primary">搜索</button></div><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>适配编码</th><th>接口名称</th><th>请求方式</th><th>适配规则</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody><tr><td>ADP001</td><td>组织架构同步接口</td><td>POST</td><td>JSON转换</td><td>''' + switch_on + '''</td><td>2024-06-10</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(6) + '''</div>
    <div class="el-tabs__content" id="tab-int-logtype"><div class="filter-bar"><div class="filter-item"><label>分类名称</label><input class="el-input__inner" placeholder="请输入分类名称"></div><button class="el-button el-button--primary">搜索</button></div><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>分类编码</th><th>分类名称</th><th>日志级别</th><th>存储周期</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody><tr><td>LT001</td><td>接口调用日志</td><td>INFO</td><td>90天</td><td>''' + switch_on + '''</td><td>2024-06-10</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(5) + '''</div>
    <div class="el-tabs__content" id="tab-int-auth"><div class="filter-bar"><div class="filter-item"><label>认证方式</label><select class="el-input__inner"><option>全部</option><option>OAuth2</option><option>Token</option></select></div><button class="el-button el-button--primary">搜索</button></div><div class="action-bar"><button class="el-button el-button--primary">+ 新增</button><button class="el-button el-button--danger">批量删除</button><button class="el-button el-button--success">导出</button><button class="el-button">刷新</button></div><table class="el-table"><thead><tr><th>认证编码</th><th>认证方式</th><th>令牌有效期</th><th>权限范围</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead><tbody><tr><td>AUTH001</td><td>OAuth2</td><td>7200秒</td><td>读/写</td><td>''' + switch_on + '''</td><td>2024-06-10</td><td><div class="actions"><a class="el-button--text">编辑</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(5) + '''</div>
    <div class="el-tabs__content" id="tab-int-analysis"><div class="filter-bar"><div class="filter-item"><label>接口名称</label><input class="el-input__inner" placeholder="请输入接口名称"></div><div class="filter-item"><label>时间范围</label><input class="el-input__inner" placeholder="开始时间">-<input class="el-input__inner" placeholder="结束时间" style="margin-left:4px"></div><button class="el-button el-button--primary">搜索</button></div><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>接口名称</th><th>调用次数</th><th>成功率</th><th>平均耗时</th><th>状态</th><th>时间</th><th>操作</th></tr></thead><tbody><tr><td>用户数据同步</td><td>12,580</td><td>99.8%</td><td>120ms</td><td>正常</td><td>2024-06-10</td><td><div class="actions"><a class="el-button--text">查看详情</a></div></td></tr></tbody></table>''' + pagination_html(15) + '''</div>
    <div class="el-tabs__content" id="tab-int-apilog"><div class="filter-bar"><div class="filter-item"><label>接口名称</label><input class="el-input__inner" placeholder="请输入接口名称"></div><div class="filter-item"><label>时间范围</label><input class="el-input__inner" placeholder="开始时间">-<input class="el-input__inner" placeholder="结束时间" style="margin-left:4px"></div><button class="el-button el-button--primary">搜索</button></div><div class="action-bar"><button class="el-button" onclick="showToast('刷新成功')">刷新</button><button class="el-button el-button--success" onclick="showToast('导出成功')">导出</button></div><table class="el-table"><thead><tr><th>日志ID</th><th>接口名称</th><th>请求方式</th><th>响应状态</th><th>耗时</th><th>调用时间</th><th>操作</th></tr></thead><tbody><tr><td>API001</td><td>用户数据同步</td><td>POST</td><td>200</td><td>120ms</td><td>2024-06-10 09:30</td><td><div class="actions"><a class="el-button--text">查看</a><a class="el-button--text">删除</a></div></td></tr></tbody></table>''' + pagination_html(18) + '''</div>
  </div></div>
</section>
'''


