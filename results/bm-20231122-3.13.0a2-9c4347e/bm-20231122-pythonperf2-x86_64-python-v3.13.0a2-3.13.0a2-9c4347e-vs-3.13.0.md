# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.01x slower
- HPT reliability: 74.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 292 ms: 1.00x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.47 ms: 1.01x slower                                            |
| docutils       | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| html5lib       | 71.9 ms                                                      | 73.7 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                           |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_generators           | 359 ms                                                       | 370 ms: 1.03x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 690 ms: 1.15x slower                                             |
| async_tree_none            | 372 ms                                                       | 429 ms: 1.15x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 542 ms: 1.20x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 556 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.07 sec: 1.26x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 435 ms: 1.28x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.08 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.9 ms: 1.05x faster                                            |
| float          | 81.9 ms                                                      | 80.9 ms: 1.01x faster                                            |
| pidigits       | 253 ms                                                       | 265 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                            |
| regex_dna      | 244 ms                                                       | 241 ms: 1.01x faster                                             |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| regex_effbot   | 3.37 ms                                                      | 3.63 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.16 sec: 1.11x faster                                           |
| xml_etree_process    | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                            |
| pickle_list          | 4.59 us                                                      | 4.34 us: 1.06x faster                                            |
| pickle               | 10.5 us                                                      | 10.0 us: 1.05x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.5 ms: 1.04x faster                                            |
| pickle_pure_python   | 318 us                                                       | 308 us: 1.03x faster                                             |
| xml_etree_generate   | 85.3 ms                                                      | 84.0 ms: 1.02x faster                                            |
| pickle_dict          | 32.1 us                                                      | 32.6 us: 1.02x slower                                            |
| xml_etree_parse      | 145 ms                                                       | 151 ms: 1.04x slower                                             |
| unpickle_pure_python | 214 us                                                       | 225 us: 1.05x slower                                             |
| json_loads           | 24.0 us                                                      | 25.5 us: 1.06x slower                                            |
| xml_etree_iterparse  | 100 ms                                                       | 108 ms: 1.08x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.9 ms: 1.03x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 11.3 ms: 1.26x slower                                            |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml     | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                            |
| genshi_text    | 26.6 ms                                                      | 25.6 ms: 1.04x faster                                            |
| mako           | 10.4 ms                                                      | 10.1 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                       | 126 us: 1.38x faster                                             |
| mypy2                      | 1.05 sec                                                     | 862 ms: 1.22x faster                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.55 ms: 1.14x faster                                            |
| tomli_loads                | 2.41 sec                                                     | 2.16 sec: 1.11x faster                                           |
| deepcopy                   | 397 us                                                       | 362 us: 1.10x faster                                             |
| deepcopy_reduce            | 3.54 us                                                      | 3.27 us: 1.08x faster                                            |
| raytrace                   | 289 ms                                                       | 271 ms: 1.07x faster                                             |
| xml_etree_process          | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.34 us: 1.06x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.3 ms: 1.06x faster                                            |
| pickle                     | 10.5 us                                                      | 10.0 us: 1.05x faster                                            |
| telco                      | 8.58 ms                                                      | 8.17 ms: 1.05x faster                                            |
| deepcopy_memo              | 39.5 us                                                      | 37.6 us: 1.05x faster                                            |
| nbody                      | 88.0 ms                                                      | 83.9 ms: 1.05x faster                                            |
| genshi_xml                 | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                            |
| gc_traversal               | 4.11 ms                                                      | 3.94 ms: 1.04x faster                                            |
| scimark_fft                | 314 ms                                                       | 301 ms: 1.04x faster                                             |
| json_dumps                 | 11.0 ms                                                      | 10.5 ms: 1.04x faster                                            |
| genshi_text                | 26.6 ms                                                      | 25.6 ms: 1.04x faster                                            |
| regex_v8                   | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                            |
| comprehensions             | 17.3 us                                                      | 16.6 us: 1.04x faster                                            |
| mako                       | 10.4 ms                                                      | 10.1 ms: 1.04x faster                                            |
| sympy_expand               | 505 ms                                                       | 488 ms: 1.03x faster                                             |
| python_startup             | 13.3 ms                                                      | 12.9 ms: 1.03x faster                                            |
| pickle_pure_python         | 318 us                                                       | 308 us: 1.03x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                             |
| sqlglot_optimize           | 59.7 ms                                                      | 58.1 ms: 1.03x faster                                            |
| sqlglot_normalize          | 118 ms                                                       | 115 ms: 1.03x faster                                             |
| coverage                   | 81.1 ms                                                      | 79.1 ms: 1.03x faster                                            |
| richards_super             | 59.8 ms                                                      | 58.3 ms: 1.03x faster                                            |
| pprint_safe_repr           | 812 ms                                                       | 792 ms: 1.03x faster                                             |
| sympy_str                  | 296 ms                                                       | 289 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.19 ms: 1.02x faster                                            |
| sympy_sum                  | 154 ms                                                       | 150 ms: 1.02x faster                                             |
| thrift                     | 877 us                                                       | 858 us: 1.02x faster                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                           |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                            |
| xml_etree_generate         | 85.3 ms                                                      | 84.0 ms: 1.02x faster                                            |
| crypto_pyaes               | 72.8 ms                                                      | 71.7 ms: 1.01x faster                                            |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.01x faster                                            |
| logging_silent             | 97.7 ns                                                      | 96.5 ns: 1.01x faster                                            |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                             |
| float                      | 81.9 ms                                                      | 80.9 ms: 1.01x faster                                            |
| regex_dna                  | 244 ms                                                       | 241 ms: 1.01x faster                                             |
| richards                   | 52.7 ms                                                      | 52.1 ms: 1.01x faster                                            |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                           |
| hexiom                     | 6.33 ms                                                      | 6.35 ms: 1.00x slower                                            |
| 2to3                       | 291 ms                                                       | 292 ms: 1.00x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| logging_simple             | 6.40 us                                                      | 6.44 us: 1.01x slower                                            |
| chameleon                  | 7.42 ms                                                      | 7.47 ms: 1.01x slower                                            |
| scimark_lu                 | 97.8 ms                                                      | 98.6 ms: 1.01x slower                                            |
| gunicorn                   | 1.04 ms                                                      | 1.05 ms: 1.01x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                            |
| nqueens                    | 88.2 ms                                                      | 89.5 ms: 1.01x slower                                            |
| pickle_dict                | 32.1 us                                                      | 32.6 us: 1.02x slower                                            |
| logging_format             | 7.07 us                                                      | 7.20 us: 1.02x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 66.9 ms: 1.02x slower                                            |
| generators                 | 33.5 ms                                                      | 34.2 ms: 1.02x slower                                            |
| fannkuch                   | 365 ms                                                       | 374 ms: 1.02x slower                                             |
| html5lib                   | 71.9 ms                                                      | 73.7 ms: 1.02x slower                                            |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.02x slower                                           |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_generators           | 359 ms                                                       | 370 ms: 1.03x slower                                             |
| pycparser                  | 1.26 sec                                                     | 1.31 sec: 1.04x slower                                           |
| xml_etree_parse            | 145 ms                                                       | 151 ms: 1.04x slower                                             |
| pyflate                    | 492 ms                                                       | 513 ms: 1.04x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.9 ms: 1.05x slower                                            |
| pidigits                   | 253 ms                                                       | 265 ms: 1.05x slower                                             |
| unpickle_pure_python       | 214 us                                                       | 225 us: 1.05x slower                                             |
| bench_thread_pool          | 901 us                                                       | 951 us: 1.06x slower                                             |
| deltablue                  | 3.41 ms                                                      | 3.61 ms: 1.06x slower                                            |
| json_loads                 | 24.0 us                                                      | 25.5 us: 1.06x slower                                            |
| xml_etree_iterparse        | 100 ms                                                       | 108 ms: 1.08x slower                                             |
| regex_effbot               | 3.37 ms                                                      | 3.63 ms: 1.08x slower                                            |
| go                         | 160 ms                                                       | 173 ms: 1.08x slower                                             |
| pathlib                    | 17.4 ms                                                      | 19.1 ms: 1.09x slower                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 690 ms: 1.15x slower                                             |
| async_tree_none            | 372 ms                                                       | 429 ms: 1.15x slower                                             |
| scimark_sor                | 126 ms                                                       | 146 ms: 1.17x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 542 ms: 1.20x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 556 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.07 sec: 1.26x slower                                           |
| python_startup_no_site     | 8.94 ms                                                      | 11.3 ms: 1.26x slower                                            |
| async_tree_none_tg         | 340 ms                                                       | 435 ms: 1.28x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.08 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (11): bench_mp_pool, tornado_http, json, unpickle, aiohttp, django_template, pylint, unpickle_list, flaskblogging, asyncio_websockets, chaos
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence

# HPT report

- Reliability score: 74.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x