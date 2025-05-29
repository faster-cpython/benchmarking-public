# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 158 ms: 1.27x faster                                                  |
| docutils       | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                |
| html5lib       | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                 |
| sphinx         | 729 ms                                                 | 559 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 57.3 ms: 6.84x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.62x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 335 ms: 3.02x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 340 ms: 2.99x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 180 ms: 2.67x faster                                                  |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.58x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 350 ms: 1.91x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 408 ms: 1.64x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                 |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 43.9 ms: 1.65x faster                                                 |
| nbody          | 92.5 ms                                                | 73.8 ms: 1.25x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.6 ms: 1.55x faster                                                 |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.53x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 188 us: 1.51x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                |
| json_dumps           | 8.31 ms                                                | 6.36 ms: 1.31x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 39.4 ms: 1.13x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 72.9 ms: 1.02x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                 |
| json_loads           | 16.6 us                                                | 18.4 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.3 ms: 1.07x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.9 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.8 ms: 1.38x faster                                                 |
| mako            | 9.81 ms                                                | 7.22 ms: 1.36x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 27.1 ms: 1.30x faster                                                 |
| django_template | 24.4 ms                                                | 19.7 ms: 1.24x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 57.3 ms: 6.84x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.62x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 91.7 us: 3.56x faster                                                 |
| subparsers                    | 39.8 ms                                                | 12.9 ms: 3.10x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 335 ms: 3.02x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 340 ms: 2.99x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 180 ms: 2.67x faster                                                  |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.58x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.04 ms: 2.44x faster                                                 |
| mdp                           | 1.65 sec                                               | 709 ms: 2.33x faster                                                  |
| go                            | 163 ms                                                 | 71.2 ms: 2.29x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 16.4 us: 2.12x faster                                                 |
| raytrace                      | 327 ms                                                 | 161 ms: 2.03x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 350 ms: 1.91x faster                                                  |
| deepcopy                      | 276 us                                                 | 145 us: 1.91x faster                                                  |
| chaos                         | 67.7 ms                                                | 35.6 ms: 1.90x faster                                                 |
| richards_super                | 61.0 ms                                                | 33.2 ms: 1.84x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 77.9 ms: 1.80x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 40.4 ms: 1.79x faster                                                 |
| richards                      | 52.3 ms                                                | 29.5 ms: 1.77x faster                                                 |
| generators                    | 31.7 ms                                                | 18.9 ms: 1.68x faster                                                 |
| hexiom                        | 6.25 ms                                                | 3.79 ms: 1.65x faster                                                 |
| float                         | 72.4 ms                                                | 43.9 ms: 1.65x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 408 ms: 1.64x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.6 us: 1.64x faster                                                 |
| pyflate                       | 448 ms                                                 | 277 ms: 1.61x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 61.6 ms: 1.55x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.53x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 188 us: 1.51x faster                                                  |
| pylint                        | 231 ms                                                 | 153 ms: 1.51x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.8 ms: 1.49x faster                                                 |
| html5lib                      | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 69.7 ms: 1.47x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.9 ms: 1.47x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 907 ms: 1.46x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.59 us: 1.46x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 447 ms: 1.45x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                |
| pycparser                     | 887 ms                                                 | 629 ms: 1.41x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.27 us: 1.41x faster                                                 |
| logging_format                | 5.03 us                                                | 3.58 us: 1.40x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 68.6 ms: 1.39x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 12.8 ms: 1.38x faster                                                 |
| mako                          | 9.81 ms                                                | 7.22 ms: 1.36x faster                                                 |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 69.7 ms: 1.33x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                                |
| json_dumps                    | 8.31 ms                                                | 6.36 ms: 1.31x faster                                                 |
| sphinx                        | 729 ms                                                 | 559 ms: 1.30x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 27.1 ms: 1.30x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.2 ms: 1.29x faster                                                 |
| 2to3                          | 201 ms                                                 | 158 ms: 1.27x faster                                                  |
| sympy_str                     | 166 ms                                                 | 131 ms: 1.26x faster                                                  |
| nbody                         | 92.5 ms                                                | 73.8 ms: 1.25x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                  |
| django_template               | 24.4 ms                                                | 19.7 ms: 1.24x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 222 ms: 1.21x faster                                                  |
| fannkuch                      | 303 ms                                                 | 254 ms: 1.19x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.89 sec: 1.19x faster                                                |
| nqueens                       | 63.8 ms                                                | 54.0 ms: 1.18x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 471 us: 1.16x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 39.4 ms: 1.13x faster                                                 |
| many_optionals                | 486 us                                                 | 439 us: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 71.0 ms: 1.09x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 207 ms: 1.09x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.3 ms: 1.07x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.1 ms: 1.07x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                 |
| connected_components          | 318 ms                                                 | 302 ms: 1.05x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 72.9 ms: 1.02x faster                                                 |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.37 ms: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| dask                          | 789 ms                                                 | 799 ms: 1.01x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.57 us: 1.06x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 13.9 ms: 1.09x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.4 us: 1.11x slower                                                 |
| async_generators              | 233 ms                                                 | 266 ms: 1.14x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.34 ms: 1.15x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.18 ms: 1.18x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 69.6 ms: 1.24x slower                                                 |
| telco                         | 3.49 ms                                                | 4.56 ms: 1.31x slower                                                 |
| logging_silent                | 117 ns                                                 | 302 ns: 2.58x slower                                                  |
| coverage                      | 41.2 ms                                                | 258 ms: 6.27x slower                                                  |
| thrift                        | 562 us                                                 | 43.1 ms: 76.71x slower                                                |
| Geometric mean                | (ref)                                                  | 1.31x faster                                                          |

Benchmark hidden because not significant (2): shortest_path, asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.335x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.17x