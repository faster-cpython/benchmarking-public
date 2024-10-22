# Results vs. base

- fork: encukou
- ref: intern_ūnus
- machine: linux-x86_64
- commit hash: a5da0a6
- commit date: 2024-07-26
- overall geometric mean: 1.00x faster
- HPT reliability: 66.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 263 ms                                                                | 262 ms: 1.00x faster                                          |
| html5lib       | 63.9 ms                                                               | 65.9 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_generators       | 432 ms                                                                | 431 ms: 1.00x faster                                          |
| asyncio_tcp_ssl        | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                        |
| async_tree_memoization | 399 ms                                                                | 413 ms: 1.04x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (10): coroutines, async_tree_none, async_tree_io, async_tree_io_tg, asyncio_websockets, asyncio_tcp, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 88.5 ms                                                               | 84.6 ms: 1.05x faster                                         |
| float          | 78.0 ms                                                               | 77.4 ms: 1.01x faster                                         |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 131 ms                                                                | 132 ms: 1.00x slower                                          |
| regex_dna      | 221 ms                                                                | 224 ms: 1.02x slower                                          |
| regex_v8       | 24.4 ms                                                               | 25.3 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_iterparse  | 105 ms                                                                | 104 ms: 1.01x faster                                          |
| xml_etree_process    | 59.0 ms                                                               | 58.5 ms: 1.01x faster                                         |
| pickle_pure_python   | 301 us                                                                | 299 us: 1.01x faster                                          |
| xml_etree_generate   | 85.3 ms                                                               | 84.7 ms: 1.01x faster                                         |
| unpickle_pure_python | 214 us                                                                | 213 us: 1.00x faster                                          |
| tomli_loads          | 2.04 sec                                                              | 2.09 sec: 1.02x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (3): json_dumps, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                         |
| python_startup_no_site | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                         |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 23.8 ms                                                               | 22.3 ms: 1.07x faster                                         |
| genshi_xml      | 51.6 ms                                                               | 50.0 ms: 1.03x faster                                         |
| django_template | 34.1 ms                                                               | 33.8 ms: 1.01x faster                                         |
| mako            | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                         |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.94 ms                                                               | 4.51 ms: 1.10x faster                                         |
| gc_traversal             | 3.72 ms                                                               | 3.49 ms: 1.07x faster                                         |
| genshi_text              | 23.8 ms                                                               | 22.3 ms: 1.07x faster                                         |
| nbody                    | 88.5 ms                                                               | 84.6 ms: 1.05x faster                                         |
| coverage                 | 92.6 ms                                                               | 89.3 ms: 1.04x faster                                         |
| genshi_xml               | 51.6 ms                                                               | 50.0 ms: 1.03x faster                                         |
| scimark_fft              | 366 ms                                                                | 355 ms: 1.03x faster                                          |
| pyflate                  | 483 ms                                                                | 469 ms: 1.03x faster                                          |
| logging_silent           | 99.6 ns                                                               | 97.5 ns: 1.02x faster                                         |
| deepcopy_memo            | 29.9 us                                                               | 29.5 us: 1.02x faster                                         |
| deltablue                | 3.17 ms                                                               | 3.12 ms: 1.01x faster                                         |
| sqlglot_normalize        | 108 ms                                                                | 106 ms: 1.01x faster                                          |
| create_gc_cycles         | 1.74 ms                                                               | 1.72 ms: 1.01x faster                                         |
| xml_etree_iterparse      | 105 ms                                                                | 104 ms: 1.01x faster                                          |
| django_template          | 34.1 ms                                                               | 33.8 ms: 1.01x faster                                         |
| hexiom                   | 6.21 ms                                                               | 6.14 ms: 1.01x faster                                         |
| xml_etree_process        | 59.0 ms                                                               | 58.5 ms: 1.01x faster                                         |
| pickle_pure_python       | 301 us                                                                | 299 us: 1.01x faster                                          |
| float                    | 78.0 ms                                                               | 77.4 ms: 1.01x faster                                         |
| sqlglot_optimize         | 53.6 ms                                                               | 53.2 ms: 1.01x faster                                         |
| xml_etree_generate       | 85.3 ms                                                               | 84.7 ms: 1.01x faster                                         |
| raytrace                 | 257 ms                                                                | 255 ms: 1.01x faster                                          |
| scimark_lu               | 113 ms                                                                | 112 ms: 1.01x faster                                          |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                         |
| unpickle_pure_python     | 214 us                                                                | 213 us: 1.00x faster                                          |
| generators               | 28.1 ms                                                               | 28.0 ms: 1.00x faster                                         |
| python_startup_no_site   | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                         |
| async_generators         | 432 ms                                                                | 431 ms: 1.00x faster                                          |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                        |
| 2to3                     | 263 ms                                                                | 262 ms: 1.00x faster                                          |
| meteor_contest           | 107 ms                                                                | 107 ms: 1.00x faster                                          |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                          |
| mdp                      | 2.52 sec                                                              | 2.52 sec: 1.00x slower                                        |
| bench_thread_pool        | 784 us                                                                | 786 us: 1.00x slower                                          |
| richards                 | 45.1 ms                                                               | 45.3 ms: 1.00x slower                                         |
| regex_compile            | 131 ms                                                                | 132 ms: 1.00x slower                                          |
| logging_simple           | 5.45 us                                                               | 5.49 us: 1.01x slower                                         |
| chaos                    | 58.4 ms                                                               | 58.9 ms: 1.01x slower                                         |
| sqlglot_transpile        | 1.57 ms                                                               | 1.58 ms: 1.01x slower                                         |
| pprint_safe_repr         | 739 ms                                                                | 745 ms: 1.01x slower                                          |
| thrift                   | 773 us                                                                | 783 us: 1.01x slower                                          |
| pprint_pformat           | 1.51 sec                                                              | 1.53 sec: 1.01x slower                                        |
| spectral_norm            | 111 ms                                                                | 113 ms: 1.01x slower                                          |
| regex_dna                | 221 ms                                                                | 224 ms: 1.02x slower                                          |
| pycparser                | 1.16 sec                                                              | 1.18 sec: 1.02x slower                                        |
| mako                     | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                         |
| tomli_loads              | 2.04 sec                                                              | 2.09 sec: 1.02x slower                                        |
| nqueens                  | 79.7 ms                                                               | 82.2 ms: 1.03x slower                                         |
| html5lib                 | 63.9 ms                                                               | 65.9 ms: 1.03x slower                                         |
| typing_runtime_protocols | 162 us                                                                | 167 us: 1.03x slower                                          |
| async_tree_memoization   | 399 ms                                                                | 413 ms: 1.04x slower                                          |
| regex_v8                 | 24.4 ms                                                               | 25.3 ms: 1.04x slower                                         |
| crypto_pyaes             | 72.1 ms                                                               | 75.1 ms: 1.04x slower                                         |
| scimark_monte_carlo      | 67.7 ms                                                               | 71.4 ms: 1.05x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (36): json, sympy_expand, sympy_str, sympy_sum, coroutines, bpe_tokeniser, async_tree_none, dask, sqlglot_parse, async_tree_io, deepcopy, async_tree_io_tg, telco, scimark_sor, sympy_integrate, json_dumps, asyncio_websockets, asyncio_tcp, pylint, go, pathlib, bench_mp_pool, tornado_http, async_tree_none_tg, richards_super, comprehensions, fannkuch, regex_effbot, logging_format, json_loads, docutils, async_tree_memoization_tg, deepcopy_reduce, xml_etree_parse, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 66.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x