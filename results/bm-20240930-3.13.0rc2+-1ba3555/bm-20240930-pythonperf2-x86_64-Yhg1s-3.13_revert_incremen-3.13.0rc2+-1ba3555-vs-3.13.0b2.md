# Results vs. 3.13.0b2

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-x86_64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.00x slower
- HPT reliability: 89.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 289 ms: 1.01x faster                                                         |
| chameleon      | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                                        |
| docutils       | 2.98 sec                                                         | 2.81 sec: 1.06x faster                                                       |
| html5lib       | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 819 ms: 1.10x faster                                                         |
| async_tree_io             | 873 ms                                                           | 847 ms: 1.03x faster                                                         |
| async_tree_none           | 365 ms                                                           | 378 ms: 1.03x slower                                                         |
| async_tree_memoization_tg | 421 ms                                                           | 468 ms: 1.11x slower                                                         |
| Geometric mean            | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                         |
| float          | 80.2 ms                                                          | 81.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 242 ms: 1.03x faster                                                         |
| regex_compile  | 144 ms                                                           | 142 ms: 1.01x faster                                                         |
| regex_v8       | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 31.0 us: 1.06x faster                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.28 sec: 1.06x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                                         |
| unpickle             | 15.7 us                                                          | 15.2 us: 1.03x faster                                                        |
| json_loads           | 25.0 us                                                          | 24.4 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100.0 ms: 1.03x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 85.3 ms: 1.00x faster                                                        |
| pickle               | 10.6 us                                                          | 10.6 us: 1.00x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 146 ms: 1.02x slower                                                         |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_process, pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                        |
| genshi_text    | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal              | 4.69 ms                                                          | 4.16 ms: 1.13x faster                                                        |
| async_tree_io_tg          | 900 ms                                                           | 819 ms: 1.10x faster                                                         |
| create_gc_cycles          | 2.00 ms                                                          | 1.83 ms: 1.10x faster                                                        |
| coverage                  | 83.5 ms                                                          | 78.6 ms: 1.06x faster                                                        |
| docutils                  | 2.98 sec                                                         | 2.81 sec: 1.06x faster                                                       |
| coroutines                | 22.0 ms                                                          | 20.8 ms: 1.06x faster                                                        |
| pickle_dict               | 32.8 us                                                          | 31.0 us: 1.06x faster                                                        |
| tomli_loads               | 2.40 sec                                                         | 2.28 sec: 1.06x faster                                                       |
| genshi_xml                | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                        |
| unpickle_pure_python      | 224 us                                                           | 214 us: 1.05x faster                                                         |
| richards_super            | 61.2 ms                                                          | 58.4 ms: 1.05x faster                                                        |
| dulwich_log               | 67.3 ms                                                          | 65.0 ms: 1.03x faster                                                        |
| regex_dna                 | 249 ms                                                           | 242 ms: 1.03x faster                                                         |
| async_tree_io             | 873 ms                                                           | 847 ms: 1.03x faster                                                         |
| richards                  | 53.4 ms                                                          | 51.9 ms: 1.03x faster                                                        |
| unpickle                  | 15.7 us                                                          | 15.2 us: 1.03x faster                                                        |
| json_loads                | 25.0 us                                                          | 24.4 us: 1.03x faster                                                        |
| html5lib                  | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 103 ms                                                           | 100.0 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.19 ms: 1.02x faster                                                        |
| dask                      | 391 ms                                                           | 382 ms: 1.02x faster                                                         |
| json                      | 5.35 ms                                                          | 5.25 ms: 1.02x faster                                                        |
| genshi_text               | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                        |
| asyncio_websockets        | 395 ms                                                           | 389 ms: 1.01x faster                                                         |
| flaskblogging             | 4.68 ms                                                          | 4.62 ms: 1.01x faster                                                        |
| generators                | 33.5 ms                                                          | 33.1 ms: 1.01x faster                                                        |
| regex_compile             | 144 ms                                                           | 142 ms: 1.01x faster                                                         |
| 2to3                      | 291 ms                                                           | 289 ms: 1.01x faster                                                         |
| regex_v8                  | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                        |
| deltablue                 | 3.37 ms                                                          | 3.35 ms: 1.01x faster                                                        |
| bpe_tokeniser             | 5.14 sec                                                         | 5.10 sec: 1.01x faster                                                       |
| xml_etree_generate        | 85.7 ms                                                          | 85.3 ms: 1.00x faster                                                        |
| pickle                    | 10.6 us                                                          | 10.6 us: 1.00x faster                                                        |
| pidigits                  | 254 ms                                                           | 253 ms: 1.00x faster                                                         |
| hexiom                    | 6.35 ms                                                          | 6.37 ms: 1.00x slower                                                        |
| chameleon                 | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                                        |
| meteor_contest            | 128 ms                                                           | 129 ms: 1.00x slower                                                         |
| sqlglot_transpile         | 1.76 ms                                                          | 1.77 ms: 1.01x slower                                                        |
| sqlglot_normalize         | 120 ms                                                           | 121 ms: 1.01x slower                                                         |
| go                        | 165 ms                                                           | 166 ms: 1.01x slower                                                         |
| asyncio_tcp               | 378 ms                                                           | 380 ms: 1.01x slower                                                         |
| sympy_integrate           | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                                        |
| spectral_norm             | 97.3 ms                                                          | 98.3 ms: 1.01x slower                                                        |
| logging_format            | 7.11 us                                                          | 7.18 us: 1.01x slower                                                        |
| python_startup            | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                        |
| python_startup_no_site    | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                        |
| sympy_str                 | 295 ms                                                           | 298 ms: 1.01x slower                                                         |
| comprehensions            | 17.0 us                                                          | 17.2 us: 1.01x slower                                                        |
| sqlglot_optimize          | 59.5 ms                                                          | 60.3 ms: 1.01x slower                                                        |
| sympy_expand              | 501 ms                                                           | 507 ms: 1.01x slower                                                         |
| async_generators          | 363 ms                                                           | 368 ms: 1.02x slower                                                         |
| telco                     | 8.40 ms                                                          | 8.53 ms: 1.02x slower                                                        |
| json_dumps                | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                        |
| deepcopy_reduce           | 3.39 us                                                          | 3.45 us: 1.02x slower                                                        |
| xml_etree_parse           | 144 ms                                                           | 146 ms: 1.02x slower                                                         |
| logging_simple            | 6.40 us                                                          | 6.52 us: 1.02x slower                                                        |
| scimark_monte_carlo       | 65.5 ms                                                          | 66.8 ms: 1.02x slower                                                        |
| float                     | 80.2 ms                                                          | 81.9 ms: 1.02x slower                                                        |
| logging_silent            | 96.3 ns                                                          | 98.5 ns: 1.02x slower                                                        |
| crypto_pyaes              | 73.6 ms                                                          | 75.3 ms: 1.02x slower                                                        |
| nqueens                   | 88.4 ms                                                          | 90.6 ms: 1.02x slower                                                        |
| pycparser                 | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                       |
| pyflate                   | 482 ms                                                           | 494 ms: 1.03x slower                                                         |
| deepcopy                  | 377 us                                                           | 388 us: 1.03x slower                                                         |
| async_tree_none           | 365 ms                                                           | 378 ms: 1.03x slower                                                         |
| deepcopy_memo             | 37.3 us                                                          | 38.6 us: 1.03x slower                                                        |
| pickle_pure_python        | 307 us                                                           | 318 us: 1.03x slower                                                         |
| mdp                       | 2.46 sec                                                         | 2.55 sec: 1.04x slower                                                       |
| pathlib                   | 17.1 ms                                                          | 17.8 ms: 1.04x slower                                                        |
| thrift                    | 880 us                                                           | 914 us: 1.04x slower                                                         |
| chaos                     | 59.6 ms                                                          | 62.2 ms: 1.04x slower                                                        |
| regex_effbot              | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                        |
| raytrace                  | 260 ms                                                           | 280 ms: 1.08x slower                                                         |
| fannkuch                  | 353 ms                                                           | 390 ms: 1.11x slower                                                         |
| scimark_sor               | 119 ms                                                           | 131 ms: 1.11x slower                                                         |
| async_tree_memoization_tg | 421 ms                                                           | 468 ms: 1.11x slower                                                         |
| mypy2                     | 764 ms                                                           | 1.05 sec: 1.37x slower                                                       |
| Geometric mean            | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (25): bench_mp_pool, nbody, gunicorn, async_tree_memoization, bench_thread_pool, django_template, xml_etree_process, sympy_sum, tornado_http, sqlite_synth, asyncio_tcp_ssl, sqlglot_parse, typing_runtime_protocols, pprint_pformat, async_tree_cpu_io_mixed, scimark_lu, pickle_list, pprint_safe_repr, aiohttp, unpickle_list, scimark_fft, mako, async_tree_cpu_io_mixed_tg, async_tree_none_tg, pylint
Ignored benchmarks (1) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: unpack_sequence

# HPT report

- Reliability score: 89.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x