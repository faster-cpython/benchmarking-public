# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: adf0b94
- commit date: 2024-07-19
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 342 ms: 1.18x slower                                        |
| docutils       | 2.81 sec                                                     | 3.43 sec: 1.22x slower                                      |
| html5lib       | 71.9 ms                                                      | 83.0 ms: 1.15x slower                                       |
| tornado_http   | 120 ms                                                       | 127 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 399 ms: 1.16x faster                                        |
| async_tree_none_tg         | 340 ms                                                       | 318 ms: 1.07x faster                                        |
| async_tree_memoization     | 452 ms                                                       | 425 ms: 1.06x faster                                        |
| async_tree_none            | 372 ms                                                       | 356 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.61 sec: 1.02x slower                                      |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                        |
| asyncio_tcp                | 380 ms                                                       | 392 ms: 1.03x slower                                        |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                       |
| async_generators           | 359 ms                                                       | 388 ms: 1.08x slower                                        |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 254 ms: 1.00x slower                                        |
| float          | 81.9 ms                                                      | 91.6 ms: 1.12x slower                                       |
| nbody          | 88.0 ms                                                      | 127 ms: 1.44x slower                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                       |
| regex_effbot   | 3.37 ms                                                      | 3.65 ms: 1.08x slower                                       |
| regex_compile  | 144 ms                                                       | 213 ms: 1.47x slower                                        |
| Geometric mean | (ref)                                                        | 1.12x slower                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 11.4 ms: 1.04x slower                                       |
| json_loads           | 24.0 us                                                      | 25.5 us: 1.06x slower                                       |
| xml_etree_process    | 60.9 ms                                                      | 68.7 ms: 1.13x slower                                       |
| xml_etree_iterparse  | 100 ms                                                       | 114 ms: 1.14x slower                                        |
| xml_etree_generate   | 85.3 ms                                                      | 97.8 ms: 1.15x slower                                       |
| tomli_loads          | 2.41 sec                                                     | 2.90 sec: 1.21x slower                                      |
| pickle_pure_python   | 318 us                                                       | 427 us: 1.34x slower                                        |
| unpickle_pure_python | 214 us                                                       | 301 us: 1.40x slower                                        |
| Geometric mean       | (ref)                                                        | 1.16x slower                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.14 ms: 1.02x slower                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 66.8 ms: 1.16x slower                                       |
| django_template | 38.9 ms                                                      | 46.3 ms: 1.19x slower                                       |
| genshi_text     | 26.6 ms                                                      | 32.8 ms: 1.23x slower                                       |
| mako            | 10.4 ms                                                      | 14.5 ms: 1.39x slower                                       |
| Geometric mean  | (ref)                                                        | 1.24x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 399 ms: 1.16x faster                                        |
| deepcopy                   | 397 us                                                       | 351 us: 1.13x faster                                        |
| generators                 | 33.5 ms                                                      | 30.2 ms: 1.11x faster                                       |
| async_tree_none_tg         | 340 ms                                                       | 318 ms: 1.07x faster                                        |
| async_tree_memoization     | 452 ms                                                       | 425 ms: 1.06x faster                                        |
| pathlib                    | 17.4 ms                                                      | 16.7 ms: 1.05x faster                                       |
| async_tree_none            | 372 ms                                                       | 356 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.47 us: 1.02x faster                                       |
| coverage                   | 81.1 ms                                                      | 80.0 ms: 1.01x faster                                       |
| regex_v8                   | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                       |
| pidigits                   | 253 ms                                                       | 254 ms: 1.00x slower                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.61 sec: 1.02x slower                                      |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.14 ms: 1.02x slower                                       |
| asyncio_tcp                | 380 ms                                                       | 392 ms: 1.03x slower                                        |
| thrift                     | 877 us                                                       | 905 us: 1.03x slower                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.82 ms: 1.03x slower                                       |
| logging_format             | 7.07 us                                                      | 7.33 us: 1.04x slower                                       |
| logging_simple             | 6.40 us                                                      | 6.65 us: 1.04x slower                                       |
| json_dumps                 | 11.0 ms                                                      | 11.4 ms: 1.04x slower                                       |
| tornado_http               | 120 ms                                                       | 127 ms: 1.06x slower                                        |
| json_loads                 | 24.0 us                                                      | 25.5 us: 1.06x slower                                       |
| telco                      | 8.58 ms                                                      | 9.17 ms: 1.07x slower                                       |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                       |
| async_generators           | 359 ms                                                       | 388 ms: 1.08x slower                                        |
| regex_effbot               | 3.37 ms                                                      | 3.65 ms: 1.08x slower                                       |
| mdp                        | 2.52 sec                                                     | 2.74 sec: 1.09x slower                                      |
| richards_super             | 59.8 ms                                                      | 65.2 ms: 1.09x slower                                       |
| gc_traversal               | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                       |
| bench_thread_pool          | 901 us                                                       | 987 us: 1.09x slower                                        |
| richards                   | 52.7 ms                                                      | 57.9 ms: 1.10x slower                                       |
| pylint                     | 346 ms                                                       | 383 ms: 1.11x slower                                        |
| json                       | 5.22 ms                                                      | 5.78 ms: 1.11x slower                                       |
| dask                       | 379 ms                                                       | 421 ms: 1.11x slower                                        |
| raytrace                   | 289 ms                                                       | 322 ms: 1.12x slower                                        |
| float                      | 81.9 ms                                                      | 91.6 ms: 1.12x slower                                       |
| xml_etree_process          | 60.9 ms                                                      | 68.7 ms: 1.13x slower                                       |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 5.82 sec: 1.14x slower                                      |
| xml_etree_iterparse        | 100 ms                                                       | 114 ms: 1.14x slower                                        |
| xml_etree_generate         | 85.3 ms                                                      | 97.8 ms: 1.15x slower                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                       |
| html5lib                   | 71.9 ms                                                      | 83.0 ms: 1.15x slower                                       |
| pycparser                  | 1.26 sec                                                     | 1.45 sec: 1.16x slower                                      |
| genshi_xml                 | 57.3 ms                                                      | 66.8 ms: 1.16x slower                                       |
| typing_runtime_protocols   | 174 us                                                       | 203 us: 1.17x slower                                        |
| 2to3                       | 291 ms                                                       | 342 ms: 1.18x slower                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 70.6 ms: 1.18x slower                                       |
| sqlglot_normalize          | 118 ms                                                       | 140 ms: 1.19x slower                                        |
| dulwich_log                | 65.5 ms                                                      | 77.8 ms: 1.19x slower                                       |
| django_template            | 38.9 ms                                                      | 46.3 ms: 1.19x slower                                       |
| sympy_integrate            | 23.3 ms                                                      | 28.1 ms: 1.20x slower                                       |
| tomli_loads                | 2.41 sec                                                     | 2.90 sec: 1.21x slower                                      |
| docutils                   | 2.81 sec                                                     | 3.43 sec: 1.22x slower                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 2.19 ms: 1.23x slower                                       |
| genshi_text                | 26.6 ms                                                      | 32.8 ms: 1.23x slower                                       |
| sympy_sum                  | 154 ms                                                       | 190 ms: 1.24x slower                                        |
| sympy_expand               | 505 ms                                                       | 628 ms: 1.24x slower                                        |
| deltablue                  | 3.41 ms                                                      | 4.25 ms: 1.25x slower                                       |
| sympy_str                  | 296 ms                                                       | 370 ms: 1.25x slower                                        |
| pyflate                    | 492 ms                                                       | 616 ms: 1.25x slower                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.73 ms: 1.25x slower                                       |
| go                         | 160 ms                                                       | 202 ms: 1.26x slower                                        |
| deepcopy_memo              | 39.5 us                                                      | 50.0 us: 1.27x slower                                       |
| pprint_safe_repr           | 812 ms                                                       | 1.04 sec: 1.28x slower                                      |
| crypto_pyaes               | 72.8 ms                                                      | 93.4 ms: 1.28x slower                                       |
| scimark_sor                | 126 ms                                                       | 161 ms: 1.28x slower                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.13 sec: 1.29x slower                                      |
| chaos                      | 61.7 ms                                                      | 79.5 ms: 1.29x slower                                       |
| nqueens                    | 88.2 ms                                                      | 114 ms: 1.29x slower                                        |
| pickle_pure_python         | 318 us                                                       | 427 us: 1.34x slower                                        |
| fannkuch                   | 365 ms                                                       | 500 ms: 1.37x slower                                        |
| scimark_fft                | 314 ms                                                       | 433 ms: 1.38x slower                                        |
| mako                       | 10.4 ms                                                      | 14.5 ms: 1.39x slower                                       |
| unpickle_pure_python       | 214 us                                                       | 301 us: 1.40x slower                                        |
| nbody                      | 88.0 ms                                                      | 127 ms: 1.44x slower                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 94.4 ms: 1.45x slower                                       |
| scimark_lu                 | 97.8 ms                                                      | 144 ms: 1.47x slower                                        |
| regex_compile              | 144 ms                                                       | 213 ms: 1.47x slower                                        |
| spectral_norm              | 97.4 ms                                                      | 150 ms: 1.54x slower                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 6.81 ms: 1.59x slower                                       |
| comprehensions             | 17.3 us                                                      | 27.6 us: 1.60x slower                                       |
| logging_silent             | 97.7 ns                                                      | 157 ns: 1.61x slower                                        |
| hexiom                     | 6.33 ms                                                      | 10.5 ms: 1.65x slower                                       |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                |

Benchmark hidden because not significant (5): async_tree_io, xml_etree_parse, regex_dna, async_tree_cpu_io_mixed, async_tree_io_tg
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.02x