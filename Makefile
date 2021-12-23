dev:
	@hugo server -D --disableFastRender

publish:
	sh scripts/publish_to_ghpages.sh