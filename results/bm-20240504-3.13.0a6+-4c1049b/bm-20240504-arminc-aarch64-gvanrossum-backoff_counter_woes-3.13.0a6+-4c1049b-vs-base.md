# Results vs. base

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-aarch64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 56.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 301 ms                                                                   | 303 ms: 1.01x slower                                                         |
| chameleon      | 9.40 ms                                                                  | 9.33 ms: 1.01x faster                                                        |
| html5lib       | 66.4 ms                                                                  | 65.9 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                   | 234 ms: 1.00x slower                                                         |
| nbody          | 110 ms                                                                   | 111 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 4.86 ms                                                                  | 4.85 ms: 1.00x faster                                                        |
| regex_dna      | 247 ms                                                                   | 246 ms: 1.00x faster                                                         |
| regex_v8       | 30.3 ms                                                                  | 31.1 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 115 ms                                                                   | 113 ms: 1.02x faster                                                         |
| xml_etree_process    | 80.5 ms                                                                  | 79.8 ms: 1.01x faster                                                        |
| unpickle             | 19.9 us                                                                  | 19.8 us: 1.00x faster                                                        |
| unpickle_pure_python | 255 us                                                                   | 254 us: 1.00x faster                                                         |
| pickle_dict          | 37.7 us                                                                  | 37.7 us: 1.00x faster                                                        |
| pickle_pure_python   | 354 us                                                                   | 355 us: 1.01x slower                                                         |
| unpickle_list        | 6.63 us                                                                  | 6.67 us: 1.01x slower                                                        |
| json_dumps           | 13.0 ms                                                                  | 13.2 ms: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                    | 1.00x slower                                                                 |

Benchmark hidden because not significant (6): pickle, xml_etree_iterparse, tomli_loads, json_loads, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                                  | 12.5 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.32 ms                                                                  | 8.42 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 42.7 ms                                                                  | 41.9 ms: 1.02x faster                                                        |
| mako            | 13.4 ms                                                                  | 13.2 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                    | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_reduce          | 4.17 us                                                                  | 4.08 us: 1.02x faster                                                        |
| deepcopy_memo            | 51.1 us                                                                  | 50.1 us: 1.02x faster                                                        |
| thrift                   | 962 us                                                                   | 945 us: 1.02x faster                                                         |
| django_template          | 42.7 ms                                                                  | 41.9 ms: 1.02x faster                                                        |
| xml_etree_generate       | 115 ms                                                                   | 113 ms: 1.02x faster                                                         |
| mako                     | 13.4 ms                                                                  | 13.2 ms: 1.01x faster                                                        |
| coroutines               | 30.2 ms                                                                  | 29.8 ms: 1.01x faster                                                        |
| xml_etree_process        | 80.5 ms                                                                  | 79.8 ms: 1.01x faster                                                        |
| generators               | 38.8 ms                                                                  | 38.4 ms: 1.01x faster                                                        |
| chameleon                | 9.40 ms                                                                  | 9.33 ms: 1.01x faster                                                        |
| deepcopy                 | 452 us                                                                   | 449 us: 1.01x faster                                                         |
| scimark_sparse_mat_mult  | 6.56 ms                                                                  | 6.52 ms: 1.01x faster                                                        |
| html5lib                 | 66.4 ms                                                                  | 65.9 ms: 1.01x faster                                                        |
| pprint_pformat           | 1.93 sec                                                                 | 1.92 sec: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 2.23 sec                                                                 | 2.22 sec: 1.00x faster                                                       |
| sqlglot_transpile        | 1.74 ms                                                                  | 1.73 ms: 1.00x faster                                                        |
| scimark_sor              | 160 ms                                                                   | 159 ms: 1.00x faster                                                         |
| unpickle                 | 19.9 us                                                                  | 19.8 us: 1.00x faster                                                        |
| unpickle_pure_python     | 255 us                                                                   | 254 us: 1.00x faster                                                         |
| regex_effbot             | 4.86 ms                                                                  | 4.85 ms: 1.00x faster                                                        |
| regex_dna                | 247 ms                                                                   | 246 ms: 1.00x faster                                                         |
| scimark_fft              | 444 ms                                                                   | 443 ms: 1.00x faster                                                         |
| pickle_dict              | 37.7 us                                                                  | 37.7 us: 1.00x faster                                                        |
| pidigits                 | 233 ms                                                                   | 234 ms: 1.00x slower                                                         |
| richards_super           | 62.1 ms                                                                  | 62.2 ms: 1.00x slower                                                        |
| go                       | 159 ms                                                                   | 159 ms: 1.00x slower                                                         |
| fannkuch                 | 462 ms                                                                   | 464 ms: 1.00x slower                                                         |
| telco                    | 9.74 ms                                                                  | 9.78 ms: 1.00x slower                                                        |
| pickle_pure_python       | 354 us                                                                   | 355 us: 1.01x slower                                                         |
| crypto_pyaes             | 83.9 ms                                                                  | 84.3 ms: 1.01x slower                                                        |
| spectral_norm            | 137 ms                                                                   | 138 ms: 1.01x slower                                                         |
| raytrace                 | 293 ms                                                                   | 295 ms: 1.01x slower                                                         |
| sqlglot_normalize        | 127 ms                                                                   | 128 ms: 1.01x slower                                                         |
| nbody                    | 110 ms                                                                   | 111 ms: 1.01x slower                                                         |
| unpickle_list            | 6.63 us                                                                  | 6.67 us: 1.01x slower                                                        |
| scimark_monte_carlo      | 80.8 ms                                                                  | 81.3 ms: 1.01x slower                                                        |
| 2to3                     | 301 ms                                                                   | 303 ms: 1.01x slower                                                         |
| coverage                 | 100 ms                                                                   | 101 ms: 1.01x slower                                                         |
| pyflate                  | 553 ms                                                                   | 559 ms: 1.01x slower                                                         |
| hexiom                   | 7.04 ms                                                                  | 7.12 ms: 1.01x slower                                                        |
| logging_format           | 7.84 us                                                                  | 7.93 us: 1.01x slower                                                        |
| python_startup           | 12.4 ms                                                                  | 12.5 ms: 1.01x slower                                                        |
| python_startup_no_site   | 8.32 ms                                                                  | 8.42 ms: 1.01x slower                                                        |
| logging_silent           | 133 ns                                                                   | 135 ns: 1.01x slower                                                         |
| json                     | 5.74 ms                                                                  | 5.83 ms: 1.02x slower                                                        |
| typing_runtime_protocols | 199 us                                                                   | 202 us: 1.02x slower                                                         |
| sqlite_synth             | 3.85 us                                                                  | 3.91 us: 1.02x slower                                                        |
| json_dumps               | 13.0 ms                                                                  | 13.2 ms: 1.02x slower                                                        |
| dulwich_log              | 57.9 ms                                                                  | 59.2 ms: 1.02x slower                                                        |
| flaskblogging            | 4.72 ms                                                                  | 4.83 ms: 1.02x slower                                                        |
| create_gc_cycles         | 2.39 ms                                                                  | 2.45 ms: 1.02x slower                                                        |
| regex_v8                 | 30.3 ms                                                                  | 31.1 ms: 1.03x slower                                                        |
| logging_simple           | 7.11 us                                                                  | 7.31 us: 1.03x slower                                                        |
| Geometric mean           | (ref)                                                                    | 1.00x slower                                                                 |

Benchmark hidden because not significant (47): async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, bench_thread_pool, aiohttp, pathlib, async_tree_none, tornado_http, asyncio_tcp, async_tree_memoization, async_generators, sqlglot_parse, docutils, meteor_contest, nqueens, richards, pprint_safe_repr, scimark_lu, genshi_xml, gunicorn, pickle, bench_mp_pool, xml_etree_iterparse, comprehensions, gc_traversal, mdp, sympy_expand, chaos, sqlglot_optimize, deltablue, sympy_sum, regex_compile, genshi_text, tomli_loads, float, json_loads, pickle_list, sympy_str, asyncio_websockets, pylint, sympy_integrate, async_tree_cpu_io_mixed, xml_etree_parse, pycparser, dask

# HPT report

- Reliability score: 56.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x