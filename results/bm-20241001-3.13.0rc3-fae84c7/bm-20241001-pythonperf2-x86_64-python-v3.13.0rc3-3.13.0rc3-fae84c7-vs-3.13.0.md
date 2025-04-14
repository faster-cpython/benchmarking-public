# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.009x faster
- HPT reliability: 60.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                               |
| chameleon      | 7.49 ms                                                      | 7.54 ms: 1.01x slower                                              |
| html5lib       | 72.9 ms                                                      | 73.7 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_websockets        | 395 ms                                                       | 386 ms: 1.02x faster                                               |
| async_generators          | 364 ms                                                       | 366 ms: 1.01x slower                                               |
| async_tree_memoization_tg | 458 ms                                                       | 463 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 603 ms: 1.01x slower                                               |
| async_tree_none           | 370 ms                                                       | 375 ms: 1.01x slower                                               |
| coroutines                | 21.6 ms                                                      | 23.0 ms: 1.07x slower                                              |
| Geometric mean            | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.5 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                        | 1.02x faster                                                       |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.55 ms: 1.01x slower                                              |
| regex_v8       | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                              |
| regex_compile  | 143 ms                                                       | 145 ms: 1.01x slower                                               |
| regex_dna      | 238 ms                                                       | 246 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python  | 322 us                                                       | 316 us: 1.02x faster                                               |
| xml_etree_process   | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                              |
| json_loads          | 24.7 us                                                      | 24.5 us: 1.01x faster                                              |
| json_dumps          | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                              |
| xml_etree_iterparse | 99.8 ms                                                      | 103 ms: 1.03x slower                                               |
| xml_etree_parse     | 144 ms                                                       | 149 ms: 1.03x slower                                               |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (3): unpickle_pure_python, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                              |
| Geometric mean | (ref)                                                        | 1.08x faster                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                              |
| genshi_xml     | 58.0 ms                                                      | 56.0 ms: 1.04x faster                                              |
| mako           | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| create_gc_cycles          | 2.65 ms                                                      | 1.80 ms: 1.47x faster                                              |
| python_startup            | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                              |
| gc_traversal              | 4.48 ms                                                      | 4.10 ms: 1.09x faster                                              |
| json                      | 5.62 ms                                                      | 5.29 ms: 1.06x faster                                              |
| scimark_sor               | 125 ms                                                       | 118 ms: 1.06x faster                                               |
| genshi_text               | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                              |
| fannkuch                  | 384 ms                                                       | 364 ms: 1.06x faster                                               |
| nbody                     | 92.1 ms                                                      | 87.5 ms: 1.05x faster                                              |
| genshi_xml                | 58.0 ms                                                      | 56.0 ms: 1.04x faster                                              |
| nqueens                   | 92.3 ms                                                      | 89.1 ms: 1.04x faster                                              |
| telco                     | 8.77 ms                                                      | 8.52 ms: 1.03x faster                                              |
| pycparser                 | 1.28 sec                                                     | 1.24 sec: 1.03x faster                                             |
| bench_thread_pool         | 929 us                                                       | 906 us: 1.03x faster                                               |
| deepcopy_memo             | 38.9 us                                                      | 37.9 us: 1.03x faster                                              |
| thrift                    | 918 us                                                       | 895 us: 1.02x faster                                               |
| asyncio_websockets        | 395 ms                                                       | 386 ms: 1.02x faster                                               |
| hexiom                    | 6.47 ms                                                      | 6.33 ms: 1.02x faster                                              |
| generators                | 33.9 ms                                                      | 33.2 ms: 1.02x faster                                              |
| raytrace                  | 267 ms                                                       | 262 ms: 1.02x faster                                               |
| pickle_pure_python        | 322 us                                                       | 316 us: 1.02x faster                                               |
| pprint_pformat            | 1.70 sec                                                     | 1.67 sec: 1.02x faster                                             |
| pprint_safe_repr          | 835 ms                                                       | 820 ms: 1.02x faster                                               |
| spectral_norm             | 97.4 ms                                                      | 95.8 ms: 1.02x faster                                              |
| richards_super            | 60.2 ms                                                      | 59.3 ms: 1.02x faster                                              |
| xml_etree_process         | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                              |
| deepcopy_reduce           | 3.49 us                                                      | 3.44 us: 1.01x faster                                              |
| dulwich_log               | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                              |
| pyflate                   | 493 ms                                                       | 487 ms: 1.01x faster                                               |
| deepcopy                  | 388 us                                                       | 384 us: 1.01x faster                                               |
| json_loads                | 24.7 us                                                      | 24.5 us: 1.01x faster                                              |
| 2to3                      | 293 ms                                                       | 290 ms: 1.01x faster                                               |
| go                        | 167 ms                                                       | 166 ms: 1.01x faster                                               |
| crypto_pyaes              | 73.5 ms                                                      | 73.0 ms: 1.01x faster                                              |
| comprehensions            | 17.3 us                                                      | 17.2 us: 1.01x faster                                              |
| meteor_contest            | 130 ms                                                       | 130 ms: 1.01x faster                                               |
| scimark_monte_carlo       | 65.2 ms                                                      | 64.9 ms: 1.01x faster                                              |
| bpe_tokeniser             | 5.09 sec                                                     | 5.10 sec: 1.00x slower                                             |
| sympy_str                 | 297 ms                                                       | 298 ms: 1.00x slower                                               |
| async_generators          | 364 ms                                                       | 366 ms: 1.01x slower                                               |
| mdp                       | 2.53 sec                                                     | 2.55 sec: 1.01x slower                                             |
| chameleon                 | 7.49 ms                                                      | 7.54 ms: 1.01x slower                                              |
| regex_effbot              | 3.51 ms                                                      | 3.55 ms: 1.01x slower                                              |
| mako                      | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                              |
| html5lib                  | 72.9 ms                                                      | 73.7 ms: 1.01x slower                                              |
| sqlglot_normalize         | 119 ms                                                       | 120 ms: 1.01x slower                                               |
| async_tree_memoization_tg | 458 ms                                                       | 463 ms: 1.01x slower                                               |
| sympy_sum                 | 154 ms                                                       | 155 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 603 ms: 1.01x slower                                               |
| async_tree_none           | 370 ms                                                       | 375 ms: 1.01x slower                                               |
| regex_v8                  | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                              |
| regex_compile             | 143 ms                                                       | 145 ms: 1.01x slower                                               |
| scimark_fft               | 298 ms                                                       | 302 ms: 1.01x slower                                               |
| sqlglot_transpile         | 1.76 ms                                                      | 1.79 ms: 1.01x slower                                              |
| sqlglot_optimize          | 58.7 ms                                                      | 60.1 ms: 1.02x slower                                              |
| json_dumps                | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                              |
| sqlglot_parse             | 1.37 ms                                                      | 1.40 ms: 1.03x slower                                              |
| xml_etree_iterparse       | 99.8 ms                                                      | 103 ms: 1.03x slower                                               |
| xml_etree_parse           | 144 ms                                                       | 149 ms: 1.03x slower                                               |
| regex_dna                 | 238 ms                                                       | 246 ms: 1.03x slower                                               |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 4.36 ms: 1.03x slower                                              |
| logging_format            | 6.95 us                                                      | 7.23 us: 1.04x slower                                              |
| logging_simple            | 6.28 us                                                      | 6.60 us: 1.05x slower                                              |
| coroutines                | 21.6 ms                                                      | 23.0 ms: 1.07x slower                                              |
| Geometric mean            | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (27): async_tree_io_tg, coverage, scimark_lu, unpickle_pure_python, bench_mp_pool, django_template, pathlib, richards, float, sympy_expand, pidigits, tomli_loads, docutils, async_tree_cpu_io_mixed_tg, deltablue, python_startup_no_site, xml_etree_generate, sympy_integrate, typing_runtime_protocols, async_tree_none_tg, logging_silent, tornado_http, pylint, chaos, async_tree_io, async_tree_memoization, mypy2
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.009x faster
# HPT report

- Reliability score: 60.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.90x