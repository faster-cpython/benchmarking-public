# Results vs. base

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.133x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                              | 357 ms: 1.21x slower                                                                                                      |
| docutils       | 2.99 sec                                                                                                            | 3.18 sec: 1.06x slower                                                                                                    |
| html5lib       | 64.3 ms                                                                                                             | 73.5 ms: 1.14x slower                                                                                                     |
| sphinx         | 1.14 sec                                                                                                            | 1.30 sec: 1.14x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.14x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 911 ms                                                                                                              | 863 ms: 1.06x faster                                                                                                      |
| async_tree_io           | 885 ms                                                                                                              | 902 ms: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed | 663 ms                                                                                                              | 689 ms: 1.04x slower                                                                                                      |
| async_tree_memoization  | 477 ms                                                                                                              | 511 ms: 1.07x slower                                                                                                      |
| asyncio_tcp             | 543 ms                                                                                                              | 589 ms: 1.08x slower                                                                                                      |
| async_tree_none         | 388 ms                                                                                                              | 428 ms: 1.10x slower                                                                                                      |
| asyncio_tcp_ssl         | 2.18 sec                                                                                                            | 2.43 sec: 1.12x slower                                                                                                    |
| async_generators        | 451 ms                                                                                                              | 514 ms: 1.14x slower                                                                                                      |
| Geometric mean          | (ref)                                                                                                               | 1.04x slower                                                                                                              |

Benchmark hidden because not significant (5): coroutines, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                                                                              | 231 ms: 1.01x faster                                                                                                      |
| float          | 87.7 ms                                                                                                             | 102 ms: 1.17x slower                                                                                                      |
| nbody          | 128 ms                                                                                                              | 181 ms: 1.42x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.18x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 29.4 ms                                                                                                             | 27.4 ms: 1.07x faster                                                                                                     |
| regex_dna      | 243 ms                                                                                                              | 248 ms: 1.02x slower                                                                                                      |
| regex_compile  | 128 ms                                                                                                              | 159 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 141 ms                                                                                                              | 127 ms: 1.11x faster                                                                                                      |
| pickle               | 15.7 us                                                                                                             | 15.0 us: 1.05x faster                                                                                                     |
| pickle_list          | 5.55 us                                                                                                             | 5.74 us: 1.03x slower                                                                                                     |
| json_loads           | 34.0 us                                                                                                             | 38.2 us: 1.12x slower                                                                                                     |
| pickle_pure_python   | 388 us                                                                                                              | 440 us: 1.14x slower                                                                                                      |
| unpickle_list        | 6.39 us                                                                                                             | 7.27 us: 1.14x slower                                                                                                     |
| unpickle_pure_python | 269 us                                                                                                              | 310 us: 1.15x slower                                                                                                      |
| unpickle             | 17.6 us                                                                                                             | 20.3 us: 1.16x slower                                                                                                     |
| xml_etree_generate   | 115 ms                                                                                                              | 134 ms: 1.16x slower                                                                                                      |
| json_dumps           | 13.7 ms                                                                                                             | 16.4 ms: 1.19x slower                                                                                                     |
| tomli_loads          | 2.50 sec                                                                                                            | 3.06 sec: 1.23x slower                                                                                                    |
| xml_etree_process    | 80.2 ms                                                                                                             | 98.6 ms: 1.23x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                               | 1.10x slower                                                                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.1 ms                                                                                                             | 19.6 ms: 1.22x slower                                                                                                     |
| python_startup_no_site | 10.2 ms                                                                                                             | 14.0 ms: 1.38x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.30x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.9 ms                                                                                                             | 74.0 ms: 1.22x slower                                                                                                     |
| django_template | 40.5 ms                                                                                                             | 53.5 ms: 1.32x slower                                                                                                     |
| genshi_text     | 26.7 ms                                                                                                             | 37.4 ms: 1.40x slower                                                                                                     |
| mako            | 14.3 ms                                                                                                             | 21.9 ms: 1.53x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.36x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 2.92 sec                                                                                                            | 57.7 ms: 50.57x faster                                                                                                    |
| gc_traversal             | 6.64 ms                                                                                                             | 2.71 ms: 2.45x faster                                                                                                     |
| create_gc_cycles         | 3.54 ms                                                                                                             | 2.08 ms: 1.71x faster                                                                                                     |
| xml_etree_iterparse      | 141 ms                                                                                                              | 127 ms: 1.11x faster                                                                                                      |
| sqlite_synth             | 3.82 us                                                                                                             | 3.44 us: 1.11x faster                                                                                                     |
| regex_v8                 | 29.4 ms                                                                                                             | 27.4 ms: 1.07x faster                                                                                                     |
| async_tree_io_tg         | 911 ms                                                                                                              | 863 ms: 1.06x faster                                                                                                      |
| pickle                   | 15.7 us                                                                                                             | 15.0 us: 1.05x faster                                                                                                     |
| pidigits                 | 234 ms                                                                                                              | 231 ms: 1.01x faster                                                                                                      |
| regex_dna                | 243 ms                                                                                                              | 248 ms: 1.02x slower                                                                                                      |
| async_tree_io            | 885 ms                                                                                                              | 902 ms: 1.02x slower                                                                                                      |
| pickle_list              | 5.55 us                                                                                                             | 5.74 us: 1.03x slower                                                                                                     |
| async_tree_cpu_io_mixed  | 663 ms                                                                                                              | 689 ms: 1.04x slower                                                                                                      |
| docutils                 | 2.99 sec                                                                                                            | 3.18 sec: 1.06x slower                                                                                                    |
| async_tree_memoization   | 477 ms                                                                                                              | 511 ms: 1.07x slower                                                                                                      |
| logging_silent           | 133 ns                                                                                                              | 143 ns: 1.08x slower                                                                                                      |
| pycparser                | 1.27 sec                                                                                                            | 1.37 sec: 1.08x slower                                                                                                    |
| pathlib                  | 22.0 ms                                                                                                             | 23.8 ms: 1.08x slower                                                                                                     |
| asyncio_tcp              | 543 ms                                                                                                              | 589 ms: 1.08x slower                                                                                                      |
| generators               | 36.5 ms                                                                                                             | 40.0 ms: 1.10x slower                                                                                                     |
| pyflate                  | 569 ms                                                                                                              | 625 ms: 1.10x slower                                                                                                      |
| async_tree_none          | 388 ms                                                                                                              | 428 ms: 1.10x slower                                                                                                      |
| json                     | 5.85 ms                                                                                                             | 6.47 ms: 1.11x slower                                                                                                     |
| asyncio_tcp_ssl          | 2.18 sec                                                                                                            | 2.43 sec: 1.12x slower                                                                                                    |
| scimark_fft              | 430 ms                                                                                                              | 481 ms: 1.12x slower                                                                                                      |
| mdp                      | 3.32 sec                                                                                                            | 3.71 sec: 1.12x slower                                                                                                    |
| k_core                   | 2.81 sec                                                                                                            | 3.14 sec: 1.12x slower                                                                                                    |
| json_loads               | 34.0 us                                                                                                             | 38.2 us: 1.12x slower                                                                                                     |
| scimark_sor              | 150 ms                                                                                                              | 169 ms: 1.12x slower                                                                                                      |
| pickle_pure_python       | 388 us                                                                                                              | 440 us: 1.14x slower                                                                                                      |
| unpickle_list            | 6.39 us                                                                                                             | 7.27 us: 1.14x slower                                                                                                     |
| sphinx                   | 1.14 sec                                                                                                            | 1.30 sec: 1.14x slower                                                                                                    |
| async_generators         | 451 ms                                                                                                              | 514 ms: 1.14x slower                                                                                                      |
| html5lib                 | 64.3 ms                                                                                                             | 73.5 ms: 1.14x slower                                                                                                     |
| dulwich_log              | 51.4 ms                                                                                                             | 59.2 ms: 1.15x slower                                                                                                     |
| unpickle_pure_python     | 269 us                                                                                                              | 310 us: 1.15x slower                                                                                                      |
| unpickle                 | 17.6 us                                                                                                             | 20.3 us: 1.16x slower                                                                                                     |
| connected_components     | 560 ms                                                                                                              | 649 ms: 1.16x slower                                                                                                      |
| shortest_path            | 577 ms                                                                                                              | 670 ms: 1.16x slower                                                                                                      |
| xml_etree_generate       | 115 ms                                                                                                              | 134 ms: 1.16x slower                                                                                                      |
| spectral_norm            | 122 ms                                                                                                              | 143 ms: 1.17x slower                                                                                                      |
| float                    | 87.7 ms                                                                                                             | 102 ms: 1.17x slower                                                                                                      |
| pprint_safe_repr         | 948 ms                                                                                                              | 1.11 sec: 1.17x slower                                                                                                    |
| go                       | 144 ms                                                                                                              | 169 ms: 1.18x slower                                                                                                      |
| sqlglot_v2_normalize     | 127 ms                                                                                                              | 150 ms: 1.18x slower                                                                                                      |
| pprint_pformat           | 1.92 sec                                                                                                            | 2.28 sec: 1.19x slower                                                                                                    |
| json_dumps               | 13.7 ms                                                                                                             | 16.4 ms: 1.19x slower                                                                                                     |
| deepcopy                 | 333 us                                                                                                              | 399 us: 1.20x slower                                                                                                      |
| pylint                   | 312 ms                                                                                                              | 373 ms: 1.20x slower                                                                                                      |
| sqlglot_v2_optimize      | 62.6 ms                                                                                                             | 75.3 ms: 1.20x slower                                                                                                     |
| thrift                   | 949 us                                                                                                              | 1.14 ms: 1.21x slower                                                                                                     |
| hexiom                   | 7.52 ms                                                                                                             | 9.08 ms: 1.21x slower                                                                                                     |
| 2to3                     | 296 ms                                                                                                              | 357 ms: 1.21x slower                                                                                                      |
| telco                    | 9.49 ms                                                                                                             | 11.5 ms: 1.21x slower                                                                                                     |
| nqueens                  | 105 ms                                                                                                              | 127 ms: 1.21x slower                                                                                                      |
| genshi_xml               | 60.9 ms                                                                                                             | 74.0 ms: 1.22x slower                                                                                                     |
| python_startup           | 16.1 ms                                                                                                             | 19.6 ms: 1.22x slower                                                                                                     |
| many_optionals           | 833 us                                                                                                              | 1.02 ms: 1.22x slower                                                                                                     |
| chaos                    | 71.3 ms                                                                                                             | 87.2 ms: 1.22x slower                                                                                                     |
| tomli_loads              | 2.50 sec                                                                                                            | 3.06 sec: 1.23x slower                                                                                                    |
| subparsers               | 25.8 ms                                                                                                             | 31.7 ms: 1.23x slower                                                                                                     |
| logging_simple           | 6.95 us                                                                                                             | 8.53 us: 1.23x slower                                                                                                     |
| xml_etree_process        | 80.2 ms                                                                                                             | 98.6 ms: 1.23x slower                                                                                                     |
| logging_format           | 7.60 us                                                                                                             | 9.42 us: 1.24x slower                                                                                                     |
| regex_compile            | 128 ms                                                                                                              | 159 ms: 1.24x slower                                                                                                      |
| crypto_pyaes             | 87.0 ms                                                                                                             | 108 ms: 1.25x slower                                                                                                      |
| deltablue                | 3.95 ms                                                                                                             | 4.97 ms: 1.26x slower                                                                                                     |
| sympy_expand             | 472 ms                                                                                                              | 595 ms: 1.26x slower                                                                                                      |
| scimark_sparse_mat_mult  | 6.54 ms                                                                                                             | 8.24 ms: 1.26x slower                                                                                                     |
| raytrace                 | 322 ms                                                                                                              | 407 ms: 1.26x slower                                                                                                      |
| comprehensions           | 21.3 us                                                                                                             | 26.9 us: 1.27x slower                                                                                                     |
| scimark_lu               | 150 ms                                                                                                              | 189 ms: 1.27x slower                                                                                                      |
| deepcopy_reduce          | 3.56 us                                                                                                             | 4.52 us: 1.27x slower                                                                                                     |
| sympy_str                | 277 ms                                                                                                              | 352 ms: 1.27x slower                                                                                                      |
| coverage                 | 100 ms                                                                                                              | 128 ms: 1.28x slower                                                                                                      |
| sympy_integrate          | 21.2 ms                                                                                                             | 27.1 ms: 1.28x slower                                                                                                     |
| bpe_tokeniser            | 5.65 sec                                                                                                            | 7.28 sec: 1.29x slower                                                                                                    |
| unpack_sequence          | 60.1 ns                                                                                                             | 77.6 ns: 1.29x slower                                                                                                     |
| sqlalchemy_declarative   | 145 ms                                                                                                              | 187 ms: 1.29x slower                                                                                                      |
| fannkuch                 | 502 ms                                                                                                              | 652 ms: 1.30x slower                                                                                                      |
| scimark_monte_carlo      | 84.5 ms                                                                                                             | 110 ms: 1.30x slower                                                                                                      |
| sqlglot_v2_transpile     | 1.79 ms                                                                                                             | 2.34 ms: 1.31x slower                                                                                                     |
| richards                 | 53.2 ms                                                                                                             | 69.8 ms: 1.31x slower                                                                                                     |
| deepcopy_memo            | 37.9 us                                                                                                             | 49.7 us: 1.31x slower                                                                                                     |
| meteor_contest           | 117 ms                                                                                                              | 155 ms: 1.32x slower                                                                                                      |
| django_template          | 40.5 ms                                                                                                             | 53.5 ms: 1.32x slower                                                                                                     |
| typing_runtime_protocols | 199 us                                                                                                              | 263 us: 1.32x slower                                                                                                      |
| sqlglot_v2_parse         | 1.45 ms                                                                                                             | 1.93 ms: 1.33x slower                                                                                                     |
| sympy_sum                | 144 ms                                                                                                              | 192 ms: 1.33x slower                                                                                                      |
| sqlalchemy_imperative    | 15.6 ms                                                                                                             | 21.1 ms: 1.36x slower                                                                                                     |
| bench_thread_pool        | 1.33 ms                                                                                                             | 1.82 ms: 1.37x slower                                                                                                     |
| python_startup_no_site   | 10.2 ms                                                                                                             | 14.0 ms: 1.38x slower                                                                                                     |
| richards_super           | 58.9 ms                                                                                                             | 81.7 ms: 1.39x slower                                                                                                     |
| genshi_text              | 26.7 ms                                                                                                             | 37.4 ms: 1.40x slower                                                                                                     |
| nbody                    | 128 ms                                                                                                              | 181 ms: 1.42x slower                                                                                                      |
| mako                     | 14.3 ms                                                                                                             | 21.9 ms: 1.53x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                               | 1.11x slower                                                                                                              |

Benchmark hidden because not significant (8): coroutines, xml_etree_parse, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, pickle_dict, async_tree_none_tg, regex_effbot

- Geometric mean (including insignificant results): 1.133x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.21x