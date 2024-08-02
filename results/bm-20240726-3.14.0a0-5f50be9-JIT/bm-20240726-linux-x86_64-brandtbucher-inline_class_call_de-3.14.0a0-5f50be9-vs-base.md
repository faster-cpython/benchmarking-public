# Results vs. base

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5f50be9
- commit date: 2024-07-26
- overall geometric mean: 1.00x slower
- HPT reliability: 96.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 272 ms: 1.00x slower                                                        |
| docutils       | 2.89 sec                                                              | 2.91 sec: 1.00x slower                                                      |
| html5lib       | 65.8 ms                                                               | 64.4 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines             | 23.3 ms                                                               | 23.1 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| async_generators       | 459 ms                                                                | 462 ms: 1.01x slower                                                        |
| async_tree_memoization | 409 ms                                                                | 420 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_io_tg, async_tree_none, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 81.2 ms                                                               | 78.9 ms: 1.03x faster                                                       |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| float          | 70.5 ms                                                               | 71.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                | 221 ms: 1.01x faster                                                        |
| regex_compile  | 134 ms                                                                | 135 ms: 1.01x slower                                                        |
| regex_effbot   | 3.69 ms                                                               | 3.74 ms: 1.01x slower                                                       |
| regex_v8       | 23.7 ms                                                               | 26.1 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse     | 147 ms                                                                | 144 ms: 1.02x faster                                                        |
| pickle_pure_python  | 298 us                                                                | 293 us: 1.02x faster                                                        |
| xml_etree_iterparse | 99.9 ms                                                               | 99.2 ms: 1.01x faster                                                       |
| xml_etree_generate  | 80.3 ms                                                               | 79.9 ms: 1.00x faster                                                       |
| json_loads          | 27.6 us                                                               | 28.0 us: 1.01x slower                                                       |
| tomli_loads         | 1.92 sec                                                              | 1.95 sec: 1.02x slower                                                      |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 7.16 ms                                                               | 7.20 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                               | 35.0 ms: 1.01x faster                                                       |
| genshi_xml      | 59.4 ms                                                               | 58.8 ms: 1.01x faster                                                       |
| mako            | 9.85 ms                                                               | 9.81 ms: 1.00x faster                                                       |
| genshi_text     | 24.8 ms                                                               | 25.4 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 170 us                                                                | 162 us: 1.05x faster                                                        |
| nbody                    | 81.2 ms                                                               | 78.9 ms: 1.03x faster                                                       |
| xml_etree_parse          | 147 ms                                                                | 144 ms: 1.02x faster                                                        |
| html5lib                 | 65.8 ms                                                               | 64.4 ms: 1.02x faster                                                       |
| pickle_pure_python       | 298 us                                                                | 293 us: 1.02x faster                                                        |
| bpe_tokeniser            | 4.52 sec                                                              | 4.45 sec: 1.02x faster                                                      |
| django_template          | 35.5 ms                                                               | 35.0 ms: 1.01x faster                                                       |
| regex_dna                | 223 ms                                                                | 221 ms: 1.01x faster                                                        |
| scimark_sor              | 130 ms                                                                | 129 ms: 1.01x faster                                                        |
| genshi_xml               | 59.4 ms                                                               | 58.8 ms: 1.01x faster                                                       |
| coroutines               | 23.3 ms                                                               | 23.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 99.9 ms                                                               | 99.2 ms: 1.01x faster                                                       |
| xml_etree_generate       | 80.3 ms                                                               | 79.9 ms: 1.00x faster                                                       |
| sympy_sum                | 169 ms                                                                | 168 ms: 1.00x faster                                                        |
| mako                     | 9.85 ms                                                               | 9.81 ms: 1.00x faster                                                       |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| 2to3                     | 271 ms                                                                | 272 ms: 1.00x slower                                                        |
| bench_thread_pool        | 824 us                                                                | 827 us: 1.00x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                               | 1.77 ms: 1.00x slower                                                       |
| scimark_fft              | 306 ms                                                                | 307 ms: 1.00x slower                                                        |
| docutils                 | 2.89 sec                                                              | 2.91 sec: 1.00x slower                                                      |
| regex_compile            | 134 ms                                                                | 135 ms: 1.01x slower                                                        |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| sqlglot_transpile        | 1.59 ms                                                               | 1.60 ms: 1.01x slower                                                       |
| python_startup_no_site   | 7.16 ms                                                               | 7.20 ms: 1.01x slower                                                       |
| async_generators         | 459 ms                                                                | 462 ms: 1.01x slower                                                        |
| sympy_str                | 293 ms                                                                | 295 ms: 1.01x slower                                                        |
| comprehensions           | 16.4 us                                                               | 16.5 us: 1.01x slower                                                       |
| crypto_pyaes             | 66.6 ms                                                               | 67.2 ms: 1.01x slower                                                       |
| generators               | 28.4 ms                                                               | 28.7 ms: 1.01x slower                                                       |
| telco                    | 7.87 ms                                                               | 7.94 ms: 1.01x slower                                                       |
| sympy_expand             | 497 ms                                                                | 502 ms: 1.01x slower                                                        |
| spectral_norm            | 102 ms                                                                | 103 ms: 1.01x slower                                                        |
| richards                 | 40.0 ms                                                               | 40.4 ms: 1.01x slower                                                       |
| float                    | 70.5 ms                                                               | 71.2 ms: 1.01x slower                                                       |
| deltablue                | 3.46 ms                                                               | 3.50 ms: 1.01x slower                                                       |
| thrift                   | 790 us                                                                | 798 us: 1.01x slower                                                        |
| raytrace                 | 265 ms                                                                | 268 ms: 1.01x slower                                                        |
| json_loads               | 27.6 us                                                               | 28.0 us: 1.01x slower                                                       |
| logging_format           | 6.07 us                                                               | 6.15 us: 1.01x slower                                                       |
| regex_effbot             | 3.69 ms                                                               | 3.74 ms: 1.01x slower                                                       |
| pyflate                  | 431 ms                                                                | 438 ms: 1.02x slower                                                        |
| meteor_contest           | 104 ms                                                                | 106 ms: 1.02x slower                                                        |
| tomli_loads              | 1.92 sec                                                              | 1.95 sec: 1.02x slower                                                      |
| deepcopy_memo            | 28.3 us                                                               | 28.8 us: 1.02x slower                                                       |
| deepcopy_reduce          | 2.75 us                                                               | 2.81 us: 1.02x slower                                                       |
| mdp                      | 2.55 sec                                                              | 2.60 sec: 1.02x slower                                                      |
| logging_silent           | 102 ns                                                                | 105 ns: 1.02x slower                                                        |
| genshi_text              | 24.8 ms                                                               | 25.4 ms: 1.02x slower                                                       |
| async_tree_memoization   | 409 ms                                                                | 420 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult  | 4.24 ms                                                               | 4.40 ms: 1.04x slower                                                       |
| pycparser                | 1.11 sec                                                              | 1.17 sec: 1.05x slower                                                      |
| gc_traversal             | 3.67 ms                                                               | 3.87 ms: 1.06x slower                                                       |
| regex_v8                 | 23.7 ms                                                               | 26.1 ms: 1.10x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (35): unpickle_pure_python, pprint_safe_repr, pprint_pformat, nqueens, pathlib, fannkuch, xml_etree_process, deepcopy, tornado_http, async_tree_memoization_tg, sqlglot_optimize, dask, sqlglot_normalize, async_tree_cpu_io_mixed_tg, asyncio_websockets, scimark_monte_carlo, async_tree_io, hexiom, logging_simple, go, bench_mp_pool, async_tree_io_tg, async_tree_none, asyncio_tcp, async_tree_cpu_io_mixed, coverage, json, sympy_integrate, chaos, pylint, sqlglot_parse, json_dumps, scimark_lu, async_tree_none_tg, richards_super

# HPT report

- Reliability score: 96.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x