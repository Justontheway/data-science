## matplotlib
* matplotlib API包含三层
    * backend_bases.FigureCanvas 图表的绘制领域
    * backend_bases.Renderer 知道如何在FigureCanvas上绘图
    * artist.Artist 知道如何使用Renderer在FigureCanvas上绘图
* FigureCanvas和Renderer需要处理底层的绘图操作
* Artist负责处理所有的高层结构,例如处理图标、文字、曲线等的绘制和布局
* 绘图的标准流程是
    * 创建Figure对象
    * 用Figure对象创建一个或多个Axes或者Subplot对象
    * 调用Axies等对象的方法创建各种简单类型的Artists
### Artist
* Artists分为
    * 简单类型 - Line2D Rectangle Text AxesImage等
    * 容器类型 - 可以包含很多简单类型,使他们组成一个整体,Axis/Axes/Figure等
* 图表中的每个元素都是一个Artist对象,每个Figure和Axes对象都有一个patch属性作为背景
* 每个Artist对象都有的属性,这些属性都通过get_* set_*进行读写
    * alpha 透明度, 0~1 完全透明~完全不透明
    * animated 布尔值,绘制动画效果时使用
    * axes 此Artist对象所在的Axes对象,可能为None
    * clip_box 对象的裁剪框
    * clip_on 是否裁剪
    * clip_path 裁剪的路径
    * contains 判断指定点是否在对象上的函数
    * figure 所在的Figure对象,可能为None
    * label 文本标签
    * picker 控制Artist对象选取
    * transform 控制偏移旋转
    * visible 是否可见
    * zorder 控制绘图顺序
#### Figure容器
* 其中最大的容器类型是Figure,它包括组成图表的所有元素
* Figure包含axes patch patches images legends lines texts等属性
#### Axes容器
* Axes容器是整个matplotlib的核心,它包含了组成图表的众多Artist对象,并且有许多方法函数帮助创建、修改这些对象.
* 它有一个patch作为背景
#### Axis容器
* Axis容器包括坐标轴上的刻度线、刻度文本、坐标网格以及坐标轴标题等内容
* 刻度分为主刻度和副刻度,每个刻度都是一个XTick或者YTick对象,它包括实际的刻度线和刻度文本





