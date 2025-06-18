# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.200x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 191 ms: 1.05x faster                                                  |
| docutils       | 1.74 sec                                               | 1.63 sec: 1.07x faster                                                |
| html5lib       | 43.5 ms                                                | 33.7 ms: 1.29x faster                                                 |
| sphinx         | 729 ms                                                 | 659 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.8 ms: 5.31x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 390 ms: 2.60x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 405 ms: 2.51x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 207 ms: 2.32x faster                                                  |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 393 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 452 ms: 1.48x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 329 ms: 1.41x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.90x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| nbody          | 92.5 ms                                                | 80.0 ms: 1.16x faster                                                 |
| pidigits       | 280 ms                                                 | 285 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 76.4 ms: 1.25x faster                                                 |
| regex_dna      | 175 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 150 us: 1.32x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 221 us: 1.29x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.41 sec: 1.22x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 43.4 ms: 1.03x faster                                                 |
| json_dumps           | 8.31 ms                                                | 8.11 ms: 1.02x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 77.1 ms: 1.04x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 64.3 ms: 1.19x slower                                                 |
| json_loads           | 16.6 us                                                | 22.8 us: 1.37x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.7 ms: 1.05x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.9 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.17 ms: 1.20x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.9 ms: 1.11x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.8 ms: 1.04x faster                                                 |
| django_template | 24.4 ms                                                | 25.8 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.8 ms: 5.31x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 125 us: 2.61x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 390 ms: 2.60x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 405 ms: 2.51x faster                                                  |
| subparsers                    | 39.8 ms                                                | 16.2 ms: 2.45x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 207 ms: 2.32x faster                                                  |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                  |
| go                            | 163 ms                                                 | 79.8 ms: 2.05x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.70 ms: 1.85x faster                                                 |
| mdp                           | 1.65 sec                                               | 895 ms: 1.84x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.6 us: 1.77x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 393 ms: 1.70x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.8 ms: 1.55x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 91.1 ms: 1.54x faster                                                 |
| raytrace                      | 327 ms                                                 | 214 ms: 1.53x faster                                                  |
| chaos                         | 67.7 ms                                                | 44.7 ms: 1.52x faster                                                 |
| richards_super                | 61.0 ms                                                | 41.0 ms: 1.49x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 452 ms: 1.48x faster                                                  |
| pyflate                       | 448 ms                                                 | 304 ms: 1.47x faster                                                  |
| deepcopy                      | 276 us                                                 | 190 us: 1.45x faster                                                  |
| richards                      | 52.3 ms                                                | 36.5 ms: 1.43x faster                                                 |
| float                         | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| generators                    | 31.7 ms                                                | 23.4 ms: 1.36x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 150 us: 1.32x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 27.3 ms: 1.30x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.7 ms: 1.29x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.29x faster                                                  |
| pylint                        | 231 ms                                                 | 181 ms: 1.28x faster                                                  |
| comprehensions                | 17.3 us                                                | 13.6 us: 1.27x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.59 sec: 1.27x faster                                                |
| hexiom                        | 6.25 ms                                                | 4.96 ms: 1.26x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 76.4 ms: 1.25x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.41 sec: 1.22x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 60.4 ms: 1.21x faster                                                 |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.20x faster                                                  |
| mako                          | 9.81 ms                                                | 8.17 ms: 1.20x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 81.9 ms: 1.16x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 88.6 ms: 1.16x faster                                                 |
| nbody                         | 92.5 ms                                                | 80.0 ms: 1.16x faster                                                 |
| logging_format                | 5.03 us                                                | 4.39 us: 1.15x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 2.04 us: 1.14x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.07 us: 1.13x faster                                                 |
| pycparser                     | 887 ms                                                 | 792 ms: 1.12x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 15.9 ms: 1.11x faster                                                 |
| sphinx                        | 729 ms                                                 | 659 ms: 1.11x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 12.2 ms: 1.08x faster                                                 |
| pathlib                       | 25.7 ms                                                | 23.8 ms: 1.08x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 86.7 ms: 1.07x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.63 sec: 1.07x faster                                                |
| 2to3                          | 201 ms                                                 | 191 ms: 1.05x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.7 ms: 1.05x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.8 ms: 1.04x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 43.4 ms: 1.03x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 8.11 ms: 1.02x faster                                                 |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                                  |
| connected_components          | 318 ms                                                 | 315 ms: 1.01x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 285 ms: 1.01x slower                                                  |
| sympy_str                     | 166 ms                                                 | 169 ms: 1.02x slower                                                  |
| thrift                        | 562 us                                                 | 575 us: 1.02x slower                                                  |
| xml_etree_parse               | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 77.1 ms: 1.04x slower                                                 |
| shortest_path                 | 328 ms                                                 | 342 ms: 1.04x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 81.4 ms: 1.05x slower                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.40 sec: 1.06x slower                                                |
| django_template               | 24.4 ms                                                | 25.8 ms: 1.06x slower                                                 |
| pprint_safe_repr              | 648 ms                                                 | 693 ms: 1.07x slower                                                  |
| nqueens                       | 63.8 ms                                                | 68.3 ms: 1.07x slower                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.71 sec: 1.08x slower                                                |
| scimark_fft                   | 225 ms                                                 | 245 ms: 1.09x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.9 ms: 1.09x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 296 ms: 1.10x slower                                                  |
| many_optionals                | 486 us                                                 | 536 us: 1.10x slower                                                  |
| fannkuch                      | 303 ms                                                 | 349 ms: 1.15x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 64.3 ms: 1.19x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.40 ms: 1.20x slower                                                 |
| json                          | 3.10 ms                                                | 3.85 ms: 1.24x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.32 ms: 1.26x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.90 us: 1.28x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 75.2 ms: 1.34x slower                                                 |
| json_loads                    | 16.6 us                                                | 22.8 us: 1.37x slower                                                 |
| async_generators              | 233 ms                                                 | 329 ms: 1.41x slower                                                  |
| coverage                      | 41.2 ms                                                | 60.8 ms: 1.48x slower                                                 |
| telco                         | 3.49 ms                                                | 5.63 ms: 1.61x slower                                                 |
| logging_silent                | 117 ns                                                 | 417 ns: 3.56x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.200x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.16x