# Results vs. 3.13.0b2

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.43x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 431 ms: 1.48x slower                                                           |
| docutils       | 2.98 sec                                                         | 3.48 sec: 1.17x slower                                                         |
| html5lib       | 74.7 ms                                                          | 109 ms: 1.46x slower                                                           |
| tornado_http   | 119 ms                                                           | 165 ms: 1.39x slower                                                           |
| Geometric mean | (ref)                                                            | 1.37x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 880 ms: 1.02x faster                                                           |
| async_tree_none_tg         | 340 ms                                                           | 360 ms: 1.06x slower                                                           |
| async_tree_io              | 873 ms                                                           | 940 ms: 1.08x slower                                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 626 ms: 1.09x slower                                                           |
| async_tree_memoization_tg  | 421 ms                                                           | 462 ms: 1.10x slower                                                           |
| async_tree_memoization     | 460 ms                                                           | 514 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 678 ms: 1.12x slower                                                           |
| async_tree_none            | 365 ms                                                           | 413 ms: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                            | 1.08x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 250 ms: 1.02x faster                                                           |
| float          | 80.2 ms                                                          | 142 ms: 1.77x slower                                                           |
| nbody          | 87.8 ms                                                          | 193 ms: 2.20x slower                                                           |
| Geometric mean | (ref)                                                            | 1.57x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 248 ms: 1.00x faster                                                           |
| regex_v8       | 26.0 ms                                                          | 27.4 ms: 1.05x slower                                                          |
| regex_effbot   | 3.40 ms                                                          | 3.65 ms: 1.07x slower                                                          |
| regex_compile  | 144 ms                                                           | 229 ms: 1.59x slower                                                           |
| Geometric mean | (ref)                                                            | 1.16x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                           | 138 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                           | 109 ms: 1.07x slower                                                           |
| json_loads           | 25.0 us                                                          | 30.0 us: 1.20x slower                                                          |
| json_dumps           | 10.8 ms                                                          | 14.1 ms: 1.31x slower                                                          |
| xml_etree_generate   | 85.7 ms                                                          | 118 ms: 1.38x slower                                                           |
| tomli_loads          | 2.40 sec                                                         | 3.32 sec: 1.38x slower                                                         |
| xml_etree_process    | 59.7 ms                                                          | 96.1 ms: 1.61x slower                                                          |
| unpickle_pure_python | 224 us                                                           | 409 us: 1.82x slower                                                           |
| pickle_pure_python   | 307 us                                                           | 594 us: 1.93x slower                                                           |
| Geometric mean       | (ref)                                                            | 1.37x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 17.1 ms: 1.30x slower                                                          |
| python_startup_no_site | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                          |
| Geometric mean         | (ref)                                                            | 1.31x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 82.9 ms: 1.43x slower                                                          |
| genshi_text     | 25.9 ms                                                          | 44.1 ms: 1.70x slower                                                          |
| django_template | 39.0 ms                                                          | 67.7 ms: 1.74x slower                                                          |
| mako            | 10.4 ms                                                          | 22.3 ms: 2.15x slower                                                          |
| Geometric mean  | (ref)                                                            | 1.73x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 3.27 ms: 1.43x faster                                                          |
| create_gc_cycles           | 2.00 ms                                                          | 1.68 ms: 1.19x faster                                                          |
| xml_etree_parse            | 144 ms                                                           | 138 ms: 1.04x faster                                                           |
| asyncio_websockets         | 395 ms                                                           | 384 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 900 ms                                                           | 880 ms: 1.02x faster                                                           |
| pidigits                   | 254 ms                                                           | 250 ms: 1.02x faster                                                           |
| regex_dna                  | 249 ms                                                           | 248 ms: 1.00x faster                                                           |
| regex_v8                   | 26.0 ms                                                          | 27.4 ms: 1.05x slower                                                          |
| async_tree_none_tg         | 340 ms                                                           | 360 ms: 1.06x slower                                                           |
| xml_etree_iterparse        | 103 ms                                                           | 109 ms: 1.07x slower                                                           |
| regex_effbot               | 3.40 ms                                                          | 3.65 ms: 1.07x slower                                                          |
| async_tree_io              | 873 ms                                                           | 940 ms: 1.08x slower                                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 626 ms: 1.09x slower                                                           |
| async_tree_memoization_tg  | 421 ms                                                           | 462 ms: 1.10x slower                                                           |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.77 sec: 1.12x slower                                                         |
| async_tree_memoization     | 460 ms                                                           | 514 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 678 ms: 1.12x slower                                                           |
| async_tree_none            | 365 ms                                                           | 413 ms: 1.13x slower                                                           |
| json                       | 5.35 ms                                                          | 6.15 ms: 1.15x slower                                                          |
| pathlib                    | 17.1 ms                                                          | 19.9 ms: 1.16x slower                                                          |
| docutils                   | 2.98 sec                                                         | 3.48 sec: 1.17x slower                                                         |
| asyncio_tcp                | 378 ms                                                           | 449 ms: 1.19x slower                                                           |
| deepcopy                   | 377 us                                                           | 451 us: 1.19x slower                                                           |
| json_loads                 | 25.0 us                                                          | 30.0 us: 1.20x slower                                                          |
| generators                 | 33.5 ms                                                          | 41.7 ms: 1.24x slower                                                          |
| coverage                   | 83.5 ms                                                          | 104 ms: 1.25x slower                                                           |
| telco                      | 8.40 ms                                                          | 10.5 ms: 1.25x slower                                                          |
| pylint                     | 339 ms                                                           | 432 ms: 1.27x slower                                                           |
| coroutines                 | 22.0 ms                                                          | 28.3 ms: 1.29x slower                                                          |
| python_startup             | 13.2 ms                                                          | 17.1 ms: 1.30x slower                                                          |
| bpe_tokeniser              | 5.14 sec                                                         | 6.69 sec: 1.30x slower                                                         |
| mdp                        | 2.46 sec                                                         | 3.21 sec: 1.31x slower                                                         |
| json_dumps                 | 10.8 ms                                                          | 14.1 ms: 1.31x slower                                                          |
| python_startup_no_site     | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                          |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.80 ms: 1.35x slower                                                          |
| meteor_contest             | 128 ms                                                           | 174 ms: 1.36x slower                                                           |
| scimark_fft                | 312 ms                                                           | 425 ms: 1.36x slower                                                           |
| xml_etree_generate         | 85.7 ms                                                          | 118 ms: 1.38x slower                                                           |
| async_generators           | 363 ms                                                           | 499 ms: 1.38x slower                                                           |
| tomli_loads                | 2.40 sec                                                         | 3.32 sec: 1.38x slower                                                         |
| tornado_http               | 119 ms                                                           | 165 ms: 1.39x slower                                                           |
| sympy_integrate            | 23.2 ms                                                          | 32.1 ms: 1.39x slower                                                          |
| deepcopy_reduce            | 3.39 us                                                          | 4.77 us: 1.41x slower                                                          |
| pycparser                  | 1.22 sec                                                         | 1.73 sec: 1.41x slower                                                         |
| deepcopy_memo              | 37.3 us                                                          | 53.0 us: 1.42x slower                                                          |
| genshi_xml                 | 58.1 ms                                                          | 82.9 ms: 1.43x slower                                                          |
| nqueens                    | 88.4 ms                                                          | 128 ms: 1.44x slower                                                           |
| html5lib                   | 74.7 ms                                                          | 109 ms: 1.46x slower                                                           |
| 2to3                       | 291 ms                                                           | 431 ms: 1.48x slower                                                           |
| richards                   | 53.4 ms                                                          | 80.8 ms: 1.51x slower                                                          |
| sympy_str                  | 295 ms                                                           | 453 ms: 1.54x slower                                                           |
| sqlglot_normalize          | 120 ms                                                           | 186 ms: 1.55x slower                                                           |
| sqlglot_optimize           | 59.5 ms                                                          | 93.5 ms: 1.57x slower                                                          |
| thrift                     | 880 us                                                           | 1.38 ms: 1.57x slower                                                          |
| pyflate                    | 482 ms                                                           | 763 ms: 1.59x slower                                                           |
| regex_compile              | 144 ms                                                           | 229 ms: 1.59x slower                                                           |
| xml_etree_process          | 59.7 ms                                                          | 96.1 ms: 1.61x slower                                                          |
| richards_super             | 61.2 ms                                                          | 98.7 ms: 1.61x slower                                                          |
| fannkuch                   | 353 ms                                                           | 569 ms: 1.61x slower                                                           |
| sympy_expand               | 501 ms                                                           | 819 ms: 1.64x slower                                                           |
| crypto_pyaes               | 73.6 ms                                                          | 121 ms: 1.64x slower                                                           |
| typing_runtime_protocols   | 171 us                                                           | 282 us: 1.66x slower                                                           |
| sympy_sum                  | 155 ms                                                           | 262 ms: 1.69x slower                                                           |
| genshi_text                | 25.9 ms                                                          | 44.1 ms: 1.70x slower                                                          |
| spectral_norm              | 97.3 ms                                                          | 166 ms: 1.71x slower                                                           |
| pprint_safe_repr           | 818 ms                                                           | 1.42 sec: 1.73x slower                                                         |
| django_template            | 39.0 ms                                                          | 67.7 ms: 1.74x slower                                                          |
| pprint_pformat             | 1.66 sec                                                         | 2.92 sec: 1.76x slower                                                         |
| logging_format             | 7.11 us                                                          | 12.6 us: 1.77x slower                                                          |
| comprehensions             | 17.0 us                                                          | 30.0 us: 1.77x slower                                                          |
| float                      | 80.2 ms                                                          | 142 ms: 1.77x slower                                                           |
| unpickle_pure_python       | 224 us                                                           | 409 us: 1.82x slower                                                           |
| logging_simple             | 6.40 us                                                          | 11.7 us: 1.83x slower                                                          |
| hexiom                     | 6.35 ms                                                          | 11.7 ms: 1.84x slower                                                          |
| bench_thread_pool          | 908 us                                                           | 1.71 ms: 1.88x slower                                                          |
| logging_silent             | 96.3 ns                                                          | 183 ns: 1.90x slower                                                           |
| sqlglot_transpile          | 1.76 ms                                                          | 3.40 ms: 1.93x slower                                                          |
| pickle_pure_python         | 307 us                                                           | 594 us: 1.93x slower                                                           |
| go                         | 165 ms                                                           | 330 ms: 2.00x slower                                                           |
| scimark_sor                | 119 ms                                                           | 240 ms: 2.02x slower                                                           |
| scimark_monte_carlo        | 65.5 ms                                                          | 134 ms: 2.04x slower                                                           |
| sqlglot_parse              | 1.39 ms                                                          | 2.87 ms: 2.06x slower                                                          |
| chaos                      | 59.6 ms                                                          | 124 ms: 2.07x slower                                                           |
| mako                       | 10.4 ms                                                          | 22.3 ms: 2.15x slower                                                          |
| nbody                      | 87.8 ms                                                          | 193 ms: 2.20x slower                                                           |
| raytrace                   | 260 ms                                                           | 599 ms: 2.30x slower                                                           |
| scimark_lu                 | 97.5 ms                                                          | 235 ms: 2.41x slower                                                           |
| deltablue                  | 3.37 ms                                                          | 8.25 ms: 2.44x slower                                                          |
| Geometric mean             | (ref)                                                            | 1.43x slower                                                                   |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.16x