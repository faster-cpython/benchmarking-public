# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.53x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                     | 395 ms: 1.44x slower                                  |
| chameleon      | 7.22 ms                                                    | 12.8 ms: 1.77x slower                                 |
| docutils       | 2.83 sec                                                   | 3.38 sec: 1.20x slower                                |
| html5lib       | 67.2 ms                                                    | 96.6 ms: 1.44x slower                                 |
| tornado_http   | 94.6 ms                                                    | 136 ms: 1.44x slower                                  |
| Geometric mean | (ref)                                                      | 1.45x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 883 ms: 1.06x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 657 ms: 1.12x slower                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 503 ms: 1.13x slower                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 715 ms: 1.17x slower                                  |
| async_tree_none_tg         | 336 ms                                                     | 396 ms: 1.18x slower                                  |
| async_tree_none            | 378 ms                                                     | 453 ms: 1.20x slower                                  |
| async_tree_memoization     | 463 ms                                                     | 559 ms: 1.21x slower                                  |
| Geometric mean             | (ref)                                                      | 1.11x slower                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 78.9 ms                                                    | 133 ms: 1.68x slower                                  |
| nbody          | 88.3 ms                                                    | 227 ms: 2.57x slower                                  |
| Geometric mean | (ref)                                                      | 1.63x slower                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                 |
| regex_v8       | 25.1 ms                                                    | 26.5 ms: 1.05x slower                                 |
| regex_compile  | 137 ms                                                     | 217 ms: 1.58x slower                                  |
| Geometric mean | (ref)                                                      | 1.13x slower                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 144 ms: 1.12x faster                                  |
| unpickle_list        | 5.34 us                                                    | 5.57 us: 1.04x slower                                 |
| pickle_list          | 5.11 us                                                    | 5.34 us: 1.04x slower                                 |
| xml_etree_iterparse  | 107 ms                                                     | 113 ms: 1.05x slower                                  |
| pickle               | 11.5 us                                                    | 12.4 us: 1.08x slower                                 |
| unpickle             | 15.1 us                                                    | 17.0 us: 1.12x slower                                 |
| json_loads           | 28.9 us                                                    | 32.7 us: 1.13x slower                                 |
| pickle_dict          | 34.8 us                                                    | 42.4 us: 1.22x slower                                 |
| xml_etree_generate   | 87.4 ms                                                    | 110 ms: 1.25x slower                                  |
| json_dumps           | 10.7 ms                                                    | 13.9 ms: 1.30x slower                                 |
| xml_etree_process    | 61.2 ms                                                    | 89.6 ms: 1.46x slower                                 |
| tomli_loads          | 2.12 sec                                                   | 3.30 sec: 1.56x slower                                |
| unpickle_pure_python | 218 us                                                     | 398 us: 1.82x slower                                  |
| pickle_pure_python   | 305 us                                                     | 570 us: 1.87x slower                                  |
| Geometric mean       | (ref)                                                      | 1.24x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 13.3 ms: 1.24x slower                                 |
| python_startup_no_site | 7.11 ms                                                    | 9.16 ms: 1.29x slower                                 |
| Geometric mean         | (ref)                                                      | 1.27x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 81.4 ms: 1.58x slower                                 |
| genshi_text     | 23.7 ms                                                    | 39.4 ms: 1.66x slower                                 |
| django_template | 34.8 ms                                                    | 60.1 ms: 1.73x slower                                 |
| mako            | 11.2 ms                                                    | 20.7 ms: 1.84x slower                                 |
| Geometric mean  | (ref)                                                      | 1.70x slower                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.42 ms: 1.28x faster                                 |
| gc_traversal               | 3.98 ms                                                    | 3.21 ms: 1.24x faster                                 |
| bench_mp_pool              | 23.9 ms                                                    | 21.0 ms: 1.14x faster                                 |
| xml_etree_parse            | 162 ms                                                     | 144 ms: 1.12x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 883 ms: 1.06x faster                                  |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                 |
| unpickle_list              | 5.34 us                                                    | 5.57 us: 1.04x slower                                 |
| pickle_list                | 5.11 us                                                    | 5.34 us: 1.04x slower                                 |
| xml_etree_iterparse        | 107 ms                                                     | 113 ms: 1.05x slower                                  |
| regex_v8                   | 25.1 ms                                                    | 26.5 ms: 1.05x slower                                 |
| sqlite_synth               | 2.99 us                                                    | 3.21 us: 1.07x slower                                 |
| pickle                     | 11.5 us                                                    | 12.4 us: 1.08x slower                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 657 ms: 1.12x slower                                  |
| unpickle                   | 15.1 us                                                    | 17.0 us: 1.12x slower                                 |
| json_loads                 | 28.9 us                                                    | 32.7 us: 1.13x slower                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 503 ms: 1.13x slower                                  |
| json                       | 5.31 ms                                                    | 6.13 ms: 1.16x slower                                 |
| asyncio_tcp                | 508 ms                                                     | 590 ms: 1.16x slower                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 2.14 sec: 1.16x slower                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 715 ms: 1.17x slower                                  |
| scimark_fft                | 392 ms                                                     | 461 ms: 1.17x slower                                  |
| async_tree_none_tg         | 336 ms                                                     | 396 ms: 1.18x slower                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 6.24 ms: 1.18x slower                                 |
| async_tree_none            | 378 ms                                                     | 453 ms: 1.20x slower                                  |
| docutils                   | 2.83 sec                                                   | 3.38 sec: 1.20x slower                                |
| pathlib                    | 17.3 ms                                                    | 20.9 ms: 1.21x slower                                 |
| async_tree_memoization     | 463 ms                                                     | 559 ms: 1.21x slower                                  |
| pickle_dict                | 34.8 us                                                    | 42.4 us: 1.22x slower                                 |
| mdp                        | 2.79 sec                                                   | 3.42 sec: 1.23x slower                                |
| generators                 | 29.6 ms                                                    | 36.6 ms: 1.24x slower                                 |
| python_startup             | 10.8 ms                                                    | 13.3 ms: 1.24x slower                                 |
| async_generators           | 442 ms                                                     | 553 ms: 1.25x slower                                  |
| xml_etree_generate         | 87.4 ms                                                    | 110 ms: 1.25x slower                                  |
| pylint                     | 317 ms                                                     | 398 ms: 1.26x slower                                  |
| python_startup_no_site     | 7.11 ms                                                    | 9.16 ms: 1.29x slower                                 |
| json_dumps                 | 10.7 ms                                                    | 13.9 ms: 1.30x slower                                 |
| dulwich_log                | 67.2 ms                                                    | 87.8 ms: 1.31x slower                                 |
| meteor_contest             | 110 ms                                                     | 145 ms: 1.32x slower                                  |
| pycparser                  | 1.16 sec                                                   | 1.56 sec: 1.35x slower                                |
| sympy_integrate            | 20.5 ms                                                    | 29.0 ms: 1.42x slower                                 |
| html5lib                   | 67.2 ms                                                    | 96.6 ms: 1.44x slower                                 |
| 2to3                       | 274 ms                                                     | 395 ms: 1.44x slower                                  |
| tornado_http               | 94.6 ms                                                    | 136 ms: 1.44x slower                                  |
| coroutines                 | 23.2 ms                                                    | 33.5 ms: 1.45x slower                                 |
| nqueens                    | 81.4 ms                                                    | 118 ms: 1.45x slower                                  |
| xml_etree_process          | 61.2 ms                                                    | 89.6 ms: 1.46x slower                                 |
| crypto_pyaes               | 77.5 ms                                                    | 115 ms: 1.48x slower                                  |
| flaskblogging              | 9.01 ms                                                    | 13.4 ms: 1.49x slower                                 |
| fannkuch                   | 402 ms                                                     | 600 ms: 1.49x slower                                  |
| sympy_str                  | 282 ms                                                     | 430 ms: 1.52x slower                                  |
| richards                   | 50.9 ms                                                    | 77.8 ms: 1.53x slower                                 |
| pyflate                    | 484 ms                                                     | 749 ms: 1.55x slower                                  |
| tomli_loads                | 2.12 sec                                                   | 3.30 sec: 1.56x slower                                |
| deepcopy_reduce            | 3.35 us                                                    | 5.22 us: 1.56x slower                                 |
| typing_runtime_protocols   | 165 us                                                     | 259 us: 1.57x slower                                  |
| deepcopy                   | 367 us                                                     | 578 us: 1.57x slower                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 87.6 ms: 1.58x slower                                 |
| genshi_xml                 | 51.6 ms                                                    | 81.4 ms: 1.58x slower                                 |
| sqlglot_normalize          | 110 ms                                                     | 174 ms: 1.58x slower                                  |
| regex_compile              | 137 ms                                                     | 217 ms: 1.58x slower                                  |
| sympy_expand               | 473 ms                                                     | 758 ms: 1.60x slower                                  |
| spectral_norm              | 116 ms                                                     | 188 ms: 1.62x slower                                  |
| richards_super             | 57.4 ms                                                    | 93.3 ms: 1.63x slower                                 |
| deepcopy_memo              | 39.7 us                                                    | 65.1 us: 1.64x slower                                 |
| sympy_sum                  | 156 ms                                                     | 258 ms: 1.66x slower                                  |
| genshi_text                | 23.7 ms                                                    | 39.4 ms: 1.66x slower                                 |
| comprehensions             | 16.6 us                                                    | 27.7 us: 1.67x slower                                 |
| float                      | 78.9 ms                                                    | 133 ms: 1.68x slower                                  |
| django_template            | 34.8 ms                                                    | 60.1 ms: 1.73x slower                                 |
| pprint_safe_repr           | 758 ms                                                     | 1.31 sec: 1.73x slower                                |
| pprint_pformat             | 1.56 sec                                                   | 2.70 sec: 1.74x slower                                |
| scimark_monte_carlo        | 69.2 ms                                                    | 122 ms: 1.77x slower                                  |
| chameleon                  | 7.22 ms                                                    | 12.8 ms: 1.77x slower                                 |
| unpickle_pure_python       | 218 us                                                     | 398 us: 1.82x slower                                  |
| logging_format             | 6.47 us                                                    | 11.8 us: 1.83x slower                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 2.99 ms: 1.83x slower                                 |
| logging_simple             | 5.74 us                                                    | 10.5 us: 1.83x slower                                 |
| mako                       | 11.2 ms                                                    | 20.7 ms: 1.84x slower                                 |
| logging_silent             | 105 ns                                                     | 195 ns: 1.86x slower                                  |
| pickle_pure_python         | 305 us                                                     | 570 us: 1.87x slower                                  |
| sqlglot_parse              | 1.32 ms                                                    | 2.52 ms: 1.91x slower                                 |
| hexiom                     | 6.30 ms                                                    | 12.3 ms: 1.96x slower                                 |
| scimark_lu                 | 122 ms                                                     | 238 ms: 1.96x slower                                  |
| chaos                      | 61.3 ms                                                    | 124 ms: 2.02x slower                                  |
| scimark_sor                | 127 ms                                                     | 270 ms: 2.12x slower                                  |
| go                         | 145 ms                                                     | 311 ms: 2.15x slower                                  |
| raytrace                   | 267 ms                                                     | 589 ms: 2.21x slower                                  |
| deltablue                  | 3.25 ms                                                    | 8.32 ms: 2.56x slower                                 |
| nbody                      | 88.3 ms                                                    | 227 ms: 2.57x slower                                  |
| bench_thread_pool          | 834 us                                                     | 3.04 ms: 3.65x slower                                 |
| coverage                   | 93.1 ms                                                    | 787 ms: 8.46x slower                                  |
| thrift                     | 823 us                                                     | 13.1 ms: 15.88x slower                                |
| telco                      | 8.41 ms                                                    | 317 ms: 37.64x slower                                 |
| Geometric mean             | (ref)                                                      | 1.53x slower                                          |

Benchmark hidden because not significant (4): async_tree_io, asyncio_websockets, regex_dna, pidigits
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dask, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.28x

# Memory
- memory change: 1.15x