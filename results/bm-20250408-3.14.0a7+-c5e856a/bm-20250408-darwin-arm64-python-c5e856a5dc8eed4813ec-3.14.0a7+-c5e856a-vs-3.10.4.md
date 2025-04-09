# Results vs. 3.10.4

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: darwin-arm64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.404x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 159 ms: 1.27x faster                                                   |
| docutils       | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                  |
| sphinx         | 729 ms                                                 | 574 ms: 1.27x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.39x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 136 ms: 3.55x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 356 ms: 2.85x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 370 ms: 2.75x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 188 ms: 2.55x faster                                                   |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.45x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 353 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                  |
| async_generators              | 233 ms                                                 | 257 ms: 1.10x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.12x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 45.8 ms: 1.58x faster                                                  |
| nbody          | 92.5 ms                                                | 70.1 ms: 1.32x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 66.7 ms: 1.43x faster                                                  |
| regex_dna      | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.6 ms: 1.22x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 201 us: 1.41x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 148 us: 1.34x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 38.1 ms: 1.17x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.36 ms: 1.13x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 72.1 ms: 1.03x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.8 ms: 1.17x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.56 ms: 1.30x faster                                                  |
| genshi_text     | 17.7 ms                                                | 13.7 ms: 1.29x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 28.6 ms: 1.23x faster                                                  |
| django_template | 24.4 ms                                                | 20.8 ms: 1.17x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.39x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 136 ms: 3.55x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 93.7 us: 3.48x faster                                                  |
| subparsers                    | 39.8 ms                                                | 12.1 ms: 3.30x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 356 ms: 2.85x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 370 ms: 2.75x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 188 ms: 2.55x faster                                                   |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.45x faster                                                   |
| mdp                           | 1.65 sec                                               | 753 ms: 2.19x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.31 ms: 2.16x faster                                                  |
| go                            | 163 ms                                                 | 78.8 ms: 2.07x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 17.8 us: 1.95x faster                                                  |
| raytrace                      | 327 ms                                                 | 169 ms: 1.93x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 353 ms: 1.89x faster                                                   |
| deepcopy                      | 276 us                                                 | 148 us: 1.86x faster                                                   |
| logging_silent                | 117 ns                                                 | 64.5 ns: 1.82x faster                                                  |
| chaos                         | 67.7 ms                                                | 37.6 ms: 1.80x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 77.8 ms: 1.80x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 41.8 ms: 1.73x faster                                                  |
| richards_super                | 61.0 ms                                                | 35.9 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                   |
| richards                      | 52.3 ms                                                | 32.2 ms: 1.62x faster                                                  |
| float                         | 72.4 ms                                                | 45.8 ms: 1.58x faster                                                  |
| pyflate                       | 448 ms                                                 | 286 ms: 1.56x faster                                                   |
| comprehensions                | 17.3 us                                                | 11.3 us: 1.53x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.58 us: 1.47x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.26 ms: 1.47x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 24.4 ms: 1.46x faster                                                  |
| logging_format                | 5.03 us                                                | 3.51 us: 1.43x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.21 us: 1.43x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 66.7 ms: 1.43x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                 |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 201 us: 1.41x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 73.3 ms: 1.40x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 68.4 ms: 1.39x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.54 ms: 1.39x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 961 ms: 1.38x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 475 ms: 1.36x faster                                                   |
| pycparser                     | 887 ms                                                 | 651 ms: 1.36x faster                                                   |
| generators                    | 31.7 ms                                                | 23.4 ms: 1.36x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 148 us: 1.34x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 54.8 ms: 1.34x faster                                                  |
| nbody                         | 92.5 ms                                                | 70.1 ms: 1.32x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                                 |
| mako                          | 9.81 ms                                                | 7.56 ms: 1.30x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 13.7 ms: 1.29x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.0 ms: 1.28x faster                                                  |
| sphinx                        | 729 ms                                                 | 574 ms: 1.27x faster                                                   |
| 2to3                          | 201 ms                                                 | 159 ms: 1.27x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 74.1 ms: 1.25x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 181 ms: 1.25x faster                                                   |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 28.6 ms: 1.23x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.7 ms: 1.23x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.6 ms: 1.22x faster                                                  |
| sympy_str                     | 166 ms                                                 | 139 ms: 1.19x faster                                                   |
| python_startup                | 19.6 ms                                                | 16.8 ms: 1.17x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 38.1 ms: 1.17x faster                                                  |
| django_template               | 24.4 ms                                                | 20.8 ms: 1.17x faster                                                  |
| fannkuch                      | 303 ms                                                 | 259 ms: 1.17x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.98 sec: 1.15x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 233 ms: 1.15x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.36 ms: 1.13x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 489 us: 1.12x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.09 ms: 1.11x faster                                                  |
| many_optionals                | 486 us                                                 | 445 us: 1.09x faster                                                   |
| nqueens                       | 63.8 ms                                                | 58.7 ms: 1.09x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.7 ms: 1.09x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 72.3 ms: 1.08x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| connected_components          | 318 ms                                                 | 304 ms: 1.05x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 72.1 ms: 1.03x faster                                                  |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                  |
| python_startup_no_site        | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                  |
| shortest_path                 | 328 ms                                                 | 331 ms: 1.01x slower                                                   |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.53 us: 1.03x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.8 ms: 1.07x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| async_generators              | 233 ms                                                 | 257 ms: 1.10x slower                                                   |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.7 ms: 1.11x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                                  |
| telco                         | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.40x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.404x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.15x