# Results vs. 3.10.4

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: darwin-arm64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.375x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 193 ms: 1.04x faster                                                       |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                     |
| html5lib       | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                      |
| sphinx         | 729 ms                                                 | 574 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                  | 1.24x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.39x faster                                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                       |
| async_tree_eager_io           | 1.01 sec                                               | 366 ms: 2.77x faster                                                       |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                                       |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.46x faster                                                       |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                       |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                       |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                      |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                       |
| Geometric mean                | (ref)                                                  | 2.08x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.8 ms: 1.62x faster                                                      |
| nbody          | 92.5 ms                                                | 64.5 ms: 1.44x faster                                                      |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.7 ms: 1.39x faster                                                      |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                       |
| regex_v8       | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                      |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.22x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                                       |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                     |
| pickle_pure_python   | 285 us                                                 | 197 us: 1.44x faster                                                       |
| xml_etree_process    | 44.6 ms                                                | 35.9 ms: 1.24x faster                                                      |
| json_dumps           | 8.31 ms                                                | 7.34 ms: 1.13x faster                                                      |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                       |
| xml_etree_generate   | 53.9 ms                                                | 51.1 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                      |
| json_loads           | 16.6 us                                                | 17.6 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.6 ms: 1.00x faster                                                      |
| python_startup_no_site | 12.8 ms                                                | 15.2 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.54 ms: 1.50x faster                                                      |
| genshi_text     | 17.7 ms                                                | 13.8 ms: 1.28x faster                                                      |
| genshi_xml      | 35.1 ms                                                | 28.9 ms: 1.21x faster                                                      |
| django_template | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                               |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.39x faster                                                      |
| typing_runtime_protocols      | 326 us                                                 | 91.9 us: 3.55x faster                                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                       |
| subparsers                    | 39.8 ms                                                | 12.0 ms: 3.31x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 366 ms: 2.77x faster                                                       |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                                       |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.46x faster                                                       |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                       |
| deltablue                     | 4.99 ms                                                | 2.16 ms: 2.31x faster                                                      |
| deepcopy_memo                 | 34.7 us                                                | 18.2 us: 1.91x faster                                                      |
| richards_super                | 61.0 ms                                                | 32.3 ms: 1.89x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                       |
| raytrace                      | 327 ms                                                 | 179 ms: 1.83x faster                                                       |
| deepcopy                      | 276 us                                                 | 151 us: 1.82x faster                                                       |
| richards                      | 52.3 ms                                                | 28.8 ms: 1.82x faster                                                      |
| logging_silent                | 117 ns                                                 | 64.8 ns: 1.81x faster                                                      |
| scimark_sor                   | 140 ms                                                 | 79.4 ms: 1.76x faster                                                      |
| go                            | 163 ms                                                 | 93.4 ms: 1.75x faster                                                      |
| chaos                         | 67.7 ms                                                | 39.3 ms: 1.72x faster                                                      |
| scimark_monte_carlo           | 72.4 ms                                                | 44.0 ms: 1.65x faster                                                      |
| float                         | 72.4 ms                                                | 44.8 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                       |
| spectral_norm                 | 95.3 ms                                                | 62.8 ms: 1.52x faster                                                      |
| mako                          | 9.81 ms                                                | 6.54 ms: 1.50x faster                                                      |
| html5lib                      | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                      |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                                       |
| deepcopy_reduce               | 2.32 us                                                | 1.58 us: 1.47x faster                                                      |
| pyflate                       | 448 ms                                                 | 307 ms: 1.46x faster                                                       |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                     |
| pickle_pure_python            | 285 us                                                 | 197 us: 1.44x faster                                                       |
| dulwich_log                   | 35.6 ms                                                | 24.7 ms: 1.44x faster                                                      |
| logging_simple                | 4.59 us                                                | 3.20 us: 1.44x faster                                                      |
| nbody                         | 92.5 ms                                                | 64.5 ms: 1.44x faster                                                      |
| logging_format                | 5.03 us                                                | 3.51 us: 1.43x faster                                                      |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                       |
| comprehensions                | 17.3 us                                                | 12.2 us: 1.42x faster                                                      |
| scimark_lu                    | 103 ms                                                 | 73.4 ms: 1.40x faster                                                      |
| regex_compile                 | 95.6 ms                                                | 68.7 ms: 1.39x faster                                                      |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.66 ms: 1.36x faster                                                      |
| hexiom                        | 6.25 ms                                                | 4.61 ms: 1.36x faster                                                      |
| generators                    | 31.7 ms                                                | 23.5 ms: 1.35x faster                                                      |
| crypto_pyaes                  | 73.3 ms                                                | 54.9 ms: 1.33x faster                                                      |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                     |
| pprint_pformat                | 1.33 sec                                               | 1.01 sec: 1.32x faster                                                     |
| pycparser                     | 887 ms                                                 | 673 ms: 1.32x faster                                                       |
| pprint_safe_repr              | 648 ms                                                 | 497 ms: 1.30x faster                                                       |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.0 ms: 1.28x faster                                                      |
| genshi_text                   | 17.7 ms                                                | 13.8 ms: 1.28x faster                                                      |
| thrift                        | 562 us                                                 | 439 us: 1.28x faster                                                       |
| sphinx                        | 729 ms                                                 | 574 ms: 1.27x faster                                                       |
| sympy_sum                     | 92.7 ms                                                | 73.9 ms: 1.25x faster                                                      |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                      |
| xml_etree_process             | 44.6 ms                                                | 35.9 ms: 1.24x faster                                                      |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                       |
| scimark_fft                   | 225 ms                                                 | 182 ms: 1.24x faster                                                       |
| regex_v8                      | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                      |
| genshi_xml                    | 35.1 ms                                                | 28.9 ms: 1.21x faster                                                      |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                     |
| sympy_str                     | 166 ms                                                 | 140 ms: 1.18x faster                                                       |
| bpe_tokeniser                 | 3.44 sec                                               | 2.96 sec: 1.16x faster                                                     |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                                      |
| django_template               | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.96 ms: 1.15x faster                                                      |
| json_dumps                    | 8.31 ms                                                | 7.34 ms: 1.13x faster                                                      |
| sympy_expand                  | 269 ms                                                 | 238 ms: 1.13x faster                                                       |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.12x faster                                                     |
| bench_thread_pool             | 545 us                                                 | 488 us: 1.12x faster                                                       |
| pathlib                       | 25.7 ms                                                | 23.3 ms: 1.11x faster                                                      |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                       |
| nqueens                       | 63.8 ms                                                | 59.2 ms: 1.08x faster                                                      |
| many_optionals                | 486 us                                                 | 451 us: 1.08x faster                                                       |
| fannkuch                      | 303 ms                                                 | 282 ms: 1.07x faster                                                       |
| connected_components          | 318 ms                                                 | 298 ms: 1.07x faster                                                       |
| xml_etree_generate            | 53.9 ms                                                | 51.1 ms: 1.06x faster                                                      |
| xml_etree_iterparse           | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                      |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                      |
| 2to3                          | 201 ms                                                 | 193 ms: 1.04x faster                                                       |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                       |
| meteor_contest                | 77.8 ms                                                | 75.7 ms: 1.03x faster                                                      |
| json                          | 3.10 ms                                                | 3.06 ms: 1.01x faster                                                      |
| python_startup                | 19.6 ms                                                | 19.6 ms: 1.00x faster                                                      |
| shortest_path                 | 328 ms                                                 | 330 ms: 1.01x slower                                                       |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                       |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.04x slower                                                      |
| json_loads                    | 16.6 us                                                | 17.6 us: 1.06x slower                                                      |
| bench_mp_pool                 | 56.0 ms                                                | 61.6 ms: 1.10x slower                                                      |
| create_gc_cycles              | 1.16 ms                                                | 1.30 ms: 1.12x slower                                                      |
| coverage                      | 41.2 ms                                                | 46.1 ms: 1.12x slower                                                      |
| gc_traversal                  | 2.71 ms                                                | 3.13 ms: 1.16x slower                                                      |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                       |
| python_startup_no_site        | 12.8 ms                                                | 15.2 ms: 1.19x slower                                                      |
| telco                         | 3.49 ms                                                | 4.52 ms: 1.29x slower                                                      |
| Geometric mean                | (ref)                                                  | 1.37x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250310-3.14.0a5+-460d0d3-JIT/bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.375x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.16x