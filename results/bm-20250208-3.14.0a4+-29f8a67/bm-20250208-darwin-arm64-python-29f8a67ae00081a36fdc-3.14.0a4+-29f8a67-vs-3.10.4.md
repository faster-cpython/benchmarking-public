# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.388x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 163 ms: 1.24x faster                                                   |
| docutils       | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.2 ms: 1.49x faster                                                  |
| sphinx         | 729 ms                                                 | 566 ms: 1.29x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.6 ms: 6.26x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 381 ms: 2.67x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.44x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                  |
| async_generators              | 233 ms                                                 | 252 ms: 1.08x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.10x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.9 ms: 1.54x faster                                                  |
| nbody          | 92.5 ms                                                | 71.1 ms: 1.30x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.1 ms: 1.42x faster                                                  |
| regex_dna      | 175 ms                                                 | 144 ms: 1.21x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.1 ms: 1.12x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 199 us: 1.43x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 143 us: 1.39x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 38.6 ms: 1.16x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 70.4 ms: 1.06x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.6 ms: 1.05x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.37 ms: 1.33x faster                                                  |
| genshi_text     | 17.7 ms                                                | 13.5 ms: 1.31x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 28.4 ms: 1.24x faster                                                  |
| django_template | 24.4 ms                                                | 20.8 ms: 1.17x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.6 ms: 6.26x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 92.4 us: 3.53x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.8 ms: 3.38x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 381 ms: 2.67x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.44x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.34 ms: 2.13x faster                                                  |
| go                            | 163 ms                                                 | 79.6 ms: 2.05x faster                                                  |
| raytrace                      | 327 ms                                                 | 171 ms: 1.91x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 18.4 us: 1.89x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| deepcopy                      | 276 us                                                 | 148 us: 1.86x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 78.1 ms: 1.79x faster                                                  |
| logging_silent                | 117 ns                                                 | 65.9 ns: 1.78x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 763 us: 1.77x faster                                                   |
| chaos                         | 67.7 ms                                                | 38.9 ms: 1.74x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 919 us: 1.70x faster                                                   |
| richards_super                | 61.0 ms                                                | 35.9 ms: 1.70x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 42.7 ms: 1.69x faster                                                  |
| richards                      | 52.3 ms                                                | 31.7 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 61.0 ms: 1.56x faster                                                  |
| pyflate                       | 448 ms                                                 | 288 ms: 1.56x faster                                                   |
| float                         | 72.4 ms                                                | 46.9 ms: 1.54x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.2 ms: 1.49x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.8 us: 1.47x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.58 us: 1.47x faster                                                  |
| pylint                        | 231 ms                                                 | 159 ms: 1.45x faster                                                   |
| hexiom                        | 6.25 ms                                                | 4.31 ms: 1.45x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.19 us: 1.44x faster                                                  |
| logging_format                | 5.03 us                                                | 3.49 us: 1.44x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 199 us: 1.43x faster                                                   |
| pprint_pformat                | 1.33 sec                                               | 931 ms: 1.43x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 67.1 ms: 1.42x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.43 ms: 1.41x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 73.0 ms: 1.41x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 462 ms: 1.40x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 52.5 ms: 1.40x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 143 us: 1.39x faster                                                   |
| generators                    | 31.7 ms                                                | 22.9 ms: 1.38x faster                                                  |
| pycparser                     | 887 ms                                                 | 647 ms: 1.37x faster                                                   |
| k_core                        | 2.01 sec                                               | 1.51 sec: 1.33x faster                                                 |
| mako                          | 9.81 ms                                                | 7.37 ms: 1.33x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 172 ms: 1.31x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 13.5 ms: 1.31x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.1 ms: 1.30x faster                                                  |
| nbody                         | 92.5 ms                                                | 71.1 ms: 1.30x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 27.3 ms: 1.30x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                  |
| thrift                        | 562 us                                                 | 436 us: 1.29x faster                                                   |
| sphinx                        | 729 ms                                                 | 566 ms: 1.29x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 73.1 ms: 1.27x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.75 ms: 1.24x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 28.4 ms: 1.24x faster                                                  |
| 2to3                          | 201 ms                                                 | 163 ms: 1.24x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                 |
| regex_dna                     | 175 ms                                                 | 144 ms: 1.21x faster                                                   |
| sympy_str                     | 166 ms                                                 | 138 ms: 1.20x faster                                                   |
| fannkuch                      | 303 ms                                                 | 254 ms: 1.19x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.89 sec: 1.19x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.2 ms: 1.18x faster                                                  |
| django_template               | 24.4 ms                                                | 20.8 ms: 1.17x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 232 ms: 1.16x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 38.6 ms: 1.16x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 32.2 ms: 1.16x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                  |
| pathlib                       | 25.7 ms                                                | 22.9 ms: 1.12x faster                                                  |
| many_optionals                | 486 us                                                 | 432 us: 1.12x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.12x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 17.1 ms: 1.12x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 491 us: 1.11x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 70.3 ms: 1.11x faster                                                  |
| nqueens                       | 63.8 ms                                                | 58.3 ms: 1.09x faster                                                  |
| sqlglot_normalize             | 192 ms                                                 | 177 ms: 1.09x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.08x faster                                                   |
| connected_components          | 318 ms                                                 | 297 ms: 1.07x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.4 ms: 1.06x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.6 ms: 1.05x faster                                                  |
| json                          | 3.10 ms                                                | 2.99 ms: 1.04x faster                                                  |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                   |
| shortest_path                 | 328 ms                                                 | 325 ms: 1.01x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.52 us: 1.03x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.2 ms: 1.06x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                  |
| async_generators              | 233 ms                                                 | 252 ms: 1.08x slower                                                   |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| coverage                      | 41.2 ms                                                | 46.0 ms: 1.12x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                  |
| telco                         | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.38x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.388x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x