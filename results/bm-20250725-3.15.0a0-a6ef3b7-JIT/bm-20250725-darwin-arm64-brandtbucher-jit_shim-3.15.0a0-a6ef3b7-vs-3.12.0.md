# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_shim
- machine: darwin-arm64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.062x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 202 ms: 1.20x slower                                            |
| docutils       | 1.45 sec                                               | 1.82 sec: 1.25x slower                                          |
| html5lib       | 33.4 ms                                                | 38.1 ms: 1.14x slower                                           |
| sphinx         | 613 ms                                                 | 690 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                  | 1.18x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 418 ms: 1.59x faster                                            |
| async_tree_io_tg                 | 673 ms                                                 | 431 ms: 1.56x faster                                            |
| async_tree_io                    | 672 ms                                                 | 433 ms: 1.55x faster                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 219 ms: 1.45x faster                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 432 ms: 1.43x faster                                            |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.42x faster                                            |
| async_tree_none_tg               | 255 ms                                                 | 181 ms: 1.41x faster                                            |
| async_tree_memoization           | 310 ms                                                 | 224 ms: 1.39x faster                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 458 ms: 1.15x faster                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 466 ms: 1.13x faster                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                            |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 394 ms: 1.05x slower                                            |
| async_generators                 | 299 ms                                                 | 316 ms: 1.06x slower                                            |
| async_tree_eager                 | 65.8 ms                                                | 71.4 ms: 1.09x slower                                           |
| asyncio_websockets               | 243 ms                                                 | 273 ms: 1.12x slower                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 435 ms: 1.25x slower                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 198 ms: 1.39x slower                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 148 ms: 3.16x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 54.1 ms                                                | 55.7 ms: 1.03x slower                                           |
| pidigits       | 283 ms                                                 | 310 ms: 1.10x slower                                            |
| nbody          | 67.6 ms                                                | 78.9 ms: 1.17x slower                                           |
| Geometric mean | (ref)                                                  | 1.10x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.35 ms: 1.04x faster                                           |
| regex_dna      | 143 ms                                                 | 152 ms: 1.06x slower                                            |
| regex_compile  | 75.9 ms                                                | 82.1 ms: 1.08x slower                                           |
| regex_v8       | 15.1 ms                                                | 17.0 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 143 us: 1.01x faster                                            |
| xml_etree_generate   | 55.4 ms                                                | 56.0 ms: 1.01x slower                                           |
| xml_etree_process    | 38.9 ms                                                | 39.3 ms: 1.01x slower                                           |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                            |
| tomli_loads          | 1.36 sec                                               | 1.39 sec: 1.02x slower                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 82.3 ms: 1.09x slower                                           |
| json_loads           | 17.0 us                                                | 19.2 us: 1.13x slower                                           |
| json_dumps           | 6.19 ms                                                | 7.25 ms: 1.17x slower                                           |
| pickle_pure_python   | 197 us                                                 | 233 us: 1.18x slower                                            |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.5 ms: 1.04x slower                                           |
| python_startup_no_site | 13.2 ms                                                | 14.0 ms: 1.07x slower                                           |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 7.15 ms: 1.04x faster                                           |
| genshi_text     | 14.7 ms                                                | 16.6 ms: 1.13x slower                                           |
| genshi_xml      | 30.5 ms                                                | 36.3 ms: 1.19x slower                                           |
| django_template | 19.7 ms                                                | 25.7 ms: 1.30x slower                                           |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 925 ms: 1.61x faster                                            |
| async_tree_eager_io              | 666 ms                                                 | 418 ms: 1.59x faster                                            |
| async_tree_io_tg                 | 673 ms                                                 | 431 ms: 1.56x faster                                            |
| async_tree_io                    | 672 ms                                                 | 433 ms: 1.55x faster                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 219 ms: 1.45x faster                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 432 ms: 1.43x faster                                            |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.42x faster                                            |
| async_tree_none_tg               | 255 ms                                                 | 181 ms: 1.41x faster                                            |
| async_tree_memoization           | 310 ms                                                 | 224 ms: 1.39x faster                                            |
| deepcopy                         | 226 us                                                 | 190 us: 1.19x faster                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 458 ms: 1.15x faster                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 466 ms: 1.13x faster                                            |
| comprehensions                   | 14.0 us                                                | 12.5 us: 1.12x faster                                           |
| spectral_norm                    | 76.5 ms                                                | 68.8 ms: 1.11x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                            |
| deepcopy_memo                    | 26.0 us                                                | 23.5 us: 1.11x faster                                           |
| subparsers                       | 32.1 ms                                                | 29.3 ms: 1.10x faster                                           |
| generators                       | 29.4 ms                                                | 26.8 ms: 1.09x faster                                           |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                           |
| raytrace                         | 204 ms                                                 | 193 ms: 1.05x faster                                            |
| mako                             | 7.44 ms                                                | 7.15 ms: 1.04x faster                                           |
| regex_effbot                     | 2.44 ms                                                | 2.35 ms: 1.04x faster                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.96 us: 1.03x faster                                           |
| go                               | 98.5 ms                                                | 95.8 ms: 1.03x faster                                           |
| unpickle_pure_python             | 145 us                                                 | 143 us: 1.01x faster                                            |
| dask                             | 779 ms                                                 | 787 ms: 1.01x slower                                            |
| xml_etree_generate               | 55.4 ms                                                | 56.0 ms: 1.01x slower                                           |
| xml_etree_process                | 38.9 ms                                                | 39.3 ms: 1.01x slower                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.32 sec: 1.01x slower                                          |
| pathlib                          | 24.7 ms                                                | 25.1 ms: 1.02x slower                                           |
| xml_etree_parse                  | 108 ms                                                 | 110 ms: 1.02x slower                                            |
| tomli_loads                      | 1.36 sec                                               | 1.39 sec: 1.02x slower                                          |
| chaos                            | 41.6 ms                                                | 42.7 ms: 1.03x slower                                           |
| pprint_pformat                   | 986 ms                                                 | 1.01 sec: 1.03x slower                                          |
| dulwich_log                      | 29.2 ms                                                | 30.1 ms: 1.03x slower                                           |
| float                            | 54.1 ms                                                | 55.7 ms: 1.03x slower                                           |
| pprint_safe_repr                 | 483 ms                                                 | 498 ms: 1.03x slower                                            |
| logging_simple                   | 3.60 us                                                | 3.73 us: 1.04x slower                                           |
| logging_format                   | 3.90 us                                                | 4.06 us: 1.04x slower                                           |
| python_startup                   | 17.8 ms                                                | 18.5 ms: 1.04x slower                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 394 ms: 1.05x slower                                            |
| async_generators                 | 299 ms                                                 | 316 ms: 1.06x slower                                            |
| regex_dna                        | 143 ms                                                 | 152 ms: 1.06x slower                                            |
| python_startup_no_site           | 13.2 ms                                                | 14.0 ms: 1.07x slower                                           |
| scimark_fft                      | 194 ms                                                 | 208 ms: 1.07x slower                                            |
| scimark_sor                      | 85.8 ms                                                | 92.0 ms: 1.07x slower                                           |
| pylint                           | 182 ms                                                 | 196 ms: 1.08x slower                                            |
| crypto_pyaes                     | 51.4 ms                                                | 55.4 ms: 1.08x slower                                           |
| regex_compile                    | 75.9 ms                                                | 82.1 ms: 1.08x slower                                           |
| async_tree_eager                 | 65.8 ms                                                | 71.4 ms: 1.09x slower                                           |
| deltablue                        | 2.57 ms                                                | 2.79 ms: 1.09x slower                                           |
| thrift                           | 468 us                                                 | 508 us: 1.09x slower                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 82.3 ms: 1.09x slower                                           |
| fannkuch                         | 250 ms                                                 | 274 ms: 1.09x slower                                            |
| pidigits                         | 283 ms                                                 | 310 ms: 1.10x slower                                            |
| pyflate                          | 311 ms                                                 | 342 ms: 1.10x slower                                            |
| scimark_monte_carlo              | 44.5 ms                                                | 49.1 ms: 1.11x slower                                           |
| scimark_lu                       | 73.5 ms                                                | 81.2 ms: 1.11x slower                                           |
| logging_silent                   | 72.5 ns                                                | 80.3 ns: 1.11x slower                                           |
| asyncio_websockets               | 243 ms                                                 | 273 ms: 1.12x slower                                            |
| sphinx                           | 613 ms                                                 | 690 ms: 1.13x slower                                            |
| nqueens                          | 59.5 ms                                                | 67.1 ms: 1.13x slower                                           |
| json_loads                       | 17.0 us                                                | 19.2 us: 1.13x slower                                           |
| regex_v8                         | 15.1 ms                                                | 17.0 ms: 1.13x slower                                           |
| sqlite_synth                     | 1.55 us                                                | 1.75 us: 1.13x slower                                           |
| json                             | 3.00 ms                                                | 3.40 ms: 1.13x slower                                           |
| genshi_text                      | 14.7 ms                                                | 16.6 ms: 1.13x slower                                           |
| html5lib                         | 33.4 ms                                                | 38.1 ms: 1.14x slower                                           |
| typing_runtime_protocols         | 91.5 us                                                | 105 us: 1.15x slower                                            |
| nbody                            | 67.6 ms                                                | 78.9 ms: 1.17x slower                                           |
| json_dumps                       | 6.19 ms                                                | 7.25 ms: 1.17x slower                                           |
| hexiom                           | 4.38 ms                                                | 5.14 ms: 1.17x slower                                           |
| pickle_pure_python               | 197 us                                                 | 233 us: 1.18x slower                                            |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.72 ms: 1.18x slower                                           |
| richards_super                   | 34.6 ms                                                | 41.0 ms: 1.19x slower                                           |
| genshi_xml                       | 30.5 ms                                                | 36.3 ms: 1.19x slower                                           |
| sympy_sum                        | 76.2 ms                                                | 91.1 ms: 1.19x slower                                           |
| sympy_str                        | 144 ms                                                 | 172 ms: 1.20x slower                                            |
| 2to3                             | 168 ms                                                 | 202 ms: 1.20x slower                                            |
| richards                         | 30.6 ms                                                | 36.7 ms: 1.20x slower                                           |
| meteor_contest                   | 69.1 ms                                                | 83.5 ms: 1.21x slower                                           |
| sympy_integrate                  | 11.1 ms                                                | 13.5 ms: 1.22x slower                                           |
| sympy_expand                     | 233 ms                                                 | 285 ms: 1.22x slower                                            |
| telco                            | 3.92 ms                                                | 4.84 ms: 1.24x slower                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 435 ms: 1.25x slower                                            |
| docutils                         | 1.45 sec                                               | 1.82 sec: 1.25x slower                                          |
| k_core                           | 1.72 sec                                               | 2.18 sec: 1.26x slower                                          |
| pycparser                        | 673 ms                                                 | 856 ms: 1.27x slower                                            |
| django_template                  | 19.7 ms                                                | 25.7 ms: 1.30x slower                                           |
| coverage                         | 38.5 ms                                                | 51.3 ms: 1.33x slower                                           |
| shortest_path                    | 331 ms                                                 | 452 ms: 1.37x slower                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 198 ms: 1.39x slower                                            |
| connected_components             | 300 ms                                                 | 419 ms: 1.40x slower                                            |
| gc_traversal                     | 2.95 ms                                                | 4.62 ms: 1.57x slower                                           |
| many_optionals                   | 403 us                                                 | 713 us: 1.77x slower                                            |
| create_gc_cycles                 | 1.15 ms                                                | 2.14 ms: 1.86x slower                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 148 ms: 3.16x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.07x slower                                                    |
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.062x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.18x