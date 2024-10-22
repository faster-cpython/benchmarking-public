# Results vs. 3.13.0

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.43x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 431 ms: 1.48x slower                                                           |
| docutils       | 2.81 sec                                                     | 3.48 sec: 1.24x slower                                                         |
| html5lib       | 71.9 ms                                                      | 109 ms: 1.51x slower                                                           |
| tornado_http   | 120 ms                                                       | 165 ms: 1.38x slower                                                           |
| Geometric mean | (ref)                                                        | 1.40x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 340 ms                                                       | 360 ms: 1.06x slower                                                           |
| async_tree_io_tg           | 819 ms                                                       | 880 ms: 1.08x slower                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 626 ms: 1.09x slower                                                           |
| async_tree_io              | 847 ms                                                       | 940 ms: 1.11x slower                                                           |
| async_tree_none            | 372 ms                                                       | 413 ms: 1.11x slower                                                           |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.77 sec: 1.12x slower                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 678 ms: 1.13x slower                                                           |
| async_tree_memoization     | 452 ms                                                       | 514 ms: 1.14x slower                                                           |
| asyncio_tcp                | 380 ms                                                       | 449 ms: 1.18x slower                                                           |
| coroutines                 | 21.6 ms                                                      | 28.3 ms: 1.31x slower                                                          |
| async_generators           | 359 ms                                                       | 499 ms: 1.39x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                                   |

Benchmark hidden because not significant (2): async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                           |
| float          | 81.9 ms                                                      | 142 ms: 1.73x slower                                                           |
| nbody          | 88.0 ms                                                      | 193 ms: 2.20x slower                                                           |
| Geometric mean | (ref)                                                        | 1.56x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 248 ms: 1.02x slower                                                           |
| regex_v8       | 26.2 ms                                                      | 27.4 ms: 1.04x slower                                                          |
| regex_effbot   | 3.37 ms                                                      | 3.65 ms: 1.08x slower                                                          |
| regex_compile  | 144 ms                                                       | 229 ms: 1.59x slower                                                           |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 138 ms: 1.05x faster                                                           |
| xml_etree_iterparse  | 100 ms                                                       | 109 ms: 1.09x slower                                                           |
| json_loads           | 24.0 us                                                      | 30.0 us: 1.25x slower                                                          |
| json_dumps           | 11.0 ms                                                      | 14.1 ms: 1.29x slower                                                          |
| tomli_loads          | 2.41 sec                                                     | 3.32 sec: 1.38x slower                                                         |
| xml_etree_generate   | 85.3 ms                                                      | 118 ms: 1.38x slower                                                           |
| xml_etree_process    | 60.9 ms                                                      | 96.1 ms: 1.58x slower                                                          |
| pickle_pure_python   | 318 us                                                       | 594 us: 1.86x slower                                                           |
| unpickle_pure_python | 214 us                                                       | 409 us: 1.91x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.38x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 17.1 ms: 1.29x slower                                                          |
| python_startup_no_site | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 82.9 ms: 1.45x slower                                                          |
| genshi_text     | 26.6 ms                                                      | 44.1 ms: 1.66x slower                                                          |
| django_template | 38.9 ms                                                      | 67.7 ms: 1.74x slower                                                          |
| mako            | 10.4 ms                                                      | 22.3 ms: 2.14x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.73x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 3.27 ms: 1.26x faster                                                          |
| xml_etree_parse            | 145 ms                                                       | 138 ms: 1.05x faster                                                           |
| create_gc_cycles           | 1.76 ms                                                      | 1.68 ms: 1.05x faster                                                          |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                           |
| regex_dna                  | 244 ms                                                       | 248 ms: 1.02x slower                                                           |
| regex_v8                   | 26.2 ms                                                      | 27.4 ms: 1.04x slower                                                          |
| bench_mp_pool              | 4.65 ms                                                      | 4.91 ms: 1.05x slower                                                          |
| async_tree_none_tg         | 340 ms                                                       | 360 ms: 1.06x slower                                                           |
| async_tree_io_tg           | 819 ms                                                       | 880 ms: 1.08x slower                                                           |
| regex_effbot               | 3.37 ms                                                      | 3.65 ms: 1.08x slower                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 626 ms: 1.09x slower                                                           |
| xml_etree_iterparse        | 100 ms                                                       | 109 ms: 1.09x slower                                                           |
| async_tree_io              | 847 ms                                                       | 940 ms: 1.11x slower                                                           |
| async_tree_none            | 372 ms                                                       | 413 ms: 1.11x slower                                                           |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.77 sec: 1.12x slower                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 678 ms: 1.13x slower                                                           |
| deepcopy                   | 397 us                                                       | 451 us: 1.13x slower                                                           |
| async_tree_memoization     | 452 ms                                                       | 514 ms: 1.14x slower                                                           |
| pathlib                    | 17.4 ms                                                      | 19.9 ms: 1.14x slower                                                          |
| json                       | 5.22 ms                                                      | 6.15 ms: 1.18x slower                                                          |
| asyncio_tcp                | 380 ms                                                       | 449 ms: 1.18x slower                                                           |
| telco                      | 8.58 ms                                                      | 10.5 ms: 1.22x slower                                                          |
| docutils                   | 2.81 sec                                                     | 3.48 sec: 1.24x slower                                                         |
| generators                 | 33.5 ms                                                      | 41.7 ms: 1.25x slower                                                          |
| pylint                     | 346 ms                                                       | 432 ms: 1.25x slower                                                           |
| json_loads                 | 24.0 us                                                      | 30.0 us: 1.25x slower                                                          |
| mdp                        | 2.52 sec                                                     | 3.21 sec: 1.27x slower                                                         |
| coverage                   | 81.1 ms                                                      | 104 ms: 1.28x slower                                                           |
| python_startup             | 13.3 ms                                                      | 17.1 ms: 1.29x slower                                                          |
| json_dumps                 | 11.0 ms                                                      | 14.1 ms: 1.29x slower                                                          |
| coroutines                 | 21.6 ms                                                      | 28.3 ms: 1.31x slower                                                          |
| bpe_tokeniser              | 5.10 sec                                                     | 6.69 sec: 1.31x slower                                                         |
| python_startup_no_site     | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                          |
| deepcopy_memo              | 39.5 us                                                      | 53.0 us: 1.34x slower                                                          |
| deepcopy_reduce            | 3.54 us                                                      | 4.77 us: 1.35x slower                                                          |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.80 ms: 1.35x slower                                                          |
| scimark_fft                | 314 ms                                                       | 425 ms: 1.35x slower                                                           |
| meteor_contest             | 128 ms                                                       | 174 ms: 1.35x slower                                                           |
| pycparser                  | 1.26 sec                                                     | 1.73 sec: 1.37x slower                                                         |
| sympy_integrate            | 23.3 ms                                                      | 32.1 ms: 1.38x slower                                                          |
| tomli_loads                | 2.41 sec                                                     | 3.32 sec: 1.38x slower                                                         |
| tornado_http               | 120 ms                                                       | 165 ms: 1.38x slower                                                           |
| xml_etree_generate         | 85.3 ms                                                      | 118 ms: 1.38x slower                                                           |
| async_generators           | 359 ms                                                       | 499 ms: 1.39x slower                                                           |
| genshi_xml                 | 57.3 ms                                                      | 82.9 ms: 1.45x slower                                                          |
| nqueens                    | 88.2 ms                                                      | 128 ms: 1.45x slower                                                           |
| 2to3                       | 291 ms                                                       | 431 ms: 1.48x slower                                                           |
| html5lib                   | 71.9 ms                                                      | 109 ms: 1.51x slower                                                           |
| sympy_str                  | 296 ms                                                       | 453 ms: 1.53x slower                                                           |
| richards                   | 52.7 ms                                                      | 80.8 ms: 1.53x slower                                                          |
| pyflate                    | 492 ms                                                       | 763 ms: 1.55x slower                                                           |
| fannkuch                   | 365 ms                                                       | 569 ms: 1.56x slower                                                           |
| sqlglot_optimize           | 59.7 ms                                                      | 93.5 ms: 1.57x slower                                                          |
| sqlglot_normalize          | 118 ms                                                       | 186 ms: 1.57x slower                                                           |
| xml_etree_process          | 60.9 ms                                                      | 96.1 ms: 1.58x slower                                                          |
| thrift                     | 877 us                                                       | 1.38 ms: 1.58x slower                                                          |
| regex_compile              | 144 ms                                                       | 229 ms: 1.59x slower                                                           |
| sympy_expand               | 505 ms                                                       | 819 ms: 1.62x slower                                                           |
| typing_runtime_protocols   | 174 us                                                       | 282 us: 1.62x slower                                                           |
| richards_super             | 59.8 ms                                                      | 98.7 ms: 1.65x slower                                                          |
| genshi_text                | 26.6 ms                                                      | 44.1 ms: 1.66x slower                                                          |
| crypto_pyaes               | 72.8 ms                                                      | 121 ms: 1.66x slower                                                           |
| sympy_sum                  | 154 ms                                                       | 262 ms: 1.71x slower                                                           |
| spectral_norm              | 97.4 ms                                                      | 166 ms: 1.71x slower                                                           |
| float                      | 81.9 ms                                                      | 142 ms: 1.73x slower                                                           |
| comprehensions             | 17.3 us                                                      | 30.0 us: 1.74x slower                                                          |
| django_template            | 38.9 ms                                                      | 67.7 ms: 1.74x slower                                                          |
| pprint_safe_repr           | 812 ms                                                       | 1.42 sec: 1.75x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 2.92 sec: 1.77x slower                                                         |
| logging_format             | 7.07 us                                                      | 12.6 us: 1.78x slower                                                          |
| logging_simple             | 6.40 us                                                      | 11.7 us: 1.83x slower                                                          |
| hexiom                     | 6.33 ms                                                      | 11.7 ms: 1.84x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 594 us: 1.86x slower                                                           |
| logging_silent             | 97.7 ns                                                      | 183 ns: 1.87x slower                                                           |
| bench_thread_pool          | 901 us                                                       | 1.71 ms: 1.89x slower                                                          |
| unpickle_pure_python       | 214 us                                                       | 409 us: 1.91x slower                                                           |
| scimark_sor                | 126 ms                                                       | 240 ms: 1.91x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 3.40 ms: 1.91x slower                                                          |
| chaos                      | 61.7 ms                                                      | 124 ms: 2.00x slower                                                           |
| scimark_monte_carlo        | 64.9 ms                                                      | 134 ms: 2.06x slower                                                           |
| go                         | 160 ms                                                       | 330 ms: 2.06x slower                                                           |
| raytrace                   | 289 ms                                                       | 599 ms: 2.07x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 2.87 ms: 2.08x slower                                                          |
| mako                       | 10.4 ms                                                      | 22.3 ms: 2.14x slower                                                          |
| nbody                      | 88.0 ms                                                      | 193 ms: 2.20x slower                                                           |
| scimark_lu                 | 97.8 ms                                                      | 235 ms: 2.40x slower                                                           |
| deltablue                  | 3.41 ms                                                      | 8.25 ms: 2.42x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.43x slower                                                                   |

Benchmark hidden because not significant (2): async_tree_memoization_tg, asyncio_websockets
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.17x