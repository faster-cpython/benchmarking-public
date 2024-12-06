# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 0c20416
- commit date: 2024-12-06
- overall geometric mean: 1.008x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 256 ms: 1.01x slower                                                      |
| docutils       | 2.57 sec                                                               | 2.61 sec: 1.02x slower                                                    |
| html5lib       | 63.6 ms                                                                | 65.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 495 ms                                                                 | 487 ms: 1.02x faster                                                      |
| async_tree_none_tg         | 267 ms                                                                 | 263 ms: 1.02x faster                                                      |
| async_tree_io              | 609 ms                                                                 | 605 ms: 1.01x faster                                                      |
| async_tree_memoization     | 340 ms                                                                 | 346 ms: 1.02x slower                                                      |
| coroutines                 | 23.7 ms                                                                | 24.5 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (6): async_tree_io_tg, async_generators, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                | 78.4 ms: 1.01x faster                                                     |
| pidigits       | 187 ms                                                                 | 189 ms: 1.01x slower                                                      |
| nbody          | 93.2 ms                                                                | 98.4 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                 | 222 ms: 1.00x faster                                                      |
| regex_v8       | 25.5 ms                                                                | 25.5 ms: 1.00x faster                                                     |
| regex_compile  | 128 ms                                                                 | 130 ms: 1.01x slower                                                      |
| regex_effbot   | 3.43 ms                                                                | 3.50 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads          | 26.4 us                                                                | 26.0 us: 1.01x faster                                                     |
| xml_etree_process   | 59.4 ms                                                                | 58.7 ms: 1.01x faster                                                     |
| xml_etree_parse     | 145 ms                                                                 | 143 ms: 1.01x faster                                                      |
| xml_etree_generate  | 85.4 ms                                                                | 84.5 ms: 1.01x faster                                                     |
| xml_etree_iterparse | 98.8 ms                                                                | 99.4 ms: 1.01x slower                                                     |
| json_dumps          | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                     |
| pickle_pure_python  | 327 us                                                                 | 331 us: 1.01x slower                                                      |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 7.03 ms: 1.01x faster                                                     |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.8 ms                                                                | 22.5 ms: 1.01x faster                                                     |
| django_template | 31.8 ms                                                                | 32.0 ms: 1.01x slower                                                     |
| genshi_xml      | 50.3 ms                                                                | 50.7 ms: 1.01x slower                                                     |
| mako            | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2+-023b7d2 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| logging_silent             | 107 ns                                                                 | 101 ns: 1.06x faster                                                      |
| gc_traversal               | 4.87 ms                                                                | 4.61 ms: 1.06x faster                                                     |
| create_gc_cycles           | 2.29 ms                                                                | 2.24 ms: 1.03x faster                                                     |
| json                       | 4.90 ms                                                                | 4.81 ms: 1.02x faster                                                     |
| typing_runtime_protocols   | 167 us                                                                 | 164 us: 1.02x faster                                                      |
| raytrace                   | 274 ms                                                                 | 269 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 495 ms                                                                 | 487 ms: 1.02x faster                                                      |
| async_tree_none_tg         | 267 ms                                                                 | 263 ms: 1.02x faster                                                      |
| coverage                   | 85.3 ms                                                                | 84.0 ms: 1.02x faster                                                     |
| float                      | 79.4 ms                                                                | 78.4 ms: 1.01x faster                                                     |
| json_loads                 | 26.4 us                                                                | 26.0 us: 1.01x faster                                                     |
| xml_etree_process          | 59.4 ms                                                                | 58.7 ms: 1.01x faster                                                     |
| genshi_text                | 22.8 ms                                                                | 22.5 ms: 1.01x faster                                                     |
| xml_etree_parse            | 145 ms                                                                 | 143 ms: 1.01x faster                                                      |
| xml_etree_generate         | 85.4 ms                                                                | 84.5 ms: 1.01x faster                                                     |
| richards                   | 45.9 ms                                                                | 45.6 ms: 1.01x faster                                                     |
| richards_super             | 52.2 ms                                                                | 51.8 ms: 1.01x faster                                                     |
| scimark_lu                 | 116 ms                                                                 | 115 ms: 1.01x faster                                                      |
| async_tree_io              | 609 ms                                                                 | 605 ms: 1.01x faster                                                      |
| python_startup_no_site     | 7.07 ms                                                                | 7.03 ms: 1.01x faster                                                     |
| go                         | 119 ms                                                                 | 118 ms: 1.01x faster                                                      |
| pycparser                  | 1.12 sec                                                               | 1.11 sec: 1.01x faster                                                    |
| regex_dna                  | 223 ms                                                                 | 222 ms: 1.00x faster                                                      |
| regex_v8                   | 25.5 ms                                                                | 25.5 ms: 1.00x faster                                                     |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                     |
| bench_thread_pool          | 853 us                                                                 | 857 us: 1.00x slower                                                      |
| django_template            | 31.8 ms                                                                | 32.0 ms: 1.01x slower                                                     |
| bpe_tokeniser              | 4.54 sec                                                               | 4.56 sec: 1.01x slower                                                    |
| xml_etree_iterparse        | 98.8 ms                                                                | 99.4 ms: 1.01x slower                                                     |
| dulwich_log                | 64.9 ms                                                                | 65.3 ms: 1.01x slower                                                     |
| many_optionals             | 950 us                                                                 | 956 us: 1.01x slower                                                      |
| sympy_integrate            | 19.9 ms                                                                | 20.0 ms: 1.01x slower                                                     |
| subparsers                 | 20.8 ms                                                                | 21.0 ms: 1.01x slower                                                     |
| 2to3                       | 254 ms                                                                 | 256 ms: 1.01x slower                                                      |
| sympy_expand               | 458 ms                                                                 | 462 ms: 1.01x slower                                                      |
| comprehensions             | 17.1 us                                                                | 17.3 us: 1.01x slower                                                     |
| generators                 | 28.6 ms                                                                | 28.8 ms: 1.01x slower                                                     |
| genshi_xml                 | 50.3 ms                                                                | 50.7 ms: 1.01x slower                                                     |
| json_dumps                 | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                                     |
| mako                       | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                     |
| sympy_str                  | 270 ms                                                                 | 272 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 53.7 ms                                                                | 54.2 ms: 1.01x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                                     |
| regex_compile              | 128 ms                                                                 | 130 ms: 1.01x slower                                                      |
| hexiom                     | 6.29 ms                                                                | 6.36 ms: 1.01x slower                                                     |
| scimark_monte_carlo        | 68.9 ms                                                                | 69.8 ms: 1.01x slower                                                     |
| crypto_pyaes               | 73.1 ms                                                                | 74.0 ms: 1.01x slower                                                     |
| pickle_pure_python         | 327 us                                                                 | 331 us: 1.01x slower                                                      |
| sympy_sum                  | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.61 ms                                                                | 1.63 ms: 1.01x slower                                                     |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.30 ms                                                                | 1.31 ms: 1.01x slower                                                     |
| pidigits                   | 187 ms                                                                 | 189 ms: 1.01x slower                                                      |
| logging_simple             | 5.58 us                                                                | 5.65 us: 1.01x slower                                                     |
| thrift                     | 766 us                                                                 | 778 us: 1.02x slower                                                      |
| docutils                   | 2.57 sec                                                               | 2.61 sec: 1.02x slower                                                    |
| sqlglot_normalize          | 107 ms                                                                 | 109 ms: 1.02x slower                                                      |
| regex_effbot               | 3.43 ms                                                                | 3.50 ms: 1.02x slower                                                     |
| async_tree_memoization     | 340 ms                                                                 | 346 ms: 1.02x slower                                                      |
| sqlalchemy_declarative     | 127 ms                                                                 | 130 ms: 1.02x slower                                                      |
| meteor_contest             | 107 ms                                                                 | 109 ms: 1.02x slower                                                      |
| connected_components       | 444 ms                                                                 | 453 ms: 1.02x slower                                                      |
| chaos                      | 60.9 ms                                                                | 62.4 ms: 1.02x slower                                                     |
| deepcopy                   | 262 us                                                                 | 268 us: 1.02x slower                                                      |
| logging_format             | 6.13 us                                                                | 6.27 us: 1.02x slower                                                     |
| html5lib                   | 63.6 ms                                                                | 65.2 ms: 1.02x slower                                                     |
| spectral_norm              | 115 ms                                                                 | 118 ms: 1.03x slower                                                      |
| shortest_path              | 483 ms                                                                 | 496 ms: 1.03x slower                                                      |
| coroutines                 | 23.7 ms                                                                | 24.5 ms: 1.03x slower                                                     |
| deepcopy_reduce            | 2.71 us                                                                | 2.81 us: 1.03x slower                                                     |
| scimark_fft                | 366 ms                                                                 | 379 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 739 ms                                                                 | 769 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.51 sec                                                               | 1.57 sec: 1.04x slower                                                    |
| pyflate                    | 469 ms                                                                 | 492 ms: 1.05x slower                                                      |
| nqueens                    | 80.6 ms                                                                | 84.9 ms: 1.05x slower                                                     |
| nbody                      | 93.2 ms                                                                | 98.4 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 4.85 ms                                                                | 5.13 ms: 1.06x slower                                                     |
| mdp                        | 2.57 sec                                                               | 2.72 sec: 1.06x slower                                                    |
| fannkuch                   | 401 ms                                                                 | 429 ms: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (18): tomli_loads, scimark_sor, telco, deltablue, async_tree_io_tg, async_generators, async_tree_none, async_tree_memoization_tg, unpickle_pure_python, sqlite_synth, deepcopy_memo, async_tree_cpu_io_mixed, asyncio_websockets, djangocms, bench_mp_pool, pylint, sphinx, k_core

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x