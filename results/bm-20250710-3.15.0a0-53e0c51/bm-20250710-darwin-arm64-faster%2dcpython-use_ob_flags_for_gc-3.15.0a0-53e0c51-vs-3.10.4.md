# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: darwin-arm64
- commit hash: 53e0c51
- commit date: 2025-07-10
- overall geometric mean: 1.245x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 188 ms: 1.07x faster                                                           |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                         |
| html5lib       | 43.5 ms                                                | 34.4 ms: 1.26x faster                                                          |
| sphinx         | 729 ms                                                 | 620 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.5 ms: 5.33x faster                                                          |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.21x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                           |
| async_tree_io                 | 1.02 sec                                               | 404 ms: 2.52x faster                                                           |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.25x faster                                                           |
| async_tree_none               | 391 ms                                                 | 180 ms: 2.17x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                           |
| coroutines                    | 20.5 ms                                                | 19.1 ms: 1.07x faster                                                          |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                           |
| async_generators              | 233 ms                                                 | 278 ms: 1.19x slower                                                           |
| Geometric mean                | (ref)                                                  | 1.93x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 59.9 ms: 1.21x faster                                                          |
| nbody          | 92.5 ms                                                | 86.6 ms: 1.07x faster                                                          |
| pidigits       | 280 ms                                                 | 286 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 144 ms: 1.21x faster                                                           |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                          |
| regex_compile  | 95.6 ms                                                | 82.2 ms: 1.16x faster                                                          |
| regex_effbot   | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.94 ms: 1.20x faster                                                          |
| tomli_loads          | 1.72 sec                                               | 1.45 sec: 1.19x faster                                                         |
| pickle_pure_python   | 285 us                                                 | 243 us: 1.17x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 98.7 ms: 1.11x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 182 us: 1.09x faster                                                           |
| xml_etree_process    | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 74.5 ms                                                | 73.5 ms: 1.01x faster                                                          |
| json_loads           | 16.6 us                                                | 16.7 us: 1.01x slower                                                          |
| xml_etree_generate   | 53.9 ms                                                | 58.9 ms: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.7 ms: 1.17x faster                                                          |
| python_startup_no_site | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.16 ms: 1.07x faster                                                          |
| genshi_text     | 17.7 ms                                                | 17.9 ms: 1.01x slower                                                          |
| django_template | 24.4 ms                                                | 25.1 ms: 1.03x slower                                                          |
| genshi_xml      | 35.1 ms                                                | 36.7 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.5 ms: 5.33x faster                                                          |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.21x faster                                                           |
| typing_runtime_protocols      | 326 us                                                 | 107 us: 3.04x faster                                                           |
| subparsers                    | 39.8 ms                                                | 14.9 ms: 2.68x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                           |
| async_tree_io                 | 1.02 sec                                               | 404 ms: 2.52x faster                                                           |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.25x faster                                                           |
| async_tree_none               | 391 ms                                                 | 180 ms: 2.17x faster                                                           |
| mdp                           | 1.65 sec                                               | 836 ms: 1.97x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                           |
| deltablue                     | 4.99 ms                                                | 2.81 ms: 1.77x faster                                                          |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 22.0 us: 1.57x faster                                                          |
| deepcopy                      | 276 us                                                 | 177 us: 1.56x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                           |
| raytrace                      | 327 ms                                                 | 215 ms: 1.52x faster                                                           |
| scimark_sor                   | 140 ms                                                 | 92.2 ms: 1.52x faster                                                          |
| logging_silent                | 117 ns                                                 | 77.7 ns: 1.51x faster                                                          |
| chaos                         | 67.7 ms                                                | 47.6 ms: 1.42x faster                                                          |
| richards_super                | 61.0 ms                                                | 43.4 ms: 1.40x faster                                                          |
| richards                      | 52.3 ms                                                | 37.8 ms: 1.38x faster                                                          |
| pylint                        | 231 ms                                                 | 169 ms: 1.37x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.36x faster                                                         |
| scimark_monte_carlo           | 72.4 ms                                                | 53.5 ms: 1.35x faster                                                          |
| pyflate                       | 448 ms                                                 | 338 ms: 1.32x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 73.3 ms: 1.30x faster                                                          |
| comprehensions                | 17.3 us                                                | 13.3 us: 1.30x faster                                                          |
| html5lib                      | 43.5 ms                                                | 34.4 ms: 1.26x faster                                                          |
| hexiom                        | 6.25 ms                                                | 5.10 ms: 1.22x faster                                                          |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                                          |
| logging_format                | 5.03 us                                                | 4.14 us: 1.22x faster                                                          |
| regex_dna                     | 175 ms                                                 | 144 ms: 1.21x faster                                                           |
| float                         | 72.4 ms                                                | 59.9 ms: 1.21x faster                                                          |
| crypto_pyaes                  | 73.3 ms                                                | 60.8 ms: 1.21x faster                                                          |
| scimark_lu                    | 103 ms                                                 | 85.3 ms: 1.20x faster                                                          |
| dulwich_log                   | 35.6 ms                                                | 29.7 ms: 1.20x faster                                                          |
| json_dumps                    | 8.31 ms                                                | 6.94 ms: 1.20x faster                                                          |
| logging_simple                | 4.59 us                                                | 3.84 us: 1.20x faster                                                          |
| tomli_loads                   | 1.72 sec                                               | 1.45 sec: 1.19x faster                                                         |
| pycparser                     | 887 ms                                                 | 748 ms: 1.19x faster                                                           |
| sphinx                        | 729 ms                                                 | 620 ms: 1.18x faster                                                           |
| thrift                        | 562 us                                                 | 478 us: 1.18x faster                                                           |
| python_startup                | 19.6 ms                                                | 16.7 ms: 1.17x faster                                                          |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                          |
| pickle_pure_python            | 285 us                                                 | 243 us: 1.17x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 82.2 ms: 1.16x faster                                                          |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                                          |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                         |
| sympy_sum                     | 92.7 ms                                                | 82.3 ms: 1.13x faster                                                          |
| xml_etree_parse               | 109 ms                                                 | 98.7 ms: 1.11x faster                                                          |
| pathlib                       | 25.7 ms                                                | 23.3 ms: 1.11x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 1.21 sec: 1.10x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 205 ms: 1.10x faster                                                           |
| pprint_safe_repr              | 648 ms                                                 | 594 ms: 1.09x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 182 us: 1.09x faster                                                           |
| 2to3                          | 201 ms                                                 | 188 ms: 1.07x faster                                                           |
| coroutines                    | 20.5 ms                                                | 19.1 ms: 1.07x faster                                                          |
| mako                          | 9.81 ms                                                | 9.16 ms: 1.07x faster                                                          |
| nbody                         | 92.5 ms                                                | 86.6 ms: 1.07x faster                                                          |
| bpe_tokeniser                 | 3.44 sec                                               | 3.28 sec: 1.05x faster                                                         |
| sympy_str                     | 166 ms                                                 | 158 ms: 1.05x faster                                                           |
| json                          | 3.10 ms                                                | 2.98 ms: 1.04x faster                                                          |
| meteor_contest                | 77.8 ms                                                | 74.9 ms: 1.04x faster                                                          |
| connected_components          | 318 ms                                                 | 307 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.31 ms: 1.03x faster                                                          |
| python_startup_no_site        | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                          |
| dask                          | 789 ms                                                 | 770 ms: 1.03x faster                                                           |
| xml_etree_process             | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 73.5 ms: 1.01x faster                                                          |
| sympy_expand                  | 269 ms                                                 | 267 ms: 1.01x faster                                                           |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                           |
| generators                    | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                          |
| json_loads                    | 16.6 us                                                | 16.7 us: 1.01x slower                                                          |
| shortest_path                 | 328 ms                                                 | 331 ms: 1.01x slower                                                           |
| regex_effbot                  | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                          |
| genshi_text                   | 17.7 ms                                                | 17.9 ms: 1.01x slower                                                          |
| pidigits                      | 280 ms                                                 | 286 ms: 1.02x slower                                                           |
| many_optionals                | 486 us                                                 | 500 us: 1.03x slower                                                           |
| django_template               | 24.4 ms                                                | 25.1 ms: 1.03x slower                                                          |
| genshi_xml                    | 35.1 ms                                                | 36.7 ms: 1.05x slower                                                          |
| fannkuch                      | 303 ms                                                 | 327 ms: 1.08x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                          |
| xml_etree_generate            | 53.9 ms                                                | 58.9 ms: 1.09x slower                                                          |
| sqlite_synth                  | 1.48 us                                                | 1.65 us: 1.12x slower                                                          |
| nqueens                       | 63.8 ms                                                | 71.6 ms: 1.12x slower                                                          |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                          |
| async_generators              | 233 ms                                                 | 278 ms: 1.19x slower                                                           |
| coverage                      | 41.2 ms                                                | 49.6 ms: 1.20x slower                                                          |
| telco                         | 3.49 ms                                                | 4.89 ms: 1.40x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                                   |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250710-3.15.0a0-53e0c51/bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.245x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.17x