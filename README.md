# Android_multi_language

项目主要是实现通过读取Excel文件，并把对应国家的文案添加到Android对应的资源文件内

代码思路：

- 使用pandas读取excel文件
- 根据国家和资源文件对应的关系找到对应的资源文件
- 获取当前国家的文案，添加到资源内

当前阶段因为还不熟悉GUI 和 输入相关内容所以是写死的，之后会把脚本写的更易用。

更新后遗留的问题：

- 只能通过Append的方式添加多语言，需要自己手动把 </resources> 放到最后
- 如果出现类似  `I'm` 格式的多语言，Android 需要转换成 `I\'m` 才能显示，现在需要手动实现这些
- Android 通配符的样式是 `%1$s` `%2$d` 多语言文案多用 `@` 代替，这个也需要手动去替换
- 支持的格式还有限制，只能是 `<string name=".*">.*</string>` 模式的资源， `<string-array>` 和其他的尚不支持
