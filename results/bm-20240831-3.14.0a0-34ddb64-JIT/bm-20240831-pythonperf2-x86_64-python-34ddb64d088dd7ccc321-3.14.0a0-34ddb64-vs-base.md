# Results vs. base

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.017x slower
- HPT reliability: 95.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                                | 310 ms: 1.10x slower                                                                                                      |
| docutils       | 2.90 sec                                                                                                              | 3.16 sec: 1.09x slower                                                                                                    |
| html5lib       | 70.4 ms                                                                                                               | 68.9 ms: 1.02x faster                                                                                                     |
| tornado_http   | 115 ms                                                                                                                | 121 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.05x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.58 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| asyncio_websockets         | 392 ms                                                                                                                | 396 ms: 1.01x slower                                                                                                      |
| asyncio_tcp                | 369 ms                                                                                                                | 372 ms: 1.01x slower                                                                                                      |
| coroutines                 | 21.8 ms                                                                                                               | 22.1 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                                                                                | 556 ms: 1.02x slower                                                                                                      |
| async_tree_io              | 816 ms                                                                                                                | 840 ms: 1.03x slower                                                                                                      |
| async_tree_none            | 320 ms                                                                                                                | 330 ms: 1.03x slower                                                                                                      |
| async_generators           | 359 ms                                                                                                                | 382 ms: 1.06x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                                                               | 75.7 ms: 1.05x faster                                                                                                     |
| pidigits       | 252 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| nbody          | 84.9 ms                                                                                                               | 89.1 ms: 1.05x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.00x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                                                                               | 3.33 ms: 1.05x faster                                                                                                     |
| regex_v8       | 26.6 ms                                                                                                               | 25.9 ms: 1.03x faster                                                                                                     |
| regex_dna      | 239 ms                                                                                                                | 234 ms: 1.02x faster                                                                                                      |
| regex_compile  | 139 ms                                                                                                                | 147 ms: 1.06x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                                                                              | 2.15 sec: 1.21x faster                                                                                                    |
| xml_etree_generate   | 84.5 ms                                                                                                               | 79.0 ms: 1.07x faster                                                                                                     |
| xml_etree_process    | 58.9 ms                                                                                                               | 55.3 ms: 1.06x faster                                                                                                     |
| json_dumps           | 10.9 ms                                                                                                               | 10.7 ms: 1.02x faster                                                                                                     |
| xml_etree_iterparse  | 100.0 ms                                                                                                              | 98.6 ms: 1.01x faster                                                                                                     |
| unpickle_pure_python | 213 us                                                                                                                | 212 us: 1.01x faster                                                                                                      |
| pickle_pure_python   | 314 us                                                                                                                | 320 us: 1.02x slower                                                                                                      |
| json_loads           | 24.6 us                                                                                                               | 25.1 us: 1.02x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                                                               | 13.4 ms: 1.00x slower                                                                                                     |
| python_startup_no_site | 9.06 ms                                                                                                               | 9.09 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                                                                               | 9.23 ms: 1.12x faster                                                                                                     |
| django_template | 39.7 ms                                                                                                               | 42.4 ms: 1.07x slower                                                                                                     |
| genshi_xml      | 53.4 ms                                                                                                               | 61.3 ms: 1.15x slower                                                                                                     |
| genshi_text     | 24.8 ms                                                                                                               | 29.4 ms: 1.19x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.07x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                | 2.59 sec                                                                                                              | 2.15 sec: 1.21x faster                                                                                                    |
| spectral_norm              | 96.3 ms                                                                                                               | 81.4 ms: 1.18x faster                                                                                                     |
| richards                   | 50.1 ms                                                                                                               | 43.7 ms: 1.15x faster                                                                                                     |
| mako                       | 10.4 ms                                                                                                               | 9.23 ms: 1.12x faster                                                                                                     |
| richards_super             | 56.3 ms                                                                                                               | 50.3 ms: 1.12x faster                                                                                                     |
| deepcopy_memo              | 29.8 us                                                                                                               | 26.7 us: 1.12x faster                                                                                                     |
| xml_etree_generate         | 84.5 ms                                                                                                               | 79.0 ms: 1.07x faster                                                                                                     |
| xml_etree_process          | 58.9 ms                                                                                                               | 55.3 ms: 1.06x faster                                                                                                     |
| deltablue                  | 3.39 ms                                                                                                               | 3.18 ms: 1.06x faster                                                                                                     |
| pyflate                    | 496 ms                                                                                                                | 468 ms: 1.06x faster                                                                                                      |
| create_gc_cycles           | 2.01 ms                                                                                                               | 1.91 ms: 1.05x faster                                                                                                     |
| regex_effbot               | 3.49 ms                                                                                                               | 3.33 ms: 1.05x faster                                                                                                     |
| float                      | 79.4 ms                                                                                                               | 75.7 ms: 1.05x faster                                                                                                     |
| dulwich_log                | 68.2 ms                                                                                                               | 65.8 ms: 1.04x faster                                                                                                     |
| crypto_pyaes               | 72.1 ms                                                                                                               | 69.7 ms: 1.03x faster                                                                                                     |
| pprint_safe_repr           | 806 ms                                                                                                                | 780 ms: 1.03x faster                                                                                                      |
| scimark_sor                | 108 ms                                                                                                                | 105 ms: 1.03x faster                                                                                                      |
| scimark_fft                | 300 ms                                                                                                                | 291 ms: 1.03x faster                                                                                                      |
| bpe_tokeniser              | 4.85 sec                                                                                                              | 4.73 sec: 1.03x faster                                                                                                    |
| regex_v8                   | 26.6 ms                                                                                                               | 25.9 ms: 1.03x faster                                                                                                     |
| gc_traversal               | 4.49 ms                                                                                                               | 4.38 ms: 1.03x faster                                                                                                     |
| coverage                   | 81.1 ms                                                                                                               | 79.2 ms: 1.02x faster                                                                                                     |
| html5lib                   | 70.4 ms                                                                                                               | 68.9 ms: 1.02x faster                                                                                                     |
| json_dumps                 | 10.9 ms                                                                                                               | 10.7 ms: 1.02x faster                                                                                                     |
| regex_dna                  | 239 ms                                                                                                                | 234 ms: 1.02x faster                                                                                                      |
| xml_etree_iterparse        | 100.0 ms                                                                                                              | 98.6 ms: 1.01x faster                                                                                                     |
| fannkuch                   | 354 ms                                                                                                                | 350 ms: 1.01x faster                                                                                                      |
| pprint_pformat             | 1.64 sec                                                                                                              | 1.63 sec: 1.01x faster                                                                                                    |
| pidigits                   | 252 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| unpickle_pure_python       | 213 us                                                                                                                | 212 us: 1.01x faster                                                                                                      |
| python_startup             | 13.4 ms                                                                                                               | 13.4 ms: 1.00x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.58 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| python_startup_no_site     | 9.06 ms                                                                                                               | 9.09 ms: 1.00x slower                                                                                                     |
| scimark_sparse_mat_mult    | 4.11 ms                                                                                                               | 4.14 ms: 1.01x slower                                                                                                     |
| meteor_contest             | 127 ms                                                                                                                | 128 ms: 1.01x slower                                                                                                      |
| asyncio_websockets         | 392 ms                                                                                                                | 396 ms: 1.01x slower                                                                                                      |
| asyncio_tcp                | 369 ms                                                                                                                | 372 ms: 1.01x slower                                                                                                      |
| pathlib                    | 15.7 ms                                                                                                               | 15.9 ms: 1.01x slower                                                                                                     |
| coroutines                 | 21.8 ms                                                                                                               | 22.1 ms: 1.01x slower                                                                                                     |
| deepcopy_reduce            | 2.89 us                                                                                                               | 2.94 us: 1.01x slower                                                                                                     |
| logging_simple             | 6.27 us                                                                                                               | 6.36 us: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                                                                                | 556 ms: 1.02x slower                                                                                                      |
| pickle_pure_python         | 314 us                                                                                                                | 320 us: 1.02x slower                                                                                                      |
| json_loads                 | 24.6 us                                                                                                               | 25.1 us: 1.02x slower                                                                                                     |
| logging_silent             | 97.6 ns                                                                                                               | 100 ns: 1.03x slower                                                                                                      |
| async_tree_io              | 816 ms                                                                                                                | 840 ms: 1.03x slower                                                                                                      |
| json                       | 5.21 ms                                                                                                               | 5.37 ms: 1.03x slower                                                                                                     |
| logging_format             | 6.80 us                                                                                                               | 7.00 us: 1.03x slower                                                                                                     |
| async_tree_none            | 320 ms                                                                                                                | 330 ms: 1.03x slower                                                                                                      |
| scimark_lu                 | 93.9 ms                                                                                                               | 96.7 ms: 1.03x slower                                                                                                     |
| mdp                        | 2.49 sec                                                                                                              | 2.59 sec: 1.04x slower                                                                                                    |
| pycparser                  | 1.21 sec                                                                                                              | 1.25 sec: 1.04x slower                                                                                                    |
| scimark_monte_carlo        | 65.8 ms                                                                                                               | 68.6 ms: 1.04x slower                                                                                                     |
| thrift                     | 852 us                                                                                                                | 894 us: 1.05x slower                                                                                                      |
| nbody                      | 84.9 ms                                                                                                               | 89.1 ms: 1.05x slower                                                                                                     |
| tornado_http               | 115 ms                                                                                                                | 121 ms: 1.05x slower                                                                                                      |
| deepcopy                   | 287 us                                                                                                                | 303 us: 1.06x slower                                                                                                      |
| sympy_expand               | 499 ms                                                                                                                | 528 ms: 1.06x slower                                                                                                      |
| regex_compile              | 139 ms                                                                                                                | 147 ms: 1.06x slower                                                                                                      |
| async_generators           | 359 ms                                                                                                                | 382 ms: 1.06x slower                                                                                                      |
| sqlglot_parse              | 1.41 ms                                                                                                               | 1.50 ms: 1.06x slower                                                                                                     |
| django_template            | 39.7 ms                                                                                                               | 42.4 ms: 1.07x slower                                                                                                     |
| sympy_str                  | 291 ms                                                                                                                | 311 ms: 1.07x slower                                                                                                      |
| typing_runtime_protocols   | 170 us                                                                                                                | 182 us: 1.07x slower                                                                                                      |
| bench_thread_pool          | 861 us                                                                                                                | 925 us: 1.07x slower                                                                                                      |
| comprehensions             | 17.2 us                                                                                                               | 18.5 us: 1.08x slower                                                                                                     |
| sqlglot_normalize          | 119 ms                                                                                                                | 130 ms: 1.09x slower                                                                                                      |
| sqlglot_transpile          | 1.78 ms                                                                                                               | 1.94 ms: 1.09x slower                                                                                                     |
| docutils                   | 2.90 sec                                                                                                              | 3.16 sec: 1.09x slower                                                                                                    |
| chaos                      | 61.8 ms                                                                                                               | 67.6 ms: 1.09x slower                                                                                                     |
| nqueens                    | 89.3 ms                                                                                                               | 98.2 ms: 1.10x slower                                                                                                     |
| 2to3                       | 281 ms                                                                                                                | 310 ms: 1.10x slower                                                                                                      |
| sqlglot_optimize           | 59.0 ms                                                                                                               | 65.6 ms: 1.11x slower                                                                                                     |
| hexiom                     | 6.27 ms                                                                                                               | 7.00 ms: 1.12x slower                                                                                                     |
| sympy_sum                  | 152 ms                                                                                                                | 170 ms: 1.12x slower                                                                                                      |
| bench_mp_pool              | 4.62 ms                                                                                                               | 5.20 ms: 1.12x slower                                                                                                     |
| go                         | 135 ms                                                                                                                | 152 ms: 1.13x slower                                                                                                      |
| raytrace                   | 271 ms                                                                                                                | 309 ms: 1.14x slower                                                                                                      |
| genshi_xml                 | 53.4 ms                                                                                                               | 61.3 ms: 1.15x slower                                                                                                     |
| sympy_integrate            | 22.9 ms                                                                                                               | 26.4 ms: 1.16x slower                                                                                                     |
| pylint                     | 347 ms                                                                                                                | 409 ms: 1.18x slower                                                                                                      |
| genshi_text                | 24.8 ms                                                                                                               | 29.4 ms: 1.19x slower                                                                                                     |
| generators                 | 28.3 ms                                                                                                               | 37.2 ms: 1.31x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (7): telco, async_tree_cpu_io_mixed, xml_etree_parse, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.017x slower
# HPT report

- Reliability score: 95.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x