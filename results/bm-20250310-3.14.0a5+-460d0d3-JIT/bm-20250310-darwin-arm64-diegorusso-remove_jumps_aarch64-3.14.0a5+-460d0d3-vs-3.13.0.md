# Results vs. 3.13.0

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: darwin-arm64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 193 ms: 1.08x slower                                                       |
| html5lib       | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                      |
| sphinx         | 602 ms                                                 | 574 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.47x faster                                                       |
| async_tree_eager_io              | 511 ms                                                 | 366 ms: 1.40x faster                                                       |
| async_tree_io_tg                 | 500 ms                                                 | 363 ms: 1.38x faster                                                       |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.37x faster                                                       |
| async_tree_io                    | 508 ms                                                 | 378 ms: 1.34x faster                                                       |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                       |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                                       |
| async_tree_none_tg               | 198 ms                                                 | 155 ms: 1.28x faster                                                       |
| coroutines                       | 20.0 ms                                                | 16.5 ms: 1.21x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                       |
| async_generators                 | 294 ms                                                 | 275 ms: 1.07x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 172 ms: 1.25x slower                                                       |
| async_tree_eager_tg              | 47.4 ms                                                | 128 ms: 2.71x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.8 ms: 1.25x faster                                                      |
| nbody          | 73.6 ms                                                | 64.5 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.18x faster                                                      |
| regex_compile  | 78.3 ms                                                | 68.7 ms: 1.14x faster                                                      |
| regex_v8       | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                      |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                     |
| unpickle_pure_python | 165 us                                                 | 134 us: 1.23x faster                                                       |
| xml_etree_process    | 41.3 ms                                                | 35.9 ms: 1.15x faster                                                      |
| xml_etree_generate   | 57.1 ms                                                | 51.1 ms: 1.12x faster                                                      |
| pickle_pure_python   | 215 us                                                 | 197 us: 1.09x faster                                                       |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                      |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                      |
| json_dumps           | 6.47 ms                                                | 7.34 ms: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                      |
| python_startup_no_site | 13.7 ms                                                | 15.2 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.23x faster                                                      |
| mako            | 7.75 ms                                                | 6.54 ms: 1.18x faster                                                      |
| genshi_xml      | 34.1 ms                                                | 28.9 ms: 1.18x faster                                                      |
| django_template | 20.5 ms                                                | 21.0 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 151 us: 1.56x faster                                                       |
| deepcopy_memo                    | 27.4 us                                                | 18.2 us: 1.51x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.47x faster                                                       |
| async_tree_eager_io              | 511 ms                                                 | 366 ms: 1.40x faster                                                       |
| async_tree_io_tg                 | 500 ms                                                 | 363 ms: 1.38x faster                                                       |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.37x faster                                                       |
| generators                       | 31.9 ms                                                | 23.5 ms: 1.36x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 378 ms: 1.34x faster                                                       |
| scimark_sor                      | 106 ms                                                 | 79.4 ms: 1.33x faster                                                      |
| deepcopy_reduce                  | 2.09 us                                                | 1.58 us: 1.33x faster                                                      |
| tomli_loads                      | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                       |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                                       |
| async_tree_none_tg               | 198 ms                                                 | 155 ms: 1.28x faster                                                       |
| richards                         | 36.2 ms                                                | 28.8 ms: 1.26x faster                                                      |
| go                               | 117 ms                                                 | 93.4 ms: 1.25x faster                                                      |
| html5lib                         | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                      |
| float                            | 55.8 ms                                                | 44.8 ms: 1.25x faster                                                      |
| unpickle_pure_python             | 165 us                                                 | 134 us: 1.23x faster                                                       |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.23x faster                                                      |
| deltablue                        | 2.65 ms                                                | 2.16 ms: 1.22x faster                                                      |
| spectral_norm                    | 76.5 ms                                                | 62.8 ms: 1.22x faster                                                      |
| richards_super                   | 39.2 ms                                                | 32.3 ms: 1.22x faster                                                      |
| coroutines                       | 20.0 ms                                                | 16.5 ms: 1.21x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| mako                             | 7.75 ms                                                | 6.54 ms: 1.18x faster                                                      |
| genshi_xml                       | 34.1 ms                                                | 28.9 ms: 1.18x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.18x faster                                                      |
| dulwich_log                      | 28.7 ms                                                | 24.7 ms: 1.16x faster                                                      |
| xml_etree_process                | 41.3 ms                                                | 35.9 ms: 1.15x faster                                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 44.0 ms: 1.15x faster                                                      |
| pyflate                          | 352 ms                                                 | 307 ms: 1.15x faster                                                       |
| nbody                            | 73.6 ms                                                | 64.5 ms: 1.14x faster                                                      |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                                      |
| regex_compile                    | 78.3 ms                                                | 68.7 ms: 1.14x faster                                                      |
| xml_etree_generate               | 57.1 ms                                                | 51.1 ms: 1.12x faster                                                      |
| logging_simple                   | 3.56 us                                                | 3.20 us: 1.11x faster                                                      |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                       |
| bpe_tokeniser                    | 3.26 sec                                               | 2.96 sec: 1.10x faster                                                     |
| logging_format                   | 3.85 us                                                | 3.51 us: 1.10x faster                                                      |
| scimark_fft                      | 200 ms                                                 | 182 ms: 1.10x faster                                                       |
| typing_runtime_protocols         | 101 us                                                 | 91.9 us: 1.10x faster                                                      |
| logging_silent                   | 71.0 ns                                                | 64.8 ns: 1.10x faster                                                      |
| pprint_pformat                   | 1.10 sec                                               | 1.01 sec: 1.09x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                      |
| pickle_pure_python               | 215 us                                                 | 197 us: 1.09x faster                                                       |
| pprint_safe_repr                 | 541 ms                                                 | 497 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                       |
| telco                            | 4.84 ms                                                | 4.52 ms: 1.07x faster                                                      |
| connected_components             | 319 ms                                                 | 298 ms: 1.07x faster                                                       |
| async_generators                 | 294 ms                                                 | 275 ms: 1.07x faster                                                       |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.06x faster                                                       |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                     |
| thrift                           | 466 us                                                 | 439 us: 1.06x faster                                                       |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                       |
| hexiom                           | 4.87 ms                                                | 4.61 ms: 1.06x faster                                                      |
| bench_mp_pool                    | 64.7 ms                                                | 61.6 ms: 1.05x faster                                                      |
| sphinx                           | 602 ms                                                 | 574 ms: 1.05x faster                                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                      |
| shortest_path                    | 345 ms                                                 | 330 ms: 1.05x faster                                                       |
| nqueens                          | 61.8 ms                                                | 59.2 ms: 1.04x faster                                                      |
| chaos                            | 41.1 ms                                                | 39.3 ms: 1.04x faster                                                      |
| pycparser                        | 701 ms                                                 | 673 ms: 1.04x faster                                                       |
| sympy_expand                     | 248 ms                                                 | 238 ms: 1.04x faster                                                       |
| sympy_str                        | 146 ms                                                 | 140 ms: 1.04x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                       |
| scimark_lu                       | 75.9 ms                                                | 73.4 ms: 1.03x faster                                                      |
| bench_thread_pool                | 503 us                                                 | 488 us: 1.03x faster                                                       |
| sympy_sum                        | 75.1 ms                                                | 73.9 ms: 1.02x faster                                                      |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.02x faster                                                     |
| raytrace                         | 181 ms                                                 | 179 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.96 ms: 1.01x faster                                                      |
| crypto_pyaes                     | 55.3 ms                                                | 54.9 ms: 1.01x faster                                                      |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.01x faster                                                      |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                       |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.66 ms: 1.00x faster                                                      |
| fannkuch                         | 279 ms                                                 | 282 ms: 1.01x slower                                                       |
| comprehensions                   | 12.0 us                                                | 12.2 us: 1.02x slower                                                      |
| meteor_contest                   | 74.0 ms                                                | 75.7 ms: 1.02x slower                                                      |
| django_template                  | 20.5 ms                                                | 21.0 ms: 1.03x slower                                                      |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                      |
| python_startup                   | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                      |
| gc_traversal                     | 2.94 ms                                                | 3.13 ms: 1.07x slower                                                      |
| 2to3                             | 179 ms                                                 | 193 ms: 1.08x slower                                                       |
| create_gc_cycles                 | 1.19 ms                                                | 1.30 ms: 1.09x slower                                                      |
| many_optionals                   | 409 us                                                 | 451 us: 1.10x slower                                                       |
| python_startup_no_site           | 13.7 ms                                                | 15.2 ms: 1.11x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                       |
| json_dumps                       | 6.47 ms                                                | 7.34 ms: 1.13x slower                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 172 ms: 1.25x slower                                                       |
| subparsers                       | 9.44 ms                                                | 12.0 ms: 1.27x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 128 ms: 2.71x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                               |

Benchmark hidden because not significant (8): docutils, coverage, asyncio_websockets, pidigits, sqlalchemy_declarative, sympy_integrate, pathlib, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250310-3.14.0a5+-460d0d3-JIT/bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x