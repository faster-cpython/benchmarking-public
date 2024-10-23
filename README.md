# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

[Currently failing benchmarks](failures.md).

**Key:** 📄: table, 📈: time plot, 🧠: memory plot

<!-- START table -->
[Most recent pystats on main (8f5e39d)](results/bm-20241019-3.14.0a1%2B-8f5e39d-PYTHON_UOPS/bm-20241019-azure-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-pystats.md)

## linux aarch64 (arminc)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-ded105a-JIT) | python/ded105a62b9d78717f8d | ded105a (JIT) | 1.10x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg) | 1.17x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg) | 1.19x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT) | nick-arm/codecache_rwx | 7b3da21 (JIT) | 1.10x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg) | 1.16x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg) | 1.18x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg) | 1.01x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg) |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT) | nick-arm/codecache | 0be1ef3 (JIT) | 1.10x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg) | 1.17x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg) | 1.19x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg) | 1.00x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base-mem.svg) |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT) | python/8f5e39d5c885318e3128 | 8f5e39d (JIT) | 1.09x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.16x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.18x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) | 1.11x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)[🧠](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg) |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d) | python/8f5e39d5c885318e3128 | 8f5e39d | 1.21x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.05x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.07x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) |  |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL) | python/8f5e39d5c885318e3128 | 8f5e39d (NOGIL) | 1.23x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.56x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.59x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) | 1.49x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)[🧠](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg) |

## linux x86_64 (linux)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-10-22](results/bm-20241022-3.14.0a1%2B-34653bb-JIT) | python/34653bba644aa5481613 | 34653bb (JIT) | 1.37x ↑<br>[📄](results/bm-20241022-3.14.0a1%2B-34653bb-JIT/bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)[📈](results/bm-20241022-3.14.0a1%2B-34653bb-JIT/bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg) | 1.04x ↑<br>[📄](results/bm-20241022-3.14.0a1%2B-34653bb-JIT/bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)[📈](results/bm-20241022-3.14.0a1%2B-34653bb-JIT/bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg) | 1.02x ↓<br>[📄](results/bm-20241022-3.14.0a1%2B-34653bb-JIT/bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)[📈](results/bm-20241022-3.14.0a1%2B-34653bb-JIT/bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg) |  |
| [2024-10-22](results/bm-20241022-3.14.0a1%2B-759a54d) | python/759a54d28ffe7eac8c23 | 759a54d | 1.39x ↑<br>[📄](results/bm-20241022-3.14.0a1%2B-759a54d/bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.10.4.md)[📈](results/bm-20241022-3.14.0a1%2B-759a54d/bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.10.4.svg) | 1.05x ↑<br>[📄](results/bm-20241022-3.14.0a1%2B-759a54d/bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.12.0.md)[📈](results/bm-20241022-3.14.0a1%2B-759a54d/bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.12.0.svg) | 1.01x ↓<br>[📄](results/bm-20241022-3.14.0a1%2B-759a54d/bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.13.0.md)[📈](results/bm-20241022-3.14.0a1%2B-759a54d/bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-ded105a-JIT) | python/ded105a62b9d78717f8d | ded105a (JIT) | 1.37x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg) | 1.05x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg) | 1.02x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT) | nick-arm/codecache_rwx | 7b3da21 (JIT) | 1.38x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg) | 1.06x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg) | 1.02x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg) | 1.01x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg) |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT) | nick-arm/codecache | 0be1ef3 (JIT) | 1.38x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg) | 1.05x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg) | 1.02x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg) | 1.00x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base-mem.svg) |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT) | python/8f5e39d5c885318e3128 | 8f5e39d (JIT) | 1.33x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.04x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.03x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) | 1.02x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)[🧠](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg) |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d) | python/8f5e39d5c885318e3128 | 8f5e39d | 1.36x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.05x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.01x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) |  |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL) | python/8f5e39d5c885318e3128 | 8f5e39d (NOGIL) | 1.07x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.37x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.46x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) | 1.44x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)[🧠](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg) |

## linux x86_64 (pythonperf2)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-10-22](results/bm-20241022-3.14.0a1%2B-759a54d-JIT) | python/759a54d28ffe7eac8c23 | 759a54d (JIT) | 1.19x ↑<br>[📄](results/bm-20241022-3.14.0a1%2B-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.10.4.md)[📈](results/bm-20241022-3.14.0a1%2B-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.10.4.svg) | 1.09x ↓<br>[📄](results/bm-20241022-3.14.0a1%2B-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.12.0.md)[📈](results/bm-20241022-3.14.0a1%2B-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.12.0.svg) | 1.09x ↓<br>[📄](results/bm-20241022-3.14.0a1%2B-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.13.0.md)[📈](results/bm-20241022-3.14.0a1%2B-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-ded105a-JIT) | python/ded105a62b9d78717f8d | ded105a (JIT) | 1.20x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg) | 1.09x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg) | 1.09x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT) | nick-arm/codecache_rwx | 7b3da21 (JIT) | 1.19x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg) | 1.09x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg) | 1.09x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg) | 1.01x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg) |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT) | nick-arm/codecache | 0be1ef3 (JIT) | 1.19x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg) | 1.09x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg) | 1.09x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg) | 1.01x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base-mem.svg) |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT) | python/8f5e39d5c885318e3128 | 8f5e39d (JIT) | 1.19x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.08x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.08x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) | 1.03x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)[🧠](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg) |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d) | python/8f5e39d5c885318e3128 | 8f5e39d | 1.23x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.05x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.05x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) |  |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL) | python/8f5e39d5c885318e3128 | 8f5e39d (NOGIL) | 1.13x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.45x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.44x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) | 1.38x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)[🧠](results/bm-20241019-3.14.0a1%2B-8f5e39d-NOGIL/bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg) |

## windows amd64 (pythonperf1)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-ded105a-JIT) | python/ded105a62b9d78717f8d | ded105a (JIT) | 1.20x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg) | 1.01x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg) | 1.03x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT) | nick-arm/codecache_rwx | 7b3da21 (JIT) | 1.23x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg) | 1.04x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg) | 1.01x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg) | 1.03x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg) |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT) | nick-arm/codecache | 0be1ef3 (JIT) | 1.23x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg) | 1.04x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg) | 1.01x ↓<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg) | 1.02x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.svg) |

## windows x86 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-ded105a-JIT) | python/ded105a62b9d78717f8d | ded105a (JIT) | 1.18x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg) | 1.20x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg) | 1.07x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT) | nick-arm/codecache_rwx | 7b3da21 (JIT) | 1.20x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg) | 1.21x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg) | 1.08x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg) | 1.01x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg) |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT) | nick-arm/codecache | 0be1ef3 (JIT) | 1.21x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg) | 1.23x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg) | 1.10x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg) | 1.03x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.svg) |

## darwin arm64 (darwin)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-ded105a-JIT) | python/ded105a62b9d78717f8d | ded105a (JIT) | 1.23x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg) | 1.04x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg) | 1.04x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg) |  |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT) | nick-arm/codecache_rwx | 7b3da21 (JIT) | 1.27x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg) | 1.06x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg) | 1.06x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg) | 1.03x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-7b3da21-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg) |
| [2024-10-21](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT) | nick-arm/codecache | 0be1ef3 (JIT) | 1.27x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg) | 1.06x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg) | 1.06x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg) | 1.03x ↑<br>[📄](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.md)[📈](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base.svg)[🧠](results/bm-20241021-3.14.0a1%2B-0be1ef3-JIT/bm-20241021-darwin-arm64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-base-mem.svg) |
| [2024-10-19](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT) | python/8f5e39d5c885318e3128 | 8f5e39d (JIT) | 1.20x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg) | 1.02x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg) | 1.02x ↑<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg) | 1.05x ↓<br>[📄](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)[📈](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)[🧠](results/bm-20241019-3.14.0a1%2B-8f5e39d-JIT/bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg) |
| [2024-10-18](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT) | diegorusso/pthread | f74cd79 (JIT) | 1.23x ↑<br>[📄](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.10.4.md)[📈](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.10.4.svg) | 1.04x ↑<br>[📄](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.12.0.md)[📈](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.12.0.svg) | 1.04x ↑<br>[📄](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.13.0.md)[📈](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-3.13.0.svg) | 1.00x ↑<br>[📄](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-base.md)[📈](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-base.svg)[🧠](results/bm-20241018-3.14.0a1%2B-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1%2B-f74cd79-vs-base-mem.svg) |
| [2024-10-17](results/bm-20241017-3.14.0a1%2B-37986e8-JIT) | python/37986e830ba25d2c3829 | 37986e8 (JIT) | 1.23x ↑<br>[📄](results/bm-20241017-3.14.0a1%2B-37986e8-JIT/bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.10.4.md)[📈](results/bm-20241017-3.14.0a1%2B-37986e8-JIT/bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.10.4.svg) | 1.03x ↑<br>[📄](results/bm-20241017-3.14.0a1%2B-37986e8-JIT/bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.12.0.md)[📈](results/bm-20241017-3.14.0a1%2B-37986e8-JIT/bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.12.0.svg) | 1.03x ↑<br>[📄](results/bm-20241017-3.14.0a1%2B-37986e8-JIT/bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.13.0.md)[📈](results/bm-20241017-3.14.0a1%2B-37986e8-JIT/bm-20241017-darwin-arm64-python-37986e830ba25d2c3829-3.14.0a1%2B-37986e8-vs-3.13.0.svg) |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.

For the results above, the "faster/slower" result is a geometric mean of each of the benchmarks. The "reliability (rel)" number is the likelihood that the change is faster or slower based on the [Hierarchical Performance Testing (HPT)](#hpt) method. For more details, visit each individual result's README.md.

## Longitudinal results

Below are longitudinal timing results. There are also [🧠 longitudinal memory results](memory.md).

![Longitudinal speed improvement](/longitudinal.svg)

![Effect of different configurations](/configs.svg)

Improvement of the HPT score of key merged benchmarks, computed with `pyperf compare`.
The results have a resolution of 0.01 (1%).

- linux: Intel® Xeon® W-2255 CPU @ 3.70GHz, running Ubuntu 20.04 LTS, gcc 9.4.0
- linux2: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Ubuntu 22.04 LTS, gcc 11.3.0
- linux-aarch64: ARM Neoverse N1, running Ubuntu 22.04 LTS, gcc 11.4.0
- macos: M1 arm64 Mac® Mini, running macOS 13.2.1, clang 1400.0.29.202
- windows: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Windows 11 Pro (21H2, 22000.1696), MSVC v143

## Data changes

This is a CHANGELOG of how any derived data has changed:

- 2024-06-27: The HPT values (and the longitudinal plots that are based on them) now correctly exclude any benchmarks in `excluded_benchmarks.txt`.

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
- Comparisons against important reference releases, as well as the merge base of the branch if `benchmark_base` was selected. These include
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

### Creating a custom comparison

If the default comparisons generated by this tool aren't sufficient, you can check
out the repo and use the same infrastructure to generate any arbitrary
comparison.

Check out a local copy of this repo:

```sh
$ git clone https://github.com/faster-cpython/benchmarking-public
```

Create a new virtual environment, activate it and install the dependencies into it:

```sh
$ cd benchmarking-public
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run `bench_runner`'s `compare` tool:

```text
usage:
        Generate a set of comparisons between arbitrary commits. The commits
        must already exist in the dataset.

       [-h] --output-dir OUTPUT_DIR [--type {1:n,n:n}] commit [commit ...]

positional arguments:
  commit                Commits to compare. Must be a git commit hash prefix. May optionally have a friendly name
                        after a comma, e.g. c0ffee,main. If ends with a "T", use the Tier 2 run for that commit. If
                        ends with a "J", use the JIT run for that commit. If ends with a "N", use the NOGIL run for
                        that commit.

options:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
                        Directory to output results to.
  --type {1:n,n:n}      Compare the first commit to all others, or do the full product of all commits
```

For example:

```sh
$ python -m bench_runner compare e418fc3,default e418fc3J,jit --output comparison --type 1:n
```

### Developer docs

The infrastructure to make all of this work is the [bench_runner
project](https://github.com/faster-cpython/bench_runner). Look there for more
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
to combine them. This file should be passed to `pyperformance run`:

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
of each run directory. The directory name will also include `PYTHON_UOPS` for
Tier 2 and `JIT` for JIT.

To reduce the number of unknown variables when comparing results, runs are
always compared against runs of the same configuration. Be aware that sometimes
the base commit on main may predate the configuration becoming available, for
example, before the JIT compiler was merged into main. (An exception to this
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

Timing benchmarks are notoriously noisy. There are a few techniques to reduce this:

- Where available (on Linux), we use [`pyperf
tune`](https://pyperf.readthedocs.io/en/latest/system.html) to set CPU
  affinity and other things that make the benchmarks more reproducible. For
  this reason, we know that the benchmarks are more predictable on Linux than on
  the other platforms.
- `pyperf` has the concept of "warmup" runs, while caches are warming up and
  other things about the system are still stabilizing. These runs are excluded
  from the timing results. This is generally effective at reducing variability,
  but also may exclude real work done during optimization, for example.
- We use the Hierarchical Performance Testing (HPT) method (see below) to
  statistically reduce the effect of benchmarks that have more variability.
  This is a different method than the simple geometric mean that `pyperf` uses
  by default. We provide both numbers in our results.

#### pystats

`pystats` are a set of counters in CPython that measure things like the number
of times each bytecode instruction is executed. (Detailed documentation of all
of the counters should be added to CPython in the future).

Collecting `pystats` requires a special build of CPython with `pystats` enabled:
(`./configure --enable-pystats`).

`pystats` must also be enabled at runtime, either using the `-Xpystats` command
line argument or `sys._stats_on()`. `pyperformance`/`pyperf` handles this step
automatically when running on a pystats-enabled build. Stats collection is
enabled during actual benchmarking code, and disabled while running the
"benchmarking harness" code in `pyperf` itself. `pyperf` has the concept of
"warmup" runs, which allow things like cache lines to warmup before actually
timing benchmarks. While they aren't included in the timing benchmarks, these
warmup runs are included in pystats collection since often Tier 2/JIT traces are
created during warmup, and we don't want the stats to appear as if the traces
ran but were not created.

Any statistics collected are then dumped at exit to the `/tmp/py_stats`
directory with a random filename. Lastly, the `Tools/scripts/summarize_stats.py`
script (in the CPython repo) is used to read all of the files from
`/tmp/py_stats` and produce a human-readable markdown summary and a JSON file
with aggregate data. Because of this design, it is imperative that:

- The `/tmp/py_stats` directory is cleared before data collection.
- No other Python processes are run that could also produce pystats data.
  Especially, this means benchmarks can not run in parallel.

For more information, see the actual code to [collect
pystats](https://github.com/faster-cpython/bench_runner/blob/main/bench_runner/templates/_pystats.src.yml).

### HPT

Hierarchical performance testing (HPT) is a method introduced in this paper:

> T. Chen, Y. Chen, Q. Guo, O. Temam, Y. Wu and W. Hu,
> "Statistical performance comparisons of computers,"
> IEEE International Symposium on High-Performance Comp Architecture,
> New Orleans, LA, USA, 2012, pp. 1-12,
> doi: 10.1109/HPCA.2012.6169043.

From the abstract:

> In traditional performance comparisons, the impact of performance variability
> is usually ignored (i.e., the means of performance measurements are compared
> regardless of the variability), or in the few cases where it is factored in
> using parametric confidence techniques, the confidence is either erroneously
> computed based on the distribution of performance measurements (with the
> implicit assumption that it obeys the normal law), instead of the distribution
> of sample mean of performance measurements, or too few measurements are
> considered for the distribution of sample mean to be normal. … We propose a
> non-parametric Hierarchical Performance Testing (HPT) framework for
> performance comparison, which is significantly more practical than standard
> parametric techniques because it does not require to collect a large number of
> measurements in order to achieve a normal distribution of the sample mean.

For each result, we compute a reliability score, as well as the estimated
speedup at the 90th, 95th and 99th percentile.

**The inclusion of HPT scores is considered experimental as we learn about their
usefulness for decision-making.**
