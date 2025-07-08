# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_targets
- machine: darwin-arm64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.059x faster
- HPT reliability: 95.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 174 ms: 1.03x slower                                               |
| docutils       | 1.45 sec                                               | 1.47 sec: 1.01x slower                                             |
| html5lib       | 33.4 ms                                                | 31.6 ms: 1.05x faster                                              |
| sphinx         | 613 ms                                                 | 586 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                               |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.79x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 379 ms: 1.78x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                               |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.62x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 193 ms: 1.60x faster                                               |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                              |
| async_generators                 | 299 ms                                                 | 280 ms: 1.07x faster                                               |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                               |
| async_tree_eager                 | 65.8 ms                                                | 64.1 ms: 1.03x faster                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.75x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.9 ms: 1.08x faster                                              |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| nbody          | 67.6 ms                                                | 75.6 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.2 ms: 1.07x faster                                              |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                              |
| regex_v8       | 15.1 ms                                                | 16.0 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 55.4 ms                                                | 50.3 ms: 1.10x faster                                              |
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.09x faster                                             |
| xml_etree_process    | 38.9 ms                                                | 35.7 ms: 1.09x faster                                              |
| unpickle_pure_python | 145 us                                                 | 135 us: 1.08x faster                                               |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 75.5 ms                                                | 72.3 ms: 1.04x faster                                              |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                              |
| pickle_pure_python   | 197 us                                                 | 209 us: 1.06x slower                                               |
| json_dumps           | 6.19 ms                                                | 6.63 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.8 ms: 1.06x slower                                              |
| python_startup_no_site | 13.2 ms                                                | 14.3 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.92 ms: 1.08x faster                                              |
| genshi_text     | 14.7 ms                                                | 14.8 ms: 1.01x slower                                              |
| genshi_xml      | 30.5 ms                                                | 31.6 ms: 1.03x slower                                              |
| django_template | 19.7 ms                                                | 21.8 ms: 1.11x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.34x faster                                              |
| mdp                              | 1.49 sec                                               | 755 ms: 1.98x faster                                               |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                               |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.79x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 379 ms: 1.78x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                               |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.62x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 193 ms: 1.60x faster                                               |
| deepcopy                         | 226 us                                                 | 156 us: 1.45x faster                                               |
| deepcopy_memo                    | 26.0 us                                                | 19.6 us: 1.33x faster                                              |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                               |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                              |
| deepcopy_reduce                  | 2.01 us                                                | 1.67 us: 1.21x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| dulwich_log                      | 29.2 ms                                                | 25.1 ms: 1.16x faster                                              |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                              |
| comprehensions                   | 14.0 us                                                | 12.2 us: 1.15x faster                                              |
| raytrace                         | 204 ms                                                 | 179 ms: 1.14x faster                                               |
| spectral_norm                    | 76.5 ms                                                | 67.2 ms: 1.14x faster                                              |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                             |
| go                               | 98.5 ms                                                | 87.3 ms: 1.13x faster                                              |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                               |
| pathlib                          | 24.7 ms                                                | 22.2 ms: 1.11x faster                                              |
| xml_etree_generate               | 55.4 ms                                                | 50.3 ms: 1.10x faster                                              |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.09x faster                                             |
| xml_etree_process                | 38.9 ms                                                | 35.7 ms: 1.09x faster                                              |
| float                            | 54.1 ms                                                | 49.9 ms: 1.08x faster                                              |
| unpickle_pure_python             | 145 us                                                 | 135 us: 1.08x faster                                               |
| pyflate                          | 311 ms                                                 | 288 ms: 1.08x faster                                               |
| mako                             | 7.44 ms                                                | 6.92 ms: 1.08x faster                                              |
| async_generators                 | 299 ms                                                 | 280 ms: 1.07x faster                                               |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                               |
| regex_compile                    | 75.9 ms                                                | 71.2 ms: 1.07x faster                                              |
| bpe_tokeniser                    | 3.28 sec                                               | 3.08 sec: 1.06x faster                                             |
| chaos                            | 41.6 ms                                                | 39.3 ms: 1.06x faster                                              |
| html5lib                         | 33.4 ms                                                | 31.6 ms: 1.05x faster                                              |
| logging_simple                   | 3.60 us                                                | 3.43 us: 1.05x faster                                              |
| thrift                           | 468 us                                                 | 445 us: 1.05x faster                                               |
| logging_format                   | 3.90 us                                                | 3.72 us: 1.05x faster                                              |
| sphinx                           | 613 ms                                                 | 586 ms: 1.05x faster                                               |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                              |
| xml_etree_iterparse              | 75.5 ms                                                | 72.3 ms: 1.04x faster                                              |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                               |
| json                             | 3.00 ms                                                | 2.88 ms: 1.04x faster                                              |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                              |
| async_tree_eager                 | 65.8 ms                                                | 64.1 ms: 1.03x faster                                              |
| sympy_sum                        | 76.2 ms                                                | 75.3 ms: 1.01x faster                                              |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                               |
| logging_silent                   | 72.5 ns                                                | 72.1 ns: 1.01x faster                                              |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| genshi_text                      | 14.7 ms                                                | 14.8 ms: 1.01x slower                                              |
| docutils                         | 1.45 sec                                               | 1.47 sec: 1.01x slower                                             |
| deltablue                        | 2.57 ms                                                | 2.60 ms: 1.01x slower                                              |
| scimark_fft                      | 194 ms                                                 | 198 ms: 1.02x slower                                               |
| shortest_path                    | 331 ms                                                 | 338 ms: 1.02x slower                                               |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                              |
| 2to3                             | 168 ms                                                 | 174 ms: 1.03x slower                                               |
| scimark_monte_carlo              | 44.5 ms                                                | 45.9 ms: 1.03x slower                                              |
| genshi_xml                       | 30.5 ms                                                | 31.6 ms: 1.03x slower                                              |
| nqueens                          | 59.5 ms                                                | 61.7 ms: 1.04x slower                                              |
| scimark_sor                      | 85.8 ms                                                | 89.0 ms: 1.04x slower                                              |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                               |
| sympy_expand                     | 233 ms                                                 | 243 ms: 1.04x slower                                               |
| pycparser                        | 673 ms                                                 | 708 ms: 1.05x slower                                               |
| python_startup                   | 17.8 ms                                                | 18.8 ms: 1.06x slower                                              |
| typing_runtime_protocols         | 91.5 us                                                | 97.3 us: 1.06x slower                                              |
| pickle_pure_python               | 197 us                                                 | 209 us: 1.06x slower                                               |
| regex_v8                         | 15.1 ms                                                | 16.0 ms: 1.06x slower                                              |
| json_dumps                       | 6.19 ms                                                | 6.63 ms: 1.07x slower                                              |
| python_startup_no_site           | 13.2 ms                                                | 14.3 ms: 1.08x slower                                              |
| crypto_pyaes                     | 51.4 ms                                                | 55.8 ms: 1.08x slower                                              |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.09x slower                                              |
| pprint_pformat                   | 986 ms                                                 | 1.07 sec: 1.09x slower                                             |
| hexiom                           | 4.38 ms                                                | 4.77 ms: 1.09x slower                                              |
| pprint_safe_repr                 | 483 ms                                                 | 532 ms: 1.10x slower                                               |
| django_template                  | 19.7 ms                                                | 21.8 ms: 1.11x slower                                              |
| scimark_lu                       | 73.5 ms                                                | 82.1 ms: 1.12x slower                                              |
| nbody                            | 67.6 ms                                                | 75.6 ms: 1.12x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                               |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.54 ms: 1.12x slower                                              |
| meteor_contest                   | 69.1 ms                                                | 77.8 ms: 1.13x slower                                              |
| richards_super                   | 34.6 ms                                                | 40.5 ms: 1.17x slower                                              |
| richards                         | 30.6 ms                                                | 35.9 ms: 1.17x slower                                              |
| telco                            | 3.92 ms                                                | 4.60 ms: 1.17x slower                                              |
| many_optionals                   | 403 us                                                 | 476 us: 1.18x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                               |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                              |
| fannkuch                         | 250 ms                                                 | 306 ms: 1.22x slower                                               |
| coverage                         | 38.5 ms                                                | 48.7 ms: 1.26x slower                                              |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.75x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (4): asyncio_websockets, sympy_str, sympy_integrate, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 95.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x