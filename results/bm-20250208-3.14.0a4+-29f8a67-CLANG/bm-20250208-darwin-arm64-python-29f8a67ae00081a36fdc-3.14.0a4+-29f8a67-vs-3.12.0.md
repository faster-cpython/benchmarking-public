# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 186 ms: 1.11x slower                                                   |
| docutils       | 1.45 sec                                               | 1.42 sec: 1.02x faster                                                 |
| html5lib       | 33.4 ms                                                | 28.7 ms: 1.16x faster                                                  |
| sphinx         | 613 ms                                                 | 538 ms: 1.14x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 334 ms: 2.00x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 338 ms: 1.98x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 341 ms: 1.97x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.77x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 350 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 185 ms: 1.72x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 402 ms: 1.31x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.29x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| async_generators                 | 299 ms                                                 | 248 ms: 1.21x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.2 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 348 ms: 1.08x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 165 ms: 1.16x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 122 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.6 ms: 1.24x faster                                                  |
| nbody          | 67.6 ms                                                | 61.9 ms: 1.09x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 61.9 ms: 1.23x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 146 ms: 1.02x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.8 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 124 us: 1.17x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 48.3 ms: 1.15x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.1 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 181 us: 1.09x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 99.8 ms: 1.08x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.09 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.3 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.4 ms: 1.18x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 26.2 ms: 1.16x faster                                                  |
| mako            | 7.44 ms                                                | 6.92 ms: 1.08x faster                                                  |
| django_template | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.3 ms: 2.85x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 334 ms: 2.00x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 338 ms: 1.98x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 341 ms: 1.97x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.77x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 350 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 185 ms: 1.72x faster                                                   |
| generators                       | 29.4 ms                                                | 17.1 ms: 1.71x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.70x faster                                                   |
| deepcopy                         | 226 us                                                 | 139 us: 1.63x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.2 us: 1.61x faster                                                  |
| go                               | 98.5 ms                                                | 70.5 ms: 1.40x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.50 us: 1.34x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.5 us: 1.33x faster                                                  |
| raytrace                         | 204 ms                                                 | 155 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 58.2 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 402 ms: 1.31x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.29x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.02 ms: 1.27x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 57.9 ns: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| logging_simple                   | 3.60 us                                                | 2.89 us: 1.25x faster                                                  |
| float                            | 54.1 ms                                                | 43.6 ms: 1.24x faster                                                  |
| pylint                           | 182 ms                                                 | 147 ms: 1.23x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 61.9 ms: 1.23x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.19 us: 1.22x faster                                                  |
| async_generators                 | 299 ms                                                 | 248 ms: 1.21x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.75 sec: 1.20x faster                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.64 ms: 1.19x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.0 ms: 1.19x faster                                                  |
| sqlglot_parse                    | 808 us                                                 | 681 us: 1.19x faster                                                   |
| genshi_text                      | 14.7 ms                                                | 12.4 ms: 1.18x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| nqueens                          | 59.5 ms                                                | 50.5 ms: 1.18x faster                                                  |
| sqlglot_transpile                | 973 us                                                 | 826 us: 1.18x faster                                                   |
| unpickle_pure_python             | 145 us                                                 | 124 us: 1.17x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 73.5 ms: 1.17x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 26.2 ms: 1.16x faster                                                  |
| html5lib                         | 33.4 ms                                                | 28.7 ms: 1.16x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 168 ms: 1.15x faster                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 38.6 ms: 1.15x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.81 ms: 1.15x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 48.3 ms: 1.15x faster                                                  |
| pyflate                          | 311 ms                                                 | 271 ms: 1.15x faster                                                   |
| thrift                           | 468 us                                                 | 408 us: 1.14x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 34.1 ms: 1.14x faster                                                  |
| sphinx                           | 613 ms                                                 | 538 ms: 1.14x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 54.5 ms: 1.14x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 58.2 ms: 1.13x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 874 ms: 1.13x faster                                                   |
| sympy_str                        | 144 ms                                                 | 128 ms: 1.12x faster                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 431 ms: 1.12x faster                                                   |
| richards_super                   | 34.6 ms                                                | 31.0 ms: 1.12x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 65.9 ms: 1.11x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 68.4 ms: 1.11x faster                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 29.8 ms: 1.11x faster                                                  |
| richards                         | 30.6 ms                                                | 27.5 ms: 1.11x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.4 ms: 1.11x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 59.4 ms: 1.10x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.5 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 47.1 ms: 1.09x faster                                                  |
| sqlglot_normalize                | 180 ms                                                 | 164 ms: 1.09x faster                                                   |
| pycparser                        | 673 ms                                                 | 616 ms: 1.09x faster                                                   |
| nbody                            | 67.6 ms                                                | 61.9 ms: 1.09x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 215 ms: 1.09x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 181 us: 1.09x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 99.8 ms: 1.08x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.13 ms: 1.08x faster                                                  |
| mako                             | 7.44 ms                                                | 6.92 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 348 ms: 1.08x faster                                                   |
| bench_thread_pool                | 483 us                                                 | 454 us: 1.06x faster                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 87.1 us: 1.05x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.04x faster                                                 |
| django_template                  | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.03x faster                                                  |
| shortest_path                    | 331 ms                                                 | 323 ms: 1.02x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.42 sec: 1.02x faster                                                 |
| connected_components             | 300 ms                                                 | 295 ms: 1.02x faster                                                   |
| fannkuch                         | 250 ms                                                 | 246 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| meteor_contest                   | 69.1 ms                                                | 68.9 ms: 1.00x faster                                                  |
| many_optionals                   | 403 us                                                 | 411 us: 1.02x slower                                                   |
| regex_dna                        | 143 ms                                                 | 146 ms: 1.02x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.08 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.3 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.09x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| 2to3                             | 168 ms                                                 | 186 ms: 1.11x slower                                                   |
| telco                            | 3.92 ms                                                | 4.44 ms: 1.13x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.09 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 165 ms: 1.16x slower                                                   |
| coverage                         | 38.5 ms                                                | 45.4 ms: 1.18x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.8 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 122 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.07x