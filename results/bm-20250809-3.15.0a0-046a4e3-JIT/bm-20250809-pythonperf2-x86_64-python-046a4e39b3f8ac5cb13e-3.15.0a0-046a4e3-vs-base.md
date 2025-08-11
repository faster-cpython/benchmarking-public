# Results vs. base

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.005x faster
- HPT reliability: 82.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                                | 287 ms: 1.02x slower                                                                                                      |
| docutils       | 2.87 sec                                                                                                              | 2.91 sec: 1.01x slower                                                                                                    |
| html5lib       | 66.1 ms                                                                                                               | 66.8 ms: 1.01x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                | 371 ms                                                                                                                | 369 ms: 1.01x faster                                                                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                                                                                | 504 ms: 1.00x slower                                                                                                      |
| async_tree_io              | 620 ms                                                                                                                | 624 ms: 1.01x slower                                                                                                      |
| asyncio_websockets         | 381 ms                                                                                                                | 386 ms: 1.01x slower                                                                                                      |
| coroutines                 | 22.1 ms                                                                                                               | 22.7 ms: 1.03x slower                                                                                                     |
| async_generators           | 422 ms                                                                                                                | 442 ms: 1.05x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 67.9 ms                                                                                                               | 65.4 ms: 1.04x faster                                                                                                     |
| pidigits       | 255 ms                                                                                                                | 255 ms: 1.00x faster                                                                                                      |
| nbody          | 91.8 ms                                                                                                               | 101 ms: 1.10x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 224 ms                                                                                                                | 222 ms: 1.01x faster                                                                                                      |
| regex_compile  | 131 ms                                                                                                                | 133 ms: 1.01x slower                                                                                                      |
| regex_v8       | 23.5 ms                                                                                                               | 24.4 ms: 1.04x slower                                                                                                     |
| regex_effbot   | 3.51 ms                                                                                                               | 3.84 ms: 1.09x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.03x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 204 us                                                                                                                | 192 us: 1.06x faster                                                                                                      |
| xml_etree_process    | 57.7 ms                                                                                                               | 55.1 ms: 1.05x faster                                                                                                     |
| xml_etree_generate   | 82.9 ms                                                                                                               | 79.4 ms: 1.04x faster                                                                                                     |
| tomli_loads          | 1.99 sec                                                                                                              | 1.91 sec: 1.04x faster                                                                                                    |
| xml_etree_parse      | 140 ms                                                                                                                | 138 ms: 1.02x faster                                                                                                      |
| unpickle_list        | 5.12 us                                                                                                               | 5.06 us: 1.01x faster                                                                                                     |
| pickle               | 12.1 us                                                                                                               | 12.2 us: 1.01x slower                                                                                                     |
| pickle_pure_python   | 327 us                                                                                                                | 332 us: 1.02x slower                                                                                                      |
| pickle_list          | 4.98 us                                                                                                               | 5.18 us: 1.04x slower                                                                                                     |
| pickle_dict          | 32.6 us                                                                                                               | 34.6 us: 1.06x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (4): json_dumps, json_loads, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                                                               | 15.3 ms: 1.00x slower                                                                                                     |
| python_startup_no_site | 8.80 ms                                                                                                               | 8.83 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako           | 10.7 ms                                                                                                               | 9.86 ms: 1.09x faster                                                                                                     |
| genshi_xml     | 53.4 ms                                                                                                               | 54.1 ms: 1.01x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| richards                   | 44.5 ms                                                                                                               | 33.9 ms: 1.31x faster                                                                                                     |
| richards_super             | 50.7 ms                                                                                                               | 40.0 ms: 1.27x faster                                                                                                     |
| deltablue                  | 3.15 ms                                                                                                               | 2.84 ms: 1.11x faster                                                                                                     |
| spectral_norm              | 86.5 ms                                                                                                               | 78.6 ms: 1.10x faster                                                                                                     |
| mako                       | 10.7 ms                                                                                                               | 9.86 ms: 1.09x faster                                                                                                     |
| unpickle_pure_python       | 204 us                                                                                                                | 192 us: 1.06x faster                                                                                                      |
| xml_etree_process          | 57.7 ms                                                                                                               | 55.1 ms: 1.05x faster                                                                                                     |
| bpe_tokeniser              | 4.71 sec                                                                                                              | 4.51 sec: 1.04x faster                                                                                                    |
| xml_etree_generate         | 82.9 ms                                                                                                               | 79.4 ms: 1.04x faster                                                                                                     |
| connected_components       | 424 ms                                                                                                                | 407 ms: 1.04x faster                                                                                                      |
| tomli_loads                | 1.99 sec                                                                                                              | 1.91 sec: 1.04x faster                                                                                                    |
| float                      | 67.9 ms                                                                                                               | 65.4 ms: 1.04x faster                                                                                                     |
| scimark_monte_carlo        | 64.8 ms                                                                                                               | 62.8 ms: 1.03x faster                                                                                                     |
| pprint_safe_repr           | 756 ms                                                                                                                | 733 ms: 1.03x faster                                                                                                      |
| k_core                     | 2.08 sec                                                                                                              | 2.02 sec: 1.03x faster                                                                                                    |
| shortest_path              | 455 ms                                                                                                                | 442 ms: 1.03x faster                                                                                                      |
| gc_traversal               | 6.74 ms                                                                                                               | 6.55 ms: 1.03x faster                                                                                                     |
| pprint_pformat             | 1.54 sec                                                                                                              | 1.50 sec: 1.03x faster                                                                                                    |
| json                       | 5.57 ms                                                                                                               | 5.45 ms: 1.02x faster                                                                                                     |
| xml_etree_parse            | 140 ms                                                                                                                | 138 ms: 1.02x faster                                                                                                      |
| scimark_fft                | 311 ms                                                                                                                | 306 ms: 1.02x faster                                                                                                      |
| sqlite_synth               | 2.87 us                                                                                                               | 2.83 us: 1.01x faster                                                                                                     |
| unpickle_list              | 5.12 us                                                                                                               | 5.06 us: 1.01x faster                                                                                                     |
| pycparser                  | 1.24 sec                                                                                                              | 1.23 sec: 1.01x faster                                                                                                    |
| coverage                   | 83.6 ms                                                                                                               | 82.7 ms: 1.01x faster                                                                                                     |
| scimark_sor                | 103 ms                                                                                                                | 102 ms: 1.01x faster                                                                                                      |
| logging_simple             | 5.98 us                                                                                                               | 5.93 us: 1.01x faster                                                                                                     |
| logging_format             | 6.54 us                                                                                                               | 6.49 us: 1.01x faster                                                                                                     |
| fannkuch                   | 367 ms                                                                                                                | 364 ms: 1.01x faster                                                                                                      |
| regex_dna                  | 224 ms                                                                                                                | 222 ms: 1.01x faster                                                                                                      |
| asyncio_tcp                | 371 ms                                                                                                                | 369 ms: 1.01x faster                                                                                                      |
| pidigits                   | 255 ms                                                                                                                | 255 ms: 1.00x faster                                                                                                      |
| python_startup             | 15.3 ms                                                                                                               | 15.3 ms: 1.00x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.58 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| python_startup_no_site     | 8.80 ms                                                                                                               | 8.83 ms: 1.00x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                                                                                | 504 ms: 1.00x slower                                                                                                      |
| pathlib                    | 16.6 ms                                                                                                               | 16.7 ms: 1.00x slower                                                                                                     |
| pickle                     | 12.1 us                                                                                                               | 12.2 us: 1.01x slower                                                                                                     |
| sqlglot_v2_parse           | 1.30 ms                                                                                                               | 1.31 ms: 1.01x slower                                                                                                     |
| async_tree_io              | 620 ms                                                                                                                | 624 ms: 1.01x slower                                                                                                      |
| subparsers                 | 42.4 ms                                                                                                               | 42.7 ms: 1.01x slower                                                                                                     |
| create_gc_cycles           | 2.90 ms                                                                                                               | 2.92 ms: 1.01x slower                                                                                                     |
| meteor_contest             | 120 ms                                                                                                                | 121 ms: 1.01x slower                                                                                                      |
| html5lib                   | 66.1 ms                                                                                                               | 66.8 ms: 1.01x slower                                                                                                     |
| chaos                      | 58.8 ms                                                                                                               | 59.4 ms: 1.01x slower                                                                                                     |
| sqlglot_v2_transpile       | 1.67 ms                                                                                                               | 1.69 ms: 1.01x slower                                                                                                     |
| scimark_lu                 | 94.0 ms                                                                                                               | 95.1 ms: 1.01x slower                                                                                                     |
| asyncio_websockets         | 381 ms                                                                                                                | 386 ms: 1.01x slower                                                                                                      |
| deepcopy_memo              | 27.2 us                                                                                                               | 27.5 us: 1.01x slower                                                                                                     |
| regex_compile              | 131 ms                                                                                                                | 133 ms: 1.01x slower                                                                                                      |
| many_optionals             | 1.21 ms                                                                                                               | 1.22 ms: 1.01x slower                                                                                                     |
| scimark_sparse_mat_mult    | 4.92 ms                                                                                                               | 4.99 ms: 1.01x slower                                                                                                     |
| docutils                   | 2.87 sec                                                                                                              | 2.91 sec: 1.01x slower                                                                                                    |
| genshi_xml                 | 53.4 ms                                                                                                               | 54.1 ms: 1.01x slower                                                                                                     |
| nqueens                    | 92.2 ms                                                                                                               | 93.5 ms: 1.01x slower                                                                                                     |
| mdp                        | 1.27 sec                                                                                                              | 1.29 sec: 1.01x slower                                                                                                    |
| pickle_pure_python         | 327 us                                                                                                                | 332 us: 1.02x slower                                                                                                      |
| deepcopy                   | 274 us                                                                                                                | 279 us: 1.02x slower                                                                                                      |
| typing_runtime_protocols   | 166 us                                                                                                                | 169 us: 1.02x slower                                                                                                      |
| sympy_integrate            | 21.9 ms                                                                                                               | 22.4 ms: 1.02x slower                                                                                                     |
| 2to3                       | 281 ms                                                                                                                | 287 ms: 1.02x slower                                                                                                      |
| sqlglot_v2_normalize       | 111 ms                                                                                                                | 114 ms: 1.02x slower                                                                                                      |
| sympy_str                  | 285 ms                                                                                                                | 292 ms: 1.02x slower                                                                                                      |
| sqlglot_v2_optimize        | 55.8 ms                                                                                                               | 57.3 ms: 1.03x slower                                                                                                     |
| coroutines                 | 22.1 ms                                                                                                               | 22.7 ms: 1.03x slower                                                                                                     |
| raytrace                   | 274 ms                                                                                                                | 281 ms: 1.03x slower                                                                                                      |
| sympy_expand               | 489 ms                                                                                                                | 503 ms: 1.03x slower                                                                                                      |
| crypto_pyaes               | 75.6 ms                                                                                                               | 78.4 ms: 1.04x slower                                                                                                     |
| regex_v8                   | 23.5 ms                                                                                                               | 24.4 ms: 1.04x slower                                                                                                     |
| pickle_list                | 4.98 us                                                                                                               | 5.18 us: 1.04x slower                                                                                                     |
| async_generators           | 422 ms                                                                                                                | 442 ms: 1.05x slower                                                                                                      |
| go                         | 119 ms                                                                                                                | 126 ms: 1.06x slower                                                                                                      |
| pickle_dict                | 32.6 us                                                                                                               | 34.6 us: 1.06x slower                                                                                                     |
| hexiom                     | 5.79 ms                                                                                                               | 6.17 ms: 1.06x slower                                                                                                     |
| comprehensions             | 16.1 us                                                                                                               | 17.4 us: 1.08x slower                                                                                                     |
| regex_effbot               | 3.51 ms                                                                                                               | 3.84 ms: 1.09x slower                                                                                                     |
| nbody                      | 91.8 ms                                                                                                               | 101 ms: 1.10x slower                                                                                                      |
| generators                 | 27.9 ms                                                                                                               | 31.5 ms: 1.13x slower                                                                                                     |
| unpack_sequence            | 42.1 ns                                                                                                               | 49.0 ns: 1.16x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (24): async_tree_memoization_tg, genshi_text, deepcopy_reduce, async_tree_memoization, async_tree_cpu_io_mixed, json_dumps, async_tree_none_tg, pyflate, djangocms, logging_silent, django_template, sympy_sum, telco, dulwich_log, json_loads, sphinx, xml_etree_iterparse, async_tree_io_tg, thrift, unpickle, async_tree_none, pylint, bench_thread_pool, bench_mp_pool

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 82.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x