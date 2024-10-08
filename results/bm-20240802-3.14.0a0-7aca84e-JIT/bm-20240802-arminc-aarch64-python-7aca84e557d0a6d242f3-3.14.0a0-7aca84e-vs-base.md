# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.00x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 372 ms                                                                  | 367 ms: 1.01x faster                                                    |
| docutils       | 3.73 sec                                                                | 3.67 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 708 ms                                                                  | 696 ms: 1.02x faster                                                    |
| asyncio_tcp                | 622 ms                                                                  | 641 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_memoization, async_generators, asyncio_tcp_ssl, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 258 ms                                                                  | 251 ms: 1.03x faster                                                    |
| regex_effbot   | 4.92 ms                                                                 | 4.88 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads    | 2.65 sec                                                                | 2.63 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (8): unpickle_pure_python, json_loads, json_dumps, pickle_pure_python, xml_etree_process, xml_etree_generate, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.86 ms                                                                 | 8.83 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 74.4 ms                                                                 | 72.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool              | 8.57 ms                                                                 | 8.23 ms: 1.04x faster                                                   |
| regex_dna                  | 258 ms                                                                  | 251 ms: 1.03x faster                                                    |
| deepcopy                   | 386 us                                                                  | 376 us: 1.03x faster                                                    |
| genshi_xml                 | 74.4 ms                                                                 | 72.7 ms: 1.02x faster                                                   |
| logging_silent             | 137 ns                                                                  | 134 ns: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 708 ms                                                                  | 696 ms: 1.02x faster                                                    |
| docutils                   | 3.73 sec                                                                | 3.67 sec: 1.02x faster                                                  |
| bench_thread_pool          | 1.32 ms                                                                 | 1.30 ms: 1.02x faster                                                   |
| fannkuch                   | 488 ms                                                                  | 481 ms: 1.02x faster                                                    |
| scimark_sor                | 155 ms                                                                  | 152 ms: 1.02x faster                                                    |
| deltablue                  | 4.51 ms                                                                 | 4.44 ms: 1.01x faster                                                   |
| 2to3                       | 372 ms                                                                  | 367 ms: 1.01x faster                                                    |
| sqlglot_parse              | 1.67 ms                                                                 | 1.65 ms: 1.01x faster                                                   |
| hexiom                     | 9.36 ms                                                                 | 9.24 ms: 1.01x faster                                                   |
| spectral_norm              | 145 ms                                                                  | 144 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.91 sec                                                                | 5.84 sec: 1.01x faster                                                  |
| regex_effbot               | 4.92 ms                                                                 | 4.88 ms: 1.01x faster                                                   |
| tomli_loads                | 2.65 sec                                                                | 2.63 sec: 1.01x faster                                                  |
| richards                   | 55.3 ms                                                                 | 54.9 ms: 1.01x faster                                                   |
| mdp                        | 3.50 sec                                                                | 3.47 sec: 1.01x faster                                                  |
| python_startup_no_site     | 8.86 ms                                                                 | 8.83 ms: 1.00x faster                                                   |
| generators                 | 57.0 ms                                                                 | 57.3 ms: 1.00x slower                                                   |
| meteor_contest             | 119 ms                                                                  | 120 ms: 1.01x slower                                                    |
| nqueens                    | 121 ms                                                                  | 123 ms: 1.01x slower                                                    |
| typing_runtime_protocols   | 210 us                                                                  | 213 us: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 6.79 ms                                                                 | 6.90 ms: 1.02x slower                                                   |
| telco                      | 10.1 ms                                                                 | 10.3 ms: 1.02x slower                                                   |
| deepcopy_reduce            | 4.15 us                                                                 | 4.22 us: 1.02x slower                                                   |
| pathlib                    | 21.7 ms                                                                 | 22.2 ms: 1.02x slower                                                   |
| asyncio_tcp                | 622 ms                                                                  | 641 ms: 1.03x slower                                                    |
| scimark_fft                | 461 ms                                                                  | 476 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (59): sqlglot_normalize, coverage, async_tree_none_tg, unpickle_pure_python, logging_format, pylint, json, sqlglot_transpile, richards_super, deepcopy_memo, async_tree_memoization, logging_simple, pprint_safe_repr, regex_compile, genshi_text, sympy_expand, pidigits, dask, sympy_sum, async_generators, scimark_lu, scimark_monte_carlo, nbody, python_startup, pycparser, asyncio_tcp_ssl, json_loads, comprehensions, json_dumps, pickle_pure_python, float, pprint_pformat, xml_etree_process, chaos, raytrace, async_tree_none, mako, sympy_integrate, pyflate, html5lib, asyncio_websockets, async_tree_cpu_io_mixed, django_template, crypto_pyaes, thrift, async_tree_memoization_tg, go, regex_v8, sqlglot_optimize, async_tree_io_tg, create_gc_cycles, xml_etree_generate, gc_traversal, async_tree_io, sympy_str, coroutines, xml_etree_parse, tornado_http, xml_etree_iterparse

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x