
Cheetah/Templates/SkeletonPage.py: Cheetah/Templates/SkeletonPage.tmpl Cheetah/Compiler.py
	PYTHONPATH=. cheetah compile --nobackup Cheetah/Templates/SkeletonPage.tmpl
	chmod a+x Cheetah/Templates/SkeletonPage.py
