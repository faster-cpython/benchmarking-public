# Results vs. base

- fork: mdboom
- ref: pyfloat_fromdouble
- machine: linux-x86_64
- commit hash: 9487962
- commit date: 2025-05-30
- overall geometric mean: 1.002x slower
- HPT reliability: 83.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 255 ms: 1.00x slower                                                |
| docutils       | 2.57 sec                                                              | 2.57 sec: 1.00x slower                                              |
| html5lib       | 61.4 ms                                                               | 62.4 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 498 ms                                                                | 485 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed    | 506 ms                                                                | 494 ms: 1.02x faster                                                |
| coroutines                 | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                               |
| async_tree_memoization     | 315 ms                                                                | 313 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none_tg, asyncio_websockets, async_generators, async_tree_none, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 200 ms                                                                | 188 ms: 1.07x faster                                                |
| nbody          | 96.3 ms                                                               | 95.8 ms: 1.01x faster                                               |
| float          | 70.1 ms                                                               | 71.3 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                | 126 ms: 1.00x faster                                                |
| regex_v8       | 22.4 ms                                                               | 23.6 ms: 1.05x slower                                               |
| regex_effbot   | 3.13 ms                                                               | 3.40 ms: 1.08x slower                                               |
| regex_dna      | 195 ms                                                                | 222 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads          | 29.9 us                                                               | 29.3 us: 1.02x faster                                               |
| xml_etree_iterparse | 99.1 ms                                                               | 98.2 ms: 1.01x faster                                               |
| xml_etree_process   | 60.0 ms                                                               | 59.6 ms: 1.01x faster                                               |
| xml_etree_parse     | 142 ms                                                                | 141 ms: 1.01x faster                                                |
| tomli_loads         | 2.03 sec                                                              | 2.02 sec: 1.01x faster                                              |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_generate, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                               |
| python_startup_no_site | 6.92 ms                                                               | 6.95 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.5 ms                                                               | 11.4 ms: 1.01x faster                                               |
| genshi_xml      | 49.1 ms                                                               | 49.6 ms: 1.01x slower                                               |
| django_template | 32.6 ms                                                               | 33.0 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits                   | 200 ms                                                                | 188 ms: 1.07x faster                                                |
| coverage                   | 435 ms                                                                | 418 ms: 1.04x faster                                                |
| generators                 | 31.0 ms                                                               | 30.0 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 498 ms                                                                | 485 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed    | 506 ms                                                                | 494 ms: 1.02x faster                                                |
| scimark_fft                | 380 ms                                                                | 371 ms: 1.02x faster                                                |
| comprehensions             | 16.3 us                                                               | 15.9 us: 1.02x faster                                               |
| json_loads                 | 29.9 us                                                               | 29.3 us: 1.02x faster                                               |
| spectral_norm              | 108 ms                                                                | 106 ms: 1.02x faster                                                |
| mako                       | 11.5 ms                                                               | 11.4 ms: 1.01x faster                                               |
| logging_silent             | 475 ns                                                                | 470 ns: 1.01x faster                                                |
| xml_etree_iterparse        | 99.1 ms                                                               | 98.2 ms: 1.01x faster                                               |
| coroutines                 | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                               |
| go                         | 111 ms                                                                | 110 ms: 1.01x faster                                                |
| sympy_expand               | 454 ms                                                                | 451 ms: 1.01x faster                                                |
| xml_etree_process          | 60.0 ms                                                               | 59.6 ms: 1.01x faster                                               |
| bpe_tokeniser              | 4.54 sec                                                              | 4.51 sec: 1.01x faster                                              |
| scimark_sor                | 121 ms                                                                | 120 ms: 1.01x faster                                                |
| xml_etree_parse            | 142 ms                                                                | 141 ms: 1.01x faster                                                |
| sympy_sum                  | 148 ms                                                                | 147 ms: 1.01x faster                                                |
| async_tree_memoization     | 315 ms                                                                | 313 ms: 1.01x faster                                                |
| tomli_loads                | 2.03 sec                                                              | 2.02 sec: 1.01x faster                                              |
| nbody                      | 96.3 ms                                                               | 95.8 ms: 1.01x faster                                               |
| raytrace                   | 270 ms                                                                | 268 ms: 1.01x faster                                                |
| sympy_integrate            | 18.9 ms                                                               | 18.8 ms: 1.00x faster                                               |
| sqlglot_v2_normalize       | 105 ms                                                                | 105 ms: 1.00x faster                                                |
| fannkuch                   | 410 ms                                                                | 409 ms: 1.00x faster                                                |
| sympy_str                  | 267 ms                                                                | 266 ms: 1.00x faster                                                |
| regex_compile              | 127 ms                                                                | 126 ms: 1.00x faster                                                |
| sqlglot_v2_optimize        | 51.9 ms                                                               | 51.7 ms: 1.00x faster                                               |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                               |
| docutils                   | 2.57 sec                                                              | 2.57 sec: 1.00x slower                                              |
| python_startup_no_site     | 6.92 ms                                                               | 6.95 ms: 1.00x slower                                               |
| dulwich_log                | 59.5 ms                                                               | 59.7 ms: 1.00x slower                                               |
| nqueens                    | 81.8 ms                                                               | 82.0 ms: 1.00x slower                                               |
| chaos                      | 61.0 ms                                                               | 61.2 ms: 1.00x slower                                               |
| 2to3                       | 254 ms                                                                | 255 ms: 1.00x slower                                                |
| scimark_lu                 | 116 ms                                                                | 116 ms: 1.01x slower                                                |
| deepcopy_memo              | 29.2 us                                                               | 29.3 us: 1.01x slower                                               |
| pprint_pformat             | 1.64 sec                                                              | 1.65 sec: 1.01x slower                                              |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.25 ms: 1.01x slower                                               |
| sqlglot_v2_transpile       | 1.54 ms                                                               | 1.55 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.56 ms                                                               | 2.58 ms: 1.01x slower                                               |
| subparsers                 | 23.4 ms                                                               | 23.6 ms: 1.01x slower                                               |
| genshi_xml                 | 49.1 ms                                                               | 49.6 ms: 1.01x slower                                               |
| django_template            | 32.6 ms                                                               | 33.0 ms: 1.01x slower                                               |
| logging_simple             | 6.12 us                                                               | 6.21 us: 1.01x slower                                               |
| typing_runtime_protocols   | 166 us                                                                | 169 us: 1.01x slower                                                |
| telco                      | 7.94 ms                                                               | 8.07 ms: 1.02x slower                                               |
| html5lib                   | 61.4 ms                                                               | 62.4 ms: 1.02x slower                                               |
| float                      | 70.1 ms                                                               | 71.3 ms: 1.02x slower                                               |
| pycparser                  | 1.10 sec                                                              | 1.12 sec: 1.02x slower                                              |
| scimark_sparse_mat_mult    | 5.10 ms                                                               | 5.20 ms: 1.02x slower                                               |
| logging_format             | 6.82 us                                                               | 6.97 us: 1.02x slower                                               |
| shortest_path              | 501 ms                                                                | 523 ms: 1.05x slower                                                |
| regex_v8                   | 22.4 ms                                                               | 23.6 ms: 1.05x slower                                               |
| gc_traversal               | 4.75 ms                                                               | 5.06 ms: 1.07x slower                                               |
| regex_effbot               | 3.13 ms                                                               | 3.40 ms: 1.08x slower                                               |
| regex_dna                  | 195 ms                                                                | 222 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (33): scimark_monte_carlo, connected_components, json, async_tree_io, pylint, pickle_pure_python, xml_etree_generate, richards, thrift, async_tree_none_tg, genshi_text, hexiom, json_dumps, asyncio_websockets, async_generators, meteor_contest, async_tree_none, sqlite_synth, deltablue, async_tree_memoization_tg, crypto_pyaes, mdp, richards_super, pyflate, k_core, deepcopy_reduce, many_optionals, unpickle_pure_python, sphinx, pathlib, deepcopy, pprint_safe_repr, async_tree_io_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 83.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x