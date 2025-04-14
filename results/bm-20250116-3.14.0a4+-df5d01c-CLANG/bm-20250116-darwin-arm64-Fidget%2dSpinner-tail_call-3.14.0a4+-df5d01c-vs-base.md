# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                                 | 156 ms: 1.08x faster                                                  |
| docutils       | 1.44 sec                                                               | 1.36 sec: 1.06x faster                                                |
| html5lib       | 32.9 ms                                                                | 28.9 ms: 1.14x faster                                                 |
| sphinx         | 577 ms                                                                 | 544 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg              | 49.0 ms                                                                | 41.0 ms: 1.19x faster                                                 |
| async_tree_eager                 | 69.6 ms                                                                | 60.4 ms: 1.15x faster                                                 |
| coroutines                       | 16.9 ms                                                                | 15.0 ms: 1.13x faster                                                 |
| async_tree_none                  | 170 ms                                                                 | 151 ms: 1.13x faster                                                  |
| async_tree_none_tg               | 158 ms                                                                 | 142 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 129 ms                                                                 | 116 ms: 1.11x faster                                                  |
| async_tree_memoization           | 209 ms                                                                 | 190 ms: 1.10x faster                                                  |
| async_tree_io                    | 379 ms                                                                 | 346 ms: 1.10x faster                                                  |
| async_tree_eager_memoization     | 147 ms                                                                 | 135 ms: 1.09x faster                                                  |
| async_tree_eager_io              | 373 ms                                                                 | 344 ms: 1.09x faster                                                  |
| async_tree_eager_io_tg           | 377 ms                                                                 | 348 ms: 1.08x faster                                                  |
| async_tree_memoization_tg        | 193 ms                                                                 | 179 ms: 1.08x faster                                                  |
| async_generators                 | 266 ms                                                                 | 247 ms: 1.08x faster                                                  |
| async_tree_io_tg                 | 365 ms                                                                 | 339 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 422 ms                                                                 | 407 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 411 ms                                                                 | 397 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 363 ms                                                                 | 351 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 338 ms                                                                 | 330 ms: 1.03x faster                                                  |
| Geometric mean                   | (ref)                                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 83.0 ms                                                                | 63.9 ms: 1.30x faster                                                 |
| float          | 51.5 ms                                                                | 44.1 ms: 1.17x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.5 ms                                                                | 62.9 ms: 1.23x faster                                                 |
| regex_v8       | 17.0 ms                                                                | 16.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.59 sec                                                               | 1.16 sec: 1.36x faster                                                |
| unpickle_pure_python | 160 us                                                                 | 125 us: 1.29x faster                                                  |
| pickle_pure_python   | 220 us                                                                 | 182 us: 1.21x faster                                                  |
| xml_etree_process    | 41.1 ms                                                                | 34.7 ms: 1.18x faster                                                 |
| xml_etree_generate   | 55.5 ms                                                                | 49.2 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 72.5 ms                                                                | 69.4 ms: 1.04x faster                                                 |
| json_dumps           | 7.41 ms                                                                | 7.10 ms: 1.04x faster                                                 |
| xml_etree_parse      | 103 ms                                                                 | 102 ms: 1.01x faster                                                  |
| json_loads           | 16.4 us                                                                | 16.3 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.2 ms                                                                | 11.6 ms: 1.05x faster                                                 |
| python_startup         | 16.7 ms                                                                | 16.3 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 15.8 ms                                                                | 12.4 ms: 1.27x faster                                                 |
| genshi_xml      | 33.2 ms                                                                | 26.5 ms: 1.25x faster                                                 |
| django_template | 22.7 ms                                                                | 19.6 ms: 1.16x faster                                                 |
| mako            | 8.07 ms                                                                | 7.05 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.21x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 25.4 ms                                                                | 17.0 ms: 1.49x faster                                                 |
| tomli_loads                      | 1.59 sec                                                               | 1.16 sec: 1.36x faster                                                |
| nbody                            | 83.0 ms                                                                | 63.9 ms: 1.30x faster                                                 |
| go                               | 92.6 ms                                                                | 71.8 ms: 1.29x faster                                                 |
| unpickle_pure_python             | 160 us                                                                 | 125 us: 1.29x faster                                                  |
| fannkuch                         | 315 ms                                                                 | 245 ms: 1.29x faster                                                  |
| deepcopy_memo                    | 21.7 us                                                                | 17.0 us: 1.28x faster                                                 |
| genshi_text                      | 15.8 ms                                                                | 12.4 ms: 1.27x faster                                                 |
| hexiom                           | 4.76 ms                                                                | 3.75 ms: 1.27x faster                                                 |
| genshi_xml                       | 33.2 ms                                                                | 26.5 ms: 1.25x faster                                                 |
| pprint_pformat                   | 1.11 sec                                                               | 885 ms: 1.25x faster                                                  |
| pprint_safe_repr                 | 547 ms                                                                 | 439 ms: 1.24x faster                                                  |
| deepcopy                         | 177 us                                                                 | 143 us: 1.24x faster                                                  |
| regex_compile                    | 77.5 ms                                                                | 62.9 ms: 1.23x faster                                                 |
| logging_silent                   | 71.3 ns                                                                | 58.4 ns: 1.22x faster                                                 |
| scimark_monte_carlo              | 47.7 ms                                                                | 39.3 ms: 1.21x faster                                                 |
| scimark_sor                      | 90.3 ms                                                                | 74.6 ms: 1.21x faster                                                 |
| pickle_pure_python               | 220 us                                                                 | 182 us: 1.21x faster                                                  |
| sqlglot_parse                    | 837 us                                                                 | 694 us: 1.21x faster                                                  |
| richards                         | 33.4 ms                                                                | 27.8 ms: 1.20x faster                                                 |
| sqlalchemy_imperative            | 7.45 ms                                                                | 6.24 ms: 1.19x faster                                                 |
| async_tree_eager_tg              | 49.0 ms                                                                | 41.0 ms: 1.19x faster                                                 |
| sqlglot_transpile                | 1.01 ms                                                                | 848 us: 1.19x faster                                                  |
| chaos                            | 42.4 ms                                                                | 35.7 ms: 1.19x faster                                                 |
| deepcopy_reduce                  | 1.76 us                                                                | 1.49 us: 1.19x faster                                                 |
| xml_etree_process                | 41.1 ms                                                                | 34.7 ms: 1.18x faster                                                 |
| richards_super                   | 36.9 ms                                                                | 31.2 ms: 1.18x faster                                                 |
| pyflate                          | 324 ms                                                                 | 275 ms: 1.18x faster                                                  |
| nqueens                          | 60.6 ms                                                                | 51.5 ms: 1.17x faster                                                 |
| deltablue                        | 2.39 ms                                                                | 2.03 ms: 1.17x faster                                                 |
| logging_simple                   | 3.43 us                                                                | 2.93 us: 1.17x faster                                                 |
| float                            | 51.5 ms                                                                | 44.1 ms: 1.17x faster                                                 |
| django_template                  | 22.7 ms                                                                | 19.6 ms: 1.16x faster                                                 |
| async_tree_eager                 | 69.6 ms                                                                | 60.4 ms: 1.15x faster                                                 |
| logging_format                   | 3.71 us                                                                | 3.23 us: 1.15x faster                                                 |
| mako                             | 8.07 ms                                                                | 7.05 ms: 1.15x faster                                                 |
| scimark_lu                       | 74.9 ms                                                                | 65.7 ms: 1.14x faster                                                 |
| comprehensions                   | 13.1 us                                                                | 11.5 us: 1.14x faster                                                 |
| html5lib                         | 32.9 ms                                                                | 28.9 ms: 1.14x faster                                                 |
| typing_runtime_protocols         | 104 us                                                                 | 91.1 us: 1.14x faster                                                 |
| xml_etree_generate               | 55.5 ms                                                                | 49.2 ms: 1.13x faster                                                 |
| coroutines                       | 16.9 ms                                                                | 15.0 ms: 1.13x faster                                                 |
| async_tree_none                  | 170 ms                                                                 | 151 ms: 1.13x faster                                                  |
| crypto_pyaes                     | 52.8 ms                                                                | 47.0 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult          | 3.08 ms                                                                | 2.75 ms: 1.12x faster                                                 |
| raytrace                         | 175 ms                                                                 | 156 ms: 1.12x faster                                                  |
| bpe_tokeniser                    | 3.20 sec                                                               | 2.86 sec: 1.12x faster                                                |
| sqlglot_normalize                | 188 ms                                                                 | 169 ms: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.4 ms                                                                | 30.9 ms: 1.11x faster                                                 |
| async_tree_none_tg               | 158 ms                                                                 | 142 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 129 ms                                                                 | 116 ms: 1.11x faster                                                  |
| sympy_str                        | 147 ms                                                                 | 132 ms: 1.11x faster                                                  |
| async_tree_memoization           | 209 ms                                                                 | 190 ms: 1.10x faster                                                  |
| sympy_expand                     | 246 ms                                                                 | 223 ms: 1.10x faster                                                  |
| sympy_sum                        | 77.3 ms                                                                | 70.3 ms: 1.10x faster                                                 |
| subparsers                       | 12.7 ms                                                                | 11.6 ms: 1.10x faster                                                 |
| scimark_fft                      | 192 ms                                                                 | 176 ms: 1.10x faster                                                  |
| many_optionals                   | 467 us                                                                 | 426 us: 1.10x faster                                                  |
| async_tree_io                    | 379 ms                                                                 | 346 ms: 1.10x faster                                                  |
| sqlalchemy_declarative           | 61.2 ms                                                                | 56.1 ms: 1.09x faster                                                 |
| spectral_norm                    | 67.7 ms                                                                | 62.2 ms: 1.09x faster                                                 |
| async_tree_eager_memoization     | 147 ms                                                                 | 135 ms: 1.09x faster                                                  |
| async_tree_eager_io              | 373 ms                                                                 | 344 ms: 1.09x faster                                                  |
| async_tree_eager_io_tg           | 377 ms                                                                 | 348 ms: 1.08x faster                                                  |
| 2to3                             | 169 ms                                                                 | 156 ms: 1.08x faster                                                  |
| thrift                           | 450 us                                                                 | 415 us: 1.08x faster                                                  |
| async_tree_memoization_tg        | 193 ms                                                                 | 179 ms: 1.08x faster                                                  |
| meteor_contest                   | 76.7 ms                                                                | 70.8 ms: 1.08x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                                | 10.3 ms: 1.08x faster                                                 |
| pylint                           | 162 ms                                                                 | 150 ms: 1.08x faster                                                  |
| async_generators                 | 266 ms                                                                 | 247 ms: 1.08x faster                                                  |
| async_tree_io_tg                 | 365 ms                                                                 | 339 ms: 1.07x faster                                                  |
| bench_thread_pool                | 498 us                                                                 | 464 us: 1.07x faster                                                  |
| dulwich_log                      | 28.4 ms                                                                | 26.6 ms: 1.07x faster                                                 |
| telco                            | 4.69 ms                                                                | 4.41 ms: 1.06x faster                                                 |
| sphinx                           | 577 ms                                                                 | 544 ms: 1.06x faster                                                  |
| docutils                         | 1.44 sec                                                               | 1.36 sec: 1.06x faster                                                |
| pycparser                        | 692 ms                                                                 | 656 ms: 1.05x faster                                                  |
| mdp                              | 1.52 sec                                                               | 1.44 sec: 1.05x faster                                                |
| python_startup_no_site           | 12.2 ms                                                                | 11.6 ms: 1.05x faster                                                 |
| xml_etree_iterparse              | 72.5 ms                                                                | 69.4 ms: 1.04x faster                                                 |
| json_dumps                       | 7.41 ms                                                                | 7.10 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed          | 422 ms                                                                 | 407 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 411 ms                                                                 | 397 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 363 ms                                                                 | 351 ms: 1.03x faster                                                  |
| python_startup                   | 16.7 ms                                                                | 16.3 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 338 ms                                                                 | 330 ms: 1.03x faster                                                  |
| pathlib                          | 22.8 ms                                                                | 22.2 ms: 1.02x faster                                                 |
| sqlite_synth                     | 1.56 us                                                                | 1.53 us: 1.02x faster                                                 |
| xml_etree_parse                  | 103 ms                                                                 | 102 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                                | 16.9 ms: 1.01x faster                                                 |
| json                             | 2.85 ms                                                                | 2.83 ms: 1.01x faster                                                 |
| json_loads                       | 16.4 us                                                                | 16.3 us: 1.01x faster                                                 |
| shortest_path                    | 324 ms                                                                 | 325 ms: 1.00x slower                                                  |
| connected_components             | 297 ms                                                                 | 298 ms: 1.01x slower                                                  |
| coverage                         | 44.7 ms                                                                | 45.1 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 1.27 ms                                                                | 1.29 ms: 1.01x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (8): bench_mp_pool, gc_traversal, k_core, dask, regex_effbot, pidigits, regex_dna, asyncio_websockets

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.02x