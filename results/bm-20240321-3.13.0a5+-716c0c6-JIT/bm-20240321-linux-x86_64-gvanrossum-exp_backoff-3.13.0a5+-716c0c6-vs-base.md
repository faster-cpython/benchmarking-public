# Results vs. base

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 716c0c6
- commit date: 2024-03-21
- overall geometric mean: 1.01x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 307 ms                                                                 | 304 ms: 1.01x faster                                              |
| chameleon      | 7.02 ms                                                                | 6.98 ms: 1.01x faster                                             |
| html5lib       | 75.2 ms                                                                | 75.8 ms: 1.01x slower                                             |
| tornado_http   | 100 ms                                                                 | 101 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 14.1 sec                                                               | 13.9 sec: 1.02x faster                                            |
| async_tree_none            | 3.44 sec                                                               | 3.39 sec: 1.02x faster                                            |
| async_tree_memoization     | 4.42 sec                                                               | 4.37 sec: 1.01x faster                                            |
| async_tree_io              | 13.2 sec                                                               | 13.1 sec: 1.01x faster                                            |
| async_tree_memoization_tg  | 4.69 sec                                                               | 4.65 sec: 1.01x faster                                            |
| async_tree_none_tg         | 3.73 sec                                                               | 3.70 sec: 1.01x faster                                            |
| async_tree_cpu_io_mixed_tg | 4.58 sec                                                               | 4.55 sec: 1.01x faster                                            |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 145 ms                                                                 | 143 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                 | 142 ms: 1.02x faster                                              |
| regex_v8       | 24.3 ms                                                                | 24.2 ms: 1.01x faster                                             |
| regex_effbot   | 3.61 ms                                                                | 3.81 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|---------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_list         | 5.24 us                                                                | 4.80 us: 1.09x faster                                             |
| pickle_dict         | 35.8 us                                                                | 34.5 us: 1.04x faster                                             |
| pickle              | 12.0 us                                                                | 11.6 us: 1.04x faster                                             |
| pickle_pure_python  | 309 us                                                                 | 303 us: 1.02x faster                                              |
| xml_etree_iterparse | 165 ms                                                                 | 163 ms: 1.01x faster                                              |
| xml_etree_generate  | 100 ms                                                                 | 99.6 ms: 1.01x faster                                             |
| unpickle_list       | 5.16 us                                                                | 5.27 us: 1.02x slower                                             |
| unpickle            | 15.0 us                                                                | 15.5 us: 1.03x slower                                             |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (6): json_loads, xml_etree_parse, unpickle_pure_python, xml_etree_process, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                                | 10.1 ms: 1.01x slower                                             |
| python_startup         | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 24.8 ms                                                                | 24.2 ms: 1.03x faster                                             |
| genshi_xml     | 60.5 ms                                                                | 59.8 ms: 1.01x faster                                             |
| mako           | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5+-50f9b0b | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_list                | 5.24 us                                                                | 4.80 us: 1.09x faster                                             |
| richards_super             | 52.8 ms                                                                | 50.0 ms: 1.06x faster                                             |
| raytrace                   | 297 ms                                                                 | 284 ms: 1.05x faster                                              |
| richards                   | 46.1 ms                                                                | 44.3 ms: 1.04x faster                                             |
| pickle_dict                | 35.8 us                                                                | 34.5 us: 1.04x faster                                             |
| pickle                     | 12.0 us                                                                | 11.6 us: 1.04x faster                                             |
| scimark_sor                | 136 ms                                                                 | 131 ms: 1.04x faster                                              |
| scimark_sparse_mat_mult    | 4.96 ms                                                                | 4.79 ms: 1.04x faster                                             |
| sqlglot_transpile          | 1.86 ms                                                                | 1.80 ms: 1.03x faster                                             |
| genshi_text                | 24.8 ms                                                                | 24.2 ms: 1.03x faster                                             |
| scimark_monte_carlo        | 71.1 ms                                                                | 69.5 ms: 1.02x faster                                             |
| logging_format             | 6.60 us                                                                | 6.47 us: 1.02x faster                                             |
| pprint_pformat             | 1.55 sec                                                               | 1.52 sec: 1.02x faster                                            |
| regex_compile              | 144 ms                                                                 | 142 ms: 1.02x faster                                              |
| dulwich_log                | 70.3 ms                                                                | 69.0 ms: 1.02x faster                                             |
| sqlglot_parse              | 1.47 ms                                                                | 1.44 ms: 1.02x faster                                             |
| sympy_integrate            | 21.8 ms                                                                | 21.4 ms: 1.02x faster                                             |
| pickle_pure_python         | 309 us                                                                 | 303 us: 1.02x faster                                              |
| logging_simple             | 5.96 us                                                                | 5.85 us: 1.02x faster                                             |
| float                      | 145 ms                                                                 | 143 ms: 1.02x faster                                              |
| scimark_lu                 | 131 ms                                                                 | 129 ms: 1.02x faster                                              |
| nqueens                    | 89.8 ms                                                                | 88.4 ms: 1.02x faster                                             |
| async_tree_io_tg           | 14.1 sec                                                               | 13.9 sec: 1.02x faster                                            |
| async_tree_none            | 3.44 sec                                                               | 3.39 sec: 1.02x faster                                            |
| sqlglot_optimize           | 59.6 ms                                                                | 58.8 ms: 1.01x faster                                             |
| pprint_safe_repr           | 762 ms                                                                 | 751 ms: 1.01x faster                                              |
| unpack_sequence            | 93.1 ns                                                                | 91.8 ns: 1.01x faster                                             |
| sympy_str                  | 292 ms                                                                 | 288 ms: 1.01x faster                                              |
| deepcopy_memo              | 39.5 us                                                                | 39.0 us: 1.01x faster                                             |
| xml_etree_iterparse        | 165 ms                                                                 | 163 ms: 1.01x faster                                              |
| genshi_xml                 | 60.5 ms                                                                | 59.8 ms: 1.01x faster                                             |
| async_tree_memoization     | 4.42 sec                                                               | 4.37 sec: 1.01x faster                                            |
| async_tree_io              | 13.2 sec                                                               | 13.1 sec: 1.01x faster                                            |
| comprehensions             | 17.8 us                                                                | 17.6 us: 1.01x faster                                             |
| create_gc_cycles           | 1.51 ms                                                                | 1.49 ms: 1.01x faster                                             |
| deepcopy                   | 362 us                                                                 | 358 us: 1.01x faster                                              |
| coroutines                 | 23.2 ms                                                                | 23.0 ms: 1.01x faster                                             |
| async_tree_memoization_tg  | 4.69 sec                                                               | 4.65 sec: 1.01x faster                                            |
| go                         | 157 ms                                                                 | 155 ms: 1.01x faster                                              |
| async_tree_none_tg         | 3.73 sec                                                               | 3.70 sec: 1.01x faster                                            |
| typing_runtime_protocols   | 112 us                                                                 | 111 us: 1.01x faster                                              |
| mako                       | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                             |
| xml_etree_generate         | 100 ms                                                                 | 99.6 ms: 1.01x faster                                             |
| 2to3                       | 307 ms                                                                 | 304 ms: 1.01x faster                                              |
| chameleon                  | 7.02 ms                                                                | 6.98 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed_tg | 4.58 sec                                                               | 4.55 sec: 1.01x faster                                            |
| bench_thread_pool          | 851 us                                                                 | 847 us: 1.01x faster                                              |
| regex_v8                   | 24.3 ms                                                                | 24.2 ms: 1.01x faster                                             |
| hexiom                     | 7.00 ms                                                                | 6.96 ms: 1.00x faster                                             |
| scimark_fft                | 342 ms                                                                 | 341 ms: 1.00x faster                                              |
| tornado_http               | 100 ms                                                                 | 101 ms: 1.00x slower                                              |
| asyncio_websockets         | 567 ms                                                                 | 570 ms: 1.01x slower                                              |
| python_startup_no_site     | 10.1 ms                                                                | 10.1 ms: 1.01x slower                                             |
| python_startup             | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                             |
| deepcopy_reduce            | 3.16 us                                                                | 3.18 us: 1.01x slower                                             |
| telco                      | 8.36 ms                                                                | 8.43 ms: 1.01x slower                                             |
| html5lib                   | 75.2 ms                                                                | 75.8 ms: 1.01x slower                                             |
| thrift                     | 805 us                                                                 | 813 us: 1.01x slower                                              |
| pycparser                  | 1.45 sec                                                               | 1.47 sec: 1.01x slower                                            |
| async_generators           | 549 ms                                                                 | 556 ms: 1.01x slower                                              |
| mdp                        | 2.81 sec                                                               | 2.86 sec: 1.01x slower                                            |
| logging_silent             | 99.9 ns                                                                | 102 ns: 1.02x slower                                              |
| pathlib                    | 18.8 ms                                                                | 19.1 ms: 1.02x slower                                             |
| crypto_pyaes               | 74.9 ms                                                                | 76.3 ms: 1.02x slower                                             |
| unpickle_list              | 5.16 us                                                                | 5.27 us: 1.02x slower                                             |
| pyflate                    | 482 ms                                                                 | 493 ms: 1.02x slower                                              |
| json                       | 5.18 ms                                                                | 5.32 ms: 1.03x slower                                             |
| unpickle                   | 15.0 us                                                                | 15.5 us: 1.03x slower                                             |
| gc_traversal               | 3.59 ms                                                                | 3.74 ms: 1.04x slower                                             |
| regex_effbot               | 3.61 ms                                                                | 3.81 ms: 1.06x slower                                             |
| deltablue                  | 3.67 ms                                                                | 3.90 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (31): json_loads, xml_etree_parse, dask, sqlglot_normalize, mypy2, aiohttp, unpickle_pure_python, sympy_expand, pylint, xml_etree_process, sympy_sum, gunicorn, coverage, spectral_norm, chaos, asyncio_tcp_ssl, generators, nbody, docutils, fannkuch, regex_dna, django_template, tomli_loads, meteor_contest, pidigits, asyncio_tcp, async_tree_cpu_io_mixed, bench_mp_pool, sqlite_synth, json_dumps, djangocms


# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.99x