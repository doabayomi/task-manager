/** @type {import('@linthtml/linthtml').LegacyConfig}*/
module.exports = {
	"raw-ignore-regex": false,
	"attr-bans": [
		"align",
		"background",
		"bgcolor",
		"border",
		"frameborder",
		"longdesc",
		"marginwidth",
		"marginheight",
		"scrolling",
		"style",
		"width"
	],
	"indent-delta": false,
	"indent-style": "nonmixed",
	"indent-width": 2,
	"indent-width-cont": false,
	"spec-char-escape": true,
	"text-ignore-regex": false,
	"tag-bans": [
		"style",
		"b",
		"i"
	],
	"tag-close": true,
	"tag-name-lowercase": true,
	"tag-name-match": true,
	"tag-self-close": false,
	"doctype-first": false,
	"doctype-html5": false,
	"attr-name-style": "dash",
	"attr-name-ignore-regex": false,
	"attr-no-dup": true,
	"attr-no-unsafe-char": true,
	"attr-order": false,
	"attr-quote-style": "double",
	"attr-req-value": true,
	"attr-new-line": false,
	"attr-validate": true,
	"id-no-dup": true,
	"id-class-no-ad": true,
	"id-class-style": "underscore",
	"class-no-dup": true,
	"class-style": false,
	"id-class-ignore-regex": false,
	"img-req-alt": true,
	"img-req-src": true,
	"html-valid-content-model": true,
	"head-valid-content-model": true,
	"href-style": false,
	"link-req-noopener": true,
	"label-req-for": true,
	"line-end-style": "lf",
	"line-no-trailing-whitespace": true,
	"line-max-len": false,
	"line-max-len-ignore-regex": false,
	"head-req-title": true,
	"title-no-dup": true,
	"title-max-len": 60,
	"html-req-lang": false,
	"lang-style": "case",
	"fig-req-figcaption": false,
	"focusable-tabindex-style": false,
	"input-radio-req-name": true,
	"input-req-label": false,
	"table-req-caption": false,
	"table-req-header": false,
	"tag-req-attr": false
}