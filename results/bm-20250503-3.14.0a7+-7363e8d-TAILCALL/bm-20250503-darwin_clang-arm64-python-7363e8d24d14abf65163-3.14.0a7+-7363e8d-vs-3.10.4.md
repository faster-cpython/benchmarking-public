# Results vs. 3.10.4

- fork: python
- ref: 7363e8d24d14abf65163
- machine: darwin-arm64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.445x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 155 ms: 1.30x faster                                                   |
| docutils       | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.2 ms: 1.49x faster                                                  |
| sphinx         | 729 ms                                                 | 556 ms: 1.31x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.0 ms: 6.75x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 132 ms: 3.67x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 339 ms: 3.00x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.62x faster                                                   |
| async_tree_none               | 391 ms                                                 | 153 ms: 2.56x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 351 ms: 1.91x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.2 ms: 1.35x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                   |
| async_generators              | 233 ms                                                 | 279 ms: 1.19x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 43.8 ms: 1.65x faster                                                  |
| nbody          | 92.5 ms                                                | 73.4 ms: 1.26x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.7 ms: 1.55x faster                                                  |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.54x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 186 us: 1.53x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 35.2 ms: 1.27x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.37 ms: 1.13x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 49.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                                   |
| json_loads           | 16.6 us                                                | 18.5 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.6 ms: 1.00x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.9 ms: 1.37x faster                                                  |
| mako            | 9.81 ms                                                | 7.19 ms: 1.36x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 27.2 ms: 1.29x faster                                                  |
| django_template | 24.4 ms                                                | 19.7 ms: 1.24x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.0 ms: 6.75x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 132 ms: 3.67x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 90.0 us: 3.62x faster                                                  |
| subparsers                    | 39.8 ms                                                | 12.6 ms: 3.16x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 339 ms: 3.00x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.62x faster                                                   |
| async_tree_none               | 391 ms                                                 | 153 ms: 2.56x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.05 ms: 2.43x faster                                                  |
| mdp                           | 1.65 sec                                               | 701 ms: 2.35x faster                                                   |
| go                            | 163 ms                                                 | 71.1 ms: 2.30x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.6 us: 2.09x faster                                                  |
| raytrace                      | 327 ms                                                 | 160 ms: 2.04x faster                                                   |
| logging_silent                | 117 ns                                                 | 60.2 ns: 1.95x faster                                                  |
| deepcopy                      | 276 us                                                 | 145 us: 1.91x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 351 ms: 1.91x faster                                                   |
| chaos                         | 67.7 ms                                                | 35.5 ms: 1.91x faster                                                  |
| richards_super                | 61.0 ms                                                | 33.0 ms: 1.85x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 78.0 ms: 1.79x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 40.6 ms: 1.78x faster                                                  |
| richards                      | 52.3 ms                                                | 29.4 ms: 1.78x faster                                                  |
| generators                    | 31.7 ms                                                | 18.7 ms: 1.70x faster                                                  |
| float                         | 72.4 ms                                                | 43.8 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                   |
| comprehensions                | 17.3 us                                                | 10.5 us: 1.65x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.79 ms: 1.65x faster                                                  |
| pyflate                       | 448 ms                                                 | 276 ms: 1.62x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 61.7 ms: 1.55x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.54x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 186 us: 1.53x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.01 us: 1.53x faster                                                  |
| pylint                        | 231 ms                                                 | 152 ms: 1.52x faster                                                   |
| logging_format                | 5.03 us                                                | 3.32 us: 1.52x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.7 ms: 1.50x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.2 ms: 1.49x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.56 us: 1.49x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 49.9 ms: 1.47x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 70.4 ms: 1.46x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.28 ms: 1.44x faster                                                  |
| pycparser                     | 887 ms                                                 | 626 ms: 1.42x faster                                                   |
| pprint_pformat                | 1.33 sec                                               | 940 ms: 1.41x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 68.7 ms: 1.39x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 471 ms: 1.38x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.9 ms: 1.37x faster                                                  |
| mako                          | 9.81 ms                                                | 7.19 ms: 1.36x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.2 ms: 1.35x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 56.3 ms: 1.34x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 70.2 ms: 1.32x faster                                                  |
| sphinx                        | 729 ms                                                 | 556 ms: 1.31x faster                                                   |
| 2to3                          | 201 ms                                                 | 155 ms: 1.30x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 27.2 ms: 1.29x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.2 ms: 1.29x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 35.2 ms: 1.27x faster                                                  |
| nbody                         | 92.5 ms                                                | 73.4 ms: 1.26x faster                                                  |
| sympy_str                     | 166 ms                                                 | 132 ms: 1.26x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                 |
| django_template               | 24.4 ms                                                | 19.7 ms: 1.24x faster                                                  |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 223 ms: 1.21x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.91 sec: 1.18x faster                                                 |
| fannkuch                      | 303 ms                                                 | 257 ms: 1.18x faster                                                   |
| nqueens                       | 63.8 ms                                                | 54.4 ms: 1.17x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 471 us: 1.16x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.37 ms: 1.13x faster                                                  |
| many_optionals                | 486 us                                                 | 436 us: 1.11x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 204 ms: 1.10x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.5 ms: 1.10x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 71.2 ms: 1.09x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 49.6 ms: 1.09x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                  |
| connected_components          | 318 ms                                                 | 302 ms: 1.06x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.32 ms: 1.03x faster                                                  |
| json                          | 3.10 ms                                                | 3.07 ms: 1.01x faster                                                  |
| shortest_path                 | 328 ms                                                 | 327 ms: 1.00x faster                                                   |
| python_startup                | 19.6 ms                                                | 19.6 ms: 1.00x faster                                                  |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.58 us: 1.07x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| json_loads                    | 16.6 us                                                | 18.5 us: 1.11x slower                                                  |
| coverage                      | 41.2 ms                                                | 46.1 ms: 1.12x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.09 ms: 1.14x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.7 ms: 1.15x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 65.8 ms: 1.17x slower                                                  |
| async_generators              | 233 ms                                                 | 279 ms: 1.19x slower                                                   |
| telco                         | 3.49 ms                                                | 4.69 ms: 1.34x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.44x faster                                                           |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (20) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.445x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.14x