# Results vs. 3.10.4

- fork: python
- ref: 98fa4a49fecbac3c990a
- machine: darwin-arm64
- commit hash: 98fa4a4
- commit date: 2025-03-09
- overall geometric mean: 1.379x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 165 ms: 1.22x faster                                                   |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.5 ms: 1.48x faster                                                  |
| sphinx         | 729 ms                                                 | 575 ms: 1.27x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.8 ms: 6.44x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 371 ms: 2.74x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.46x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                  |
| async_generators              | 233 ms                                                 | 272 ms: 1.17x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.09x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.8 ms: 1.62x faster                                                  |
| nbody          | 92.5 ms                                                | 64.5 ms: 1.43x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.4 ms: 1.40x faster                                                  |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.25 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 196 us: 1.45x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.33 ms: 1.13x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                   |
| xml_etree_generate   | 53.9 ms                                                | 50.7 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 70.7 ms: 1.05x faster                                                  |
| json_loads           | 16.6 us                                                | 17.6 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 15.2 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.50 ms: 1.51x faster                                                  |
| genshi_text     | 17.7 ms                                                | 13.7 ms: 1.29x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 28.9 ms: 1.21x faster                                                  |
| django_template | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.8 ms: 6.44x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 92.2 us: 3.54x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.1 ms: 3.28x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 371 ms: 2.74x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.46x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.15 ms: 2.32x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 18.2 us: 1.91x faster                                                  |
| richards_super                | 61.0 ms                                                | 32.2 ms: 1.89x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| deepcopy                      | 276 us                                                 | 150 us: 1.84x faster                                                   |
| raytrace                      | 327 ms                                                 | 178 ms: 1.83x faster                                                   |
| richards                      | 52.3 ms                                                | 28.8 ms: 1.81x faster                                                  |
| logging_silent                | 117 ns                                                 | 65.0 ns: 1.80x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 79.4 ms: 1.76x faster                                                  |
| go                            | 163 ms                                                 | 92.7 ms: 1.76x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.3 ms: 1.72x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 44.5 ms: 1.63x faster                                                  |
| float                         | 72.4 ms                                                | 44.8 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| mako                          | 9.81 ms                                                | 6.50 ms: 1.51x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 63.4 ms: 1.50x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.5 ms: 1.48x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.58 us: 1.47x faster                                                  |
| pyflate                       | 448 ms                                                 | 306 ms: 1.46x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 196 us: 1.45x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 24.5 ms: 1.45x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                 |
| logging_format                | 5.03 us                                                | 3.50 us: 1.44x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.19 us: 1.44x faster                                                  |
| nbody                         | 92.5 ms                                                | 64.5 ms: 1.43x faster                                                  |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                   |
| comprehensions                | 17.3 us                                                | 12.1 us: 1.43x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 73.2 ms: 1.40x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 68.4 ms: 1.40x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.67 ms: 1.36x faster                                                  |
| generators                    | 31.7 ms                                                | 23.3 ms: 1.36x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.61 ms: 1.36x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 995 ms: 1.33x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 55.0 ms: 1.33x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                 |
| pycparser                     | 887 ms                                                 | 671 ms: 1.32x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 495 ms: 1.31x faster                                                   |
| thrift                        | 562 us                                                 | 435 us: 1.29x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.7 ms: 1.29x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 13.7 ms: 1.29x faster                                                  |
| sphinx                        | 729 ms                                                 | 575 ms: 1.27x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 73.9 ms: 1.25x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                  |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 182 ms: 1.24x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                  |
| 2to3                          | 201 ms                                                 | 165 ms: 1.22x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 28.9 ms: 1.21x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                 |
| sympy_str                     | 166 ms                                                 | 141 ms: 1.18x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.93 sec: 1.17x faster                                                 |
| django_template               | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.96 ms: 1.15x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.33 ms: 1.13x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 238 ms: 1.13x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 486 us: 1.12x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.47 sec: 1.12x faster                                                 |
| pathlib                       | 25.7 ms                                                | 23.3 ms: 1.11x faster                                                  |
| fannkuch                      | 303 ms                                                 | 279 ms: 1.08x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                   |
| nqueens                       | 63.8 ms                                                | 59.3 ms: 1.08x faster                                                  |
| many_optionals                | 486 us                                                 | 456 us: 1.07x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 50.7 ms: 1.06x faster                                                  |
| connected_components          | 318 ms                                                 | 299 ms: 1.06x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.7 ms: 1.05x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 74.5 ms: 1.04x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.25 ms: 1.04x faster                                                  |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| json_loads                    | 16.6 us                                                | 17.6 us: 1.06x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 61.9 ms: 1.10x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.30 ms: 1.11x slower                                                  |
| coverage                      | 41.2 ms                                                | 46.0 ms: 1.12x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.67 us: 1.13x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.14 ms: 1.16x slower                                                  |
| async_generators              | 233 ms                                                 | 272 ms: 1.17x slower                                                   |
| python_startup_no_site        | 12.8 ms                                                | 15.2 ms: 1.19x slower                                                  |
| telco                         | 3.49 ms                                                | 4.49 ms: 1.29x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.37x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, python_startup, shortest_path
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250309-3.14.0a5+-98fa4a4-JIT/bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.379x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.17x