# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.008x faster
- HPT reliability: 71.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 291 ms: 1.00x faster                                               |
| chameleon      | 7.49 ms                                                      | 7.37 ms: 1.02x faster                                              |
| docutils       | 2.81 sec                                                     | 3.00 sec: 1.07x slower                                             |
| html5lib       | 72.9 ms                                                      | 74.6 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 434 ms: 1.05x faster                                               |
| asyncio_websockets        | 395 ms                                                       | 390 ms: 1.01x faster                                               |
| async_generators          | 364 ms                                                       | 368 ms: 1.01x slower                                               |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 615 ms: 1.03x slower                                               |
| async_tree_memoization    | 447 ms                                                       | 466 ms: 1.04x slower                                               |
| async_tree_io             | 832 ms                                                       | 879 ms: 1.06x slower                                               |
| async_tree_io_tg          | 823 ms                                                       | 913 ms: 1.11x slower                                               |
| Geometric mean            | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 80.5 ms: 1.01x faster                                              |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 143 ms: 1.00x slower                                               |
| regex_v8       | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                              |
| regex_dna      | 238 ms                                                       | 248 ms: 1.04x slower                                               |
| regex_effbot   | 3.51 ms                                                      | 3.74 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                        | 1.03x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 24.7 us                                                      | 23.8 us: 1.04x faster                                              |
| pickle_pure_python   | 322 us                                                       | 311 us: 1.04x faster                                               |
| xml_etree_generate   | 85.2 ms                                                      | 87.4 ms: 1.03x slower                                              |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                               |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.03x slower                                              |
| unpickle_pure_python | 216 us                                                       | 229 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                              |
| Geometric mean | (ref)                                                        | 1.08x faster                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                              |
| genshi_xml      | 58.0 ms                                                      | 57.2 ms: 1.01x faster                                              |
| django_template | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mypy2                     | 1.02 sec                                                     | 769 ms: 1.33x faster                                               |
| create_gc_cycles          | 2.65 ms                                                      | 2.00 ms: 1.32x faster                                              |
| python_startup            | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                              |
| json                      | 5.62 ms                                                      | 5.19 ms: 1.08x faster                                              |
| scimark_sor               | 125 ms                                                       | 118 ms: 1.06x faster                                               |
| async_tree_memoization_tg | 458 ms                                                       | 434 ms: 1.05x faster                                               |
| coverage                  | 84.5 ms                                                      | 80.4 ms: 1.05x faster                                              |
| bench_mp_pool             | 4.82 ms                                                      | 4.61 ms: 1.05x faster                                              |
| fannkuch                  | 384 ms                                                       | 369 ms: 1.04x faster                                               |
| json_loads                | 24.7 us                                                      | 23.8 us: 1.04x faster                                              |
| thrift                    | 918 us                                                       | 882 us: 1.04x faster                                               |
| pycparser                 | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                             |
| bench_thread_pool         | 929 us                                                       | 897 us: 1.04x faster                                               |
| pickle_pure_python        | 322 us                                                       | 311 us: 1.04x faster                                               |
| genshi_text               | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                              |
| deepcopy_memo             | 38.9 us                                                      | 37.7 us: 1.03x faster                                              |
| raytrace                  | 267 ms                                                       | 260 ms: 1.03x faster                                               |
| pyflate                   | 493 ms                                                       | 481 ms: 1.02x faster                                               |
| richards_super            | 60.2 ms                                                      | 58.8 ms: 1.02x faster                                              |
| hexiom                    | 6.47 ms                                                      | 6.32 ms: 1.02x faster                                              |
| deepcopy                  | 388 us                                                       | 381 us: 1.02x faster                                               |
| chameleon                 | 7.49 ms                                                      | 7.37 ms: 1.02x faster                                              |
| crypto_pyaes              | 73.5 ms                                                      | 72.4 ms: 1.02x faster                                              |
| pprint_safe_repr          | 835 ms                                                       | 823 ms: 1.02x faster                                               |
| genshi_xml                | 58.0 ms                                                      | 57.2 ms: 1.01x faster                                              |
| deepcopy_reduce           | 3.49 us                                                      | 3.44 us: 1.01x faster                                              |
| telco                     | 8.77 ms                                                      | 8.65 ms: 1.01x faster                                              |
| float                     | 81.6 ms                                                      | 80.5 ms: 1.01x faster                                              |
| nqueens                   | 92.3 ms                                                      | 91.1 ms: 1.01x faster                                              |
| pathlib                   | 17.4 ms                                                      | 17.2 ms: 1.01x faster                                              |
| pprint_pformat            | 1.70 sec                                                     | 1.68 sec: 1.01x faster                                             |
| asyncio_websockets        | 395 ms                                                       | 390 ms: 1.01x faster                                               |
| richards                  | 52.5 ms                                                      | 52.0 ms: 1.01x faster                                              |
| go                        | 167 ms                                                       | 165 ms: 1.01x faster                                               |
| meteor_contest            | 130 ms                                                       | 129 ms: 1.01x faster                                               |
| comprehensions            | 17.3 us                                                      | 17.1 us: 1.01x faster                                              |
| chaos                     | 60.6 ms                                                      | 60.1 ms: 1.01x faster                                              |
| logging_silent            | 97.5 ns                                                      | 96.9 ns: 1.01x faster                                              |
| dulwich_log               | 65.5 ms                                                      | 65.1 ms: 1.01x faster                                              |
| scimark_lu                | 97.4 ms                                                      | 96.9 ms: 1.00x faster                                              |
| 2to3                      | 293 ms                                                       | 291 ms: 1.00x faster                                               |
| sympy_integrate           | 23.4 ms                                                      | 23.5 ms: 1.00x slower                                              |
| spectral_norm             | 97.4 ms                                                      | 97.8 ms: 1.00x slower                                              |
| regex_compile             | 143 ms                                                       | 143 ms: 1.00x slower                                               |
| sympy_expand              | 506 ms                                                       | 509 ms: 1.00x slower                                               |
| pidigits                  | 252 ms                                                       | 254 ms: 1.01x slower                                               |
| bpe_tokeniser             | 5.09 sec                                                     | 5.13 sec: 1.01x slower                                             |
| sympy_sum                 | 154 ms                                                       | 155 ms: 1.01x slower                                               |
| mdp                       | 2.53 sec                                                     | 2.55 sec: 1.01x slower                                             |
| sympy_str                 | 297 ms                                                       | 299 ms: 1.01x slower                                               |
| django_template           | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| async_generators          | 364 ms                                                       | 368 ms: 1.01x slower                                               |
| scimark_fft               | 298 ms                                                       | 302 ms: 1.01x slower                                               |
| scimark_monte_carlo       | 65.2 ms                                                      | 66.2 ms: 1.01x slower                                              |
| sqlglot_transpile         | 1.76 ms                                                      | 1.79 ms: 1.02x slower                                              |
| regex_v8                  | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                              |
| html5lib                  | 72.9 ms                                                      | 74.6 ms: 1.02x slower                                              |
| sqlglot_optimize          | 58.7 ms                                                      | 60.1 ms: 1.02x slower                                              |
| xml_etree_generate        | 85.2 ms                                                      | 87.4 ms: 1.03x slower                                              |
| xml_etree_iterparse       | 99.8 ms                                                      | 103 ms: 1.03x slower                                               |
| sqlglot_normalize         | 119 ms                                                       | 122 ms: 1.03x slower                                               |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 615 ms: 1.03x slower                                               |
| json_dumps                | 10.8 ms                                                      | 11.2 ms: 1.03x slower                                              |
| sqlglot_parse             | 1.37 ms                                                      | 1.41 ms: 1.04x slower                                              |
| regex_dna                 | 238 ms                                                       | 248 ms: 1.04x slower                                               |
| async_tree_memoization    | 447 ms                                                       | 466 ms: 1.04x slower                                               |
| async_tree_io             | 832 ms                                                       | 879 ms: 1.06x slower                                               |
| unpickle_pure_python      | 216 us                                                       | 229 us: 1.06x slower                                               |
| regex_effbot              | 3.51 ms                                                      | 3.74 ms: 1.07x slower                                              |
| docutils                  | 2.81 sec                                                     | 3.00 sec: 1.07x slower                                             |
| async_tree_io_tg          | 823 ms                                                       | 913 ms: 1.11x slower                                               |
| Geometric mean            | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (18): nbody, tomli_loads, logging_simple, async_tree_none, python_startup_no_site, deltablue, tornado_http, gc_traversal, logging_format, generators, mako, xml_etree_process, xml_etree_parse, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, async_tree_none_tg, scimark_sparse_mat_mult, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 71.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.91x