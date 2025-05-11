# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.189x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 210 ms: 1.04x slower                                                  |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.14x faster                                                |
| html5lib       | 43.5 ms                                                | 36.0 ms: 1.21x faster                                                 |
| sphinx         | 729 ms                                                 | 637 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 86.8 ms: 4.51x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 157 ms: 3.08x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.93x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 358 ms: 2.84x faster                                                  |
| async_tree_none               | 391 ms                                                 | 171 ms: 2.29x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 211 ms: 2.28x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 377 ms: 1.77x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 421 ms: 1.59x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.08x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 293 ms: 1.26x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.94x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 55.2 ms: 1.31x faster                                                 |
| nbody          | 92.5 ms                                                | 95.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 135 ms: 1.29x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.2 ms: 1.26x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.12 ms: 1.10x faster                                                 |
| regex_compile  | 95.6 ms                                                | 95.9 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.5 ms                                                | 67.4 ms: 1.10x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 99.1 ms: 1.10x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.63 sec: 1.06x faster                                                |
| unpickle_pure_python | 198 us                                                 | 190 us: 1.04x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 274 us: 1.04x faster                                                  |
| json_dumps           | 8.31 ms                                                | 8.32 ms: 1.00x slower                                                 |
| xml_etree_process    | 44.6 ms                                                | 48.4 ms: 1.09x slower                                                 |
| json_loads           | 16.6 us                                                | 19.2 us: 1.16x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 63.7 ms: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.5 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 35.1 ms                                                | 39.3 ms: 1.12x slower                                                 |
| genshi_text     | 17.7 ms                                                | 19.9 ms: 1.12x slower                                                 |
| django_template | 24.4 ms                                                | 28.0 ms: 1.15x slower                                                 |
| mako            | 9.81 ms                                                | 11.6 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 86.8 ms: 4.51x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 157 ms: 3.08x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.93x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 358 ms: 2.84x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.2 ms: 2.62x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 125 us: 2.60x faster                                                  |
| async_tree_none               | 391 ms                                                 | 171 ms: 2.29x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 211 ms: 2.28x faster                                                  |
| gc_traversal                  | 2.71 ms                                                | 1.50 ms: 1.80x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 377 ms: 1.77x faster                                                  |
| mdp                           | 1.65 sec                                               | 930 ms: 1.77x faster                                                  |
| deltablue                     | 4.99 ms                                                | 3.03 ms: 1.65x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 421 ms: 1.59x faster                                                  |
| go                            | 163 ms                                                 | 111 ms: 1.47x faster                                                  |
| raytrace                      | 327 ms                                                 | 228 ms: 1.43x faster                                                  |
| create_gc_cycles              | 1.16 ms                                                | 830 us: 1.40x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 100 ms: 1.40x faster                                                  |
| deepcopy                      | 276 us                                                 | 202 us: 1.36x faster                                                  |
| chaos                         | 67.7 ms                                                | 50.4 ms: 1.34x faster                                                 |
| float                         | 72.4 ms                                                | 55.2 ms: 1.31x faster                                                 |
| richards_super                | 61.0 ms                                                | 46.6 ms: 1.31x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 26.7 us: 1.30x faster                                                 |
| regex_dna                     | 175 ms                                                 | 135 ms: 1.29x faster                                                  |
| pylint                        | 231 ms                                                 | 179 ms: 1.29x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 28.2 ms: 1.26x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.2 ms: 1.26x faster                                                 |
| richards                      | 52.3 ms                                                | 41.6 ms: 1.26x faster                                                 |
| pyflate                       | 448 ms                                                 | 363 ms: 1.23x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.64 sec: 1.23x faster                                                |
| html5lib                      | 43.5 ms                                                | 36.0 ms: 1.21x faster                                                 |
| pycparser                     | 887 ms                                                 | 736 ms: 1.21x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 60.3 ms: 1.20x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 80.6 ms: 1.18x faster                                                 |
| comprehensions                | 17.3 us                                                | 15.0 us: 1.15x faster                                                 |
| sphinx                        | 729 ms                                                 | 637 ms: 1.14x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.14x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 66.2 ms: 1.11x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 67.4 ms: 1.10x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 99.1 ms: 1.10x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.12 ms: 1.10x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.08x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 2.14 us: 1.08x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.77 ms: 1.08x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.0 ms: 1.07x faster                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.38 us: 1.07x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 12.4 ms: 1.06x faster                                                 |
| thrift                        | 562 us                                                 | 532 us: 1.06x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.63 sec: 1.06x faster                                                |
| scimark_lu                    | 103 ms                                                 | 97.8 ms: 1.05x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.27 sec: 1.05x faster                                                |
| bpe_tokeniser                 | 3.44 sec                                               | 3.28 sec: 1.05x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 88.7 ms: 1.04x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 190 us: 1.04x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 625 ms: 1.04x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 274 us: 1.04x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 8.32 ms: 1.00x slower                                                 |
| regex_compile                 | 95.6 ms                                                | 95.9 ms: 1.00x slower                                                 |
| logging_format                | 5.03 us                                                | 5.06 us: 1.01x slower                                                 |
| generators                    | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                 |
| logging_simple                | 4.59 us                                                | 4.68 us: 1.02x slower                                                 |
| json                          | 3.10 ms                                                | 3.18 ms: 1.02x slower                                                 |
| nbody                         | 92.5 ms                                                | 95.5 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.55 ms: 1.04x slower                                                 |
| connected_components          | 318 ms                                                 | 331 ms: 1.04x slower                                                  |
| sympy_str                     | 166 ms                                                 | 173 ms: 1.04x slower                                                  |
| 2to3                          | 201 ms                                                 | 210 ms: 1.04x slower                                                  |
| fannkuch                      | 303 ms                                                 | 317 ms: 1.05x slower                                                  |
| many_optionals                | 486 us                                                 | 517 us: 1.06x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 83.6 ms: 1.07x slower                                                 |
| xml_etree_process             | 44.6 ms                                                | 48.4 ms: 1.09x slower                                                 |
| shortest_path                 | 328 ms                                                 | 357 ms: 1.09x slower                                                  |
| sympy_expand                  | 269 ms                                                 | 297 ms: 1.10x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 39.3 ms: 1.12x slower                                                 |
| genshi_text                   | 17.7 ms                                                | 19.9 ms: 1.12x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 14.5 ms: 1.14x slower                                                 |
| django_template               | 24.4 ms                                                | 28.0 ms: 1.15x slower                                                 |
| json_loads                    | 16.6 us                                                | 19.2 us: 1.16x slower                                                 |
| nqueens                       | 63.8 ms                                                | 74.0 ms: 1.16x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 63.7 ms: 1.18x slower                                                 |
| mako                          | 9.81 ms                                                | 11.6 ms: 1.19x slower                                                 |
| async_generators              | 233 ms                                                 | 293 ms: 1.26x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 73.3 ms: 1.31x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 760 us: 1.39x slower                                                  |
| telco                         | 3.49 ms                                                | 5.32 ms: 1.52x slower                                                 |
| coverage                      | 41.2 ms                                                | 66.9 ms: 1.62x slower                                                 |
| logging_silent                | 117 ns                                                 | 377 ns: 3.22x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (2): scimark_fft, pidigits
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.189x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.34x