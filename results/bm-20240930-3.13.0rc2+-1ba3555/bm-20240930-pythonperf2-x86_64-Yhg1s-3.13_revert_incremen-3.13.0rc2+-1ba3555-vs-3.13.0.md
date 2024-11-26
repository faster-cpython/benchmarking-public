# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-x86_64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.008x faster
- HPT reliability: 96.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| chameleon      | 7.49 ms                                                      | 7.42 ms: 1.01x faster                                                        |
| html5lib       | 72.9 ms                                                      | 72.7 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 580 ms: 1.01x slower                                                         |
| async_tree_none_tg         | 342 ms                                                       | 346 ms: 1.01x slower                                                         |
| async_generators           | 364 ms                                                       | 368 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 606 ms: 1.02x slower                                                         |
| async_tree_io              | 832 ms                                                       | 847 ms: 1.02x slower                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 468 ms: 1.02x slower                                                         |
| async_tree_none            | 370 ms                                                       | 378 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.0 ms: 1.06x faster                                                        |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| float          | 81.6 ms                                                      | 81.9 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                        |
| regex_dna      | 238 ms                                                       | 242 ms: 1.01x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 25.8 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.28 sec: 1.07x faster                                                       |
| xml_etree_process    | 60.7 ms                                                      | 59.6 ms: 1.02x faster                                                        |
| json_loads           | 24.7 us                                                      | 24.4 us: 1.02x faster                                                        |
| unpickle_pure_python | 216 us                                                       | 214 us: 1.01x faster                                                         |
| pickle_pure_python   | 322 us                                                       | 318 us: 1.01x faster                                                         |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                        |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                        |
| genshi_xml     | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                        |
| mako           | 10.3 ms                                                      | 10.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.83 ms: 1.45x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.16 ms: 1.08x faster                                                        |
| coverage                   | 84.5 ms                                                      | 78.6 ms: 1.08x faster                                                        |
| json                       | 5.62 ms                                                      | 5.25 ms: 1.07x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.28 sec: 1.07x faster                                                       |
| nbody                      | 92.1 ms                                                      | 87.0 ms: 1.06x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| richards_super             | 60.2 ms                                                      | 58.4 ms: 1.03x faster                                                        |
| bench_thread_pool          | 929 us                                                       | 903 us: 1.03x faster                                                         |
| telco                      | 8.77 ms                                                      | 8.53 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 176 us                                                       | 171 us: 1.03x faster                                                         |
| generators                 | 33.9 ms                                                      | 33.1 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.02x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.02x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 90.6 ms: 1.02x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.6 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 820 ms: 1.02x faster                                                         |
| hexiom                     | 6.47 ms                                                      | 6.37 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                         |
| json_loads                 | 24.7 us                                                      | 24.4 us: 1.02x faster                                                        |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.01x faster                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 3.45 us: 1.01x faster                                                        |
| richards                   | 52.5 ms                                                      | 51.9 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 214 us: 1.01x faster                                                         |
| pickle_pure_python         | 322 us                                                       | 318 us: 1.01x faster                                                         |
| deltablue                  | 3.38 ms                                                      | 3.35 ms: 1.01x faster                                                        |
| chameleon                  | 7.49 ms                                                      | 7.42 ms: 1.01x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 38.6 us: 1.01x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 65.0 ms: 1.01x faster                                                        |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.01x faster                                                        |
| go                         | 167 ms                                                       | 166 ms: 1.01x faster                                                         |
| sympy_integrate            | 23.4 ms                                                      | 23.4 ms: 1.00x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 72.7 ms: 1.00x faster                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 5.10 sec: 1.00x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 97.7 ms: 1.00x slower                                                        |
| pyflate                    | 493 ms                                                       | 494 ms: 1.00x slower                                                         |
| float                      | 81.6 ms                                                      | 81.9 ms: 1.00x slower                                                        |
| sympy_str                  | 297 ms                                                       | 298 ms: 1.01x slower                                                         |
| sympy_sum                  | 154 ms                                                       | 155 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 1.77 ms: 1.01x slower                                                        |
| spectral_norm              | 97.4 ms                                                      | 98.3 ms: 1.01x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.55 sec: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 580 ms: 1.01x slower                                                         |
| async_tree_none_tg         | 342 ms                                                       | 346 ms: 1.01x slower                                                         |
| regex_effbot               | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.01x slower                                                        |
| async_generators           | 364 ms                                                       | 368 ms: 1.01x slower                                                         |
| regex_dna                  | 238 ms                                                       | 242 ms: 1.01x slower                                                         |
| mako                       | 10.3 ms                                                      | 10.5 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 606 ms: 1.02x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 121 ms: 1.02x slower                                                         |
| async_tree_io              | 832 ms                                                       | 847 ms: 1.02x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 17.8 ms: 1.02x slower                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 468 ms: 1.02x slower                                                         |
| async_tree_none            | 370 ms                                                       | 378 ms: 1.02x slower                                                         |
| crypto_pyaes               | 73.5 ms                                                      | 75.3 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.8 ms: 1.03x slower                                                        |
| chaos                      | 60.6 ms                                                      | 62.2 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 60.3 ms: 1.03x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.18 us: 1.03x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.8 ms: 1.04x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.52 us: 1.04x slower                                                        |
| raytrace                   | 267 ms                                                       | 280 ms: 1.05x slower                                                         |
| scimark_sor                | 125 ms                                                       | 131 ms: 1.05x slower                                                         |
| scimark_fft                | 298 ms                                                       | 314 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (16): bench_mp_pool, async_tree_io_tg, thrift, deepcopy, regex_compile, django_template, xml_etree_generate, docutils, xml_etree_iterparse, sympy_expand, tornado_http, pylint, logging_silent, fannkuch, async_tree_memoization, mypy2
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 96.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.90x