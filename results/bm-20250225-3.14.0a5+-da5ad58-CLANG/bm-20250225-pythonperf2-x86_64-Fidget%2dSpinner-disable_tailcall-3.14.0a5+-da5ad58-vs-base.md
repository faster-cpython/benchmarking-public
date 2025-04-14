# Results vs. base

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-x86_64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.153x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                       | 307 ms: 1.12x slower                                                               |
| docutils       | 2.82 sec                                                                     | 2.98 sec: 1.06x slower                                                             |
| html5lib       | 65.9 ms                                                                      | 73.0 ms: 1.11x slower                                                              |
| sphinx         | 1.06 sec                                                                     | 1.16 sec: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.09x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_generators           | 416 ms                                                                       | 445 ms: 1.07x slower                                                               |
| async_tree_cpu_io_mixed_tg | 525 ms                                                                       | 568 ms: 1.08x slower                                                               |
| async_tree_cpu_io_mixed    | 539 ms                                                                       | 586 ms: 1.09x slower                                                               |
| coroutines                 | 20.7 ms                                                                      | 22.6 ms: 1.09x slower                                                              |
| async_tree_io              | 615 ms                                                                       | 713 ms: 1.16x slower                                                               |
| async_tree_memoization_tg  | 317 ms                                                                       | 372 ms: 1.17x slower                                                               |
| async_tree_none_tg         | 261 ms                                                                       | 307 ms: 1.17x slower                                                               |
| async_tree_none            | 272 ms                                                                       | 319 ms: 1.17x slower                                                               |
| async_tree_io_tg           | 606 ms                                                                       | 713 ms: 1.18x slower                                                               |
| async_tree_memoization     | 328 ms                                                                       | 390 ms: 1.19x slower                                                               |
| Geometric mean             | (ref)                                                                        | 1.12x slower                                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 292 ms                                                                       | 293 ms: 1.00x slower                                                               |
| float          | 66.4 ms                                                                      | 84.7 ms: 1.28x slower                                                              |
| nbody          | 83.5 ms                                                                      | 123 ms: 1.47x slower                                                               |
| Geometric mean | (ref)                                                                        | 1.24x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 2.95 ms                                                                      | 3.01 ms: 1.02x slower                                                              |
| regex_dna      | 219 ms                                                                       | 226 ms: 1.03x slower                                                               |
| regex_v8       | 24.6 ms                                                                      | 26.4 ms: 1.07x slower                                                              |
| regex_compile  | 131 ms                                                                       | 165 ms: 1.26x slower                                                               |
| Geometric mean | (ref)                                                                        | 1.09x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads           | 26.6 us                                                                      | 26.7 us: 1.01x slower                                                              |
| json_dumps           | 11.6 ms                                                                      | 12.3 ms: 1.06x slower                                                              |
| xml_etree_iterparse  | 103 ms                                                                       | 114 ms: 1.10x slower                                                               |
| xml_etree_generate   | 77.3 ms                                                                      | 92.0 ms: 1.19x slower                                                              |
| xml_etree_process    | 54.2 ms                                                                      | 67.8 ms: 1.25x slower                                                              |
| pickle_pure_python   | 314 us                                                                       | 404 us: 1.29x slower                                                               |
| tomli_loads          | 2.00 sec                                                                     | 2.75 sec: 1.37x slower                                                             |
| unpickle_pure_python | 199 us                                                                       | 275 us: 1.39x slower                                                               |
| Geometric mean       | (ref)                                                                        | 1.18x slower                                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 9.13 ms                                                                      | 9.26 ms: 1.01x slower                                                              |
| python_startup         | 16.1 ms                                                                      | 16.4 ms: 1.02x slower                                                              |
| Geometric mean         | (ref)                                                                        | 1.02x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 10.8 ms                                                                      | 12.9 ms: 1.19x slower                                                              |
| genshi_xml      | 51.8 ms                                                                      | 62.7 ms: 1.21x slower                                                              |
| genshi_text     | 21.7 ms                                                                      | 28.5 ms: 1.31x slower                                                              |
| django_template | 32.2 ms                                                                      | 42.4 ms: 1.32x slower                                                              |
| Geometric mean  | (ref)                                                                        | 1.26x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.85 ms                                                                      | 2.77 ms: 1.03x faster                                                              |
| gc_traversal               | 5.47 ms                                                                      | 5.31 ms: 1.03x faster                                                              |
| pidigits                   | 292 ms                                                                       | 293 ms: 1.00x slower                                                               |
| json_loads                 | 26.6 us                                                                      | 26.7 us: 1.01x slower                                                              |
| python_startup_no_site     | 9.13 ms                                                                      | 9.26 ms: 1.01x slower                                                              |
| python_startup             | 16.1 ms                                                                      | 16.4 ms: 1.02x slower                                                              |
| k_core                     | 2.06 sec                                                                     | 2.10 sec: 1.02x slower                                                             |
| json                       | 5.29 ms                                                                      | 5.40 ms: 1.02x slower                                                              |
| regex_effbot               | 2.95 ms                                                                      | 3.01 ms: 1.02x slower                                                              |
| connected_components       | 424 ms                                                                       | 436 ms: 1.03x slower                                                               |
| regex_dna                  | 219 ms                                                                       | 226 ms: 1.03x slower                                                               |
| shortest_path              | 445 ms                                                                       | 459 ms: 1.03x slower                                                               |
| sqlite_synth               | 2.74 us                                                                      | 2.88 us: 1.05x slower                                                              |
| docutils                   | 2.82 sec                                                                     | 2.98 sec: 1.06x slower                                                             |
| json_dumps                 | 11.6 ms                                                                      | 12.3 ms: 1.06x slower                                                              |
| pathlib                    | 16.3 ms                                                                      | 17.4 ms: 1.07x slower                                                              |
| async_generators           | 416 ms                                                                       | 445 ms: 1.07x slower                                                               |
| regex_v8                   | 24.6 ms                                                                      | 26.4 ms: 1.07x slower                                                              |
| many_optionals             | 986 us                                                                       | 1.06 ms: 1.08x slower                                                              |
| async_tree_cpu_io_mixed_tg | 525 ms                                                                       | 568 ms: 1.08x slower                                                               |
| mdp                        | 2.61 sec                                                                     | 2.83 sec: 1.08x slower                                                             |
| telco                      | 7.53 ms                                                                      | 8.17 ms: 1.09x slower                                                              |
| async_tree_cpu_io_mixed    | 539 ms                                                                       | 586 ms: 1.09x slower                                                               |
| sphinx                     | 1.06 sec                                                                     | 1.16 sec: 1.09x slower                                                             |
| coverage                   | 73.1 ms                                                                      | 79.8 ms: 1.09x slower                                                              |
| coroutines                 | 20.7 ms                                                                      | 22.6 ms: 1.09x slower                                                              |
| pylint                     | 306 ms                                                                       | 336 ms: 1.10x slower                                                               |
| xml_etree_iterparse        | 103 ms                                                                       | 114 ms: 1.10x slower                                                               |
| dulwich_log                | 64.9 ms                                                                      | 71.5 ms: 1.10x slower                                                              |
| sqlalchemy_declarative     | 139 ms                                                                       | 154 ms: 1.11x slower                                                               |
| meteor_contest             | 129 ms                                                                       | 143 ms: 1.11x slower                                                               |
| html5lib                   | 65.9 ms                                                                      | 73.0 ms: 1.11x slower                                                              |
| sympy_integrate            | 22.1 ms                                                                      | 24.7 ms: 1.12x slower                                                              |
| sqlalchemy_imperative      | 17.3 ms                                                                      | 19.3 ms: 1.12x slower                                                              |
| 2to3                       | 275 ms                                                                       | 307 ms: 1.12x slower                                                               |
| sympy_sum                  | 146 ms                                                                       | 164 ms: 1.12x slower                                                               |
| pycparser                  | 1.21 sec                                                                     | 1.37 sec: 1.13x slower                                                             |
| thrift                     | 792 us                                                                       | 899 us: 1.13x slower                                                               |
| sympy_expand               | 469 ms                                                                       | 532 ms: 1.13x slower                                                               |
| bpe_tokeniser              | 4.51 sec                                                                     | 5.12 sec: 1.13x slower                                                             |
| sympy_str                  | 278 ms                                                                       | 316 ms: 1.13x slower                                                               |
| subparsers                 | 21.9 ms                                                                      | 24.9 ms: 1.14x slower                                                              |
| bench_thread_pool          | 892 us                                                                       | 1.03 ms: 1.15x slower                                                              |
| crypto_pyaes               | 74.8 ms                                                                      | 86.4 ms: 1.16x slower                                                              |
| async_tree_io              | 615 ms                                                                       | 713 ms: 1.16x slower                                                               |
| async_tree_memoization_tg  | 317 ms                                                                       | 372 ms: 1.17x slower                                                               |
| typing_runtime_protocols   | 155 us                                                                       | 182 us: 1.17x slower                                                               |
| async_tree_none_tg         | 261 ms                                                                       | 307 ms: 1.17x slower                                                               |
| async_tree_none            | 272 ms                                                                       | 319 ms: 1.17x slower                                                               |
| async_tree_io_tg           | 606 ms                                                                       | 713 ms: 1.18x slower                                                               |
| sqlglot_optimize           | 54.3 ms                                                                      | 63.9 ms: 1.18x slower                                                              |
| async_tree_memoization     | 328 ms                                                                       | 390 ms: 1.19x slower                                                               |
| xml_etree_generate         | 77.3 ms                                                                      | 92.0 ms: 1.19x slower                                                              |
| sqlglot_normalize          | 110 ms                                                                       | 131 ms: 1.19x slower                                                               |
| mako                       | 10.8 ms                                                                      | 12.9 ms: 1.19x slower                                                              |
| genshi_xml                 | 51.8 ms                                                                      | 62.7 ms: 1.21x slower                                                              |
| logging_format             | 6.61 us                                                                      | 8.07 us: 1.22x slower                                                              |
| deepcopy_reduce            | 2.70 us                                                                      | 3.33 us: 1.24x slower                                                              |
| logging_simple             | 5.92 us                                                                      | 7.34 us: 1.24x slower                                                              |
| generators                 | 29.8 ms                                                                      | 37.0 ms: 1.24x slower                                                              |
| deepcopy                   | 258 us                                                                       | 320 us: 1.24x slower                                                               |
| sqlglot_transpile          | 1.66 ms                                                                      | 2.07 ms: 1.25x slower                                                              |
| scimark_sparse_mat_mult    | 4.17 ms                                                                      | 5.21 ms: 1.25x slower                                                              |
| xml_etree_process          | 54.2 ms                                                                      | 67.8 ms: 1.25x slower                                                              |
| regex_compile              | 131 ms                                                                       | 165 ms: 1.26x slower                                                               |
| float                      | 66.4 ms                                                                      | 84.7 ms: 1.28x slower                                                              |
| nqueens                    | 85.4 ms                                                                      | 110 ms: 1.28x slower                                                               |
| pprint_safe_repr           | 752 ms                                                                       | 967 ms: 1.29x slower                                                               |
| pickle_pure_python         | 314 us                                                                       | 404 us: 1.29x slower                                                               |
| pprint_pformat             | 1.52 sec                                                                     | 1.97 sec: 1.30x slower                                                             |
| chaos                      | 55.8 ms                                                                      | 72.6 ms: 1.30x slower                                                              |
| sqlglot_parse              | 1.29 ms                                                                      | 1.68 ms: 1.30x slower                                                              |
| pyflate                    | 395 ms                                                                       | 517 ms: 1.31x slower                                                               |
| genshi_text                | 21.7 ms                                                                      | 28.5 ms: 1.31x slower                                                              |
| raytrace                   | 253 ms                                                                       | 333 ms: 1.32x slower                                                               |
| django_template            | 32.2 ms                                                                      | 42.4 ms: 1.32x slower                                                              |
| scimark_fft                | 266 ms                                                                       | 351 ms: 1.32x slower                                                               |
| comprehensions             | 15.3 us                                                                      | 20.3 us: 1.33x slower                                                              |
| scimark_lu                 | 86.3 ms                                                                      | 118 ms: 1.37x slower                                                               |
| spectral_norm              | 72.4 ms                                                                      | 99.0 ms: 1.37x slower                                                              |
| tomli_loads                | 2.00 sec                                                                     | 2.75 sec: 1.37x slower                                                             |
| unpickle_pure_python       | 199 us                                                                       | 275 us: 1.39x slower                                                               |
| scimark_monte_carlo        | 58.3 ms                                                                      | 82.3 ms: 1.41x slower                                                              |
| fannkuch                   | 351 ms                                                                       | 496 ms: 1.41x slower                                                               |
| deltablue                  | 3.09 ms                                                                      | 4.36 ms: 1.41x slower                                                              |
| richards_super             | 47.0 ms                                                                      | 66.4 ms: 1.41x slower                                                              |
| deepcopy_memo              | 26.8 us                                                                      | 37.9 us: 1.42x slower                                                              |
| hexiom                     | 5.68 ms                                                                      | 8.11 ms: 1.43x slower                                                              |
| logging_silent             | 79.6 ns                                                                      | 114 ns: 1.43x slower                                                               |
| richards                   | 41.4 ms                                                                      | 59.9 ms: 1.45x slower                                                              |
| go                         | 121 ms                                                                       | 175 ms: 1.45x slower                                                               |
| nbody                      | 83.5 ms                                                                      | 123 ms: 1.47x slower                                                               |
| scimark_sor                | 91.4 ms                                                                      | 147 ms: 1.61x slower                                                               |
| Geometric mean             | (ref)                                                                        | 1.18x slower                                                                       |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_websockets, bench_mp_pool
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.153x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.02x