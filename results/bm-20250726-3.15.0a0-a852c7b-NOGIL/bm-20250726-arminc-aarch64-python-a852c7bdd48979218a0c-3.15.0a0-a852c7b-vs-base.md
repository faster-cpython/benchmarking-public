# Results vs. base

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.126x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 301 ms                                                                                                            | 354 ms: 1.18x slower                                                                                                    |
| docutils       | 2.97 sec                                                                                                          | 3.16 sec: 1.06x slower                                                                                                  |
| html5lib       | 61.5 ms                                                                                                           | 70.4 ms: 1.14x slower                                                                                                   |
| sphinx         | 1.14 sec                                                                                                          | 1.29 sec: 1.14x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                                                                            | 824 ms: 1.09x faster                                                                                                    |
| async_tree_memoization_tg  | 456 ms                                                                                                            | 445 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 373 ms                                                                                                            | 366 ms: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 646 ms                                                                                                            | 633 ms: 1.02x faster                                                                                                    |
| async_tree_memoization     | 459 ms                                                                                                            | 472 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 655 ms                                                                                                            | 674 ms: 1.03x slower                                                                                                    |
| async_tree_none            | 381 ms                                                                                                            | 397 ms: 1.04x slower                                                                                                    |
| asyncio_tcp                | 545 ms                                                                                                            | 573 ms: 1.05x slower                                                                                                    |
| coroutines                 | 29.6 ms                                                                                                           | 31.4 ms: 1.06x slower                                                                                                   |
| async_generators           | 453 ms                                                                                                            | 500 ms: 1.11x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                                                                          | 2.45 sec: 1.12x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 85.6 ms                                                                                                           | 93.8 ms: 1.10x slower                                                                                                   |
| nbody          | 125 ms                                                                                                            | 182 ms: 1.46x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.16x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                                                                           | 3.76 ms: 1.02x faster                                                                                                   |
| regex_dna      | 223 ms                                                                                                            | 240 ms: 1.08x slower                                                                                                    |
| regex_compile  | 124 ms                                                                                                            | 149 ms: 1.20x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 142 ms                                                                                                            | 133 ms: 1.07x faster                                                                                                    |
| pickle               | 15.6 us                                                                                                           | 15.0 us: 1.04x faster                                                                                                   |
| json_dumps           | 13.5 ms                                                                                                           | 14.8 ms: 1.09x slower                                                                                                   |
| unpickle             | 18.4 us                                                                                                           | 20.2 us: 1.10x slower                                                                                                   |
| unpickle_pure_python | 265 us                                                                                                            | 301 us: 1.14x slower                                                                                                    |
| json_loads           | 33.1 us                                                                                                           | 37.6 us: 1.14x slower                                                                                                   |
| pickle_pure_python   | 391 us                                                                                                            | 452 us: 1.16x slower                                                                                                    |
| tomli_loads          | 2.44 sec                                                                                                          | 2.89 sec: 1.18x slower                                                                                                  |
| xml_etree_generate   | 113 ms                                                                                                            | 139 ms: 1.23x slower                                                                                                    |
| xml_etree_process    | 80.1 ms                                                                                                           | 100 ms: 1.25x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (4): pickle_list, xml_etree_parse, pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                                                           | 20.0 ms: 1.34x slower                                                                                                   |
| python_startup_no_site | 8.54 ms                                                                                                           | 12.2 ms: 1.42x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.38x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 62.2 ms                                                                                                           | 75.7 ms: 1.22x slower                                                                                                   |
| genshi_text     | 28.0 ms                                                                                                           | 35.7 ms: 1.27x slower                                                                                                   |
| django_template | 39.2 ms                                                                                                           | 51.3 ms: 1.31x slower                                                                                                   |
| mako            | 13.7 ms                                                                                                           | 21.3 ms: 1.55x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.33x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 2.17 sec                                                                                                          | 64.7 ms: 33.53x faster                                                                                                  |
| gc_traversal               | 6.78 ms                                                                                                           | 2.92 ms: 2.32x faster                                                                                                   |
| create_gc_cycles           | 3.76 ms                                                                                                           | 2.28 ms: 1.65x faster                                                                                                   |
| sqlite_synth               | 3.76 us                                                                                                           | 3.44 us: 1.10x faster                                                                                                   |
| async_tree_io_tg           | 900 ms                                                                                                            | 824 ms: 1.09x faster                                                                                                    |
| xml_etree_iterparse        | 142 ms                                                                                                            | 133 ms: 1.07x faster                                                                                                    |
| pickle                     | 15.6 us                                                                                                           | 15.0 us: 1.04x faster                                                                                                   |
| async_tree_memoization_tg  | 456 ms                                                                                                            | 445 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 373 ms                                                                                                            | 366 ms: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 646 ms                                                                                                            | 633 ms: 1.02x faster                                                                                                    |
| regex_effbot               | 3.83 ms                                                                                                           | 3.76 ms: 1.02x faster                                                                                                   |
| async_tree_memoization     | 459 ms                                                                                                            | 472 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 655 ms                                                                                                            | 674 ms: 1.03x slower                                                                                                    |
| pathlib                    | 22.7 ms                                                                                                           | 23.5 ms: 1.03x slower                                                                                                   |
| async_tree_none            | 381 ms                                                                                                            | 397 ms: 1.04x slower                                                                                                    |
| asyncio_tcp                | 545 ms                                                                                                            | 573 ms: 1.05x slower                                                                                                    |
| docutils                   | 2.97 sec                                                                                                          | 3.16 sec: 1.06x slower                                                                                                  |
| coroutines                 | 29.6 ms                                                                                                           | 31.4 ms: 1.06x slower                                                                                                   |
| scimark_sparse_mat_mult    | 7.19 ms                                                                                                           | 7.71 ms: 1.07x slower                                                                                                   |
| logging_silent             | 131 ns                                                                                                            | 140 ns: 1.07x slower                                                                                                    |
| regex_dna                  | 223 ms                                                                                                            | 240 ms: 1.08x slower                                                                                                    |
| pycparser                  | 1.25 sec                                                                                                          | 1.35 sec: 1.08x slower                                                                                                  |
| k_core                     | 2.82 sec                                                                                                          | 3.07 sec: 1.09x slower                                                                                                  |
| json                       | 5.84 ms                                                                                                           | 6.36 ms: 1.09x slower                                                                                                   |
| json_dumps                 | 13.5 ms                                                                                                           | 14.8 ms: 1.09x slower                                                                                                   |
| float                      | 85.6 ms                                                                                                           | 93.8 ms: 1.10x slower                                                                                                   |
| unpickle                   | 18.4 us                                                                                                           | 20.2 us: 1.10x slower                                                                                                   |
| scimark_fft                | 424 ms                                                                                                            | 467 ms: 1.10x slower                                                                                                    |
| async_generators           | 453 ms                                                                                                            | 500 ms: 1.11x slower                                                                                                    |
| pyflate                    | 527 ms                                                                                                            | 588 ms: 1.12x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                                                                          | 2.45 sec: 1.12x slower                                                                                                  |
| generators                 | 35.9 ms                                                                                                           | 40.3 ms: 1.12x slower                                                                                                   |
| scimark_sor                | 143 ms                                                                                                            | 162 ms: 1.13x slower                                                                                                    |
| sphinx                     | 1.14 sec                                                                                                          | 1.29 sec: 1.14x slower                                                                                                  |
| unpickle_pure_python       | 265 us                                                                                                            | 301 us: 1.14x slower                                                                                                    |
| json_loads                 | 33.1 us                                                                                                           | 37.6 us: 1.14x slower                                                                                                   |
| html5lib                   | 61.5 ms                                                                                                           | 70.4 ms: 1.14x slower                                                                                                   |
| hexiom                     | 6.81 ms                                                                                                           | 7.81 ms: 1.15x slower                                                                                                   |
| spectral_norm              | 123 ms                                                                                                            | 142 ms: 1.15x slower                                                                                                    |
| telco                      | 163 ms                                                                                                            | 189 ms: 1.16x slower                                                                                                    |
| dulwich_log                | 51.3 ms                                                                                                           | 59.3 ms: 1.16x slower                                                                                                   |
| pickle_pure_python         | 391 us                                                                                                            | 452 us: 1.16x slower                                                                                                    |
| pprint_safe_repr           | 894 ms                                                                                                            | 1.04 sec: 1.17x slower                                                                                                  |
| logging_simple             | 6.86 us                                                                                                           | 8.03 us: 1.17x slower                                                                                                   |
| shortest_path              | 581 ms                                                                                                            | 682 ms: 1.17x slower                                                                                                    |
| 2to3                       | 301 ms                                                                                                            | 354 ms: 1.18x slower                                                                                                    |
| pprint_pformat             | 1.82 sec                                                                                                          | 2.14 sec: 1.18x slower                                                                                                  |
| tomli_loads                | 2.44 sec                                                                                                          | 2.89 sec: 1.18x slower                                                                                                  |
| mdp                        | 1.64 sec                                                                                                          | 1.93 sec: 1.18x slower                                                                                                  |
| scimark_lu                 | 155 ms                                                                                                            | 184 ms: 1.18x slower                                                                                                    |
| sqlglot_v2_normalize       | 125 ms                                                                                                            | 148 ms: 1.19x slower                                                                                                    |
| deltablue                  | 3.99 ms                                                                                                           | 4.74 ms: 1.19x slower                                                                                                   |
| connected_components       | 557 ms                                                                                                            | 662 ms: 1.19x slower                                                                                                    |
| regex_compile              | 124 ms                                                                                                            | 149 ms: 1.20x slower                                                                                                    |
| deepcopy_reduce            | 3.56 us                                                                                                           | 4.27 us: 1.20x slower                                                                                                   |
| logging_format             | 7.57 us                                                                                                           | 9.09 us: 1.20x slower                                                                                                   |
| raytrace                   | 327 ms                                                                                                            | 394 ms: 1.20x slower                                                                                                    |
| chaos                      | 67.7 ms                                                                                                           | 81.9 ms: 1.21x slower                                                                                                   |
| sqlglot_v2_optimize        | 60.6 ms                                                                                                           | 73.4 ms: 1.21x slower                                                                                                   |
| many_optionals             | 924 us                                                                                                            | 1.12 ms: 1.21x slower                                                                                                   |
| deepcopy                   | 325 us                                                                                                            | 395 us: 1.22x slower                                                                                                    |
| pylint                     | 316 ms                                                                                                            | 385 ms: 1.22x slower                                                                                                    |
| genshi_xml                 | 62.2 ms                                                                                                           | 75.7 ms: 1.22x slower                                                                                                   |
| nqueens                    | 98.5 ms                                                                                                           | 121 ms: 1.23x slower                                                                                                    |
| xml_etree_generate         | 113 ms                                                                                                            | 139 ms: 1.23x slower                                                                                                    |
| go                         | 126 ms                                                                                                            | 154 ms: 1.23x slower                                                                                                    |
| meteor_contest             | 111 ms                                                                                                            | 136 ms: 1.23x slower                                                                                                    |
| deepcopy_memo              | 37.4 us                                                                                                           | 46.1 us: 1.23x slower                                                                                                   |
| sympy_expand               | 476 ms                                                                                                            | 589 ms: 1.24x slower                                                                                                    |
| subparsers                 | 48.6 ms                                                                                                           | 60.4 ms: 1.24x slower                                                                                                   |
| comprehensions             | 19.8 us                                                                                                           | 24.6 us: 1.24x slower                                                                                                   |
| bpe_tokeniser              | 5.51 sec                                                                                                          | 6.89 sec: 1.25x slower                                                                                                  |
| xml_etree_process          | 80.1 ms                                                                                                           | 100 ms: 1.25x slower                                                                                                    |
| typing_runtime_protocols   | 194 us                                                                                                            | 244 us: 1.26x slower                                                                                                    |
| thrift                     | 954 us                                                                                                            | 1.20 ms: 1.26x slower                                                                                                   |
| sympy_str                  | 273 ms                                                                                                            | 345 ms: 1.27x slower                                                                                                    |
| sympy_sum                  | 147 ms                                                                                                            | 186 ms: 1.27x slower                                                                                                    |
| sqlglot_v2_parse           | 1.42 ms                                                                                                           | 1.80 ms: 1.27x slower                                                                                                   |
| genshi_text                | 28.0 ms                                                                                                           | 35.7 ms: 1.27x slower                                                                                                   |
| crypto_pyaes               | 83.6 ms                                                                                                           | 107 ms: 1.28x slower                                                                                                    |
| fannkuch                   | 463 ms                                                                                                            | 596 ms: 1.29x slower                                                                                                    |
| django_template            | 39.2 ms                                                                                                           | 51.3 ms: 1.31x slower                                                                                                   |
| scimark_monte_carlo        | 78.8 ms                                                                                                           | 103 ms: 1.31x slower                                                                                                    |
| sympy_integrate            | 19.9 ms                                                                                                           | 26.1 ms: 1.31x slower                                                                                                   |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                           | 2.30 ms: 1.32x slower                                                                                                   |
| richards                   | 53.2 ms                                                                                                           | 70.8 ms: 1.33x slower                                                                                                   |
| python_startup             | 15.0 ms                                                                                                           | 20.0 ms: 1.34x slower                                                                                                   |
| bench_thread_pool          | 1.37 ms                                                                                                           | 1.83 ms: 1.34x slower                                                                                                   |
| richards_super             | 59.0 ms                                                                                                           | 82.2 ms: 1.39x slower                                                                                                   |
| coverage                   | 102 ms                                                                                                            | 143 ms: 1.39x slower                                                                                                    |
| unpack_sequence            | 51.1 ns                                                                                                           | 72.7 ns: 1.42x slower                                                                                                   |
| python_startup_no_site     | 8.54 ms                                                                                                           | 12.2 ms: 1.42x slower                                                                                                   |
| nbody                      | 125 ms                                                                                                            | 182 ms: 1.46x slower                                                                                                    |
| mako                       | 13.7 ms                                                                                                           | 21.3 ms: 1.55x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.10x slower                                                                                                            |

Benchmark hidden because not significant (8): regex_v8, pickle_list, pidigits, asyncio_websockets, async_tree_io, xml_etree_parse, pickle_dict, unpickle_list
Ignored benchmarks (1) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: djangocms

- Geometric mean (including insignificant results): 1.126x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.20x