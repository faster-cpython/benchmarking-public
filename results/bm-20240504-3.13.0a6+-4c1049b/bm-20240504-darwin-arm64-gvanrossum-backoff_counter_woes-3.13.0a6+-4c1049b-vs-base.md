# Results vs. base

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: darwin-arm64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x faster
- HPT reliability: 57.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                 | 159 ms: 1.01x faster                                                       |
| chameleon      | 4.34 ms                                                                | 4.38 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager                 | 61.1 ms                                                                | 60.4 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 326 ms                                                                 | 328 ms: 1.01x slower                                                       |
| async_tree_eager_tg              | 41.4 ms                                                                | 42.0 ms: 1.01x slower                                                      |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (13): async_tree_io, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_eager_io_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                                | 59.3 ms: 1.12x faster                                                      |
| float          | 49.3 ms                                                                | 48.6 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 68.3 ms                                                                | 68.7 ms: 1.01x slower                                                      |
| regex_effbot   | 2.55 ms                                                                | 2.56 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps         | 6.36 ms                                                                | 6.14 ms: 1.04x faster                                                      |
| unpickle_list      | 3.34 us                                                                | 3.26 us: 1.02x faster                                                      |
| xml_etree_parse    | 98.6 ms                                                                | 98.1 ms: 1.00x faster                                                      |
| pickle_list        | 2.97 us                                                                | 2.99 us: 1.01x slower                                                      |
| xml_etree_process  | 36.8 ms                                                                | 37.0 ms: 1.01x slower                                                      |
| xml_etree_generate | 52.4 ms                                                                | 53.1 ms: 1.01x slower                                                      |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (8): unpickle, tomli_loads, pickle_dict, json_loads, pickle, unpickle_pure_python, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                                      |
| python_startup         | 13.8 ms                                                                | 13.7 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 14.0 ms                                                                | 13.9 ms: 1.01x faster                                                      |
| mako           | 6.85 ms                                                                | 6.89 ms: 1.01x slower                                                      |
| genshi_xml     | 29.8 ms                                                                | 30.0 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody                            | 66.3 ms                                                                | 59.3 ms: 1.12x faster                                                      |
| mdp                              | 1.67 sec                                                               | 1.50 sec: 1.11x faster                                                     |
| json_dumps                       | 6.36 ms                                                                | 6.14 ms: 1.04x faster                                                      |
| typing_runtime_protocols         | 92.0 us                                                                | 88.9 us: 1.03x faster                                                      |
| scimark_fft                      | 190 ms                                                                 | 184 ms: 1.03x faster                                                       |
| chaos                            | 35.6 ms                                                                | 34.7 ms: 1.03x faster                                                      |
| unpickle_list                    | 3.34 us                                                                | 3.26 us: 1.02x faster                                                      |
| spectral_norm                    | 67.8 ms                                                                | 66.5 ms: 1.02x faster                                                      |
| scimark_monte_carlo              | 43.1 ms                                                                | 42.4 ms: 1.02x faster                                                      |
| comprehensions                   | 10.8 us                                                                | 10.6 us: 1.02x faster                                                      |
| float                            | 49.3 ms                                                                | 48.6 ms: 1.01x faster                                                      |
| coverage                         | 46.0 ms                                                                | 45.4 ms: 1.01x faster                                                      |
| raytrace                         | 150 ms                                                                 | 148 ms: 1.01x faster                                                       |
| python_startup_no_site           | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                                      |
| async_tree_eager                 | 61.1 ms                                                                | 60.4 ms: 1.01x faster                                                      |
| pprint_pformat                   | 959 ms                                                                 | 949 ms: 1.01x faster                                                       |
| python_startup                   | 13.8 ms                                                                | 13.7 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult          | 2.78 ms                                                                | 2.76 ms: 1.01x faster                                                      |
| genshi_text                      | 14.0 ms                                                                | 13.9 ms: 1.01x faster                                                      |
| scimark_sor                      | 95.8 ms                                                                | 95.1 ms: 1.01x faster                                                      |
| 2to3                             | 160 ms                                                                 | 159 ms: 1.01x faster                                                       |
| deepcopy_reduce                  | 1.79 us                                                                | 1.78 us: 1.00x faster                                                      |
| xml_etree_parse                  | 98.6 ms                                                                | 98.1 ms: 1.00x faster                                                      |
| gc_traversal                     | 2.50 ms                                                                | 2.49 ms: 1.00x faster                                                      |
| deepcopy                         | 203 us                                                                 | 202 us: 1.00x faster                                                       |
| sympy_integrate                  | 10.3 ms                                                                | 10.3 ms: 1.00x faster                                                      |
| create_gc_cycles                 | 948 us                                                                 | 946 us: 1.00x faster                                                       |
| sqlite_synth                     | 1.55 us                                                                | 1.55 us: 1.00x faster                                                      |
| meteor_contest                   | 71.3 ms                                                                | 71.5 ms: 1.00x slower                                                      |
| sympy_expand                     | 226 ms                                                                 | 227 ms: 1.00x slower                                                       |
| richards_super                   | 35.1 ms                                                                | 35.3 ms: 1.00x slower                                                      |
| dulwich_log                      | 27.2 ms                                                                | 27.3 ms: 1.00x slower                                                      |
| pyflate                          | 319 ms                                                                 | 321 ms: 1.01x slower                                                       |
| async_tree_eager_cpu_io_mixed_tg | 326 ms                                                                 | 328 ms: 1.01x slower                                                       |
| logging_silent                   | 60.2 ns                                                                | 60.5 ns: 1.01x slower                                                      |
| mako                             | 6.85 ms                                                                | 6.89 ms: 1.01x slower                                                      |
| logging_format                   | 3.31 us                                                                | 3.33 us: 1.01x slower                                                      |
| regex_compile                    | 68.3 ms                                                                | 68.7 ms: 1.01x slower                                                      |
| genshi_xml                       | 29.8 ms                                                                | 30.0 ms: 1.01x slower                                                      |
| regex_effbot                     | 2.55 ms                                                                | 2.56 ms: 1.01x slower                                                      |
| hexiom                           | 4.08 ms                                                                | 4.10 ms: 1.01x slower                                                      |
| sympy_str                        | 131 ms                                                                 | 132 ms: 1.01x slower                                                       |
| pickle_list                      | 2.97 us                                                                | 2.99 us: 1.01x slower                                                      |
| xml_etree_process                | 36.8 ms                                                                | 37.0 ms: 1.01x slower                                                      |
| chameleon                        | 4.34 ms                                                                | 4.38 ms: 1.01x slower                                                      |
| xml_etree_generate               | 52.4 ms                                                                | 53.1 ms: 1.01x slower                                                      |
| fannkuch                         | 255 ms                                                                 | 258 ms: 1.01x slower                                                       |
| scimark_lu                       | 66.9 ms                                                                | 67.8 ms: 1.01x slower                                                      |
| async_tree_eager_tg              | 41.4 ms                                                                | 42.0 ms: 1.01x slower                                                      |
| json                             | 2.97 ms                                                                | 3.03 ms: 1.02x slower                                                      |
| flaskblogging                    | 4.28 ms                                                                | 5.18 ms: 1.21x slower                                                      |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (58): bench_mp_pool, gunicorn, dask, async_tree_io, unpickle, pprint_safe_repr, tornado_http, asyncio_tcp, generators, mypy2, tomli_loads, sqlglot_optimize, django_template, docutils, pickle_dict, sqlglot_normalize, json_loads, pycparser, aiohttp, pidigits, logging_simple, regex_v8, go, crypto_pyaes, pickle, async_tree_eager_cpu_io_mixed, sqlglot_parse, unpickle_pure_python, regex_dna, xml_etree_iterparse, bench_thread_pool, nqueens, asyncio_websockets, async_tree_cpu_io_mixed, deepcopy_memo, html5lib, pickle_pure_python, async_tree_eager_memoization, richards, deltablue, telco, sympy_sum, async_tree_cpu_io_mixed_tg, thrift, async_generators, async_tree_eager_io, async_tree_none_tg, async_tree_eager_memoization_tg, pathlib, async_tree_memoization_tg, asyncio_tcp_ssl, pylint, sqlglot_transpile, async_tree_memoization, async_tree_none, async_tree_eager_io_tg, coroutines, async_tree_io_tg

# HPT report

- Reliability score: 57.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x