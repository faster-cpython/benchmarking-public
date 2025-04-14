# Results vs. base

- fork: python
- ref: 52b5eb95b770fa00ebbd
- machine: linux-x86_64
- commit hash: 52b5eb9
- commit date: 2025-03-26
- overall geometric mean: 1.005x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 258 ms: 1.01x slower                                                   |
| docutils       | 2.58 sec                                                               | 2.63 sec: 1.02x slower                                                 |
| sphinx         | 1.00 sec                                                               | 1.02 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 470 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 487 ms: 1.01x faster                                                   |
| async_tree_memoization     | 310 ms                                                                 | 311 ms: 1.00x slower                                                   |
| coroutines                 | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_generators, asyncio_websockets, async_tree_none_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 98.6 ms                                                                | 97.3 ms: 1.01x faster                                                  |
| float          | 69.1 ms                                                                | 70.5 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                   |
| regex_dna      | 220 ms                                                                 | 224 ms: 1.02x slower                                                   |
| regex_v8       | 22.5 ms                                                                | 23.0 ms: 1.02x slower                                                  |
| regex_effbot   | 3.21 ms                                                                | 3.47 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                                 |
| xml_etree_process    | 59.0 ms                                                                | 59.3 ms: 1.01x slower                                                  |
| xml_etree_generate   | 84.5 ms                                                                | 85.2 ms: 1.01x slower                                                  |
| unpickle_pure_python | 216 us                                                                 | 218 us: 1.01x slower                                                   |
| pickle_pure_python   | 314 us                                                                 | 319 us: 1.02x slower                                                   |
| json_dumps           | 11.3 ms                                                                | 11.7 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                  |
| python_startup_no_site | 8.17 ms                                                                | 8.19 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 21.4 ms: 1.01x slower                                                  |
| django_template | 31.6 ms                                                                | 32.0 ms: 1.01x slower                                                  |
| mako            | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                  |
| genshi_xml      | 48.7 ms                                                                | 50.0 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pyflate                    | 462 ms                                                                 | 442 ms: 1.04x faster                                                   |
| gc_traversal               | 5.01 ms                                                                | 4.84 ms: 1.04x faster                                                  |
| fannkuch                   | 428 ms                                                                 | 418 ms: 1.02x faster                                                   |
| connected_components       | 455 ms                                                                 | 449 ms: 1.01x faster                                                   |
| subparsers                 | 21.1 ms                                                                | 20.8 ms: 1.01x faster                                                  |
| spectral_norm              | 100 ms                                                                 | 99.0 ms: 1.01x faster                                                  |
| nbody                      | 98.6 ms                                                                | 97.3 ms: 1.01x faster                                                  |
| hexiom                     | 6.32 ms                                                                | 6.25 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 470 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 487 ms: 1.01x faster                                                   |
| dulwich_log                | 58.5 ms                                                                | 58.1 ms: 1.01x faster                                                  |
| sqlglot_v2_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                   |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                  |
| sqlglot_v2_optimize        | 52.9 ms                                                                | 53.0 ms: 1.00x slower                                                  |
| nqueens                    | 82.5 ms                                                                | 82.7 ms: 1.00x slower                                                  |
| comprehensions             | 16.8 us                                                                | 16.9 us: 1.00x slower                                                  |
| python_startup_no_site     | 8.17 ms                                                                | 8.19 ms: 1.00x slower                                                  |
| sqlalchemy_imperative      | 16.7 ms                                                                | 16.7 ms: 1.00x slower                                                  |
| many_optionals             | 947 us                                                                 | 951 us: 1.00x slower                                                   |
| chaos                      | 58.6 ms                                                                | 58.8 ms: 1.00x slower                                                  |
| async_tree_memoization     | 310 ms                                                                 | 311 ms: 1.00x slower                                                   |
| deepcopy_memo              | 29.2 us                                                                | 29.3 us: 1.00x slower                                                  |
| sqlglot_v2_parse           | 1.26 ms                                                                | 1.27 ms: 1.00x slower                                                  |
| sqlglot_v2_transpile       | 1.57 ms                                                                | 1.58 ms: 1.00x slower                                                  |
| tomli_loads                | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                                 |
| xml_etree_process          | 59.0 ms                                                                | 59.3 ms: 1.01x slower                                                  |
| sqlalchemy_declarative     | 130 ms                                                                 | 131 ms: 1.01x slower                                                   |
| sympy_expand               | 455 ms                                                                 | 458 ms: 1.01x slower                                                   |
| regex_compile              | 126 ms                                                                 | 127 ms: 1.01x slower                                                   |
| genshi_text                | 21.3 ms                                                                | 21.4 ms: 1.01x slower                                                  |
| deltablue                  | 3.14 ms                                                                | 3.16 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                                 | 161 us: 1.01x slower                                                   |
| raytrace                   | 264 ms                                                                 | 265 ms: 1.01x slower                                                   |
| generators                 | 28.4 ms                                                                | 28.6 ms: 1.01x slower                                                  |
| sympy_sum                  | 148 ms                                                                 | 149 ms: 1.01x slower                                                   |
| sympy_integrate            | 19.4 ms                                                                | 19.5 ms: 1.01x slower                                                  |
| coroutines                 | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                  |
| xml_etree_generate         | 84.5 ms                                                                | 85.2 ms: 1.01x slower                                                  |
| scimark_fft                | 351 ms                                                                 | 355 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 216 us                                                                 | 218 us: 1.01x slower                                                   |
| sympy_str                  | 266 ms                                                                 | 268 ms: 1.01x slower                                                   |
| 2to3                       | 256 ms                                                                 | 258 ms: 1.01x slower                                                   |
| django_template            | 31.6 ms                                                                | 32.0 ms: 1.01x slower                                                  |
| go                         | 116 ms                                                                 | 117 ms: 1.01x slower                                                   |
| scimark_sor                | 118 ms                                                                 | 120 ms: 1.01x slower                                                   |
| crypto_pyaes               | 73.5 ms                                                                | 74.5 ms: 1.01x slower                                                  |
| deepcopy_reduce            | 2.66 us                                                                | 2.69 us: 1.01x slower                                                  |
| mako                       | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.46 ms                                                                | 2.50 ms: 1.01x slower                                                  |
| sphinx                     | 1.00 sec                                                               | 1.02 sec: 1.02x slower                                                 |
| telco                      | 7.81 ms                                                                | 7.93 ms: 1.02x slower                                                  |
| deepcopy                   | 254 us                                                                 | 259 us: 1.02x slower                                                   |
| pickle_pure_python         | 314 us                                                                 | 319 us: 1.02x slower                                                   |
| float                      | 69.1 ms                                                                | 70.5 ms: 1.02x slower                                                  |
| regex_dna                  | 220 ms                                                                 | 224 ms: 1.02x slower                                                   |
| docutils                   | 2.58 sec                                                               | 2.63 sec: 1.02x slower                                                 |
| scimark_monte_carlo        | 66.7 ms                                                                | 68.0 ms: 1.02x slower                                                  |
| regex_v8                   | 22.5 ms                                                                | 23.0 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                                 | 117 ms: 1.03x slower                                                   |
| genshi_xml                 | 48.7 ms                                                                | 50.0 ms: 1.03x slower                                                  |
| richards                   | 43.2 ms                                                                | 44.5 ms: 1.03x slower                                                  |
| json_dumps                 | 11.3 ms                                                                | 11.7 ms: 1.03x slower                                                  |
| richards_super             | 49.4 ms                                                                | 51.0 ms: 1.03x slower                                                  |
| pycparser                  | 1.12 sec                                                               | 1.18 sec: 1.05x slower                                                 |
| regex_effbot               | 3.21 ms                                                                | 3.47 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (31): k_core, json, async_tree_io, async_tree_io_tg, pprint_safe_repr, bpe_tokeniser, logging_format, async_generators, json_loads, bench_mp_pool, xml_etree_parse, logging_silent, pidigits, coverage, bench_thread_pool, pprint_pformat, shortest_path, mdp, sqlite_synth, meteor_contest, asyncio_websockets, pathlib, html5lib, async_tree_none_tg, pylint, thrift, xml_etree_iterparse, logging_simple, scimark_sparse_mat_mult, async_tree_none, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x