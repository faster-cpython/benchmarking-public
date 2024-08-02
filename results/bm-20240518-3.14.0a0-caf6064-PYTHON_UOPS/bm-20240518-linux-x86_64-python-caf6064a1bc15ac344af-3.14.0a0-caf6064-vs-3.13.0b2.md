# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.36x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 379 ms: 1.38x slower                                                  |
| chameleon      | 7.22 ms                                                    | 8.87 ms: 1.23x slower                                                 |
| docutils       | 2.83 sec                                                   | 3.57 sec: 1.26x slower                                                |
| html5lib       | 67.2 ms                                                    | 85.0 ms: 1.26x slower                                                 |
| tornado_http   | 94.6 ms                                                    | 107 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                      | 1.25x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 624 ms: 1.06x slower                                                  |
| async_tree_io              | 939 ms                                                     | 998 ms: 1.06x slower                                                  |
| async_tree_none            | 378 ms                                                     | 409 ms: 1.08x slower                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 665 ms: 1.09x slower                                                  |
| async_tree_io_tg           | 936 ms                                                     | 1.05 sec: 1.12x slower                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 496 ms: 1.12x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 382 ms: 1.13x slower                                                  |
| async_tree_memoization     | 463 ms                                                     | 532 ms: 1.15x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.10x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 193 ms: 1.01x slower                                                  |
| float          | 78.9 ms                                                    | 131 ms: 1.66x slower                                                  |
| nbody          | 88.3 ms                                                    | 198 ms: 2.24x slower                                                  |
| Geometric mean | (ref)                                                      | 1.56x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 25.6 ms: 1.02x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                 |
| regex_compile  | 137 ms                                                     | 239 ms: 1.75x slower                                                  |
| Geometric mean | (ref)                                                      | 1.16x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 33.5 us: 1.04x faster                                                 |
| unpickle             | 15.1 us                                                    | 15.5 us: 1.02x slower                                                 |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| unpickle_list        | 5.34 us                                                    | 5.70 us: 1.07x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.54 us: 1.09x slower                                                 |
| json_dumps           | 10.7 ms                                                    | 11.7 ms: 1.09x slower                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 128 ms: 1.19x slower                                                  |
| xml_etree_process    | 61.2 ms                                                    | 80.1 ms: 1.31x slower                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 116 ms: 1.32x slower                                                  |
| tomli_loads          | 2.12 sec                                                   | 3.61 sec: 1.70x slower                                                |
| pickle_pure_python   | 305 us                                                     | 556 us: 1.82x slower                                                  |
| unpickle_pure_python | 218 us                                                     | 405 us: 1.86x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.21x slower                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 49.6 ms: 1.43x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 86.0 ms: 1.67x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 40.6 ms: 1.72x slower                                                 |
| mako            | 11.2 ms                                                    | 20.9 ms: 1.86x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.66x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| pickle_dict                | 34.8 us                                                    | 33.5 us: 1.04x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                 |
| pidigits                   | 191 ms                                                     | 193 ms: 1.01x slower                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.84 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.87 sec: 1.02x slower                                                |
| regex_v8                   | 25.1 ms                                                    | 25.6 ms: 1.02x slower                                                 |
| thrift                     | 823 us                                                     | 841 us: 1.02x slower                                                  |
| unpickle                   | 15.1 us                                                    | 15.5 us: 1.02x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                 |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| pathlib                    | 17.3 ms                                                    | 17.9 ms: 1.04x slower                                                 |
| sqlite_synth               | 2.99 us                                                    | 3.13 us: 1.05x slower                                                 |
| asyncio_tcp                | 508 ms                                                     | 532 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 624 ms: 1.06x slower                                                  |
| async_tree_io              | 939 ms                                                     | 998 ms: 1.06x slower                                                  |
| unpickle_list              | 5.34 us                                                    | 5.70 us: 1.07x slower                                                 |
| coroutines                 | 23.2 ms                                                    | 24.8 ms: 1.07x slower                                                 |
| flaskblogging              | 9.01 ms                                                    | 9.68 ms: 1.07x slower                                                 |
| async_tree_none            | 378 ms                                                     | 409 ms: 1.08x slower                                                  |
| dask                       | 369 ms                                                     | 400 ms: 1.08x slower                                                  |
| generators                 | 29.6 ms                                                    | 32.1 ms: 1.08x slower                                                 |
| json                       | 5.31 ms                                                    | 5.76 ms: 1.08x slower                                                 |
| pickle_list                | 5.11 us                                                    | 5.54 us: 1.09x slower                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 665 ms: 1.09x slower                                                  |
| json_dumps                 | 10.7 ms                                                    | 11.7 ms: 1.09x slower                                                 |
| mdp                        | 2.79 sec                                                   | 3.08 sec: 1.11x slower                                                |
| async_tree_io_tg           | 936 ms                                                     | 1.05 sec: 1.12x slower                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 496 ms: 1.12x slower                                                  |
| async_generators           | 442 ms                                                     | 499 ms: 1.13x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 382 ms: 1.13x slower                                                  |
| tornado_http               | 94.6 ms                                                    | 107 ms: 1.13x slower                                                  |
| async_tree_memoization     | 463 ms                                                     | 532 ms: 1.15x slower                                                  |
| dulwich_log                | 67.2 ms                                                    | 77.9 ms: 1.16x slower                                                 |
| logging_format             | 6.47 us                                                    | 7.54 us: 1.17x slower                                                 |
| logging_simple             | 5.74 us                                                    | 6.78 us: 1.18x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 128 ms: 1.19x slower                                                  |
| bench_thread_pool          | 834 us                                                     | 1.01 ms: 1.21x slower                                                 |
| chameleon                  | 7.22 ms                                                    | 8.87 ms: 1.23x slower                                                 |
| pylint                     | 317 ms                                                     | 391 ms: 1.23x slower                                                  |
| docutils                   | 2.83 sec                                                   | 3.57 sec: 1.26x slower                                                |
| html5lib                   | 67.2 ms                                                    | 85.0 ms: 1.26x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 213 us: 1.30x slower                                                  |
| sympy_expand               | 473 ms                                                     | 614 ms: 1.30x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 203 ms: 1.30x slower                                                  |
| xml_etree_process          | 61.2 ms                                                    | 80.1 ms: 1.31x slower                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 4.41 us: 1.32x slower                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 116 ms: 1.32x slower                                                  |
| sympy_str                  | 282 ms                                                     | 379 ms: 1.34x slower                                                  |
| meteor_contest             | 110 ms                                                     | 148 ms: 1.35x slower                                                  |
| 2to3                       | 274 ms                                                     | 379 ms: 1.38x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 28.5 ms: 1.39x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 77.5 ms: 1.40x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.62 sec: 1.40x slower                                                |
| scimark_sor                | 127 ms                                                     | 179 ms: 1.41x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 156 ms: 1.42x slower                                                  |
| raytrace                   | 267 ms                                                     | 379 ms: 1.42x slower                                                  |
| django_template            | 34.8 ms                                                    | 49.6 ms: 1.43x slower                                                 |
| scimark_fft                | 392 ms                                                     | 599 ms: 1.53x slower                                                  |
| deepcopy                   | 367 us                                                     | 561 us: 1.53x slower                                                  |
| go                         | 145 ms                                                     | 222 ms: 1.53x slower                                                  |
| richards_super             | 57.4 ms                                                    | 88.7 ms: 1.55x slower                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 2.61 ms: 1.60x slower                                                 |
| richards                   | 50.9 ms                                                    | 81.7 ms: 1.60x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 2.15 ms: 1.63x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 200 ms: 1.65x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 5.36 ms: 1.65x slower                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 128 ms: 1.66x slower                                                  |
| float                      | 78.9 ms                                                    | 131 ms: 1.66x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 86.0 ms: 1.67x slower                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 8.96 ms: 1.70x slower                                                 |
| tomli_loads                | 2.12 sec                                                   | 3.61 sec: 1.70x slower                                                |
| pprint_safe_repr           | 758 ms                                                     | 1.30 sec: 1.71x slower                                                |
| genshi_text                | 23.7 ms                                                    | 40.6 ms: 1.72x slower                                                 |
| pprint_pformat             | 1.56 sec                                                   | 2.69 sec: 1.73x slower                                                |
| regex_compile              | 137 ms                                                     | 239 ms: 1.75x slower                                                  |
| pyflate                    | 484 ms                                                     | 849 ms: 1.75x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 144 ms: 1.77x slower                                                  |
| fannkuch                   | 402 ms                                                     | 726 ms: 1.81x slower                                                  |
| chaos                      | 61.3 ms                                                    | 111 ms: 1.81x slower                                                  |
| pickle_pure_python         | 305 us                                                     | 556 us: 1.82x slower                                                  |
| mako                       | 11.2 ms                                                    | 20.9 ms: 1.86x slower                                                 |
| unpickle_pure_python       | 218 us                                                     | 405 us: 1.86x slower                                                  |
| spectral_norm              | 116 ms                                                     | 223 ms: 1.92x slower                                                  |
| deepcopy_memo              | 39.7 us                                                    | 77.9 us: 1.96x slower                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 136 ms: 1.97x slower                                                  |
| logging_silent             | 105 ns                                                     | 223 ns: 2.13x slower                                                  |
| nbody                      | 88.3 ms                                                    | 198 ms: 2.24x slower                                                  |
| comprehensions             | 16.6 us                                                    | 38.1 us: 2.29x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 15.2 ms: 2.42x slower                                                 |
| telco                      | 8.41 ms                                                    | 182 ms: 21.64x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.36x slower                                                          |

Benchmark hidden because not significant (3): json_loads, coverage, asyncio_websockets
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 1.01x