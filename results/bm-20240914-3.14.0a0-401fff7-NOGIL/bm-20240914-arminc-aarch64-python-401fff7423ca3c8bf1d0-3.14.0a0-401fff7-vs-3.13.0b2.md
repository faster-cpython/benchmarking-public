# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.50x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 509 ms: 1.67x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.97 sec: 1.28x slower                                                  |
| html5lib       | 66.1 ms                                                      | 118 ms: 1.79x slower                                                    |
| tornado_http   | 128 ms                                                       | 203 ms: 1.59x slower                                                    |
| Geometric mean | (ref)                                                        | 1.57x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.34 sec: 1.05x slower                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.37 sec: 1.12x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 723 ms: 1.12x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 866 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 901 ms: 1.14x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 692 ms: 1.14x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 562 ms: 1.18x slower                                                    |
| async_tree_none            | 492 ms                                                       | 600 ms: 1.22x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 205 ms: 2.24x slower                                                    |
| nbody          | 114 ms                                                       | 281 ms: 2.47x slower                                                    |
| Geometric mean | (ref)                                                        | 1.77x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.47 ms: 1.11x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 32.2 ms: 1.04x slower                                                   |
| regex_compile  | 128 ms                                                       | 246 ms: 1.92x slower                                                    |
| Geometric mean | (ref)                                                        | 1.15x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 183 ms: 1.04x faster                                                    |
| pickle_list          | 5.27 us                                                      | 5.35 us: 1.01x slower                                                   |
| pickle_dict          | 37.6 us                                                      | 39.0 us: 1.04x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 153 ms: 1.04x slower                                                    |
| unpickle_list        | 6.52 us                                                      | 6.98 us: 1.07x slower                                                   |
| unpickle             | 19.8 us                                                      | 21.5 us: 1.09x slower                                                   |
| json_loads           | 32.1 us                                                      | 38.1 us: 1.19x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.4 ms: 1.32x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 155 ms: 1.37x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 125 ms: 1.54x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.12 sec: 1.60x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 749 us: 2.09x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 525 us: 2.09x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.27x slower                                                            |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 18.1 ms: 1.39x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 12.0 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.39x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 100 ms: 1.66x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 51.0 ms: 1.86x slower                                                   |
| django_template | 42.3 ms                                                      | 79.2 ms: 1.87x slower                                                   |
| mako            | 13.2 ms                                                      | 28.4 ms: 2.16x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.88x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.46 ms: 1.50x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.60 ms: 1.45x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.47 ms: 1.11x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 183 ms: 1.04x faster                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 6.94 ms: 1.01x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.35 us: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 672 ms: 1.02x slower                                                    |
| sqlite_synth               | 3.90 us                                                      | 4.01 us: 1.03x slower                                                   |
| regex_v8                   | 31.1 ms                                                      | 32.2 ms: 1.04x slower                                                   |
| pickle_dict                | 37.6 us                                                      | 39.0 us: 1.04x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 153 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.34 sec: 1.05x slower                                                  |
| unpickle_list              | 6.52 us                                                      | 6.98 us: 1.07x slower                                                   |
| unpickle                   | 19.8 us                                                      | 21.5 us: 1.09x slower                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.37 sec: 1.12x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 723 ms: 1.12x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 866 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 901 ms: 1.14x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 692 ms: 1.14x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.1 ms: 1.15x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 677 ms: 1.16x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.61 sec: 1.18x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 562 ms: 1.18x slower                                                    |
| deepcopy                   | 448 us                                                       | 530 us: 1.18x slower                                                    |
| json_loads                 | 32.1 us                                                      | 38.1 us: 1.19x slower                                                   |
| json                       | 5.64 ms                                                      | 6.75 ms: 1.20x slower                                                   |
| async_tree_none            | 492 ms                                                       | 600 ms: 1.22x slower                                                    |
| telco                      | 10.0 ms                                                      | 12.7 ms: 1.27x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.97 sec: 1.28x slower                                                  |
| mdp                        | 3.33 sec                                                     | 4.29 sec: 1.29x slower                                                  |
| scimark_fft                | 445 ms                                                       | 579 ms: 1.30x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.64 ms: 1.32x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 17.4 ms: 1.32x slower                                                   |
| coverage                   | 98.4 ms                                                      | 130 ms: 1.33x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 67.7 us: 1.33x slower                                                   |
| async_generators           | 488 ms                                                       | 656 ms: 1.34x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 39.2 ms: 1.35x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 155 ms: 1.37x slower                                                    |
| python_startup             | 13.0 ms                                                      | 18.1 ms: 1.39x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 12.0 ms: 1.39x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 5.71 us: 1.42x slower                                                   |
| meteor_contest             | 113 ms                                                       | 167 ms: 1.47x slower                                                    |
| pylint                     | 337 ms                                                       | 506 ms: 1.50x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 149 ms: 1.51x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 125 ms: 1.54x slower                                                    |
| generators                 | 37.1 ms                                                      | 58.3 ms: 1.57x slower                                                   |
| tornado_http               | 128 ms                                                       | 203 ms: 1.59x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 9.33 sec: 1.60x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 4.12 sec: 1.60x slower                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 2.02 ms: 1.61x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 95.1 ms: 1.63x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.99 sec: 1.63x slower                                                  |
| spectral_norm              | 141 ms                                                       | 231 ms: 1.64x slower                                                    |
| fannkuch                   | 451 ms                                                       | 741 ms: 1.64x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 34.4 ms: 1.65x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 100 ms: 1.66x slower                                                    |
| 2to3                       | 305 ms                                                       | 509 ms: 1.67x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 137 ms: 1.67x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 324 us: 1.68x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 219 ms: 1.69x slower                                                    |
| thrift                     | 962 us                                                       | 1.63 ms: 1.70x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 109 ms: 1.74x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.40 sec: 1.76x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.65 sec: 1.77x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 118 ms: 1.79x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.00 sec: 1.80x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 51.0 ms: 1.86x slower                                                   |
| django_template            | 42.3 ms                                                      | 79.2 ms: 1.87x slower                                                   |
| sympy_str                  | 265 ms                                                       | 507 ms: 1.91x slower                                                    |
| regex_compile              | 128 ms                                                       | 246 ms: 1.92x slower                                                    |
| comprehensions             | 20.5 us                                                      | 40.1 us: 1.96x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.1 us: 1.96x slower                                                   |
| logging_format             | 7.82 us                                                      | 15.5 us: 1.98x slower                                                   |
| sympy_expand               | 457 ms                                                       | 936 ms: 2.05x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 172 ms: 2.08x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 749 us: 2.09x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 525 us: 2.09x slower                                                    |
| richards                   | 55.9 ms                                                      | 119 ms: 2.13x slower                                                    |
| logging_silent             | 133 ns                                                       | 285 ns: 2.14x slower                                                    |
| scimark_sor                | 159 ms                                                       | 341 ms: 2.14x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.3 ms: 2.16x slower                                                   |
| mako                       | 13.2 ms                                                      | 28.4 ms: 2.16x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 317 ms: 2.20x slower                                                    |
| float                      | 91.4 ms                                                      | 205 ms: 2.24x slower                                                    |
| richards_super             | 62.3 ms                                                      | 140 ms: 2.25x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 329 ms: 2.33x slower                                                    |
| chaos                      | 68.3 ms                                                      | 160 ms: 2.34x slower                                                    |
| go                         | 161 ms                                                       | 382 ms: 2.38x slower                                                    |
| nbody                      | 114 ms                                                       | 281 ms: 2.47x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.22 ms: 2.47x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.71 ms: 2.61x slower                                                   |
| raytrace                   | 297 ms                                                       | 813 ms: 2.74x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.5 ms: 3.21x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.50x slower                                                            |

Benchmark hidden because not significant (3): pickle, regex_dna, pidigits
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.42x
- 95% likely to have a slowdown of 1.37x
- 99% likely to have a slowdown of 1.33x

# Memory
- memory change: 1.16x