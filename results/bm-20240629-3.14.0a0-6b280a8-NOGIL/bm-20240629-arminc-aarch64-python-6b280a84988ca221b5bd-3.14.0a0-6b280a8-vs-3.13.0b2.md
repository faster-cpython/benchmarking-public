# Results vs. 3.13.0b2

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.57x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 523 ms: 1.72x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.12 sec: 1.33x slower                                                  |
| html5lib       | 66.1 ms                                                      | 120 ms: 1.82x slower                                                    |
| tornado_http   | 128 ms                                                       | 202 ms: 1.58x slower                                                    |
| Geometric mean | (ref)                                                        | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 871 ms: 1.14x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 698 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.42 sec: 1.16x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 925 ms: 1.17x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 762 ms: 1.18x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 579 ms: 1.22x slower                                                    |
| async_tree_none            | 492 ms                                                       | 625 ms: 1.27x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 211 ms: 2.31x slower                                                    |
| nbody          | 114 ms                                                       | 293 ms: 2.57x slower                                                    |
| Geometric mean | (ref)                                                        | 1.81x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.27 ms: 1.17x faster                                                   |
| regex_dna      | 259 ms                                                       | 241 ms: 1.07x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 32.2 ms: 1.04x slower                                                   |
| regex_compile  | 128 ms                                                       | 258 ms: 2.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.14x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 155 ms: 1.06x slower                                                    |
| json_loads           | 32.1 us                                                      | 38.4 us: 1.20x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 18.1 ms: 1.38x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 164 ms: 1.44x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 131 ms: 1.62x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.29 sec: 1.67x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 778 us: 2.17x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 546 us: 2.17x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.46x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 17.7 ms: 1.36x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.9 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.37x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 105 ms: 1.73x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 52.5 ms: 1.92x slower                                                   |
| django_template | 42.3 ms                                                      | 82.4 ms: 1.95x slower                                                   |
| mako            | 13.2 ms                                                      | 28.7 ms: 2.18x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.94x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.43 ms: 1.51x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.59 ms: 1.47x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.27 ms: 1.17x faster                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 6.25 ms: 1.12x faster                                                   |
| regex_dna                  | 259 ms                                                       | 241 ms: 1.07x faster                                                    |
| xml_etree_parse            | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| asyncio_websockets         | 657 ms                                                       | 668 ms: 1.02x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 32.2 ms: 1.04x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 155 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.48 sec: 1.12x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 871 ms: 1.14x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 698 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.42 sec: 1.16x slower                                                  |
| asyncio_tcp                | 584 ms                                                       | 681 ms: 1.17x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 925 ms: 1.17x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 762 ms: 1.18x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.9 ms: 1.18x slower                                                   |
| json_loads                 | 32.1 us                                                      | 38.4 us: 1.20x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 579 ms: 1.22x slower                                                    |
| json                       | 5.64 ms                                                      | 6.89 ms: 1.22x slower                                                   |
| deepcopy                   | 448 us                                                       | 562 us: 1.25x slower                                                    |
| telco                      | 10.0 ms                                                      | 12.6 ms: 1.26x slower                                                   |
| async_tree_none            | 492 ms                                                       | 625 ms: 1.27x slower                                                    |
| scimark_fft                | 445 ms                                                       | 589 ms: 1.32x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.42 sec: 1.33x slower                                                  |
| docutils                   | 3.10 sec                                                     | 4.12 sec: 1.33x slower                                                  |
| python_startup             | 13.0 ms                                                      | 17.7 ms: 1.36x slower                                                   |
| async_generators           | 488 ms                                                       | 667 ms: 1.37x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 39.9 ms: 1.38x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 18.1 ms: 1.38x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 11.9 ms: 1.38x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 9.16 ms: 1.40x slower                                                   |
| deepcopy_memo              | 50.8 us                                                      | 72.6 us: 1.43x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 164 ms: 1.44x slower                                                    |
| coverage                   | 98.4 ms                                                      | 142 ms: 1.44x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.87 ms: 1.49x slower                                                   |
| pylint                     | 337 ms                                                       | 507 ms: 1.50x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 6.11 us: 1.51x slower                                                   |
| generators                 | 37.1 ms                                                      | 57.2 ms: 1.54x slower                                                   |
| meteor_contest             | 113 ms                                                       | 176 ms: 1.55x slower                                                    |
| tornado_http               | 128 ms                                                       | 202 ms: 1.58x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 156 ms: 1.58x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 131 ms: 1.62x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 95.9 ms: 1.64x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 9.55 sec: 1.64x slower                                                  |
| spectral_norm              | 141 ms                                                       | 235 ms: 1.67x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.29 sec: 1.67x slower                                                  |
| pycparser                  | 1.22 sec                                                     | 2.06 sec: 1.69x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 35.3 ms: 1.69x slower                                                   |
| fannkuch                   | 451 ms                                                       | 769 ms: 1.71x slower                                                    |
| 2to3                       | 305 ms                                                       | 523 ms: 1.72x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 105 ms: 1.73x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 142 ms: 1.73x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 338 us: 1.75x slower                                                    |
| thrift                     | 962 us                                                       | 1.72 ms: 1.79x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 232 ms: 1.80x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.01 sec: 1.82x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 120 ms: 1.82x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 116 ms: 1.85x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 52.5 ms: 1.92x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 3.73 sec: 1.93x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.81 sec: 1.94x slower                                                  |
| django_template            | 42.3 ms                                                      | 82.4 ms: 1.95x slower                                                   |
| sympy_str                  | 265 ms                                                       | 519 ms: 1.96x slower                                                    |
| comprehensions             | 20.5 us                                                      | 40.8 us: 1.99x slower                                                   |
| regex_compile              | 128 ms                                                       | 258 ms: 2.01x slower                                                    |
| logging_simple             | 7.21 us                                                      | 14.6 us: 2.03x slower                                                   |
| logging_format             | 7.82 us                                                      | 16.0 us: 2.04x slower                                                   |
| logging_silent             | 133 ns                                                       | 276 ns: 2.07x slower                                                    |
| sympy_expand               | 457 ms                                                       | 956 ms: 2.09x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 172 ms: 2.09x slower                                                    |
| scimark_sor                | 159 ms                                                       | 340 ms: 2.13x slower                                                    |
| richards                   | 55.9 ms                                                      | 119 ms: 2.14x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 778 us: 2.17x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 546 us: 2.17x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.7 ms: 2.18x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 314 ms: 2.19x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.9 ms: 2.25x slower                                                   |
| richards_super             | 62.3 ms                                                      | 142 ms: 2.27x slower                                                    |
| float                      | 91.4 ms                                                      | 211 ms: 2.31x slower                                                    |
| chaos                      | 68.3 ms                                                      | 163 ms: 2.38x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 345 ms: 2.44x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.28 ms: 2.50x slower                                                   |
| nbody                      | 114 ms                                                       | 293 ms: 2.57x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 3.69 ms: 2.59x slower                                                   |
| raytrace                   | 297 ms                                                       | 824 ms: 2.78x slower                                                    |
| go                         | 161 ms                                                       | 449 ms: 2.79x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.3 ms: 3.18x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.57x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.42x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.15x