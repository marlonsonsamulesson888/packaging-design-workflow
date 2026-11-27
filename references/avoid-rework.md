# 包装设计防返工手册

面向做彩盒、开窗盒、吊卡和餐具包装的人。用一张已确认的母版、一个实物尺寸基准和几项可复查的证据推进项目；不是印厂放行标准或自动验收工具。所有例子是通用说明，不取自客户工单。

## 每单只选自己用得到的检查

| 容易返工的地方 | 怎么检查 | 什么情况必须停 |
|---|---|---|
| 同盒产品被拉伸、头尾或工作面不一致 | 逐件核实总长、头宽、柄长和朝向，用同一比例排列。单件替换后回看全盒，同时核工作端和相邻同类件的倾角。 | SKU、尺寸来源或批准的方向不清，不凭画面猜。 |
| 抽拉外套与内托不配，开合图像是不同尺寸 | 在同组几何下核闭合、半开和俯视；半开只改行程，不挪缩零件。白样实装检查抽拉、止脱和全闭。 | 没有可核尺寸或白样，外观可以评审，不能放行结构。 |
| 凹槽能摆放，却没有真正固定 | 逐件核限位、盖合净空、取放和异响。吊卡把视觉装饰与真实固定结构分开。 | 未验固定件和实物装配，不把效果图当成运输或量产验证。 |
| 刀模转 3D 漏小舌、切口或折轴 | 对照原展开刀模列主盖、尾舌、锁舌、防尘翼、糊口和切口，以实际存在部件为准。逐项对应模型并检查实际打开图；闭盒图看不见时补证据视角。 | 部件缺失、被遮挡且无其他视图验证，不能判结构通过。 |
| 抠图毛边和真实产品细节被抹掉 | 深浅底放大检查叉齿、齿缝、孔洞和细柄；和原图逐一核对，不磨掉正常的轮廓、反光或纹样。 | 残线、白边或变形未修，不放进交付画面。 |
| 改一处却改了整套，或整盒需求只做局部 | 开工写清改动与保护范围。局部按同尺度比对确认稿和导出；整盒查正背侧顶底，保留已确认产品、文字及未授权变更的结构。 | 未确认的保护项有差异，或缺面，不用新稿替换母版。 |
| 看稿正确，导出却出现旧图层或错误版本 | 重开实际发出的文件，核版本、SKU、套数、刀线用途和图层可见性。按订单验证需要的可编辑性、转曲及分辨率。 | 有错误或关键证据未核，写明未通过或待核，不叫已完成或可送印。 |
| 技能包本地合格，但发布失败或跑错版本 | 先确认更新还是新建，逐包检查展示名、平台字段、引用和许可。若平台拒绝示例数量不一致，补齐对应双语样例后再重验。 | 本地 ZIP 通过不等于平台已审核、公开或在新会话可用。 |

**最小记录**：任务/版本｜适用检查｜实际看了什么｜通过/未通过/待验证/不适用｜证据｜下一步。先核容易返工的内容，再写交付结论。用与订单一致的材料、刀模和颜色要求；案例尺寸不是默认工艺值。

**虚构练习**：一款开窗礼盒有 3 件产品，示意效果里的最后一件被拉短且反放，打开图又看不出卡舌。先用三件实物尺寸和批准摆位纠正排布，再独立核对原刀模与开盒图。若白样未试装，交付状态只能写“外观可评审，结构待验证”。

## 已公开技能索引

这是已有仓库索引，不新装依赖，也不把第三方开源工具、私用资料或旧压缩包转成自有项目。以各仓库的当前许可、功能说明和适用范围为准。“—”表示本次公开账号清单未找到该名称；不是自动同步结果。

| 阶段 | 技能或项目 | 用来做什么 | GitHub | GitLab |
|---|---|---|---|---|
| 来稿与方案 | packaging-design-workflow | 从需求、方案到精修、3D 和交付 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-design-workflow) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-design-workflow) |
| 来稿与方案 | packaging-intake-router | 辨别缺资料、版本冲突和下一步 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-intake-router) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-intake-router) |
| 来稿与方案 | tableware-packaging-style | 比较原创视觉方向，保留已确认的产品事实 | [GitHub](https://github.com/marlonsonsamulesson888/tableware-packaging-style) | [GitLab](https://gitlab.com/marlonsonsamulesson/tableware-packaging-style) |
| 素材与视觉 | packaging-asset-mapper | 把真实素材对应到件型、套数和面位 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-asset-mapper) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-asset-mapper) |
| 素材与视觉 | product-cutout-preflight | 人工核对轮廓、透明边和金属保真 | [GitHub](https://github.com/marlonsonsamulesson888/product-cutout-preflight) | [GitLab](https://gitlab.com/marlonsonsamulesson/product-cutout-preflight) |
| 素材与视觉 | product-lighting-library | 做受控的灯光方向比较 | [GitHub](https://github.com/marlonsonsamulesson888/product-lighting-library) | [GitLab](https://gitlab.com/marlonsonsamulesson/product-lighting-library) |
| 结构与打样 | packaging-dieline-catalog | 归档和检索既有刀模，标明尺寸基准和验证状态 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-dieline-catalog) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-dieline-catalog) |
| 结构与打样 | packaging-die-pdf-measure | 读取矢量 PDF 的实际几何，不推定可生产 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-die-pdf-measure) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-die-pdf-measure) |
| 结构与打样 | window-box-cutlery-layout | 计算净空、排位、窗宽；不替代实物试装 | [GitHub](https://github.com/marlonsonsamulesson888/window-box-cutlery-layout) | [GitLab](https://gitlab.com/marlonsonsamulesson/window-box-cutlery-layout) |
| 结构与打样 | packaging-unboxing-review | 审阅开盖、展示和取出顺序 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-unboxing-review) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-unboxing-review) |
| 视觉和改稿验收 | packaging-3d-proofread | 核对视图、面位、方向和证据 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-3d-proofread) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-3d-proofread) |
| 视觉和改稿验收 | packaging-render-1to1-audit | 复量已标定的平面效果图，不适用于透视图 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-render-1to1-audit) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-render-1to1-audit) |
| 视觉和改稿验收 | packaging-revision-guard | 界定改动、保护项和版本证据 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-revision-guard) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-revision-guard) |
| 印前与归档 | factory-packaging-prepress | 核对工单、印厂要求及可交付证据 | [GitHub](https://github.com/marlonsonsamulesson888/factory-packaging-prepress) | [GitLab](https://gitlab.com/marlonsonsamulesson/factory-packaging-prepress) |
| 印前与归档 | packaging-delivery-export-check | 核导出文件，不代替打开原生稿 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-delivery-export-check) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-delivery-export-check) |
| 印前与归档 | packaging-project-archive | 保护原稿、核对归档副本与缺项 | [GitHub](https://github.com/marlonsonsamulesson888/packaging-project-archive) | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-project-archive) |
| 本地辅助 | packaging-svg-inventory | 只读盘点 SVG 尺寸、图层与外链 | — | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-svg-inventory) |
| 本地辅助 | packaging-zint-barcodes | 从已提供的数据生成符号；不分配商品编码 | — | [GitLab](https://gitlab.com/marlonsonsamulesson/packaging-zint-barcodes) |
| 项目辅助 | carton-orbit | 独立项目；并非每单的必需依赖 | [GitHub](https://github.com/marlonsonsamulesson888/carton-orbit) | — |

一单通常从来稿、结构、视觉或印前中选当前关卡，不必把所有工具都跑一遍。
