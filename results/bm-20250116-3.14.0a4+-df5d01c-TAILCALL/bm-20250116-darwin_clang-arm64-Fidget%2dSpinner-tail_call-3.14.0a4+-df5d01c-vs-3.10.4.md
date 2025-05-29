# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.466x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 156 ms: 1.29x faster                                                  |
| docutils       | 1.74 sec                                               | 1.36 sec: 1.27x faster                                                |
| html5lib       | 43.5 ms                                                | 28.9 ms: 1.51x faster                                                 |
| sphinx         | 729 ms                                                 | 544 ms: 1.34x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.4 ms: 6.49x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 135 ms: 3.58x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 344 ms: 2.95x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 346 ms: 2.94x faster                                                  |
| async_tree_none               | 391 ms                                                 | 151 ms: 2.59x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 190 ms: 2.54x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 351 ms: 1.91x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 407 ms: 1.64x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                 |
| async_generators              | 233 ms                                                 | 247 ms: 1.06x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.18x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.1 ms: 1.64x faster                                                 |
| nbody          | 92.5 ms                                                | 63.9 ms: 1.45x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 62.9 ms: 1.52x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.26x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.05 ms: 1.14x faster                                                 |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 125 us: 1.59x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 182 us: 1.56x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.16 sec: 1.48x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 34.7 ms: 1.29x faster                                                 |
| json_dumps           | 8.31 ms                                                | 7.10 ms: 1.17x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 49.2 ms: 1.10x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 69.4 ms: 1.07x faster                                                 |
| json_loads           | 16.6 us                                                | 16.3 us: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.3 ms: 1.21x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 11.6 ms: 1.10x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.4 ms: 1.43x faster                                                 |
| mako            | 9.81 ms                                                | 7.05 ms: 1.39x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 26.5 ms: 1.32x faster                                                 |
| django_template | 24.4 ms                                                | 19.6 ms: 1.24x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.4 ms: 6.49x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 91.1 us: 3.58x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 135 ms: 3.58x faster                                                  |
| subparsers                    | 39.8 ms                                                | 11.6 ms: 3.44x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 344 ms: 2.95x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 346 ms: 2.94x faster                                                  |
| async_tree_none               | 391 ms                                                 | 151 ms: 2.59x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 190 ms: 2.54x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.03 ms: 2.46x faster                                                 |
| go                            | 163 ms                                                 | 71.8 ms: 2.28x faster                                                 |
| raytrace                      | 327 ms                                                 | 156 ms: 2.09x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 17.0 us: 2.04x faster                                                 |
| logging_silent                | 117 ns                                                 | 58.4 ns: 2.00x faster                                                 |
| richards_super                | 61.0 ms                                                | 31.2 ms: 1.95x faster                                                 |
| sqlglot_parse                 | 1.35 ms                                                | 694 us: 1.94x faster                                                  |
| deepcopy                      | 276 us                                                 | 143 us: 1.93x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 351 ms: 1.91x faster                                                  |
| chaos                         | 67.7 ms                                                | 35.7 ms: 1.90x faster                                                 |
| richards                      | 52.3 ms                                                | 27.8 ms: 1.88x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 74.6 ms: 1.88x faster                                                 |
| generators                    | 31.7 ms                                                | 17.0 ms: 1.86x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 39.3 ms: 1.84x faster                                                 |
| sqlglot_transpile             | 1.56 ms                                                | 848 us: 1.84x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.75 ms: 1.66x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 407 ms: 1.64x faster                                                  |
| float                         | 72.4 ms                                                | 44.1 ms: 1.64x faster                                                 |
| pyflate                       | 448 ms                                                 | 275 ms: 1.63x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 125 us: 1.59x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.93 us: 1.57x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.49 us: 1.56x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 182 us: 1.56x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 65.7 ms: 1.56x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 47.0 ms: 1.56x faster                                                 |
| logging_format                | 5.03 us                                                | 3.23 us: 1.56x faster                                                 |
| pylint                        | 231 ms                                                 | 150 ms: 1.54x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 62.2 ms: 1.53x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 62.9 ms: 1.52x faster                                                 |
| html5lib                      | 43.5 ms                                                | 28.9 ms: 1.51x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 885 ms: 1.50x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.5 us: 1.50x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.16 sec: 1.48x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 439 ms: 1.48x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.24 ms: 1.45x faster                                                 |
| nbody                         | 92.5 ms                                                | 63.9 ms: 1.45x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 12.4 ms: 1.43x faster                                                 |
| mako                          | 9.81 ms                                                | 7.05 ms: 1.39x faster                                                 |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.48 sec: 1.36x faster                                                |
| thrift                        | 562 us                                                 | 415 us: 1.35x faster                                                  |
| pycparser                     | 887 ms                                                 | 656 ms: 1.35x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 56.1 ms: 1.35x faster                                                 |
| sphinx                        | 729 ms                                                 | 544 ms: 1.34x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.6 ms: 1.34x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 26.5 ms: 1.32x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 70.3 ms: 1.32x faster                                                 |
| 2to3                          | 201 ms                                                 | 156 ms: 1.29x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 34.7 ms: 1.29x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 176 ms: 1.28x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.3 ms: 1.28x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.36 sec: 1.27x faster                                                |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.26x faster                                                  |
| sympy_str                     | 166 ms                                                 | 132 ms: 1.26x faster                                                  |
| django_template               | 24.4 ms                                                | 19.6 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.75 ms: 1.24x faster                                                 |
| nqueens                       | 63.8 ms                                                | 51.5 ms: 1.24x faster                                                 |
| fannkuch                      | 303 ms                                                 | 245 ms: 1.24x faster                                                  |
| python_startup                | 19.6 ms                                                | 16.3 ms: 1.21x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 223 ms: 1.21x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 30.9 ms: 1.20x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 2.86 sec: 1.20x faster                                                |
| bench_thread_pool             | 545 us                                                 | 464 us: 1.17x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.10 ms: 1.17x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.2 ms: 1.16x faster                                                 |
| mdp                           | 1.65 sec                                               | 1.44 sec: 1.14x faster                                                |
| many_optionals                | 486 us                                                 | 426 us: 1.14x faster                                                  |
| sqlglot_normalize             | 192 ms                                                 | 169 ms: 1.14x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.05 ms: 1.14x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                 |
| python_startup_no_site        | 12.8 ms                                                | 11.6 ms: 1.10x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 70.8 ms: 1.10x faster                                                 |
| json                          | 3.10 ms                                                | 2.83 ms: 1.10x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 49.2 ms: 1.10x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.08x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 69.4 ms: 1.07x faster                                                 |
| connected_components          | 318 ms                                                 | 298 ms: 1.07x faster                                                  |
| dask                          | 789 ms                                                 | 770 ms: 1.03x faster                                                  |
| json_loads                    | 16.6 us                                                | 16.3 us: 1.02x faster                                                 |
| shortest_path                 | 328 ms                                                 | 325 ms: 1.01x faster                                                  |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.53 us: 1.03x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 58.9 ms: 1.05x slower                                                 |
| async_generators              | 233 ms                                                 | 247 ms: 1.06x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.1 ms: 1.09x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.10x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                 |
| telco                         | 3.49 ms                                                | 4.41 ms: 1.26x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.46x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250116-3.14.0a4+-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.466x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.13x