
dev:
	@hugo server -D

pages:
	rm -rf public/
	hugo -D
	echo "mikeder.net" > public/CNAME
	cd public && git add --all && git commit -m "Publishing to gh-pages" && cd ..
