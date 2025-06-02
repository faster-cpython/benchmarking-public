# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.153x faster
- HPT reliability: 98.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 203 ms: 1.01x slower                                                  |
| docutils       | 1.74 sec                                               | 1.60 sec: 1.09x faster                                                |
| html5lib       | 43.5 ms                                                | 35.1 ms: 1.24x faster                                                 |
| sphinx         | 729 ms                                                 | 682 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.8 ms: 4.79x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.25x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 333 ms: 3.04x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 345 ms: 2.95x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 200 ms: 2.41x faster                                                  |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.37x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 392 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.1 ms: 1.14x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 313 ms: 1.34x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.98x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.3 ms: 1.47x faster                                                 |
| nbody          | 92.5 ms                                                | 92.7 ms: 1.00x slower                                                 |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_compile  | 95.6 ms                                                | 83.8 ms: 1.14x faster                                                 |
| regex_v8       | 19.1 ms                                                | 17.1 ms: 1.12x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 238 us: 1.20x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 169 us: 1.17x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                |
| xml_etree_iterparse  | 74.5 ms                                                | 69.2 ms: 1.08x faster                                                 |
| json_dumps           | 8.31 ms                                                | 8.38 ms: 1.01x slower                                                 |
| xml_etree_parse      | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| xml_etree_process    | 44.6 ms                                                | 50.0 ms: 1.12x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 72.5 ms: 1.34x slower                                                 |
| json_loads           | 16.6 us                                                | 24.4 us: 1.47x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.3 ms: 1.03x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.5 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 18.3 ms: 1.03x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                 |
| mako            | 9.81 ms                                                | 11.0 ms: 1.12x slower                                                 |
| django_template | 24.4 ms                                                | 28.2 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.8 ms: 4.79x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.25x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 333 ms: 3.04x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 345 ms: 2.95x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 200 ms: 2.41x faster                                                  |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.37x faster                                                  |
| subparsers                    | 39.8 ms                                                | 17.0 ms: 2.35x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 140 us: 2.33x faster                                                  |
| go                            | 163 ms                                                 | 85.0 ms: 1.92x faster                                                 |
| gc_traversal                  | 2.71 ms                                                | 1.43 ms: 1.89x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.74 ms: 1.82x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 392 ms: 1.71x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.00 sec: 1.64x faster                                                |
| deepcopy_memo                 | 34.7 us                                                | 22.5 us: 1.54x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                                  |
| float                         | 72.4 ms                                                | 49.3 ms: 1.47x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 97.0 ms: 1.44x faster                                                 |
| pyflate                       | 448 ms                                                 | 323 ms: 1.39x faster                                                  |
| raytrace                      | 327 ms                                                 | 236 ms: 1.38x faster                                                  |
| chaos                         | 67.7 ms                                                | 49.1 ms: 1.38x faster                                                 |
| create_gc_cycles              | 1.16 ms                                                | 855 us: 1.36x faster                                                  |
| generators                    | 31.7 ms                                                | 24.2 ms: 1.31x faster                                                 |
| richards_super                | 61.0 ms                                                | 46.9 ms: 1.30x faster                                                 |
| deepcopy                      | 276 us                                                 | 213 us: 1.30x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 56.2 ms: 1.29x faster                                                 |
| richards                      | 52.3 ms                                                | 41.0 ms: 1.28x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.96 ms: 1.26x faster                                                 |
| html5lib                      | 43.5 ms                                                | 35.1 ms: 1.24x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 28.9 ms: 1.23x faster                                                 |
| pylint                        | 231 ms                                                 | 189 ms: 1.22x faster                                                  |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| pycparser                     | 887 ms                                                 | 738 ms: 1.20x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 238 us: 1.20x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 169 us: 1.17x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.74 sec: 1.15x faster                                                |
| regex_compile                 | 95.6 ms                                                | 83.8 ms: 1.14x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.1 ms: 1.14x faster                                                 |
| comprehensions                | 17.3 us                                                | 15.4 us: 1.12x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 17.1 ms: 1.12x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                |
| docutils                      | 1.74 sec                                               | 1.60 sec: 1.09x faster                                                |
| xml_etree_iterparse           | 74.5 ms                                                | 69.2 ms: 1.08x faster                                                 |
| sphinx                        | 729 ms                                                 | 682 ms: 1.07x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 90.9 ms: 1.05x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.39 us: 1.05x faster                                                 |
| logging_format                | 5.03 us                                                | 4.82 us: 1.04x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 70.4 ms: 1.04x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 2.27 us: 1.02x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 13.0 ms: 1.01x faster                                                 |
| nbody                         | 92.5 ms                                                | 92.7 ms: 1.00x slower                                                 |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| scimark_lu                    | 103 ms                                                 | 103 ms: 1.01x slower                                                  |
| json_dumps                    | 8.31 ms                                                | 8.38 ms: 1.01x slower                                                 |
| 2to3                          | 201 ms                                                 | 203 ms: 1.01x slower                                                  |
| sympy_sum                     | 92.7 ms                                                | 94.1 ms: 1.02x slower                                                 |
| xml_etree_parse               | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| python_startup                | 19.6 ms                                                | 20.3 ms: 1.03x slower                                                 |
| genshi_text                   | 17.7 ms                                                | 18.3 ms: 1.03x slower                                                 |
| connected_components          | 318 ms                                                 | 334 ms: 1.05x slower                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.39 sec: 1.05x slower                                                |
| pprint_safe_repr              | 648 ms                                                 | 684 ms: 1.06x slower                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.66 sec: 1.06x slower                                                |
| meteor_contest                | 77.8 ms                                                | 83.0 ms: 1.07x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                 |
| sympy_str                     | 166 ms                                                 | 184 ms: 1.11x slower                                                  |
| shortest_path                 | 328 ms                                                 | 365 ms: 1.11x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.64 us: 1.11x slower                                                 |
| xml_etree_process             | 44.6 ms                                                | 50.0 ms: 1.12x slower                                                 |
| mako                          | 9.81 ms                                                | 11.0 ms: 1.12x slower                                                 |
| many_optionals                | 486 us                                                 | 549 us: 1.13x slower                                                  |
| thrift                        | 562 us                                                 | 636 us: 1.13x slower                                                  |
| nqueens                       | 63.8 ms                                                | 72.5 ms: 1.14x slower                                                 |
| django_template               | 24.4 ms                                                | 28.2 ms: 1.16x slower                                                 |
| fannkuch                      | 303 ms                                                 | 359 ms: 1.19x slower                                                  |
| sympy_expand                  | 269 ms                                                 | 325 ms: 1.21x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.5 ms: 1.21x slower                                                 |
| scimark_fft                   | 225 ms                                                 | 288 ms: 1.28x slower                                                  |
| json                          | 3.10 ms                                                | 4.05 ms: 1.30x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.54 ms: 1.33x slower                                                 |
| async_generators              | 233 ms                                                 | 313 ms: 1.34x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 72.5 ms: 1.34x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 78.4 ms: 1.40x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 774 us: 1.42x slower                                                  |
| json_loads                    | 16.6 us                                                | 24.4 us: 1.47x slower                                                 |
| telco                         | 3.49 ms                                                | 6.25 ms: 1.79x slower                                                 |
| coverage                      | 41.2 ms                                                | 76.0 ms: 1.84x slower                                                 |
| logging_silent                | 117 ns                                                 | 450 ns: 3.84x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.153x faster

# HPT report

- Reliability score: 98.43% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.33x