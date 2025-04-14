# Results vs. 3.12.0

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: darwin-arm64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.088x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 161 ms: 1.05x faster                                                          |
| docutils       | 1.45 sec                                               | 1.43 sec: 1.01x faster                                                        |
| html5lib       | 33.4 ms                                                | 29.7 ms: 1.12x faster                                                         |
| sphinx         | 613 ms                                                 | 579 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 361 ms: 1.86x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 375 ms: 1.79x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.68x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.63x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 191 ms: 1.62x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                          |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                         |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                          |
| async_tree_eager                 | 65.8 ms                                                | 62.8 ms: 1.05x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                          |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                          |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.24x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.0 ms: 1.15x faster                                                         |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| nbody          | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.6 ms: 1.12x faster                                                         |
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                         |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                          |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                        |
| xml_etree_iterparse  | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                         |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                          |
| xml_etree_generate   | 55.4 ms                                                | 54.8 ms: 1.01x faster                                                         |
| xml_etree_process    | 38.9 ms                                                | 38.6 ms: 1.01x faster                                                         |
| unpickle_pure_python | 145 us                                                 | 149 us: 1.03x slower                                                          |
| pickle_pure_python   | 197 us                                                 | 205 us: 1.04x slower                                                          |
| json_loads           | 17.0 us                                                | 18.1 us: 1.06x slower                                                         |
| json_dumps           | 6.19 ms                                                | 7.48 ms: 1.21x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                         |
| python_startup_no_site | 13.2 ms                                                | 13.0 ms: 1.02x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.8 ms: 1.06x faster                                                         |
| genshi_xml      | 30.5 ms                                                | 28.8 ms: 1.06x faster                                                         |
| mako            | 7.44 ms                                                | 7.62 ms: 1.02x slower                                                         |
| django_template | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.3 ms: 2.61x faster                                                         |
| mdp                              | 1.49 sec                                               | 765 ms: 1.95x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 361 ms: 1.86x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 375 ms: 1.79x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.68x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.63x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 191 ms: 1.62x faster                                                          |
| deepcopy                         | 226 us                                                 | 153 us: 1.48x faster                                                          |
| deepcopy_memo                    | 26.0 us                                                | 18.2 us: 1.43x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                          |
| generators                       | 29.4 ms                                                | 23.4 ms: 1.25x faster                                                         |
| deepcopy_reduce                  | 2.01 us                                                | 1.62 us: 1.24x faster                                                         |
| go                               | 98.5 ms                                                | 79.9 ms: 1.23x faster                                                         |
| comprehensions                   | 14.0 us                                                | 11.5 us: 1.22x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                          |
| dulwich_log                      | 29.2 ms                                                | 24.5 ms: 1.19x faster                                                         |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                         |
| raytrace                         | 204 ms                                                 | 172 ms: 1.18x faster                                                          |
| float                            | 54.1 ms                                                | 47.0 ms: 1.15x faster                                                         |
| regex_compile                    | 75.9 ms                                                | 67.6 ms: 1.12x faster                                                         |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                          |
| html5lib                         | 33.4 ms                                                | 29.7 ms: 1.12x faster                                                         |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.12x faster                                                        |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                          |
| logging_simple                   | 3.60 us                                                | 3.22 us: 1.12x faster                                                         |
| tomli_loads                      | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                        |
| spectral_norm                    | 76.5 ms                                                | 68.9 ms: 1.11x faster                                                         |
| bench_mp_pool                    | 65.5 ms                                                | 59.3 ms: 1.10x faster                                                         |
| logging_format                   | 3.90 us                                                | 3.54 us: 1.10x faster                                                         |
| chaos                            | 41.6 ms                                                | 38.0 ms: 1.09x faster                                                         |
| deltablue                        | 2.57 ms                                                | 2.35 ms: 1.09x faster                                                         |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                         |
| logging_silent                   | 72.5 ns                                                | 67.1 ns: 1.08x faster                                                         |
| bpe_tokeniser                    | 3.28 sec                                               | 3.04 sec: 1.08x faster                                                        |
| scimark_sor                      | 85.8 ms                                                | 79.5 ms: 1.08x faster                                                         |
| pyflate                          | 311 ms                                                 | 291 ms: 1.07x faster                                                          |
| scimark_fft                      | 194 ms                                                 | 183 ms: 1.06x faster                                                          |
| genshi_text                      | 14.7 ms                                                | 13.8 ms: 1.06x faster                                                         |
| sphinx                           | 613 ms                                                 | 579 ms: 1.06x faster                                                          |
| genshi_xml                       | 30.5 ms                                                | 28.8 ms: 1.06x faster                                                         |
| scimark_monte_carlo              | 44.5 ms                                                | 42.2 ms: 1.05x faster                                                         |
| xml_etree_iterparse              | 75.5 ms                                                | 71.8 ms: 1.05x faster                                                         |
| 2to3                             | 168 ms                                                 | 161 ms: 1.05x faster                                                          |
| async_tree_eager                 | 65.8 ms                                                | 62.8 ms: 1.05x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                          |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                          |
| python_startup                   | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                         |
| sqlalchemy_declarative           | 61.9 ms                                                | 59.9 ms: 1.03x faster                                                         |
| pathlib                          | 24.7 ms                                                | 24.0 ms: 1.03x faster                                                         |
| pycparser                        | 673 ms                                                 | 656 ms: 1.03x faster                                                          |
| sympy_integrate                  | 11.1 ms                                                | 10.8 ms: 1.02x faster                                                         |
| python_startup_no_site           | 13.2 ms                                                | 13.0 ms: 1.02x faster                                                         |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                          |
| docutils                         | 1.45 sec                                               | 1.43 sec: 1.01x faster                                                        |
| sympy_sum                        | 76.2 ms                                                | 75.1 ms: 1.01x faster                                                         |
| sympy_str                        | 144 ms                                                 | 142 ms: 1.01x faster                                                          |
| xml_etree_generate               | 55.4 ms                                                | 54.8 ms: 1.01x faster                                                         |
| hexiom                           | 4.38 ms                                                | 4.34 ms: 1.01x faster                                                         |
| xml_etree_process                | 38.9 ms                                                | 38.6 ms: 1.01x faster                                                         |
| nqueens                          | 59.5 ms                                                | 59.3 ms: 1.00x faster                                                         |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.57 ms: 1.00x faster                                                         |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| pprint_safe_repr                 | 483 ms                                                 | 487 ms: 1.01x slower                                                          |
| scimark_lu                       | 73.5 ms                                                | 74.2 ms: 1.01x slower                                                         |
| connected_components             | 300 ms                                                 | 303 ms: 1.01x slower                                                          |
| mako                             | 7.44 ms                                                | 7.62 ms: 1.02x slower                                                         |
| bench_thread_pool                | 483 us                                                 | 495 us: 1.03x slower                                                          |
| unpickle_pure_python             | 145 us                                                 | 149 us: 1.03x slower                                                          |
| typing_runtime_protocols         | 91.5 us                                                | 93.9 us: 1.03x slower                                                         |
| json                             | 3.00 ms                                                | 3.09 ms: 1.03x slower                                                         |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                         |
| sympy_expand                     | 233 ms                                                 | 241 ms: 1.03x slower                                                          |
| pickle_pure_python               | 197 us                                                 | 205 us: 1.04x slower                                                          |
| meteor_contest                   | 69.1 ms                                                | 72.1 ms: 1.04x slower                                                         |
| fannkuch                         | 250 ms                                                 | 262 ms: 1.05x slower                                                          |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                         |
| richards_super                   | 34.6 ms                                                | 36.5 ms: 1.05x slower                                                         |
| nbody                            | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                         |
| richards                         | 30.6 ms                                                | 32.5 ms: 1.06x slower                                                         |
| json_loads                       | 17.0 us                                                | 18.1 us: 1.06x slower                                                         |
| django_template                  | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                         |
| crypto_pyaes                     | 51.4 ms                                                | 55.6 ms: 1.08x slower                                                         |
| many_optionals                   | 403 us                                                 | 446 us: 1.11x slower                                                          |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.12x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                          |
| telco                            | 3.92 ms                                                | 4.70 ms: 1.20x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                                          |
| json_dumps                       | 6.19 ms                                                | 7.48 ms: 1.21x slower                                                         |
| coverage                         | 38.5 ms                                                | 47.0 ms: 1.22x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                                  |

Benchmark hidden because not significant (4): sqlite_synth, scimark_sparse_mat_mult, pprint_pformat, shortest_path
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-darwin-arm64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.088x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x