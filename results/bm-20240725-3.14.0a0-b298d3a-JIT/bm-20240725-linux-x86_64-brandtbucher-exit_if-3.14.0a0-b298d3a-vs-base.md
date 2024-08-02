# Results vs. base

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: b298d3a
- commit date: 2024-07-25
- overall geometric mean: 1.00x slower
- HPT reliability: 77.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| html5lib       | 65.2 ms                                                               | 64.6 ms: 1.01x faster                                          |
| tornado_http   | 94.4 ms                                                               | 93.5 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_generators | 455 ms                                                                | 453 ms: 1.00x faster                                           |
| asyncio_tcp      | 501 ms                                                                | 504 ms: 1.01x slower                                           |
| coroutines       | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                          |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (10): async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, asyncio_websockets, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 79.4 ms: 1.03x faster                                          |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 136 ms                                                                | 135 ms: 1.01x faster                                           |
| regex_dna      | 228 ms                                                                | 227 ms: 1.01x faster                                           |
| regex_effbot   | 3.73 ms                                                               | 3.77 ms: 1.01x slower                                          |
| regex_v8       | 23.8 ms                                                               | 25.8 ms: 1.08x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate  | 81.4 ms                                                               | 80.8 ms: 1.01x faster                                          |
| pickle_pure_python  | 297 us                                                                | 295 us: 1.01x faster                                           |
| xml_etree_iterparse | 98.8 ms                                                               | 98.3 ms: 1.00x faster                                          |
| tomli_loads         | 1.93 sec                                                              | 1.96 sec: 1.01x slower                                         |
| json_loads          | 27.7 us                                                               | 28.1 us: 1.02x slower                                          |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_process, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                          |
| python_startup_no_site | 7.24 ms                                                               | 7.17 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako           | 9.78 ms                                                               | 9.73 ms: 1.00x faster                                          |
| genshi_xml     | 58.0 ms                                                               | 58.4 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal            | 3.86 ms                                                               | 3.58 ms: 1.08x faster                                          |
| mdp                     | 2.66 sec                                                              | 2.53 sec: 1.05x faster                                         |
| scimark_sparse_mat_mult | 4.34 ms                                                               | 4.21 ms: 1.03x faster                                          |
| nbody                   | 81.6 ms                                                               | 79.4 ms: 1.03x faster                                          |
| deepcopy_reduce         | 2.80 us                                                               | 2.74 us: 1.02x faster                                          |
| dulwich_log             | 69.8 ms                                                               | 68.5 ms: 1.02x faster                                          |
| scimark_fft             | 307 ms                                                                | 302 ms: 1.02x faster                                           |
| create_gc_cycles        | 1.77 ms                                                               | 1.75 ms: 1.02x faster                                          |
| nqueens                 | 87.0 ms                                                               | 85.7 ms: 1.02x faster                                          |
| sympy_sum               | 170 ms                                                                | 168 ms: 1.01x faster                                           |
| python_startup          | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                          |
| tornado_http            | 94.4 ms                                                               | 93.5 ms: 1.01x faster                                          |
| coverage                | 92.4 ms                                                               | 91.4 ms: 1.01x faster                                          |
| python_startup_no_site  | 7.24 ms                                                               | 7.17 ms: 1.01x faster                                          |
| html5lib                | 65.2 ms                                                               | 64.6 ms: 1.01x faster                                          |
| pyflate                 | 436 ms                                                                | 432 ms: 1.01x faster                                           |
| xml_etree_generate      | 81.4 ms                                                               | 80.8 ms: 1.01x faster                                          |
| regex_compile           | 136 ms                                                                | 135 ms: 1.01x faster                                           |
| spectral_norm           | 101 ms                                                                | 100 ms: 1.01x faster                                           |
| comprehensions          | 16.5 us                                                               | 16.4 us: 1.01x faster                                          |
| pickle_pure_python      | 297 us                                                                | 295 us: 1.01x faster                                           |
| chaos                   | 58.0 ms                                                               | 57.7 ms: 1.01x faster                                          |
| regex_dna               | 228 ms                                                                | 227 ms: 1.01x faster                                           |
| xml_etree_iterparse     | 98.8 ms                                                               | 98.3 ms: 1.00x faster                                          |
| mako                    | 9.78 ms                                                               | 9.73 ms: 1.00x faster                                          |
| sympy_str               | 297 ms                                                                | 296 ms: 1.00x faster                                           |
| sympy_expand            | 501 ms                                                                | 499 ms: 1.00x faster                                           |
| async_generators        | 455 ms                                                                | 453 ms: 1.00x faster                                           |
| sympy_integrate         | 22.2 ms                                                               | 22.2 ms: 1.00x faster                                          |
| bench_thread_pool       | 822 us                                                                | 824 us: 1.00x slower                                           |
| pidigits                | 185 ms                                                                | 186 ms: 1.00x slower                                           |
| richards                | 40.1 ms                                                               | 40.4 ms: 1.01x slower                                          |
| asyncio_tcp             | 501 ms                                                                | 504 ms: 1.01x slower                                           |
| logging_simple          | 5.56 us                                                               | 5.60 us: 1.01x slower                                          |
| fannkuch                | 369 ms                                                                | 372 ms: 1.01x slower                                           |
| genshi_xml              | 58.0 ms                                                               | 58.4 ms: 1.01x slower                                          |
| go                      | 145 ms                                                                | 146 ms: 1.01x slower                                           |
| regex_effbot            | 3.73 ms                                                               | 3.77 ms: 1.01x slower                                          |
| tomli_loads             | 1.93 sec                                                              | 1.96 sec: 1.01x slower                                         |
| coroutines              | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                          |
| richards_super          | 45.9 ms                                                               | 46.6 ms: 1.01x slower                                          |
| json                    | 5.17 ms                                                               | 5.25 ms: 1.02x slower                                          |
| thrift                  | 791 us                                                                | 804 us: 1.02x slower                                           |
| json_loads              | 27.7 us                                                               | 28.1 us: 1.02x slower                                          |
| scimark_monte_carlo     | 59.9 ms                                                               | 60.9 ms: 1.02x slower                                          |
| raytrace                | 266 ms                                                                | 271 ms: 1.02x slower                                           |
| deepcopy_memo           | 28.2 us                                                               | 28.7 us: 1.02x slower                                          |
| scimark_lu              | 124 ms                                                                | 127 ms: 1.02x slower                                           |
| logging_silent          | 103 ns                                                                | 106 ns: 1.03x slower                                           |
| deltablue               | 3.51 ms                                                               | 3.61 ms: 1.03x slower                                          |
| scimark_sor             | 125 ms                                                                | 130 ms: 1.04x slower                                           |
| pycparser               | 1.12 sec                                                              | 1.17 sec: 1.04x slower                                         |
| regex_v8                | 23.8 ms                                                               | 25.8 ms: 1.08x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (38): pprint_safe_repr, unpickle_pure_python, dask, async_tree_io, async_tree_cpu_io_mixed, sqlglot_parse, async_tree_none, sqlglot_normalize, crypto_pyaes, xml_etree_process, generators, pathlib, sqlglot_optimize, bpe_tokeniser, pylint, django_template, meteor_contest, docutils, genshi_text, bench_mp_pool, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, hexiom, asyncio_websockets, async_tree_none_tg, async_tree_io_tg, sqlglot_transpile, 2to3, deepcopy, async_tree_memoization_tg, float, json_dumps, logging_format, async_tree_memoization, telco, xml_etree_parse, pprint_pformat

# HPT report

- Reliability score: 77.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x