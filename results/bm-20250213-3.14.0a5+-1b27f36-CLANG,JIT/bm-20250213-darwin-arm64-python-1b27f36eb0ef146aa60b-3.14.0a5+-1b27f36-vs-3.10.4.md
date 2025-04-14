# Results vs. 3.10.4

- fork: python
- ref: 1b27f36eb0ef146aa60b
- machine: darwin-arm64
- commit hash: 1b27f36
- commit date: 2025-02-13
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 179 ms: 1.13x faster                                                   |
| docutils       | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.1 ms: 1.49x faster                                                  |
| sphinx         | 729 ms                                                 | 547 ms: 1.33x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.2 ms: 6.41x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 345 ms: 2.95x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 349 ms: 2.91x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 185 ms: 2.60x faster                                                   |
| async_tree_none               | 391 ms                                                 | 154 ms: 2.54x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 353 ms: 1.90x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 407 ms: 1.64x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                  |
| async_generators              | 233 ms                                                 | 269 ms: 1.15x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.16x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.2 ms: 1.64x faster                                                  |
| nbody          | 92.5 ms                                                | 63.6 ms: 1.46x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 63.8 ms: 1.50x faster                                                  |
| regex_dna      | 175 ms                                                 | 147 ms: 1.19x faster                                                   |
| regex_v8       | 19.1 ms                                                | 18.0 ms: 1.06x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 128 us: 1.54x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 186 us: 1.53x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.16 sec: 1.48x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 33.2 ms: 1.34x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.12 ms: 1.17x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 97.1 ms: 1.13x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.1 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                  |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.7 ms: 1.18x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 12.0 ms: 1.07x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.47 ms: 1.52x faster                                                  |
| genshi_text     | 17.7 ms                                                | 12.7 ms: 1.39x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 27.4 ms: 1.28x faster                                                  |
| django_template | 24.4 ms                                                | 19.0 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.2 ms: 6.41x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 89.4 us: 3.65x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.5 ms: 3.48x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 345 ms: 2.95x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 349 ms: 2.91x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 185 ms: 2.60x faster                                                   |
| async_tree_none               | 391 ms                                                 | 154 ms: 2.54x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.07 ms: 2.41x faster                                                  |
| go                            | 163 ms                                                 | 72.8 ms: 2.25x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.7 us: 2.08x faster                                                  |
| raytrace                      | 327 ms                                                 | 163 ms: 2.01x faster                                                   |
| logging_silent                | 117 ns                                                 | 58.4 ns: 2.01x faster                                                  |
| deepcopy                      | 276 us                                                 | 139 us: 1.98x faster                                                   |
| richards_super                | 61.0 ms                                                | 31.3 ms: 1.95x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 353 ms: 1.90x faster                                                   |
| chaos                         | 67.7 ms                                                | 35.8 ms: 1.89x faster                                                  |
| richards                      | 52.3 ms                                                | 27.7 ms: 1.89x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 74.3 ms: 1.88x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 39.5 ms: 1.83x faster                                                  |
| generators                    | 31.7 ms                                                | 17.4 ms: 1.83x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 814 us: 1.66x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 407 ms: 1.64x faster                                                   |
| float                         | 72.4 ms                                                | 44.2 ms: 1.64x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 968 us: 1.61x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.91 ms: 1.60x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.93 us: 1.57x faster                                                  |
| logging_format                | 5.03 us                                                | 3.21 us: 1.57x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.49 us: 1.56x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 128 us: 1.54x faster                                                   |
| pylint                        | 231 ms                                                 | 151 ms: 1.53x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 186 us: 1.53x faster                                                   |
| mako                          | 9.81 ms                                                | 6.47 ms: 1.52x faster                                                  |
| pyflate                       | 448 ms                                                 | 295 ms: 1.52x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 63.8 ms: 1.50x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.6 us: 1.50x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.1 ms: 1.49x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.16 sec: 1.48x faster                                                 |
| nbody                         | 92.5 ms                                                | 63.6 ms: 1.46x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 70.9 ms: 1.45x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.37 ms: 1.42x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 51.5 ms: 1.42x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 68.1 ms: 1.40x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 12.7 ms: 1.39x faster                                                  |
| thrift                        | 562 us                                                 | 410 us: 1.37x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.5 ms: 1.36x faster                                                  |
| pycparser                     | 887 ms                                                 | 656 ms: 1.35x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 33.2 ms: 1.34x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 993 ms: 1.34x faster                                                   |
| sphinx                        | 729 ms                                                 | 547 ms: 1.33x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 487 ms: 1.33x faster                                                   |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 70.3 ms: 1.32x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 27.0 ms: 1.32x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 27.4 ms: 1.28x faster                                                  |
| django_template               | 24.4 ms                                                | 19.0 ms: 1.28x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.3 ms: 1.27x faster                                                  |
| sympy_str                     | 166 ms                                                 | 132 ms: 1.26x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 181 ms: 1.24x faster                                                   |
| sympy_expand                  | 269 ms                                                 | 222 ms: 1.21x faster                                                   |
| nqueens                       | 63.8 ms                                                | 53.0 ms: 1.21x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 31.0 ms: 1.20x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.89 sec: 1.19x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 459 us: 1.19x faster                                                   |
| regex_dna                     | 175 ms                                                 | 147 ms: 1.19x faster                                                   |
| python_startup                | 19.6 ms                                                | 16.7 ms: 1.18x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.12 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.94 ms: 1.16x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.43 sec: 1.15x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.4 ms: 1.15x faster                                                  |
| sqlglot_normalize             | 192 ms                                                 | 168 ms: 1.14x faster                                                   |
| many_optionals                | 486 us                                                 | 430 us: 1.13x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 97.1 ms: 1.13x faster                                                  |
| 2to3                          | 201 ms                                                 | 179 ms: 1.13x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 48.1 ms: 1.12x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                  |
| fannkuch                      | 303 ms                                                 | 284 ms: 1.07x faster                                                   |
| python_startup_no_site        | 12.8 ms                                                | 12.0 ms: 1.07x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 18.0 ms: 1.06x faster                                                  |
| connected_components          | 318 ms                                                 | 300 ms: 1.06x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 74.6 ms: 1.04x faster                                                  |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 770 ms: 1.03x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 58.0 ms: 1.04x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.53 us: 1.04x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| coverage                      | 41.2 ms                                                | 44.8 ms: 1.09x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.09 ms: 1.14x slower                                                  |
| async_generators              | 233 ms                                                 | 269 ms: 1.15x slower                                                   |
| telco                         | 3.49 ms                                                | 4.47 ms: 1.28x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.43x faster                                                           |

Benchmark hidden because not significant (2): shortest_path, asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250213-3.14.0a5+-1b27f36-CLANG,JIT/bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.14x