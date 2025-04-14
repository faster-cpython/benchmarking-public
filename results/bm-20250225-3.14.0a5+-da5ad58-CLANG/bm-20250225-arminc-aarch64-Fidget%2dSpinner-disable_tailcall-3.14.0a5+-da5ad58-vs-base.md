# Results vs. base

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-aarch64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.119x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 300 ms                                                                   | 337 ms: 1.12x slower                                                           |
| docutils       | 3.01 sec                                                                 | 3.16 sec: 1.05x slower                                                         |
| html5lib       | 59.9 ms                                                                  | 70.3 ms: 1.17x slower                                                          |
| sphinx         | 1.13 sec                                                                 | 1.23 sec: 1.09x slower                                                         |
| Geometric mean | (ref)                                                                    | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 735 ms                                                                   | 761 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed    | 745 ms                                                                   | 789 ms: 1.06x slower                                                           |
| async_tree_io_tg           | 912 ms                                                                   | 993 ms: 1.09x slower                                                           |
| async_tree_io              | 904 ms                                                                   | 999 ms: 1.11x slower                                                           |
| async_tree_none_tg         | 377 ms                                                                   | 422 ms: 1.12x slower                                                           |
| async_tree_memoization     | 475 ms                                                                   | 534 ms: 1.13x slower                                                           |
| async_tree_memoization_tg  | 467 ms                                                                   | 529 ms: 1.13x slower                                                           |
| async_tree_none            | 383 ms                                                                   | 434 ms: 1.13x slower                                                           |
| coroutines                 | 28.5 ms                                                                  | 32.4 ms: 1.14x slower                                                          |
| async_generators           | 415 ms                                                                   | 484 ms: 1.17x slower                                                           |
| Geometric mean             | (ref)                                                                    | 1.10x slower                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 86.3 ms                                                                  | 100 ms: 1.16x slower                                                           |
| nbody          | 118 ms                                                                   | 145 ms: 1.24x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.13x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 123 ms                                                                   | 156 ms: 1.27x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.05x slower                                                                   |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 155 ms                                                                   | 164 ms: 1.06x slower                                                           |
| json_dumps           | 14.5 ms                                                                  | 15.9 ms: 1.10x slower                                                          |
| xml_etree_generate   | 110 ms                                                                   | 125 ms: 1.14x slower                                                           |
| pickle_pure_python   | 385 us                                                                   | 465 us: 1.21x slower                                                           |
| xml_etree_process    | 74.8 ms                                                                  | 92.9 ms: 1.24x slower                                                          |
| unpickle_pure_python | 255 us                                                                   | 333 us: 1.31x slower                                                           |
| tomli_loads          | 2.47 sec                                                                 | 3.26 sec: 1.32x slower                                                         |
| Geometric mean       | (ref)                                                                    | 1.15x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                  | 16.9 ms: 1.03x slower                                                          |
| python_startup_no_site | 9.09 ms                                                                  | 9.39 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 13.7 ms                                                                  | 16.0 ms: 1.17x slower                                                          |
| django_template | 38.4 ms                                                                  | 45.5 ms: 1.18x slower                                                          |
| genshi_xml      | 60.1 ms                                                                  | 73.1 ms: 1.22x slower                                                          |
| genshi_text     | 26.9 ms                                                                  | 33.7 ms: 1.26x slower                                                          |
| Geometric mean  | (ref)                                                                    | 1.21x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| shortest_path              | 569 ms                                                                   | 582 ms: 1.02x slower                                                           |
| python_startup             | 16.4 ms                                                                  | 16.9 ms: 1.03x slower                                                          |
| python_startup_no_site     | 9.09 ms                                                                  | 9.39 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 735 ms                                                                   | 761 ms: 1.04x slower                                                           |
| k_core                     | 2.83 sec                                                                 | 2.95 sec: 1.04x slower                                                         |
| docutils                   | 3.01 sec                                                                 | 3.16 sec: 1.05x slower                                                         |
| connected_components       | 535 ms                                                                   | 561 ms: 1.05x slower                                                           |
| mdp                        | 3.27 sec                                                                 | 3.46 sec: 1.06x slower                                                         |
| xml_etree_iterparse        | 155 ms                                                                   | 164 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed    | 745 ms                                                                   | 789 ms: 1.06x slower                                                           |
| sqlalchemy_declarative     | 145 ms                                                                   | 154 ms: 1.06x slower                                                           |
| sqlalchemy_imperative      | 16.1 ms                                                                  | 17.4 ms: 1.08x slower                                                          |
| async_tree_io_tg           | 912 ms                                                                   | 993 ms: 1.09x slower                                                           |
| meteor_contest             | 120 ms                                                                   | 131 ms: 1.09x slower                                                           |
| sphinx                     | 1.13 sec                                                                 | 1.23 sec: 1.09x slower                                                         |
| telco                      | 9.22 ms                                                                  | 10.1 ms: 1.10x slower                                                          |
| json_dumps                 | 14.5 ms                                                                  | 15.9 ms: 1.10x slower                                                          |
| bench_thread_pool          | 1.27 ms                                                                  | 1.40 ms: 1.10x slower                                                          |
| coverage                   | 94.0 ms                                                                  | 104 ms: 1.10x slower                                                           |
| async_tree_io              | 904 ms                                                                   | 999 ms: 1.11x slower                                                           |
| sympy_str                  | 272 ms                                                                   | 303 ms: 1.11x slower                                                           |
| async_tree_none_tg         | 377 ms                                                                   | 422 ms: 1.12x slower                                                           |
| 2to3                       | 300 ms                                                                   | 337 ms: 1.12x slower                                                           |
| spectral_norm              | 111 ms                                                                   | 125 ms: 1.12x slower                                                           |
| async_tree_memoization     | 475 ms                                                                   | 534 ms: 1.13x slower                                                           |
| pycparser                  | 1.28 sec                                                                 | 1.44 sec: 1.13x slower                                                         |
| bpe_tokeniser              | 5.42 sec                                                                 | 6.13 sec: 1.13x slower                                                         |
| async_tree_memoization_tg  | 467 ms                                                                   | 529 ms: 1.13x slower                                                           |
| sympy_integrate            | 20.7 ms                                                                  | 23.5 ms: 1.13x slower                                                          |
| async_tree_none            | 383 ms                                                                   | 434 ms: 1.13x slower                                                           |
| xml_etree_generate         | 110 ms                                                                   | 125 ms: 1.14x slower                                                           |
| coroutines                 | 28.5 ms                                                                  | 32.4 ms: 1.14x slower                                                          |
| many_optionals             | 844 us                                                                   | 963 us: 1.14x slower                                                           |
| sqlglot_optimize           | 61.6 ms                                                                  | 70.4 ms: 1.14x slower                                                          |
| comprehensions             | 19.5 us                                                                  | 22.4 us: 1.15x slower                                                          |
| sympy_expand               | 461 ms                                                                   | 532 ms: 1.15x slower                                                           |
| float                      | 86.3 ms                                                                  | 100 ms: 1.16x slower                                                           |
| scimark_fft                | 386 ms                                                                   | 448 ms: 1.16x slower                                                           |
| crypto_pyaes               | 87.1 ms                                                                  | 101 ms: 1.16x slower                                                           |
| sympy_sum                  | 139 ms                                                                   | 161 ms: 1.16x slower                                                           |
| thrift                     | 937 us                                                                   | 1.09 ms: 1.17x slower                                                          |
| async_generators           | 415 ms                                                                   | 484 ms: 1.17x slower                                                           |
| typing_runtime_protocols   | 186 us                                                                   | 217 us: 1.17x slower                                                           |
| subparsers                 | 26.2 ms                                                                  | 30.6 ms: 1.17x slower                                                          |
| mako                       | 13.7 ms                                                                  | 16.0 ms: 1.17x slower                                                          |
| html5lib                   | 59.9 ms                                                                  | 70.3 ms: 1.17x slower                                                          |
| scimark_lu                 | 146 ms                                                                   | 172 ms: 1.18x slower                                                           |
| django_template            | 38.4 ms                                                                  | 45.5 ms: 1.18x slower                                                          |
| dulwich_log                | 58.7 ms                                                                  | 69.5 ms: 1.19x slower                                                          |
| raytrace                   | 308 ms                                                                   | 368 ms: 1.19x slower                                                           |
| deepcopy                   | 318 us                                                                   | 379 us: 1.19x slower                                                           |
| sqlglot_normalize          | 126 ms                                                                   | 151 ms: 1.20x slower                                                           |
| logging_simple             | 6.94 us                                                                  | 8.33 us: 1.20x slower                                                          |
| pyflate                    | 527 ms                                                                   | 633 ms: 1.20x slower                                                           |
| pprint_pformat             | 1.92 sec                                                                 | 2.32 sec: 1.20x slower                                                         |
| logging_format             | 7.49 us                                                                  | 9.02 us: 1.20x slower                                                          |
| pickle_pure_python         | 385 us                                                                   | 465 us: 1.21x slower                                                           |
| nqueens                    | 98.6 ms                                                                  | 120 ms: 1.21x slower                                                           |
| pprint_safe_repr           | 934 ms                                                                   | 1.14 sec: 1.22x slower                                                         |
| genshi_xml                 | 60.1 ms                                                                  | 73.1 ms: 1.22x slower                                                          |
| chaos                      | 66.8 ms                                                                  | 82.2 ms: 1.23x slower                                                          |
| deepcopy_reduce            | 3.28 us                                                                  | 4.03 us: 1.23x slower                                                          |
| deltablue                  | 3.91 ms                                                                  | 4.82 ms: 1.23x slower                                                          |
| nbody                      | 118 ms                                                                   | 145 ms: 1.24x slower                                                           |
| sqlglot_transpile          | 1.69 ms                                                                  | 2.09 ms: 1.24x slower                                                          |
| xml_etree_process          | 74.8 ms                                                                  | 92.9 ms: 1.24x slower                                                          |
| genshi_text                | 26.9 ms                                                                  | 33.7 ms: 1.26x slower                                                          |
| sqlglot_parse              | 1.38 ms                                                                  | 1.76 ms: 1.27x slower                                                          |
| fannkuch                   | 492 ms                                                                   | 624 ms: 1.27x slower                                                           |
| regex_compile              | 123 ms                                                                   | 156 ms: 1.27x slower                                                           |
| richards                   | 48.5 ms                                                                  | 61.6 ms: 1.27x slower                                                          |
| go                         | 138 ms                                                                   | 175 ms: 1.27x slower                                                           |
| scimark_sor                | 144 ms                                                                   | 185 ms: 1.29x slower                                                           |
| hexiom                     | 7.04 ms                                                                  | 9.10 ms: 1.29x slower                                                          |
| generators                 | 37.5 ms                                                                  | 48.5 ms: 1.29x slower                                                          |
| logging_silent             | 112 ns                                                                   | 147 ns: 1.31x slower                                                           |
| unpickle_pure_python       | 255 us                                                                   | 333 us: 1.31x slower                                                           |
| tomli_loads                | 2.47 sec                                                                 | 3.26 sec: 1.32x slower                                                         |
| scimark_monte_carlo        | 76.8 ms                                                                  | 101 ms: 1.32x slower                                                           |
| richards_super             | 55.0 ms                                                                  | 73.0 ms: 1.33x slower                                                          |
| deepcopy_memo              | 35.6 us                                                                  | 47.8 us: 1.34x slower                                                          |
| Geometric mean             | (ref)                                                                    | 1.14x slower                                                                   |

Benchmark hidden because not significant (15): regex_effbot, regex_dna, create_gc_cycles, gc_traversal, pidigits, xml_etree_parse, asyncio_websockets, scimark_sparse_mat_mult, sqlite_synth, regex_v8, json_loads, json, pathlib, pylint, bench_mp_pool
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.119x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.02x