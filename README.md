# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

**Key:** 📄: table, 📈: time plot, 🧠: memory plot

<!-- START table -->
[Most recent pystats on main (48c0b05)](results/bm-20240326-3.13.0a5%2B-48c0b05/bm-20240326-azure-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-pystats.md)

## linux x86_64 (linux)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.11.0: | vs. 3.12.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-03-28](results/bm-20240328-3.13.0a5%2B-174fc24-JIT) | faster-cpython/no_thresholds | 174fc24 (JIT) | 1.27x ↑<br>[📄](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-3.10.4.md)[📈](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-3.10.4.png) | 1.01x ↑<br>[📄](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-3.11.0.md)[📈](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-3.11.0.png) | 1.01x ↓<br>[📄](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-3.12.0.md)[📈](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-3.12.0.png) | 1.03x ↓<br>[📄](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-base.md)[📈](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-base.png)[🧠](results/bm-20240328-3.13.0a5%2B-174fc24-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-174fc24-vs-base-mem.png) |
| [2024-03-28](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT) | faster-cpython/no_thresholds | a4985b2 (JIT) | 1.28x ↑<br>[📄](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-3.10.4.md)[📈](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-3.10.4.png) | 1.01x ↑<br>[📄](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-3.11.0.md)[📈](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-3.11.0.png) | 1.01x ↓<br>[📄](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-3.12.0.md)[📈](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-3.12.0.png) | 1.02x ↓<br>[📄](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-base.md)[📈](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-base.png)[🧠](results/bm-20240328-3.13.0a5%2B-a4985b2-JIT/bm-20240328-linux-x86_64-faster%252dcpython-no_thresholds-3.13.0a5%2B-a4985b2-vs-base-mem.png) |
| [2024-03-28](results/bm-20240328-3.13.0a5%2B-6c8ac8a-JIT) | python/6c8ac8a32fd6de196052 | 6c8ac8a (JIT) | 1.31x ↑<br>[📄](results/bm-20240328-3.13.0a5%2B-6c8ac8a-JIT/bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5%2B-6c8ac8a-vs-3.10.4.md)[📈](results/bm-20240328-3.13.0a5%2B-6c8ac8a-JIT/bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5%2B-6c8ac8a-vs-3.10.4.png) | 1.04x ↑<br>[📄](results/bm-20240328-3.13.0a5%2B-6c8ac8a-JIT/bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5%2B-6c8ac8a-vs-3.11.0.md)[📈](results/bm-20240328-3.13.0a5%2B-6c8ac8a-JIT/bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5%2B-6c8ac8a-vs-3.11.0.png) | 1.01x ↑<br>[📄](results/bm-20240328-3.13.0a5%2B-6c8ac8a-JIT/bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5%2B-6c8ac8a-vs-3.12.0.md)[📈](results/bm-20240328-3.13.0a5%2B-6c8ac8a-JIT/bm-20240328-linux-x86_64-python-6c8ac8a32fd6de196052-3.13.0a5%2B-6c8ac8a-vs-3.12.0.png) |  |
| [2024-03-27](results/bm-20240327-3.13.0a5%2B-74c8568) | python/74c8568d07719529b874 | 74c8568 | 1.34x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-3.10.4.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-3.10.4.png) | 1.06x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-3.11.0.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-3.11.0.png) | 1.04x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-3.12.0.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-3.12.0.png) | 1.01x ↓<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-base.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-base.png)[🧠](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5%2B-74c8568-vs-base-mem.png) |
| [2024-03-27](results/bm-20240327-3.13.0a5%2B-74c8568) | brandtbucher/main | 74c8568 | 1.35x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.10.4.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.10.4.png) | 1.07x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.11.0.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.11.0.png) | 1.05x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.12.0.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.12.0.png) | 1.00x ↓<br>[📄](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-base.md)[📈](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-base.png)[🧠](results/bm-20240327-3.13.0a5%2B-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-base-mem.png) |
| [2024-03-27](results/bm-20240327-3.13.0a5%2B-ce00de4) | python/ce00de4c8cd39816f992 | ce00de4 | 1.35x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-ce00de4/bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.10.4.md)[📈](results/bm-20240327-3.13.0a5%2B-ce00de4/bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.10.4.png) | 1.07x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-ce00de4/bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.11.0.md)[📈](results/bm-20240327-3.13.0a5%2B-ce00de4/bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.11.0.png) | 1.05x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-ce00de4/bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.12.0.md)[📈](results/bm-20240327-3.13.0a5%2B-ce00de4/bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.12.0.png) |  |
| [2024-03-27](results/bm-20240327-3.13.0a5%2B-225ea17-JIT) | gvanrossum/exp_backoff | 225ea17 (JIT) | 1.29x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.10.4.md)[📈](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.10.4.png) | 1.03x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.11.0.md)[📈](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.11.0.png) | 1.00x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.12.0.md)[📈](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.12.0.png) | 1.01x ↓<br>[📄](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-base.md)[📈](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-base.png)[🧠](results/bm-20240327-3.13.0a5%2B-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-base-mem.png) |
| [2024-03-27](results/bm-20240327-3.13.0a5%2B-0f9d2fe) | brandtbucher/revert_90a1b28 | 0f9d2fe | 1.35x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.10.4.md)[📈](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.10.4.png) | 1.08x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.11.0.md)[📈](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.11.0.png) | 1.05x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.12.0.md)[📈](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.12.0.png) | 1.01x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-base.md)[📈](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-base.png)[🧠](results/bm-20240327-3.13.0a5%2B-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-base-mem.png) |
| [2024-03-26](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT) | gvanrossum/exp_backoff | f6bf194 (JIT) | 1.32x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.10.4.md)[📈](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.10.4.png) | 1.05x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.11.0.md)[📈](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.11.0.png) | 1.02x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.12.0.md)[📈](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.12.0.png) | 1.01x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-base.md)[📈](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-base.png)[🧠](results/bm-20240326-3.13.0a5%2B-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-base-mem.png) |
| [2024-03-26](results/bm-20240326-3.13.0a5%2B-cb4cc72) | faster-cpython/specialize_binary_fl | cb4cc72 | 1.35x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-cb4cc72/bm-20240326-linux-x86_64-faster%252dcpython-specialize_binary_fl-3.13.0a5%2B-cb4cc72-vs-3.10.4.md)[📈](results/bm-20240326-3.13.0a5%2B-cb4cc72/bm-20240326-linux-x86_64-faster%252dcpython-specialize_binary_fl-3.13.0a5%2B-cb4cc72-vs-3.10.4.png) | 1.07x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-cb4cc72/bm-20240326-linux-x86_64-faster%252dcpython-specialize_binary_fl-3.13.0a5%2B-cb4cc72-vs-3.11.0.md)[📈](results/bm-20240326-3.13.0a5%2B-cb4cc72/bm-20240326-linux-x86_64-faster%252dcpython-specialize_binary_fl-3.13.0a5%2B-cb4cc72-vs-3.11.0.png) | 1.04x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-cb4cc72/bm-20240326-linux-x86_64-faster%252dcpython-specialize_binary_fl-3.13.0a5%2B-cb4cc72-vs-3.12.0.md)[📈](results/bm-20240326-3.13.0a5%2B-cb4cc72/bm-20240326-linux-x86_64-faster%252dcpython-specialize_binary_fl-3.13.0a5%2B-cb4cc72-vs-3.12.0.png) |  |
| [2024-03-26](results/bm-20240326-3.13.0a5%2B-c05d01d) | faster-cpython/inline_values | c05d01d | 1.36x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-c05d01d/bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.10.4.md)[📈](results/bm-20240326-3.13.0a5%2B-c05d01d/bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.10.4.png) | 1.08x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-c05d01d/bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.11.0.md)[📈](results/bm-20240326-3.13.0a5%2B-c05d01d/bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.11.0.png) | 1.05x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-c05d01d/bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.12.0.md)[📈](results/bm-20240326-3.13.0a5%2B-c05d01d/bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.12.0.png) |  |
| [2024-03-26](results/bm-20240326-3.13.0a5%2B-48c0b05-JIT) | python/48c0b05cf0dd2db275bd | 48c0b05 (JIT) | 1.31x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.10.4.md)[📈](results/bm-20240326-3.13.0a5%2B-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.10.4.png) | 1.04x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.11.0.md)[📈](results/bm-20240326-3.13.0a5%2B-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.11.0.png) | 1.02x ↑<br>[📄](results/bm-20240326-3.13.0a5%2B-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.12.0.md)[📈](results/bm-20240326-3.13.0a5%2B-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.12.0.png) |  |
| [2024-03-25](results/bm-20240325-3.13.0a5%2B-37627d3-JIT) | faster-cpython/tier2_hot_cold_split | 37627d3 (JIT) | 1.31x ↑<br>[📄](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.10.4.md)[📈](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.10.4.png) | 1.04x ↑<br>[📄](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.11.0.md)[📈](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.11.0.png) | 1.02x ↑<br>[📄](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.12.0.md)[📈](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.12.0.png) | 1.00x ↑<br>[📄](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-base.md)[📈](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-base.png)[🧠](results/bm-20240325-3.13.0a5%2B-37627d3-JIT/bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-base-mem.png) |
| [2024-03-25](results/bm-20240325-3.13.0a5%2B-507896d-JIT) | python/507896d97dcff2d7999e | 507896d (JIT) | 1.31x ↑<br>[📄](results/bm-20240325-3.13.0a5%2B-507896d-JIT/bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.10.4.md)[📈](results/bm-20240325-3.13.0a5%2B-507896d-JIT/bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.10.4.png) | 1.04x ↑<br>[📄](results/bm-20240325-3.13.0a5%2B-507896d-JIT/bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.11.0.md)[📈](results/bm-20240325-3.13.0a5%2B-507896d-JIT/bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.11.0.png) | 1.01x ↑<br>[📄](results/bm-20240325-3.13.0a5%2B-507896d-JIT/bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.12.0.md)[📈](results/bm-20240325-3.13.0a5%2B-507896d-JIT/bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.12.0.png) |  |

## linux x86_64 (pythonperf2)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.11.0: | vs. 3.12.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-JIT) | python/d610d821fd210dce63a1 | d610d82 (JIT) | 1.25x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.04x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.03x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.04x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png)[🧠](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base-mem.png) |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS) | python/d610d821fd210dce63a1 | d610d82 ️(T2) | 1.15x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.04x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.12x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.13x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png)[🧠](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base-mem.png) |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82) | python/d610d821fd210dce63a1 | d610d82 | 1.30x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.08x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.01x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) |  |

## windows amd64 (pythonperf1)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.11.0: | vs. 3.12.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-03-27](results/bm-20240327-3.13.0a5%2B-8183250) | faster-cpython/specialize_binary_op | 8183250 | 1.20x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-8183250/bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.10.4.md)[📈](results/bm-20240327-3.13.0a5%2B-8183250/bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.10.4.png) | 1.08x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-8183250/bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.11.0.md)[📈](results/bm-20240327-3.13.0a5%2B-8183250/bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.11.0.png) | 1.05x ↑<br>[📄](results/bm-20240327-3.13.0a5%2B-8183250/bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.12.0.md)[📈](results/bm-20240327-3.13.0a5%2B-8183250/bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.12.0.png) |  |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-JIT) | python/d610d821fd210dce63a1 | d610d82 (JIT) | 1.21x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.09x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.06x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.01x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png) |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS) | python/d610d821fd210dce63a1 | d610d82 ️(T2) | 1.13x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.02x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.01x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.08x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png) |

## windows x86 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.11.0: | vs. 3.12.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-JIT) | python/d610d821fd210dce63a1 | d610d82 (JIT) | 1.05x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.16x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.09x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.12x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png) |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS) | python/d610d821fd210dce63a1 | d610d82 ️(T2) | 1.12x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.24x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.17x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.05x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png) |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82) | python/d610d821fd210dce63a1 | d610d82 | 1.18x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.30x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.22x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) |  |

## darwin arm64 (darwin)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.11.0: | vs. 3.12.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-JIT) | python/d610d821fd210dce63a1 | d610d82 (JIT) | 1.19x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.02x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.01x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.04x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png)[🧠](results/bm-20240323-3.13.0a5%2B-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base-mem.png) |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS) | python/d610d821fd210dce63a1 | d610d82 ️(T2) | 1.13x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.08x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.05x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) | 1.10x ↓<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base.png)[🧠](results/bm-20240323-3.13.0a5%2B-d610d82-PYTHON_UOPS/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-base-mem.png) |
| [2024-03-23](results/bm-20240323-3.13.0a5%2B-d610d82) | python/d610d821fd210dce63a1 | d610d82 | 1.24x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.10.4.png) | 1.02x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.11.0.png) | 1.05x ↑<br>[📄](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.md)[📈](results/bm-20240323-3.13.0a5%2B-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5%2B-d610d82-vs-3.12.0.png) |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.

For the results above, the "faster/slower" result is a geometric mean of each of the benchmarks. The "reliability (rel)" number is the likelihood that the change is faster or slower based on the [Hierarchical Performance Testing (HPT)](#hpt) method.  For more details, visit each individual result's README.md.

## Longitudinal results

Below are longitudinal timing results. There are also [🧠 longitudinal memory results](memory.md).

![Longitudinal speed improvement](/longitudinal.png)

![Effect of different configurations](/configs.png)

Improvement of the HPT score of key merged benchmarks, computed with `pyperf compare`.
The results have a resolution of 0.01 (1%).

- linux: Intel® Xeon® W-2255 CPU @ 3.70GHz, running Ubuntu 20.04 LTS, gcc 9.4.0
- linux2: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Ubuntu 22.04 LTS, gcc 11.3.0
- macos: M1 arm64 Mac® Mini, running macOS 13.2.1, clang 1400.0.29.202
- windows: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Windows 11 Pro (21H2, 22000.1696), MSVC v143

## Documentation

### Running benchmarks from the GitHub web UI

Visit the 🔒 [benchmark action](../../actions/workflows/benchmark.yml) and click the "Run Workflow" button.

The available parameters are:

- `fork`: The fork of CPython to benchmark.
  If benchmarking a pull request, this would normally be your GitHub username.
- `ref`: The branch, tag or commit SHA to benchmark.
  If a SHA, it must be the full SHA, since finding it by a prefix is not supported.
- `machine`: The machine to run on.
  One of `linux-amd64` (default), `windows-amd64`, `darwin-arm64` or `all`.
- `benchmark_base`: If checked, the base of the selected branch will also be benchmarked.
  The base is determined by running `git merge-base upstream/main $ref`.
- `pystats`: If checked, collect the pystats from running the benchmarks.

To watch the progress of the benchmark, select it from the 🔒 [benchmark action page](../../actions/workflows/benchmark.yml).
It may be canceled from there as well.
To show only your benchmark workflows, select your GitHub ID from the "Actor" dropdown.

When the benchmarking is complete, the results are published to this repository and will appear in the [master table](RESULTS.md).
Each set of benchmarks will have:

- The raw `.json` results from pyperformance.
- Comparisons against important reference releases, as well as the merge base of the branch if `benchmark_base` was selected.  These include
  - A markdown table produced by `pyperf compare_to`.
  - A set of "violin" plots showing the distribution of results for each benchmark.
  - A set of plots showing the memory change for each benchmark (for immediate bases only, on non-Windows platforms).

The most convenient way to get results locally is to clone this repo and `git pull` from it.

### Running benchmarks from the GitHub CLI

To automate benchmarking runs, it may be more convenient to use the [GitHub CLI](https://cli.github.com/).
Once you have `gh` installed and configured, you can run benchmarks by cloning this repository and then from inside it:

```bash
$ gh workflow run benchmark.yml -f fork=me -f ref=my_branch
```

Any of the parameters described above are available at the commandline using the `-f key=value` syntax.

### Collecting Linux perf profiling data

To collect Linux perf sampling profile data for a benchmarking run, run the `_benchmark` action and check the `perf` checkbox.

### Developer docs

The infrastructure to make all of this work is the [bench_runner
project](https://github.com/faster-cpython/bench_runner).  Look there for more
detailed developer docs.

### Details about how results are collected

The easiest way to reproduce what is here is to use the [bench_runner
project](https://github.com/faster-cpython/bench_runner) library directly, but
if you want to run parts of it in a different context or better understand how the
numbers are calculated, this section describes some of the things that the
benchmarking infrastructure does.

#### Benchmarks from pyperformance and python-macrobenchmarks

These results combine benchmarks that live in the
[pyperformance](https://github.com/python/pyperformance) and
[pyston/python-macrobenchmarks](https://github.com/pyston/python-macrobenchmarks)
projects, so running the default set from `pyperformance` will definitely
produce different results. To combine these benchmarks in the same run, clone
both repos side-by-side in the same directory and [use a manifest
file](https://github.com/faster-cpython/bench_runner/blob/main/bench_runner/templates/benchmarks.manifest)
to combine them.  This file should be passed to `pyperformance run`:

```
pyperformance run --manifest benchmarks.manifest
```

#### Different configurations

Benchmarks and stats collection can happen in three different configurations.
Here "configuration" may be a combination of both build-time and run-time flags:

- Default: A PGO build of CPython (`./configure --enable-optimizations
  --with-lto=yes`).
- Tier 2: The same build as above, but with the `PYTHON_UOPS` environment
  variable set at runtime to use the Tier 2 interpreter.
- JIT: A JIT and PGO build of CPython (`./configure --enable-optimizations
  --with-lto=yes --enable-experimental-jit`).

Information about the configuration of the run is in the `README.md` at the root
of each run directory.  The directory name will also include `PYTHON_UOPS` for
Tier 2 and `JIT` for JIT.

To reduce the number of unknown variables when comparing results, runs are
always compared against runs of the same configuration. Be aware that sometimes
the base commit on main may predate the configuration becoming available, for
example, before the JIT compiler was merged into main.  (An exception to this
rule are the weekly benchmarks of upstream main, there Tier 2 and JIT
configurations are compared against default configurations of the same commit,
but that isn't relevant for the common case of testing a pull request).

An additional sharp edge is that, by default, `pyperformance` does not pass
environment variables to the child process that actually does the work.
Therefore for a Tier 2 configuration, the `--inherit-environ=PYTHON_UOPS` flag
must be passed to `pyperformance run` when running benchmarks.

For detailed information, see how configurations affect [build time flags in the
Github Actions
configuration.](https://github.com/faster-cpython/bench_runner/blob/main/bench_runner/templates/_benchmark.src.yml).

#### Timing benchmarks

Timing benchmarks are notoriously noisy.  There are a few techniques to reduce this:

- Where available (on Linux), we use [`pyperf
  tune`](https://pyperf.readthedocs.io/en/latest/system.html) to set CPU
  affinity and other things that make the benchmarks more reproducible.  For
  this reason, we know that the benchmarks are more predictable on Linux than on
  the other platforms.
- `pyperf` has the concept of "warmup" runs, while caches are warming up and
  other things about the system are still stabilizing. These runs are excluded
  from the timing results. This is generally effective at reducing variability,
  but also may exclude real work done during optimization, for example.
- We use the Hierarchical Performance Testing (HPT) method (see below) to
  statistically reduce the effect of benchmarks that have more variability.
  This is a different method than the simple geometric mean that `pyperf` uses
  by default.  We provide both numbers in our results.

#### pystats

`pystats` are a set of counters in CPython that measure things like the number
of times each bytecode instruction is executed.  (Detailed documentation of all
of the counters should be added to CPython in the future).

Collecting `pystats` requires a special build of CPython with `pystats` enabled:
(`./configure --enable-pystats`).

`pystats` must also be enabled at runtime, either using the `-Xpystats` command
line argument or `sys._stats_on()`. `pyperformance`/`pyperf` handles this step
automatically when running on a pystats-enabled build.  Stats collection is
enabled during actual benchmarking code, and disabled while running the
"benchmarking harness" code in `pyperf` itself.  `pyperf` has the concept of
"warmup" runs, which allow things like cache lines to warmup before actually
timing benchmarks. While they aren't included in the timing benchmarks, these
warmup runs are included in pystats collection since often Tier 2/JIT traces are
created during warmup, and we don't want the stats to appear as if the traces
ran but were not created.

Any statistics collected are then dumped at exit to the `/tmp/py_stats`
directory with a random filename. Lastly, the `Tools/scripts/summarize_stats.py`
script (in the CPython repo) is used to read all of the files from
`/tmp/py_stats` and produce a human-readable markdown summary and a JSON file
with aggregate data.  Because of this design, it is imperative that:

- The `/tmp/py_stats` directory is cleared before data collection.
- No other Python processes are run that could also produce pystats data.
  Especially, this means benchmarks can not run in parallel.

For more information, see the actual code to [collect
pystats](https://github.com/faster-cpython/bench_runner/blob/main/bench_runner/templates/_pystats.src.yml).

### HPT

Hierarchical performance testing (HPT) is a method introduced in this paper:

> T. Chen, Y. Chen, Q. Guo, O. Temam, Y. Wu and W. Hu,
"Statistical performance comparisons of computers,"
IEEE International Symposium on High-Performance Comp Architecture,
New Orleans, LA, USA, 2012, pp. 1-12,
doi: 10.1109/HPCA.2012.6169043.

From the abstract:

> In traditional performance comparisons, the impact of performance variability
is usually ignored (i.e., the means of performance measurements are compared
regardless of the variability), or in the few cases where it is factored in
using parametric confidence techniques, the confidence is either erroneously
computed based on the distribution of performance measurements (with the
implicit assumption that it obeys the normal law), instead of the distribution
of sample mean of performance measurements, or too few measurements are
considered for the distribution of sample mean to be normal. …  We propose a
non-parametric Hierarchical Performance Testing (HPT) framework for
performance comparison, which is significantly more practical than standard
parametric techniques because it does not require to collect a large number of
measurements in order to achieve a normal distribution of the sample mean.

For each result, we compute a reliability score, as well as the estimated
speedup at the 90th, 95th and 99th percentile.

**The inclusion of HPT scores is considered experimental as we learn about their
usefulness for decision-making.**
