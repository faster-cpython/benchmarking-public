# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.41x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 394 ms: 1.44x slower                                                  |
| docutils       | 2.83 sec                                                   | 3.35 sec: 1.19x slower                                                |
| html5lib       | 67.2 ms                                                    | 97.3 ms: 1.45x slower                                                 |
| tornado_http   | 94.6 ms                                                    | 136 ms: 1.44x slower                                                  |
| Geometric mean | (ref)                                                      | 1.37x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                                  |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 597 ms: 1.02x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 346 ms: 1.03x slower                                                  |
| async_tree_none            | 378 ms                                                     | 406 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 662 ms: 1.08x slower                                                  |
| async_tree_memoization     | 463 ms                                                     | 510 ms: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 184 ms: 1.04x faster                                                  |
| float          | 78.9 ms                                                    | 142 ms: 1.80x slower                                                  |
| nbody          | 88.3 ms                                                    | 217 ms: 2.46x slower                                                  |
| Geometric mean | (ref)                                                      | 1.62x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                                 |
| regex_compile  | 137 ms                                                     | 217 ms: 1.59x slower                                                  |
| Geometric mean | (ref)                                                      | 1.13x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 142 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 111 ms: 1.03x slower                                                  |
| json_loads           | 28.9 us                                                    | 32.2 us: 1.11x slower                                                 |
| json_dumps           | 10.7 ms                                                    | 13.4 ms: 1.25x slower                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 111 ms: 1.27x slower                                                  |
| xml_etree_process    | 61.2 ms                                                    | 89.5 ms: 1.46x slower                                                 |
| tomli_loads          | 2.12 sec                                                   | 3.22 sec: 1.52x slower                                                |
| unpickle_pure_python | 218 us                                                     | 399 us: 1.83x slower                                                  |
| pickle_pure_python   | 305 us                                                     | 571 us: 1.87x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.32x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 13.4 ms: 1.25x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 9.08 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.26x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 83.9 ms: 1.62x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 40.2 ms: 1.70x slower                                                 |
| django_template | 34.8 ms                                                    | 60.9 ms: 1.75x slower                                                 |
| mako            | 11.2 ms                                                    | 21.1 ms: 1.88x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.74x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 3.98 ms                                                    | 2.89 ms: 1.37x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.37 ms: 1.33x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 142 ms: 1.14x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                                  |
| pidigits                   | 191 ms                                                     | 184 ms: 1.04x faster                                                  |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 597 ms: 1.02x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 346 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 111 ms: 1.03x slower                                                  |
| regex_v8                   | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                                 |
| async_tree_none            | 378 ms                                                     | 406 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 662 ms: 1.08x slower                                                  |
| async_tree_memoization     | 463 ms                                                     | 510 ms: 1.10x slower                                                  |
| pathlib                    | 17.3 ms                                                    | 19.2 ms: 1.11x slower                                                 |
| json_loads                 | 28.9 us                                                    | 32.2 us: 1.11x slower                                                 |
| asyncio_tcp                | 508 ms                                                     | 567 ms: 1.12x slower                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 2.08 sec: 1.13x slower                                                |
| json                       | 5.31 ms                                                    | 5.99 ms: 1.13x slower                                                 |
| deepcopy                   | 367 us                                                     | 423 us: 1.15x slower                                                  |
| coverage                   | 93.1 ms                                                    | 110 ms: 1.18x slower                                                  |
| docutils                   | 2.83 sec                                                   | 3.35 sec: 1.19x slower                                                |
| telco                      | 8.41 ms                                                    | 10.0 ms: 1.19x slower                                                 |
| scimark_fft                | 392 ms                                                     | 475 ms: 1.21x slower                                                  |
| mdp                        | 2.79 sec                                                   | 3.37 sec: 1.21x slower                                                |
| pylint                     | 317 ms                                                     | 394 ms: 1.24x slower                                                  |
| json_dumps                 | 10.7 ms                                                    | 13.4 ms: 1.25x slower                                                 |
| python_startup             | 10.8 ms                                                    | 13.4 ms: 1.25x slower                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 6.63 ms: 1.26x slower                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 111 ms: 1.27x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 9.08 ms: 1.28x slower                                                 |
| async_generators           | 442 ms                                                     | 565 ms: 1.28x slower                                                  |
| generators                 | 29.6 ms                                                    | 38.0 ms: 1.28x slower                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 6.61 sec: 1.32x slower                                                |
| deepcopy_memo              | 39.7 us                                                    | 52.3 us: 1.32x slower                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 4.42 us: 1.32x slower                                                 |
| coroutines                 | 23.2 ms                                                    | 31.2 ms: 1.35x slower                                                 |
| meteor_contest             | 110 ms                                                     | 148 ms: 1.35x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 28.7 ms: 1.40x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.64 sec: 1.41x slower                                                |
| tornado_http               | 94.6 ms                                                    | 136 ms: 1.44x slower                                                  |
| 2to3                       | 274 ms                                                     | 394 ms: 1.44x slower                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 112 ms: 1.45x slower                                                  |
| html5lib                   | 67.2 ms                                                    | 97.3 ms: 1.45x slower                                                 |
| xml_etree_process          | 61.2 ms                                                    | 89.5 ms: 1.46x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 119 ms: 1.47x slower                                                  |
| sympy_str                  | 282 ms                                                     | 424 ms: 1.50x slower                                                  |
| fannkuch                   | 402 ms                                                     | 608 ms: 1.51x slower                                                  |
| tomli_loads                | 2.12 sec                                                   | 3.22 sec: 1.52x slower                                                |
| thrift                     | 823 us                                                     | 1.25 ms: 1.52x slower                                                 |
| richards                   | 50.9 ms                                                    | 78.0 ms: 1.53x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 254 us: 1.54x slower                                                  |
| regex_compile              | 137 ms                                                     | 217 ms: 1.59x slower                                                  |
| sympy_expand               | 473 ms                                                     | 753 ms: 1.59x slower                                                  |
| spectral_norm              | 116 ms                                                     | 186 ms: 1.60x slower                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 88.8 ms: 1.60x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 177 ms: 1.60x slower                                                  |
| pyflate                    | 484 ms                                                     | 777 ms: 1.61x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 83.9 ms: 1.62x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 254 ms: 1.63x slower                                                  |
| richards_super             | 57.4 ms                                                    | 94.6 ms: 1.65x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 40.2 ms: 1.70x slower                                                 |
| comprehensions             | 16.6 us                                                    | 28.7 us: 1.73x slower                                                 |
| pprint_safe_repr           | 758 ms                                                     | 1.32 sec: 1.73x slower                                                |
| pprint_pformat             | 1.56 sec                                                   | 2.72 sec: 1.75x slower                                                |
| django_template            | 34.8 ms                                                    | 60.9 ms: 1.75x slower                                                 |
| logging_silent             | 105 ns                                                     | 185 ns: 1.77x slower                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 124 ms: 1.79x slower                                                  |
| float                      | 78.9 ms                                                    | 142 ms: 1.80x slower                                                  |
| unpickle_pure_python       | 218 us                                                     | 399 us: 1.83x slower                                                  |
| logging_format             | 6.47 us                                                    | 12.0 us: 1.85x slower                                                 |
| logging_simple             | 5.74 us                                                    | 10.7 us: 1.85x slower                                                 |
| pickle_pure_python         | 305 us                                                     | 571 us: 1.87x slower                                                  |
| mako                       | 11.2 ms                                                    | 21.1 ms: 1.88x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 12.0 ms: 1.91x slower                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 3.20 ms: 1.96x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 245 ms: 2.01x slower                                                  |
| chaos                      | 61.3 ms                                                    | 124 ms: 2.03x slower                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 2.71 ms: 2.05x slower                                                 |
| scimark_sor                | 127 ms                                                     | 264 ms: 2.07x slower                                                  |
| go                         | 145 ms                                                     | 307 ms: 2.12x slower                                                  |
| raytrace                   | 267 ms                                                     | 593 ms: 2.22x slower                                                  |
| nbody                      | 88.3 ms                                                    | 217 ms: 2.46x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 8.28 ms: 2.55x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 3.03 ms: 3.63x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.41x slower                                                          |

Benchmark hidden because not significant (3): regex_dna, bench_mp_pool, async_tree_memoization_tg
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.30x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.15x