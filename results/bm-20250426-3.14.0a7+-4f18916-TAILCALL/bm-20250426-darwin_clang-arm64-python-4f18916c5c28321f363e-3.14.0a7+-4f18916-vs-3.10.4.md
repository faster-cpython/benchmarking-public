# Results vs. 3.10.4

- fork: python
- ref: 4f18916c5c28321f363e
- machine: darwin-arm64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.472x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| docutils       | 1.74 sec                                               | 1.37 sec: 1.27x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.0 ms: 1.50x faster                                                  |
| sphinx         | 729 ms                                                 | 548 ms: 1.33x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.8 ms: 7.02x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.72x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.66x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.69x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.7 ms: 1.39x faster                                                  |
| async_generators              | 233 ms                                                 | 256 ms: 1.10x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.24x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 42.6 ms: 1.70x faster                                                  |
| nbody          | 92.5 ms                                                | 71.3 ms: 1.30x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 60.4 ms: 1.58x faster                                                  |
| regex_dna      | 175 ms                                                 | 147 ms: 1.19x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.18x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.32 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 127 us: 1.56x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 185 us: 1.54x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.5 ms: 1.29x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.07 ms: 1.17x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.6 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 70.4 ms: 1.06x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                                   |
| json_loads           | 16.6 us                                                | 17.8 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.7 ms: 1.05x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.6 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                  |
| mako            | 9.81 ms                                                | 7.28 ms: 1.35x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.7 ms: 1.32x faster                                                  |
| django_template | 24.4 ms                                                | 19.2 ms: 1.27x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.8 ms: 7.02x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 87.0 us: 3.75x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.72x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.4 ms: 3.50x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.66x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.04 ms: 2.45x faster                                                  |
| mdp                           | 1.65 sec                                               | 684 ms: 2.41x faster                                                   |
| go                            | 163 ms                                                 | 70.7 ms: 2.31x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.2 us: 2.15x faster                                                  |
| raytrace                      | 327 ms                                                 | 156 ms: 2.09x faster                                                   |
| logging_silent                | 117 ns                                                 | 57.9 ns: 2.02x faster                                                  |
| deepcopy                      | 276 us                                                 | 139 us: 1.99x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.94x faster                                                   |
| chaos                         | 67.7 ms                                                | 35.0 ms: 1.94x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 73.2 ms: 1.91x faster                                                  |
| richards_super                | 61.0 ms                                                | 33.1 ms: 1.84x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 39.6 ms: 1.83x faster                                                  |
| richards                      | 52.3 ms                                                | 29.3 ms: 1.78x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.0 us: 1.73x faster                                                  |
| float                         | 72.4 ms                                                | 42.6 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.69x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.75 ms: 1.67x faster                                                  |
| generators                    | 31.7 ms                                                | 19.1 ms: 1.66x faster                                                  |
| pyflate                       | 448 ms                                                 | 275 ms: 1.63x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 60.4 ms: 1.58x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 127 us: 1.56x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.50 us: 1.55x faster                                                  |
| pylint                        | 231 ms                                                 | 149 ms: 1.55x faster                                                   |
| logging_format                | 5.03 us                                                | 3.27 us: 1.54x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 185 us: 1.54x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.01 us: 1.53x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.4 ms: 1.52x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.0 ms: 1.50x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 49.1 ms: 1.49x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.17 ms: 1.47x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 70.0 ms: 1.47x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 66.3 ms: 1.44x faster                                                  |
| pycparser                     | 887 ms                                                 | 621 ms: 1.43x faster                                                   |
| pprint_pformat                | 1.33 sec                                               | 936 ms: 1.42x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 462 ms: 1.40x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                  |
| coroutines                    | 20.5 ms                                                | 14.7 ms: 1.39x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.3 ms: 1.37x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 68.3 ms: 1.36x faster                                                  |
| mako                          | 9.81 ms                                                | 7.28 ms: 1.35x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.51 sec: 1.33x faster                                                 |
| sphinx                        | 729 ms                                                 | 548 ms: 1.33x faster                                                   |
| 2to3                          | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| sympy_integrate               | 13.2 ms                                                | 9.99 ms: 1.32x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 26.7 ms: 1.32x faster                                                  |
| nbody                         | 92.5 ms                                                | 71.3 ms: 1.30x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 34.5 ms: 1.29x faster                                                  |
| sympy_str                     | 166 ms                                                 | 129 ms: 1.29x faster                                                   |
| django_template               | 24.4 ms                                                | 19.2 ms: 1.27x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.37 sec: 1.27x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 216 ms: 1.24x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.78 sec: 1.24x faster                                                 |
| fannkuch                      | 303 ms                                                 | 249 ms: 1.22x faster                                                   |
| nqueens                       | 63.8 ms                                                | 52.7 ms: 1.21x faster                                                  |
| regex_dna                     | 175 ms                                                 | 147 ms: 1.19x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 460 us: 1.18x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 191 ms: 1.18x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.18x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.07 ms: 1.17x faster                                                  |
| many_optionals                | 486 us                                                 | 418 us: 1.16x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 48.6 ms: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.2 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.17 ms: 1.08x faster                                                  |
| connected_components          | 318 ms                                                 | 300 ms: 1.06x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.4 ms: 1.06x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.7 ms: 1.05x faster                                                  |
| pathlib                       | 25.7 ms                                                | 24.6 ms: 1.05x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.04x faster                                                   |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.32 ms: 1.01x faster                                                  |
| shortest_path                 | 328 ms                                                 | 326 ms: 1.01x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.53 us: 1.03x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.07x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| async_generators              | 233 ms                                                 | 256 ms: 1.10x slower                                                   |
| coverage                      | 41.2 ms                                                | 45.7 ms: 1.11x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.08 ms: 1.14x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.6 ms: 1.14x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 64.5 ms: 1.15x slower                                                  |
| telco                         | 3.49 ms                                                | 4.53 ms: 1.30x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (20) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.472x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.13x