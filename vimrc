set nu
set ts=4
set expandtab
"color scheme
set t_Co=256
color molokai
"highlighe function name
autocmd BufNewFile,BufRead * :syntax match cfunctions "\<[a-zA-Z_][a-zA-Z_0-9]*\>[^()]*)("me=e-2
autocmd BufNewFile,BufRead * :syntax match cfunctions "\<[a-zA-Z_][a-zA-Z_0-9]*\>\s*("me=e-1

hi cfunctions ctermfg=81

"let g:molokai_original = 1
"let g:rehash256 = 1
