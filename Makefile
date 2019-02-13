BUILD_DIR=./_build

.PHONY: build
build: $(BUILD_DIR) $(BUILD_DIR)/index.md
	pandoc --self-contained -t html5 --css containers_micro_optimizations/static/style.css -o $(BUILD_DIR)/index.html $(BUILD_DIR)/index.md

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)

$(BUILD_DIR)/index.md: $(BUILD_DIR) ./containers_micro_optimizations/templates/index.j2.md
	containers-micro-optimizations-generate -b $(BUILD_DIR) -i index.md

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)
