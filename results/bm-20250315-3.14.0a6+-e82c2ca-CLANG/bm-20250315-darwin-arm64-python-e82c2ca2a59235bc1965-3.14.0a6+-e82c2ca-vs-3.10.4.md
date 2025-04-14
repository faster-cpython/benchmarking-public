# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: darwin-arm64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.394x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 157 ms: 1.28x faster                                                   |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                 |
| html5lib       | 43.5 ms                                                | 30.6 ms: 1.42x faster                                                  |
| sphinx         | 729 ms                                                 | 575 ms: 1.27x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.5 ms: 6.70x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.52x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 354 ms: 2.87x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 189 ms: 2.54x faster                                                   |
| async_tree_none               | 391 ms                                                 | 156 ms: 2.51x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 355 ms: 1.88x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.2 ms: 1.35x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 250 ms: 1.03x slower                                                   |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.15x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 45.8 ms: 1.58x faster                                                  |
| nbody          | 92.5 ms                                                | 66.7 ms: 1.39x faster                                                  |
| pidigits       | 280 ms                                                 | 290 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 65.8 ms: 1.45x faster                                                  |
| regex_dna      | 175 ms                                                 | 153 ms: 1.14x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.45 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 194 us: 1.47x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.21 sec: 1.42x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 35.5 ms: 1.26x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.44 ms: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 70.3 ms: 1.06x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 51.0 ms: 1.06x faster                                                  |
| json_loads           | 16.6 us                                                | 18.3 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.7 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 13.3 ms: 1.33x faster                                                  |
| mako            | 9.81 ms                                                | 7.56 ms: 1.30x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 28.4 ms: 1.24x faster                                                  |
| django_template | 24.4 ms                                                | 20.1 ms: 1.21x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.5 ms: 6.70x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 90.5 us: 3.60x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.52x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.0 ms: 3.32x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 354 ms: 2.87x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 189 ms: 2.54x faster                                                   |
| async_tree_none               | 391 ms                                                 | 156 ms: 2.51x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.18 ms: 2.29x faster                                                  |
| go                            | 163 ms                                                 | 76.2 ms: 2.14x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 17.3 us: 2.01x faster                                                  |
| logging_silent                | 117 ns                                                 | 60.0 ns: 1.95x faster                                                  |
| raytrace                      | 327 ms                                                 | 170 ms: 1.92x faster                                                   |
| deepcopy                      | 276 us                                                 | 146 us: 1.89x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 355 ms: 1.88x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 75.1 ms: 1.86x faster                                                  |
| richards_super                | 61.0 ms                                                | 34.1 ms: 1.79x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 41.0 ms: 1.77x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.0 ms: 1.74x faster                                                  |
| richards                      | 52.3 ms                                                | 30.4 ms: 1.72x faster                                                  |
| generators                    | 31.7 ms                                                | 19.0 ms: 1.67x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.5 us: 1.64x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                   |
| float                         | 72.4 ms                                                | 45.8 ms: 1.58x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.02 ms: 1.55x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.56 us: 1.49x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                                   |
| pylint                        | 231 ms                                                 | 156 ms: 1.48x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 194 us: 1.47x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 24.3 ms: 1.47x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 65.8 ms: 1.45x faster                                                  |
| logging_format                | 5.03 us                                                | 3.47 us: 1.45x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.19 us: 1.44x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.33 ms: 1.43x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.21 sec: 1.42x faster                                                 |
| html5lib                      | 43.5 ms                                                | 30.6 ms: 1.42x faster                                                  |
| pyflate                       | 448 ms                                                 | 317 ms: 1.41x faster                                                   |
| pprint_pformat                | 1.33 sec                                               | 942 ms: 1.41x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 73.2 ms: 1.40x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 463 ms: 1.40x faster                                                   |
| nbody                         | 92.5 ms                                                | 66.7 ms: 1.39x faster                                                  |
| pycparser                     | 887 ms                                                 | 652 ms: 1.36x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.2 ms: 1.35x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 13.3 ms: 1.33x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 57.0 ms: 1.33x faster                                                  |
| thrift                        | 562 us                                                 | 429 us: 1.31x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 55.9 ms: 1.31x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                 |
| mako                          | 9.81 ms                                                | 7.56 ms: 1.30x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 72.3 ms: 1.28x faster                                                  |
| 2to3                          | 201 ms                                                 | 157 ms: 1.28x faster                                                   |
| sphinx                        | 729 ms                                                 | 575 ms: 1.27x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 35.5 ms: 1.26x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 76.6 ms: 1.24x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 28.4 ms: 1.24x faster                                                  |
| sympy_str                     | 166 ms                                                 | 136 ms: 1.22x faster                                                   |
| django_template               | 24.4 ms                                                | 20.1 ms: 1.21x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.21x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 188 ms: 1.20x faster                                                   |
| sympy_expand                  | 269 ms                                                 | 228 ms: 1.18x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 473 us: 1.15x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.99 ms: 1.14x faster                                                  |
| regex_dna                     | 175 ms                                                 | 153 ms: 1.14x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.1 ms: 1.12x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.44 ms: 1.12x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.11x faster                                                 |
| many_optionals                | 486 us                                                 | 441 us: 1.10x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.13 sec: 1.10x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                  |
| fannkuch                      | 303 ms                                                 | 281 ms: 1.08x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 72.5 ms: 1.07x faster                                                  |
| nqueens                       | 63.8 ms                                                | 60.0 ms: 1.06x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.3 ms: 1.06x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 51.0 ms: 1.06x faster                                                  |
| connected_components          | 318 ms                                                 | 303 ms: 1.05x faster                                                   |
| dask                          | 789 ms                                                 | 765 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.18 ms: 1.02x slower                                                  |
| asyncio_websockets            | 242 ms                                                 | 250 ms: 1.03x slower                                                   |
| pidigits                      | 280 ms                                                 | 290 ms: 1.03x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.45 ms: 1.05x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.7 ms: 1.08x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 61.8 ms: 1.10x slower                                                  |
| json_loads                    | 16.6 us                                                | 18.3 us: 1.11x slower                                                  |
| coverage                      | 41.2 ms                                                | 46.4 ms: 1.13x slower                                                  |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                   |
| create_gc_cycles              | 1.16 ms                                                | 1.33 ms: 1.14x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                  |
| telco                         | 3.49 ms                                                | 4.65 ms: 1.33x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.39x faster                                                           |

Benchmark hidden because not significant (1): shortest_path
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.394x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x