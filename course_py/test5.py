

  " 将当前文件内容保存到新文件中
  if new_name != ""
    write fnameescape(new_name)  " 使用 Vim 内部命令保存文件
  endif

  " 如果需要清空当前文件内容
  if g:delete_content
    call DeleteFulltext()  " 清空内容
    write  " 保存清空后的文件状态
