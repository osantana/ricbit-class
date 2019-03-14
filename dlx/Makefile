all : dlx1 dlx2 dlx3 dlx-pre

dlx%.c : dlx%.w
	ctangle $^

dlx% : dlx%.c
	gcc -O3 -march=native -g $^ -o $@ -lgb -I/Users/osantana/Work/ricbit-course/ricbit-course/sgb/include -L/Users/osantana/Work/ricbit-course/ricbit-course/sgb/lib
