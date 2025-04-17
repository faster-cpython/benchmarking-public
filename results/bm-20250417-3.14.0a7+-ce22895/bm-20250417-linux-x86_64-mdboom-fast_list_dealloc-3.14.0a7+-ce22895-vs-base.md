# Results vs. base

- fork: mdboom
- ref: fast_list_dealloc
- machine: linux-x86_64
- commit hash: ce22895
- commit date: 2025-04-17
- overall geometric mean: 1.001x slower
- HPT reliability: 61.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 255 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_generators           | 396 ms                                                                 | 388 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 475 ms: 1.01x faster                                                |
| coroutines                 | 23.8 ms                                                                | 23.6 ms: 1.01x faster                                               |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (8): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 194 ms                                                                 | 187 ms: 1.04x faster                                                |
| nbody          | 94.0 ms                                                                | 95.8 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                 | 124 ms: 1.00x faster                                                |
| regex_v8       | 23.0 ms                                                                | 23.1 ms: 1.01x slower                                               |
| regex_effbot   | 3.06 ms                                                                | 3.09 ms: 1.01x slower                                               |
| regex_dna      | 200 ms                                                                 | 206 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process  | 59.4 ms                                                                | 58.2 ms: 1.02x faster                                               |
| xml_etree_generate | 84.9 ms                                                                | 83.8 ms: 1.01x faster                                               |
| pickle_pure_python | 314 us                                                                 | 311 us: 1.01x faster                                                |
| json_loads         | 29.8 us                                                                | 30.0 us: 1.01x slower                                               |
| json_dumps         | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                               |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site | 8.19 ms                                                                | 8.23 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 20.9 ms                                                                | 20.8 ms: 1.01x faster                                               |
| django_template | 31.6 ms                                                                | 31.4 ms: 1.01x faster                                               |
| mako            | 11.0 ms                                                                | 11.5 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| logging_silent             | 98.4 ns                                                                | 94.2 ns: 1.04x faster                                               |
| pyflate                    | 444 ms                                                                 | 425 ms: 1.04x faster                                                |
| pidigits                   | 194 ms                                                                 | 187 ms: 1.04x faster                                                |
| hexiom                     | 6.29 ms                                                                | 6.13 ms: 1.03x faster                                               |
| async_generators           | 396 ms                                                                 | 388 ms: 1.02x faster                                                |
| xml_etree_process          | 59.4 ms                                                                | 58.2 ms: 1.02x faster                                               |
| generators                 | 29.8 ms                                                                | 29.3 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                                               | 1.46 sec: 1.01x faster                                              |
| meteor_contest             | 106 ms                                                                 | 104 ms: 1.01x faster                                                |
| fannkuch                   | 412 ms                                                                 | 406 ms: 1.01x faster                                                |
| xml_etree_generate         | 84.9 ms                                                                | 83.8 ms: 1.01x faster                                               |
| go                         | 111 ms                                                                 | 110 ms: 1.01x faster                                                |
| logging_simple             | 5.54 us                                                                | 5.48 us: 1.01x faster                                               |
| pickle_pure_python         | 314 us                                                                 | 311 us: 1.01x faster                                                |
| comprehensions             | 16.6 us                                                                | 16.5 us: 1.01x faster                                               |
| mdp                        | 1.21 sec                                                               | 1.20 sec: 1.01x faster                                              |
| sqlite_synth               | 2.82 us                                                                | 2.80 us: 1.01x faster                                               |
| pprint_safe_repr           | 721 ms                                                                 | 716 ms: 1.01x faster                                                |
| genshi_text                | 20.9 ms                                                                | 20.8 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 475 ms: 1.01x faster                                                |
| deltablue                  | 3.34 ms                                                                | 3.31 ms: 1.01x faster                                               |
| coroutines                 | 23.8 ms                                                                | 23.6 ms: 1.01x faster                                               |
| django_template            | 31.6 ms                                                                | 31.4 ms: 1.01x faster                                               |
| sqlglot_v2_transpile       | 1.54 ms                                                                | 1.53 ms: 1.01x faster                                               |
| create_gc_cycles           | 2.48 ms                                                                | 2.47 ms: 1.00x faster                                               |
| sqlalchemy_declarative     | 132 ms                                                                 | 132 ms: 1.00x faster                                                |
| regex_compile              | 125 ms                                                                 | 124 ms: 1.00x faster                                                |
| sqlglot_v2_optimize        | 52.0 ms                                                                | 51.9 ms: 1.00x faster                                               |
| sympy_integrate            | 19.0 ms                                                                | 19.0 ms: 1.00x slower                                               |
| sympy_str                  | 265 ms                                                                 | 266 ms: 1.00x slower                                                |
| sympy_expand               | 451 ms                                                                 | 453 ms: 1.00x slower                                                |
| python_startup             | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site     | 8.19 ms                                                                | 8.23 ms: 1.01x slower                                               |
| bench_thread_pool          | 883 us                                                                 | 888 us: 1.01x slower                                                |
| regex_v8                   | 23.0 ms                                                                | 23.1 ms: 1.01x slower                                               |
| json_loads                 | 29.8 us                                                                | 30.0 us: 1.01x slower                                               |
| scimark_monte_carlo        | 65.8 ms                                                                | 66.3 ms: 1.01x slower                                               |
| chaos                      | 56.6 ms                                                                | 57.0 ms: 1.01x slower                                               |
| sympy_sum                  | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| json_dumps                 | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                               |
| pathlib                    | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                               |
| scimark_fft                | 354 ms                                                                 | 358 ms: 1.01x slower                                                |
| sqlalchemy_imperative      | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                               |
| json                       | 5.33 ms                                                                | 5.38 ms: 1.01x slower                                               |
| bench_mp_pool              | 81.3 ms                                                                | 82.1 ms: 1.01x slower                                               |
| regex_effbot               | 3.06 ms                                                                | 3.09 ms: 1.01x slower                                               |
| pycparser                  | 1.11 sec                                                               | 1.12 sec: 1.01x slower                                              |
| deepcopy_reduce            | 2.65 us                                                                | 2.69 us: 1.02x slower                                               |
| typing_runtime_protocols   | 163 us                                                                 | 165 us: 1.02x slower                                                |
| nbody                      | 94.0 ms                                                                | 95.8 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                                 | 267 ms: 1.02x slower                                                |
| 2to3                       | 249 ms                                                                 | 255 ms: 1.02x slower                                                |
| regex_dna                  | 200 ms                                                                 | 206 ms: 1.03x slower                                                |
| spectral_norm              | 103 ms                                                                 | 106 ms: 1.03x slower                                                |
| gc_traversal               | 4.62 ms                                                                | 4.80 ms: 1.04x slower                                               |
| mako                       | 11.0 ms                                                                | 11.5 ms: 1.04x slower                                               |
| scimark_sparse_mat_mult    | 4.65 ms                                                                | 5.01 ms: 1.08x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (38): async_tree_io, async_tree_none_tg, deepcopy_memo, shortest_path, async_tree_cpu_io_mixed, pylint, async_tree_none, nqueens, async_tree_memoization, async_tree_io_tg, richards, async_tree_memoization_tg, telco, richards_super, sqlglot_v2_normalize, float, xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, scimark_sor, crypto_pyaes, deepcopy, tomli_loads, html5lib, sqlglot_v2_parse, dulwich_log, asyncio_websockets, many_optionals, sphinx, genshi_xml, bpe_tokeniser, docutils, subparsers, logging_format, scimark_lu, connected_components, k_core, coverage

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 61.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x