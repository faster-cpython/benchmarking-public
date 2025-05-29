# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.473x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| docutils       | 1.74 sec                                               | 1.42 sec: 1.22x faster                                                 |
| html5lib       | 43.5 ms                                                | 28.7 ms: 1.52x faster                                                  |
| sphinx         | 729 ms                                                 | 538 ms: 1.35x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.2 ms: 6.74x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 134 ms: 3.60x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 338 ms: 3.01x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 183 ms: 2.63x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 348 ms: 1.92x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 402 ms: 1.66x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                  |
| async_generators              | 233 ms                                                 | 248 ms: 1.06x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 43.6 ms: 1.66x faster                                                  |
| nbody          | 92.5 ms                                                | 61.9 ms: 1.50x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.9 ms: 1.54x faster                                                  |
| regex_dna      | 175 ms                                                 | 146 ms: 1.20x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.8 ms: 1.07x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 124 us: 1.60x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 181 us: 1.57x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.15 sec: 1.50x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.1 ms: 1.31x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.09 ms: 1.17x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.3 ms: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 99.8 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                  |
| json_loads           | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.3 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.4 ms: 1.43x faster                                                  |
| mako            | 9.81 ms                                                | 6.92 ms: 1.42x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.2 ms: 1.34x faster                                                  |
| django_template | 24.4 ms                                                | 19.0 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.2 ms: 6.74x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 87.1 us: 3.74x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 134 ms: 3.60x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.3 ms: 3.54x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 334 ms: 3.04x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 338 ms: 3.01x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 183 ms: 2.63x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.02 ms: 2.47x faster                                                  |
| go                            | 163 ms                                                 | 70.5 ms: 2.32x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.2 us: 2.14x faster                                                  |
| raytrace                      | 327 ms                                                 | 155 ms: 2.11x faster                                                   |
| logging_silent                | 117 ns                                                 | 57.9 ns: 2.02x faster                                                  |
| deepcopy                      | 276 us                                                 | 139 us: 1.99x faster                                                   |
| sqlglot_parse                 | 1.35 ms                                                | 681 us: 1.98x faster                                                   |
| richards_super                | 61.0 ms                                                | 31.0 ms: 1.97x faster                                                  |
| chaos                         | 67.7 ms                                                | 35.0 ms: 1.93x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 348 ms: 1.92x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 73.5 ms: 1.90x faster                                                  |
| richards                      | 52.3 ms                                                | 27.5 ms: 1.90x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 826 us: 1.89x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 38.6 ms: 1.88x faster                                                  |
| generators                    | 31.7 ms                                                | 17.1 ms: 1.85x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 402 ms: 1.66x faster                                                   |
| float                         | 72.4 ms                                                | 43.6 ms: 1.66x faster                                                  |
| pyflate                       | 448 ms                                                 | 271 ms: 1.65x faster                                                   |
| comprehensions                | 17.3 us                                                | 10.5 us: 1.64x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.81 ms: 1.64x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 58.2 ms: 1.64x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 124 us: 1.60x faster                                                   |
| logging_simple                | 4.59 us                                                | 2.89 us: 1.59x faster                                                  |
| logging_format                | 5.03 us                                                | 3.19 us: 1.58x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 181 us: 1.57x faster                                                   |
| pylint                        | 231 ms                                                 | 147 ms: 1.57x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 47.1 ms: 1.56x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 65.9 ms: 1.56x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.50 us: 1.55x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 61.9 ms: 1.54x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 874 ms: 1.52x faster                                                   |
| html5lib                      | 43.5 ms                                                | 28.7 ms: 1.52x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 431 ms: 1.50x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.15 sec: 1.50x faster                                                 |
| nbody                         | 92.5 ms                                                | 61.9 ms: 1.50x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.13 ms: 1.48x faster                                                  |
| pycparser                     | 887 ms                                                 | 616 ms: 1.44x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.4 ms: 1.43x faster                                                  |
| mako                          | 9.81 ms                                                | 6.92 ms: 1.42x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 54.5 ms: 1.39x faster                                                  |
| thrift                        | 562 us                                                 | 408 us: 1.38x faster                                                   |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.36x faster                                                 |
| sphinx                        | 729 ms                                                 | 538 ms: 1.35x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 68.4 ms: 1.35x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.4 ms: 1.35x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 26.2 ms: 1.34x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 168 ms: 1.34x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 34.1 ms: 1.31x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.1 ms: 1.30x faster                                                  |
| sympy_str                     | 166 ms                                                 | 128 ms: 1.30x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.64 ms: 1.29x faster                                                  |
| django_template               | 24.4 ms                                                | 19.0 ms: 1.28x faster                                                  |
| nqueens                       | 63.8 ms                                                | 50.5 ms: 1.26x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 215 ms: 1.25x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.75 sec: 1.25x faster                                                 |
| sqlglot_optimize              | 37.2 ms                                                | 29.8 ms: 1.25x faster                                                  |
| fannkuch                      | 303 ms                                                 | 246 ms: 1.23x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.42 sec: 1.22x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 454 us: 1.20x faster                                                   |
| regex_dna                     | 175 ms                                                 | 146 ms: 1.20x faster                                                   |
| many_optionals                | 486 us                                                 | 411 us: 1.18x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.09 ms: 1.17x faster                                                  |
| sqlglot_normalize             | 192 ms                                                 | 164 ms: 1.17x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.43 sec: 1.15x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.5 ms: 1.15x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 68.9 ms: 1.13x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.3 ms: 1.12x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 99.8 ms: 1.10x faster                                                  |
| 2to3                          | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| connected_components          | 318 ms                                                 | 295 ms: 1.08x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.8 ms: 1.07x faster                                                  |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| python_startup                | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| shortest_path                 | 328 ms                                                 | 323 ms: 1.02x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.50 us: 1.01x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.4 ms: 1.06x slower                                                  |
| async_generators              | 233 ms                                                 | 248 ms: 1.06x slower                                                   |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.4 ms: 1.10x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.3 ms: 1.12x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.08 ms: 1.14x slower                                                  |
| telco                         | 3.49 ms                                                | 4.44 ms: 1.27x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.473x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.12x