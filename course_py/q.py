
nnoremap <leader>m :let g:delete_content = 0<CR>:call RenameFile()<CR>
nnoremap <leader>rm :let g:delete_content = 1<CR>:call RenameFile()<CR>

function! RenameFile()
  let new_name = input("New filename (without .py): ")
  execute ":!w"

  if new_name !~# '\.py$'
    let new_name .= ".py"
  endif

  if new_name != ""
    execute 'w ' . fnameescape(new_name)
  endif

  if g:delete_content
    call DeleteFulltext()
  endif
  let g:delete_content = 0
  execute ":!w"

endfunction
