# Results vs. 3.12.0

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| chameleon      | 7.23 ms                                                      | 8.59 ms: 1.19x slower                                                               |
| tornado_http   | 121 ms                                                       | 141 ms: 1.17x slower                                                                |
| Geometric mean | (ref)                                                        | 1.18x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 360 ms: 1.20x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 458 ms: 1.18x faster                                                                |
| async_tree_none            | 452 ms                                                       | 391 ms: 1.15x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 920 ms: 1.15x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 937 ms: 1.11x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 629 ms: 1.11x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 496 ms: 1.10x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 644 ms: 1.08x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 259 ms: 1.02x faster                                                                |
| float          | 76.6 ms                                                      | 98.7 ms: 1.29x slower                                                               |
| nbody          | 88.0 ms                                                      | 130 ms: 1.48x slower                                                                |
| Geometric mean | (ref)                                                        | 1.23x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                                |
| regex_v8       | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                               |
| regex_compile  | 144 ms                                                       | 231 ms: 1.61x slower                                                                |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_loads           | 24.4 us                                                      | 24.5 us: 1.01x slower                                                               |
| pickle_dict          | 32.5 us                                                      | 32.9 us: 1.01x slower                                                               |
| unpickle_list        | 4.66 us                                                      | 4.72 us: 1.01x slower                                                               |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                               |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 116 ms: 1.12x slower                                                                |
| xml_etree_generate   | 86.1 ms                                                      | 99.2 ms: 1.15x slower                                                               |
| xml_etree_process    | 58.4 ms                                                      | 68.1 ms: 1.17x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 471 us: 1.48x slower                                                                |
| tomli_loads          | 2.16 sec                                                     | 3.36 sec: 1.56x slower                                                              |
| unpickle_pure_python | 210 us                                                       | 338 us: 1.61x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.14x slower                                                                        |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                               |
| python_startup         | 11.6 ms                                                      | 13.0 ms: 1.12x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 47.5 ms: 1.25x slower                                                               |
| mako            | 10.0 ms                                                      | 14.3 ms: 1.43x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.33x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 360 ms: 1.20x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 458 ms: 1.18x faster                                                                |
| async_tree_none            | 452 ms                                                       | 391 ms: 1.15x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 920 ms: 1.15x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 937 ms: 1.11x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 629 ms: 1.11x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 496 ms: 1.10x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 644 ms: 1.08x faster                                                                |
| generators                 | 37.4 ms                                                      | 35.6 ms: 1.05x faster                                                               |
| pidigits                   | 265 ms                                                       | 259 ms: 1.02x faster                                                                |
| pathlib                    | 18.9 ms                                                      | 18.5 ms: 1.02x faster                                                               |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.01x slower                                                               |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                              |
| pickle_dict                | 32.5 us                                                      | 32.9 us: 1.01x slower                                                               |
| unpickle_list              | 4.66 us                                                      | 4.72 us: 1.01x slower                                                               |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                               |
| coroutines                 | 23.0 ms                                                      | 23.4 ms: 1.02x slower                                                               |
| asyncio_websockets         | 387 ms                                                       | 395 ms: 1.02x slower                                                                |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                                |
| logging_format             | 7.48 us                                                      | 7.69 us: 1.03x slower                                                               |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                                |
| async_generators           | 390 ms                                                       | 403 ms: 1.03x slower                                                                |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                               |
| asyncio_tcp                | 378 ms                                                       | 395 ms: 1.05x slower                                                                |
| sqlite_synth               | 2.77 us                                                      | 2.93 us: 1.06x slower                                                               |
| logging_simple             | 6.71 us                                                      | 7.09 us: 1.06x slower                                                               |
| mdp                        | 2.57 sec                                                     | 2.73 sec: 1.06x slower                                                              |
| json                       | 5.12 ms                                                      | 5.50 ms: 1.07x slower                                                               |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                               |
| bench_thread_pool          | 950 us                                                       | 1.05 ms: 1.11x slower                                                               |
| python_startup             | 11.6 ms                                                      | 13.0 ms: 1.12x slower                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 116 ms: 1.12x slower                                                                |
| dask                       | 392 ms                                                       | 441 ms: 1.13x slower                                                                |
| regex_v8                   | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                               |
| xml_etree_generate         | 86.1 ms                                                      | 99.2 ms: 1.15x slower                                                               |
| meteor_contest             | 128 ms                                                       | 149 ms: 1.17x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 68.1 ms: 1.17x slower                                                               |
| tornado_http               | 121 ms                                                       | 141 ms: 1.17x slower                                                                |
| coverage                   | 66.7 ms                                                      | 78.1 ms: 1.17x slower                                                               |
| crypto_pyaes               | 80.3 ms                                                      | 94.8 ms: 1.18x slower                                                               |
| chameleon                  | 7.23 ms                                                      | 8.59 ms: 1.19x slower                                                               |
| raytrace                   | 298 ms                                                       | 360 ms: 1.21x slower                                                                |
| mypy2                      | 830 ms                                                       | 1.01 sec: 1.22x slower                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 4.14 us: 1.23x slower                                                               |
| django_template            | 38.2 ms                                                      | 47.5 ms: 1.25x slower                                                               |
| pycparser                  | 1.23 sec                                                     | 1.55 sec: 1.25x slower                                                              |
| gunicorn                   | 1.00 ms                                                      | 1.26 ms: 1.26x slower                                                               |
| comprehensions             | 21.9 us                                                      | 27.7 us: 1.26x slower                                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 2.26 ms: 1.27x slower                                                               |
| sympy_integrate            | 23.9 ms                                                      | 30.6 ms: 1.28x slower                                                               |
| chaos                      | 64.0 ms                                                      | 81.9 ms: 1.28x slower                                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.77 ms: 1.28x slower                                                               |
| aiohttp                    | 1.02 ms                                                      | 1.31 ms: 1.29x slower                                                               |
| float                      | 76.6 ms                                                      | 98.7 ms: 1.29x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.06 ms: 1.30x slower                                                               |
| sqlglot_optimize           | 57.5 ms                                                      | 74.6 ms: 1.30x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 4.52 ms: 1.30x slower                                                               |
| sympy_sum                  | 162 ms                                                       | 211 ms: 1.30x slower                                                                |
| telco                      | 6.96 ms                                                      | 9.15 ms: 1.31x slower                                                               |
| deepcopy                   | 368 us                                                       | 485 us: 1.32x slower                                                                |
| sqlglot_normalize          | 116 ms                                                       | 155 ms: 1.34x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 204 us: 1.34x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 2.24 sec: 1.36x slower                                                              |
| pprint_safe_repr           | 807 ms                                                       | 1.10 sec: 1.36x slower                                                              |
| nqueens                    | 89.9 ms                                                      | 122 ms: 1.36x slower                                                                |
| sympy_str                  | 302 ms                                                       | 417 ms: 1.38x slower                                                                |
| dulwich_log                | 65.4 ms                                                      | 91.1 ms: 1.39x slower                                                               |
| fannkuch                   | 350 ms                                                       | 497 ms: 1.42x slower                                                                |
| scimark_fft                | 301 ms                                                       | 428 ms: 1.42x slower                                                                |
| mako                       | 10.0 ms                                                      | 14.3 ms: 1.43x slower                                                               |
| pyflate                    | 439 ms                                                       | 632 ms: 1.44x slower                                                                |
| sympy_expand               | 484 ms                                                       | 698 ms: 1.44x slower                                                                |
| go                         | 150 ms                                                       | 217 ms: 1.45x slower                                                                |
| nbody                      | 88.0 ms                                                      | 130 ms: 1.48x slower                                                                |
| pickle_pure_python         | 318 us                                                       | 471 us: 1.48x slower                                                                |
| scimark_sor                | 109 ms                                                       | 165 ms: 1.52x slower                                                                |
| scimark_lu                 | 98.8 ms                                                      | 151 ms: 1.53x slower                                                                |
| richards_super             | 51.3 ms                                                      | 79.8 ms: 1.55x slower                                                               |
| tomli_loads                | 2.16 sec                                                     | 3.36 sec: 1.56x slower                                                              |
| richards                   | 45.7 ms                                                      | 72.0 ms: 1.57x slower                                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 109 ms: 1.59x slower                                                                |
| spectral_norm              | 91.6 ms                                                      | 147 ms: 1.60x slower                                                                |
| regex_compile              | 144 ms                                                       | 231 ms: 1.61x slower                                                                |
| unpickle_pure_python       | 210 us                                                       | 338 us: 1.61x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.82 ms: 1.62x slower                                                               |
| deepcopy_memo              | 36.8 us                                                      | 61.3 us: 1.67x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 10.9 ms: 1.82x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 6.15 ms: 1.90x slower                                                               |
| logging_silent             | 94.4 ns                                                      | 185 ns: 1.96x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.21x slower                                                                        |

Benchmark hidden because not significant (4): unpickle, regex_effbot, pickle_list, bench_mp_pool
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: 2to3, docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (3) of results/bm-20240504-3.13.0a6+-6f75dbe-PYTHON_UOPS/bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe.json: flaskblogging, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 0.93x