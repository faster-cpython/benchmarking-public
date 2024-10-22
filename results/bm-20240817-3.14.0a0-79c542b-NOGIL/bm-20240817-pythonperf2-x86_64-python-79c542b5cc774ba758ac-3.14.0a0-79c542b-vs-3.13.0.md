# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.46x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 442 ms: 1.52x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.52 sec: 1.25x slower                                                      |
| html5lib       | 71.9 ms                                                      | 110 ms: 1.53x slower                                                        |
| tornado_http   | 120 ms                                                       | 170 ms: 1.42x slower                                                        |
| Geometric mean | (ref)                                                        | 1.43x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 479 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 634 ms: 1.10x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.77 sec: 1.12x slower                                                      |
| async_tree_io_tg           | 819 ms                                                       | 920 ms: 1.12x slower                                                        |
| async_tree_io              | 847 ms                                                       | 964 ms: 1.14x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 387 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 688 ms: 1.15x slower                                                        |
| async_tree_none            | 372 ms                                                       | 428 ms: 1.15x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 533 ms: 1.18x slower                                                        |
| asyncio_tcp                | 380 ms                                                       | 452 ms: 1.19x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 30.5 ms: 1.41x slower                                                       |
| async_generators           | 359 ms                                                       | 511 ms: 1.42x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| float          | 81.9 ms                                                      | 143 ms: 1.75x slower                                                        |
| nbody          | 88.0 ms                                                      | 196 ms: 2.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.57x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 255 ms: 1.05x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.59 ms: 1.07x slower                                                       |
| regex_v8       | 26.2 ms                                                      | 28.5 ms: 1.09x slower                                                       |
| regex_compile  | 144 ms                                                       | 234 ms: 1.62x slower                                                        |
| Geometric mean | (ref)                                                        | 1.18x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 140 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 112 ms: 1.12x slower                                                        |
| json_loads           | 24.0 us                                                      | 30.1 us: 1.26x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 14.6 ms: 1.34x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 116 ms: 1.36x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.43 sec: 1.43x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 95.7 ms: 1.57x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 608 us: 1.91x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 427 us: 1.99x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.40x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 17.3 ms: 1.30x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 11.9 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 84.2 ms: 1.47x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 43.4 ms: 1.63x slower                                                       |
| django_template | 38.9 ms                                                      | 68.4 ms: 1.76x slower                                                       |
| mako            | 10.4 ms                                                      | 21.8 ms: 2.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.72x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 2.90 ms: 1.42x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.70 ms: 1.04x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 140 ms: 1.03x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 479 ms: 1.04x slower                                                        |
| regex_dna                  | 244 ms                                                       | 255 ms: 1.05x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.95 ms: 1.06x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.59 ms: 1.07x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 28.5 ms: 1.09x slower                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 634 ms: 1.10x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 112 ms: 1.12x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.77 sec: 1.12x slower                                                      |
| async_tree_io_tg           | 819 ms                                                       | 920 ms: 1.12x slower                                                        |
| deepcopy                   | 397 us                                                       | 450 us: 1.13x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.8 ms: 1.14x slower                                                       |
| async_tree_io              | 847 ms                                                       | 964 ms: 1.14x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 387 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 688 ms: 1.15x slower                                                        |
| async_tree_none            | 372 ms                                                       | 428 ms: 1.15x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 533 ms: 1.18x slower                                                        |
| json                       | 5.22 ms                                                      | 6.19 ms: 1.18x slower                                                       |
| asyncio_tcp                | 380 ms                                                       | 452 ms: 1.19x slower                                                        |
| telco                      | 8.58 ms                                                      | 10.7 ms: 1.25x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.52 sec: 1.25x slower                                                      |
| scimark_fft                | 314 ms                                                       | 394 ms: 1.25x slower                                                        |
| json_loads                 | 24.0 us                                                      | 30.1 us: 1.26x slower                                                       |
| generators                 | 33.5 ms                                                      | 42.4 ms: 1.27x slower                                                       |
| pylint                     | 346 ms                                                       | 440 ms: 1.27x slower                                                        |
| mdp                        | 2.52 sec                                                     | 3.25 sec: 1.29x slower                                                      |
| python_startup             | 13.3 ms                                                      | 17.3 ms: 1.30x slower                                                       |
| deepcopy_memo              | 39.5 us                                                      | 51.7 us: 1.31x slower                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.65 ms: 1.32x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 11.9 ms: 1.33x slower                                                       |
| json_dumps                 | 11.0 ms                                                      | 14.6 ms: 1.34x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 6.88 sec: 1.35x slower                                                      |
| deepcopy_reduce            | 3.54 us                                                      | 4.78 us: 1.35x slower                                                       |
| meteor_contest             | 128 ms                                                       | 174 ms: 1.35x slower                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 116 ms: 1.36x slower                                                        |
| coverage                   | 81.1 ms                                                      | 110 ms: 1.36x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.76 sec: 1.40x slower                                                      |
| sympy_integrate            | 23.3 ms                                                      | 32.9 ms: 1.41x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 30.5 ms: 1.41x slower                                                       |
| tornado_http               | 120 ms                                                       | 170 ms: 1.42x slower                                                        |
| async_generators           | 359 ms                                                       | 511 ms: 1.42x slower                                                        |
| tomli_loads                | 2.41 sec                                                     | 3.43 sec: 1.43x slower                                                      |
| genshi_xml                 | 57.3 ms                                                      | 84.2 ms: 1.47x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 130 ms: 1.48x slower                                                        |
| 2to3                       | 291 ms                                                       | 442 ms: 1.52x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 110 ms: 1.53x slower                                                        |
| sympy_str                  | 296 ms                                                       | 462 ms: 1.56x slower                                                        |
| xml_etree_process          | 60.9 ms                                                      | 95.7 ms: 1.57x slower                                                       |
| thrift                     | 877 us                                                       | 1.39 ms: 1.58x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 189 ms: 1.59x slower                                                        |
| pyflate                    | 492 ms                                                       | 785 ms: 1.60x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 279 us: 1.61x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 95.9 ms: 1.61x slower                                                       |
| regex_compile              | 144 ms                                                       | 234 ms: 1.62x slower                                                        |
| richards                   | 52.7 ms                                                      | 85.7 ms: 1.62x slower                                                       |
| fannkuch                   | 365 ms                                                       | 593 ms: 1.62x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 43.4 ms: 1.63x slower                                                       |
| sympy_expand               | 505 ms                                                       | 837 ms: 1.66x slower                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 122 ms: 1.68x slower                                                        |
| spectral_norm              | 97.4 ms                                                      | 165 ms: 1.69x slower                                                        |
| richards_super             | 59.8 ms                                                      | 103 ms: 1.72x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 266 ms: 1.73x slower                                                        |
| float                      | 81.9 ms                                                      | 143 ms: 1.75x slower                                                        |
| django_template            | 38.9 ms                                                      | 68.4 ms: 1.76x slower                                                       |
| comprehensions             | 17.3 us                                                      | 30.9 us: 1.79x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 1.47 sec: 1.81x slower                                                      |
| logging_format             | 7.07 us                                                      | 12.9 us: 1.82x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 3.04 sec: 1.85x slower                                                      |
| logging_simple             | 6.40 us                                                      | 11.9 us: 1.86x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 1.70 ms: 1.89x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 608 us: 1.91x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 12.2 ms: 1.92x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 3.42 ms: 1.92x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 427 us: 1.99x slower                                                        |
| chaos                      | 61.7 ms                                                      | 126 ms: 2.04x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 202 ns: 2.06x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 135 ms: 2.08x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.88 ms: 2.09x slower                                                       |
| mako                       | 10.4 ms                                                      | 21.8 ms: 2.09x slower                                                       |
| scimark_sor                | 126 ms                                                       | 266 ms: 2.12x slower                                                        |
| raytrace                   | 289 ms                                                       | 626 ms: 2.17x slower                                                        |
| go                         | 160 ms                                                       | 351 ms: 2.18x slower                                                        |
| nbody                      | 88.0 ms                                                      | 196 ms: 2.22x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 238 ms: 2.43x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.55 ms: 2.51x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.46x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.32x

# Memory
- memory change: 1.17x