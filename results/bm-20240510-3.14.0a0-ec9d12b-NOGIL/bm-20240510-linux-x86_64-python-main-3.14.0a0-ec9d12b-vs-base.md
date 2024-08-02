# Results vs. base

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.49x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 269 ms                                                                | 395 ms: 1.47x slower                                  |
| chameleon      | 7.08 ms                                                               | 12.8 ms: 1.80x slower                                 |
| docutils       | 2.81 sec                                                              | 3.38 sec: 1.21x slower                                |
| html5lib       | 68.3 ms                                                               | 96.6 ms: 1.41x slower                                 |
| tornado_http   | 93.9 ms                                                               | 136 ms: 1.45x slower                                  |
| Geometric mean | (ref)                                                                 | 1.46x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_io_tg           | 981 ms                                                                | 883 ms: 1.11x faster                                  |
| async_tree_memoization_tg  | 459 ms                                                                | 503 ms: 1.09x slower                                  |
| async_tree_cpu_io_mixed_tg | 585 ms                                                                | 657 ms: 1.12x slower                                  |
| async_tree_none_tg         | 349 ms                                                                | 396 ms: 1.14x slower                                  |
| async_tree_cpu_io_mixed    | 617 ms                                                                | 715 ms: 1.16x slower                                  |
| async_tree_memoization     | 479 ms                                                                | 559 ms: 1.17x slower                                  |
| async_tree_none            | 363 ms                                                                | 453 ms: 1.25x slower                                  |
| Geometric mean             | (ref)                                                                 | 1.10x slower                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 189 ms                                                                | 191 ms: 1.01x slower                                  |
| float          | 78.6 ms                                                               | 133 ms: 1.69x slower                                  |
| nbody          | 88.0 ms                                                               | 227 ms: 2.58x slower                                  |
| Geometric mean | (ref)                                                                 | 1.64x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                               | 3.56 ms: 1.06x faster                                 |
| regex_dna      | 215 ms                                                                | 221 ms: 1.03x slower                                  |
| regex_v8       | 25.1 ms                                                               | 26.5 ms: 1.05x slower                                 |
| regex_compile  | 135 ms                                                                | 217 ms: 1.60x slower                                  |
| Geometric mean | (ref)                                                                 | 1.13x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 163 ms                                                                | 144 ms: 1.13x faster                                  |
| pickle_list          | 5.29 us                                                               | 5.34 us: 1.01x slower                                 |
| unpickle_list        | 5.34 us                                                               | 5.57 us: 1.04x slower                                 |
| xml_etree_iterparse  | 108 ms                                                                | 113 ms: 1.05x slower                                  |
| pickle               | 11.7 us                                                               | 12.4 us: 1.06x slower                                 |
| unpickle             | 16.1 us                                                               | 17.0 us: 1.06x slower                                 |
| json_loads           | 29.0 us                                                               | 32.7 us: 1.13x slower                                 |
| pickle_dict          | 35.1 us                                                               | 42.4 us: 1.21x slower                                 |
| xml_etree_generate   | 89.0 ms                                                               | 110 ms: 1.23x slower                                  |
| json_dumps           | 10.7 ms                                                               | 13.9 ms: 1.30x slower                                 |
| xml_etree_process    | 61.5 ms                                                               | 89.6 ms: 1.46x slower                                 |
| tomli_loads          | 2.10 sec                                                              | 3.30 sec: 1.57x slower                                |
| unpickle_pure_python | 220 us                                                                | 398 us: 1.80x slower                                  |
| pickle_pure_python   | 310 us                                                                | 570 us: 1.84x slower                                  |
| Geometric mean       | (ref)                                                                 | 1.23x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.3 ms                                                               | 13.3 ms: 1.29x slower                                 |
| python_startup_no_site | 7.08 ms                                                               | 9.16 ms: 1.29x slower                                 |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_xml      | 51.7 ms                                                               | 81.4 ms: 1.57x slower                                 |
| genshi_text     | 23.7 ms                                                               | 39.4 ms: 1.66x slower                                 |
| django_template | 35.1 ms                                                               | 60.1 ms: 1.71x slower                                 |
| mako            | 11.1 ms                                                               | 20.7 ms: 1.86x slower                                 |
| Geometric mean  | (ref)                                                                 | 1.70x slower                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------:|
| create_gc_cycles           | 1.80 ms                                                               | 1.42 ms: 1.26x faster                                 |
| gc_traversal               | 3.67 ms                                                               | 3.21 ms: 1.14x faster                                 |
| bench_mp_pool              | 23.8 ms                                                               | 21.0 ms: 1.13x faster                                 |
| xml_etree_parse            | 163 ms                                                                | 144 ms: 1.13x faster                                  |
| async_tree_io_tg           | 981 ms                                                                | 883 ms: 1.11x faster                                  |
| regex_effbot               | 3.78 ms                                                               | 3.56 ms: 1.06x faster                                 |
| asyncio_websockets         | 563 ms                                                                | 566 ms: 1.01x slower                                  |
| pickle_list                | 5.29 us                                                               | 5.34 us: 1.01x slower                                 |
| pidigits                   | 189 ms                                                                | 191 ms: 1.01x slower                                  |
| regex_dna                  | 215 ms                                                                | 221 ms: 1.03x slower                                  |
| unpickle_list              | 5.34 us                                                               | 5.57 us: 1.04x slower                                 |
| xml_etree_iterparse        | 108 ms                                                                | 113 ms: 1.05x slower                                  |
| regex_v8                   | 25.1 ms                                                               | 26.5 ms: 1.05x slower                                 |
| pickle                     | 11.7 us                                                               | 12.4 us: 1.06x slower                                 |
| unpickle                   | 16.1 us                                                               | 17.0 us: 1.06x slower                                 |
| sqlite_synth               | 2.94 us                                                               | 3.21 us: 1.09x slower                                 |
| async_tree_memoization_tg  | 459 ms                                                                | 503 ms: 1.09x slower                                  |
| async_tree_cpu_io_mixed_tg | 585 ms                                                                | 657 ms: 1.12x slower                                  |
| json_loads                 | 29.0 us                                                               | 32.7 us: 1.13x slower                                 |
| json                       | 5.44 ms                                                               | 6.13 ms: 1.13x slower                                 |
| async_tree_none_tg         | 349 ms                                                                | 396 ms: 1.14x slower                                  |
| asyncio_tcp                | 510 ms                                                                | 590 ms: 1.16x slower                                  |
| asyncio_tcp_ssl            | 1.85 sec                                                              | 2.14 sec: 1.16x slower                                |
| async_tree_cpu_io_mixed    | 617 ms                                                                | 715 ms: 1.16x slower                                  |
| async_tree_memoization     | 479 ms                                                                | 559 ms: 1.17x slower                                  |
| pathlib                    | 17.6 ms                                                               | 20.9 ms: 1.19x slower                                 |
| docutils                   | 2.81 sec                                                              | 3.38 sec: 1.21x slower                                |
| scimark_fft                | 382 ms                                                                | 461 ms: 1.21x slower                                  |
| pickle_dict                | 35.1 us                                                               | 42.4 us: 1.21x slower                                 |
| scimark_sparse_mat_mult    | 5.10 ms                                                               | 6.24 ms: 1.22x slower                                 |
| xml_etree_generate         | 89.0 ms                                                               | 110 ms: 1.23x slower                                  |
| async_generators           | 446 ms                                                                | 553 ms: 1.24x slower                                  |
| pylint                     | 319 ms                                                                | 398 ms: 1.25x slower                                  |
| async_tree_none            | 363 ms                                                                | 453 ms: 1.25x slower                                  |
| generators                 | 29.3 ms                                                               | 36.6 ms: 1.25x slower                                 |
| python_startup             | 10.3 ms                                                               | 13.3 ms: 1.29x slower                                 |
| python_startup_no_site     | 7.08 ms                                                               | 9.16 ms: 1.29x slower                                 |
| json_dumps                 | 10.7 ms                                                               | 13.9 ms: 1.30x slower                                 |
| meteor_contest             | 111 ms                                                                | 145 ms: 1.31x slower                                  |
| mdp                        | 2.57 sec                                                              | 3.42 sec: 1.33x slower                                |
| dulwich_log                | 65.8 ms                                                               | 87.8 ms: 1.34x slower                                 |
| pycparser                  | 1.16 sec                                                              | 1.56 sec: 1.34x slower                                |
| html5lib                   | 68.3 ms                                                               | 96.6 ms: 1.41x slower                                 |
| sympy_integrate            | 20.5 ms                                                               | 29.0 ms: 1.42x slower                                 |
| tornado_http               | 93.9 ms                                                               | 136 ms: 1.45x slower                                  |
| xml_etree_process          | 61.5 ms                                                               | 89.6 ms: 1.46x slower                                 |
| 2to3                       | 269 ms                                                                | 395 ms: 1.47x slower                                  |
| coroutines                 | 22.8 ms                                                               | 33.5 ms: 1.47x slower                                 |
| nqueens                    | 80.3 ms                                                               | 118 ms: 1.47x slower                                  |
| flaskblogging              | 8.94 ms                                                               | 13.4 ms: 1.50x slower                                 |
| fannkuch                   | 400 ms                                                                | 600 ms: 1.50x slower                                  |
| sympy_str                  | 279 ms                                                                | 430 ms: 1.54x slower                                  |
| crypto_pyaes               | 74.5 ms                                                               | 115 ms: 1.54x slower                                  |
| typing_runtime_protocols   | 167 us                                                                | 259 us: 1.55x slower                                  |
| tomli_loads                | 2.10 sec                                                              | 3.30 sec: 1.57x slower                                |
| genshi_xml                 | 51.7 ms                                                               | 81.4 ms: 1.57x slower                                 |
| deepcopy                   | 366 us                                                                | 578 us: 1.58x slower                                  |
| pyflate                    | 474 ms                                                                | 749 ms: 1.58x slower                                  |
| sqlglot_optimize           | 55.2 ms                                                               | 87.6 ms: 1.59x slower                                 |
| sqlglot_normalize          | 109 ms                                                                | 174 ms: 1.59x slower                                  |
| deepcopy_reduce            | 3.27 us                                                               | 5.22 us: 1.60x slower                                 |
| regex_compile              | 135 ms                                                                | 217 ms: 1.60x slower                                  |
| sympy_expand               | 469 ms                                                                | 758 ms: 1.62x slower                                  |
| deepcopy_memo              | 40.3 us                                                               | 65.1 us: 1.62x slower                                 |
| richards                   | 48.0 ms                                                               | 77.8 ms: 1.62x slower                                 |
| spectral_norm              | 115 ms                                                                | 188 ms: 1.63x slower                                  |
| sympy_sum                  | 157 ms                                                                | 258 ms: 1.65x slower                                  |
| comprehensions             | 16.8 us                                                               | 27.7 us: 1.65x slower                                 |
| genshi_text                | 23.7 ms                                                               | 39.4 ms: 1.66x slower                                 |
| float                      | 78.6 ms                                                               | 133 ms: 1.69x slower                                  |
| django_template            | 35.1 ms                                                               | 60.1 ms: 1.71x slower                                 |
| richards_super             | 54.5 ms                                                               | 93.3 ms: 1.71x slower                                 |
| pprint_safe_repr           | 764 ms                                                                | 1.31 sec: 1.72x slower                                |
| pprint_pformat             | 1.56 sec                                                              | 2.70 sec: 1.73x slower                                |
| scimark_monte_carlo        | 67.9 ms                                                               | 122 ms: 1.80x slower                                  |
| unpickle_pure_python       | 220 us                                                                | 398 us: 1.80x slower                                  |
| chameleon                  | 7.08 ms                                                               | 12.8 ms: 1.80x slower                                 |
| logging_simple             | 5.77 us                                                               | 10.5 us: 1.83x slower                                 |
| telco                      | 173 ms                                                                | 317 ms: 1.83x slower                                  |
| logging_format             | 6.42 us                                                               | 11.8 us: 1.84x slower                                 |
| pickle_pure_python         | 310 us                                                                | 570 us: 1.84x slower                                  |
| sqlglot_transpile          | 1.62 ms                                                               | 2.99 ms: 1.84x slower                                 |
| mako                       | 11.1 ms                                                               | 20.7 ms: 1.86x slower                                 |
| logging_silent             | 104 ns                                                                | 195 ns: 1.87x slower                                  |
| sqlglot_parse              | 1.31 ms                                                               | 2.52 ms: 1.92x slower                                 |
| hexiom                     | 6.28 ms                                                               | 12.3 ms: 1.96x slower                                 |
| scimark_lu                 | 117 ms                                                                | 238 ms: 2.04x slower                                  |
| chaos                      | 60.3 ms                                                               | 124 ms: 2.05x slower                                  |
| scimark_sor                | 130 ms                                                                | 270 ms: 2.07x slower                                  |
| go                         | 144 ms                                                                | 311 ms: 2.16x slower                                  |
| raytrace                   | 267 ms                                                                | 589 ms: 2.21x slower                                  |
| deltablue                  | 3.27 ms                                                               | 8.32 ms: 2.54x slower                                 |
| nbody                      | 88.0 ms                                                               | 227 ms: 2.58x slower                                  |
| bench_thread_pool          | 833 us                                                                | 3.04 ms: 3.65x slower                                 |
| coverage                   | 93.8 ms                                                               | 787 ms: 8.40x slower                                  |
| thrift                     | 820 us                                                                | 13.1 ms: 15.94x slower                                |
| Geometric mean             | (ref)                                                                 | 1.49x slower                                          |

Benchmark hidden because not significant (1): async_tree_io
Ignored benchmarks (1) of results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.15x