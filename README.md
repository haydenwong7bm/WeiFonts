# 创建 Windows 中文字体代替字体
将字体转換为 Windows 雅黑、正黑、宋体、细明体等代替字体。
## 使用方法

### 1. 使用图形界面
可从 [Releases](https://github.com/GuiWonder/toWinFonts/releases) 页面下载应用包。

### 2. 使用命令行

#### 转換思源字体（或其衍生字体）至全部Windows中日韩代替字体

把思源黑体及宋体所有字重分別放在`input/sans`及`input/serif`目彔內，之后运行 `python winfont.py`。字体保存于`output/sans`及`output/serif`目彔內。

#### 转換个別字体

运行 `python winfont.py -i InFont -tg Target -wt Weight -d OutDirectory`。
- `-i` 输入字体(Input)。
- `-tg` 目标字体(Target)，具体如下表。

  | tg | 目标字体 |
  | ---- | :---- |
  | msyh   | 微软雅黑、微软雅黑 UI |
  | msjh   | 微軟正黑體、微軟正黑體 UI |
  | mingliu | 細明體、新細明體、細明體_HKSCS |
  | mingliub | 細明體-ExtB、新細明體-ExtB、細明體_HKSCS-ExtB |
  | simsun  | 宋体、新宋体 |
  | simsunb  | 宋体-ExtB |
  | yugoth  | Yu Gothic、Yu Gothic UI |
  | msgothic | MS Gothic、MS UI Gothic、MS PGothic |
  | malgun  | Malgun Gothic |
  | msmincho | MS Mincho、MS PMincho |
  | meiryo  | Meiryo、Meiryo UI |
  | batang  | Batang、BatangChe、Gungsuh、GungsuhChe |
- `-wt` 字重(Weight)，可使用 `"ExtraLight", "Light", "Semilight", "Normal", "Regular", "Medium", "SemiBold", "Bold", "Heavy"`。如未指定字重，程序会自动判断字重。
- `-d` 字体保存目彔(Output Directory)，如未指定，则使用当前目彔。

> NOTE: 目标为 `yugoth` 时，不建议使用 `"Semilight"` 和 `"SemiBold"`。
