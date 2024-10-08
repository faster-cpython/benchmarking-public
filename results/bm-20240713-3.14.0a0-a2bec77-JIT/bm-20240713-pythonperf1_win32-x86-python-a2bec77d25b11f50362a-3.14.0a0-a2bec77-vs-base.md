# Results vs. base

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 93.16%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                                                                   | 253 ms: 1.02x slower                                                                                                         |
| docutils       | 1.87 sec                                                                                                                 | 1.93 sec: 1.03x slower                                                                                                       |
| html5lib       | 48.6 ms                                                                                                                  | 47.0 ms: 1.03x faster                                                                                                        |
| tornado_http   | 95.0 ms                                                                                                                  | 97.5 ms: 1.03x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                    | 1.01x slower                                                                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 477 ms                                                                                                                   | 468 ms: 1.02x faster                                                                                                         |
| async_tree_none            | 225 ms                                                                                                                   | 220 ms: 1.02x faster                                                                                                         |
| async_tree_cpu_io_mixed_tg | 466 ms                                                                                                                   | 458 ms: 1.02x faster                                                                                                         |
| async_tree_io              | 546 ms                                                                                                                   | 538 ms: 1.01x faster                                                                                                         |
| Geometric mean             | (ref)                                                                                                                    | 1.01x faster                                                                                                                 |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 89.0 ms                                                                                                                  | 54.7 ms: 1.63x faster                                                                                                        |
| float          | 58.9 ms                                                                                                                  | 43.9 ms: 1.34x faster                                                                                                        |
| pidigits       | 196 ms                                                                                                                   | 195 ms: 1.01x faster                                                                                                         |
| Geometric mean | (ref)                                                                                                                    | 1.30x faster                                                                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                                                                   | 95.3 ms: 1.09x faster                                                                                                        |
| regex_v8       | 16.0 ms                                                                                                                  | 16.0 ms: 1.00x slower                                                                                                        |
| regex_effbot   | 1.92 ms                                                                                                                  | 1.99 ms: 1.04x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                    | 1.01x faster                                                                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| pickle_pure_python   | 250 us                                                                                                                   | 209 us: 1.20x faster                                                                                                         |
| tomli_loads          | 1.79 sec                                                                                                                 | 1.53 sec: 1.17x faster                                                                                                       |
| unpickle_pure_python | 167 us                                                                                                                   | 147 us: 1.13x faster                                                                                                         |
| xml_etree_generate   | 68.3 ms                                                                                                                  | 61.4 ms: 1.11x faster                                                                                                        |
| xml_etree_process    | 49.7 ms                                                                                                                  | 46.5 ms: 1.07x faster                                                                                                        |
| xml_etree_iterparse  | 66.0 ms                                                                                                                  | 61.9 ms: 1.07x faster                                                                                                        |
| xml_etree_parse      | 105 ms                                                                                                                   | 104 ms: 1.01x faster                                                                                                         |
| json_loads           | 21.2 us                                                                                                                  | 21.0 us: 1.01x faster                                                                                                        |
| Geometric mean       | (ref)                                                                                                                    | 1.08x faster                                                                                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                                                                                  | 23.1 ms: 1.01x slower                                                                                                        |
| python_startup_no_site | 18.9 ms                                                                                                                  | 19.1 ms: 1.01x slower                                                                                                        |
| Geometric mean         | (ref)                                                                                                                    | 1.01x slower                                                                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| mako           | 7.95 ms                                                                                                                  | 5.44 ms: 1.46x faster                                                                                                        |
| genshi_text    | 21.9 ms                                                                                                                  | 23.5 ms: 1.07x slower                                                                                                        |
| genshi_xml     | 46.3 ms                                                                                                                  | 53.6 ms: 1.16x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                    | 1.04x faster                                                                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 89.0 ms                                                                                                                  | 54.7 ms: 1.63x faster                                                                                                        |
| spectral_norm              | 75.3 ms                                                                                                                  | 47.2 ms: 1.60x faster                                                                                                        |
| mako                       | 7.95 ms                                                                                                                  | 5.44 ms: 1.46x faster                                                                                                        |
| deepcopy_memo              | 21.4 us                                                                                                                  | 15.3 us: 1.40x faster                                                                                                        |
| float                      | 58.9 ms                                                                                                                  | 43.9 ms: 1.34x faster                                                                                                        |
| scimark_fft                | 220 ms                                                                                                                   | 166 ms: 1.33x faster                                                                                                         |
| fannkuch                   | 309 ms                                                                                                                   | 236 ms: 1.31x faster                                                                                                         |
| scimark_sparse_mat_mult    | 3.09 ms                                                                                                                  | 2.38 ms: 1.30x faster                                                                                                        |
| logging_silent             | 74.9 ns                                                                                                                  | 58.4 ns: 1.28x faster                                                                                                        |
| scimark_monte_carlo        | 52.4 ms                                                                                                                  | 42.3 ms: 1.24x faster                                                                                                        |
| pyflate                    | 335 ms                                                                                                                   | 277 ms: 1.21x faster                                                                                                         |
| crypto_pyaes               | 57.7 ms                                                                                                                  | 48.0 ms: 1.20x faster                                                                                                        |
| pickle_pure_python         | 250 us                                                                                                                   | 209 us: 1.20x faster                                                                                                         |
| telco                      | 6.35 ms                                                                                                                  | 5.31 ms: 1.20x faster                                                                                                        |
| tomli_loads                | 1.79 sec                                                                                                                 | 1.53 sec: 1.17x faster                                                                                                       |
| comprehensions             | 13.3 us                                                                                                                  | 11.5 us: 1.16x faster                                                                                                        |
| unpickle_pure_python       | 167 us                                                                                                                   | 147 us: 1.13x faster                                                                                                         |
| pprint_safe_repr           | 634 ms                                                                                                                   | 565 ms: 1.12x faster                                                                                                         |
| pprint_pformat             | 1.30 sec                                                                                                                 | 1.16 sec: 1.11x faster                                                                                                       |
| xml_etree_generate         | 68.3 ms                                                                                                                  | 61.4 ms: 1.11x faster                                                                                                        |
| sqlglot_parse              | 1.05 ms                                                                                                                  | 956 us: 1.09x faster                                                                                                         |
| richards                   | 36.8 ms                                                                                                                  | 33.7 ms: 1.09x faster                                                                                                        |
| regex_compile              | 103 ms                                                                                                                   | 95.3 ms: 1.09x faster                                                                                                        |
| xml_etree_process          | 49.7 ms                                                                                                                  | 46.5 ms: 1.07x faster                                                                                                        |
| xml_etree_iterparse        | 66.0 ms                                                                                                                  | 61.9 ms: 1.07x faster                                                                                                        |
| hexiom                     | 5.01 ms                                                                                                                  | 4.70 ms: 1.07x faster                                                                                                        |
| meteor_contest             | 79.1 ms                                                                                                                  | 75.1 ms: 1.05x faster                                                                                                        |
| sqlglot_transpile          | 1.28 ms                                                                                                                  | 1.22 ms: 1.05x faster                                                                                                        |
| json                       | 4.41 ms                                                                                                                  | 4.20 ms: 1.05x faster                                                                                                        |
| richards_super             | 40.7 ms                                                                                                                  | 39.1 ms: 1.04x faster                                                                                                        |
| html5lib                   | 48.6 ms                                                                                                                  | 47.0 ms: 1.03x faster                                                                                                        |
| chaos                      | 53.8 ms                                                                                                                  | 52.3 ms: 1.03x faster                                                                                                        |
| logging_format             | 8.43 us                                                                                                                  | 8.21 us: 1.03x faster                                                                                                        |
| thrift                     | 778 us                                                                                                                   | 760 us: 1.02x faster                                                                                                         |
| logging_simple             | 7.74 us                                                                                                                  | 7.56 us: 1.02x faster                                                                                                        |
| deepcopy_reduce            | 2.47 us                                                                                                                  | 2.41 us: 1.02x faster                                                                                                        |
| async_tree_cpu_io_mixed    | 477 ms                                                                                                                   | 468 ms: 1.02x faster                                                                                                         |
| async_tree_none            | 225 ms                                                                                                                   | 220 ms: 1.02x faster                                                                                                         |
| deepcopy                   | 241 us                                                                                                                   | 237 us: 1.02x faster                                                                                                         |
| async_tree_cpu_io_mixed_tg | 466 ms                                                                                                                   | 458 ms: 1.02x faster                                                                                                         |
| async_tree_io              | 546 ms                                                                                                                   | 538 ms: 1.01x faster                                                                                                         |
| xml_etree_parse            | 105 ms                                                                                                                   | 104 ms: 1.01x faster                                                                                                         |
| coverage                   | 52.6 ms                                                                                                                  | 52.0 ms: 1.01x faster                                                                                                        |
| json_loads                 | 21.2 us                                                                                                                  | 21.0 us: 1.01x faster                                                                                                        |
| go                         | 114 ms                                                                                                                   | 113 ms: 1.01x faster                                                                                                         |
| pidigits                   | 196 ms                                                                                                                   | 195 ms: 1.01x faster                                                                                                         |
| regex_v8                   | 16.0 ms                                                                                                                  | 16.0 ms: 1.00x slower                                                                                                        |
| asyncio_tcp_ssl            | 16.8 sec                                                                                                                 | 16.9 sec: 1.01x slower                                                                                                       |
| python_startup             | 22.9 ms                                                                                                                  | 23.1 ms: 1.01x slower                                                                                                        |
| sympy_str                  | 218 ms                                                                                                                   | 220 ms: 1.01x slower                                                                                                         |
| python_startup_no_site     | 18.9 ms                                                                                                                  | 19.1 ms: 1.01x slower                                                                                                        |
| create_gc_cycles           | 748 us                                                                                                                   | 757 us: 1.01x slower                                                                                                         |
| 2to3                       | 249 ms                                                                                                                   | 253 ms: 1.02x slower                                                                                                         |
| pycparser                  | 824 ms                                                                                                                   | 845 ms: 1.02x slower                                                                                                         |
| tornado_http               | 95.0 ms                                                                                                                  | 97.5 ms: 1.03x slower                                                                                                        |
| sympy_sum                  | 108 ms                                                                                                                   | 111 ms: 1.03x slower                                                                                                         |
| sqlglot_optimize           | 43.1 ms                                                                                                                  | 44.4 ms: 1.03x slower                                                                                                        |
| deltablue                  | 2.61 ms                                                                                                                  | 2.69 ms: 1.03x slower                                                                                                        |
| sympy_expand               | 381 ms                                                                                                                   | 393 ms: 1.03x slower                                                                                                         |
| docutils                   | 1.87 sec                                                                                                                 | 1.93 sec: 1.03x slower                                                                                                       |
| generators                 | 26.6 ms                                                                                                                  | 27.6 ms: 1.03x slower                                                                                                        |
| regex_effbot               | 1.92 ms                                                                                                                  | 1.99 ms: 1.04x slower                                                                                                        |
| bench_mp_pool              | 70.5 ms                                                                                                                  | 73.7 ms: 1.05x slower                                                                                                        |
| sympy_integrate            | 15.3 ms                                                                                                                  | 16.0 ms: 1.05x slower                                                                                                        |
| coroutines                 | 17.2 ms                                                                                                                  | 18.0 ms: 1.05x slower                                                                                                        |
| raytrace                   | 215 ms                                                                                                                   | 229 ms: 1.06x slower                                                                                                         |
| genshi_text                | 21.9 ms                                                                                                                  | 23.5 ms: 1.07x slower                                                                                                        |
| sqlglot_normalize          | 226 ms                                                                                                                   | 241 ms: 1.07x slower                                                                                                         |
| async_generators           | 285 ms                                                                                                                   | 307 ms: 1.08x slower                                                                                                         |
| pylint                     | 223 ms                                                                                                                   | 241 ms: 1.08x slower                                                                                                         |
| scimark_sor                | 95.0 ms                                                                                                                  | 104 ms: 1.10x slower                                                                                                         |
| genshi_xml                 | 46.3 ms                                                                                                                  | 53.6 ms: 1.16x slower                                                                                                        |
| scimark_lu                 | 67.2 ms                                                                                                                  | 82.6 ms: 1.23x slower                                                                                                        |
| Geometric mean             | (ref)                                                                                                                    | 1.05x faster                                                                                                                 |

Benchmark hidden because not significant (14): async_tree_io_tg, bench_thread_pool, async_tree_memoization, async_tree_none_tg, pathlib, regex_dna, django_template, mdp, nqueens, json_dumps, typing_runtime_protocols, gc_traversal, async_tree_memoization_tg, asyncio_tcp

# HPT report

- Reliability score: 93.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown