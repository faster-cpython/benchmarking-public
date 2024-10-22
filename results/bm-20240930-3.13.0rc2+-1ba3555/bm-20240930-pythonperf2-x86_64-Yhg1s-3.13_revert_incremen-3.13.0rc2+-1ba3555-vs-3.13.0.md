# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-x86_64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.00x slower
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 289 ms: 1.01x faster                                                         |
| html5lib       | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 580 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 606 ms: 1.01x slower                                                         |
| async_tree_memoization_tg  | 461 ms                                                       | 468 ms: 1.01x slower                                                         |
| async_tree_none            | 372 ms                                                       | 378 ms: 1.02x slower                                                         |
| async_tree_none_tg         | 340 ms                                                       | 346 ms: 1.02x slower                                                         |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                         |
| async_generators           | 359 ms                                                       | 368 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): asyncio_tcp_ssl, asyncio_tcp, async_tree_io_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                        |
| regex_compile  | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| regex_dna      | 244 ms                                                       | 242 ms: 1.01x faster                                                         |
| regex_effbot   | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads       | 2.41 sec                                                     | 2.28 sec: 1.06x faster                                                       |
| pickle_dict       | 32.1 us                                                      | 31.0 us: 1.03x faster                                                        |
| pickle_list       | 4.59 us                                                      | 4.46 us: 1.03x faster                                                        |
| xml_etree_process | 60.9 ms                                                      | 59.6 ms: 1.02x faster                                                        |
| xml_etree_parse   | 145 ms                                                       | 146 ms: 1.01x slower                                                         |
| json_loads        | 24.0 us                                                      | 24.4 us: 1.02x slower                                                        |
| unpickle_list     | 4.62 us                                                      | 4.73 us: 1.02x slower                                                        |
| Geometric mean    | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (7): unpickle_pure_python, pickle_pure_python, xml_etree_iterparse, xml_etree_generate, json_dumps, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                        |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 25.4 ms: 1.05x faster                                                        |
| genshi_xml     | 57.3 ms                                                      | 55.2 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpack_sequence            | 56.8 ns                                                      | 49.8 ns: 1.14x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.28 sec: 1.06x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 25.4 ms: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 55.2 ms: 1.04x faster                                                        |
| pickle_dict                | 32.1 us                                                      | 31.0 us: 1.03x faster                                                        |
| coverage                   | 81.1 ms                                                      | 78.6 ms: 1.03x faster                                                        |
| raytrace                   | 289 ms                                                       | 280 ms: 1.03x faster                                                         |
| pickle_list                | 4.59 us                                                      | 4.46 us: 1.03x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.45 us: 1.03x faster                                                        |
| deepcopy                   | 397 us                                                       | 388 us: 1.02x faster                                                         |
| richards_super             | 59.8 ms                                                      | 58.4 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.19 ms: 1.02x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 38.6 us: 1.02x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.6 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 171 us: 1.02x faster                                                         |
| deltablue                  | 3.41 ms                                                      | 3.35 ms: 1.02x faster                                                        |
| richards                   | 52.7 ms                                                      | 51.9 ms: 1.02x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                        |
| regex_compile              | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| nbody                      | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                        |
| generators                 | 33.5 ms                                                      | 33.1 ms: 1.01x faster                                                        |
| regex_dna                  | 244 ms                                                       | 242 ms: 1.01x faster                                                         |
| 2to3                       | 291 ms                                                       | 289 ms: 1.01x faster                                                         |
| dulwich_log                | 65.5 ms                                                      | 65.0 ms: 1.01x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.53 ms: 1.01x faster                                                        |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.01x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.77 ms: 1.00x faster                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                         |
| pyflate                    | 492 ms                                                       | 494 ms: 1.00x slower                                                         |
| sympy_expand               | 505 ms                                                       | 507 ms: 1.01x slower                                                         |
| hexiom                     | 6.33 ms                                                      | 6.37 ms: 1.01x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 155 ms: 1.01x slower                                                         |
| sympy_str                  | 296 ms                                                       | 298 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                                       |
| aiohttp                    | 1.07 ms                                                      | 1.08 ms: 1.01x slower                                                        |
| spectral_norm              | 97.4 ms                                                      | 98.3 ms: 1.01x slower                                                        |
| chaos                      | 61.7 ms                                                      | 62.2 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 580 ms: 1.01x slower                                                         |
| xml_etree_parse            | 145 ms                                                       | 146 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 606 ms: 1.01x slower                                                         |
| sqlglot_optimize           | 59.7 ms                                                      | 60.3 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 812 ms                                                       | 820 ms: 1.01x slower                                                         |
| mdp                        | 2.52 sec                                                     | 2.55 sec: 1.01x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.16 ms: 1.01x slower                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 468 ms: 1.01x slower                                                         |
| json_loads                 | 24.0 us                                                      | 24.4 us: 1.02x slower                                                        |
| async_tree_none            | 372 ms                                                       | 378 ms: 1.02x slower                                                         |
| logging_format             | 7.07 us                                                      | 7.18 us: 1.02x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 346 ms: 1.02x slower                                                         |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                         |
| pathlib                    | 17.4 ms                                                      | 17.8 ms: 1.02x slower                                                        |
| logging_simple             | 6.40 us                                                      | 6.52 us: 1.02x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 121 ms: 1.02x slower                                                         |
| unpickle_list              | 4.62 us                                                      | 4.73 us: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 368 ms: 1.03x slower                                                         |
| nqueens                    | 88.2 ms                                                      | 90.6 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.8 ms: 1.03x slower                                                        |
| go                         | 160 ms                                                       | 166 ms: 1.03x slower                                                         |
| crypto_pyaes               | 72.8 ms                                                      | 75.3 ms: 1.04x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.83 ms: 1.04x slower                                                        |
| thrift                     | 877 us                                                       | 914 us: 1.04x slower                                                         |
| scimark_sor                | 126 ms                                                       | 131 ms: 1.05x slower                                                         |
| regex_effbot               | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                        |
| fannkuch                   | 365 ms                                                       | 390 ms: 1.07x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (34): pycparser, tornado_http, unpickle_pure_python, scimark_lu, pickle_pure_python, mypy2, xml_etree_iterparse, gunicorn, docutils, xml_etree_generate, chameleon, pidigits, asyncio_tcp_ssl, json_dumps, float, django_template, scimark_fft, flaskblogging, asyncio_tcp, async_tree_io_tg, bpe_tokeniser, sympy_integrate, async_tree_io, pylint, bench_thread_pool, sqlite_synth, pickle, json, mako, unpickle, dask, logging_silent, async_tree_memoization, bench_mp_pool

# HPT report

- Reliability score: 99.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x