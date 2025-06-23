# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.247x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.08x faster                                                            |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                          |
| html5lib       | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                           |
| sphinx         | 729 ms                                                 | 618 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.1 ms: 5.36x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 393 ms: 2.58x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.45x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 215 ms: 2.24x faster                                                            |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.54x faster                                                            |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                           |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.93x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.7 ms: 1.26x faster                                                           |
| nbody          | 92.5 ms                                                | 85.1 ms: 1.09x faster                                                           |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 144 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                           |
| regex_compile  | 95.6 ms                                                | 81.5 ms: 1.17x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.35 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.81 ms: 1.22x faster                                                           |
| tomli_loads          | 1.72 sec                                               | 1.46 sec: 1.18x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 243 us: 1.17x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 180 us: 1.10x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 43.5 ms: 1.02x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.21 ms: 1.06x faster                                                           |
| genshi_text     | 17.7 ms                                                | 17.8 ms: 1.01x slower                                                           |
| genshi_xml      | 35.1 ms                                                | 36.3 ms: 1.03x slower                                                           |
| django_template | 24.4 ms                                                | 25.5 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.1 ms: 5.36x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 110 us: 2.97x faster                                                            |
| subparsers                    | 39.8 ms                                                | 14.9 ms: 2.68x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 393 ms: 2.58x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.45x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 215 ms: 2.24x faster                                                            |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                                            |
| mdp                           | 1.65 sec                                               | 830 ms: 1.99x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.81 ms: 1.77x faster                                                           |
| go                            | 163 ms                                                 | 99.2 ms: 1.65x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 22.0 us: 1.58x faster                                                           |
| deepcopy                      | 276 us                                                 | 176 us: 1.57x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 89.7 ms: 1.56x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.54x faster                                                            |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                            |
| richards_super                | 61.0 ms                                                | 41.5 ms: 1.47x faster                                                           |
| chaos                         | 67.7 ms                                                | 47.2 ms: 1.44x faster                                                           |
| richards                      | 52.3 ms                                                | 37.6 ms: 1.39x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 52.7 ms: 1.37x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                          |
| pylint                        | 231 ms                                                 | 169 ms: 1.36x faster                                                            |
| dulwich_log                   | 35.6 ms                                                | 26.5 ms: 1.34x faster                                                           |
| pyflate                       | 448 ms                                                 | 336 ms: 1.33x faster                                                            |
| spectral_norm                 | 95.3 ms                                                | 71.7 ms: 1.33x faster                                                           |
| comprehensions                | 17.3 us                                                | 13.2 us: 1.31x faster                                                           |
| html5lib                      | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                           |
| float                         | 72.4 ms                                                | 57.7 ms: 1.26x faster                                                           |
| hexiom                        | 6.25 ms                                                | 5.10 ms: 1.23x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 6.81 ms: 1.22x faster                                                           |
| regex_dna                     | 175 ms                                                 | 144 ms: 1.22x faster                                                            |
| deepcopy_reduce               | 2.32 us                                                | 1.91 us: 1.22x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 60.9 ms: 1.20x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 85.4 ms: 1.20x faster                                                           |
| thrift                        | 562 us                                                 | 473 us: 1.19x faster                                                            |
| pycparser                     | 887 ms                                                 | 748 ms: 1.19x faster                                                            |
| sphinx                        | 729 ms                                                 | 618 ms: 1.18x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.46 sec: 1.18x faster                                                          |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 81.5 ms: 1.17x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 243 us: 1.17x faster                                                            |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                           |
| logging_format                | 5.03 us                                                | 4.38 us: 1.15x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                          |
| sympy_sum                     | 92.7 ms                                                | 81.4 ms: 1.14x faster                                                           |
| logging_simple                | 4.59 us                                                | 4.10 us: 1.12x faster                                                           |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 201 ms: 1.12x faster                                                            |
| unpickle_pure_python          | 198 us                                                 | 180 us: 1.10x faster                                                            |
| python_startup                | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                           |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                           |
| nbody                         | 92.5 ms                                                | 85.1 ms: 1.09x faster                                                           |
| 2to3                          | 201 ms                                                 | 187 ms: 1.08x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.18 ms: 1.07x faster                                                           |
| sympy_str                     | 166 ms                                                 | 155 ms: 1.07x faster                                                            |
| mako                          | 9.81 ms                                                | 9.21 ms: 1.06x faster                                                           |
| connected_components          | 318 ms                                                 | 300 ms: 1.06x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.26 sec: 1.05x faster                                                          |
| json                          | 3.10 ms                                                | 2.95 ms: 1.05x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| meteor_contest                | 77.8 ms                                                | 74.2 ms: 1.05x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 1.27 sec: 1.04x faster                                                          |
| pprint_safe_repr              | 648 ms                                                 | 627 ms: 1.03x faster                                                            |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 43.5 ms: 1.02x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 263 ms: 1.02x faster                                                            |
| generators                    | 31.7 ms                                                | 31.6 ms: 1.00x faster                                                           |
| regex_effbot                  | 2.34 ms                                                | 2.35 ms: 1.00x slower                                                           |
| genshi_text                   | 17.7 ms                                                | 17.8 ms: 1.01x slower                                                           |
| fannkuch                      | 303 ms                                                 | 305 ms: 1.01x slower                                                            |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| genshi_xml                    | 35.1 ms                                                | 36.3 ms: 1.03x slower                                                           |
| many_optionals                | 486 us                                                 | 502 us: 1.03x slower                                                            |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                           |
| django_template               | 24.4 ms                                                | 25.5 ms: 1.05x slower                                                           |
| xml_etree_generate            | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.10x slower                                                           |
| nqueens                       | 63.8 ms                                                | 70.9 ms: 1.11x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                           |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                           |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                            |
| coverage                      | 41.2 ms                                                | 49.6 ms: 1.20x slower                                                           |
| telco                         | 3.49 ms                                                | 4.74 ms: 1.36x slower                                                           |
| logging_silent                | 117 ns                                                 | 345 ns: 2.95x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, shortest_path, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.247x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.17x