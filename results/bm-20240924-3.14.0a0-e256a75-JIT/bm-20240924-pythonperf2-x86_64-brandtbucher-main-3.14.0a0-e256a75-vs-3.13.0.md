# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.00x faster
- HPT reliability: 78.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 311 ms: 1.07x slower                                              |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                            |
| html5lib       | 71.9 ms                                                      | 69.7 ms: 1.03x faster                                             |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                        | 1.04x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                              |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                              |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                              |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                              |
| async_tree_io              | 847 ms                                                       | 802 ms: 1.06x faster                                              |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.05x faster                                              |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                              |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                            |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                             |
| asyncio_websockets         | 382 ms                                                       | 393 ms: 1.03x slower                                              |
| async_generators           | 359 ms                                                       | 384 ms: 1.07x slower                                              |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                      |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 73.8 ms: 1.11x faster                                             |
| nbody          | 88.0 ms                                                      | 81.5 ms: 1.08x faster                                             |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                        | 1.06x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 233 ms: 1.04x faster                                              |
| regex_v8       | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                             |
| regex_effbot   | 3.37 ms                                                      | 3.39 ms: 1.01x slower                                             |
| regex_compile  | 144 ms                                                       | 149 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 55.9 ms: 1.09x faster                                             |
| xml_etree_generate   | 85.3 ms                                                      | 79.1 ms: 1.08x faster                                             |
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                             |
| xml_etree_iterparse  | 100 ms                                                       | 98.3 ms: 1.02x faster                                             |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                              |
| pickle_list          | 4.59 us                                                      | 4.55 us: 1.01x faster                                             |
| unpickle_list        | 4.62 us                                                      | 4.67 us: 1.01x slower                                             |
| json_loads           | 24.0 us                                                      | 24.2 us: 1.01x slower                                             |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                              |
| pickle_dict          | 32.1 us                                                      | 32.6 us: 1.02x slower                                             |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                             |
| pickle_pure_python   | 318 us                                                       | 331 us: 1.04x slower                                              |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.99 ms: 1.00x slower                                             |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                             |
| django_template | 38.9 ms                                                      | 43.3 ms: 1.12x slower                                             |
| genshi_xml      | 57.3 ms                                                      | 66.8 ms: 1.16x slower                                             |
| genshi_text     | 26.6 ms                                                      | 31.1 ms: 1.17x slower                                             |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 26.6 us: 1.48x faster                                             |
| deepcopy                   | 397 us                                                       | 297 us: 1.34x faster                                              |
| scimark_sor                | 126 ms                                                       | 105 ms: 1.20x faster                                              |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                             |
| spectral_norm              | 97.4 ms                                                      | 81.9 ms: 1.19x faster                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 390 ms: 1.18x faster                                              |
| richards                   | 52.7 ms                                                      | 44.8 ms: 1.18x faster                                             |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                              |
| richards_super             | 59.8 ms                                                      | 52.3 ms: 1.14x faster                                             |
| mako                       | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                             |
| tomli_loads                | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                            |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 3.81 ms: 1.12x faster                                             |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                              |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                             |
| float                      | 81.9 ms                                                      | 73.8 ms: 1.11x faster                                             |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                              |
| scimark_fft                | 314 ms                                                       | 288 ms: 1.09x faster                                              |
| xml_etree_process          | 60.9 ms                                                      | 55.9 ms: 1.09x faster                                             |
| nbody                      | 88.0 ms                                                      | 81.5 ms: 1.08x faster                                             |
| xml_etree_generate         | 85.3 ms                                                      | 79.1 ms: 1.08x faster                                             |
| go                         | 160 ms                                                       | 149 ms: 1.08x faster                                              |
| bpe_tokeniser              | 5.10 sec                                                     | 4.76 sec: 1.07x faster                                            |
| deltablue                  | 3.41 ms                                                      | 3.21 ms: 1.06x faster                                             |
| async_tree_io              | 847 ms                                                       | 802 ms: 1.06x faster                                              |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.05x faster                                              |
| regex_dna                  | 244 ms                                                       | 233 ms: 1.04x faster                                              |
| pyflate                    | 492 ms                                                       | 474 ms: 1.04x faster                                              |
| telco                      | 8.58 ms                                                      | 8.28 ms: 1.04x faster                                             |
| html5lib                   | 71.9 ms                                                      | 69.7 ms: 1.03x faster                                             |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                             |
| sqlite_synth               | 2.79 us                                                      | 2.71 us: 1.03x faster                                             |
| regex_v8                   | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                             |
| pprint_safe_repr           | 812 ms                                                       | 792 ms: 1.02x faster                                              |
| asyncio_tcp                | 380 ms                                                       | 372 ms: 1.02x faster                                              |
| crypto_pyaes               | 72.8 ms                                                      | 71.3 ms: 1.02x faster                                             |
| dulwich_log                | 65.5 ms                                                      | 64.2 ms: 1.02x faster                                             |
| xml_etree_iterparse        | 100 ms                                                       | 98.3 ms: 1.02x faster                                             |
| fannkuch                   | 365 ms                                                       | 360 ms: 1.01x faster                                              |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                              |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                              |
| pickle_list                | 4.59 us                                                      | 4.55 us: 1.01x faster                                             |
| scimark_lu                 | 97.8 ms                                                      | 97.3 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                            |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                              |
| python_startup_no_site     | 8.94 ms                                                      | 8.99 ms: 1.00x slower                                             |
| regex_effbot               | 3.37 ms                                                      | 3.39 ms: 1.01x slower                                             |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                             |
| json                       | 5.22 ms                                                      | 5.26 ms: 1.01x slower                                             |
| unpickle_list              | 4.62 us                                                      | 4.67 us: 1.01x slower                                             |
| json_loads                 | 24.0 us                                                      | 24.2 us: 1.01x slower                                             |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                              |
| coverage                   | 81.1 ms                                                      | 82.0 ms: 1.01x slower                                             |
| thrift                     | 877 us                                                       | 887 us: 1.01x slower                                              |
| logging_format             | 7.07 us                                                      | 7.17 us: 1.01x slower                                             |
| pickle_dict                | 32.1 us                                                      | 32.6 us: 1.02x slower                                             |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                             |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                              |
| bench_thread_pool          | 901 us                                                       | 921 us: 1.02x slower                                              |
| pycparser                  | 1.26 sec                                                     | 1.29 sec: 1.02x slower                                            |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.03x slower                                              |
| asyncio_websockets         | 382 ms                                                       | 393 ms: 1.03x slower                                              |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                            |
| regex_compile              | 144 ms                                                       | 149 ms: 1.03x slower                                              |
| logging_simple             | 6.40 us                                                      | 6.61 us: 1.03x slower                                             |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                              |
| sympy_str                  | 296 ms                                                       | 308 ms: 1.04x slower                                              |
| sympy_expand               | 505 ms                                                       | 528 ms: 1.05x slower                                              |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.2 ms: 1.05x slower                                             |
| comprehensions             | 17.3 us                                                      | 18.3 us: 1.06x slower                                             |
| 2to3                       | 291 ms                                                       | 311 ms: 1.07x slower                                              |
| async_generators           | 359 ms                                                       | 384 ms: 1.07x slower                                              |
| typing_runtime_protocols   | 174 us                                                       | 186 us: 1.07x slower                                              |
| chaos                      | 61.7 ms                                                      | 66.1 ms: 1.07x slower                                             |
| gc_traversal               | 4.11 ms                                                      | 4.41 ms: 1.07x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                             |
| sympy_sum                  | 154 ms                                                       | 168 ms: 1.09x slower                                              |
| hexiom                     | 6.33 ms                                                      | 6.92 ms: 1.09x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.95 ms: 1.09x slower                                             |
| raytrace                   | 289 ms                                                       | 318 ms: 1.10x slower                                              |
| sqlglot_optimize           | 59.7 ms                                                      | 65.7 ms: 1.10x slower                                             |
| sqlglot_normalize          | 118 ms                                                       | 131 ms: 1.10x slower                                              |
| nqueens                    | 88.2 ms                                                      | 98.3 ms: 1.11x slower                                             |
| django_template            | 38.9 ms                                                      | 43.3 ms: 1.12x slower                                             |
| bench_mp_pool              | 4.65 ms                                                      | 5.21 ms: 1.12x slower                                             |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                            |
| sympy_integrate            | 23.3 ms                                                      | 26.4 ms: 1.13x slower                                             |
| genshi_xml                 | 57.3 ms                                                      | 66.8 ms: 1.16x slower                                             |
| genshi_text                | 26.6 ms                                                      | 31.1 ms: 1.17x slower                                             |
| pylint                     | 346 ms                                                       | 410 ms: 1.18x slower                                              |
| generators                 | 33.5 ms                                                      | 42.5 ms: 1.27x slower                                             |
| unpack_sequence            | 56.8 ns                                                      | 88.0 ns: 1.55x slower                                             |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                      |

Benchmark hidden because not significant (3): async_tree_io_tg, unpickle, pprint_pformat
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 78.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x