# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: f5dec96
- commit date: 2024-12-06
- overall geometric mean: 1.003x slower
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.00x slower                                                      |
| docutils       | 2.57 sec                                                               | 2.61 sec: 1.02x slower                                                    |
| html5lib       | 63.6 ms                                                                | 63.0 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 495 ms                                                                 | 489 ms: 1.01x faster                                                      |
| async_tree_io              | 609 ms                                                                 | 605 ms: 1.01x faster                                                      |
| async_tree_memoization     | 340 ms                                                                 | 347 ms: 1.02x slower                                                      |
| coroutines                 | 23.7 ms                                                                | 24.4 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_none, async_generators, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                | 78.8 ms: 1.01x faster                                                     |
| pidigits       | 187 ms                                                                 | 189 ms: 1.01x slower                                                      |
| nbody          | 93.2 ms                                                                | 97.1 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.43 ms                                                                | 3.35 ms: 1.03x faster                                                     |
| regex_dna      | 223 ms                                                                 | 219 ms: 1.02x faster                                                      |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                                      |
| regex_v8       | 25.5 ms                                                                | 26.4 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process  | 59.4 ms                                                                | 58.6 ms: 1.01x faster                                                     |
| json_loads         | 26.4 us                                                                | 26.2 us: 1.01x faster                                                     |
| xml_etree_generate | 85.4 ms                                                                | 84.7 ms: 1.01x faster                                                     |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (6): unpickle_pure_python, json_dumps, tomli_loads, pickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 7.09 ms: 1.00x slower                                                     |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 22.8 ms                                                                | 22.1 ms: 1.03x faster                                                     |
| genshi_xml     | 50.3 ms                                                                | 49.6 ms: 1.01x faster                                                     |
| mako           | 11.6 ms                                                                | 11.8 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| logging_silent             | 107 ns                                                                 | 97.5 ns: 1.10x faster                                                     |
| gc_traversal               | 4.87 ms                                                                | 4.57 ms: 1.07x faster                                                     |
| genshi_text                | 22.8 ms                                                                | 22.1 ms: 1.03x faster                                                     |
| scimark_lu                 | 116 ms                                                                 | 113 ms: 1.03x faster                                                      |
| regex_effbot               | 3.43 ms                                                                | 3.35 ms: 1.03x faster                                                     |
| coverage                   | 85.3 ms                                                                | 83.2 ms: 1.02x faster                                                     |
| raytrace                   | 274 ms                                                                 | 267 ms: 1.02x faster                                                      |
| deepcopy_memo              | 30.6 us                                                                | 30.0 us: 1.02x faster                                                     |
| regex_dna                  | 223 ms                                                                 | 219 ms: 1.02x faster                                                      |
| connected_components       | 444 ms                                                                 | 436 ms: 1.02x faster                                                      |
| go                         | 119 ms                                                                 | 117 ms: 1.02x faster                                                      |
| hexiom                     | 6.29 ms                                                                | 6.19 ms: 1.02x faster                                                     |
| xml_etree_process          | 59.4 ms                                                                | 58.6 ms: 1.01x faster                                                     |
| sqlite_synth               | 2.90 us                                                                | 2.86 us: 1.01x faster                                                     |
| genshi_xml                 | 50.3 ms                                                                | 49.6 ms: 1.01x faster                                                     |
| json                       | 4.90 ms                                                                | 4.83 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 495 ms                                                                 | 489 ms: 1.01x faster                                                      |
| regex_compile              | 128 ms                                                                 | 127 ms: 1.01x faster                                                      |
| create_gc_cycles           | 2.29 ms                                                                | 2.27 ms: 1.01x faster                                                     |
| deltablue                  | 3.28 ms                                                                | 3.25 ms: 1.01x faster                                                     |
| html5lib                   | 63.6 ms                                                                | 63.0 ms: 1.01x faster                                                     |
| sqlglot_parse              | 1.30 ms                                                                | 1.28 ms: 1.01x faster                                                     |
| sqlglot_transpile          | 1.61 ms                                                                | 1.59 ms: 1.01x faster                                                     |
| shortest_path              | 483 ms                                                                 | 479 ms: 1.01x faster                                                      |
| json_loads                 | 26.4 us                                                                | 26.2 us: 1.01x faster                                                     |
| xml_etree_generate         | 85.4 ms                                                                | 84.7 ms: 1.01x faster                                                     |
| float                      | 79.4 ms                                                                | 78.8 ms: 1.01x faster                                                     |
| richards_super             | 52.2 ms                                                                | 51.9 ms: 1.01x faster                                                     |
| async_tree_io              | 609 ms                                                                 | 605 ms: 1.01x faster                                                      |
| richards                   | 45.9 ms                                                                | 45.7 ms: 1.01x faster                                                     |
| crypto_pyaes               | 73.1 ms                                                                | 72.8 ms: 1.00x faster                                                     |
| scimark_fft                | 366 ms                                                                 | 367 ms: 1.00x slower                                                      |
| bench_thread_pool          | 853 us                                                                 | 855 us: 1.00x slower                                                      |
| python_startup_no_site     | 7.07 ms                                                                | 7.09 ms: 1.00x slower                                                     |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.00x slower                                                      |
| deepcopy                   | 262 us                                                                 | 263 us: 1.01x slower                                                      |
| bpe_tokeniser              | 4.54 sec                                                               | 4.57 sec: 1.01x slower                                                    |
| sympy_str                  | 270 ms                                                                 | 271 ms: 1.01x slower                                                      |
| sympy_sum                  | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| sympy_integrate            | 19.9 ms                                                                | 20.0 ms: 1.01x slower                                                     |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                     |
| chaos                      | 60.9 ms                                                                | 61.4 ms: 1.01x slower                                                     |
| bench_mp_pool              | 78.5 ms                                                                | 79.1 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 107 ms                                                                 | 108 ms: 1.01x slower                                                      |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                                      |
| many_optionals             | 950 us                                                                 | 959 us: 1.01x slower                                                      |
| pidigits                   | 187 ms                                                                 | 189 ms: 1.01x slower                                                      |
| sqlalchemy_imperative      | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                                     |
| spectral_norm              | 115 ms                                                                 | 117 ms: 1.01x slower                                                      |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.02x slower                                                     |
| sqlalchemy_declarative     | 127 ms                                                                 | 129 ms: 1.02x slower                                                      |
| docutils                   | 2.57 sec                                                               | 2.61 sec: 1.02x slower                                                    |
| pyflate                    | 469 ms                                                                 | 476 ms: 1.02x slower                                                      |
| generators                 | 28.6 ms                                                                | 29.1 ms: 1.02x slower                                                     |
| mdp                        | 2.57 sec                                                               | 2.62 sec: 1.02x slower                                                    |
| logging_format             | 6.13 us                                                                | 6.25 us: 1.02x slower                                                     |
| pprint_safe_repr           | 739 ms                                                                 | 755 ms: 1.02x slower                                                      |
| async_tree_memoization     | 340 ms                                                                 | 347 ms: 1.02x slower                                                      |
| mako                       | 11.6 ms                                                                | 11.8 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.51 sec                                                               | 1.54 sec: 1.02x slower                                                    |
| logging_simple             | 5.58 us                                                                | 5.71 us: 1.02x slower                                                     |
| thrift                     | 766 us                                                                 | 785 us: 1.02x slower                                                      |
| deepcopy_reduce            | 2.71 us                                                                | 2.79 us: 1.03x slower                                                     |
| coroutines                 | 23.7 ms                                                                | 24.4 ms: 1.03x slower                                                     |
| pycparser                  | 1.12 sec                                                               | 1.15 sec: 1.03x slower                                                    |
| regex_v8                   | 25.5 ms                                                                | 26.4 ms: 1.03x slower                                                     |
| scimark_sor                | 127 ms                                                                 | 132 ms: 1.04x slower                                                      |
| nbody                      | 93.2 ms                                                                | 97.1 ms: 1.04x slower                                                     |
| fannkuch                   | 401 ms                                                                 | 423 ms: 1.06x slower                                                      |
| nqueens                    | 80.6 ms                                                                | 85.6 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 4.85 ms                                                                | 5.19 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (26): telco, async_tree_none_tg, typing_runtime_protocols, unpickle_pure_python, scimark_monte_carlo, json_dumps, async_tree_memoization_tg, tomli_loads, pickle_pure_python, sqlglot_optimize, xml_etree_parse, sympy_expand, comprehensions, asyncio_websockets, subparsers, async_tree_none, async_generators, django_template, dulwich_log, async_tree_cpu_io_mixed, xml_etree_iterparse, async_tree_io_tg, pylint, k_core, sphinx, djangocms

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x