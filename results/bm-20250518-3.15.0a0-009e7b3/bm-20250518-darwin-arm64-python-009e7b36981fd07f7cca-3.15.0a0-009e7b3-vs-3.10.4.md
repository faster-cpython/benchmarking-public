# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 193 ms: 1.04x faster                                                  |
| docutils       | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                |
| html5lib       | 43.5 ms                                                | 35.1 ms: 1.24x faster                                                 |
| sphinx         | 729 ms                                                 | 637 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 77.5 ms: 5.06x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 155 ms: 3.12x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 407 ms: 2.49x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 425 ms: 2.40x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.16x faster                                                  |
| async_tree_none               | 391 ms                                                 | 185 ms: 2.11x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 440 ms: 1.52x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.88x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.7 ms: 1.23x faster                                                 |
| nbody          | 92.5 ms                                                | 91.7 ms: 1.01x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                 |
| regex_compile  | 95.6 ms                                                | 86.6 ms: 1.10x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.18 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 7.14 ms: 1.16x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                |
| pickle_pure_python   | 285 us                                                 | 251 us: 1.13x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 190 us: 1.04x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 76.1 ms: 1.02x slower                                                 |
| xml_etree_process    | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                 |
| json_loads           | 16.6 us                                                | 18.4 us: 1.11x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 61.3 ms: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.5 ms: 1.06x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.0 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.15 ms: 1.07x faster                                                 |
| genshi_text     | 17.7 ms                                                | 18.7 ms: 1.05x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                 |
| django_template | 24.4 ms                                                | 26.5 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 77.5 ms: 5.06x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 155 ms: 3.12x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 113 us: 2.89x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.2 ms: 2.61x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 407 ms: 2.49x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 425 ms: 2.40x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.16x faster                                                  |
| async_tree_none               | 391 ms                                                 | 185 ms: 2.11x faster                                                  |
| mdp                           | 1.65 sec                                               | 867 ms: 1.90x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.86 ms: 1.74x faster                                                 |
| raytrace                      | 327 ms                                                 | 207 ms: 1.58x faster                                                  |
| go                            | 163 ms                                                 | 106 ms: 1.55x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 440 ms: 1.52x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 95.0 ms: 1.47x faster                                                 |
| deepcopy                      | 276 us                                                 | 187 us: 1.47x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 23.8 us: 1.46x faster                                                 |
| chaos                         | 67.7 ms                                                | 47.0 ms: 1.44x faster                                                 |
| richards_super                | 61.0 ms                                                | 43.9 ms: 1.39x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 53.8 ms: 1.35x faster                                                 |
| richards                      | 52.3 ms                                                | 39.5 ms: 1.32x faster                                                 |
| pylint                        | 231 ms                                                 | 176 ms: 1.31x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 27.2 ms: 1.31x faster                                                 |
| pyflate                       | 448 ms                                                 | 351 ms: 1.28x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.58 sec: 1.28x faster                                                |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| html5lib                      | 43.5 ms                                                | 35.1 ms: 1.24x faster                                                 |
| float                         | 72.4 ms                                                | 58.7 ms: 1.23x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 78.7 ms: 1.21x faster                                                 |
| comprehensions                | 17.3 us                                                | 14.5 us: 1.19x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 61.7 ms: 1.19x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 86.8 ms: 1.18x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.98 us: 1.17x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.14 ms: 1.16x faster                                                 |
| pycparser                     | 887 ms                                                 | 765 ms: 1.16x faster                                                  |
| sphinx                        | 729 ms                                                 | 637 ms: 1.14x faster                                                  |
| hexiom                        | 6.25 ms                                                | 5.47 ms: 1.14x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                |
| pickle_pure_python            | 285 us                                                 | 251 us: 1.13x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.7 ms: 1.13x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 82.8 ms: 1.12x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.20 sec: 1.11x faster                                                |
| docutils                      | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                |
| logging_format                | 5.03 us                                                | 4.54 us: 1.11x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 587 ms: 1.10x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 86.6 ms: 1.10x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.22 us: 1.09x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 209 ms: 1.08x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.18 ms: 1.07x faster                                                 |
| mako                          | 9.81 ms                                                | 9.15 ms: 1.07x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.5 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.24 ms: 1.05x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 190 us: 1.04x faster                                                  |
| 2to3                          | 201 ms                                                 | 193 ms: 1.04x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.04x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| sympy_str                     | 166 ms                                                 | 160 ms: 1.04x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.32 sec: 1.04x faster                                                |
| connected_components          | 318 ms                                                 | 314 ms: 1.01x faster                                                  |
| nbody                         | 92.5 ms                                                | 91.7 ms: 1.01x faster                                                 |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                 |
| fannkuch                      | 303 ms                                                 | 302 ms: 1.00x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 544 us: 1.00x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 271 ms: 1.01x slower                                                  |
| json                          | 3.10 ms                                                | 3.13 ms: 1.01x slower                                                 |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 78.9 ms: 1.01x slower                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 76.1 ms: 1.02x slower                                                 |
| xml_etree_process             | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                 |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                  |
| genshi_text                   | 17.7 ms                                                | 18.7 ms: 1.05x slower                                                 |
| many_optionals                | 486 us                                                 | 513 us: 1.06x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                 |
| django_template               | 24.4 ms                                                | 26.5 ms: 1.09x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.61 us: 1.09x slower                                                 |
| dask                          | 789 ms                                                 | 861 ms: 1.09x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.0 ms: 1.10x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.4 us: 1.11x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 61.3 ms: 1.14x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.16x slower                                                 |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                  |
| nqueens                       | 63.8 ms                                                | 75.9 ms: 1.19x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.22 ms: 1.19x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 71.5 ms: 1.28x slower                                                 |
| telco                         | 3.49 ms                                                | 4.82 ms: 1.38x slower                                                 |
| logging_silent                | 117 ns                                                 | 346 ns: 2.96x slower                                                  |
| coverage                      | 41.2 ms                                                | 333 ms: 8.08x slower                                                  |
| thrift                        | 562 us                                                 | 44.1 ms: 78.47x slower                                                |
| Geometric mean                | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (2): pathlib, asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.16x