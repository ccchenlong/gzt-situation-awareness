# -*- coding: utf-8 -*-
import re, os, shutil

src = r'd:\00 云上江西\03 赣政通\需求设计\态势感知\gzt-prototype\index.html'
bak = src + '.bak'

# 备份
shutil.copy2(src, bak)

with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

switch_on = '<label class="switch"><input type="checkbox" checked><span class="slider"></span></label>'
switch_off = '<label class="switch"><input type="checkbox"><span class="slider"></span></label>'

def progress_html(val):
    return f'<div class="progress-bar"><div class="progress-fill" style="width:{val}%"></div></div><div class="progress-text">{val}%</div>'

def pagination_html(total):
    return f'<div class="pagination"><button>&lt;</button><button class="active">1</button><button>2</button><button>3</button><button>&gt;</button><span style="color:#909399;font-size:13px;">共 {total} 条</span></div>'

# ========== 新的数据转换提取配置模块 ==========
new_section = '''<section id="page-extract-config" class="page-section active"><div class="card"><div class="card-body"><div class="topbar-left" style="margin-bottom:16px;font-size:16px;">数据转换提取配置</div>
<div class="tabs"><div class="tab-item active" data-tab="tab-report" onclick="showTab('page-extract-config','tab-report')">报表导出配置</div><div class="tab-item" data-tab="tab-chart" onclick="showTab('page-extract-config','tab-chart')">图表导出配置</div></div>

<div id="tab-report" class="tab-panel active">
<div class="filter-bar">
<div class="form-item"><label>模板名称</label><input class="el-input" placeholder="请输入模板名称"></div>
<div class="form-item"><label>数据来源</label><select class="el-select"><option value="">全部</option><option>用户中心</option><option>待办中心</option><option>应用中心</option><option>行为日志</option><option>组织架构</option></select></div>
<div class="form-item"><label>导出格式</label><select class="el-select"><option value="">全部</option><option>CSV</option><option>Excel</option><option>PDF</option></select></div>
<div class="form-item"><label>状态</label><select class="el-select"><option value="">全部</option><option>启用</option><option>禁用</option></select></div>
<button class="btn btn-primary" onclick="showToast('查询成功')">搜索</button><button class="btn" onclick="showToast('已重置')">重置</button>
</div>
<div class="toolbar">
<div class="btn-group">
<button class="btn btn-primary" onclick="openDialog('新增报表导出模板','report-add')">+ 新增</button>
<button class="btn btn-danger" onclick="showToast('批量删除成功')">批量删除</button>
<button class="btn btn-success" onclick="openDialog('报表导出','report-export')">导出</button>
<button class="btn btn-info" onclick="openDialog('复制报表导出模板','report-copy')">复制</button>
<button class="btn btn-warning" onclick="openDialog('模板版本管理','version')">版本管理</button>
<button class="btn" onclick="openDialog('导出预览','preview')">预览</button>
<button class="btn" onclick="openDialog('导出历史记录','history')">历史记录</button>
<button class="btn" onclick="showToast('刷新成功')">刷新</button>
</div>
<div style="color:#909399;font-size:13px;">共 <span class="total-num">24</span> 条</div>
</div>
<table class="data-table"><thead><tr>
<th><input type="checkbox"></th>
<th>模板编码</th><th>模板名称</th><th>数据来源</th><th>导出格式</th>
<th>字段配置</th><th>排序规则</th><th>过滤条件</th><th>分页大小</th><th>是否脱敏</th><th>样式</th>
<th>状态</th><th>系统通知</th><th>导出进度</th><th>创建时间</th><th>操作</th>
</tr></thead><tbody>
<tr>
<td><input type="checkbox"></td>
<td>RPT001</td><td>月度活跃用户报表</td><td>用户中心</td><td>Excel</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按创建时间降序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>500</td><td>''' + switch_on + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(50) + '''</td><td>2024-01-15 09:23</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT002</td><td>待办事项办结统计</td><td>待办中心</td><td>CSV</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按办结时间升序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>1000</td><td>''' + switch_off + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_off + '''</td><td>''' + progress_html(100) + '''</td><td>2024-02-08 14:11</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT003</td><td>应用访问量排行</td><td>应用中心</td><td>PDF</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按访问量降序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>200</td><td>''' + switch_on + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(75) + '''</td><td>2024-03-22 10:45</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT004</td><td>用户登录行为分析</td><td>行为日志</td><td>Excel</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按登录时间降序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>800</td><td>''' + switch_on + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_off + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(30) + '''</td><td>2024-04-05 16:02</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT005</td><td>部门协同效率报表</td><td>组织架构</td><td>Excel</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按部门编码升序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>300</td><td>''' + switch_off + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_off + '''</td><td>''' + progress_html(100) + '''</td><td>2024-05-18 08:55</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT006</td><td>网络电话通话记录</td><td>通话服务</td><td>CSV</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按通话时长降序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>600</td><td>''' + switch_on + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(60) + '''</td><td>2024-06-30 11:38</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT007</td><td>日程安排汇总表</td><td>日程中心</td><td>PDF</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按日程时间升序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>400</td><td>''' + switch_off + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(90) + '''</td><td>2024-07-12 13:20</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT008</td><td>群组活跃度统计</td><td>群组中心</td><td>Excel</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按消息数降序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>700</td><td>''' + switch_on + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_off + '''</td><td>''' + progress_html(45) + '''</td><td>2024-08-25 09:50</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT009</td><td>区域用户分布报表</td><td>区域编码</td><td>Excel</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按区域编码升序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>350</td><td>''' + switch_on + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(100) + '''</td><td>2024-09-03 15:42</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>RPT010</td><td>系统对接调用统计</td><td>接口网关</td><td>CSV</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('字段配置','view-fields')">查看</a></td>
<td>按调用次数降序</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('过滤条件','view-filter')">查看</a></td>
<td>900</td><td>''' + switch_off + '''</td>
<td><span class="tag tag-blue">已配置</span> <a onclick="openDialog('样式配置','view-style')">查看</a></td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(20) + '''</td><td>2024-10-17 07:33</td>
<td><a onclick="openDialog('编辑报表导出模板','report-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制报表导出模板','report-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
</tbody></table>
''' + pagination_html(24) + '''
</div>

<div id="tab-chart" class="tab-panel">
<div class="filter-bar">
<div class="form-item"><label>模板名称</label><input class="el-input" placeholder="请输入模板名称"></div>
<div class="form-item"><label>图表类型</label><select class="el-select"><option value="">全部</option><option>折线图</option><option>柱状图</option><option>饼图</option><option>面积图</option></select></div>
<div class="form-item"><label>数据源</label><select class="el-select"><option value="">全部</option><option>用户中心</option><option>待办中心</option><option>应用中心</option><option>行为日志</option><option>组织架构</option></select></div>
<div class="form-item"><label>状态</label><select class="el-select"><option value="">全部</option><option>启用</option><option>禁用</option></select></div>
<button class="btn btn-primary" onclick="showToast('查询成功')">搜索</button><button class="btn" onclick="showToast('已重置')">重置</button>
</div>
<div class="toolbar">
<div class="btn-group">
<button class="btn btn-primary" onclick="openDialog('新增图表导出模板','chart-add')">+ 新增</button>
<button class="btn btn-danger" onclick="showToast('批量删除成功')">批量删除</button>
<button class="btn btn-success" onclick="openDialog('图表导出','chart-export')">导出</button>
<button class="btn btn-info" onclick="openDialog('复制图表导出模板','chart-copy')">复制</button>
<button class="btn btn-warning" onclick="openDialog('模板版本管理','version')">版本管理</button>
<button class="btn" onclick="openDialog('图表组合','chart-combine')">组合</button>
<button class="btn" onclick="openDialog('导出预览','preview')">预览</button>
<button class="btn" onclick="openDialog('导出历史记录','history')">历史记录</button>
<button class="btn" onclick="showToast('刷新成功')">刷新</button>
</div>
<div style="color:#909399;font-size:13px;">共 <span class="total-num">18</span> 条</div>
</div>
<table class="data-table"><thead><tr>
<th><input type="checkbox"></th>
<th>模板编码</th><th>模板名称</th><th>数据源</th><th>图表类型</th><th>图表组合</th><th>数据表配置</th>
<th>样式与布局</th><th>交互配置</th><th>导出格式</th><th>分辨率</th><th>是否分页</th><th>是否脱敏</th>
<th>状态</th><th>系统通知</th><th>导出进度</th><th>创建时间</th><th>操作</th>
</tr></thead><tbody>
<tr>
<td><input type="checkbox"></td>
<td>CHT001</td><td>用户增长趋势图</td><td>用户中心</td><td>折线图</td>
<td><span class="tag tag-green">已组合3个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>PNG</td><td>1920x1080</td><td>''' + switch_on + '''</td><td>''' + switch_on + '''</td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(100) + '''</td><td>2024-01-20 10:00</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>CHT002</td><td>待办办结对比图</td><td>待办中心</td><td>柱状图</td>
<td><span class="tag tag-green">已组合2个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>JPG</td><td>1280x720</td><td>''' + switch_off + '''</td><td>''' + switch_off + '''</td>
<td>''' + switch_on + '''</td><td>''' + switch_off + '''</td><td>''' + progress_html(80) + '''</td><td>2024-02-14 11:30</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>CHT003</td><td>应用使用占比</td><td>应用中心</td><td>饼图</td>
<td><span class="tag tag-green">已组合1个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>PNG</td><td>1024x768</td><td>''' + switch_off + '''</td><td>''' + switch_on + '''</td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(100) + '''</td><td>2024-03-08 14:20</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>CHT004</td><td>登录时段分布</td><td>行为日志</td><td>面积图</td>
<td><span class="tag tag-green">已组合4个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>SVG</td><td>1920x1080</td><td>''' + switch_on + '''</td><td>''' + switch_on + '''</td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(55) + '''</td><td>2024-04-22 09:10</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>CHT005</td><td>部门任务完成率</td><td>组织架构</td><td>柱状图</td>
<td><span class="tag tag-green">已组合2个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>PNG</td><td>1600x900</td><td>''' + switch_on + '''</td><td>''' + switch_off + '''</td>
<td>''' + switch_off + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(40) + '''</td><td>2024-05-30 16:45</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>CHT006</td><td>通话时长趋势</td><td>通话服务</td><td>折线图</td>
<td><span class="tag tag-green">已组合3个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>JPG</td><td>1920x1080</td><td>''' + switch_off + '''</td><td>''' + switch_on + '''</td>
<td>''' + switch_on + '''</td><td>''' + switch_off + '''</td><td>''' + progress_html(100) + '''</td><td>2024-06-18 08:25</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>CHT007</td><td>日程类型分布</td><td>日程中心</td><td>饼图</td>
<td><span class="tag tag-green">已组合1个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>PNG</td><td>1280x720</td><td>''' + switch_off + '''</td><td>''' + switch_off + '''</td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(90) + '''</td><td>2024-07-25 13:15</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
<tr>
<td><input type="checkbox"></td>
<td>CHT008</td><td>群组消息热度</td><td>群组中心</td><td>面积图</td>
<td><span class="tag tag-green">已组合2个</span> <a onclick="openDialog('图表组合详情','chart-combine')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('数据表配置','view-table-config')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('样式与布局','view-layout')">查看</a></td>
<td><span class="tag tag-green">已配置</span> <a onclick="openDialog('交互配置','view-interaction')">查看</a></td>
<td>SVG</td><td>1920x1080</td><td>''' + switch_on + '''</td><td>''' + switch_on + '''</td>
<td>''' + switch_on + '''</td><td>''' + switch_on + '''</td><td>''' + progress_html(65) + '''</td><td>2024-08-09 10:50</td>
<td><a onclick="openDialog('编辑图表导出模板','chart-edit')">编辑</a> <a onclick="showToast('删除成功')">删除</a> <a onclick="openDialog('复制图表导出模板','chart-copy')">复制</a> <a onclick="openDialog('模板版本管理','version')">版本</a> <a onclick="openDialog('修改记录','modify-record')">修改记录</a> <a onclick="openDialog('导出预览','preview')">预览</a> <a onclick="openDialog('导出进度','view-progress')">进度</a></td>
</tr>
</tbody></table>
''' + pagination_html(18) + '''
</div>
</div></div></section>'''

# ========== 新的 DIALOG_CONTENTS ==========
new_dialog = '''var DIALOG_CONTENTS = {
  "report-add": `<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>模板名称</label><input class="el-input" placeholder="请输入模板名称"></div><div class="form-item2"><label class="form-label"><span class="required">*</span>模板编码</label><input class="el-input" placeholder="请输入模板编码"></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>数据来源</label><select class="el-select"><option>用户中心</option><option>待办中心</option><option>应用中心</option><option>行为日志</option><option>组织架构</option></select></div><div class="form-item2"><label class="form-label"><span class="required">*</span>导出格式</label><select class="el-select"><option>CSV</option><option>Excel</option><option>PDF</option></select></div></div>
<div class="form-item-full"><label class="form-label">字段配置</label>
<div class="transfer-box"><div class="transfer-panel"><div class="transfer-header">待选字段</div><div class="transfer-list"><div class="transfer-item">用户ID</div><div class="transfer-item">用户姓名</div><div class="transfer-item">所属单位</div><div class="transfer-item">登录时间</div><div class="transfer-item">操作类型</div></div></div><div class="transfer-btns"><button>&gt;</button><button>&gt;&gt;</button><button>&lt;</button><button>&lt;&lt;</button></div><div class="transfer-panel"><div class="transfer-header">已选字段</div><div class="transfer-list"><div class="transfer-item">用户ID</div><div class="transfer-item">用户姓名</div></div></div></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">排序规则</label><select class="el-select"><option>按创建时间降序</option><option>按创建时间升序</option><option>按编码升序</option><option>按编码降序</option></select></div><div class="form-item2"><label class="form-label">分页大小</label><input class="el-input" value="500" placeholder="请输入分页大小"></div></div>
<div class="form-item-full"><label class="form-label">过滤条件</label><textarea class="el-textarea" placeholder="请输入过滤条件"></textarea></div>
<div class="form-row"><div class="form-item2"><label class="form-label">样式配置-表头颜色</label><input class="el-input" value="#409EFF" placeholder="表头颜色"></div><div class="form-item2"><label class="form-label">样式配置-字体大小</label><select class="el-select"><option>12px</option><option>14px</option><option>16px</option></select></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">数据脱敏</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div><div class="form-item2"><label class="form-label">系统通知</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">状态</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>`,
  "report-edit": `<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>模板名称</label><input class="el-input" value="月度活跃用户报表"></div><div class="form-item2"><label class="form-label"><span class="required">*</span>模板编码</label><input class="el-input" value="RPT001" readonly></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>数据来源</label><select class="el-select"><option selected>用户中心</option><option>待办中心</option><option>应用中心</option><option>行为日志</option><option>组织架构</option></select></div><div class="form-item2"><label class="form-label"><span class="required">*</span>导出格式</label><select class="el-select"><option>CSV</option><option selected>Excel</option><option>PDF</option></select></div></div>
<div class="form-item-full"><label class="form-label">字段配置</label>
<div class="transfer-box"><div class="transfer-panel"><div class="transfer-header">待选字段</div><div class="transfer-list"><div class="transfer-item">用户ID</div><div class="transfer-item">用户姓名</div><div class="transfer-item">所属单位</div><div class="transfer-item">登录时间</div><div class="transfer-item">操作类型</div></div></div><div class="transfer-btns"><button>&gt;</button><button>&gt;&gt;</button><button>&lt;</button><button>&lt;&lt;</button></div><div class="transfer-panel"><div class="transfer-header">已选字段</div><div class="transfer-list"><div class="transfer-item">用户ID</div><div class="transfer-item">用户姓名</div></div></div></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">排序规则</label><select class="el-select"><option selected>按创建时间降序</option><option>按创建时间升序</option><option>按编码升序</option><option>按编码降序</option></select></div><div class="form-item2"><label class="form-label">分页大小</label><input class="el-input" value="500" placeholder="请输入分页大小"></div></div>
<div class="form-item-full"><label class="form-label">过滤条件</label><textarea class="el-textarea" placeholder="请输入过滤条件"></textarea></div>
<div class="form-row"><div class="form-item2"><label class="form-label">样式配置-表头颜色</label><input class="el-input" value="#409EFF" placeholder="表头颜色"></div><div class="form-item2"><label class="form-label">样式配置-字体大小</label><select class="el-select"><option>12px</option><option selected>14px</option><option>16px</option></select></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">数据脱敏</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div><div class="form-item2"><label class="form-label">系统通知</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">状态</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>`,
  "chart-add": `<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>模板名称</label><input class="el-input" placeholder="请输入模板名称"></div><div class="form-item2"><label class="form-label"><span class="required">*</span>模板编码</label><input class="el-input" placeholder="请输入模板编码"></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>数据源</label><select class="el-select"><option>用户中心</option><option>待办中心</option><option>应用中心</option><option>行为日志</option><option>组织架构</option></select></div><div class="form-item2"><label class="form-label"><span class="required">*</span>图表类型</label><select class="el-select"><option>折线图</option><option>柱状图</option><option>饼图</option><option>面积图</option></select></div></div>
<div class="form-item-full"><label class="form-label">数据表配置</label>
<div class="transfer-box"><div class="transfer-panel"><div class="transfer-header">待选数据表</div><div class="transfer-list"><div class="transfer-item">用户表</div><div class="transfer-item">待办表</div><div class="transfer-item">应用表</div><div class="transfer-item">行为日志表</div></div></div><div class="transfer-btns"><button>&gt;</button><button>&gt;&gt;</button><button>&lt;</button><button>&lt;&lt;</button></div><div class="transfer-panel"><div class="transfer-header">已选数据表</div><div class="transfer-list"><div class="transfer-item">用户表</div></div></div></div></div>
<div class="form-item-full"><label class="form-label">图表组合</label>
<div class="transfer-box"><div class="transfer-panel"><div class="transfer-header">待选图表</div><div class="transfer-list"><div class="transfer-item">用户增长趋势图</div><div class="transfer-item">待办办结对比图</div><div class="transfer-item">应用使用占比</div><div class="transfer-item">登录时段分布</div></div></div><div class="transfer-btns"><button>&gt;</button><button>&gt;&gt;</button><button>&lt;</button><button>&lt;&lt;</button></div><div class="transfer-panel"><div class="transfer-header">已组合图表</div><div class="transfer-list"><div class="transfer-item">用户增长趋势图</div></div></div></div></div>
<div class="form-item-full"><label class="form-label">交互配置</label><div style="display:flex;gap:16px;align-items:center;height:32px;"><label style="color:#606266;cursor:pointer;"><input type="checkbox" checked> 启用下钻</label><label style="color:#606266;cursor:pointer;"><input type="checkbox" checked> 悬停提示</label><label style="color:#606266;cursor:pointer;"><input type="checkbox"> 图例点击</label></div></div>
<div class="form-row"><div class="form-item-full"><label class="form-label">样式与布局</label><textarea class="el-textarea" placeholder="颜色、字体、图例位置、标题样式等"></textarea></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>导出格式</label><select class="el-select"><option>PNG</option><option>JPG</option><option>SVG</option><option>PDF</option></select></div><div class="form-item2"><label class="form-label"><span class="required">*</span>分辨率</label><select class="el-select"><option>1920x1080</option><option>1280x720</option><option>1024x768</option><option>1600x900</option></select></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">是否分页</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div><div class="form-item2"><label class="form-label">数据脱敏</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">状态</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div><div class="form-item2"><label class="form-label">系统通知</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>`,
  "chart-edit": `<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>模板名称</label><input class="el-input" value="用户增长趋势图"></div><div class="form-item2"><label class="form-label"><span class="required">*</span>模板编码</label><input class="el-input" value="CHT001" readonly></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>数据源</label><select class="el-select"><option selected>用户中心</option><option>待办中心</option><option>应用中心</option><option>行为日志</option><option>组织架构</option></select></div><div class="form-item2"><label class="form-label"><span class="required">*</span>图表类型</label><select class="el-select"><option selected>折线图</option><option>柱状图</option><option>饼图</option><option>面积图</option></select></div></div>
<div class="form-item-full"><label class="form-label">数据表配置</label>
<div class="transfer-box"><div class="transfer-panel"><div class="transfer-header">待选数据表</div><div class="transfer-list"><div class="transfer-item">用户表</div><div class="transfer-item">待办表</div><div class="transfer-item">应用表</div><div class="transfer-item">行为日志表</div></div></div><div class="transfer-btns"><button>&gt;</button><button>&gt;&gt;</button><button>&lt;</button><button>&lt;&lt;</button></div><div class="transfer-panel"><div class="transfer-header">已选数据表</div><div class="transfer-list"><div class="transfer-item">用户表</div></div></div></div></div>
<div class="form-item-full"><label class="form-label">图表组合</label>
<div class="transfer-box"><div class="transfer-panel"><div class="transfer-header">待选图表</div><div class="transfer-list"><div class="transfer-item">用户增长趋势图</div><div class="transfer-item">待办办结对比图</div><div class="transfer-item">应用使用占比</div><div class="transfer-item">登录时段分布</div></div></div><div class="transfer-btns"><button>&gt;</button><button>&gt;&gt;</button><button>&lt;</button><button>&lt;&lt;</button></div><div class="transfer-panel"><div class="transfer-header">已组合图表</div><div class="transfer-list"><div class="transfer-item">用户增长趋势图</div></div></div></div></div>
<div class="form-item-full"><label class="form-label">交互配置</label><div style="display:flex;gap:16px;align-items:center;height:32px;"><label style="color:#606266;cursor:pointer;"><input type="checkbox" checked> 启用下钻</label><label style="color:#606266;cursor:pointer;"><input type="checkbox" checked> 悬停提示</label><label style="color:#606266;cursor:pointer;"><input type="checkbox"> 图例点击</label></div></div>
<div class="form-row"><div class="form-item-full"><label class="form-label">样式与布局</label><textarea class="el-textarea" placeholder="颜色、字体、图例位置、标题样式等"></textarea></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>导出格式</label><select class="el-select"><option selected>PNG</option><option>JPG</option><option>SVG</option><option>PDF</option></select></div><div class="form-item2"><label class="form-label"><span class="required">*</span>分辨率</label><select class="el-select"><option selected>1920x1080</option><option>1280x720</option><option>1024x768</option><option>1600x900</option></select></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">是否分页</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div><div class="form-item2"><label class="form-label">数据脱敏</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label">状态</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div><div class="form-item2"><label class="form-label">系统通知</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>`,
  "version": `<h4 style="margin-bottom:12px;color:#303133;">版本历史</h4><table class="data-table"><thead><tr><th>版本号</th><th>修改人</th><th>修改时间</th><th>修改说明</th><th>操作</th></tr></thead><tbody><tr><td>v1.3</td><td>张三</td><td>2024-10-10 09:00</td><td>修复字段排序问题</td><td><a onclick="showToast('回滚成功')">回滚</a> <a>查看</a></td></tr><tr><td>v1.2</td><td>李四</td><td>2024-09-20 15:30</td><td>新增脱敏配置</td><td><a onclick="showToast('回滚成功')">回滚</a> <a>查看</a></td></tr><tr><td>v1.1</td><td>王五</td><td>2024-08-12 11:20</td><td>优化导出格式</td><td><a onclick="showToast('回滚成功')">回滚</a> <a>查看</a></td></tr><tr><td>v1.0</td><td>赵六</td><td>2024-07-01 08:00</td><td>初始版本</td><td><a onclick="showToast('回滚成功')">回滚</a> <a>查看</a></td></tr></tbody></table>`,
  "modify-record": `<h4 style="margin-bottom:12px;color:#303133;">修改记录</h4><table class="data-table"><thead><tr><th>修改时间</th><th>修改人</th><th>修改字段</th><th>修改前</th><th>修改后</th></tr></thead><tbody><tr><td>2024-10-10 09:00</td><td>张三</td><td>分页大小</td><td>500</td><td>1000</td></tr><tr><td>2024-10-09 16:30</td><td>李四</td><td>是否脱敏</td><td>否</td><td>是</td></tr><tr><td>2024-10-08 10:15</td><td>王五</td><td>导出格式</td><td>CSV</td><td>Excel</td></tr><tr><td>2024-10-07 14:20</td><td>赵六</td><td>状态</td><td>禁用</td><td>启用</td></tr></tbody></table>`,
  "history": `<h4 style="margin-bottom:12px;color:#303133;">导出历史记录</h4><table class="data-table"><thead><tr><th>导出时间</th><th>模板名称</th><th>导出格式</th><th>文件大小</th><th>导出状态</th><th>操作</th></tr></thead><tbody><tr><td>2024-10-11 10:00</td><td>月度活跃用户报表</td><td>Excel</td><td>2.5MB</td><td>成功</td><td><a onclick="showToast('开始重新导出')">重新导出</a> <a>下载</a></td></tr><tr><td>2024-10-10 09:30</td><td>待办事项办结统计</td><td>CSV</td><td>1.2MB</td><td>成功</td><td><a onclick="showToast('开始重新导出')">重新导出</a> <a>下载</a></td></tr><tr><td>2024-10-09 17:00</td><td>应用访问量排行</td><td>PDF</td><td>3.8MB</td><td>失败</td><td><a onclick="showToast('开始重新导出')">重新导出</a> <a>下载</a></td></tr><tr><td>2024-10-08 11:20</td><td>用户登录行为分析</td><td>Excel</td><td>5.1MB</td><td>成功</td><td><a onclick="showToast('开始重新导出')">重新导出</a> <a>下载</a></td></tr></tbody></table>`,
  "preview": `<div class="preview-box" style="margin-bottom:12px;border:1px dashed #dcdfe6;border-radius:4px;padding:20px;background:#fafafa;"><h4 style="margin-bottom:12px;color:#303133;">导出预览</h4><table class="data-table"><thead><tr><th>序号</th><th>指标</th><th>数值</th></tr></thead><tbody><tr><td>1</td><td>活跃用户数</td><td>12,580</td></tr><tr><td>2</td><td>新增用户数</td><td>1,230</td></tr><tr><td>3</td><td>登录次数</td><td>45,670</td></tr><tr><td>4</td><td>待办办结数</td><td>8,920</td></tr><tr><td>5</td><td>应用访问次数</td><td>34,120</td></tr></tbody></table></div><div style="text-align:center;color:#909399;">导出进度：100%</div>`,
  "chart-combine": `<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>组合名称</label><input class="el-input" placeholder="请输入组合名称"></div></div>
<div class="form-item-full"><label class="form-label">选择图表（将多个图表组合到一个导出文件中）</label>
<div class="transfer-box"><div class="transfer-panel"><div class="transfer-header">待选图表</div><div class="transfer-list"><div class="transfer-item">用户增长趋势图</div><div class="transfer-item">待办办结对比图</div><div class="transfer-item">应用使用占比</div><div class="transfer-item">登录时段分布</div><div class="transfer-item">部门任务完成率</div></div></div><div class="transfer-btns"><button>&gt;</button><button>&gt;&gt;</button><button>&lt;</button><button>&lt;&lt;</button></div><div class="transfer-panel"><div class="transfer-header">已组合图表</div><div class="transfer-list"><div class="transfer-item">用户增长趋势图</div><div class="transfer-item">待办办结对比图</div></div></div></div></div>
<div class="form-row"><div class="form-item2"><label class="form-label"><span class="required">*</span>导出格式</label><select class="el-select"><option>PNG</option><option>JPG</option><option>SVG</option><option>PDF</option></select></div><div class="form-item2"><label class="form-label"><span class="required">*</span>布局方式</label><select class="el-select"><option>横向排列</option><option>纵向排列</option><option>网格排列</option></select></div></div>`,
  "report-export": `<h4 style="margin-bottom:12px;color:#303133;">报表导出</h4><div class="form-row"><div class="form-item2"><label class="form-label">选择模板</label><select class="el-select"><option>月度活跃用户报表</option><option>待办事项办结统计</option><option>应用访问量排行</option></select></div><div class="form-item2"><label class="form-label">导出格式</label><select class="el-select"><option>Excel</option><option>CSV</option><option>PDF</option></select></div></div><div class="form-row"><div class="form-item2"><label class="form-label">分页大小</label><input class="el-input" value="500"></div><div class="form-item2"><label class="form-label">数据脱敏</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div><div class="form-item-full"><label class="form-label">导出进度</label><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><div class="progress-text">等待导出</div></div>`,
  "chart-export": `<h4 style="margin-bottom:12px;color:#303133;">图表导出</h4><div class="form-row"><div class="form-item2"><label class="form-label">选择模板</label><select class="el-select"><option>用户增长趋势图</option><option>待办办结对比图</option><option>应用使用占比</option></select></div><div class="form-item2"><label class="form-label">导出格式</label><select class="el-select"><option>PNG</option><option>JPG</option><option>SVG</option><option>PDF</option></select></div></div><div class="form-row"><div class="form-item2"><label class="form-label">分辨率</label><select class="el-select"><option>1920x1080</option><option>1280x720</option></select></div><div class="form-item2"><label class="form-label">是否分页</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div><div class="form-item-full"><label class="form-label">导出进度</label><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><div class="progress-text">等待导出</div></div>`,
  "report-copy": `<h4 style="margin-bottom:12px;color:#303133;">复制报表导出模板</h4><div class="form-row"><div class="form-item2"><label class="form-label">原模板名称</label><input class="el-input" value="月度活跃用户报表" readonly></div><div class="form-item2"><label class="form-label">新模板名称</label><input class="el-input" value="月度活跃用户报表_副本"></div></div><div class="form-row"><div class="form-item2"><label class="form-label">新模板编码</label><input class="el-input" value="RPT001_COPY"></div><div class="form-item2"><label class="form-label">导出格式</label><select class="el-select"><option selected>Excel</option><option>CSV</option><option>PDF</option></select></div></div><div class="form-item-full" style="color:#909399;font-size:13px;">将复制原模板的字段、排序规则、过滤条件、样式等全部配置。</div>`,
  "chart-copy": `<h4 style="margin-bottom:12px;color:#303133;">复制图表导出模板</h4><div class="form-row"><div class="form-item2"><label class="form-label">原模板名称</label><input class="el-input" value="用户增长趋势图" readonly></div><div class="form-item2"><label class="form-label">新模板名称</label><input class="el-input" value="用户增长趋势图_副本"></div></div><div class="form-row"><div class="form-item2"><label class="form-label">新模板编码</label><input class="el-input" value="CHT001_COPY"></div><div class="form-item2"><label class="form-label">图表类型</label><select class="el-select"><option selected>折线图</option><option>柱状图</option><option>饼图</option><option>面积图</option></select></div></div><div class="form-item-full" style="color:#909399;font-size:13px;">将复制原模板的图表类型、数据源、组合、样式布局等全部配置。</div>`,
  "view-fields": `<h4 style="margin-bottom:12px;color:#303133;">字段配置</h4><table class="data-table"><thead><tr><th>字段名</th><th>字段类型</th><th>显示名称</th><th>是否导出</th><th>排序</th></tr></thead><tbody><tr><td>user_id</td><td>字符串</td><td>用户ID</td><td>是</td><td>1</td></tr><tr><td>user_name</td><td>字符串</td><td>用户姓名</td><td>是</td><td>2</td></tr><tr><td>dept_name</td><td>字符串</td><td>所属部门</td><td>否</td><td>3</td></tr><tr><td>login_time</td><td>日期时间</td><td>登录时间</td><td>是</td><td>4</td></tr></tbody></table>`,
  "view-filter": `<h4 style="margin-bottom:12px;color:#303133;">过滤条件配置</h4><table class="data-table"><thead><tr><th>字段</th><th>条件</th><th>值</th><th>逻辑</th></tr></thead><tbody><tr><td>login_time</td><td>大于等于</td><td>2024-01-01</td><td>且</td></tr><tr><td>status</td><td>等于</td><td>启用</td><td>且</td></tr><tr><td>dept_id</td><td>包含</td><td>D001,D002</td><td>或</td></tr></tbody></table>`,
  "view-style": `<h4 style="margin-bottom:12px;color:#303133;">样式配置</h4><div class="form-row"><div class="form-item2"><label class="form-label">表头背景色</label><input class="el-input" value="#409EFF"></div><div class="form-item2"><label class="form-label">表头字体颜色</label><input class="el-input" value="#FFFFFF"></div></div><div class="form-row"><div class="form-item2"><label class="form-label">正文字体大小</label><select class="el-select"><option>12px</option><option selected>14px</option><option>16px</option></select></div><div class="form-item2"><label class="form-label">行高</label><input class="el-input" value="32px"></div></div><div class="form-row"><div class="form-item2"><label class="form-label">边框样式</label><select class="el-select"><option>实线</option><option>虚线</option><option>无</option></select></div><div class="form-item2"><label class="form-label">是否自动换行</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>`,
  "view-table-config": `<h4 style="margin-bottom:12px;color:#303133;">数据表配置</h4><table class="data-table"><thead><tr><th>数据表</th><th>关联字段</th><th>关联方式</th><th>数据来源</th></tr></thead><tbody><tr><td>用户表</td><td>user_id</td><td>左连接</td><td>用户中心</td></tr><tr><td>登录日志表</td><td>user_id</td><td>内连接</td><td>行为日志</td></tr><tr><td>单位表</td><td>unit_id</td><td>左连接</td><td>组织架构</td></tr></tbody></table>`,
  "view-layout": `<h4 style="margin-bottom:12px;color:#303133;">样式与布局配置</h4><div class="form-row"><div class="form-item2"><label class="form-label">主题颜色</label><input class="el-input" value="#409EFF"></div><div class="form-item2"><label class="form-label">字体</label><select class="el-select"><option>微软雅黑</option><option>宋体</option><option>黑体</option></select></div></div><div class="form-row"><div class="form-item2"><label class="form-label">图例位置</label><select class="el-select"><option>顶部</option><option>底部</option><option>左侧</option><option>右侧</option></select></div><div class="form-item2"><label class="form-label">标题样式</label><input class="el-input" value="18px 加粗"></div></div><div class="form-row"><div class="form-item2"><label class="form-label">背景色</label><input class="el-input" value="#FFFFFF"></div><div class="form-item2"><label class="form-label">网格线</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div>`,
  "view-interaction": `<h4 style="margin-bottom:12px;color:#303133;">交互配置</h4><table class="data-table"><thead><tr><th>交互类型</th><th>是否启用</th><th>说明</th></tr></thead><tbody><tr><td>下钻</td><td>是</td><td>点击图表元素可下钻查看明细</td></tr><tr><td>悬停提示</td><td>是</td><td>鼠标悬停显示数据详情</td></tr><tr><td>图例点击</td><td>否</td><td>点击图例可隐藏/显示对应系列</td></tr><tr><td>数据缩放</td><td>是</td><td>支持区域缩放查看</td></tr></tbody></table>`,
  "view-datasource": `<h4 style="margin-bottom:12px;color:#303133;">数据源配置</h4><table class="data-table"><thead><tr><th>数据源名称</th><th>数据源类型</th><th>连接方式</th><th>状态</th></tr></thead><tbody><tr><td>用户中心</td><td>MySQL</td><td>JDBC</td><td>正常</td></tr><tr><td>待办中心</td><td>MySQL</td><td>JDBC</td><td>正常</td></tr><tr><td>应用中心</td><td>Oracle</td><td>JDBC</td><td>正常</td></tr><tr><td>行为日志</td><td>Elasticsearch</td><td>REST API</td><td>正常</td></tr></tbody></table>`,
  "view-progress": `<h4 style="margin-bottom:12px;color:#303133;">导出进度详情</h4><div style="margin-bottom:16px;"><div style="display:flex;justify-content:space-between;margin-bottom:6px;color:#606266;"><span>任务ID：EXP-202410110001</span><span>状态：导出中</span></div><div class="progress-bar"><div class="progress-fill" style="width:65%"></div></div><div class="progress-text">65%</div></div><table class="data-table"><thead><tr><th>阶段</th><th>状态</th><th>开始时间</th><th>结束时间</th></tr></thead><tbody><tr><td>数据读取</td><td>已完成</td><td>10:00:00</td><td>10:00:15</td></tr><tr><td>数据转换</td><td>已完成</td><td>10:00:16</td><td>10:00:45</td></tr><tr><td>文件生成</td><td>进行中</td><td>10:00:46</td><td>--</td></tr><tr><td>文件上传</td><td>待开始</td><td>--</td><td>--</td></tr></tbody></table>`,
  "view-notify": `<h4 style="margin-bottom:12px;color:#303133;">系统通知配置</h4><div class="form-row"><div class="form-item2"><label class="form-label">启用邮件通知</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div><div class="form-item2"><label class="form-label">启用站内信通知</label><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div></div><div class="form-row"><div class="form-item-full"><label class="form-label">通知接收人</label><input class="el-input" value="管理员; 张三; 李四"></div></div><div class="form-row"><div class="form-item-full"><label class="form-label">通知模板</label><textarea class="el-textarea">您的导出任务已完成，请及时下载。</textarea></div></div>`,
};'''

# 替换 section
m = re.search(r'<section id="page-extract-config".*?</section>', html, re.DOTALL)
if not m:
    raise RuntimeError('未找到 page-extract-config section')
html = html[:m.start()] + new_section + html[m.end():]

# 替换 DIALOG_CONTENTS
m2 = re.search(r'var DIALOG_CONTENTS = \{.*?\};', html, re.DOTALL)
if not m2:
    raise RuntimeError('未找到 DIALOG_CONTENTS')
html = html[:m2.start()] + new_dialog + html[m2.end():]

with open(src, 'w', encoding='utf-8') as f:
    f.write(html)

print('替换完成，已备份至', bak)
