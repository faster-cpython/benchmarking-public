# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 6b9055c
- commit date: 2024-08-14
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 353 ms: 1.21x slower                                                                |
| docutils       | 2.81 sec                                                     | 3.54 sec: 1.26x slower                                                              |
| html5lib       | 71.9 ms                                                      | 85.2 ms: 1.18x slower                                                               |
| tornado_http   | 120 ms                                                       | 127 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                        | 1.18x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 404 ms: 1.14x faster                                                                |
| async_tree_none            | 372 ms                                                       | 348 ms: 1.07x faster                                                                |
| async_tree_none_tg         | 340 ms                                                       | 320 ms: 1.06x faster                                                                |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                                |
| async_tree_memoization     | 452 ms                                                       | 443 ms: 1.02x faster                                                                |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.60 sec: 1.01x slower                                                              |
| asyncio_tcp                | 380 ms                                                       | 388 ms: 1.02x slower                                                                |
| asyncio_websockets         | 382 ms                                                       | 398 ms: 1.04x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                               |
| async_generators           | 359 ms                                                       | 385 ms: 1.07x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                        |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 255 ms: 1.01x slower                                                                |
| float          | 81.9 ms                                                      | 93.8 ms: 1.15x slower                                                               |
| nbody          | 88.0 ms                                                      | 128 ms: 1.45x slower                                                                |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 240 ms: 1.01x faster                                                                |
| regex_v8       | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                               |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                               |
| regex_compile  | 144 ms                                                       | 208 ms: 1.44x slower                                                                |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                                |
| json_loads           | 24.0 us                                                      | 25.6 us: 1.07x slower                                                               |
| json_dumps           | 11.0 ms                                                      | 11.9 ms: 1.09x slower                                                               |
| xml_etree_process    | 60.9 ms                                                      | 70.0 ms: 1.15x slower                                                               |
| xml_etree_iterparse  | 100 ms                                                       | 116 ms: 1.16x slower                                                                |
| xml_etree_generate   | 85.3 ms                                                      | 101 ms: 1.18x slower                                                                |
| tomli_loads          | 2.41 sec                                                     | 2.87 sec: 1.19x slower                                                              |
| unpickle_pure_python | 214 us                                                       | 272 us: 1.27x slower                                                                |
| pickle_pure_python   | 318 us                                                       | 410 us: 1.29x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.15x slower                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                               |
| python_startup_no_site | 8.94 ms                                                      | 9.12 ms: 1.02x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.9 ms                                                      | 44.4 ms: 1.14x slower                                                               |
| genshi_xml      | 57.3 ms                                                      | 65.7 ms: 1.15x slower                                                               |
| genshi_text     | 26.6 ms                                                      | 30.8 ms: 1.16x slower                                                               |
| mako            | 10.4 ms                                                      | 14.6 ms: 1.40x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 404 ms: 1.14x faster                                                                |
| deepcopy                   | 397 us                                                       | 355 us: 1.12x faster                                                                |
| deepcopy_reduce            | 3.54 us                                                      | 3.23 us: 1.10x faster                                                               |
| async_tree_none            | 372 ms                                                       | 348 ms: 1.07x faster                                                                |
| async_tree_none_tg         | 340 ms                                                       | 320 ms: 1.06x faster                                                                |
| pathlib                    | 17.4 ms                                                      | 16.8 ms: 1.04x faster                                                               |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                                |
| async_tree_memoization     | 452 ms                                                       | 443 ms: 1.02x faster                                                                |
| regex_dna                  | 244 ms                                                       | 240 ms: 1.01x faster                                                                |
| coverage                   | 81.1 ms                                                      | 80.0 ms: 1.01x faster                                                               |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                                |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                               |
| pidigits                   | 253 ms                                                       | 255 ms: 1.01x slower                                                                |
| thrift                     | 877 us                                                       | 886 us: 1.01x slower                                                                |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.60 sec: 1.01x slower                                                              |
| python_startup_no_site     | 8.94 ms                                                      | 9.12 ms: 1.02x slower                                                               |
| asyncio_tcp                | 380 ms                                                       | 388 ms: 1.02x slower                                                                |
| regex_v8                   | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                               |
| logging_format             | 7.07 us                                                      | 7.27 us: 1.03x slower                                                               |
| asyncio_websockets         | 382 ms                                                       | 398 ms: 1.04x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                               |
| telco                      | 8.58 ms                                                      | 8.95 ms: 1.04x slower                                                               |
| logging_simple             | 6.40 us                                                      | 6.67 us: 1.04x slower                                                               |
| tornado_http               | 120 ms                                                       | 127 ms: 1.06x slower                                                                |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                               |
| json_loads                 | 24.0 us                                                      | 25.6 us: 1.07x slower                                                               |
| async_generators           | 359 ms                                                       | 385 ms: 1.07x slower                                                                |
| bench_mp_pool              | 4.65 ms                                                      | 4.99 ms: 1.07x slower                                                               |
| json_dumps                 | 11.0 ms                                                      | 11.9 ms: 1.09x slower                                                               |
| bench_thread_pool          | 901 us                                                       | 982 us: 1.09x slower                                                                |
| json                       | 5.22 ms                                                      | 5.78 ms: 1.11x slower                                                               |
| mdp                        | 2.52 sec                                                     | 2.80 sec: 1.11x slower                                                              |
| raytrace                   | 289 ms                                                       | 325 ms: 1.13x slower                                                                |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                                                |
| bpe_tokeniser              | 5.10 sec                                                     | 5.77 sec: 1.13x slower                                                              |
| django_template            | 38.9 ms                                                      | 44.4 ms: 1.14x slower                                                               |
| float                      | 81.9 ms                                                      | 93.8 ms: 1.15x slower                                                               |
| genshi_xml                 | 57.3 ms                                                      | 65.7 ms: 1.15x slower                                                               |
| typing_runtime_protocols   | 174 us                                                       | 200 us: 1.15x slower                                                                |
| xml_etree_process          | 60.9 ms                                                      | 70.0 ms: 1.15x slower                                                               |
| xml_etree_iterparse        | 100 ms                                                       | 116 ms: 1.16x slower                                                                |
| gc_traversal               | 4.11 ms                                                      | 4.76 ms: 1.16x slower                                                               |
| genshi_text                | 26.6 ms                                                      | 30.8 ms: 1.16x slower                                                               |
| create_gc_cycles           | 1.76 ms                                                      | 2.04 ms: 1.16x slower                                                               |
| xml_etree_generate         | 85.3 ms                                                      | 101 ms: 1.18x slower                                                                |
| html5lib                   | 71.9 ms                                                      | 85.2 ms: 1.18x slower                                                               |
| pylint                     | 346 ms                                                       | 411 ms: 1.19x slower                                                                |
| richards_super             | 59.8 ms                                                      | 71.2 ms: 1.19x slower                                                               |
| tomli_loads                | 2.41 sec                                                     | 2.87 sec: 1.19x slower                                                              |
| sqlglot_normalize          | 118 ms                                                       | 142 ms: 1.20x slower                                                                |
| deepcopy_memo              | 39.5 us                                                      | 47.5 us: 1.20x slower                                                               |
| richards                   | 52.7 ms                                                      | 63.6 ms: 1.21x slower                                                               |
| 2to3                       | 291 ms                                                       | 353 ms: 1.21x slower                                                                |
| sqlglot_optimize           | 59.7 ms                                                      | 72.5 ms: 1.21x slower                                                               |
| sympy_integrate            | 23.3 ms                                                      | 28.5 ms: 1.22x slower                                                               |
| pycparser                  | 1.26 sec                                                     | 1.54 sec: 1.23x slower                                                              |
| sqlglot_transpile          | 1.78 ms                                                      | 2.21 ms: 1.24x slower                                                               |
| sympy_expand               | 505 ms                                                       | 626 ms: 1.24x slower                                                                |
| go                         | 160 ms                                                       | 199 ms: 1.24x slower                                                                |
| sympy_sum                  | 154 ms                                                       | 192 ms: 1.25x slower                                                                |
| pyflate                    | 492 ms                                                       | 613 ms: 1.25x slower                                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.73 ms: 1.25x slower                                                               |
| sympy_str                  | 296 ms                                                       | 373 ms: 1.26x slower                                                                |
| docutils                   | 2.81 sec                                                     | 3.54 sec: 1.26x slower                                                              |
| pprint_safe_repr           | 812 ms                                                       | 1.03 sec: 1.27x slower                                                              |
| unpickle_pure_python       | 214 us                                                       | 272 us: 1.27x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 2.11 sec: 1.28x slower                                                              |
| pickle_pure_python         | 318 us                                                       | 410 us: 1.29x slower                                                                |
| scimark_lu                 | 97.8 ms                                                      | 127 ms: 1.30x slower                                                                |
| chaos                      | 61.7 ms                                                      | 80.0 ms: 1.30x slower                                                               |
| crypto_pyaes               | 72.8 ms                                                      | 95.2 ms: 1.31x slower                                                               |
| nqueens                    | 88.2 ms                                                      | 116 ms: 1.32x slower                                                                |
| generators                 | 33.5 ms                                                      | 45.3 ms: 1.35x slower                                                               |
| scimark_fft                | 314 ms                                                       | 426 ms: 1.36x slower                                                                |
| fannkuch                   | 365 ms                                                       | 496 ms: 1.36x slower                                                                |
| mako                       | 10.4 ms                                                      | 14.6 ms: 1.40x slower                                                               |
| scimark_sor                | 126 ms                                                       | 181 ms: 1.44x slower                                                                |
| scimark_monte_carlo        | 64.9 ms                                                      | 93.7 ms: 1.44x slower                                                               |
| regex_compile              | 144 ms                                                       | 208 ms: 1.44x slower                                                                |
| nbody                      | 88.0 ms                                                      | 128 ms: 1.45x slower                                                                |
| deltablue                  | 3.41 ms                                                      | 5.24 ms: 1.54x slower                                                               |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 6.62 ms: 1.54x slower                                                               |
| logging_silent             | 97.7 ns                                                      | 154 ns: 1.57x slower                                                                |
| comprehensions             | 17.3 us                                                      | 27.2 us: 1.57x slower                                                               |
| spectral_norm              | 97.4 ms                                                      | 155 ms: 1.59x slower                                                                |
| hexiom                     | 6.33 ms                                                      | 10.4 ms: 1.65x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                        |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.02x