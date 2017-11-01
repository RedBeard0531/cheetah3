
Cheetah/Templates/SkeletonPage.py: Cheetah/Templates/SkeletonPage.tmpl
	PYTHONPATH=. cheetah compile $<
	chmod a+x $@
