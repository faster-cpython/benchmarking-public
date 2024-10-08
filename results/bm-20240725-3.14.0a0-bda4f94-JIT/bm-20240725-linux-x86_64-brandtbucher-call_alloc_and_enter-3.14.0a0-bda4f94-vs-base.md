# Results vs. base

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: bda4f94
- commit date: 2024-07-25
- overall geometric mean: 1.00x faster
- HPT reliability: 80.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tornado_http   | 93.1 ms                                                               | 92.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines       | 23.3 ms                                                               | 22.4 ms: 1.04x faster                                                       |
| asyncio_tcp      | 496 ms                                                                | 486 ms: 1.02x faster                                                        |
| async_generators | 459 ms                                                                | 455 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                      |
| Geometric mean   | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 81.2 ms                                                               | 79.9 ms: 1.02x faster                                                       |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                | 132 ms: 1.01x faster                                                        |
| regex_effbot   | 3.69 ms                                                               | 3.67 ms: 1.01x faster                                                       |
| regex_v8       | 23.7 ms                                                               | 24.0 ms: 1.01x slower                                                       |
| regex_dna      | 223 ms                                                                | 231 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse | 99.9 ms                                                               | 98.5 ms: 1.01x faster                                                       |
| xml_etree_process   | 56.4 ms                                                               | 55.9 ms: 1.01x faster                                                       |
| xml_etree_generate  | 80.3 ms                                                               | 79.7 ms: 1.01x faster                                                       |
| tomli_loads         | 1.92 sec                                                              | 1.93 sec: 1.01x slower                                                      |
| json_dumps          | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (4): unpickle_pure_python, pickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                               | 7.15 ms: 1.00x faster                                                       |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 9.85 ms                                                               | 9.85 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines               | 23.3 ms                                                               | 22.4 ms: 1.04x faster                                                       |
| gc_traversal             | 3.67 ms                                                               | 3.56 ms: 1.03x faster                                                       |
| asyncio_tcp              | 496 ms                                                                | 486 ms: 1.02x faster                                                        |
| spectral_norm            | 102 ms                                                                | 100 ms: 1.02x faster                                                        |
| scimark_sor              | 130 ms                                                                | 128 ms: 1.02x faster                                                        |
| nbody                    | 81.2 ms                                                               | 79.9 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 99.9 ms                                                               | 98.5 ms: 1.01x faster                                                       |
| typing_runtime_protocols | 170 us                                                                | 168 us: 1.01x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                       |
| regex_compile            | 134 ms                                                                | 132 ms: 1.01x faster                                                        |
| thrift                   | 790 us                                                                | 782 us: 1.01x faster                                                        |
| xml_etree_process        | 56.4 ms                                                               | 55.9 ms: 1.01x faster                                                       |
| tornado_http             | 93.1 ms                                                               | 92.3 ms: 1.01x faster                                                       |
| async_generators         | 459 ms                                                                | 455 ms: 1.01x faster                                                        |
| xml_etree_generate       | 80.3 ms                                                               | 79.7 ms: 1.01x faster                                                       |
| regex_effbot             | 3.69 ms                                                               | 3.67 ms: 1.01x faster                                                       |
| bpe_tokeniser            | 4.52 sec                                                              | 4.49 sec: 1.01x faster                                                      |
| coverage                 | 92.2 ms                                                               | 91.6 ms: 1.01x faster                                                       |
| crypto_pyaes             | 66.6 ms                                                               | 66.3 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                      |
| sympy_integrate          | 22.2 ms                                                               | 22.2 ms: 1.00x faster                                                       |
| python_startup_no_site   | 7.16 ms                                                               | 7.15 ms: 1.00x faster                                                       |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                       |
| mako                     | 9.85 ms                                                               | 9.85 ms: 1.00x slower                                                       |
| sympy_str                | 293 ms                                                                | 294 ms: 1.00x slower                                                        |
| sympy_expand             | 497 ms                                                                | 499 ms: 1.00x slower                                                        |
| generators               | 28.4 ms                                                               | 28.6 ms: 1.01x slower                                                       |
| tomli_loads              | 1.92 sec                                                              | 1.93 sec: 1.01x slower                                                      |
| comprehensions           | 16.4 us                                                               | 16.5 us: 1.01x slower                                                       |
| regex_v8                 | 23.7 ms                                                               | 24.0 ms: 1.01x slower                                                       |
| richards_super           | 46.3 ms                                                               | 46.9 ms: 1.01x slower                                                       |
| deepcopy_memo            | 28.3 us                                                               | 28.6 us: 1.01x slower                                                       |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| deltablue                | 3.46 ms                                                               | 3.51 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult  | 4.24 ms                                                               | 4.29 ms: 1.01x slower                                                       |
| richards                 | 40.0 ms                                                               | 40.5 ms: 1.01x slower                                                       |
| meteor_contest           | 104 ms                                                                | 106 ms: 1.02x slower                                                        |
| chaos                    | 57.5 ms                                                               | 58.4 ms: 1.02x slower                                                       |
| scimark_fft              | 306 ms                                                                | 312 ms: 1.02x slower                                                        |
| fannkuch                 | 369 ms                                                                | 377 ms: 1.02x slower                                                        |
| scimark_lu               | 125 ms                                                                | 127 ms: 1.02x slower                                                        |
| regex_dna                | 223 ms                                                                | 231 ms: 1.03x slower                                                        |
| logging_silent           | 102 ns                                                                | 107 ns: 1.04x slower                                                        |
| mdp                      | 2.55 sec                                                              | 2.71 sec: 1.07x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (45): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, unpickle_pure_python, async_tree_none_tg, pprint_pformat, async_tree_io_tg, async_tree_cpu_io_mixed, nqueens, pylint, genshi_xml, telco, async_tree_io, pathlib, sqlglot_normalize, pickle_pure_python, logging_simple, genshi_text, asyncio_websockets, deepcopy, sqlglot_transpile, 2to3, sympy_sum, json, json_loads, sqlglot_optimize, html5lib, docutils, hexiom, bench_mp_pool, bench_thread_pool, dask, float, sqlglot_parse, django_template, logging_format, go, pycparser, async_tree_none, xml_etree_parse, pyflate, pprint_safe_repr, raytrace, scimark_monte_carlo, deepcopy_reduce

# HPT report

- Reliability score: 80.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x