# Results vs. base

- fork: faster-cpython
- ref: variable_sized_line_
- machine: linux-x86_64
- commit hash: 262abf1
- commit date: 2024-12-30
- overall geometric mean: 1.001x faster
- HPT reliability: 83.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 255 ms: 1.00x faster                                                             |
| docutils       | 2.59 sec                                                               | 2.60 sec: 1.00x slower                                                           |
| html5lib       | 63.0 ms                                                                | 62.6 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 423 ms                                                                 | 420 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 500 ms: 1.02x slower                                                             |
| coroutines                 | 23.1 ms                                                                | 23.7 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 483 ms: 1.03x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (7): async_tree_io_tg, asyncio_websockets, async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 94.4 ms                                                                | 93.2 ms: 1.01x faster                                                            |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.30 ms                                                                | 3.27 ms: 1.01x faster                                                            |
| regex_v8       | 25.3 ms                                                                | 25.4 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 26.8 us                                                                | 26.6 us: 1.01x faster                                                            |
| xml_etree_process    | 59.2 ms                                                                | 59.0 ms: 1.00x faster                                                            |
| unpickle_pure_python | 218 us                                                                 | 219 us: 1.00x slower                                                             |
| json_dumps           | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                            |
| tomli_loads          | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                                            |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 11.7 ms                                                                | 11.8 ms: 1.00x slower                                                            |
| genshi_xml     | 49.5 ms                                                                | 49.8 ms: 1.01x slower                                                            |
| genshi_text    | 22.2 ms                                                                | 22.4 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3+-180d417 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 2.71 sec                                                               | 2.51 sec: 1.08x faster                                                           |
| gc_traversal               | 4.77 ms                                                                | 4.62 ms: 1.03x faster                                                            |
| telco                      | 7.97 ms                                                                | 7.84 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.52 sec                                                               | 1.50 sec: 1.02x faster                                                           |
| logging_format             | 6.27 us                                                                | 6.18 us: 1.02x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                                | 72.0 ms: 1.01x faster                                                            |
| scimark_sor                | 124 ms                                                                 | 123 ms: 1.01x faster                                                             |
| coverage                   | 84.5 ms                                                                | 83.3 ms: 1.01x faster                                                            |
| nbody                      | 94.4 ms                                                                | 93.2 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 4.58 sec                                                               | 4.53 sec: 1.01x faster                                                           |
| comprehensions             | 17.1 us                                                                | 16.9 us: 1.01x faster                                                            |
| regex_effbot               | 3.30 ms                                                                | 3.27 ms: 1.01x faster                                                            |
| scimark_monte_carlo        | 68.8 ms                                                                | 68.1 ms: 1.01x faster                                                            |
| sqlite_synth               | 2.80 us                                                                | 2.77 us: 1.01x faster                                                            |
| dulwich_log                | 64.8 ms                                                                | 64.2 ms: 1.01x faster                                                            |
| nqueens                    | 80.4 ms                                                                | 79.7 ms: 1.01x faster                                                            |
| html5lib                   | 63.0 ms                                                                | 62.6 ms: 1.01x faster                                                            |
| richards                   | 44.7 ms                                                                | 44.3 ms: 1.01x faster                                                            |
| json_loads                 | 26.8 us                                                                | 26.6 us: 1.01x faster                                                            |
| hexiom                     | 6.40 ms                                                                | 6.36 ms: 1.01x faster                                                            |
| scimark_fft                | 355 ms                                                                 | 353 ms: 1.01x faster                                                             |
| async_generators           | 423 ms                                                                 | 420 ms: 1.01x faster                                                             |
| pprint_safe_repr           | 741 ms                                                                 | 736 ms: 1.01x faster                                                             |
| 2to3                       | 256 ms                                                                 | 255 ms: 1.00x faster                                                             |
| xml_etree_process          | 59.2 ms                                                                | 59.0 ms: 1.00x faster                                                            |
| fannkuch                   | 410 ms                                                                 | 408 ms: 1.00x faster                                                             |
| deepcopy                   | 259 us                                                                 | 258 us: 1.00x faster                                                             |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                             |
| python_startup_no_site     | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                                            |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                            |
| bench_thread_pool          | 864 us                                                                 | 866 us: 1.00x slower                                                             |
| docutils                   | 2.59 sec                                                               | 2.60 sec: 1.00x slower                                                           |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                            |
| regex_v8                   | 25.3 ms                                                                | 25.4 ms: 1.00x slower                                                            |
| unpickle_pure_python       | 218 us                                                                 | 219 us: 1.00x slower                                                             |
| mako                       | 11.7 ms                                                                | 11.8 ms: 1.00x slower                                                            |
| sqlglot_normalize          | 103 ms                                                                 | 104 ms: 1.01x slower                                                             |
| raytrace                   | 274 ms                                                                 | 275 ms: 1.01x slower                                                             |
| sqlglot_optimize           | 52.4 ms                                                                | 52.7 ms: 1.01x slower                                                            |
| genshi_xml                 | 49.5 ms                                                                | 49.8 ms: 1.01x slower                                                            |
| many_optionals             | 945 us                                                                 | 952 us: 1.01x slower                                                             |
| sqlglot_transpile          | 1.59 ms                                                                | 1.60 ms: 1.01x slower                                                            |
| json_dumps                 | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                            |
| spectral_norm              | 106 ms                                                                 | 107 ms: 1.01x slower                                                             |
| thrift                     | 767 us                                                                 | 774 us: 1.01x slower                                                             |
| genshi_text                | 22.2 ms                                                                | 22.4 ms: 1.01x slower                                                            |
| pathlib                    | 16.4 ms                                                                | 16.6 ms: 1.01x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                                | 1.28 ms: 1.01x slower                                                            |
| deltablue                  | 3.30 ms                                                                | 3.34 ms: 1.01x slower                                                            |
| tomli_loads                | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                                           |
| typing_runtime_protocols   | 161 us                                                                 | 163 us: 1.01x slower                                                             |
| shortest_path              | 480 ms                                                                 | 486 ms: 1.01x slower                                                             |
| deepcopy_memo              | 31.0 us                                                                | 31.4 us: 1.01x slower                                                            |
| scimark_lu                 | 117 ms                                                                 | 118 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 500 ms: 1.02x slower                                                             |
| pyflate                    | 463 ms                                                                 | 474 ms: 1.02x slower                                                             |
| coroutines                 | 23.1 ms                                                                | 23.7 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 483 ms: 1.03x slower                                                             |
| generators                 | 27.9 ms                                                                | 28.6 ms: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (39): logging_silent, xml_etree_parse, sympy_str, xml_etree_iterparse, json, sympy_expand, deepcopy_reduce, meteor_contest, async_tree_io_tg, sqlalchemy_imperative, regex_dna, asyncio_websockets, sympy_sum, bench_mp_pool, sqlalchemy_declarative, logging_simple, regex_compile, k_core, sympy_integrate, chaos, xml_etree_generate, scimark_sparse_mat_mult, pycparser, django_template, richards_super, sphinx, go, subparsers, pylint, pickle_pure_python, async_tree_io, async_tree_memoization_tg, mypy2, connected_components, async_tree_none, async_tree_memoization, async_tree_none_tg, float, djangocms

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 83.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x