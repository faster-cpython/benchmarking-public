# Results vs. 3.10.4

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: darwin-arm64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.295x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 183 ms: 1.10x faster                                                     |
| docutils       | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                   |
| html5lib       | 43.5 ms                                                | 31.0 ms: 1.40x faster                                                    |
| sphinx         | 729 ms                                                 | 597 ms: 1.22x faster                                                     |
| Geometric mean | (ref)                                                  | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 82.1 ms: 4.77x faster                                                    |
| async_tree_eager_io           | 1.01 sec                                               | 316 ms: 3.21x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.17x faster                                                     |
| async_tree_io                 | 1.02 sec                                               | 331 ms: 3.07x faster                                                     |
| async_tree_none               | 391 ms                                                 | 159 ms: 2.46x faster                                                     |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.45x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.81x faster                                                     |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                     |
| coroutines                    | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                    |
| asyncio_websockets            | 242 ms                                                 | 237 ms: 1.02x faster                                                     |
| async_generators              | 233 ms                                                 | 259 ms: 1.11x slower                                                     |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.1 ms: 1.54x faster                                                    |
| nbody          | 92.5 ms                                                | 87.1 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 75.0 ms: 1.27x faster                                                    |
| regex_dna      | 175 ms                                                 | 137 ms: 1.27x faster                                                     |
| regex_v8       | 19.1 ms                                                | 15.4 ms: 1.24x faster                                                    |
| regex_effbot   | 2.34 ms                                                | 2.08 ms: 1.12x faster                                                    |
| Geometric mean | (ref)                                                  | 1.23x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 153 us: 1.29x faster                                                     |
| pickle_pure_python   | 285 us                                                 | 222 us: 1.28x faster                                                     |
| tomli_loads          | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.65 ms: 1.09x faster                                                    |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.7 ms: 1.05x slower                                                    |
| python_startup_no_site | 12.8 ms                                                | 16.1 ms: 1.26x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 15.9 ms: 1.12x faster                                                    |
| genshi_xml      | 35.1 ms                                                | 32.3 ms: 1.09x faster                                                    |
| django_template | 24.4 ms                                                | 24.0 ms: 1.02x faster                                                    |
| mako            | 9.81 ms                                                | 9.96 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 82.1 ms: 4.77x faster                                                    |
| async_tree_eager_io           | 1.01 sec                                               | 316 ms: 3.21x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.17x faster                                                     |
| subparsers                    | 39.8 ms                                                | 12.8 ms: 3.12x faster                                                    |
| async_tree_io                 | 1.02 sec                                               | 331 ms: 3.07x faster                                                     |
| typing_runtime_protocols      | 326 us                                                 | 113 us: 2.87x faster                                                     |
| async_tree_none               | 391 ms                                                 | 159 ms: 2.46x faster                                                     |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.45x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.81x faster                                                     |
| go                            | 163 ms                                                 | 91.2 ms: 1.79x faster                                                    |
| deltablue                     | 4.99 ms                                                | 2.86 ms: 1.74x faster                                                    |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                     |
| deepcopy_memo                 | 34.7 us                                                | 21.5 us: 1.61x faster                                                    |
| deepcopy                      | 276 us                                                 | 172 us: 1.60x faster                                                     |
| chaos                         | 67.7 ms                                                | 43.1 ms: 1.57x faster                                                    |
| scimark_sor                   | 140 ms                                                 | 90.2 ms: 1.55x faster                                                    |
| raytrace                      | 327 ms                                                 | 211 ms: 1.55x faster                                                     |
| float                         | 72.4 ms                                                | 47.1 ms: 1.54x faster                                                    |
| sqlglot_parse                 | 1.35 ms                                                | 881 us: 1.53x faster                                                     |
| richards_super                | 61.0 ms                                                | 40.3 ms: 1.51x faster                                                    |
| logging_silent                | 117 ns                                                 | 79.3 ns: 1.48x faster                                                    |
| richards                      | 52.3 ms                                                | 35.6 ms: 1.47x faster                                                    |
| sqlglot_transpile             | 1.56 ms                                                | 1.07 ms: 1.46x faster                                                    |
| pyflate                       | 448 ms                                                 | 307 ms: 1.46x faster                                                     |
| scimark_monte_carlo           | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                    |
| html5lib                      | 43.5 ms                                                | 31.0 ms: 1.40x faster                                                    |
| pycparser                     | 887 ms                                                 | 633 ms: 1.40x faster                                                     |
| pylint                        | 231 ms                                                 | 168 ms: 1.38x faster                                                     |
| generators                    | 31.7 ms                                                | 24.0 ms: 1.32x faster                                                    |
| spectral_norm                 | 95.3 ms                                                | 72.6 ms: 1.31x faster                                                    |
| comprehensions                | 17.3 us                                                | 13.3 us: 1.31x faster                                                    |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.30x faster                                                    |
| hexiom                        | 6.25 ms                                                | 4.80 ms: 1.30x faster                                                    |
| unpickle_pure_python          | 198 us                                                 | 153 us: 1.29x faster                                                     |
| pickle_pure_python            | 285 us                                                 | 222 us: 1.28x faster                                                     |
| regex_compile                 | 95.6 ms                                                | 75.0 ms: 1.27x faster                                                    |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.27x faster                                                     |
| tomli_loads                   | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.66 us: 1.25x faster                                                    |
| crypto_pyaes                  | 73.3 ms                                                | 58.7 ms: 1.25x faster                                                    |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.26 ms: 1.25x faster                                                    |
| k_core                        | 2.01 sec                                               | 1.62 sec: 1.25x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.40 sec: 1.24x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 15.4 ms: 1.24x faster                                                    |
| logging_format                | 5.03 us                                                | 4.07 us: 1.24x faster                                                    |
| sphinx                        | 729 ms                                                 | 597 ms: 1.22x faster                                                     |
| coroutines                    | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                    |
| dulwich_log                   | 35.6 ms                                                | 29.2 ms: 1.22x faster                                                    |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.21x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 541 ms: 1.20x faster                                                     |
| scimark_lu                    | 103 ms                                                 | 88.2 ms: 1.16x faster                                                    |
| sympy_sum                     | 92.7 ms                                                | 79.8 ms: 1.16x faster                                                    |
| bpe_tokeniser                 | 3.44 sec                                               | 3.01 sec: 1.14x faster                                                   |
| thrift                        | 562 us                                                 | 496 us: 1.13x faster                                                     |
| sqlalchemy_declarative        | 75.7 ms                                                | 66.9 ms: 1.13x faster                                                    |
| pathlib                       | 25.7 ms                                                | 22.8 ms: 1.13x faster                                                    |
| regex_effbot                  | 2.34 ms                                                | 2.08 ms: 1.12x faster                                                    |
| sqlite_synth                  | 1.48 us                                                | 1.32 us: 1.12x faster                                                    |
| genshi_text                   | 17.7 ms                                                | 15.9 ms: 1.12x faster                                                    |
| 2to3                          | 201 ms                                                 | 183 ms: 1.10x faster                                                     |
| create_gc_cycles              | 1.16 ms                                                | 1.06 ms: 1.10x faster                                                    |
| genshi_xml                    | 35.1 ms                                                | 32.3 ms: 1.09x faster                                                    |
| json_dumps                    | 8.31 ms                                                | 7.65 ms: 1.09x faster                                                    |
| sqlglot_optimize              | 37.2 ms                                                | 34.4 ms: 1.08x faster                                                    |
| sympy_integrate               | 13.2 ms                                                | 12.2 ms: 1.07x faster                                                    |
| scimark_fft                   | 225 ms                                                 | 210 ms: 1.07x faster                                                     |
| fannkuch                      | 303 ms                                                 | 283 ms: 1.07x faster                                                     |
| many_optionals                | 486 us                                                 | 456 us: 1.07x faster                                                     |
| sympy_str                     | 166 ms                                                 | 156 ms: 1.06x faster                                                     |
| nbody                         | 92.5 ms                                                | 87.1 ms: 1.06x faster                                                    |
| nqueens                       | 63.8 ms                                                | 60.2 ms: 1.06x faster                                                    |
| mdp                           | 1.65 sec                                               | 1.57 sec: 1.05x faster                                                   |
| json                          | 3.10 ms                                                | 2.97 ms: 1.04x faster                                                    |
| sqlglot_normalize             | 192 ms                                                 | 188 ms: 1.03x faster                                                     |
| asyncio_websockets            | 242 ms                                                 | 237 ms: 1.02x faster                                                     |
| sympy_expand                  | 269 ms                                                 | 264 ms: 1.02x faster                                                     |
| django_template               | 24.4 ms                                                | 24.0 ms: 1.02x faster                                                    |
| mako                          | 9.81 ms                                                | 9.96 ms: 1.01x slower                                                    |
| meteor_contest                | 77.8 ms                                                | 79.0 ms: 1.02x slower                                                    |
| connected_components          | 318 ms                                                 | 326 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.56 ms: 1.04x slower                                                    |
| python_startup                | 19.6 ms                                                | 20.7 ms: 1.05x slower                                                    |
| shortest_path                 | 328 ms                                                 | 349 ms: 1.06x slower                                                     |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                    |
| async_generators              | 233 ms                                                 | 259 ms: 1.11x slower                                                     |
| bench_mp_pool                 | 56.0 ms                                                | 66.3 ms: 1.18x slower                                                    |
| python_startup_no_site        | 12.8 ms                                                | 16.1 ms: 1.26x slower                                                    |
| coverage                      | 41.2 ms                                                | 54.2 ms: 1.32x slower                                                    |
| gc_traversal                  | 2.71 ms                                                | 3.74 ms: 1.38x slower                                                    |
| telco                         | 3.49 ms                                                | 4.94 ms: 1.42x slower                                                    |
| bench_thread_pool             | 545 us                                                 | 788 us: 1.45x slower                                                     |
| Geometric mean                | (ref)                                                  | 1.28x faster                                                             |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
Ignored benchmarks (8) of results/bm-20250122-3.14.0a4+-1b4e8c3-NOGIL/bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.295x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.28x