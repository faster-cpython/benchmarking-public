# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.322x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 170 ms: 1.18x faster                                                   |
| docutils       | 1.74 sec                                               | 1.48 sec: 1.17x faster                                                 |
| html5lib       | 43.5 ms                                                | 32.3 ms: 1.35x faster                                                  |
| sphinx         | 729 ms                                                 | 598 ms: 1.22x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.4 ms: 5.99x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 143 ms: 3.37x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 385 ms: 2.63x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 391 ms: 2.60x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 202 ms: 2.38x faster                                                   |
| async_tree_none               | 391 ms                                                 | 167 ms: 2.34x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                   |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.19x faster                                                  |
| async_generators              | 233 ms                                                 | 283 ms: 1.22x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.02x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 45.7 ms: 1.58x faster                                                  |
| nbody          | 92.5 ms                                                | 69.6 ms: 1.33x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 73.5 ms: 1.30x faster                                                  |
| regex_dna      | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 140 us: 1.42x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.25 sec: 1.38x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 212 us: 1.34x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 36.5 ms: 1.22x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 99.1 ms: 1.10x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.53 ms: 1.10x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 51.4 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                  |
| json_loads           | 16.6 us                                                | 17.8 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.7 ms: 1.05x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.2 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.69 ms: 1.47x faster                                                  |
| genshi_text     | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 32.1 ms: 1.10x faster                                                  |
| django_template | 24.4 ms                                                | 22.7 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.4 ms: 5.99x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 143 ms: 3.37x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 98.3 us: 3.32x faster                                                  |
| subparsers                    | 39.8 ms                                                | 12.8 ms: 3.12x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 385 ms: 2.63x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 391 ms: 2.60x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 202 ms: 2.38x faster                                                   |
| async_tree_none               | 391 ms                                                 | 167 ms: 2.34x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.29 ms: 2.18x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| richards_super                | 61.0 ms                                                | 35.3 ms: 1.73x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 20.3 us: 1.71x faster                                                  |
| raytrace                      | 327 ms                                                 | 192 ms: 1.70x faster                                                   |
| deepcopy                      | 276 us                                                 | 162 us: 1.70x faster                                                   |
| richards                      | 52.3 ms                                                | 31.7 ms: 1.65x faster                                                  |
| logging_silent                | 117 ns                                                 | 71.3 ns: 1.64x faster                                                  |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 87.8 ms: 1.59x faster                                                  |
| float                         | 72.4 ms                                                | 45.7 ms: 1.58x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.3 ms: 1.56x faster                                                  |
| chaos                         | 67.7 ms                                                | 43.8 ms: 1.54x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 64.3 ms: 1.48x faster                                                  |
| mako                          | 9.81 ms                                                | 6.69 ms: 1.47x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 140 us: 1.42x faster                                                   |
| pyflate                       | 448 ms                                                 | 321 ms: 1.40x faster                                                   |
| comprehensions                | 17.3 us                                                | 12.4 us: 1.39x faster                                                  |
| pylint                        | 231 ms                                                 | 167 ms: 1.38x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.25 sec: 1.38x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 25.9 ms: 1.38x faster                                                  |
| html5lib                      | 43.5 ms                                                | 32.3 ms: 1.35x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 212 us: 1.34x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.74 us: 1.34x faster                                                  |
| nbody                         | 92.5 ms                                                | 69.6 ms: 1.33x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.96 ms: 1.30x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 73.5 ms: 1.30x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 79.9 ms: 1.28x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.04 sec: 1.28x faster                                                 |
| logging_format                | 5.03 us                                                | 3.92 us: 1.28x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 507 ms: 1.28x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.60 us: 1.28x faster                                                  |
| generators                    | 31.7 ms                                                | 25.0 ms: 1.27x faster                                                  |
| pycparser                     | 887 ms                                                 | 713 ms: 1.24x faster                                                   |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| hexiom                        | 6.25 ms                                                | 5.06 ms: 1.24x faster                                                  |
| thrift                        | 562 us                                                 | 456 us: 1.23x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.4 ms: 1.23x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 36.5 ms: 1.22x faster                                                  |
| sphinx                        | 729 ms                                                 | 598 ms: 1.22x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 76.1 ms: 1.22x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 60.6 ms: 1.21x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 189 ms: 1.19x faster                                                   |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.19x faster                                                  |
| 2to3                          | 201 ms                                                 | 170 ms: 1.18x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.48 sec: 1.17x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.02 sec: 1.14x faster                                                 |
| sympy_str                     | 166 ms                                                 | 146 ms: 1.13x faster                                                   |
| sympy_integrate               | 13.2 ms                                                | 11.7 ms: 1.12x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.11x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.07 ms: 1.11x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 99.1 ms: 1.10x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.53 ms: 1.10x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 32.1 ms: 1.10x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 505 us: 1.08x faster                                                   |
| sympy_expand                  | 269 ms                                                 | 250 ms: 1.08x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.9 ms: 1.08x faster                                                  |
| django_template               | 24.4 ms                                                | 22.7 ms: 1.08x faster                                                  |
| fannkuch                      | 303 ms                                                 | 287 ms: 1.06x faster                                                   |
| python_startup                | 19.6 ms                                                | 18.7 ms: 1.05x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 51.4 ms: 1.05x faster                                                  |
| connected_components          | 318 ms                                                 | 304 ms: 1.05x faster                                                   |
| many_optionals                | 486 us                                                 | 473 us: 1.03x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 75.8 ms: 1.03x faster                                                  |
| json                          | 3.10 ms                                                | 3.07 ms: 1.01x faster                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| shortest_path                 | 328 ms                                                 | 336 ms: 1.02x slower                                                   |
| nqueens                       | 63.8 ms                                                | 66.0 ms: 1.03x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.07x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 61.4 ms: 1.10x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.2 ms: 1.11x slower                                                  |
| coverage                      | 41.2 ms                                                | 47.1 ms: 1.14x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.13 ms: 1.16x slower                                                  |
| async_generators              | 233 ms                                                 | 283 ms: 1.22x slower                                                   |
| telco                         | 3.49 ms                                                | 4.49 ms: 1.29x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.32x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.322x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.17x