# Results vs. 3.10.4

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: darwin-arm64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.328x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 169 ms: 1.19x faster                                                   |
| docutils       | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                 |
| html5lib       | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                  |
| sphinx         | 729 ms                                                 | 591 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.0 ms: 6.03x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.46x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 373 ms: 2.72x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 390 ms: 2.61x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                                   |
| async_tree_none               | 391 ms                                                 | 167 ms: 2.34x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 412 ms: 1.62x faster                                                   |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                  |
| async_generators              | 233 ms                                                 | 261 ms: 1.12x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.05x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.5 ms: 1.46x faster                                                  |
| nbody          | 92.5 ms                                                | 75.7 ms: 1.22x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 73.2 ms: 1.30x faster                                                  |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.28 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 220 us: 1.29x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.34 sec: 1.28x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 162 us: 1.23x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 39.9 ms: 1.12x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.43 ms: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 73.6 ms: 1.01x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.3 ms: 1.02x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.87 ms: 1.25x faster                                                  |
| genshi_text     | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 30.8 ms: 1.14x faster                                                  |
| django_template | 24.4 ms                                                | 22.2 ms: 1.10x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.0 ms: 6.03x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.46x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 98.3 us: 3.32x faster                                                  |
| subparsers                    | 39.8 ms                                                | 12.6 ms: 3.17x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 373 ms: 2.72x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 390 ms: 2.61x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                                   |
| async_tree_none               | 391 ms                                                 | 167 ms: 2.34x faster                                                   |
| mdp                           | 1.65 sec                                               | 785 ms: 2.10x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.56 ms: 1.95x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                                   |
| go                            | 163 ms                                                 | 88.7 ms: 1.84x faster                                                  |
| raytrace                      | 327 ms                                                 | 179 ms: 1.83x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 19.3 us: 1.80x faster                                                  |
| deepcopy                      | 276 us                                                 | 159 us: 1.73x faster                                                   |
| logging_silent                | 117 ns                                                 | 69.0 ns: 1.70x faster                                                  |
| chaos                         | 67.7 ms                                                | 40.9 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 412 ms: 1.62x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 88.6 ms: 1.58x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.4 ms: 1.56x faster                                                  |
| richards_super                | 61.0 ms                                                | 40.5 ms: 1.50x faster                                                  |
| float                         | 72.4 ms                                                | 49.5 ms: 1.46x faster                                                  |
| richards                      | 52.3 ms                                                | 36.5 ms: 1.43x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 25.3 ms: 1.41x faster                                                  |
| pyflate                       | 448 ms                                                 | 318 ms: 1.41x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.67 us: 1.39x faster                                                  |
| pylint                        | 231 ms                                                 | 166 ms: 1.39x faster                                                   |
| html5lib                      | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                  |
| comprehensions                | 17.3 us                                                | 12.6 us: 1.37x faster                                                  |
| logging_format                | 5.03 us                                                | 3.77 us: 1.34x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 71.5 ms: 1.33x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.45 us: 1.33x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.85 ms: 1.32x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 73.2 ms: 1.30x faster                                                  |
| generators                    | 31.7 ms                                                | 24.3 ms: 1.30x faster                                                  |
| pycparser                     | 887 ms                                                 | 682 ms: 1.30x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 220 us: 1.29x faster                                                   |
| hexiom                        | 6.25 ms                                                | 4.84 ms: 1.29x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.34 sec: 1.28x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.04 sec: 1.28x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 57.5 ms: 1.27x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 514 ms: 1.26x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 81.4 ms: 1.26x faster                                                  |
| mako                          | 9.81 ms                                                | 7.87 ms: 1.25x faster                                                  |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.2 ms: 1.24x faster                                                  |
| sphinx                        | 729 ms                                                 | 591 ms: 1.23x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 162 us: 1.23x faster                                                   |
| nbody                         | 92.5 ms                                                | 75.7 ms: 1.22x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 77.6 ms: 1.19x faster                                                  |
| 2to3                          | 201 ms                                                 | 169 ms: 1.19x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 194 ms: 1.16x faster                                                   |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 30.8 ms: 1.14x faster                                                  |
| sympy_str                     | 166 ms                                                 | 148 ms: 1.12x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 39.9 ms: 1.12x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.43 ms: 1.12x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.12 sec: 1.10x faster                                                 |
| django_template               | 24.4 ms                                                | 22.2 ms: 1.10x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 248 ms: 1.08x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 505 us: 1.08x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.8 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.20 ms: 1.07x faster                                                  |
| many_optionals                | 486 us                                                 | 456 us: 1.07x faster                                                   |
| fannkuch                      | 303 ms                                                 | 284 ms: 1.06x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 75.7 ms: 1.03x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.28 ms: 1.03x faster                                                  |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                  |
| python_startup                | 19.6 ms                                                | 19.3 ms: 1.02x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 73.6 ms: 1.01x faster                                                  |
| nqueens                       | 63.8 ms                                                | 64.0 ms: 1.00x slower                                                  |
| connected_components          | 318 ms                                                 | 320 ms: 1.00x slower                                                   |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| xml_etree_generate            | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                  |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 61.2 ms: 1.09x slower                                                  |
| async_generators              | 233 ms                                                 | 261 ms: 1.12x slower                                                   |
| coverage                      | 41.2 ms                                                | 46.4 ms: 1.13x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                  |
| telco                         | 3.49 ms                                                | 4.68 ms: 1.34x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.32x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250403-3.14.0a6+-275056a/bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.328x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.14x