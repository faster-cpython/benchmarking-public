# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.155x faster
- HPT reliability: 98.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 233 ms: 1.16x slower                                                  |
| docutils       | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                |
| html5lib       | 43.5 ms                                                | 34.6 ms: 1.26x faster                                                 |
| sphinx         | 729 ms                                                 | 678 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.8 ms: 4.79x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.28x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 333 ms: 3.05x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 344 ms: 2.96x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.38x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 395 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 320 ms: 1.37x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.98x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.1 ms: 1.47x faster                                                 |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| nbody          | 92.5 ms                                                | 95.0 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_compile  | 95.6 ms                                                | 83.6 ms: 1.14x faster                                                 |
| regex_v8       | 19.1 ms                                                | 17.0 ms: 1.12x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 237 us: 1.20x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 167 us: 1.19x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                |
| xml_etree_iterparse  | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.01x slower                                                  |
| json_dumps           | 8.31 ms                                                | 8.41 ms: 1.01x slower                                                 |
| xml_etree_process    | 44.6 ms                                                | 49.8 ms: 1.12x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 72.1 ms: 1.34x slower                                                 |
| json_loads           | 16.6 us                                                | 24.6 us: 1.48x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 21.0 ms: 1.07x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 16.0 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 18.3 ms: 1.03x slower                                                 |
| mako            | 9.81 ms                                                | 11.0 ms: 1.12x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 39.4 ms: 1.12x slower                                                 |
| django_template | 24.4 ms                                                | 28.2 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.8 ms: 4.79x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.28x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 333 ms: 3.05x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 344 ms: 2.96x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.38x faster                                                  |
| subparsers                    | 39.8 ms                                                | 16.9 ms: 2.35x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 140 us: 2.34x faster                                                  |
| go                            | 163 ms                                                 | 84.3 ms: 1.94x faster                                                 |
| gc_traversal                  | 2.71 ms                                                | 1.42 ms: 1.91x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.70 ms: 1.85x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 395 ms: 1.70x faster                                                  |
| mdp                           | 1.65 sec                                               | 989 ms: 1.67x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 22.2 us: 1.57x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                  |
| float                         | 72.4 ms                                                | 49.1 ms: 1.47x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 96.6 ms: 1.45x faster                                                 |
| pyflate                       | 448 ms                                                 | 317 ms: 1.41x faster                                                  |
| raytrace                      | 327 ms                                                 | 235 ms: 1.39x faster                                                  |
| chaos                         | 67.7 ms                                                | 49.2 ms: 1.38x faster                                                 |
| create_gc_cycles              | 1.16 ms                                                | 861 us: 1.35x faster                                                  |
| generators                    | 31.7 ms                                                | 23.9 ms: 1.33x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 55.2 ms: 1.31x faster                                                 |
| richards_super                | 61.0 ms                                                | 46.7 ms: 1.30x faster                                                 |
| deepcopy                      | 276 us                                                 | 214 us: 1.29x faster                                                  |
| richards                      | 52.3 ms                                                | 40.7 ms: 1.28x faster                                                 |
| html5lib                      | 43.5 ms                                                | 34.6 ms: 1.26x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.97 ms: 1.26x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 28.7 ms: 1.24x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.64 sec: 1.23x faster                                                |
| pylint                        | 231 ms                                                 | 189 ms: 1.22x faster                                                  |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| pycparser                     | 887 ms                                                 | 736 ms: 1.21x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 237 us: 1.20x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 167 us: 1.19x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 83.6 ms: 1.14x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                                 |
| comprehensions                | 17.3 us                                                | 15.3 us: 1.13x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 17.0 ms: 1.12x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                |
| docutils                      | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                |
| xml_etree_iterparse           | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                 |
| sphinx                        | 729 ms                                                 | 678 ms: 1.08x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.20 ms: 1.06x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 90.2 ms: 1.06x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.36 us: 1.05x faster                                                 |
| logging_format                | 5.03 us                                                | 4.79 us: 1.05x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.7 ms: 1.04x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 70.7 ms: 1.04x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 100 ms: 1.02x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 12.9 ms: 1.02x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 2.29 us: 1.02x faster                                                 |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| xml_etree_parse               | 109 ms                                                 | 111 ms: 1.01x slower                                                  |
| json_dumps                    | 8.31 ms                                                | 8.41 ms: 1.01x slower                                                 |
| connected_components          | 318 ms                                                 | 322 ms: 1.01x slower                                                  |
| sympy_sum                     | 92.7 ms                                                | 93.9 ms: 1.01x slower                                                 |
| nbody                         | 92.5 ms                                                | 95.0 ms: 1.03x slower                                                 |
| genshi_text                   | 17.7 ms                                                | 18.3 ms: 1.03x slower                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.40 sec: 1.05x slower                                                |
| shortest_path                 | 328 ms                                                 | 346 ms: 1.05x slower                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.64 sec: 1.06x slower                                                |
| pprint_safe_repr              | 648 ms                                                 | 687 ms: 1.06x slower                                                  |
| python_startup                | 19.6 ms                                                | 21.0 ms: 1.07x slower                                                 |
| meteor_contest                | 77.8 ms                                                | 83.2 ms: 1.07x slower                                                 |
| sympy_str                     | 166 ms                                                 | 183 ms: 1.10x slower                                                  |
| xml_etree_process             | 44.6 ms                                                | 49.8 ms: 1.12x slower                                                 |
| mako                          | 9.81 ms                                                | 11.0 ms: 1.12x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 39.4 ms: 1.12x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.67 us: 1.13x slower                                                 |
| thrift                        | 562 us                                                 | 635 us: 1.13x slower                                                  |
| nqueens                       | 63.8 ms                                                | 72.5 ms: 1.14x slower                                                 |
| many_optionals                | 486 us                                                 | 557 us: 1.15x slower                                                  |
| 2to3                          | 201 ms                                                 | 233 ms: 1.16x slower                                                  |
| django_template               | 24.4 ms                                                | 28.2 ms: 1.16x slower                                                 |
| fannkuch                      | 303 ms                                                 | 354 ms: 1.17x slower                                                  |
| sympy_expand                  | 269 ms                                                 | 324 ms: 1.21x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 16.0 ms: 1.25x slower                                                 |
| scimark_fft                   | 225 ms                                                 | 287 ms: 1.27x slower                                                  |
| json                          | 3.10 ms                                                | 4.08 ms: 1.32x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.53 ms: 1.33x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 72.1 ms: 1.34x slower                                                 |
| async_generators              | 233 ms                                                 | 320 ms: 1.37x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 78.6 ms: 1.40x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 777 us: 1.43x slower                                                  |
| json_loads                    | 16.6 us                                                | 24.6 us: 1.48x slower                                                 |
| telco                         | 3.49 ms                                                | 6.11 ms: 1.75x slower                                                 |
| coverage                      | 41.2 ms                                                | 75.7 ms: 1.84x slower                                                 |
| logging_silent                | 117 ns                                                 | 444 ns: 3.79x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.13x faster                                                          |
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.155x faster

# HPT report

- Reliability score: 98.89% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.33x