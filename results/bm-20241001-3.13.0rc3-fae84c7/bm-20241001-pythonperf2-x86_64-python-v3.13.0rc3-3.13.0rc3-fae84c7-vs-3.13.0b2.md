# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.00x slower
- HPT reliability: 81.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 290 ms: 1.00x faster                                               |
| chameleon      | 7.40 ms                                                          | 7.54 ms: 1.02x slower                                              |
| docutils       | 2.98 sec                                                         | 2.81 sec: 1.06x faster                                             |
| html5lib       | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                            | 1.01x faster                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 816 ms: 1.10x faster                                               |
| async_tree_io             | 873 ms                                                           | 842 ms: 1.04x faster                                               |
| async_tree_none           | 365 ms                                                           | 375 ms: 1.03x slower                                               |
| async_tree_memoization_tg | 421 ms                                                           | 463 ms: 1.10x slower                                               |
| Geometric mean            | (ref)                                                            | 1.00x faster                                                       |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                               |
| float          | 80.2 ms                                                          | 81.6 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                            | 1.00x slower                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                              |
| regex_dna      | 249 ms                                                           | 246 ms: 1.01x faster                                               |
| regex_compile  | 144 ms                                                           | 145 ms: 1.00x slower                                               |
| regex_effbot   | 3.40 ms                                                          | 3.55 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                            | 1.00x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.4 us: 1.08x faster                                              |
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                               |
| pickle               | 10.6 us                                                          | 10.2 us: 1.04x faster                                              |
| pickle_list          | 4.44 us                                                          | 4.31 us: 1.03x faster                                              |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                              |
| xml_etree_generate   | 85.7 ms                                                          | 85.3 ms: 1.00x faster                                              |
| tomli_loads          | 2.40 sec                                                         | 2.43 sec: 1.01x slower                                             |
| unpickle             | 15.7 us                                                          | 16.0 us: 1.02x slower                                              |
| unpickle_list        | 4.70 us                                                          | 4.81 us: 1.02x slower                                              |
| pickle_pure_python   | 307 us                                                           | 316 us: 1.03x slower                                               |
| json_dumps           | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                              |
| xml_etree_parse      | 144 ms                                                           | 149 ms: 1.03x slower                                               |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                              |
| python_startup_no_site | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 56.0 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                            | 1.01x faster                                                       |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal              | 4.69 ms                                                          | 4.10 ms: 1.14x faster                                              |
| create_gc_cycles          | 2.00 ms                                                          | 1.80 ms: 1.11x faster                                              |
| async_tree_io_tg          | 900 ms                                                           | 816 ms: 1.10x faster                                               |
| pickle_dict               | 32.8 us                                                          | 30.4 us: 1.08x faster                                              |
| docutils                  | 2.98 sec                                                         | 2.81 sec: 1.06x faster                                             |
| dulwich_log               | 67.3 ms                                                          | 64.6 ms: 1.04x faster                                              |
| unpickle_pure_python      | 224 us                                                           | 216 us: 1.04x faster                                               |
| pickle                    | 10.6 us                                                          | 10.2 us: 1.04x faster                                              |
| async_tree_io             | 873 ms                                                           | 842 ms: 1.04x faster                                               |
| genshi_xml                | 58.1 ms                                                          | 56.0 ms: 1.04x faster                                              |
| scimark_fft               | 312 ms                                                           | 302 ms: 1.03x faster                                               |
| richards_super            | 61.2 ms                                                          | 59.3 ms: 1.03x faster                                              |
| pickle_list               | 4.44 us                                                          | 4.31 us: 1.03x faster                                              |
| regex_v8                  | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                              |
| dask                      | 391 ms                                                           | 379 ms: 1.03x faster                                               |
| json_loads                | 25.0 us                                                          | 24.5 us: 1.02x faster                                              |
| asyncio_websockets        | 395 ms                                                           | 386 ms: 1.02x faster                                               |
| richards                  | 53.4 ms                                                          | 52.5 ms: 1.02x faster                                              |
| gunicorn                  | 1.04 ms                                                          | 1.03 ms: 1.02x faster                                              |
| spectral_norm             | 97.3 ms                                                          | 95.8 ms: 1.02x faster                                              |
| flaskblogging             | 4.68 ms                                                          | 4.61 ms: 1.02x faster                                              |
| html5lib                  | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                              |
| regex_dna                 | 249 ms                                                           | 246 ms: 1.01x faster                                               |
| json                      | 5.35 ms                                                          | 5.29 ms: 1.01x faster                                              |
| generators                | 33.5 ms                                                          | 33.2 ms: 1.01x faster                                              |
| scimark_monte_carlo       | 65.5 ms                                                          | 64.9 ms: 1.01x faster                                              |
| crypto_pyaes              | 73.6 ms                                                          | 73.0 ms: 1.01x faster                                              |
| bpe_tokeniser             | 5.14 sec                                                         | 5.10 sec: 1.01x faster                                             |
| pidigits                  | 254 ms                                                           | 252 ms: 1.01x faster                                               |
| xml_etree_generate        | 85.7 ms                                                          | 85.3 ms: 1.00x faster                                              |
| scimark_sor               | 119 ms                                                           | 118 ms: 1.00x faster                                               |
| 2to3                      | 291 ms                                                           | 290 ms: 1.00x faster                                               |
| hexiom                    | 6.35 ms                                                          | 6.33 ms: 1.00x faster                                              |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                             |
| regex_compile             | 144 ms                                                           | 145 ms: 1.00x slower                                               |
| sympy_sum                 | 155 ms                                                           | 155 ms: 1.00x slower                                               |
| go                        | 165 ms                                                           | 166 ms: 1.00x slower                                               |
| pprint_pformat            | 1.66 sec                                                         | 1.67 sec: 1.01x slower                                             |
| raytrace                  | 260 ms                                                           | 262 ms: 1.01x slower                                               |
| nqueens                   | 88.4 ms                                                          | 89.1 ms: 1.01x slower                                              |
| aiohttp                   | 1.07 ms                                                          | 1.08 ms: 1.01x slower                                              |
| async_generators          | 363 ms                                                           | 366 ms: 1.01x slower                                               |
| python_startup            | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                              |
| sqlglot_parse             | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                              |
| coverage                  | 83.5 ms                                                          | 84.3 ms: 1.01x slower                                              |
| sqlglot_optimize          | 59.5 ms                                                          | 60.1 ms: 1.01x slower                                              |
| python_startup_no_site    | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                              |
| pyflate                   | 482 ms                                                           | 487 ms: 1.01x slower                                               |
| sympy_str                 | 295 ms                                                           | 298 ms: 1.01x slower                                               |
| sympy_expand              | 501 ms                                                           | 506 ms: 1.01x slower                                               |
| meteor_contest            | 128 ms                                                           | 130 ms: 1.01x slower                                               |
| sympy_integrate           | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                              |
| sqlglot_transpile         | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                              |
| tomli_loads               | 2.40 sec                                                         | 2.43 sec: 1.01x slower                                             |
| comprehensions            | 17.0 us                                                          | 17.2 us: 1.01x slower                                              |
| telco                     | 8.40 ms                                                          | 8.52 ms: 1.01x slower                                              |
| deepcopy_reduce           | 3.39 us                                                          | 3.44 us: 1.02x slower                                              |
| logging_silent            | 96.3 ns                                                          | 97.8 ns: 1.02x slower                                              |
| pathlib                   | 17.1 ms                                                          | 17.4 ms: 1.02x slower                                              |
| logging_format            | 7.11 us                                                          | 7.23 us: 1.02x slower                                              |
| asyncio_tcp               | 378 ms                                                           | 384 ms: 1.02x slower                                               |
| deepcopy_memo             | 37.3 us                                                          | 37.9 us: 1.02x slower                                              |
| float                     | 80.2 ms                                                          | 81.6 ms: 1.02x slower                                              |
| thrift                    | 880 us                                                           | 895 us: 1.02x slower                                               |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.36 ms: 1.02x slower                                              |
| deepcopy                  | 377 us                                                           | 384 us: 1.02x slower                                               |
| pycparser                 | 1.22 sec                                                         | 1.24 sec: 1.02x slower                                             |
| unpickle                  | 15.7 us                                                          | 16.0 us: 1.02x slower                                              |
| chameleon                 | 7.40 ms                                                          | 7.54 ms: 1.02x slower                                              |
| chaos                     | 59.6 ms                                                          | 60.9 ms: 1.02x slower                                              |
| unpickle_list             | 4.70 us                                                          | 4.81 us: 1.02x slower                                              |
| async_tree_none           | 365 ms                                                           | 375 ms: 1.03x slower                                               |
| pickle_pure_python        | 307 us                                                           | 316 us: 1.03x slower                                               |
| logging_simple            | 6.40 us                                                          | 6.60 us: 1.03x slower                                              |
| json_dumps                | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                              |
| typing_runtime_protocols  | 171 us                                                           | 176 us: 1.03x slower                                               |
| fannkuch                  | 353 ms                                                           | 364 ms: 1.03x slower                                               |
| mdp                       | 2.46 sec                                                         | 2.55 sec: 1.03x slower                                             |
| xml_etree_parse           | 144 ms                                                           | 149 ms: 1.03x slower                                               |
| regex_effbot              | 3.40 ms                                                          | 3.55 ms: 1.04x slower                                              |
| coroutines                | 22.0 ms                                                          | 23.0 ms: 1.05x slower                                              |
| async_tree_memoization_tg | 421 ms                                                           | 463 ms: 1.10x slower                                               |
| mypy2                     | 764 ms                                                           | 1.05 sec: 1.38x slower                                             |
| Geometric mean            | (ref)                                                            | 1.00x slower                                                       |

Benchmark hidden because not significant (19): bench_mp_pool, async_tree_memoization, genshi_text, django_template, nbody, scimark_lu, async_tree_cpu_io_mixed, bench_thread_pool, sqlglot_normalize, tornado_http, xml_etree_process, async_tree_cpu_io_mixed_tg, pprint_safe_repr, deltablue, sqlite_synth, xml_etree_iterparse, mako, async_tree_none_tg, pylint
Ignored benchmarks (1) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: unpack_sequence

# HPT report

- Reliability score: 81.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x