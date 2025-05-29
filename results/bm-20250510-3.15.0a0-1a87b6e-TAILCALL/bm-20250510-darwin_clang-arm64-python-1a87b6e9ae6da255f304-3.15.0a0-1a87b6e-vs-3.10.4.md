# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 158 ms: 1.28x faster                                                  |
| docutils       | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                |
| html5lib       | 43.5 ms                                                | 29.5 ms: 1.48x faster                                                 |
| sphinx         | 729 ms                                                 | 560 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 57.2 ms: 6.85x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.63x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 336 ms: 3.02x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 341 ms: 2.98x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 179 ms: 2.68x faster                                                  |
| async_tree_none               | 391 ms                                                 | 151 ms: 2.60x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 350 ms: 1.91x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 406 ms: 1.65x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                 |
| async_generators              | 233 ms                                                 | 267 ms: 1.14x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.1 ms: 1.64x faster                                                 |
| nbody          | 92.5 ms                                                | 73.5 ms: 1.26x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.9 ms: 1.54x faster                                                 |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.21 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 130 us: 1.53x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 188 us: 1.52x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 39.3 ms: 1.13x faster                                                 |
| json_dumps           | 8.31 ms                                                | 7.34 ms: 1.13x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 72.6 ms: 1.02x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 55.5 ms: 1.03x slower                                                 |
| json_loads           | 16.6 us                                                | 18.3 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.6 ms: 1.12x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.9 ms: 1.37x faster                                                 |
| mako            | 9.81 ms                                                | 7.25 ms: 1.35x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 27.1 ms: 1.29x faster                                                 |
| django_template | 24.4 ms                                                | 19.6 ms: 1.24x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 57.2 ms: 6.85x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.63x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 91.0 us: 3.58x faster                                                 |
| subparsers                    | 39.8 ms                                                | 12.6 ms: 3.15x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 336 ms: 3.02x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 341 ms: 2.98x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 179 ms: 2.68x faster                                                  |
| async_tree_none               | 391 ms                                                 | 151 ms: 2.60x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.05 ms: 2.44x faster                                                 |
| mdp                           | 1.65 sec                                               | 706 ms: 2.34x faster                                                  |
| go                            | 163 ms                                                 | 71.1 ms: 2.30x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 16.4 us: 2.12x faster                                                 |
| raytrace                      | 327 ms                                                 | 168 ms: 1.94x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 350 ms: 1.91x faster                                                  |
| chaos                         | 67.7 ms                                                | 35.6 ms: 1.90x faster                                                 |
| deepcopy                      | 276 us                                                 | 145 us: 1.90x faster                                                  |
| richards_super                | 61.0 ms                                                | 33.2 ms: 1.84x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 77.7 ms: 1.80x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 40.5 ms: 1.79x faster                                                 |
| richards                      | 52.3 ms                                                | 29.5 ms: 1.78x faster                                                 |
| generators                    | 31.7 ms                                                | 18.9 ms: 1.68x faster                                                 |
| hexiom                        | 6.25 ms                                                | 3.77 ms: 1.65x faster                                                 |
| comprehensions                | 17.3 us                                                | 10.5 us: 1.65x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 406 ms: 1.65x faster                                                  |
| float                         | 72.4 ms                                                | 44.1 ms: 1.64x faster                                                 |
| pyflate                       | 448 ms                                                 | 277 ms: 1.62x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 61.9 ms: 1.54x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 130 us: 1.53x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 188 us: 1.52x faster                                                  |
| pylint                        | 231 ms                                                 | 152 ms: 1.51x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.8 ms: 1.49x faster                                                 |
| html5lib                      | 43.5 ms                                                | 29.5 ms: 1.48x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.8 ms: 1.47x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.58 us: 1.47x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 69.7 ms: 1.47x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 915 ms: 1.45x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 448 ms: 1.45x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                |
| pycparser                     | 887 ms                                                 | 630 ms: 1.41x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.26 us: 1.41x faster                                                 |
| logging_format                | 5.03 us                                                | 3.59 us: 1.40x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 68.9 ms: 1.38x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 12.9 ms: 1.37x faster                                                 |
| mako                          | 9.81 ms                                                | 7.25 ms: 1.35x faster                                                 |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 69.7 ms: 1.33x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                |
| sphinx                        | 729 ms                                                 | 560 ms: 1.30x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.2 ms: 1.30x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 27.1 ms: 1.29x faster                                                 |
| 2to3                          | 201 ms                                                 | 158 ms: 1.28x faster                                                  |
| sympy_str                     | 166 ms                                                 | 131 ms: 1.26x faster                                                  |
| nbody                         | 92.5 ms                                                | 73.5 ms: 1.26x faster                                                 |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                  |
| django_template               | 24.4 ms                                                | 19.6 ms: 1.24x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                |
| regex_v8                      | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 222 ms: 1.21x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.89 sec: 1.19x faster                                                |
| fannkuch                      | 303 ms                                                 | 255 ms: 1.18x faster                                                  |
| nqueens                       | 63.8 ms                                                | 54.5 ms: 1.17x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 473 us: 1.15x faster                                                  |
| pathlib                       | 25.7 ms                                                | 22.5 ms: 1.14x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 39.3 ms: 1.13x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.34 ms: 1.13x faster                                                 |
| python_startup                | 19.6 ms                                                | 17.6 ms: 1.12x faster                                                 |
| many_optionals                | 486 us                                                 | 440 us: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.6 ms: 1.10x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 205 ms: 1.10x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.21 ms: 1.06x faster                                                 |
| connected_components          | 318 ms                                                 | 302 ms: 1.05x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 72.6 ms: 1.02x faster                                                 |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.37 ms: 1.02x faster                                                 |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| dask                          | 789 ms                                                 | 802 ms: 1.02x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 55.5 ms: 1.03x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.56 us: 1.06x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.3 us: 1.10x slower                                                 |
| async_generators              | 233 ms                                                 | 267 ms: 1.14x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.34 ms: 1.15x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.22 ms: 1.19x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 68.9 ms: 1.23x slower                                                 |
| telco                         | 3.49 ms                                                | 4.51 ms: 1.29x slower                                                 |
| logging_silent                | 117 ns                                                 | 302 ns: 2.58x slower                                                  |
| coverage                      | 41.2 ms                                                | 258 ms: 6.26x slower                                                  |
| thrift                        | 562 us                                                 | 43.1 ms: 76.58x slower                                                |
| Geometric mean                | (ref)                                                  | 1.31x faster                                                          |

Benchmark hidden because not significant (2): shortest_path, asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.335x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.17x