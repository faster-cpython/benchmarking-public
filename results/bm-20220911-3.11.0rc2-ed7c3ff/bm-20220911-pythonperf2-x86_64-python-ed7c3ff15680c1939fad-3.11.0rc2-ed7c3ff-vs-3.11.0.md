
# Results vs. 3.11.0

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: linux-x86_64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.00x slower \*
- HPT reliability: 75.91%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| chameleon      | 7.67 ms                                                      | 7.50 ms: 1.02x faster                                                        |
| tornado_http   | 122 ms                                                       | 125 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 75.1 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.29 ms: 1.06x faster                                                        |
| regex_dna      | 227 ms                                                       | 225 ms: 1.01x faster                                                         |
| regex_v8       | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle             | 13.4 us                                                      | 13.0 us: 1.03x faster                                                        |
| pickle_list          | 3.83 us                                                      | 3.77 us: 1.02x faster                                                        |
| json_loads           | 28.7 us                                                      | 28.4 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 104 ms: 1.01x faster                                                         |
| pickle_dict          | 30.8 us                                                      | 30.7 us: 1.00x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 80.8 ms: 1.00x slower                                                        |
| json_dumps           | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                                        |
| xml_etree_process    | 56.5 ms                                                      | 57.0 ms: 1.01x slower                                                        |
| xml_etree_parse      | 158 ms                                                       | 160 ms: 1.02x slower                                                         |
| pickle_pure_python   | 319 us                                                       | 324 us: 1.02x slower                                                         |
| unpickle_pure_python | 241 us                                                       | 250 us: 1.04x slower                                                         |
| unpickle_list        | 4.53 us                                                      | 4.72 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.72 ms: 1.00x faster                                                        |
| python_startup         | 10.8 ms                                                      | 10.7 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 59.2 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot            | 3.50 ms                                                      | 3.29 ms: 1.06x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.63 ms: 1.06x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 121 ms: 1.04x faster                                                         |
| gunicorn                | 973 us                                                       | 941 us: 1.03x faster                                                         |
| generators              | 56.0 ms                                                      | 54.2 ms: 1.03x faster                                                        |
| unpickle                | 13.4 us                                                      | 13.0 us: 1.03x faster                                                        |
| raytrace                | 317 ms                                                       | 307 ms: 1.03x faster                                                         |
| scimark_fft             | 285 ms                                                       | 277 ms: 1.03x faster                                                         |
| chameleon               | 7.67 ms                                                      | 7.50 ms: 1.02x faster                                                        |
| thrift                  | 925 us                                                       | 906 us: 1.02x faster                                                         |
| flaskblogging           | 3.88 ms                                                      | 3.80 ms: 1.02x faster                                                        |
| aiohttp                 | 985 us                                                       | 966 us: 1.02x faster                                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 58.8 ms: 1.02x faster                                                        |
| nqueens                 | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| pickle_list             | 3.83 us                                                      | 3.77 us: 1.02x faster                                                        |
| json                    | 5.65 ms                                                      | 5.57 ms: 1.01x faster                                                        |
| scimark_sor             | 111 ms                                                       | 110 ms: 1.01x faster                                                         |
| mdp                     | 2.75 sec                                                     | 2.72 sec: 1.01x faster                                                       |
| json_loads              | 28.7 us                                                      | 28.4 us: 1.01x faster                                                        |
| logging_format          | 8.11 us                                                      | 8.03 us: 1.01x faster                                                        |
| regex_dna               | 227 ms                                                       | 225 ms: 1.01x faster                                                         |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.01 ms: 1.01x faster                                                        |
| sympy_sum               | 185 ms                                                       | 183 ms: 1.01x faster                                                         |
| sqlalchemy_imperative   | 20.1 ms                                                      | 19.9 ms: 1.01x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 104 ms: 1.01x faster                                                         |
| scimark_lu              | 115 ms                                                       | 114 ms: 1.01x faster                                                         |
| python_startup_no_site  | 7.76 ms                                                      | 7.72 ms: 1.00x faster                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 746 ms: 1.00x faster                                                         |
| python_startup          | 10.8 ms                                                      | 10.7 ms: 1.00x faster                                                        |
| pickle_dict             | 30.8 us                                                      | 30.7 us: 1.00x faster                                                        |
| sympy_expand            | 555 ms                                                       | 553 ms: 1.00x faster                                                         |
| xml_etree_generate      | 80.5 ms                                                      | 80.8 ms: 1.00x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 19.1 ms: 1.01x slower                                                        |
| json_dumps              | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.9 ms: 1.01x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 791 ms: 1.01x slower                                                         |
| async_tree_memoization  | 630 ms                                                       | 636 ms: 1.01x slower                                                         |
| pprint_pformat          | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                                       |
| xml_etree_process       | 56.5 ms                                                      | 57.0 ms: 1.01x slower                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 84.3 ms: 1.01x slower                                                        |
| pycparser               | 1.32 sec                                                     | 1.34 sec: 1.01x slower                                                       |
| genshi_xml              | 58.5 ms                                                      | 59.2 ms: 1.01x slower                                                        |
| coroutines              | 27.6 ms                                                      | 27.9 ms: 1.01x slower                                                        |
| meteor_contest          | 131 ms                                                       | 132 ms: 1.01x slower                                                         |
| float                   | 74.2 ms                                                      | 75.1 ms: 1.01x slower                                                        |
| xml_etree_parse         | 158 ms                                                       | 160 ms: 1.02x slower                                                         |
| pickle_pure_python      | 319 us                                                       | 324 us: 1.02x slower                                                         |
| regex_v8                | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                        |
| dulwich_log             | 68.4 ms                                                      | 69.6 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.56 ms: 1.02x slower                                                        |
| deepcopy                | 399 us                                                       | 407 us: 1.02x slower                                                         |
| dask                    | 410 ms                                                       | 420 ms: 1.02x slower                                                         |
| spectral_norm           | 93.3 ms                                                      | 95.5 ms: 1.02x slower                                                        |
| deltablue               | 4.00 ms                                                      | 4.09 ms: 1.02x slower                                                        |
| fannkuch                | 429 ms                                                       | 441 ms: 1.03x slower                                                         |
| tornado_http            | 122 ms                                                       | 125 ms: 1.03x slower                                                         |
| create_gc_cycles        | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                                        |
| logging_simple          | 7.19 us                                                      | 7.43 us: 1.03x slower                                                        |
| comprehensions          | 24.6 us                                                      | 25.5 us: 1.04x slower                                                        |
| async_generators        | 316 ms                                                       | 328 ms: 1.04x slower                                                         |
| unpickle_pure_python    | 241 us                                                       | 250 us: 1.04x slower                                                         |
| unpickle_list           | 4.53 us                                                      | 4.72 us: 1.04x slower                                                        |
| go                      | 164 ms                                                       | 172 ms: 1.05x slower                                                         |
| deepcopy_memo           | 38.8 us                                                      | 41.0 us: 1.06x slower                                                        |
| richards                | 48.3 ms                                                      | 53.5 ms: 1.11x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (29): bench_mp_pool, django_template, nbody, mako, bench_thread_pool, sqlite_synth, async_tree_none, pickle, genshi_text, 2to3, mypy2, hexiom, regex_compile, asyncio_tcp, deepcopy_reduce, pidigits, sympy_str, docutils, sqlglot_transpile, async_tree_io, logging_silent, unpack_sequence, pyflate, telco, html5lib, chaos, scimark_monte_carlo, sqlalchemy_declarative, pylint
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 75.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
