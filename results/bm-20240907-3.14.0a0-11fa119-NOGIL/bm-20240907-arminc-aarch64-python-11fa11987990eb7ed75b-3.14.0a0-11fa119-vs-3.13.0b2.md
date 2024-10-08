# Results vs. 3.13.0b2

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.54x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 518 ms: 1.70x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.10 sec: 1.32x slower                                                  |
| html5lib       | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| tornado_http   | 128 ms                                                       | 207 ms: 1.62x slower                                                    |
| Geometric mean | (ref)                                                        | 1.61x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 871 ms: 1.14x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 739 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 914 ms: 1.15x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 699 ms: 1.16x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 572 ms: 1.20x slower                                                    |
| async_tree_none            | 492 ms                                                       | 625 ms: 1.27x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 207 ms: 2.27x slower                                                    |
| nbody          | 114 ms                                                       | 281 ms: 2.46x slower                                                    |
| Geometric mean | (ref)                                                        | 1.77x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.48 ms: 1.11x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| regex_compile  | 128 ms                                                       | 259 ms: 2.03x slower                                                    |
| Geometric mean | (ref)                                                        | 1.18x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 184 ms: 1.04x faster                                                    |
| pickle_dict          | 37.6 us                                                      | 38.8 us: 1.03x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 157 ms: 1.07x slower                                                    |
| unpickle_list        | 6.52 us                                                      | 6.99 us: 1.07x slower                                                   |
| unpickle             | 19.8 us                                                      | 21.7 us: 1.10x slower                                                   |
| json_loads           | 32.1 us                                                      | 39.3 us: 1.22x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.9 ms: 1.37x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 163 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 130 ms: 1.61x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.19 sec: 1.63x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 542 us: 2.16x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 777 us: 2.17x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.30x slower                                                            |

Benchmark hidden because not significant (2): pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 18.2 ms: 1.40x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 12.2 ms: 1.42x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.41x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 53.3 ms: 1.94x slower                                                   |
| django_template | 42.3 ms                                                      | 83.4 ms: 1.97x slower                                                   |
| mako            | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.95x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.45 ms: 1.50x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.62 ms: 1.44x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.48 ms: 1.11x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 184 ms: 1.04x faster                                                    |
| asyncio_websockets         | 657 ms                                                       | 672 ms: 1.02x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.20 ms: 1.02x slower                                                   |
| pickle_dict                | 37.6 us                                                      | 38.8 us: 1.03x slower                                                   |
| regex_v8                   | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| sqlite_synth               | 3.90 us                                                      | 4.17 us: 1.07x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 157 ms: 1.07x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.99 us: 1.07x slower                                                   |
| unpickle                   | 19.8 us                                                      | 21.7 us: 1.10x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 871 ms: 1.14x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 739 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 914 ms: 1.15x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 699 ms: 1.16x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 683 ms: 1.17x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.8 ms: 1.18x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.62 sec: 1.18x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 572 ms: 1.20x slower                                                    |
| json_loads                 | 32.1 us                                                      | 39.3 us: 1.22x slower                                                   |
| json                       | 5.64 ms                                                      | 7.03 ms: 1.25x slower                                                   |
| async_tree_none            | 492 ms                                                       | 625 ms: 1.27x slower                                                    |
| deepcopy                   | 448 us                                                       | 571 us: 1.27x slower                                                    |
| telco                      | 10.0 ms                                                      | 12.8 ms: 1.28x slower                                                   |
| scimark_fft                | 445 ms                                                       | 573 ms: 1.29x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.32 sec: 1.30x slower                                                  |
| docutils                   | 3.10 sec                                                     | 4.10 sec: 1.32x slower                                                  |
| async_generators           | 488 ms                                                       | 653 ms: 1.34x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.82 ms: 1.35x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 17.9 ms: 1.37x slower                                                   |
| coverage                   | 98.4 ms                                                      | 136 ms: 1.38x slower                                                    |
| python_startup             | 13.0 ms                                                      | 18.2 ms: 1.40x slower                                                   |
| coroutines                 | 29.0 ms                                                      | 40.9 ms: 1.41x slower                                                   |
| deepcopy_memo              | 50.8 us                                                      | 72.1 us: 1.42x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 12.2 ms: 1.42x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 163 ms: 1.43x slower                                                    |
| meteor_contest             | 113 ms                                                       | 167 ms: 1.47x slower                                                    |
| pylint                     | 337 ms                                                       | 511 ms: 1.52x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 6.14 us: 1.52x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 152 ms: 1.54x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.7 ms: 1.55x slower                                                   |
| spectral_norm              | 141 ms                                                       | 226 ms: 1.60x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 130 ms: 1.61x slower                                                    |
| tornado_http               | 128 ms                                                       | 207 ms: 1.62x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 9.48 sec: 1.63x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 4.19 sec: 1.63x slower                                                  |
| fannkuch                   | 451 ms                                                       | 738 ms: 1.64x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 96.1 ms: 1.64x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 2.02 sec: 1.66x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 34.7 ms: 1.66x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 137 ms: 1.67x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 2.13 ms: 1.69x slower                                                   |
| 2to3                       | 305 ms                                                       | 518 ms: 1.70x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 336 us: 1.74x slower                                                    |
| thrift                     | 962 us                                                       | 1.69 ms: 1.75x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 237 ms: 1.83x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.02 sec: 1.83x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.76 sec: 1.88x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 3.64 sec: 1.88x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 119 ms: 1.89x slower                                                    |
| sympy_str                  | 265 ms                                                       | 514 ms: 1.94x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 53.3 ms: 1.94x slower                                                   |
| django_template            | 42.3 ms                                                      | 83.4 ms: 1.97x slower                                                   |
| comprehensions             | 20.5 us                                                      | 40.9 us: 1.99x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.6 us: 2.03x slower                                                   |
| regex_compile              | 128 ms                                                       | 259 ms: 2.03x slower                                                    |
| logging_format             | 7.82 us                                                      | 15.9 us: 2.04x slower                                                   |
| richards                   | 55.9 ms                                                      | 117 ms: 2.09x slower                                                    |
| sympy_expand               | 457 ms                                                       | 961 ms: 2.10x slower                                                    |
| logging_silent             | 133 ns                                                       | 284 ns: 2.13x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 176 ms: 2.14x slower                                                    |
| scimark_sor                | 159 ms                                                       | 341 ms: 2.14x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 542 us: 2.16x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 777 us: 2.17x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 318 ms: 2.21x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.9 ms: 2.25x slower                                                   |
| float                      | 91.4 ms                                                      | 207 ms: 2.27x slower                                                    |
| richards_super             | 62.3 ms                                                      | 143 ms: 2.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 160 ms: 2.34x slower                                                    |
| nbody                      | 114 ms                                                       | 281 ms: 2.46x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 350 ms: 2.48x slower                                                    |
| go                         | 161 ms                                                       | 404 ms: 2.51x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 3.67 ms: 2.58x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 4.45 ms: 2.60x slower                                                   |
| raytrace                   | 297 ms                                                       | 815 ms: 2.75x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.7 ms: 3.28x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.54x slower                                                            |

Benchmark hidden because not significant (4): pickle, pidigits, regex_dna, pickle_list
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.16x