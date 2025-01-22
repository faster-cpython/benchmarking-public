# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: darwin-arm64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.359x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 197 ms: 1.02x faster                                           |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.14x faster                                         |
| html5lib       | 43.5 ms                                                | 31.2 ms: 1.39x faster                                          |
| sphinx         | 729 ms                                                 | 582 ms: 1.25x faster                                           |
| Geometric mean | (ref)                                                  | 1.20x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.4 ms: 6.39x faster                                          |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.43x faster                                           |
| async_tree_eager_io           | 1.01 sec                                               | 377 ms: 2.69x faster                                           |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.68x faster                                           |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.45x faster                                           |
| async_tree_memoization        | 481 ms                                                 | 201 ms: 2.40x faster                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                           |
| coroutines                    | 20.5 ms                                                | 16.0 ms: 1.28x faster                                          |
| async_generators              | 233 ms                                                 | 250 ms: 1.07x slower                                           |
| Geometric mean                | (ref)                                                  | 2.09x faster                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 72.4 ms                                                | 48.6 ms: 1.49x faster                                          |
| nbody          | 92.5 ms                                                | 68.6 ms: 1.35x faster                                          |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.26x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.0 ms: 1.43x faster                                          |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                           |
| regex_v8       | 19.1 ms                                                | 16.8 ms: 1.14x faster                                          |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 197 us: 1.44x faster                                           |
| tomli_loads          | 1.72 sec                                               | 1.20 sec: 1.43x faster                                         |
| unpickle_pure_python | 198 us                                                 | 147 us: 1.35x faster                                           |
| json_dumps           | 8.31 ms                                                | 7.49 ms: 1.11x faster                                          |
| xml_etree_process    | 44.6 ms                                                | 41.1 ms: 1.09x faster                                          |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 74.5 ms                                                | 71.1 ms: 1.05x faster                                          |
| xml_etree_generate   | 53.9 ms                                                | 53.4 ms: 1.01x faster                                          |
| json_loads           | 16.6 us                                                | 16.5 us: 1.00x faster                                          |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.7 ms: 1.05x faster                                          |
| python_startup_no_site | 12.8 ms                                                | 13.9 ms: 1.08x slower                                          |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.19 ms: 1.36x faster                                          |
| genshi_xml      | 35.1 ms                                                | 28.8 ms: 1.22x faster                                          |
| genshi_text     | 17.7 ms                                                | 14.5 ms: 1.22x faster                                          |
| django_template | 24.4 ms                                                | 21.3 ms: 1.14x faster                                          |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                   |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.4 ms: 6.39x faster                                          |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.43x faster                                           |
| typing_runtime_protocols      | 326 us                                                 | 96.9 us: 3.36x faster                                          |
| subparsers                    | 39.8 ms                                                | 12.3 ms: 3.25x faster                                          |
| async_tree_eager_io           | 1.01 sec                                               | 377 ms: 2.69x faster                                           |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.68x faster                                           |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.45x faster                                           |
| async_tree_memoization        | 481 ms                                                 | 201 ms: 2.40x faster                                           |
| deepcopy_memo                 | 34.7 us                                                | 18.0 us: 1.93x faster                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                           |
| deepcopy                      | 276 us                                                 | 148 us: 1.86x faster                                           |
| go                            | 163 ms                                                 | 87.8 ms: 1.86x faster                                          |
| deltablue                     | 4.99 ms                                                | 2.70 ms: 1.85x faster                                          |
| chaos                         | 67.7 ms                                                | 39.4 ms: 1.72x faster                                          |
| scimark_sor                   | 140 ms                                                 | 85.6 ms: 1.63x faster                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                           |
| raytrace                      | 327 ms                                                 | 204 ms: 1.60x faster                                           |
| richards_super                | 61.0 ms                                                | 38.0 ms: 1.60x faster                                          |
| sqlglot_parse                 | 1.35 ms                                                | 845 us: 1.60x faster                                           |
| spectral_norm                 | 95.3 ms                                                | 60.7 ms: 1.57x faster                                          |
| sqlglot_transpile             | 1.56 ms                                                | 1.01 ms: 1.54x faster                                          |
| richards                      | 52.3 ms                                                | 34.2 ms: 1.53x faster                                          |
| logging_silent                | 117 ns                                                 | 77.7 ns: 1.51x faster                                          |
| pyflate                       | 448 ms                                                 | 300 ms: 1.49x faster                                           |
| float                         | 72.4 ms                                                | 48.6 ms: 1.49x faster                                          |
| deepcopy_reduce               | 2.32 us                                                | 1.57 us: 1.48x faster                                          |
| hexiom                        | 6.25 ms                                                | 4.25 ms: 1.47x faster                                          |
| scimark_monte_carlo           | 72.4 ms                                                | 49.8 ms: 1.45x faster                                          |
| pickle_pure_python            | 285 us                                                 | 197 us: 1.44x faster                                           |
| tomli_loads                   | 1.72 sec                                               | 1.20 sec: 1.43x faster                                         |
| pprint_pformat                | 1.33 sec                                               | 929 ms: 1.43x faster                                           |
| regex_compile                 | 95.6 ms                                                | 67.0 ms: 1.43x faster                                          |
| pylint                        | 231 ms                                                 | 163 ms: 1.42x faster                                           |
| scimark_lu                    | 103 ms                                                 | 72.5 ms: 1.41x faster                                          |
| generators                    | 31.7 ms                                                | 22.5 ms: 1.41x faster                                          |
| pprint_safe_repr              | 648 ms                                                 | 464 ms: 1.40x faster                                           |
| html5lib                      | 43.5 ms                                                | 31.2 ms: 1.39x faster                                          |
| logging_format                | 5.03 us                                                | 3.61 us: 1.39x faster                                          |
| crypto_pyaes                  | 73.3 ms                                                | 53.1 ms: 1.38x faster                                          |
| logging_simple                | 4.59 us                                                | 3.35 us: 1.37x faster                                          |
| mako                          | 9.81 ms                                                | 7.19 ms: 1.36x faster                                          |
| pycparser                     | 887 ms                                                 | 653 ms: 1.36x faster                                           |
| unpickle_pure_python          | 198 us                                                 | 147 us: 1.35x faster                                           |
| nbody                         | 92.5 ms                                                | 68.6 ms: 1.35x faster                                          |
| comprehensions                | 17.3 us                                                | 12.9 us: 1.35x faster                                          |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.74 ms: 1.34x faster                                          |
| k_core                        | 2.01 sec                                               | 1.51 sec: 1.33x faster                                         |
| scimark_fft                   | 225 ms                                                 | 173 ms: 1.30x faster                                           |
| dulwich_log                   | 35.6 ms                                                | 27.5 ms: 1.29x faster                                          |
| coroutines                    | 20.5 ms                                                | 16.0 ms: 1.28x faster                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.69 ms: 1.27x faster                                          |
| sphinx                        | 729 ms                                                 | 582 ms: 1.25x faster                                           |
| sympy_sum                     | 92.7 ms                                                | 74.3 ms: 1.25x faster                                          |
| sqlalchemy_declarative        | 75.7 ms                                                | 60.8 ms: 1.25x faster                                          |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                           |
| thrift                        | 562 us                                                 | 457 us: 1.23x faster                                           |
| fannkuch                      | 303 ms                                                 | 247 ms: 1.23x faster                                           |
| genshi_xml                    | 35.1 ms                                                | 28.8 ms: 1.22x faster                                          |
| genshi_text                   | 17.7 ms                                                | 14.5 ms: 1.22x faster                                          |
| sympy_str                     | 166 ms                                                 | 139 ms: 1.19x faster                                           |
| sympy_integrate               | 13.2 ms                                                | 11.1 ms: 1.18x faster                                          |
| bpe_tokeniser                 | 3.44 sec                                               | 2.95 sec: 1.16x faster                                         |
| sympy_expand                  | 269 ms                                                 | 235 ms: 1.14x faster                                           |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.14x faster                                         |
| django_template               | 24.4 ms                                                | 21.3 ms: 1.14x faster                                          |
| regex_v8                      | 19.1 ms                                                | 16.8 ms: 1.14x faster                                          |
| sqlglot_optimize              | 37.2 ms                                                | 33.1 ms: 1.12x faster                                          |
| bench_thread_pool             | 545 us                                                 | 486 us: 1.12x faster                                           |
| pathlib                       | 25.7 ms                                                | 23.1 ms: 1.12x faster                                          |
| json_dumps                    | 8.31 ms                                                | 7.49 ms: 1.11x faster                                          |
| nqueens                       | 63.8 ms                                                | 57.7 ms: 1.11x faster                                          |
| many_optionals                | 486 us                                                 | 444 us: 1.09x faster                                           |
| xml_etree_process             | 44.6 ms                                                | 41.1 ms: 1.09x faster                                          |
| meteor_contest                | 77.8 ms                                                | 71.7 ms: 1.08x faster                                          |
| mdp                           | 1.65 sec                                               | 1.52 sec: 1.08x faster                                         |
| json                          | 3.10 ms                                                | 2.87 ms: 1.08x faster                                          |
| connected_components          | 318 ms                                                 | 296 ms: 1.08x faster                                           |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                           |
| sqlglot_normalize             | 192 ms                                                 | 180 ms: 1.07x faster                                           |
| python_startup                | 19.6 ms                                                | 18.7 ms: 1.05x faster                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 71.1 ms: 1.05x faster                                          |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                          |
| 2to3                          | 201 ms                                                 | 197 ms: 1.02x faster                                           |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                           |
| shortest_path                 | 328 ms                                                 | 324 ms: 1.01x faster                                           |
| xml_etree_generate            | 53.9 ms                                                | 53.4 ms: 1.01x faster                                          |
| json_loads                    | 16.6 us                                                | 16.5 us: 1.00x faster                                          |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                           |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.04x slower                                          |
| async_generators              | 233 ms                                                 | 250 ms: 1.07x slower                                           |
| bench_mp_pool                 | 56.0 ms                                                | 60.2 ms: 1.07x slower                                          |
| python_startup_no_site        | 12.8 ms                                                | 13.9 ms: 1.08x slower                                          |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                          |
| coverage                      | 41.2 ms                                                | 46.0 ms: 1.12x slower                                          |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.15x slower                                          |
| telco                         | 3.49 ms                                                | 4.52 ms: 1.30x slower                                          |
| Geometric mean                | (ref)                                                  | 1.35x faster                                                   |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.359x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.13x