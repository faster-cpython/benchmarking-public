# Results vs. 3.12.0

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: e5eacd1
- commit date: 2025-05-21
- overall geometric mean: 1.011x faster
- HPT reliability: 99.21%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 169 ms: 1.00x slower                                               |
| html5lib       | 33.4 ms                                                | 30.8 ms: 1.08x faster                                              |
| sphinx         | 613 ms                                                 | 581 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 352 ms: 1.89x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                               |
| async_tree_io                    | 672 ms                                                 | 373 ms: 1.80x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.71x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 150 ms: 1.70x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 363 ms: 1.70x faster                                               |
| async_tree_none                  | 263 ms                                                 | 156 ms: 1.68x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 186 ms: 1.67x faster                                               |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 405 ms: 1.30x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 409 ms: 1.29x faster                                               |
| coroutines                       | 19.7 ms                                                | 16.2 ms: 1.22x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.21x faster                                               |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                              |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                               |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 354 ms: 1.06x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 164 ms: 1.16x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.26x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.1 ms: 1.26x faster                                              |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                               |
| nbody          | 67.6 ms                                                | 75.5 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.2 ms: 1.13x faster                                              |
| regex_effbot   | 2.44 ms                                                | 2.26 ms: 1.08x faster                                              |
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                               |
| regex_v8       | 15.1 ms                                                | 15.8 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.21 sec: 1.12x faster                                             |
| xml_etree_process    | 38.9 ms                                                | 35.5 ms: 1.09x faster                                              |
| xml_etree_generate   | 55.4 ms                                                | 51.1 ms: 1.08x faster                                              |
| unpickle_pure_python | 145 us                                                 | 135 us: 1.07x faster                                               |
| xml_etree_iterparse  | 75.5 ms                                                | 71.5 ms: 1.06x faster                                              |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                               |
| pickle_pure_python   | 197 us                                                 | 198 us: 1.01x slower                                               |
| json_dumps           | 6.19 ms                                                | 6.60 ms: 1.07x slower                                              |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.1 ms: 1.08x slower                                              |
| python_startup_no_site | 13.2 ms                                                | 14.6 ms: 1.11x slower                                              |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.77 ms: 1.10x faster                                              |
| genshi_text     | 14.7 ms                                                | 13.7 ms: 1.07x faster                                              |
| genshi_xml      | 30.5 ms                                                | 28.9 ms: 1.05x faster                                              |
| django_template | 19.7 ms                                                | 20.8 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.3 ms: 2.41x faster                                              |
| mdp                              | 1.49 sec                                               | 757 ms: 1.97x faster                                               |
| async_tree_eager_io              | 666 ms                                                 | 352 ms: 1.89x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                               |
| async_tree_io                    | 672 ms                                                 | 373 ms: 1.80x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.71x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 150 ms: 1.70x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 363 ms: 1.70x faster                                               |
| async_tree_none                  | 263 ms                                                 | 156 ms: 1.68x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 186 ms: 1.67x faster                                               |
| deepcopy                         | 226 us                                                 | 149 us: 1.51x faster                                               |
| deepcopy_memo                    | 26.0 us                                                | 17.5 us: 1.48x faster                                              |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 405 ms: 1.30x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 409 ms: 1.29x faster                                               |
| generators                       | 29.4 ms                                                | 23.1 ms: 1.27x faster                                              |
| float                            | 54.1 ms                                                | 43.1 ms: 1.26x faster                                              |
| deepcopy_reduce                  | 2.01 us                                                | 1.61 us: 1.25x faster                                              |
| go                               | 98.5 ms                                                | 79.2 ms: 1.24x faster                                              |
| coroutines                       | 19.7 ms                                                | 16.2 ms: 1.22x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.21x faster                                               |
| raytrace                         | 204 ms                                                 | 170 ms: 1.20x faster                                               |
| dulwich_log                      | 29.2 ms                                                | 24.6 ms: 1.19x faster                                              |
| regex_compile                    | 75.9 ms                                                | 67.2 ms: 1.13x faster                                              |
| tomli_loads                      | 1.36 sec                                               | 1.21 sec: 1.12x faster                                             |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                               |
| comprehensions                   | 14.0 us                                                | 12.6 us: 1.11x faster                                              |
| scimark_sor                      | 85.8 ms                                                | 77.5 ms: 1.11x faster                                              |
| spectral_norm                    | 76.5 ms                                                | 69.1 ms: 1.11x faster                                              |
| chaos                            | 41.6 ms                                                | 37.7 ms: 1.10x faster                                              |
| mako                             | 7.44 ms                                                | 6.77 ms: 1.10x faster                                              |
| xml_etree_process                | 38.9 ms                                                | 35.5 ms: 1.09x faster                                              |
| html5lib                         | 33.4 ms                                                | 30.8 ms: 1.08x faster                                              |
| xml_etree_generate               | 55.4 ms                                                | 51.1 ms: 1.08x faster                                              |
| regex_effbot                     | 2.44 ms                                                | 2.26 ms: 1.08x faster                                              |
| k_core                           | 1.72 sec                                               | 1.60 sec: 1.08x faster                                             |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                              |
| unpickle_pure_python             | 145 us                                                 | 135 us: 1.07x faster                                               |
| genshi_text                      | 14.7 ms                                                | 13.7 ms: 1.07x faster                                              |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                               |
| pyflate                          | 311 ms                                                 | 291 ms: 1.07x faster                                               |
| bpe_tokeniser                    | 3.28 sec                                               | 3.09 sec: 1.06x faster                                             |
| pathlib                          | 24.7 ms                                                | 23.4 ms: 1.06x faster                                              |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 354 ms: 1.06x faster                                               |
| deltablue                        | 2.57 ms                                                | 2.43 ms: 1.06x faster                                              |
| xml_etree_iterparse              | 75.5 ms                                                | 71.5 ms: 1.06x faster                                              |
| sphinx                           | 613 ms                                                 | 581 ms: 1.05x faster                                               |
| genshi_xml                       | 30.5 ms                                                | 28.9 ms: 1.05x faster                                              |
| scimark_monte_carlo              | 44.5 ms                                                | 42.3 ms: 1.05x faster                                              |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                               |
| logging_simple                   | 3.60 us                                                | 3.46 us: 1.04x faster                                              |
| sympy_str                        | 144 ms                                                 | 139 ms: 1.04x faster                                               |
| sympy_sum                        | 76.2 ms                                                | 73.6 ms: 1.04x faster                                              |
| logging_format                   | 3.90 us                                                | 3.77 us: 1.03x faster                                              |
| sympy_integrate                  | 11.1 ms                                                | 10.7 ms: 1.03x faster                                              |
| hexiom                           | 4.38 ms                                                | 4.28 ms: 1.02x faster                                              |
| nqueens                          | 59.5 ms                                                | 59.4 ms: 1.00x faster                                              |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                               |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                               |
| 2to3                             | 168 ms                                                 | 169 ms: 1.00x slower                                               |
| pickle_pure_python               | 197 us                                                 | 198 us: 1.01x slower                                               |
| json                             | 3.00 ms                                                | 3.03 ms: 1.01x slower                                              |
| sympy_expand                     | 233 ms                                                 | 236 ms: 1.01x slower                                               |
| scimark_lu                       | 73.5 ms                                                | 74.4 ms: 1.01x slower                                              |
| pycparser                        | 673 ms                                                 | 685 ms: 1.02x slower                                               |
| richards_super                   | 34.6 ms                                                | 35.9 ms: 1.04x slower                                              |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.04x slower                                              |
| dask                             | 779 ms                                                 | 814 ms: 1.04x slower                                               |
| richards                         | 30.6 ms                                                | 32.0 ms: 1.05x slower                                              |
| regex_v8                         | 15.1 ms                                                | 15.8 ms: 1.05x slower                                              |
| django_template                  | 19.7 ms                                                | 20.8 ms: 1.06x slower                                              |
| shortest_path                    | 331 ms                                                 | 350 ms: 1.06x slower                                               |
| connected_components             | 300 ms                                                 | 319 ms: 1.06x slower                                               |
| scimark_fft                      | 194 ms                                                 | 207 ms: 1.06x slower                                               |
| json_dumps                       | 6.19 ms                                                | 6.60 ms: 1.07x slower                                              |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                              |
| python_startup                   | 17.8 ms                                                | 19.1 ms: 1.08x slower                                              |
| crypto_pyaes                     | 51.4 ms                                                | 55.6 ms: 1.08x slower                                              |
| bench_mp_pool                    | 65.5 ms                                                | 71.0 ms: 1.08x slower                                              |
| typing_runtime_protocols         | 91.5 us                                                | 99.5 us: 1.09x slower                                              |
| gc_traversal                     | 2.95 ms                                                | 3.21 ms: 1.09x slower                                              |
| pprint_pformat                   | 986 ms                                                 | 1.08 sec: 1.10x slower                                             |
| pprint_safe_repr                 | 483 ms                                                 | 533 ms: 1.10x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                               |
| python_startup_no_site           | 13.2 ms                                                | 14.6 ms: 1.11x slower                                              |
| nbody                            | 67.6 ms                                                | 75.5 ms: 1.12x slower                                              |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.54 ms: 1.13x slower                                              |
| meteor_contest                   | 69.1 ms                                                | 78.2 ms: 1.13x slower                                              |
| many_optionals                   | 403 us                                                 | 463 us: 1.15x slower                                               |
| telco                            | 3.92 ms                                                | 4.54 ms: 1.16x slower                                              |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 164 ms: 1.16x slower                                               |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                              |
| fannkuch                         | 250 ms                                                 | 312 ms: 1.25x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                               |
| logging_silent                   | 72.5 ns                                                | 321 ns: 4.43x slower                                               |
| coverage                         | 38.5 ms                                                | 269 ms: 6.99x slower                                               |
| thrift                           | 468 us                                                 | 43.4 ms: 92.72x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (3): asyncio_websockets, docutils, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250521-3.15.0a0-e5eacd1-JIT/bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 99.21% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x