# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.370x faster
- HPT reliability: 59.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                                                               | 216 ms: 1.02x faster                                                                                                     |
| docutils       | 1.62 sec                                                                                                             | 1.68 sec: 1.04x slower                                                                                                   |
| sphinx         | 635 ms                                                                                                               | 652 ms: 1.03x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 169 ms                                                                                                               | 170 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 328 ms                                                                                                               | 332 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 338 ms                                                                                                               | 342 ms: 1.01x slower                                                                                                     |
| async_tree_io_tg           | 395 ms                                                                                                               | 402 ms: 1.02x slower                                                                                                     |
| asyncio_websockets         | 161 ms                                                                                                               | 167 ms: 1.04x slower                                                                                                     |
| async_generators           | 227 ms                                                                                                               | 246 ms: 1.08x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (5): async_tree_io, coroutines, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 60.9 ms                                                                                                              | 59.7 ms: 1.02x faster                                                                                                    |
| float          | 43.9 ms                                                                                                              | 43.4 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 79.6 ms                                                                                                              | 70.6 ms: 1.13x faster                                                                                                    |
| regex_dna      | 116 ms                                                                                                               | 119 ms: 1.03x slower                                                                                                     |
| regex_v8       | 13.1 ms                                                                                                              | 13.9 ms: 1.06x slower                                                                                                    |
| regex_effbot   | 1.45 ms                                                                                                              | 1.66 ms: 1.15x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                                                               | 110 us: 1.22x faster                                                                                                     |
| tomli_loads          | 1.35 sec                                                                                                             | 1.15 sec: 1.17x faster                                                                                                   |
| xml_etree_process    | 39.1 ms                                                                                                              | 36.2 ms: 1.08x faster                                                                                                    |
| xml_etree_generate   | 55.9 ms                                                                                                              | 52.0 ms: 1.07x faster                                                                                                    |
| pickle_pure_python   | 212 us                                                                                                               | 207 us: 1.02x faster                                                                                                     |
| json_loads           | 14.1 us                                                                                                              | 14.4 us: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.3 ms                                                                                                              | 19.6 ms: 1.02x slower                                                                                                    |
| python_startup         | 25.5 ms                                                                                                              | 26.0 ms: 1.02x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.38 ms                                                                                                              | 5.43 ms: 1.17x faster                                                                                                    |
| django_template | 24.6 ms                                                                                                              | 24.2 ms: 1.01x faster                                                                                                    |
| genshi_text     | 15.2 ms                                                                                                              | 15.3 ms: 1.01x slower                                                                                                    |
| genshi_xml      | 33.9 ms                                                                                                              | 34.3 ms: 1.01x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.04x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat             | 1.09 sec                                                                                                             | 995 ns: 1091777.90x faster                                                                                               |
| pprint_safe_repr           | 533 ms                                                                                                               | 579 ns: 919794.86x faster                                                                                                |
| unpickle_pure_python       | 134 us                                                                                                               | 110 us: 1.22x faster                                                                                                     |
| mako                       | 6.38 ms                                                                                                              | 5.43 ms: 1.17x faster                                                                                                    |
| tomli_loads                | 1.35 sec                                                                                                             | 1.15 sec: 1.17x faster                                                                                                   |
| regex_compile              | 79.6 ms                                                                                                              | 70.6 ms: 1.13x faster                                                                                                    |
| bpe_tokeniser              | 2.89 sec                                                                                                             | 2.62 sec: 1.10x faster                                                                                                   |
| xml_etree_process          | 39.1 ms                                                                                                              | 36.2 ms: 1.08x faster                                                                                                    |
| xml_etree_generate         | 55.9 ms                                                                                                              | 52.0 ms: 1.07x faster                                                                                                    |
| telco                      | 4.65 ms                                                                                                              | 4.35 ms: 1.07x faster                                                                                                    |
| scimark_fft                | 172 ms                                                                                                               | 161 ms: 1.07x faster                                                                                                     |
| pyflate                    | 278 ms                                                                                                               | 263 ms: 1.06x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.49 ms                                                                                                              | 2.37 ms: 1.05x faster                                                                                                    |
| k_core                     | 1.71 sec                                                                                                             | 1.64 sec: 1.04x faster                                                                                                   |
| nqueens                    | 60.6 ms                                                                                                              | 58.9 ms: 1.03x faster                                                                                                    |
| subparsers                 | 17.1 ms                                                                                                              | 16.7 ms: 1.03x faster                                                                                                    |
| deepcopy_reduce            | 1.84 us                                                                                                              | 1.80 us: 1.02x faster                                                                                                    |
| pickle_pure_python         | 212 us                                                                                                               | 207 us: 1.02x faster                                                                                                     |
| nbody                      | 60.9 ms                                                                                                              | 59.7 ms: 1.02x faster                                                                                                    |
| sqlglot_v2_normalize       | 70.5 ms                                                                                                              | 69.1 ms: 1.02x faster                                                                                                    |
| coverage                   | 49.4 ms                                                                                                              | 48.4 ms: 1.02x faster                                                                                                    |
| fannkuch                   | 255 ms                                                                                                               | 250 ms: 1.02x faster                                                                                                     |
| dulwich_log                | 41.2 ms                                                                                                              | 40.4 ms: 1.02x faster                                                                                                    |
| sqlglot_v2_parse           | 815 us                                                                                                               | 799 us: 1.02x faster                                                                                                     |
| connected_components       | 335 ms                                                                                                               | 328 ms: 1.02x faster                                                                                                     |
| sqlglot_v2_transpile       | 1.02 ms                                                                                                              | 1.00 ms: 1.02x faster                                                                                                    |
| 2to3                       | 220 ms                                                                                                               | 216 ms: 1.02x faster                                                                                                     |
| sqlite_synth               | 1.58 us                                                                                                              | 1.56 us: 1.02x faster                                                                                                    |
| shortest_path              | 365 ms                                                                                                               | 359 ms: 1.02x faster                                                                                                     |
| many_optionals             | 441 us                                                                                                               | 435 us: 1.02x faster                                                                                                     |
| django_template            | 24.6 ms                                                                                                              | 24.2 ms: 1.01x faster                                                                                                    |
| richards                   | 27.4 ms                                                                                                              | 27.0 ms: 1.01x faster                                                                                                    |
| logging_silent             | 320 ns                                                                                                               | 316 ns: 1.01x faster                                                                                                     |
| deepcopy                   | 170 us                                                                                                               | 168 us: 1.01x faster                                                                                                     |
| richards_super             | 30.9 ms                                                                                                              | 30.5 ms: 1.01x faster                                                                                                    |
| logging_simple             | 6.26 us                                                                                                              | 6.19 us: 1.01x faster                                                                                                    |
| float                      | 43.9 ms                                                                                                              | 43.4 ms: 1.01x faster                                                                                                    |
| scimark_lu                 | 57.1 ms                                                                                                              | 56.8 ms: 1.01x faster                                                                                                    |
| generators                 | 19.8 ms                                                                                                              | 19.6 ms: 1.01x faster                                                                                                    |
| async_tree_none            | 169 ms                                                                                                               | 170 ms: 1.01x slower                                                                                                     |
| chaos                      | 39.3 ms                                                                                                              | 39.6 ms: 1.01x slower                                                                                                    |
| mdp                        | 795 ms                                                                                                               | 802 ms: 1.01x slower                                                                                                     |
| create_gc_cycles           | 1.32 ms                                                                                                              | 1.34 ms: 1.01x slower                                                                                                    |
| go                         | 75.7 ms                                                                                                              | 76.4 ms: 1.01x slower                                                                                                    |
| sympy_str                  | 169 ms                                                                                                               | 170 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 328 ms                                                                                                               | 332 ms: 1.01x slower                                                                                                     |
| genshi_text                | 15.2 ms                                                                                                              | 15.3 ms: 1.01x slower                                                                                                    |
| sympy_integrate            | 12.4 ms                                                                                                              | 12.5 ms: 1.01x slower                                                                                                    |
| genshi_xml                 | 33.9 ms                                                                                                              | 34.3 ms: 1.01x slower                                                                                                    |
| hexiom                     | 4.00 ms                                                                                                              | 4.06 ms: 1.01x slower                                                                                                    |
| raytrace                   | 180 ms                                                                                                               | 183 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 338 ms                                                                                                               | 342 ms: 1.01x slower                                                                                                     |
| python_startup_no_site     | 19.3 ms                                                                                                              | 19.6 ms: 1.02x slower                                                                                                    |
| async_tree_io_tg           | 395 ms                                                                                                               | 402 ms: 1.02x slower                                                                                                     |
| comprehensions             | 10.6 us                                                                                                              | 10.8 us: 1.02x slower                                                                                                    |
| python_startup             | 25.5 ms                                                                                                              | 26.0 ms: 1.02x slower                                                                                                    |
| deepcopy_memo              | 17.3 us                                                                                                              | 17.7 us: 1.02x slower                                                                                                    |
| sympy_expand               | 289 ms                                                                                                               | 296 ms: 1.02x slower                                                                                                     |
| json_loads                 | 14.1 us                                                                                                              | 14.4 us: 1.03x slower                                                                                                    |
| regex_dna                  | 116 ms                                                                                                               | 119 ms: 1.03x slower                                                                                                     |
| sphinx                     | 635 ms                                                                                                               | 652 ms: 1.03x slower                                                                                                     |
| pycparser                  | 702 ms                                                                                                               | 722 ms: 1.03x slower                                                                                                     |
| scimark_monte_carlo        | 39.5 ms                                                                                                              | 40.7 ms: 1.03x slower                                                                                                    |
| scimark_sor                | 72.9 ms                                                                                                              | 75.0 ms: 1.03x slower                                                                                                    |
| meteor_contest             | 71.7 ms                                                                                                              | 74.3 ms: 1.04x slower                                                                                                    |
| docutils                   | 1.62 sec                                                                                                             | 1.68 sec: 1.04x slower                                                                                                   |
| asyncio_websockets         | 161 ms                                                                                                               | 167 ms: 1.04x slower                                                                                                     |
| typing_runtime_protocols   | 100 us                                                                                                               | 105 us: 1.04x slower                                                                                                     |
| regex_v8                   | 13.1 ms                                                                                                              | 13.9 ms: 1.06x slower                                                                                                    |
| spectral_norm              | 57.0 ms                                                                                                              | 60.8 ms: 1.07x slower                                                                                                    |
| async_generators           | 227 ms                                                                                                               | 246 ms: 1.08x slower                                                                                                     |
| regex_effbot               | 1.45 ms                                                                                                              | 1.66 ms: 1.15x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.36x faster                                                                                                             |

Benchmark hidden because not significant (20): async_tree_io, logging_format, json, json_dumps, pathlib, xml_etree_parse, coroutines, async_tree_memoization, deltablue, crypto_pyaes, async_tree_memoization_tg, thrift, pidigits, sympy_sum, xml_etree_iterparse, sqlglot_v2_optimize, async_tree_none_tg, html5lib, gc_traversal, pylint

- Geometric mean (including insignificant results): 1.370x faster

# HPT report

- Reliability score: 59.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown