Quick Start
Requirements: NVIDIA GPU (tested on H100/A100/RTX 4090), Python 3.10+, uv.

# Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/RightNow-AI/autokernel.git
cd autokernel
uv sync

# One-time setup: test data + baselines
uv run prepare.py

# Profile a model (ships with GPT-2, LLaMA, BERT -- no transformers needed)
uv run profile.py --model models/llama_7b.py --class-name LlamaModel \
 --input-shape 1,512 --dtype float16

# Extract top bottleneck kernels
uv run extract.py --top 5

# Verify benchmark works
uv run bench.py
