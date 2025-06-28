# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_nops
- machine: darwin-arm64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.060x faster
- HPT reliability: 94.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 173 ms: 1.03x slower                                            |
| docutils       | 1.45 sec                                               | 1.47 sec: 1.01x slower                                          |
| html5lib       | 33.4 ms                                                | 31.7 ms: 1.05x faster                                           |
| sphinx         | 613 ms                                                 | 587 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                            |
| async_tree_io                    | 672 ms                                                 | 373 ms: 1.80x faster                                            |
| async_tree_io_tg                 | 673 ms                                                 | 380 ms: 1.77x faster                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                            |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                            |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.62x faster                                            |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                           |
| async_generators                 | 299 ms                                                 | 277 ms: 1.08x faster                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                            |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.74x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.8 ms: 1.09x faster                                           |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                            |
| nbody          | 67.6 ms                                                | 75.4 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.5 ms: 1.06x faster                                           |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                           |
| regex_v8       | 15.1 ms                                                | 16.1 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_process    | 38.9 ms                                                | 35.5 ms: 1.09x faster                                           |
| xml_etree_generate   | 55.4 ms                                                | 50.7 ms: 1.09x faster                                           |
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.09x faster                                          |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.08x faster                                            |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                            |
| xml_etree_iterparse  | 75.5 ms                                                | 72.3 ms: 1.04x faster                                           |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                           |
| json_dumps           | 6.19 ms                                                | 6.56 ms: 1.06x slower                                           |
| pickle_pure_python   | 197 us                                                 | 210 us: 1.07x slower                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.3 ms: 1.03x slower                                           |
| python_startup_no_site | 13.2 ms                                                | 13.8 ms: 1.04x slower                                           |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.93 ms: 1.07x faster                                           |
| genshi_text     | 14.7 ms                                                | 14.8 ms: 1.01x slower                                           |
| genshi_xml      | 30.5 ms                                                | 31.3 ms: 1.02x slower                                           |
| django_template | 19.7 ms                                                | 21.9 ms: 1.11x slower                                           |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.9 ms: 2.32x faster                                           |
| mdp                              | 1.49 sec                                               | 758 ms: 1.97x faster                                            |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                            |
| async_tree_io                    | 672 ms                                                 | 373 ms: 1.80x faster                                            |
| async_tree_io_tg                 | 673 ms                                                 | 380 ms: 1.77x faster                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                            |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                            |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.62x faster                                            |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                            |
| deepcopy                         | 226 us                                                 | 156 us: 1.45x faster                                            |
| deepcopy_memo                    | 26.0 us                                                | 19.5 us: 1.33x faster                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                            |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.67 us: 1.20x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| dulwich_log                      | 29.2 ms                                                | 25.0 ms: 1.17x faster                                           |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                           |
| comprehensions                   | 14.0 us                                                | 12.1 us: 1.15x faster                                           |
| raytrace                         | 204 ms                                                 | 179 ms: 1.14x faster                                            |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                          |
| spectral_norm                    | 76.5 ms                                                | 67.8 ms: 1.13x faster                                           |
| go                               | 98.5 ms                                                | 87.4 ms: 1.13x faster                                           |
| pylint                           | 182 ms                                                 | 163 ms: 1.12x faster                                            |
| pathlib                          | 24.7 ms                                                | 22.2 ms: 1.11x faster                                           |
| xml_etree_process                | 38.9 ms                                                | 35.5 ms: 1.09x faster                                           |
| xml_etree_generate               | 55.4 ms                                                | 50.7 ms: 1.09x faster                                           |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.09x faster                                          |
| float                            | 54.1 ms                                                | 49.8 ms: 1.09x faster                                           |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.08x faster                                            |
| async_generators                 | 299 ms                                                 | 277 ms: 1.08x faster                                            |
| mako                             | 7.44 ms                                                | 6.93 ms: 1.07x faster                                           |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                            |
| pyflate                          | 311 ms                                                 | 292 ms: 1.07x faster                                            |
| bpe_tokeniser                    | 3.28 sec                                               | 3.09 sec: 1.06x faster                                          |
| regex_compile                    | 75.9 ms                                                | 71.5 ms: 1.06x faster                                           |
| chaos                            | 41.6 ms                                                | 39.2 ms: 1.06x faster                                           |
| thrift                           | 468 us                                                 | 442 us: 1.06x faster                                            |
| html5lib                         | 33.4 ms                                                | 31.7 ms: 1.05x faster                                           |
| sphinx                           | 613 ms                                                 | 587 ms: 1.04x faster                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 72.3 ms: 1.04x faster                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                            |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                           |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                           |
| logging_format                   | 3.90 us                                                | 3.77 us: 1.04x faster                                           |
| logging_simple                   | 3.60 us                                                | 3.48 us: 1.04x faster                                           |
| json                             | 3.00 ms                                                | 2.91 ms: 1.03x faster                                           |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                           |
| dask                             | 779 ms                                                 | 767 ms: 1.02x faster                                            |
| sympy_sum                        | 76.2 ms                                                | 75.4 ms: 1.01x faster                                           |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.00x faster                                           |
| logging_silent                   | 72.5 ns                                                | 72.3 ns: 1.00x faster                                           |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                            |
| docutils                         | 1.45 sec                                               | 1.47 sec: 1.01x slower                                          |
| genshi_text                      | 14.7 ms                                                | 14.8 ms: 1.01x slower                                           |
| shortest_path                    | 331 ms                                                 | 338 ms: 1.02x slower                                            |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                           |
| genshi_xml                       | 30.5 ms                                                | 31.3 ms: 1.02x slower                                           |
| python_startup                   | 17.8 ms                                                | 18.3 ms: 1.03x slower                                           |
| 2to3                             | 168 ms                                                 | 173 ms: 1.03x slower                                            |
| scimark_fft                      | 194 ms                                                 | 200 ms: 1.03x slower                                            |
| scimark_monte_carlo              | 44.5 ms                                                | 46.0 ms: 1.03x slower                                           |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                            |
| scimark_sor                      | 85.8 ms                                                | 89.0 ms: 1.04x slower                                           |
| nqueens                          | 59.5 ms                                                | 61.9 ms: 1.04x slower                                           |
| deltablue                        | 2.57 ms                                                | 2.67 ms: 1.04x slower                                           |
| python_startup_no_site           | 13.2 ms                                                | 13.8 ms: 1.04x slower                                           |
| sympy_expand                     | 233 ms                                                 | 244 ms: 1.05x slower                                            |
| pycparser                        | 673 ms                                                 | 709 ms: 1.05x slower                                            |
| json_dumps                       | 6.19 ms                                                | 6.56 ms: 1.06x slower                                           |
| typing_runtime_protocols         | 91.5 us                                                | 97.6 us: 1.07x slower                                           |
| pickle_pure_python               | 197 us                                                 | 210 us: 1.07x slower                                            |
| regex_v8                         | 15.1 ms                                                | 16.1 ms: 1.07x slower                                           |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                           |
| pprint_pformat                   | 986 ms                                                 | 1.07 sec: 1.09x slower                                          |
| crypto_pyaes                     | 51.4 ms                                                | 56.0 ms: 1.09x slower                                           |
| hexiom                           | 4.38 ms                                                | 4.77 ms: 1.09x slower                                           |
| pprint_safe_repr                 | 483 ms                                                 | 527 ms: 1.09x slower                                            |
| meteor_contest                   | 69.1 ms                                                | 76.1 ms: 1.10x slower                                           |
| django_template                  | 19.7 ms                                                | 21.9 ms: 1.11x slower                                           |
| nbody                            | 67.6 ms                                                | 75.4 ms: 1.12x slower                                           |
| scimark_lu                       | 73.5 ms                                                | 82.3 ms: 1.12x slower                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                            |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.55 ms: 1.13x slower                                           |
| telco                            | 3.92 ms                                                | 4.55 ms: 1.16x slower                                           |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                            |
| richards_super                   | 34.6 ms                                                | 41.2 ms: 1.19x slower                                           |
| many_optionals                   | 403 us                                                 | 479 us: 1.19x slower                                            |
| richards                         | 30.6 ms                                                | 36.5 ms: 1.19x slower                                           |
| fannkuch                         | 250 ms                                                 | 299 ms: 1.20x slower                                            |
| coverage                         | 38.5 ms                                                | 48.0 ms: 1.25x slower                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.74x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                    |

Benchmark hidden because not significant (3): sympy_str, asyncio_websockets, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-darwin-arm64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 94.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x