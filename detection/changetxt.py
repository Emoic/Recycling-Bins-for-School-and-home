

m=0
a=b=0
paper='备覆盖率上升是因为银行感到后期不良贷款增长有反弹的压力，因此半年报中都显示有加大计提的迹象。今年4月30日银保监会对商业银行金融资产风险分类暂行办法进行了征求意见，未来分类的要求会更高，所以处置压力会上升。但拨备覆盖率上限制定为最低标准的2倍，是合理的。”国家金融与发展实验室特聘研究员董希淼表示'
others=' 砖瓦 陶瓷 渣土 餐巾纸 一次性餐具 卫生纸 尿不湿 妇女卫生用品 烟蒂 打火机 渣土 陶瓷 碗碟 骨头 植物 硬壳 花草 拖把 抹布 牙签 一次性筷子 树枝 餐巾纸 旧浴缸 盆子 坏马桶 旧水槽 贝壳 化妆刷 坛子 海锦 花生壳 菜板 砖块 卫生纸 篮球 桃核 杯子 陶瓷碗 一次性筷子 西梅核 坏的花盆 木质梳子 脏污衣服 烟蒂 渣土 湿垃圾袋 瓦片 扫把 '
kitchen=' 木瓜 草莓 玉米油 米糠油 芝麻油 橘子 柑子 猕猴桃 花生 开心果 腰果 松子 糙米饭 猪肝 杏仁 大豆芒果 杏 柿子 西瓜 菜叶 橙皮 饼干 狗 番茄酱 蛋壳 西瓜皮 马铃薯 剩菜 死鱼 死老鼠 蟑螂 剩饭 菜叶 果皮 蛋壳 茶渣 骨 贝壳 鱼骨 甘蔗 玉米 骨头 鸡骨头 鸭骨头 鹅骨头 虾壳 蛋糕 面包 草莓 西红柿 梨 蟹壳 香蕉皮 辣椒 巧克力 茄子 豌豆皮 苹果 树叶'
recycle=' 金属瓶罐 易拉罐 食品罐 金属厨具 菜刀 锅 金属工具 旧衣服 床单 枕头 棉被 皮鞋 毛绒玩具 布偶 ' \
        '棉袄 包 皮带 丝绸制品 刀片 指甲剪 螺丝刀 金属制品 铁钉 铁皮 铝箔 易拉罐 调料瓶 酒瓶 化妆品瓶 玻璃杯 窗玻璃 ' \
        '玻璃制品 放大镜 玻璃摆件 碎玻璃 塑料瓶罐 瓶盖 饮料瓶 奶瓶 洗发水瓶 乳液罐 食用油桶 塑料碗 盆  塑料盒子 食品保鲜盒 收纳盒 ' \
        ' 塑料玩具 塑料积木 塑料模型  塑料衣架 施工安全帽 PE塑料 pvc 亚克力板 塑料卡片 密胺餐具 kt板 泡沫 ' \
        '泡沫塑料 水果网套 纸板箱 报纸 废弃书本 快递纸袋 打印纸 信封 广告单 纸塑铝 复合包装 易拉罐 金属罐头盒' \
        ' 装饰物 铝箔 报纸 杂志 图书 各种包装纸 办公用纸 纸盒塑料瓶 食品罐头 玻璃瓶 易拉罐 报纸 旧书包 旧手提包 ' \
        '旧鞋子 牛奶盒 旧塑料蓝子 旧玩偶 玻璃壶 旧铁锅 垃圾桶 旧镜子 牙刷 塑料梳子 旧帽子 旧夹子 废锁头 牙膏皮 雨伞骨架 旧纸袋 纸盒 旧玩具'
poision=' 漆桶 电池 打火机 创口贴 酒精 调色板 油漆 过期的胶囊药物 温度计 过期药片 荧光灯 蓄电池 医用棉签 杀虫剂 水彩笔 农药瓶 医用纱布 口服液瓶 香水瓶 荧光棒 过期化妆品 发胶 注射器 废弃灯泡 煤气罐 医用手套'
good=recycle
for i in range(1000):
    if(good[i]==' '):
        m=m+1
        if(m%2!=0):
            a=i
            flag=1
        if (m % 2 == 0):
            b=i
            flag=0
        if(flag==1):
            #c=paper[b:b+4]+good[b:a]+paper[a+5:a+10]
            #c=good[b:a]+paper[a:a+5]
            c = good[b:a]
        if (flag == 0):
            #c=paper[a:a+4]+good[a:b]+paper[b+5:b+10]
            #c = good[a:b]+paper[b:b+5]
            c = good[a:b]

        d=str(m+200)

        if(m>1):
            f = open('recycle'+d+'.txt','w',encoding='utf-8')
            f.write(c)
            print(m)
            print(c)
