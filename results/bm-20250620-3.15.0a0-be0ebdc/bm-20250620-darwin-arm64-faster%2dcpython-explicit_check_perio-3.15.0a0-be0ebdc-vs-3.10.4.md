# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.244x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 188 ms: 1.07x faster                                                            |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.14x faster                                                          |
| html5lib       | 43.5 ms                                                | 34.3 ms: 1.27x faster                                                           |
| sphinx         | 729 ms                                                 | 620 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.32x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.57x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 417 ms: 2.44x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                                            |
| async_tree_none               | 391 ms                                                 | 185 ms: 2.12x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.54x faster                                                            |
| coroutines                    | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                           |
| async_generators              | 233 ms                                                 | 278 ms: 1.19x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.8 ms: 1.25x faster                                                           |
| nbody          | 92.5 ms                                                | 85.3 ms: 1.08x faster                                                           |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                           |
| regex_compile  | 95.6 ms                                                | 82.0 ms: 1.16x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.40 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                           |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                            |
| tomli_loads          | 1.72 sec                                               | 1.46 sec: 1.17x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 180 us: 1.10x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 43.8 ms: 1.02x faster                                                           |
| json_loads           | 16.6 us                                                | 16.7 us: 1.01x slower                                                           |
| xml_etree_generate   | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.6 ms: 1.11x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.10 ms: 1.08x faster                                                           |
| genshi_text     | 17.7 ms                                                | 17.8 ms: 1.00x slower                                                           |
| genshi_xml      | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                           |
| django_template | 24.4 ms                                                | 25.5 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.32x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 109 us: 2.98x faster                                                            |
| subparsers                    | 39.8 ms                                                | 14.9 ms: 2.67x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.57x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 417 ms: 2.44x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                                            |
| async_tree_none               | 391 ms                                                 | 185 ms: 2.12x faster                                                            |
| mdp                           | 1.65 sec                                               | 831 ms: 1.99x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.83 ms: 1.76x faster                                                           |
| go                            | 163 ms                                                 | 99.5 ms: 1.64x faster                                                           |
| deepcopy                      | 276 us                                                 | 175 us: 1.58x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 22.1 us: 1.57x faster                                                           |
| scimark_sor                   | 140 ms                                                 | 90.0 ms: 1.55x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.54x faster                                                            |
| raytrace                      | 327 ms                                                 | 213 ms: 1.54x faster                                                            |
| richards_super                | 61.0 ms                                                | 41.7 ms: 1.46x faster                                                           |
| chaos                         | 67.7 ms                                                | 47.2 ms: 1.43x faster                                                           |
| richards                      | 52.3 ms                                                | 37.4 ms: 1.40x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                          |
| pylint                        | 231 ms                                                 | 169 ms: 1.37x faster                                                            |
| scimark_monte_carlo           | 72.4 ms                                                | 53.0 ms: 1.37x faster                                                           |
| pyflate                       | 448 ms                                                 | 333 ms: 1.34x faster                                                            |
| dulwich_log                   | 35.6 ms                                                | 26.5 ms: 1.34x faster                                                           |
| comprehensions                | 17.3 us                                                | 13.2 us: 1.32x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 72.6 ms: 1.31x faster                                                           |
| html5lib                      | 43.5 ms                                                | 34.3 ms: 1.27x faster                                                           |
| float                         | 72.4 ms                                                | 57.8 ms: 1.25x faster                                                           |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.91 us: 1.22x faster                                                           |
| hexiom                        | 6.25 ms                                                | 5.14 ms: 1.22x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 61.1 ms: 1.20x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 85.6 ms: 1.20x faster                                                           |
| pycparser                     | 887 ms                                                 | 742 ms: 1.20x faster                                                            |
| thrift                        | 562 us                                                 | 471 us: 1.19x faster                                                            |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                            |
| sphinx                        | 729 ms                                                 | 620 ms: 1.18x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.46 sec: 1.17x faster                                                          |
| regex_compile                 | 95.6 ms                                                | 82.0 ms: 1.16x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.14x faster                                                          |
| logging_format                | 5.03 us                                                | 4.43 us: 1.14x faster                                                           |
| sympy_sum                     | 92.7 ms                                                | 81.7 ms: 1.13x faster                                                           |
| pathlib                       | 25.7 ms                                                | 22.8 ms: 1.13x faster                                                           |
| python_startup                | 19.6 ms                                                | 17.6 ms: 1.11x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 203 ms: 1.11x faster                                                            |
| logging_simple                | 4.59 us                                                | 4.14 us: 1.11x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 180 us: 1.10x faster                                                            |
| coroutines                    | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                           |
| nbody                         | 92.5 ms                                                | 85.3 ms: 1.08x faster                                                           |
| mako                          | 9.81 ms                                                | 9.10 ms: 1.08x faster                                                           |
| 2to3                          | 201 ms                                                 | 188 ms: 1.07x faster                                                            |
| sympy_str                     | 166 ms                                                 | 156 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.22 ms: 1.06x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| json                          | 3.10 ms                                                | 2.96 ms: 1.05x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.29 sec: 1.05x faster                                                          |
| meteor_contest                | 77.8 ms                                                | 74.5 ms: 1.04x faster                                                           |
| connected_components          | 318 ms                                                 | 305 ms: 1.04x faster                                                            |
| pprint_pformat                | 1.33 sec                                               | 1.27 sec: 1.04x faster                                                          |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 630 ms: 1.03x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 43.8 ms: 1.02x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 264 ms: 1.02x faster                                                            |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 17.8 ms: 1.00x slower                                                           |
| fannkuch                      | 303 ms                                                 | 304 ms: 1.00x slower                                                            |
| shortest_path                 | 328 ms                                                 | 330 ms: 1.01x slower                                                            |
| json_loads                    | 16.6 us                                                | 16.7 us: 1.01x slower                                                           |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.40 ms: 1.03x slower                                                           |
| many_optionals                | 486 us                                                 | 499 us: 1.03x slower                                                            |
| python_startup_no_site        | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                           |
| genshi_xml                    | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                           |
| django_template               | 24.4 ms                                                | 25.5 ms: 1.05x slower                                                           |
| nqueens                       | 63.8 ms                                                | 69.8 ms: 1.09x slower                                                           |
| xml_etree_generate            | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.63 us: 1.10x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                           |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                           |
| async_generators              | 233 ms                                                 | 278 ms: 1.19x slower                                                            |
| coverage                      | 41.2 ms                                                | 49.4 ms: 1.20x slower                                                           |
| telco                         | 3.49 ms                                                | 4.74 ms: 1.36x slower                                                           |
| logging_silent                | 117 ns                                                 | 344 ns: 2.94x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.244x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.17x