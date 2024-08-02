# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.31x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 375 ms: 1.37x slower                                                  |
| chameleon      | 7.22 ms                                                    | 8.91 ms: 1.23x slower                                                 |
| docutils       | 2.83 sec                                                   | 3.51 sec: 1.24x slower                                                |
| html5lib       | 67.2 ms                                                    | 82.2 ms: 1.22x slower                                                 |
| tornado_http   | 94.6 ms                                                    | 107 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                      | 1.24x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 620 ms: 1.05x slower                                                  |
| async_tree_io_tg           | 936 ms                                                     | 1.00 sec: 1.07x slower                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 477 ms: 1.08x slower                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 665 ms: 1.09x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 366 ms: 1.09x slower                                                  |
| async_tree_io              | 939 ms                                                     | 1.03 sec: 1.10x slower                                                |
| async_tree_none            | 378 ms                                                     | 428 ms: 1.13x slower                                                  |
| async_tree_memoization     | 463 ms                                                     | 531 ms: 1.15x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.09x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 194 ms: 1.01x slower                                                  |
| float          | 78.9 ms                                                    | 130 ms: 1.64x slower                                                  |
| nbody          | 88.3 ms                                                    | 193 ms: 2.19x slower                                                  |
| Geometric mean | (ref)                                                      | 1.54x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.87 ms: 1.06x slower                                                 |
| regex_dna      | 221 ms                                                     | 235 ms: 1.06x slower                                                  |
| regex_v8       | 25.1 ms                                                    | 26.9 ms: 1.07x slower                                                 |
| regex_compile  | 137 ms                                                     | 236 ms: 1.73x slower                                                  |
| Geometric mean | (ref)                                                      | 1.20x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.05x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.17 us: 1.03x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 35.5 us: 1.02x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.23 us: 1.03x slower                                                 |
| pickle               | 11.5 us                                                    | 12.2 us: 1.06x slower                                                 |
| json_dumps           | 10.7 ms                                                    | 11.7 ms: 1.09x slower                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 125 ms: 1.17x slower                                                  |
| xml_etree_process    | 61.2 ms                                                    | 78.3 ms: 1.28x slower                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 114 ms: 1.30x slower                                                  |
| tomli_loads          | 2.12 sec                                                   | 3.49 sec: 1.64x slower                                                |
| unpickle_pure_python | 218 us                                                     | 396 us: 1.82x slower                                                  |
| pickle_pure_python   | 305 us                                                     | 560 us: 1.83x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.19x slower                                                          |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 49.6 ms: 1.42x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 85.5 ms: 1.66x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 41.3 ms: 1.74x slower                                                 |
| mako            | 11.2 ms                                                    | 19.9 ms: 1.77x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.64x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.05x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.17 us: 1.03x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.89 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                 |
| thrift                     | 823 us                                                     | 831 us: 1.01x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                 |
| coverage                   | 93.1 ms                                                    | 94.1 ms: 1.01x slower                                                 |
| pidigits                   | 191 ms                                                     | 194 ms: 1.01x slower                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.84 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.87 sec: 1.02x slower                                                |
| pickle_dict                | 34.8 us                                                    | 35.5 us: 1.02x slower                                                 |
| pickle_list                | 5.11 us                                                    | 5.23 us: 1.03x slower                                                 |
| asyncio_tcp                | 508 ms                                                     | 525 ms: 1.03x slower                                                  |
| pathlib                    | 17.3 ms                                                    | 18.0 ms: 1.04x slower                                                 |
| coroutines                 | 23.2 ms                                                    | 24.2 ms: 1.04x slower                                                 |
| sqlite_synth               | 2.99 us                                                    | 3.13 us: 1.05x slower                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 620 ms: 1.05x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.87 ms: 1.06x slower                                                 |
| json                       | 5.31 ms                                                    | 5.62 ms: 1.06x slower                                                 |
| flaskblogging              | 9.01 ms                                                    | 9.56 ms: 1.06x slower                                                 |
| regex_dna                  | 221 ms                                                     | 235 ms: 1.06x slower                                                  |
| pickle                     | 11.5 us                                                    | 12.2 us: 1.06x slower                                                 |
| dask                       | 369 ms                                                     | 394 ms: 1.07x slower                                                  |
| regex_v8                   | 25.1 ms                                                    | 26.9 ms: 1.07x slower                                                 |
| async_tree_io_tg           | 936 ms                                                     | 1.00 sec: 1.07x slower                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 477 ms: 1.08x slower                                                  |
| generators                 | 29.6 ms                                                    | 31.9 ms: 1.08x slower                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 665 ms: 1.09x slower                                                  |
| async_tree_none_tg         | 336 ms                                                     | 366 ms: 1.09x slower                                                  |
| json_dumps                 | 10.7 ms                                                    | 11.7 ms: 1.09x slower                                                 |
| mdp                        | 2.79 sec                                                   | 3.05 sec: 1.10x slower                                                |
| async_tree_io              | 939 ms                                                     | 1.03 sec: 1.10x slower                                                |
| async_generators           | 442 ms                                                     | 496 ms: 1.12x slower                                                  |
| async_tree_none            | 378 ms                                                     | 428 ms: 1.13x slower                                                  |
| tornado_http               | 94.6 ms                                                    | 107 ms: 1.13x slower                                                  |
| logging_format             | 6.47 us                                                    | 7.42 us: 1.15x slower                                                 |
| async_tree_memoization     | 463 ms                                                     | 531 ms: 1.15x slower                                                  |
| dulwich_log                | 67.2 ms                                                    | 77.3 ms: 1.15x slower                                                 |
| logging_simple             | 5.74 us                                                    | 6.65 us: 1.16x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 125 ms: 1.17x slower                                                  |
| bench_thread_pool          | 834 us                                                     | 996 us: 1.19x slower                                                  |
| html5lib                   | 67.2 ms                                                    | 82.2 ms: 1.22x slower                                                 |
| pylint                     | 317 ms                                                     | 388 ms: 1.22x slower                                                  |
| chameleon                  | 7.22 ms                                                    | 8.91 ms: 1.23x slower                                                 |
| docutils                   | 2.83 sec                                                   | 3.51 sec: 1.24x slower                                                |
| telco                      | 8.41 ms                                                    | 10.6 ms: 1.26x slower                                                 |
| xml_etree_process          | 61.2 ms                                                    | 78.3 ms: 1.28x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 199 ms: 1.28x slower                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 114 ms: 1.30x slower                                                  |
| sympy_expand               | 473 ms                                                     | 615 ms: 1.30x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 4.38 us: 1.31x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 216 us: 1.31x slower                                                  |
| meteor_contest             | 110 ms                                                     | 145 ms: 1.32x slower                                                  |
| sympy_str                  | 282 ms                                                     | 378 ms: 1.34x slower                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 75.6 ms: 1.36x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 150 ms: 1.36x slower                                                  |
| 2to3                       | 274 ms                                                     | 375 ms: 1.37x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 28.2 ms: 1.38x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.61 sec: 1.39x slower                                                |
| scimark_sor                | 127 ms                                                     | 179 ms: 1.40x slower                                                  |
| django_template            | 34.8 ms                                                    | 49.6 ms: 1.42x slower                                                 |
| raytrace                   | 267 ms                                                     | 384 ms: 1.44x slower                                                  |
| deepcopy                   | 367 us                                                     | 554 us: 1.51x slower                                                  |
| scimark_fft                | 392 ms                                                     | 598 ms: 1.52x slower                                                  |
| richards_super             | 57.4 ms                                                    | 88.1 ms: 1.54x slower                                                 |
| go                         | 145 ms                                                     | 222 ms: 1.54x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 2.57 ms: 1.57x slower                                                 |
| richards                   | 50.9 ms                                                    | 81.0 ms: 1.59x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 196 ms: 1.61x slower                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 2.14 ms: 1.62x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 5.33 ms: 1.64x slower                                                 |
| tomli_loads                | 2.12 sec                                                   | 3.49 sec: 1.64x slower                                                |
| float                      | 78.9 ms                                                    | 130 ms: 1.64x slower                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 128 ms: 1.65x slower                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 8.72 ms: 1.66x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 85.5 ms: 1.66x slower                                                 |
| pprint_safe_repr           | 758 ms                                                     | 1.27 sec: 1.67x slower                                                |
| pprint_pformat             | 1.56 sec                                                   | 2.63 sec: 1.69x slower                                                |
| pyflate                    | 484 ms                                                     | 826 ms: 1.71x slower                                                  |
| regex_compile              | 137 ms                                                     | 236 ms: 1.73x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 41.3 ms: 1.74x slower                                                 |
| fannkuch                   | 402 ms                                                     | 701 ms: 1.75x slower                                                  |
| mako                       | 11.2 ms                                                    | 19.9 ms: 1.77x slower                                                 |
| chaos                      | 61.3 ms                                                    | 109 ms: 1.78x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 145 ms: 1.79x slower                                                  |
| unpickle_pure_python       | 218 us                                                     | 396 us: 1.82x slower                                                  |
| pickle_pure_python         | 305 us                                                     | 560 us: 1.83x slower                                                  |
| spectral_norm              | 116 ms                                                     | 216 ms: 1.86x slower                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 135 ms: 1.96x slower                                                  |
| deepcopy_memo              | 39.7 us                                                    | 77.8 us: 1.96x slower                                                 |
| logging_silent             | 105 ns                                                     | 222 ns: 2.12x slower                                                  |
| nbody                      | 88.3 ms                                                    | 193 ms: 2.19x slower                                                  |
| comprehensions             | 16.6 us                                                    | 37.6 us: 2.26x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 15.0 ms: 2.37x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.31x slower                                                          |

Benchmark hidden because not significant (4): asyncio_websockets, unpickle, json_loads, bench_mp_pool
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.01x