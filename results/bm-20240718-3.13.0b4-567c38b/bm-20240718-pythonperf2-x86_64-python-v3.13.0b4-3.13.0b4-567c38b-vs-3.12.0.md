# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.000x faster
- HPT reliability: 75.63%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.20 ms: 1.00x faster                                            |
| docutils       | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                           |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 427 ms: 1.27x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                             |
| async_tree_none            | 452 ms                                                       | 367 ms: 1.23x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 875 ms: 1.19x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 464 ms: 1.17x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 905 ms: 1.16x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 614 ms: 1.13x faster                                             |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                             |
| float          | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                            |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| regex_dna      | 239 ms                                                       | 251 ms: 1.05x slower                                             |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                             |
| xml_etree_generate   | 86.1 ms                                                      | 86.9 ms: 1.01x slower                                            |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                             |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.03x slower                                             |
| xml_etree_iterparse  | 103 ms                                                       | 106 ms: 1.04x slower                                             |
| xml_etree_process    | 58.4 ms                                                      | 61.5 ms: 1.05x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                           |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                            |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                            |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.1 ms: 1.03x slower                                            |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                            |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 427 ms: 1.27x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                             |
| async_tree_none            | 452 ms                                                       | 367 ms: 1.23x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 875 ms: 1.19x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 464 ms: 1.17x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 905 ms: 1.16x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 614 ms: 1.13x faster                                             |
| raytrace                   | 298 ms                                                       | 263 ms: 1.13x faster                                             |
| generators                 | 37.4 ms                                                      | 33.4 ms: 1.12x faster                                            |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                            |
| mypy2                      | 830 ms                                                       | 768 ms: 1.08x faster                                             |
| async_generators           | 390 ms                                                       | 362 ms: 1.08x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 74.6 ms: 1.08x faster                                            |
| logging_format             | 7.48 us                                                      | 7.01 us: 1.07x faster                                            |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                             |
| bench_thread_pool          | 950 us                                                       | 901 us: 1.05x faster                                             |
| chaos                      | 64.0 ms                                                      | 60.9 ms: 1.05x faster                                            |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.1 ms: 1.04x faster                                            |
| logging_simple             | 6.71 us                                                      | 6.47 us: 1.04x faster                                            |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.04x faster                                            |
| scimark_lu                 | 98.8 ms                                                      | 96.2 ms: 1.03x faster                                            |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                            |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.02x faster                                             |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                             |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                            |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.01x faster                                             |
| mdp                        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                           |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.16 ms: 1.01x faster                                            |
| regex_effbot               | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                           |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                             |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| chameleon                  | 7.23 ms                                                      | 7.20 ms: 1.00x faster                                            |
| scimark_fft                | 301 ms                                                       | 302 ms: 1.00x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                           |
| pprint_safe_repr           | 807 ms                                                       | 814 ms: 1.01x slower                                             |
| xml_etree_generate         | 86.1 ms                                                      | 86.9 ms: 1.01x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 66.3 ms: 1.01x slower                                            |
| logging_silent             | 94.4 ns                                                      | 95.9 ns: 1.02x slower                                            |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                            |
| deepcopy_memo              | 36.8 us                                                      | 37.5 us: 1.02x slower                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.44 us: 1.02x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                             |
| deepcopy                   | 368 us                                                       | 377 us: 1.02x slower                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 58.9 ms: 1.02x slower                                            |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.02x slower                                            |
| django_template            | 38.2 ms                                                      | 39.1 ms: 1.03x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                             |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                             |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 149 ms: 1.03x slower                                             |
| xml_etree_iterparse        | 103 ms                                                       | 106 ms: 1.04x slower                                             |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                            |
| docutils                   | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                           |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                             |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                            |
| float                      | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.05x slower                                            |
| regex_dna                  | 239 ms                                                       | 251 ms: 1.05x slower                                             |
| xml_etree_process          | 58.4 ms                                                      | 61.5 ms: 1.05x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 97.6 ms: 1.07x slower                                            |
| scimark_sor                | 109 ms                                                       | 116 ms: 1.07x slower                                             |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                            |
| hexiom                     | 5.96 ms                                                      | 6.38 ms: 1.07x slower                                            |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                             |
| pyflate                    | 439 ms                                                       | 492 ms: 1.12x slower                                             |
| tomli_loads                | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                           |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                             |
| richards_super             | 51.3 ms                                                      | 59.0 ms: 1.15x slower                                            |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                            |
| richards                   | 45.7 ms                                                      | 53.0 ms: 1.16x slower                                            |
| telco                      | 6.96 ms                                                      | 8.29 ms: 1.19x slower                                            |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 4.60 ms: 1.32x slower                                            |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (6): bench_mp_pool, pycparser, sqlglot_transpile, asyncio_websockets, dask, nbody
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 75.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.94x