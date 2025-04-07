# Results vs. 3.10.4

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: darwin-arm64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.464x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| docutils       | 1.74 sec                                               | 1.37 sec: 1.27x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.0 ms: 1.50x faster                                                  |
| sphinx         | 729 ms                                                 | 548 ms: 1.33x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.2 ms: 6.97x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.71x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 339 ms: 3.00x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 338 ms: 3.00x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 179 ms: 2.69x faster                                                   |
| async_tree_none               | 391 ms                                                 | 155 ms: 2.53x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 398 ms: 1.68x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.8 ms: 1.39x faster                                                  |
| async_generators              | 233 ms                                                 | 239 ms: 1.03x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.24x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 42.9 ms: 1.69x faster                                                  |
| nbody          | 92.5 ms                                                | 71.6 ms: 1.29x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                  |
| regex_dna      | 175 ms                                                 | 148 ms: 1.18x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.7 ms: 1.15x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.54x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 186 us: 1.53x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.16 sec: 1.48x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.4 ms: 1.30x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.20 ms: 1.15x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.5 ms: 1.11x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 98.8 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 70.2 ms: 1.06x faster                                                  |
| json_loads           | 16.6 us                                                | 18.0 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                  |
| mako            | 9.81 ms                                                | 7.32 ms: 1.34x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.7 ms: 1.32x faster                                                  |
| django_template | 24.4 ms                                                | 19.3 ms: 1.26x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.2 ms: 6.97x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 86.5 us: 3.77x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.71x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.5 ms: 3.46x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 339 ms: 3.00x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 338 ms: 3.00x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 179 ms: 2.69x faster                                                   |
| async_tree_none               | 391 ms                                                 | 155 ms: 2.53x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.06 ms: 2.42x faster                                                  |
| mdp                           | 1.65 sec                                               | 691 ms: 2.39x faster                                                   |
| go                            | 163 ms                                                 | 70.8 ms: 2.31x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.0 us: 2.17x faster                                                  |
| raytrace                      | 327 ms                                                 | 157 ms: 2.08x faster                                                   |
| logging_silent                | 117 ns                                                 | 57.9 ns: 2.02x faster                                                  |
| deepcopy                      | 276 us                                                 | 141 us: 1.95x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| chaos                         | 67.7 ms                                                | 35.5 ms: 1.91x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 75.2 ms: 1.86x faster                                                  |
| richards_super                | 61.0 ms                                                | 33.1 ms: 1.84x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 39.4 ms: 1.84x faster                                                  |
| richards                      | 52.3 ms                                                | 29.4 ms: 1.78x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.1 us: 1.72x faster                                                  |
| float                         | 72.4 ms                                                | 42.9 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 398 ms: 1.68x faster                                                   |
| generators                    | 31.7 ms                                                | 19.0 ms: 1.67x faster                                                  |
| pyflate                       | 448 ms                                                 | 273 ms: 1.64x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.83 ms: 1.63x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.54x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 186 us: 1.53x faster                                                   |
| logging_format                | 5.03 us                                                | 3.28 us: 1.53x faster                                                  |
| pylint                        | 231 ms                                                 | 151 ms: 1.53x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.01 us: 1.52x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.53 us: 1.52x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.4 ms: 1.52x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.0 ms: 1.50x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.16 sec: 1.48x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.5 ms: 1.48x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 69.4 ms: 1.48x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.18 ms: 1.47x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 929 ms: 1.43x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 66.8 ms: 1.43x faster                                                  |
| pycparser                     | 887 ms                                                 | 626 ms: 1.42x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 461 ms: 1.41x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                  |
| coroutines                    | 20.5 ms                                                | 14.8 ms: 1.39x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.2 ms: 1.37x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.49 sec: 1.35x faster                                                 |
| mako                          | 9.81 ms                                                | 7.32 ms: 1.34x faster                                                  |
| sphinx                        | 729 ms                                                 | 548 ms: 1.33x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 69.9 ms: 1.33x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 26.7 ms: 1.32x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.1 ms: 1.30x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 34.4 ms: 1.30x faster                                                  |
| nbody                         | 92.5 ms                                                | 71.6 ms: 1.29x faster                                                  |
| sympy_str                     | 166 ms                                                 | 130 ms: 1.27x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.37 sec: 1.27x faster                                                 |
| django_template               | 24.4 ms                                                | 19.3 ms: 1.26x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 219 ms: 1.23x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.81 sec: 1.22x faster                                                 |
| nqueens                       | 63.8 ms                                                | 52.8 ms: 1.21x faster                                                  |
| fannkuch                      | 303 ms                                                 | 251 ms: 1.21x faster                                                   |
| regex_dna                     | 175 ms                                                 | 148 ms: 1.18x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 462 us: 1.18x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 194 ms: 1.16x faster                                                   |
| many_optionals                | 486 us                                                 | 420 us: 1.16x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.20 ms: 1.15x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.7 ms: 1.15x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.5 ms: 1.11x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.2 ms: 1.11x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 98.8 ms: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.4 ms: 1.11x faster                                                  |
| 2to3                          | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.20 ms: 1.07x faster                                                  |
| connected_components          | 318 ms                                                 | 299 ms: 1.07x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.2 ms: 1.06x faster                                                  |
| json                          | 3.10 ms                                                | 3.03 ms: 1.02x faster                                                  |
| python_startup                | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| shortest_path                 | 328 ms                                                 | 324 ms: 1.01x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                  |
| async_generators              | 233 ms                                                 | 239 ms: 1.03x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.52 us: 1.03x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.0 ms: 1.07x slower                                                  |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.09x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.3 ms: 1.10x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.09 ms: 1.14x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                  |
| telco                         | 3.49 ms                                                | 4.51 ms: 1.29x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.46x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.464x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.13x