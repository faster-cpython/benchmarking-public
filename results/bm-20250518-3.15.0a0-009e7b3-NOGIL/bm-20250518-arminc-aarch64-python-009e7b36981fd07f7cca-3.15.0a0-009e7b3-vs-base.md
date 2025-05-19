# Results vs. base

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.052x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 299 ms                                                                                                            | 352 ms: 1.18x slower                                                                                                    |
| docutils       | 2.94 sec                                                                                                          | 3.24 sec: 1.10x slower                                                                                                  |
| html5lib       | 63.0 ms                                                                                                           | 68.6 ms: 1.09x slower                                                                                                   |
| sphinx         | 1.15 sec                                                                                                          | 1.30 sec: 1.13x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.12x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 903 ms                                                                                                            | 841 ms: 1.07x faster                                                                                                    |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 452 ms: 1.03x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 638 ms: 1.03x faster                                                                                                    |
| coroutines                 | 29.5 ms                                                                                                           | 30.3 ms: 1.03x slower                                                                                                   |
| async_tree_none            | 392 ms                                                                                                            | 409 ms: 1.04x slower                                                                                                    |
| async_tree_memoization     | 461 ms                                                                                                            | 482 ms: 1.05x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 649 ms                                                                                                            | 684 ms: 1.05x slower                                                                                                    |
| asyncio_tcp                | 539 ms                                                                                                            | 582 ms: 1.08x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.41 sec: 1.10x slower                                                                                                  |
| async_generators           | 449 ms                                                                                                            | 498 ms: 1.11x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (3): async_tree_none_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 238 ms                                                                                                            | 231 ms: 1.03x faster                                                                                                    |
| float          | 86.4 ms                                                                                                           | 95.5 ms: 1.10x slower                                                                                                   |
| nbody          | 122 ms                                                                                                            | 170 ms: 1.40x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.14x slower                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 231 ms                                                                                                            | 238 ms: 1.03x slower                                                                                                    |
| regex_effbot   | 3.82 ms                                                                                                           | 3.96 ms: 1.04x slower                                                                                                   |
| regex_compile  | 122 ms                                                                                                            | 151 ms: 1.23x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 141 ms                                                                                                            | 128 ms: 1.10x faster                                                                                                    |
| json_dumps           | 13.6 ms                                                                                                           | 14.7 ms: 1.08x slower                                                                                                   |
| unpickle_list        | 6.45 us                                                                                                           | 6.97 us: 1.08x slower                                                                                                   |
| json_loads           | 36.0 us                                                                                                           | 39.0 us: 1.08x slower                                                                                                   |
| pickle_pure_python   | 382 us                                                                                                            | 428 us: 1.12x slower                                                                                                    |
| unpickle             | 18.2 us                                                                                                           | 21.0 us: 1.16x slower                                                                                                   |
| unpickle_pure_python | 262 us                                                                                                            | 302 us: 1.16x slower                                                                                                    |
| tomli_loads          | 2.44 sec                                                                                                          | 2.84 sec: 1.16x slower                                                                                                  |
| xml_etree_generate   | 114 ms                                                                                                            | 142 ms: 1.24x slower                                                                                                    |
| xml_etree_process    | 79.3 ms                                                                                                           | 101 ms: 1.27x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (4): pickle_list, pickle, xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 20.1 ms: 1.34x slower                                                                                                   |
| python_startup_no_site | 8.62 ms                                                                                                           | 12.2 ms: 1.42x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.38x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                                                                           | 72.1 ms: 1.20x slower                                                                                                   |
| django_template | 39.5 ms                                                                                                           | 50.6 ms: 1.28x slower                                                                                                   |
| genshi_text     | 26.7 ms                                                                                                           | 35.0 ms: 1.31x slower                                                                                                   |
| mako            | 13.9 ms                                                                                                           | 21.3 ms: 1.53x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.32x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| thrift                     | 197 ms                                                                                                            | 1.16 ms: 169.40x faster                                                                                                 |
| bench_mp_pool              | 4.22 sec                                                                                                          | 62.3 ms: 67.74x faster                                                                                                  |
| coverage                   | 548 ms                                                                                                            | 146 ms: 3.75x faster                                                                                                    |
| gc_traversal               | 6.82 ms                                                                                                           | 2.88 ms: 2.37x faster                                                                                                   |
| create_gc_cycles           | 3.76 ms                                                                                                           | 2.30 ms: 1.63x faster                                                                                                   |
| sqlite_synth               | 3.94 us                                                                                                           | 3.46 us: 1.14x faster                                                                                                   |
| xml_etree_iterparse        | 141 ms                                                                                                            | 128 ms: 1.10x faster                                                                                                    |
| async_tree_io_tg           | 903 ms                                                                                                            | 841 ms: 1.07x faster                                                                                                    |
| pidigits                   | 238 ms                                                                                                            | 231 ms: 1.03x faster                                                                                                    |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 452 ms: 1.03x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 638 ms: 1.03x faster                                                                                                    |
| coroutines                 | 29.5 ms                                                                                                           | 30.3 ms: 1.03x slower                                                                                                   |
| regex_dna                  | 231 ms                                                                                                            | 238 ms: 1.03x slower                                                                                                    |
| regex_effbot               | 3.82 ms                                                                                                           | 3.96 ms: 1.04x slower                                                                                                   |
| async_tree_none            | 392 ms                                                                                                            | 409 ms: 1.04x slower                                                                                                    |
| async_tree_memoization     | 461 ms                                                                                                            | 482 ms: 1.05x slower                                                                                                    |
| scimark_fft                | 439 ms                                                                                                            | 460 ms: 1.05x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 649 ms                                                                                                            | 684 ms: 1.05x slower                                                                                                    |
| pycparser                  | 1.26 sec                                                                                                          | 1.35 sec: 1.07x slower                                                                                                  |
| generators                 | 37.5 ms                                                                                                           | 40.3 ms: 1.07x slower                                                                                                   |
| spectral_norm              | 130 ms                                                                                                            | 140 ms: 1.08x slower                                                                                                    |
| json_dumps                 | 13.6 ms                                                                                                           | 14.7 ms: 1.08x slower                                                                                                   |
| asyncio_tcp                | 539 ms                                                                                                            | 582 ms: 1.08x slower                                                                                                    |
| unpickle_list              | 6.45 us                                                                                                           | 6.97 us: 1.08x slower                                                                                                   |
| json_loads                 | 36.0 us                                                                                                           | 39.0 us: 1.08x slower                                                                                                   |
| json                       | 6.11 ms                                                                                                           | 6.63 ms: 1.09x slower                                                                                                   |
| html5lib                   | 63.0 ms                                                                                                           | 68.6 ms: 1.09x slower                                                                                                   |
| scimark_sor                | 146 ms                                                                                                            | 159 ms: 1.09x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.41 sec: 1.10x slower                                                                                                  |
| scimark_sparse_mat_mult    | 6.99 ms                                                                                                           | 7.67 ms: 1.10x slower                                                                                                   |
| docutils                   | 2.94 sec                                                                                                          | 3.24 sec: 1.10x slower                                                                                                  |
| float                      | 86.4 ms                                                                                                           | 95.5 ms: 1.10x slower                                                                                                   |
| async_generators           | 449 ms                                                                                                            | 498 ms: 1.11x slower                                                                                                    |
| dulwich_log                | 54.7 ms                                                                                                           | 61.1 ms: 1.12x slower                                                                                                   |
| pickle_pure_python         | 382 us                                                                                                            | 428 us: 1.12x slower                                                                                                    |
| chaos                      | 70.3 ms                                                                                                           | 78.9 ms: 1.12x slower                                                                                                   |
| sphinx                     | 1.15 sec                                                                                                          | 1.30 sec: 1.13x slower                                                                                                  |
| hexiom                     | 7.25 ms                                                                                                           | 8.24 ms: 1.14x slower                                                                                                   |
| nqueens                    | 102 ms                                                                                                            | 116 ms: 1.14x slower                                                                                                    |
| pyflate                    | 525 ms                                                                                                            | 600 ms: 1.14x slower                                                                                                    |
| k_core                     | 2.80 sec                                                                                                          | 3.24 sec: 1.15x slower                                                                                                  |
| unpickle                   | 18.2 us                                                                                                           | 21.0 us: 1.16x slower                                                                                                   |
| unpickle_pure_python       | 262 us                                                                                                            | 302 us: 1.16x slower                                                                                                    |
| deepcopy                   | 333 us                                                                                                            | 386 us: 1.16x slower                                                                                                    |
| tomli_loads                | 2.44 sec                                                                                                          | 2.84 sec: 1.16x slower                                                                                                  |
| sqlglot_v2_optimize        | 61.7 ms                                                                                                           | 72.1 ms: 1.17x slower                                                                                                   |
| deepcopy_reduce            | 3.58 us                                                                                                           | 4.18 us: 1.17x slower                                                                                                   |
| sqlglot_v2_normalize       | 124 ms                                                                                                            | 146 ms: 1.17x slower                                                                                                    |
| pprint_safe_repr           | 905 ms                                                                                                            | 1.07 sec: 1.18x slower                                                                                                  |
| 2to3                       | 299 ms                                                                                                            | 352 ms: 1.18x slower                                                                                                    |
| connected_components       | 552 ms                                                                                                            | 653 ms: 1.18x slower                                                                                                    |
| telco                      | 9.57 ms                                                                                                           | 11.3 ms: 1.18x slower                                                                                                   |
| scimark_lu                 | 148 ms                                                                                                            | 175 ms: 1.18x slower                                                                                                    |
| shortest_path              | 573 ms                                                                                                            | 681 ms: 1.19x slower                                                                                                    |
| pprint_pformat             | 1.85 sec                                                                                                          | 2.20 sec: 1.19x slower                                                                                                  |
| raytrace                   | 322 ms                                                                                                            | 383 ms: 1.19x slower                                                                                                    |
| many_optionals             | 878 us                                                                                                            | 1.05 ms: 1.19x slower                                                                                                   |
| genshi_xml                 | 60.3 ms                                                                                                           | 72.1 ms: 1.20x slower                                                                                                   |
| mdp                        | 1.65 sec                                                                                                          | 1.97 sec: 1.20x slower                                                                                                  |
| logging_simple             | 7.57 us                                                                                                           | 9.07 us: 1.20x slower                                                                                                   |
| go                         | 131 ms                                                                                                            | 158 ms: 1.20x slower                                                                                                    |
| subparsers                 | 29.0 ms                                                                                                           | 35.0 ms: 1.20x slower                                                                                                   |
| logging_format             | 8.27 us                                                                                                           | 10.1 us: 1.23x slower                                                                                                   |
| regex_compile              | 122 ms                                                                                                            | 151 ms: 1.23x slower                                                                                                    |
| sympy_expand               | 469 ms                                                                                                            | 581 ms: 1.24x slower                                                                                                    |
| xml_etree_generate         | 114 ms                                                                                                            | 142 ms: 1.24x slower                                                                                                    |
| bpe_tokeniser              | 5.56 sec                                                                                                          | 6.93 sec: 1.25x slower                                                                                                  |
| scimark_monte_carlo        | 82.9 ms                                                                                                           | 103 ms: 1.25x slower                                                                                                    |
| pylint                     | 307 ms                                                                                                            | 383 ms: 1.25x slower                                                                                                    |
| deltablue                  | 3.74 ms                                                                                                           | 4.68 ms: 1.25x slower                                                                                                   |
| deepcopy_memo              | 38.0 us                                                                                                           | 48.1 us: 1.27x slower                                                                                                   |
| logging_silent             | 604 ns                                                                                                            | 765 ns: 1.27x slower                                                                                                    |
| sympy_str                  | 270 ms                                                                                                            | 343 ms: 1.27x slower                                                                                                    |
| xml_etree_process          | 79.3 ms                                                                                                           | 101 ms: 1.27x slower                                                                                                    |
| comprehensions             | 21.2 us                                                                                                           | 27.0 us: 1.27x slower                                                                                                   |
| crypto_pyaes               | 86.2 ms                                                                                                           | 110 ms: 1.27x slower                                                                                                    |
| sympy_sum                  | 147 ms                                                                                                            | 188 ms: 1.28x slower                                                                                                    |
| django_template            | 39.5 ms                                                                                                           | 50.6 ms: 1.28x slower                                                                                                   |
| sympy_integrate            | 20.2 ms                                                                                                           | 25.9 ms: 1.28x slower                                                                                                   |
| sqlglot_v2_parse           | 1.41 ms                                                                                                           | 1.82 ms: 1.29x slower                                                                                                   |
| genshi_text                | 26.7 ms                                                                                                           | 35.0 ms: 1.31x slower                                                                                                   |
| sqlglot_v2_transpile       | 1.74 ms                                                                                                           | 2.29 ms: 1.31x slower                                                                                                   |
| meteor_contest             | 114 ms                                                                                                            | 151 ms: 1.32x slower                                                                                                    |
| fannkuch                   | 466 ms                                                                                                            | 618 ms: 1.33x slower                                                                                                    |
| typing_runtime_protocols   | 203 us                                                                                                            | 271 us: 1.33x slower                                                                                                    |
| python_startup             | 15.1 ms                                                                                                           | 20.1 ms: 1.34x slower                                                                                                   |
| bench_thread_pool          | 1.35 ms                                                                                                           | 1.81 ms: 1.34x slower                                                                                                   |
| richards                   | 50.5 ms                                                                                                           | 68.3 ms: 1.35x slower                                                                                                   |
| richards_super             | 57.5 ms                                                                                                           | 78.3 ms: 1.36x slower                                                                                                   |
| nbody                      | 122 ms                                                                                                            | 170 ms: 1.40x slower                                                                                                    |
| python_startup_no_site     | 8.62 ms                                                                                                           | 12.2 ms: 1.42x slower                                                                                                   |
| unpack_sequence            | 50.8 ns                                                                                                           | 73.4 ns: 1.44x slower                                                                                                   |
| mako                       | 13.9 ms                                                                                                           | 21.3 ms: 1.53x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (9): regex_v8, async_tree_none_tg, asyncio_websockets, async_tree_io, pickle_list, pickle, xml_etree_parse, pickle_dict, pathlib

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.22x