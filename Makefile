
dev:
	@hugo server -D

pages:
	rm -rf public/
	hugo -D
	echo "mikeder.net" > public/CNAME
	cd public && git add --all && git commit -m "Publishing to gh-pages" && cd ..

publish:
	sh scripts/publish_to_ghpages.sh