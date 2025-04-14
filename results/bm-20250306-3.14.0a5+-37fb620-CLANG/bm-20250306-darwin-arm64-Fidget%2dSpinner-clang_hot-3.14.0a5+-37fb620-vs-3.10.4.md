# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: clang_hot
- machine: darwin-arm64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.469x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 150 ms: 1.34x faster                                                  |
| docutils       | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                |
| html5lib       | 43.5 ms                                                | 28.8 ms: 1.51x faster                                                 |
| sphinx         | 729 ms                                                 | 540 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.3 ms: 7.09x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 131 ms: 3.69x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 332 ms: 3.05x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 344 ms: 2.96x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 182 ms: 2.65x faster                                                  |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 342 ms: 1.95x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 404 ms: 1.65x faster                                                  |
| coroutines                    | 20.5 ms                                                | 14.9 ms: 1.38x faster                                                 |
| async_generators              | 233 ms                                                 | 237 ms: 1.02x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.24x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.2 ms: 1.64x faster                                                 |
| nbody          | 92.5 ms                                                | 63.6 ms: 1.45x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                 |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.6 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 123 us: 1.62x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 183 us: 1.55x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 33.3 ms: 1.34x faster                                                 |
| json_dumps           | 8.31 ms                                                | 7.10 ms: 1.17x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 48.2 ms: 1.12x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 68.9 ms: 1.08x faster                                                 |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.8 ms: 1.04x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.9 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.5 ms: 1.41x faster                                                 |
| mako            | 9.81 ms                                                | 7.06 ms: 1.39x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                 |
| django_template | 24.4 ms                                                | 18.7 ms: 1.30x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.3 ms: 7.09x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 84.3 us: 3.87x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 131 ms: 3.69x faster                                                  |
| subparsers                    | 39.8 ms                                                | 11.4 ms: 3.50x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 332 ms: 3.05x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 344 ms: 2.96x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 182 ms: 2.65x faster                                                  |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.04 ms: 2.44x faster                                                 |
| go                            | 163 ms                                                 | 70.7 ms: 2.31x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 16.3 us: 2.13x faster                                                 |
| raytrace                      | 327 ms                                                 | 162 ms: 2.02x faster                                                  |
| logging_silent                | 117 ns                                                 | 59.0 ns: 1.98x faster                                                 |
| deepcopy                      | 276 us                                                 | 139 us: 1.98x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 342 ms: 1.95x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 695 us: 1.94x faster                                                  |
| chaos                         | 67.7 ms                                                | 34.9 ms: 1.94x faster                                                 |
| richards_super                | 61.0 ms                                                | 31.4 ms: 1.94x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 73.6 ms: 1.90x faster                                                 |
| richards                      | 52.3 ms                                                | 27.9 ms: 1.87x faster                                                 |
| sqlglot_transpile             | 1.56 ms                                                | 841 us: 1.85x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 39.3 ms: 1.84x faster                                                 |
| generators                    | 31.7 ms                                                | 17.7 ms: 1.80x faster                                                 |
| comprehensions                | 17.3 us                                                | 9.72 us: 1.78x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 404 ms: 1.65x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.80 ms: 1.64x faster                                                 |
| float                         | 72.4 ms                                                | 44.2 ms: 1.64x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 123 us: 1.62x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.91 us: 1.58x faster                                                 |
| logging_format                | 5.03 us                                                | 3.20 us: 1.57x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.48 us: 1.57x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 183 us: 1.55x faster                                                  |
| pylint                        | 231 ms                                                 | 149 ms: 1.55x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                 |
| pyflate                       | 448 ms                                                 | 295 ms: 1.52x faster                                                  |
| html5lib                      | 43.5 ms                                                | 28.8 ms: 1.51x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 880 ms: 1.51x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.06 ms: 1.49x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 436 ms: 1.49x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 69.1 ms: 1.48x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.9 ms: 1.47x faster                                                 |
| nbody                         | 92.5 ms                                                | 63.6 ms: 1.45x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 12.5 ms: 1.41x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 67.9 ms: 1.40x faster                                                 |
| sqlalchemy_declarative        | 75.7 ms                                                | 54.2 ms: 1.40x faster                                                 |
| mako                          | 9.81 ms                                                | 7.06 ms: 1.39x faster                                                 |
| thrift                        | 562 us                                                 | 406 us: 1.38x faster                                                  |
| coroutines                    | 20.5 ms                                                | 14.9 ms: 1.38x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.48 sec: 1.36x faster                                                |
| sphinx                        | 729 ms                                                 | 540 ms: 1.35x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.4 ms: 1.35x faster                                                 |
| 2to3                          | 201 ms                                                 | 150 ms: 1.34x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 69.0 ms: 1.34x faster                                                 |
| pycparser                     | 887 ms                                                 | 661 ms: 1.34x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 33.3 ms: 1.34x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 173 ms: 1.30x faster                                                  |
| django_template               | 24.4 ms                                                | 18.7 ms: 1.30x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.1 ms: 1.30x faster                                                 |
| sympy_str                     | 166 ms                                                 | 129 ms: 1.29x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                |
| nqueens                       | 63.8 ms                                                | 50.7 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.73 ms: 1.25x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 215 ms: 1.25x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 29.9 ms: 1.25x faster                                                 |
| fannkuch                      | 303 ms                                                 | 245 ms: 1.24x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.83 sec: 1.21x faster                                                |
| bench_thread_pool             | 545 us                                                 | 451 us: 1.21x faster                                                  |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| sqlglot_normalize             | 192 ms                                                 | 162 ms: 1.18x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.10 ms: 1.17x faster                                                 |
| many_optionals                | 486 us                                                 | 416 us: 1.17x faster                                                  |
| pathlib                       | 25.7 ms                                                | 22.8 ms: 1.13x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 69.3 ms: 1.12x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 48.2 ms: 1.12x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 17.6 ms: 1.09x faster                                                 |
| connected_components          | 318 ms                                                 | 294 ms: 1.08x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 68.9 ms: 1.08x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.8 ms: 1.04x faster                                                 |
| json                          | 3.10 ms                                                | 2.99 ms: 1.04x faster                                                 |
| mdp                           | 1.65 sec                                               | 1.60 sec: 1.03x faster                                                |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                  |
| shortest_path                 | 328 ms                                                 | 322 ms: 1.02x faster                                                  |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.49 us: 1.01x slower                                                 |
| async_generators              | 233 ms                                                 | 237 ms: 1.02x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.8 ms: 1.07x slower                                                 |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                 |
| coverage                      | 41.2 ms                                                | 44.2 ms: 1.07x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.25 ms: 1.07x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 13.9 ms: 1.09x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.08 ms: 1.14x slower                                                 |
| telco                         | 3.49 ms                                                | 4.42 ms: 1.27x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.46x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.469x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.12x