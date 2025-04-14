# Results vs. 3.10.4

- fork: nascheme
- ref: pgo_benchmark_task
- machine: darwin-arm64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.444x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                   |
| docutils       | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                 |
| html5lib       | 43.5 ms                                                | 28.2 ms: 1.54x faster                                                  |
| sphinx         | 729 ms                                                 | 577 ms: 1.26x faster                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.4 ms: 7.08x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 132 ms: 3.66x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 345 ms: 2.94x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 353 ms: 2.88x faster                                                   |
| async_tree_none               | 391 ms                                                 | 145 ms: 2.70x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 180 ms: 2.68x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.68x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.4 ms: 1.43x faster                                                  |
| async_generators              | 233 ms                                                 | 253 ms: 1.09x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 42.8 ms: 1.69x faster                                                  |
| nbody          | 92.5 ms                                                | 66.9 ms: 1.38x faster                                                  |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 64.0 ms: 1.49x faster                                                  |
| regex_dna      | 175 ms                                                 | 127 ms: 1.37x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.5 ms: 1.09x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 185 us: 1.54x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 35.8 ms: 1.25x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.05 ms: 1.18x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 93.7 ms: 1.17x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 50.6 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 71.2 ms: 1.05x faster                                                  |
| json_loads           | 16.6 us                                                | 17.3 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.6 ms: 1.06x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.97 ms: 1.41x faster                                                  |
| genshi_text     | 17.7 ms                                                | 13.3 ms: 1.34x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 27.8 ms: 1.26x faster                                                  |
| django_template | 24.4 ms                                                | 20.4 ms: 1.19x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.4 ms: 7.08x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 83.6 us: 3.90x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 132 ms: 3.66x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.9 ms: 3.35x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 345 ms: 2.94x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 353 ms: 2.88x faster                                                   |
| async_tree_none               | 391 ms                                                 | 145 ms: 2.70x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 180 ms: 2.68x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.04 ms: 2.44x faster                                                  |
| go                            | 163 ms                                                 | 70.3 ms: 2.33x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.7 us: 2.08x faster                                                  |
| raytrace                      | 327 ms                                                 | 159 ms: 2.05x faster                                                   |
| logging_silent                | 117 ns                                                 | 59.2 ns: 1.98x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 71.8 ms: 1.95x faster                                                  |
| chaos                         | 67.7 ms                                                | 34.8 ms: 1.94x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.94x faster                                                   |
| deepcopy                      | 276 us                                                 | 143 us: 1.93x faster                                                   |
| sqlglot_parse                 | 1.35 ms                                                | 723 us: 1.87x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 38.8 ms: 1.86x faster                                                  |
| richards_super                | 61.0 ms                                                | 32.7 ms: 1.86x faster                                                  |
| richards                      | 52.3 ms                                                | 29.3 ms: 1.79x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 882 us: 1.77x faster                                                   |
| comprehensions                | 17.3 us                                                | 9.99 us: 1.73x faster                                                  |
| float                         | 72.4 ms                                                | 42.8 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.68x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.73 ms: 1.67x faster                                                  |
| html5lib                      | 43.5 ms                                                | 28.2 ms: 1.54x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 185 us: 1.54x faster                                                   |
| generators                    | 31.7 ms                                                | 20.7 ms: 1.53x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.52 us: 1.53x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 875 ms: 1.52x faster                                                   |
| pyflate                       | 448 ms                                                 | 297 ms: 1.51x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 434 ms: 1.49x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 64.0 ms: 1.49x faster                                                  |
| pylint                        | 231 ms                                                 | 156 ms: 1.48x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 64.5 ms: 1.48x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                                   |
| logging_format                | 5.03 us                                                | 3.42 us: 1.47x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.12 us: 1.47x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.23 ms: 1.46x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 50.5 ms: 1.45x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.44x faster                                                 |
| coroutines                    | 20.5 ms                                                | 14.4 ms: 1.43x faster                                                  |
| mako                          | 9.81 ms                                                | 6.97 ms: 1.41x faster                                                  |
| pycparser                     | 887 ms                                                 | 639 ms: 1.39x faster                                                   |
| nbody                         | 92.5 ms                                                | 66.9 ms: 1.38x faster                                                  |
| regex_dna                     | 175 ms                                                 | 127 ms: 1.37x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.3 ms: 1.37x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 167 ms: 1.35x faster                                                   |
| k_core                        | 2.01 sec                                               | 1.49 sec: 1.35x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 13.3 ms: 1.34x faster                                                  |
| thrift                        | 562 us                                                 | 424 us: 1.33x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 77.9 ms: 1.32x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 27.1 ms: 1.31x faster                                                  |
| fannkuch                      | 303 ms                                                 | 235 ms: 1.29x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 73.0 ms: 1.27x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 27.8 ms: 1.26x faster                                                  |
| sphinx                        | 729 ms                                                 | 577 ms: 1.26x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.73 ms: 1.25x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 35.8 ms: 1.25x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                 |
| sympy_str                     | 166 ms                                                 | 135 ms: 1.23x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 63.5 ms: 1.22x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.21x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 225 ms: 1.19x faster                                                   |
| django_template               | 24.4 ms                                                | 20.4 ms: 1.19x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.05 ms: 1.18x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 93.7 ms: 1.17x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 469 us: 1.16x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.98 sec: 1.15x faster                                                 |
| mdp                           | 1.65 sec                                               | 1.44 sec: 1.15x faster                                                 |
| many_optionals                | 486 us                                                 | 425 us: 1.14x faster                                                   |
| nqueens                       | 63.8 ms                                                | 56.1 ms: 1.14x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 32.9 ms: 1.13x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.5 ms: 1.09x faster                                                  |
| 2to3                          | 201 ms                                                 | 185 ms: 1.09x faster                                                   |
| connected_components          | 318 ms                                                 | 294 ms: 1.08x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 180 ms: 1.07x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 50.6 ms: 1.06x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.6 ms: 1.06x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 71.2 ms: 1.05x faster                                                  |
| json                          | 3.10 ms                                                | 2.97 ms: 1.04x faster                                                  |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                   |
| shortest_path                 | 328 ms                                                 | 322 ms: 1.02x faster                                                   |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                   |
| json_loads                    | 16.6 us                                                | 17.3 us: 1.04x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.4 ms: 1.08x slower                                                  |
| async_generators              | 233 ms                                                 | 253 ms: 1.09x slower                                                   |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| coverage                      | 41.2 ms                                                | 46.6 ms: 1.13x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.09 ms: 1.14x slower                                                  |
| telco                         | 3.49 ms                                                | 4.41 ms: 1.26x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.44x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, sqlite_synth
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.444x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.11x