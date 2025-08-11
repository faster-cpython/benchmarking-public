# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.323x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 171 ms: 1.18x faster                                                  |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                |
| html5lib       | 43.5 ms                                                | 33.0 ms: 1.32x faster                                                 |
| sphinx         | 729 ms                                                 | 576 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.1 ms: 6.02x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 376 ms: 2.70x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 382 ms: 2.67x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 168 ms: 2.33x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 420 ms: 1.59x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                 |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.05x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 50.6 ms: 1.43x faster                                                 |
| nbody          | 92.5 ms                                                | 81.3 ms: 1.14x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 73.1 ms: 1.31x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.15 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 5.77 ms: 1.44x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 219 us: 1.30x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 158 us: 1.25x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 39.7 ms: 1.12x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 71.2 ms: 1.04x faster                                                 |
| json_loads           | 16.6 us                                                | 17.1 us: 1.03x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.6 ms: 1.11x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.95 ms: 1.23x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.2 ms: 1.17x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 32.7 ms: 1.07x faster                                                 |
| django_template | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.1 ms: 6.02x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 95.7 us: 3.41x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 376 ms: 2.70x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 382 ms: 2.67x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 168 ms: 2.33x faster                                                  |
| mdp                           | 1.65 sec                                               | 776 ms: 2.13x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.44 ms: 2.04x faster                                                 |
| go                            | 163 ms                                                 | 86.1 ms: 1.90x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| raytrace                      | 327 ms                                                 | 178 ms: 1.84x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.3 ms: 1.72x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 85.1 ms: 1.65x faster                                                 |
| richards_super                | 61.0 ms                                                | 37.8 ms: 1.61x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 45.3 ms: 1.60x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 21.7 us: 1.60x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 420 ms: 1.59x faster                                                  |
| deepcopy                      | 276 us                                                 | 173 us: 1.59x faster                                                  |
| subparsers                    | 39.8 ms                                                | 25.3 ms: 1.57x faster                                                 |
| logging_silent                | 117 ns                                                 | 75.2 ns: 1.56x faster                                                 |
| richards                      | 52.3 ms                                                | 33.8 ms: 1.55x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 62.8 ms: 1.52x faster                                                 |
| comprehensions                | 17.3 us                                                | 11.7 us: 1.47x faster                                                 |
| pyflate                       | 448 ms                                                 | 306 ms: 1.46x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 5.77 ms: 1.44x faster                                                 |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                  |
| float                         | 72.4 ms                                                | 50.6 ms: 1.43x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 25.0 ms: 1.42x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 52.7 ms: 1.39x faster                                                 |
| logging_format                | 5.03 us                                                | 3.63 us: 1.39x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.36 us: 1.37x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 75.9 ms: 1.35x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.64 ms: 1.34x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.0 ms: 1.32x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                                |
| deepcopy_reduce               | 2.32 us                                                | 1.77 us: 1.31x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 73.1 ms: 1.31x faster                                                 |
| generators                    | 31.7 ms                                                | 24.3 ms: 1.31x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 219 us: 1.30x faster                                                  |
| pycparser                     | 887 ms                                                 | 694 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| sphinx                        | 729 ms                                                 | 576 ms: 1.27x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 158 us: 1.25x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| thrift                        | 562 us                                                 | 455 us: 1.24x faster                                                  |
| mako                          | 9.81 ms                                                | 7.95 ms: 1.23x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.8 ms: 1.22x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.21x faster                                                |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 540 ms: 1.20x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 77.2 ms: 1.20x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 188 ms: 1.20x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                |
| 2to3                          | 201 ms                                                 | 171 ms: 1.18x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 15.2 ms: 1.17x faster                                                 |
| nbody                         | 92.5 ms                                                | 81.3 ms: 1.14x faster                                                 |
| sympy_str                     | 166 ms                                                 | 146 ms: 1.14x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 39.7 ms: 1.12x faster                                                 |
| python_startup                | 19.6 ms                                                | 17.6 ms: 1.11x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 247 ms: 1.09x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.15 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.14 ms: 1.09x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 502 us: 1.09x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.19 sec: 1.08x faster                                                |
| genshi_xml                    | 35.1 ms                                                | 32.7 ms: 1.07x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.2 ms: 1.07x faster                                                 |
| django_template               | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 74.0 ms: 1.05x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 71.2 ms: 1.04x faster                                                 |
| nqueens                       | 63.8 ms                                                | 61.4 ms: 1.04x faster                                                 |
| connected_components          | 318 ms                                                 | 306 ms: 1.04x faster                                                  |
| json                          | 3.10 ms                                                | 2.99 ms: 1.04x faster                                                 |
| fannkuch                      | 303 ms                                                 | 293 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 795 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| shortest_path                 | 328 ms                                                 | 336 ms: 1.02x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.1 us: 1.03x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.64 us: 1.11x slower                                                 |
| coverage                      | 41.2 ms                                                | 46.4 ms: 1.13x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.21 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                                  |
| many_optionals                | 486 us                                                 | 593 us: 1.22x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 71.0 ms: 1.27x slower                                                 |
| telco                         | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.32x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.323x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.17x