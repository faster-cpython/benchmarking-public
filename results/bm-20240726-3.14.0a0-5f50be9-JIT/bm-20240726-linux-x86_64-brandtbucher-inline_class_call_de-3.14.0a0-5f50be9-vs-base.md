# Results vs. base

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5f50be9
- commit date: 2024-07-26
- overall geometric mean: 1.01x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 272 ms: 1.00x slower                                                        |
| html5lib       | 64.7 ms                                                               | 64.4 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| async_generators       | 456 ms                                                                | 462 ms: 1.01x slower                                                        |
| coroutines             | 22.8 ms                                                               | 23.1 ms: 1.02x slower                                                       |
| asyncio_tcp            | 487 ms                                                                | 497 ms: 1.02x slower                                                        |
| async_tree_memoization | 406 ms                                                                | 420 ms: 1.04x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 79.4 ms                                                               | 78.9 ms: 1.01x faster                                                       |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 226 ms                                                                | 221 ms: 1.02x faster                                                        |
| regex_compile  | 133 ms                                                                | 135 ms: 1.01x slower                                                        |
| regex_effbot   | 3.68 ms                                                               | 3.74 ms: 1.02x slower                                                       |
| regex_v8       | 24.5 ms                                                               | 26.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 147 ms                                                                | 144 ms: 1.02x faster                                                        |
| pickle_pure_python   | 297 us                                                                | 293 us: 1.01x faster                                                        |
| xml_etree_generate   | 80.6 ms                                                               | 79.9 ms: 1.01x faster                                                       |
| unpickle_pure_python | 215 us                                                                | 216 us: 1.00x slower                                                        |
| xml_etree_iterparse  | 98.7 ms                                                               | 99.2 ms: 1.01x slower                                                       |
| json_loads           | 27.8 us                                                               | 28.0 us: 1.01x slower                                                       |
| tomli_loads          | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.00x faster                                                       |
| python_startup_no_site | 7.22 ms                                                               | 7.20 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                               | 35.0 ms: 1.01x faster                                                       |
| mako            | 9.67 ms                                                               | 9.81 ms: 1.01x slower                                                       |
| genshi_text     | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                                       |
| genshi_xml      | 56.7 ms                                                               | 58.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 168 us                                                                | 162 us: 1.04x faster                                                        |
| mdp                      | 2.67 sec                                                              | 2.60 sec: 1.03x faster                                                      |
| regex_dna                | 226 ms                                                                | 221 ms: 1.02x faster                                                        |
| xml_etree_parse          | 147 ms                                                                | 144 ms: 1.02x faster                                                        |
| bpe_tokeniser            | 4.53 sec                                                              | 4.45 sec: 1.02x faster                                                      |
| pickle_pure_python       | 297 us                                                                | 293 us: 1.01x faster                                                        |
| django_template          | 35.5 ms                                                               | 35.0 ms: 1.01x faster                                                       |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                       |
| deepcopy                 | 271 us                                                                | 269 us: 1.01x faster                                                        |
| xml_etree_generate       | 80.6 ms                                                               | 79.9 ms: 1.01x faster                                                       |
| hexiom                   | 6.57 ms                                                               | 6.52 ms: 1.01x faster                                                       |
| html5lib                 | 64.7 ms                                                               | 64.4 ms: 1.01x faster                                                       |
| nbody                    | 79.4 ms                                                               | 78.9 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 56.2 ms                                                               | 55.9 ms: 1.01x faster                                                       |
| python_startup           | 10.7 ms                                                               | 10.6 ms: 1.00x faster                                                       |
| create_gc_cycles         | 1.77 ms                                                               | 1.77 ms: 1.00x faster                                                       |
| sympy_integrate          | 22.3 ms                                                               | 22.3 ms: 1.00x faster                                                       |
| python_startup_no_site   | 7.22 ms                                                               | 7.20 ms: 1.00x faster                                                       |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| 2to3                     | 271 ms                                                                | 272 ms: 1.00x slower                                                        |
| bench_thread_pool        | 824 us                                                                | 827 us: 1.00x slower                                                        |
| scimark_lu               | 125 ms                                                                | 125 ms: 1.00x slower                                                        |
| unpickle_pure_python     | 215 us                                                                | 216 us: 1.00x slower                                                        |
| xml_etree_iterparse      | 98.7 ms                                                               | 99.2 ms: 1.01x slower                                                       |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                        |
| fannkuch                 | 366 ms                                                                | 368 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.59 ms                                                               | 1.60 ms: 1.01x slower                                                       |
| coverage                 | 91.7 ms                                                               | 92.3 ms: 1.01x slower                                                       |
| json_loads               | 27.8 us                                                               | 28.0 us: 1.01x slower                                                       |
| sqlglot_parse            | 1.26 ms                                                               | 1.27 ms: 1.01x slower                                                       |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| raytrace                 | 266 ms                                                                | 268 ms: 1.01x slower                                                        |
| logging_simple           | 5.49 us                                                               | 5.55 us: 1.01x slower                                                       |
| json                     | 5.10 ms                                                               | 5.16 ms: 1.01x slower                                                       |
| nqueens                  | 85.2 ms                                                               | 86.2 ms: 1.01x slower                                                       |
| regex_compile            | 133 ms                                                                | 135 ms: 1.01x slower                                                        |
| deepcopy_memo            | 28.5 us                                                               | 28.8 us: 1.01x slower                                                       |
| async_generators         | 456 ms                                                                | 462 ms: 1.01x slower                                                        |
| mako                     | 9.67 ms                                                               | 9.81 ms: 1.01x slower                                                       |
| logging_format           | 6.06 us                                                               | 6.15 us: 1.01x slower                                                       |
| regex_effbot             | 3.68 ms                                                               | 3.74 ms: 1.02x slower                                                       |
| coroutines               | 22.8 ms                                                               | 23.1 ms: 1.02x slower                                                       |
| spectral_norm            | 101 ms                                                                | 103 ms: 1.02x slower                                                        |
| asyncio_tcp              | 487 ms                                                                | 497 ms: 1.02x slower                                                        |
| scimark_sor              | 126 ms                                                                | 129 ms: 1.02x slower                                                        |
| deepcopy_reduce          | 2.75 us                                                               | 2.81 us: 1.02x slower                                                       |
| thrift                   | 778 us                                                                | 798 us: 1.03x slower                                                        |
| genshi_text              | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                                       |
| async_tree_memoization   | 406 ms                                                                | 420 ms: 1.04x slower                                                        |
| logging_silent           | 101 ns                                                                | 105 ns: 1.04x slower                                                        |
| gc_traversal             | 3.73 ms                                                               | 3.87 ms: 1.04x slower                                                       |
| genshi_xml               | 56.7 ms                                                               | 58.8 ms: 1.04x slower                                                       |
| pycparser                | 1.12 sec                                                              | 1.17 sec: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 4.17 ms                                                               | 4.40 ms: 1.06x slower                                                       |
| regex_v8                 | 24.5 ms                                                               | 26.1 ms: 1.06x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (34): xml_etree_process, richards, pprint_safe_repr, generators, richards_super, sympy_sum, sqlglot_normalize, chaos, pathlib, scimark_fft, deltablue, pyflate, dask, pylint, async_tree_cpu_io_mixed, tornado_http, telco, bench_mp_pool, pprint_pformat, json_dumps, async_tree_cpu_io_mixed_tg, asyncio_websockets, sympy_expand, docutils, sympy_str, go, float, async_tree_none, scimark_monte_carlo, crypto_pyaes, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x