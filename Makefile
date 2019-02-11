BUILD_DIR=./_build

.PHONY: build
build: $(BUILD_DIR) $(BUILD_DIR)/index.md
	pandoc -o $(BUILD_DIR)/index.html $(BUILD_DIR)/index.md

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)

$(BUILD_DIR)/index.md: $(BUILD_DIR)
	containers-micro-optimizations-generate -b $(BUILD_DIR) -i index.md

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)
