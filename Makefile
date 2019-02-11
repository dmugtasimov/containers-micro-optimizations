BUILD_DIR=./blogpost/build

.PHONY: build
build: $(BUILD_DIR) $(BUILD_DIR)/index.md
	pandoc -o $(BUILD_DIR)/index.html $(BUILD_DIR)/index.md

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)

$(BUILD_DIR)/index.md: $(BUILD_DIR) $(BUILD_DIR)/python-version.txt
	markdown-pp blogpost/index.mdpp -o $(BUILD_DIR)/index.md

$(BUILD_DIR)/python-version.txt: $(BUILD_DIR)
	echo '$$ python --version' > $(BUILD_DIR)/python-version.txt
	python --version >> $(BUILD_DIR)/python-version.txt

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)
