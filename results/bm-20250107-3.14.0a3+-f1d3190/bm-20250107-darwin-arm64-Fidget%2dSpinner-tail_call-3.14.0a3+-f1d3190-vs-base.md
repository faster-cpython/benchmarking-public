# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.145x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                 | 151 ms: 1.12x faster                                                  |
| docutils       | 1.45 sec                                                               | 1.37 sec: 1.06x faster                                                |
| html5lib       | 34.0 ms                                                                | 29.0 ms: 1.17x faster                                                 |
| sphinx         | 581 ms                                                                 | 539 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg              | 48.2 ms                                                                | 40.4 ms: 1.19x faster                                                 |
| async_tree_eager                 | 69.7 ms                                                                | 58.8 ms: 1.18x faster                                                 |
| coroutines                       | 17.1 ms                                                                | 14.7 ms: 1.17x faster                                                 |
| async_tree_none                  | 174 ms                                                                 | 152 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 158 ms                                                                 | 138 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 377 ms                                                                 | 331 ms: 1.14x faster                                                  |
| async_tree_memoization           | 215 ms                                                                 | 191 ms: 1.13x faster                                                  |
| async_tree_io                    | 388 ms                                                                 | 348 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 128 ms                                                                 | 115 ms: 1.11x faster                                                  |
| async_tree_eager_io              | 378 ms                                                                 | 340 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 383 ms                                                                 | 345 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 148 ms                                                                 | 135 ms: 1.10x faster                                                  |
| async_tree_memoization_tg        | 198 ms                                                                 | 181 ms: 1.10x faster                                                  |
| async_generators                 | 300 ms                                                                 | 279 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 419 ms                                                                 | 401 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 414 ms                                                                 | 398 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 361 ms                                                                 | 350 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 338 ms                                                                 | 329 ms: 1.03x faster                                                  |
| Geometric mean                   | (ref)                                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 79.8 ms                                                                | 60.2 ms: 1.33x faster                                                 |
| float          | 53.7 ms                                                                | 43.4 ms: 1.24x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 79.4 ms                                                                | 61.9 ms: 1.28x faster                                                 |
| regex_v8       | 17.1 ms                                                                | 16.8 ms: 1.02x faster                                                 |
| regex_effbot   | 2.06 ms                                                                | 2.05 ms: 1.00x faster                                                 |
| regex_dna      | 138 ms                                                                 | 138 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.63 sec                                                               | 1.14 sec: 1.43x faster                                                |
| unpickle_pure_python | 164 us                                                                 | 120 us: 1.36x faster                                                  |
| pickle_pure_python   | 225 us                                                                 | 182 us: 1.24x faster                                                  |
| xml_etree_process    | 41.3 ms                                                                | 33.9 ms: 1.22x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                                | 48.4 ms: 1.17x faster                                                 |
| xml_etree_parse      | 103 ms                                                                 | 97.7 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 72.8 ms                                                                | 68.8 ms: 1.06x faster                                                 |
| json_dumps           | 7.46 ms                                                                | 7.08 ms: 1.05x faster                                                 |
| json_loads           | 16.2 us                                                                | 16.1 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                                  | 1.17x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.5 ms                                                                | 13.6 ms: 1.01x slower                                                 |
| python_startup         | 18.5 ms                                                                | 18.6 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.7 ms                                                                | 12.4 ms: 1.34x faster                                                 |
| genshi_xml      | 35.1 ms                                                                | 26.5 ms: 1.33x faster                                                 |
| django_template | 23.4 ms                                                                | 19.1 ms: 1.23x faster                                                 |
| mako            | 8.22 ms                                                                | 6.91 ms: 1.19x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 24.7 ms                                                                | 17.2 ms: 1.44x faster                                                 |
| tomli_loads                      | 1.63 sec                                                               | 1.14 sec: 1.43x faster                                                |
| deepcopy_memo                    | 23.2 us                                                                | 16.5 us: 1.40x faster                                                 |
| unpickle_pure_python             | 164 us                                                                 | 120 us: 1.36x faster                                                  |
| go                               | 96.2 ms                                                                | 70.9 ms: 1.36x faster                                                 |
| genshi_text                      | 16.7 ms                                                                | 12.4 ms: 1.34x faster                                                 |
| hexiom                           | 4.93 ms                                                                | 3.71 ms: 1.33x faster                                                 |
| genshi_xml                       | 35.1 ms                                                                | 26.5 ms: 1.33x faster                                                 |
| nbody                            | 79.8 ms                                                                | 60.2 ms: 1.33x faster                                                 |
| logging_silent                   | 75.5 ns                                                                | 57.8 ns: 1.31x faster                                                 |
| fannkuch                         | 313 ms                                                                 | 240 ms: 1.31x faster                                                  |
| deepcopy                         | 182 us                                                                 | 140 us: 1.30x faster                                                  |
| pprint_pformat                   | 1.14 sec                                                               | 875 ms: 1.30x faster                                                  |
| regex_compile                    | 79.4 ms                                                                | 61.9 ms: 1.28x faster                                                 |
| scimark_monte_carlo              | 48.0 ms                                                                | 37.6 ms: 1.28x faster                                                 |
| pprint_safe_repr                 | 557 ms                                                                 | 437 ms: 1.28x faster                                                  |
| sqlglot_parse                    | 870 us                                                                 | 684 us: 1.27x faster                                                  |
| comprehensions                   | 13.6 us                                                                | 10.7 us: 1.27x faster                                                 |
| chaos                            | 43.6 ms                                                                | 34.5 ms: 1.26x faster                                                 |
| scimark_sor                      | 91.1 ms                                                                | 72.7 ms: 1.25x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                                | 1.46 us: 1.25x faster                                                 |
| sqlglot_transpile                | 1.05 ms                                                                | 840 us: 1.25x faster                                                  |
| float                            | 53.7 ms                                                                | 43.4 ms: 1.24x faster                                                 |
| pickle_pure_python               | 225 us                                                                 | 182 us: 1.24x faster                                                  |
| richards                         | 33.8 ms                                                                | 27.4 ms: 1.23x faster                                                 |
| sqlalchemy_imperative            | 7.55 ms                                                                | 6.15 ms: 1.23x faster                                                 |
| django_template                  | 23.4 ms                                                                | 19.1 ms: 1.23x faster                                                 |
| richards_super                   | 37.5 ms                                                                | 30.8 ms: 1.22x faster                                                 |
| nqueens                          | 61.8 ms                                                                | 50.7 ms: 1.22x faster                                                 |
| xml_etree_process                | 41.3 ms                                                                | 33.9 ms: 1.22x faster                                                 |
| deltablue                        | 2.49 ms                                                                | 2.05 ms: 1.21x faster                                                 |
| async_tree_eager_tg              | 48.2 ms                                                                | 40.4 ms: 1.19x faster                                                 |
| mako                             | 8.22 ms                                                                | 6.91 ms: 1.19x faster                                                 |
| async_tree_eager                 | 69.7 ms                                                                | 58.8 ms: 1.18x faster                                                 |
| scimark_lu                       | 76.4 ms                                                                | 64.6 ms: 1.18x faster                                                 |
| logging_simple                   | 3.46 us                                                                | 2.92 us: 1.18x faster                                                 |
| raytrace                         | 179 ms                                                                 | 152 ms: 1.18x faster                                                  |
| pyflate                          | 332 ms                                                                 | 282 ms: 1.18x faster                                                  |
| html5lib                         | 34.0 ms                                                                | 29.0 ms: 1.17x faster                                                 |
| typing_runtime_protocols         | 105 us                                                                 | 89.7 us: 1.17x faster                                                 |
| spectral_norm                    | 69.4 ms                                                                | 59.4 ms: 1.17x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                                | 48.4 ms: 1.17x faster                                                 |
| scimark_fft                      | 195 ms                                                                 | 167 ms: 1.17x faster                                                  |
| coroutines                       | 17.1 ms                                                                | 14.7 ms: 1.17x faster                                                 |
| logging_format                   | 3.75 us                                                                | 3.23 us: 1.16x faster                                                 |
| scimark_sparse_mat_mult          | 3.02 ms                                                                | 2.60 ms: 1.16x faster                                                 |
| sympy_str                        | 149 ms                                                                 | 130 ms: 1.15x faster                                                  |
| pycparser                        | 697 ms                                                                 | 609 ms: 1.15x faster                                                  |
| sqlglot_normalize                | 191 ms                                                                 | 167 ms: 1.14x faster                                                  |
| async_tree_none                  | 174 ms                                                                 | 152 ms: 1.14x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                                | 30.4 ms: 1.14x faster                                                 |
| async_tree_none_tg               | 158 ms                                                                 | 138 ms: 1.14x faster                                                  |
| async_tree_io_tg                 | 377 ms                                                                 | 331 ms: 1.14x faster                                                  |
| crypto_pyaes                     | 52.9 ms                                                                | 46.6 ms: 1.13x faster                                                 |
| sympy_expand                     | 249 ms                                                                 | 220 ms: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                                               | 2.86 sec: 1.13x faster                                                |
| async_tree_memoization           | 215 ms                                                                 | 191 ms: 1.13x faster                                                  |
| sympy_sum                        | 78.1 ms                                                                | 69.3 ms: 1.13x faster                                                 |
| 2to3                             | 170 ms                                                                 | 151 ms: 1.12x faster                                                  |
| sqlalchemy_declarative           | 61.8 ms                                                                | 55.3 ms: 1.12x faster                                                 |
| subparsers                       | 12.7 ms                                                                | 11.4 ms: 1.12x faster                                                 |
| many_optionals                   | 471 us                                                                 | 423 us: 1.11x faster                                                  |
| async_tree_io                    | 388 ms                                                                 | 348 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 128 ms                                                                 | 115 ms: 1.11x faster                                                  |
| async_tree_eager_io              | 378 ms                                                                 | 340 ms: 1.11x faster                                                  |
| meteor_contest                   | 77.7 ms                                                                | 70.0 ms: 1.11x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                                | 10.2 ms: 1.11x faster                                                 |
| async_tree_eager_io_tg           | 383 ms                                                                 | 345 ms: 1.11x faster                                                  |
| bench_thread_pool                | 503 us                                                                 | 454 us: 1.11x faster                                                  |
| async_tree_eager_memoization     | 148 ms                                                                 | 135 ms: 1.10x faster                                                  |
| async_tree_memoization_tg        | 198 ms                                                                 | 181 ms: 1.10x faster                                                  |
| thrift                           | 452 us                                                                 | 416 us: 1.09x faster                                                  |
| pylint                           | 163 ms                                                                 | 150 ms: 1.08x faster                                                  |
| dulwich_log                      | 28.3 ms                                                                | 26.2 ms: 1.08x faster                                                 |
| sphinx                           | 581 ms                                                                 | 539 ms: 1.08x faster                                                  |
| async_generators                 | 300 ms                                                                 | 279 ms: 1.08x faster                                                  |
| telco                            | 4.73 ms                                                                | 4.41 ms: 1.07x faster                                                 |
| mdp                              | 1.51 sec                                                               | 1.43 sec: 1.06x faster                                                |
| docutils                         | 1.45 sec                                                               | 1.37 sec: 1.06x faster                                                |
| xml_etree_parse                  | 103 ms                                                                 | 97.7 ms: 1.06x faster                                                 |
| xml_etree_iterparse              | 72.8 ms                                                                | 68.8 ms: 1.06x faster                                                 |
| json_dumps                       | 7.46 ms                                                                | 7.08 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed          | 419 ms                                                                 | 401 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 414 ms                                                                 | 398 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 361 ms                                                                 | 350 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 338 ms                                                                 | 329 ms: 1.03x faster                                                  |
| shortest_path                    | 328 ms                                                                 | 320 ms: 1.03x faster                                                  |
| json                             | 2.85 ms                                                                | 2.78 ms: 1.03x faster                                                 |
| bench_mp_pool                    | 61.2 ms                                                                | 59.9 ms: 1.02x faster                                                 |
| sqlite_synth                     | 1.57 us                                                                | 1.54 us: 1.02x faster                                                 |
| regex_v8                         | 17.1 ms                                                                | 16.8 ms: 1.02x faster                                                 |
| json_loads                       | 16.2 us                                                                | 16.1 us: 1.01x faster                                                 |
| regex_effbot                     | 2.06 ms                                                                | 2.05 ms: 1.00x faster                                                 |
| regex_dna                        | 138 ms                                                                 | 138 ms: 1.00x faster                                                  |
| python_startup_no_site           | 13.5 ms                                                                | 13.6 ms: 1.01x slower                                                 |
| python_startup                   | 18.5 ms                                                                | 18.6 ms: 1.01x slower                                                 |
| coverage                         | 44.5 ms                                                                | 45.0 ms: 1.01x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (7): k_core, connected_components, pidigits, gc_traversal, asyncio_websockets, create_gc_cycles, pathlib

- Geometric mean (including insignificant results): 1.145x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.00x