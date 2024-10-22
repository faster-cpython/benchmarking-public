# Results vs. base

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 799510c
- commit date: 2024-07-10
- overall geometric mean: 1.06x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 271 ms: 1.00x faster                                            |
| docutils       | 2.88 sec                                                              | 6.74 sec: 2.34x slower                                          |
| html5lib       | 65.4 ms                                                               | 77.0 ms: 1.18x slower                                           |
| tornado_http   | 93.8 ms                                                               | 97.9 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                                 | 1.30x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 545 ms                                                                | 552 ms: 1.01x slower                                            |
| async_tree_io              | 842 ms                                                                | 896 ms: 1.06x slower                                            |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                    |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 79.5 ms                                                               | 77.4 ms: 1.03x faster                                           |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                            |
| float          | 70.4 ms                                                               | 70.9 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                | 130 ms: 1.04x faster                                            |
| regex_dna      | 227 ms                                                                | 223 ms: 1.02x faster                                            |
| regex_v8       | 25.5 ms                                                               | 25.6 ms: 1.01x slower                                           |
| regex_effbot   | 3.84 ms                                                               | 3.88 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps          | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                           |
| tomli_loads         | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                          |
| xml_etree_process   | 57.5 ms                                                               | 58.1 ms: 1.01x slower                                           |
| pickle_pure_python  | 296 us                                                                | 303 us: 1.03x slower                                            |
| xml_etree_iterparse | 99.0 ms                                                               | 102 ms: 1.03x slower                                            |
| xml_etree_generate  | 81.1 ms                                                               | 84.8 ms: 1.05x slower                                           |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.12 ms: 1.00x slower                                           |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.77 ms                                                               | 9.87 ms: 1.01x slower                                           |
| genshi_text     | 25.1 ms                                                               | 27.0 ms: 1.08x slower                                           |
| genshi_xml      | 56.9 ms                                                               | 62.2 ms: 1.09x slower                                           |
| django_template | 36.1 ms                                                               | 40.3 ms: 1.12x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.07x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| richards                   | 41.5 ms                                                               | 38.5 ms: 1.08x faster                                           |
| richards_super             | 47.7 ms                                                               | 44.6 ms: 1.07x faster                                           |
| logging_silent             | 108 ns                                                                | 102 ns: 1.06x faster                                            |
| deepcopy                   | 274 us                                                                | 261 us: 1.05x faster                                            |
| deltablue                  | 3.58 ms                                                               | 3.43 ms: 1.04x faster                                           |
| deepcopy_memo              | 28.4 us                                                               | 27.2 us: 1.04x faster                                           |
| deepcopy_reduce            | 2.76 us                                                               | 2.64 us: 1.04x faster                                           |
| go                         | 146 ms                                                                | 140 ms: 1.04x faster                                            |
| regex_compile              | 135 ms                                                                | 130 ms: 1.04x faster                                            |
| scimark_lu                 | 126 ms                                                                | 121 ms: 1.04x faster                                            |
| dulwich_log                | 68.0 ms                                                               | 65.4 ms: 1.04x faster                                           |
| scimark_sor                | 131 ms                                                                | 126 ms: 1.04x faster                                            |
| spectral_norm              | 101 ms                                                                | 98.0 ms: 1.03x faster                                           |
| chaos                      | 57.8 ms                                                               | 56.0 ms: 1.03x faster                                           |
| nbody                      | 79.5 ms                                                               | 77.4 ms: 1.03x faster                                           |
| typing_runtime_protocols   | 171 us                                                                | 167 us: 1.02x faster                                            |
| pycparser                  | 1.19 sec                                                              | 1.16 sec: 1.02x faster                                          |
| regex_dna                  | 227 ms                                                                | 223 ms: 1.02x faster                                            |
| json                       | 5.15 ms                                                               | 5.08 ms: 1.01x faster                                           |
| logging_simple             | 5.61 us                                                               | 5.54 us: 1.01x faster                                           |
| bpe_tokeniser              | 4.82 sec                                                              | 4.76 sec: 1.01x faster                                          |
| comprehensions             | 16.7 us                                                               | 16.6 us: 1.01x faster                                           |
| create_gc_cycles           | 1.77 ms                                                               | 1.75 ms: 1.01x faster                                           |
| meteor_contest             | 108 ms                                                                | 107 ms: 1.01x faster                                            |
| logging_format             | 6.16 us                                                               | 6.11 us: 1.01x faster                                           |
| hexiom                     | 6.56 ms                                                               | 6.52 ms: 1.01x faster                                           |
| crypto_pyaes               | 67.0 ms                                                               | 66.6 ms: 1.01x faster                                           |
| mdp                        | 2.71 sec                                                              | 2.70 sec: 1.00x faster                                          |
| 2to3                       | 272 ms                                                                | 271 ms: 1.00x faster                                            |
| python_startup_no_site     | 7.11 ms                                                               | 7.12 ms: 1.00x slower                                           |
| pidigits                   | 185 ms                                                                | 186 ms: 1.00x slower                                            |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                           |
| regex_v8                   | 25.5 ms                                                               | 25.6 ms: 1.01x slower                                           |
| coverage                   | 92.7 ms                                                               | 93.3 ms: 1.01x slower                                           |
| sqlglot_normalize          | 113 ms                                                                | 114 ms: 1.01x slower                                            |
| float                      | 70.4 ms                                                               | 70.9 ms: 1.01x slower                                           |
| json_dumps                 | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                           |
| tomli_loads                | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                          |
| pathlib                    | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                           |
| thrift                     | 799 us                                                                | 806 us: 1.01x slower                                            |
| mako                       | 9.77 ms                                                               | 9.87 ms: 1.01x slower                                           |
| regex_effbot               | 3.84 ms                                                               | 3.88 ms: 1.01x slower                                           |
| async_tree_cpu_io_mixed_tg | 545 ms                                                                | 552 ms: 1.01x slower                                            |
| xml_etree_process          | 57.5 ms                                                               | 58.1 ms: 1.01x slower                                           |
| asyncio_tcp                | 504 ms                                                                | 516 ms: 1.02x slower                                            |
| bench_thread_pool          | 833 us                                                                | 853 us: 1.02x slower                                            |
| pickle_pure_python         | 296 us                                                                | 303 us: 1.03x slower                                            |
| sympy_str                  | 293 ms                                                                | 302 ms: 1.03x slower                                            |
| sqlglot_transpile          | 1.60 ms                                                               | 1.65 ms: 1.03x slower                                           |
| xml_etree_iterparse        | 99.0 ms                                                               | 102 ms: 1.03x slower                                            |
| scimark_fft                | 305 ms                                                                | 316 ms: 1.03x slower                                            |
| fannkuch                   | 364 ms                                                                | 377 ms: 1.04x slower                                            |
| pyflate                    | 446 ms                                                                | 463 ms: 1.04x slower                                            |
| gc_traversal               | 3.64 ms                                                               | 3.80 ms: 1.04x slower                                           |
| tornado_http               | 93.8 ms                                                               | 97.9 ms: 1.04x slower                                           |
| xml_etree_generate         | 81.1 ms                                                               | 84.8 ms: 1.05x slower                                           |
| scimark_monte_carlo        | 60.8 ms                                                               | 64.1 ms: 1.05x slower                                           |
| dask                       | 363 ms                                                                | 383 ms: 1.06x slower                                            |
| async_tree_io              | 842 ms                                                                | 896 ms: 1.06x slower                                            |
| scimark_sparse_mat_mult    | 4.37 ms                                                               | 4.67 ms: 1.07x slower                                           |
| genshi_text                | 25.1 ms                                                               | 27.0 ms: 1.08x slower                                           |
| sqlglot_optimize           | 55.7 ms                                                               | 60.0 ms: 1.08x slower                                           |
| nqueens                    | 86.2 ms                                                               | 94.1 ms: 1.09x slower                                           |
| genshi_xml                 | 56.9 ms                                                               | 62.2 ms: 1.09x slower                                           |
| django_template            | 36.1 ms                                                               | 40.3 ms: 1.12x slower                                           |
| async_generators           | 455 ms                                                                | 514 ms: 1.13x slower                                            |
| sympy_integrate            | 21.9 ms                                                               | 25.3 ms: 1.16x slower                                           |
| coroutines                 | 23.5 ms                                                               | 27.5 ms: 1.17x slower                                           |
| html5lib                   | 65.4 ms                                                               | 77.0 ms: 1.18x slower                                           |
| pylint                     | 336 ms                                                                | 425 ms: 1.26x slower                                            |
| generators                 | 29.8 ms                                                               | 47.6 ms: 1.60x slower                                           |
| docutils                   | 2.88 sec                                                              | 6.74 sec: 2.34x slower                                          |
| raytrace                   | 271 ms                                                                | 4.85 sec: 17.88x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                    |

Benchmark hidden because not significant (18): json_loads, asyncio_websockets, telco, xml_etree_parse, pprint_safe_repr, bench_mp_pool, asyncio_tcp_ssl, sympy_expand, pprint_pformat, unpickle_pure_python, sympy_sum, sqlglot_parse, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x