# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.45x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 435 ms: 1.50x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.54 sec: 1.26x slower                                                      |
| html5lib       | 71.9 ms                                                      | 109 ms: 1.52x slower                                                        |
| tornado_http   | 120 ms                                                       | 163 ms: 1.36x slower                                                        |
| Geometric mean | (ref)                                                        | 1.40x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 479 ms: 1.04x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 372 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 634 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 911 ms: 1.11x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.77 sec: 1.12x slower                                                      |
| async_tree_io              | 847 ms                                                       | 967 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 687 ms: 1.15x slower                                                        |
| async_tree_none            | 372 ms                                                       | 430 ms: 1.16x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 531 ms: 1.18x slower                                                        |
| asyncio_tcp                | 380 ms                                                       | 453 ms: 1.19x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 28.1 ms: 1.30x slower                                                       |
| async_generators           | 359 ms                                                       | 508 ms: 1.41x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 256 ms: 1.01x slower                                                        |
| float          | 81.9 ms                                                      | 144 ms: 1.76x slower                                                        |
| nbody          | 88.0 ms                                                      | 200 ms: 2.28x slower                                                        |
| Geometric mean | (ref)                                                        | 1.60x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 239 ms: 1.02x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.52 ms: 1.05x slower                                                       |
| regex_v8       | 26.2 ms                                                      | 27.8 ms: 1.06x slower                                                       |
| regex_compile  | 144 ms                                                       | 233 ms: 1.61x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 109 ms: 1.09x slower                                                        |
| json_loads           | 24.0 us                                                      | 29.8 us: 1.24x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 14.3 ms: 1.30x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 116 ms: 1.35x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.43 sec: 1.42x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 94.3 ms: 1.55x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 596 us: 1.87x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 421 us: 1.96x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.39x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 16.7 ms: 1.25x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 11.4 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 84.3 ms: 1.47x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 43.4 ms: 1.63x slower                                                       |
| django_template | 38.9 ms                                                      | 69.0 ms: 1.77x slower                                                       |
| mako            | 10.4 ms                                                      | 22.1 ms: 2.13x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.73x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 2.88 ms: 1.43x faster                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 4.40 ms: 1.06x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| regex_dna                  | 244 ms                                                       | 239 ms: 1.02x faster                                                        |
| pidigits                   | 253 ms                                                       | 256 ms: 1.01x slower                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 479 ms: 1.04x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.52 ms: 1.05x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 27.8 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 109 ms: 1.09x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 372 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 634 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 911 ms: 1.11x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.77 sec: 1.12x slower                                                      |
| pathlib                    | 17.4 ms                                                      | 19.6 ms: 1.12x slower                                                       |
| deepcopy                   | 397 us                                                       | 453 us: 1.14x slower                                                        |
| async_tree_io              | 847 ms                                                       | 967 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 687 ms: 1.15x slower                                                        |
| async_tree_none            | 372 ms                                                       | 430 ms: 1.16x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 531 ms: 1.18x slower                                                        |
| json                       | 5.22 ms                                                      | 6.21 ms: 1.19x slower                                                       |
| asyncio_tcp                | 380 ms                                                       | 453 ms: 1.19x slower                                                        |
| telco                      | 8.58 ms                                                      | 10.3 ms: 1.20x slower                                                       |
| json_loads                 | 24.0 us                                                      | 29.8 us: 1.24x slower                                                       |
| generators                 | 33.5 ms                                                      | 41.9 ms: 1.25x slower                                                       |
| python_startup             | 13.3 ms                                                      | 16.7 ms: 1.25x slower                                                       |
| pylint                     | 346 ms                                                       | 435 ms: 1.26x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.54 sec: 1.26x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 11.4 ms: 1.28x slower                                                       |
| mdp                        | 2.52 sec                                                     | 3.27 sec: 1.29x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 28.1 ms: 1.30x slower                                                       |
| json_dumps                 | 11.0 ms                                                      | 14.3 ms: 1.30x slower                                                       |
| coverage                   | 81.1 ms                                                      | 107 ms: 1.32x slower                                                        |
| scimark_fft                | 314 ms                                                       | 417 ms: 1.33x slower                                                        |
| deepcopy_memo              | 39.5 us                                                      | 53.2 us: 1.35x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 6.90 sec: 1.35x slower                                                      |
| xml_etree_generate         | 85.3 ms                                                      | 116 ms: 1.35x slower                                                        |
| tornado_http               | 120 ms                                                       | 163 ms: 1.36x slower                                                        |
| meteor_contest             | 128 ms                                                       | 175 ms: 1.37x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 4.85 us: 1.37x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 32.4 ms: 1.39x slower                                                       |
| pycparser                  | 1.26 sec                                                     | 1.75 sec: 1.40x slower                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 6.01 ms: 1.40x slower                                                       |
| async_generators           | 359 ms                                                       | 508 ms: 1.41x slower                                                        |
| tomli_loads                | 2.41 sec                                                     | 3.43 sec: 1.42x slower                                                      |
| genshi_xml                 | 57.3 ms                                                      | 84.3 ms: 1.47x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 130 ms: 1.48x slower                                                        |
| 2to3                       | 291 ms                                                       | 435 ms: 1.50x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 109 ms: 1.52x slower                                                        |
| sympy_str                  | 296 ms                                                       | 456 ms: 1.54x slower                                                        |
| xml_etree_process          | 60.9 ms                                                      | 94.3 ms: 1.55x slower                                                       |
| thrift                     | 877 us                                                       | 1.37 ms: 1.57x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 188 ms: 1.59x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 95.2 ms: 1.60x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 278 us: 1.60x slower                                                        |
| regex_compile              | 144 ms                                                       | 233 ms: 1.61x slower                                                        |
| richards                   | 52.7 ms                                                      | 85.1 ms: 1.62x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 43.4 ms: 1.63x slower                                                       |
| sympy_expand               | 505 ms                                                       | 830 ms: 1.64x slower                                                        |
| pyflate                    | 492 ms                                                       | 813 ms: 1.65x slower                                                        |
| fannkuch                   | 365 ms                                                       | 614 ms: 1.69x slower                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 124 ms: 1.70x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 262 ms: 1.71x slower                                                        |
| richards_super             | 59.8 ms                                                      | 103 ms: 1.73x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 1.56 ms: 1.73x slower                                                       |
| spectral_norm              | 97.4 ms                                                      | 169 ms: 1.74x slower                                                        |
| comprehensions             | 17.3 us                                                      | 30.3 us: 1.76x slower                                                       |
| float                      | 81.9 ms                                                      | 144 ms: 1.76x slower                                                        |
| django_template            | 38.9 ms                                                      | 69.0 ms: 1.77x slower                                                       |
| logging_format             | 7.07 us                                                      | 12.7 us: 1.79x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 1.47 sec: 1.81x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 3.04 sec: 1.84x slower                                                      |
| logging_simple             | 6.40 us                                                      | 11.8 us: 1.84x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 596 us: 1.87x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 12.1 ms: 1.90x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 187 ns: 1.91x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.44 ms: 1.93x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 421 us: 1.96x slower                                                        |
| chaos                      | 61.7 ms                                                      | 124 ms: 2.01x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 136 ms: 2.10x slower                                                        |
| go                         | 160 ms                                                       | 338 ms: 2.10x slower                                                        |
| raytrace                   | 289 ms                                                       | 612 ms: 2.12x slower                                                        |
| scimark_sor                | 126 ms                                                       | 266 ms: 2.12x slower                                                        |
| mako                       | 10.4 ms                                                      | 22.1 ms: 2.13x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 2.94 ms: 2.13x slower                                                       |
| nbody                      | 88.0 ms                                                      | 200 ms: 2.28x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.40 ms: 2.46x slower                                                       |
| scimark_lu                 | 97.8 ms                                                      | 242 ms: 2.48x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.45x slower                                                                |

Benchmark hidden because not significant (2): create_gc_cycles, asyncio_websockets
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.17x