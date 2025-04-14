# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 195 ms: 1.03x faster                                                   |
| docutils       | 1.74 sec                                               | 1.47 sec: 1.18x faster                                                 |
| html5lib       | 43.5 ms                                                | 36.2 ms: 1.20x faster                                                  |
| sphinx         | 729 ms                                                 | 635 ms: 1.15x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 83.9 ms: 4.67x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.19x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 343 ms: 2.96x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 358 ms: 2.84x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 207 ms: 2.32x faster                                                   |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.27x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                   |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.98x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 54.8 ms: 1.32x faster                                                  |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                   |
| nbody          | 92.5 ms                                                | 105 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 19.1 ms                                                | 14.9 ms: 1.28x faster                                                  |
| regex_dna      | 175 ms                                                 | 137 ms: 1.28x faster                                                   |
| regex_effbot   | 2.34 ms                                                | 2.08 ms: 1.12x faster                                                  |
| regex_compile  | 95.6 ms                                                | 86.4 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 250 us: 1.14x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 66.4 ms: 1.12x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.60 sec: 1.08x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 187 us: 1.06x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.95 ms: 1.04x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 44.9 ms: 1.01x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 60.5 ms: 1.12x slower                                                  |
| json_loads           | 16.6 us                                                | 18.6 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 15.6 ms: 1.22x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 18.3 ms: 1.04x slower                                                  |
| genshi_xml      | 35.1 ms                                                | 37.4 ms: 1.06x slower                                                  |
| mako            | 9.81 ms                                                | 10.8 ms: 1.10x slower                                                  |
| django_template | 24.4 ms                                                | 26.9 ms: 1.10x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 83.9 ms: 4.67x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.19x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 343 ms: 2.96x faster                                                   |
| subparsers                    | 39.8 ms                                                | 13.6 ms: 2.93x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 358 ms: 2.84x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 116 us: 2.80x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 207 ms: 2.32x faster                                                   |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.27x faster                                                   |
| gc_traversal                  | 2.71 ms                                                | 1.43 ms: 1.89x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                                   |
| deltablue                     | 4.99 ms                                                | 3.08 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                   |
| go                            | 163 ms                                                 | 107 ms: 1.52x faster                                                   |
| create_gc_cycles              | 1.16 ms                                                | 780 us: 1.49x faster                                                   |
| deepcopy                      | 276 us                                                 | 186 us: 1.49x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 24.8 us: 1.40x faster                                                  |
| raytrace                      | 327 ms                                                 | 239 ms: 1.37x faster                                                   |
| chaos                         | 67.7 ms                                                | 49.7 ms: 1.36x faster                                                  |
| logging_silent                | 117 ns                                                 | 87.2 ns: 1.34x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 106 ms: 1.32x faster                                                   |
| float                         | 72.4 ms                                                | 54.8 ms: 1.32x faster                                                  |
| pylint                        | 231 ms                                                 | 177 ms: 1.30x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 27.7 ms: 1.28x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 14.9 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.28x faster                                                   |
| richards_super                | 61.0 ms                                                | 48.7 ms: 1.25x faster                                                  |
| pycparser                     | 887 ms                                                 | 711 ms: 1.25x faster                                                   |
| richards                      | 52.3 ms                                                | 42.4 ms: 1.23x faster                                                  |
| pyflate                       | 448 ms                                                 | 370 ms: 1.21x faster                                                   |
| html5lib                      | 43.5 ms                                                | 36.2 ms: 1.20x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 60.6 ms: 1.19x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.47 sec: 1.18x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.96 us: 1.18x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.72 sec: 1.17x faster                                                 |
| comprehensions                | 17.3 us                                                | 14.8 us: 1.17x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.77 ms: 1.17x faster                                                  |
| sphinx                        | 729 ms                                                 | 635 ms: 1.15x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 250 us: 1.14x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.08 ms: 1.12x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 66.4 ms: 1.12x faster                                                  |
| logging_simple                | 4.59 us                                                | 4.13 us: 1.11x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.33 us: 1.11x faster                                                  |
| logging_format                | 5.03 us                                                | 4.53 us: 1.11x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 86.4 ms: 1.11x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                  |
| thrift                        | 562 us                                                 | 513 us: 1.10x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 67.0 ms: 1.09x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 69.6 ms: 1.09x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.23 sec: 1.08x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 85.8 ms: 1.08x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.60 sec: 1.08x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 604 ms: 1.07x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                   |
| generators                    | 31.7 ms                                                | 29.8 ms: 1.07x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 187 us: 1.06x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 90.6 ms: 1.05x faster                                                  |
| pathlib                       | 25.7 ms                                                | 24.5 ms: 1.05x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.95 ms: 1.04x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 98.6 ms: 1.04x faster                                                  |
| hexiom                        | 6.25 ms                                                | 6.02 ms: 1.04x faster                                                  |
| 2to3                          | 201 ms                                                 | 195 ms: 1.03x faster                                                   |
| python_startup                | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 3.38 sec: 1.02x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 13.0 ms: 1.01x faster                                                  |
| many_optionals                | 486 us                                                 | 484 us: 1.00x faster                                                   |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                   |
| xml_etree_process             | 44.6 ms                                                | 44.9 ms: 1.01x slower                                                  |
| mdp                           | 1.65 sec                                               | 1.67 sec: 1.01x slower                                                 |
| sympy_str                     | 166 ms                                                 | 168 ms: 1.01x slower                                                   |
| genshi_text                   | 17.7 ms                                                | 18.3 ms: 1.04x slower                                                  |
| scimark_fft                   | 225 ms                                                 | 238 ms: 1.06x slower                                                   |
| sympy_expand                  | 269 ms                                                 | 286 ms: 1.06x slower                                                   |
| genshi_xml                    | 35.1 ms                                                | 37.4 ms: 1.06x slower                                                  |
| fannkuch                      | 303 ms                                                 | 327 ms: 1.08x slower                                                   |
| mako                          | 9.81 ms                                                | 10.8 ms: 1.10x slower                                                  |
| django_template               | 24.4 ms                                                | 26.9 ms: 1.10x slower                                                  |
| connected_components          | 318 ms                                                 | 352 ms: 1.10x slower                                                   |
| xml_etree_generate            | 53.9 ms                                                | 60.5 ms: 1.12x slower                                                  |
| json_loads                    | 16.6 us                                                | 18.6 us: 1.12x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 87.6 ms: 1.13x slower                                                  |
| shortest_path                 | 328 ms                                                 | 370 ms: 1.13x slower                                                   |
| nbody                         | 92.5 ms                                                | 105 ms: 1.13x slower                                                   |
| nqueens                       | 63.8 ms                                                | 75.0 ms: 1.17x slower                                                  |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                   |
| bench_mp_pool                 | 56.0 ms                                                | 66.6 ms: 1.19x slower                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.09 ms: 1.20x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.6 ms: 1.22x slower                                                  |
| bench_thread_pool             | 545 us                                                 | 756 us: 1.39x slower                                                   |
| coverage                      | 41.2 ms                                                | 61.1 ms: 1.48x slower                                                  |
| telco                         | 3.49 ms                                                | 5.24 ms: 1.50x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): json
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.30x