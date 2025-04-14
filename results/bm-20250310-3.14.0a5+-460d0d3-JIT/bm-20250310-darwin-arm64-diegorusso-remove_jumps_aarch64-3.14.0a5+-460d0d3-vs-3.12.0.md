# Results vs. 3.12.0

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: darwin-arm64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 193 ms: 1.15x slower                                                       |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                     |
| html5lib       | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                      |
| sphinx         | 613 ms                                                 | 574 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 363 ms: 1.86x faster                                                       |
| async_tree_eager_io              | 666 ms                                                 | 366 ms: 1.82x faster                                                       |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                                       |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                       |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                       |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                       |
| coroutines                       | 19.7 ms                                                | 16.5 ms: 1.19x faster                                                      |
| async_generators                 | 299 ms                                                 | 275 ms: 1.08x faster                                                       |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                       |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 172 ms: 1.21x slower                                                       |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.73x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.8 ms: 1.21x faster                                                      |
| nbody          | 67.6 ms                                                | 64.5 ms: 1.05x faster                                                      |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 68.7 ms: 1.10x faster                                                      |
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                      |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                       |
| regex_v8       | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                     |
| xml_etree_generate   | 55.4 ms                                                | 51.1 ms: 1.09x faster                                                      |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.09x faster                                                       |
| xml_etree_process    | 38.9 ms                                                | 35.9 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                      |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.06x faster                                                       |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                      |
| json_dumps           | 6.19 ms                                                | 7.34 ms: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                      |
| python_startup_no_site | 13.2 ms                                                | 15.2 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.54 ms: 1.14x faster                                                      |
| genshi_text     | 14.7 ms                                                | 13.8 ms: 1.06x faster                                                      |
| genshi_xml      | 30.5 ms                                                | 28.9 ms: 1.05x faster                                                      |
| django_template | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.0 ms: 2.67x faster                                                      |
| async_tree_io_tg                 | 673 ms                                                 | 363 ms: 1.86x faster                                                       |
| async_tree_eager_io              | 666 ms                                                 | 366 ms: 1.82x faster                                                       |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                                       |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                       |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                       |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                       |
| deepcopy                         | 226 us                                                 | 151 us: 1.49x faster                                                       |
| deepcopy_memo                    | 26.0 us                                                | 18.2 us: 1.43x faster                                                      |
| deepcopy_reduce                  | 2.01 us                                                | 1.58 us: 1.27x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                       |
| generators                       | 29.4 ms                                                | 23.5 ms: 1.25x faster                                                      |
| spectral_norm                    | 76.5 ms                                                | 62.8 ms: 1.22x faster                                                      |
| float                            | 54.1 ms                                                | 44.8 ms: 1.21x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                       |
| coroutines                       | 19.7 ms                                                | 16.5 ms: 1.19x faster                                                      |
| deltablue                        | 2.57 ms                                                | 2.16 ms: 1.19x faster                                                      |
| dulwich_log                      | 29.2 ms                                                | 24.7 ms: 1.18x faster                                                      |
| comprehensions                   | 14.0 us                                                | 12.2 us: 1.15x faster                                                      |
| raytrace                         | 204 ms                                                 | 179 ms: 1.14x faster                                                       |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                     |
| mako                             | 7.44 ms                                                | 6.54 ms: 1.14x faster                                                      |
| html5lib                         | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                      |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                     |
| logging_simple                   | 3.60 us                                                | 3.20 us: 1.13x faster                                                      |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                       |
| logging_silent                   | 72.5 ns                                                | 64.8 ns: 1.12x faster                                                      |
| logging_format                   | 3.90 us                                                | 3.51 us: 1.11x faster                                                      |
| bpe_tokeniser                    | 3.28 sec                                               | 2.96 sec: 1.11x faster                                                     |
| regex_compile                    | 75.9 ms                                                | 68.7 ms: 1.10x faster                                                      |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                      |
| xml_etree_generate               | 55.4 ms                                                | 51.1 ms: 1.09x faster                                                      |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.09x faster                                                       |
| async_generators                 | 299 ms                                                 | 275 ms: 1.08x faster                                                       |
| xml_etree_process                | 38.9 ms                                                | 35.9 ms: 1.08x faster                                                      |
| scimark_sor                      | 85.8 ms                                                | 79.4 ms: 1.08x faster                                                      |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                                      |
| richards_super                   | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                      |
| scimark_fft                      | 194 ms                                                 | 182 ms: 1.07x faster                                                       |
| sphinx                           | 613 ms                                                 | 574 ms: 1.07x faster                                                       |
| xml_etree_iterparse              | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                      |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.06x faster                                                       |
| thrift                           | 468 us                                                 | 439 us: 1.06x faster                                                       |
| bench_mp_pool                    | 65.5 ms                                                | 61.6 ms: 1.06x faster                                                      |
| genshi_text                      | 14.7 ms                                                | 13.8 ms: 1.06x faster                                                      |
| pathlib                          | 24.7 ms                                                | 23.3 ms: 1.06x faster                                                      |
| richards                         | 30.6 ms                                                | 28.8 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.96 ms: 1.06x faster                                                      |
| chaos                            | 41.6 ms                                                | 39.3 ms: 1.06x faster                                                      |
| go                               | 98.5 ms                                                | 93.4 ms: 1.05x faster                                                      |
| genshi_xml                       | 30.5 ms                                                | 28.9 ms: 1.05x faster                                                      |
| sqlalchemy_declarative           | 61.9 ms                                                | 59.0 ms: 1.05x faster                                                      |
| nbody                            | 67.6 ms                                                | 64.5 ms: 1.05x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                       |
| sympy_sum                        | 76.2 ms                                                | 73.9 ms: 1.03x faster                                                      |
| sympy_str                        | 144 ms                                                 | 140 ms: 1.02x faster                                                       |
| dask                             | 779 ms                                                 | 767 ms: 1.01x faster                                                       |
| pyflate                          | 311 ms                                                 | 307 ms: 1.01x faster                                                       |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                       |
| scimark_monte_carlo              | 44.5 ms                                                | 44.0 ms: 1.01x faster                                                      |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                     |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                     |
| connected_components             | 300 ms                                                 | 298 ms: 1.01x faster                                                       |
| nqueens                          | 59.5 ms                                                | 59.2 ms: 1.01x faster                                                      |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                       |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.66 ms: 1.01x slower                                                      |
| bench_thread_pool                | 483 us                                                 | 488 us: 1.01x slower                                                       |
| json                             | 3.00 ms                                                | 3.06 ms: 1.02x slower                                                      |
| sympy_expand                     | 233 ms                                                 | 238 ms: 1.02x slower                                                       |
| pprint_pformat                   | 986 ms                                                 | 1.01 sec: 1.02x slower                                                     |
| sympy_integrate                  | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                      |
| pprint_safe_repr                 | 483 ms                                                 | 497 ms: 1.03x slower                                                       |
| regex_v8                         | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                      |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                      |
| hexiom                           | 4.38 ms                                                | 4.61 ms: 1.05x slower                                                      |
| gc_traversal                     | 2.95 ms                                                | 3.13 ms: 1.06x slower                                                      |
| django_template                  | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                      |
| crypto_pyaes                     | 51.4 ms                                                | 54.9 ms: 1.07x slower                                                      |
| meteor_contest                   | 69.1 ms                                                | 75.7 ms: 1.09x slower                                                      |
| python_startup                   | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                      |
| many_optionals                   | 403 us                                                 | 451 us: 1.12x slower                                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                       |
| fannkuch                         | 250 ms                                                 | 282 ms: 1.13x slower                                                       |
| create_gc_cycles                 | 1.15 ms                                                | 1.30 ms: 1.13x slower                                                      |
| 2to3                             | 168 ms                                                 | 193 ms: 1.15x slower                                                       |
| telco                            | 3.92 ms                                                | 4.52 ms: 1.15x slower                                                      |
| python_startup_no_site           | 13.2 ms                                                | 15.2 ms: 1.16x slower                                                      |
| json_dumps                       | 6.19 ms                                                | 7.34 ms: 1.19x slower                                                      |
| coverage                         | 38.5 ms                                                | 46.1 ms: 1.20x slower                                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 172 ms: 1.21x slower                                                       |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.73x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                               |

Benchmark hidden because not significant (7): shortest_path, scimark_lu, asyncio_websockets, sqlite_synth, pickle_pure_python, pycparser, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250310-3.14.0a5+-460d0d3-JIT/bm-20250310-darwin-arm64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x