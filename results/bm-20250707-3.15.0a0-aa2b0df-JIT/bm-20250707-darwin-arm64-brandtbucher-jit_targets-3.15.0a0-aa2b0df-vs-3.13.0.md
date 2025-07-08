# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_targets
- machine: darwin-arm64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 174 ms: 1.03x faster                                               |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                             |
| html5lib       | 36.7 ms                                                | 31.6 ms: 1.16x faster                                              |
| sphinx         | 602 ms                                                 | 586 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                               |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 193 ms: 1.39x faster                                               |
| async_tree_io                    | 508 ms                                                 | 374 ms: 1.36x faster                                               |
| async_tree_io_tg                 | 500 ms                                                 | 379 ms: 1.32x faster                                               |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.30x faster                                               |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                               |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.20x faster                                               |
| coroutines                       | 20.0 ms                                                | 17.1 ms: 1.17x faster                                              |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                               |
| async_tree_eager                 | 69.9 ms                                                | 64.1 ms: 1.09x faster                                              |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                               |
| async_generators                 | 294 ms                                                 | 280 ms: 1.05x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                               |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                               |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.9 ms: 1.12x faster                                              |
| nbody          | 73.6 ms                                                | 75.6 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.13x faster                                              |
| regex_compile  | 78.3 ms                                                | 71.2 ms: 1.10x faster                                              |
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.06x faster                                              |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                             |
| unpickle_pure_python | 165 us                                                 | 135 us: 1.23x faster                                               |
| xml_etree_process    | 41.3 ms                                                | 35.7 ms: 1.16x faster                                              |
| xml_etree_generate   | 57.1 ms                                                | 50.3 ms: 1.13x faster                                              |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                               |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                              |
| xml_etree_iterparse  | 74.2 ms                                                | 72.3 ms: 1.03x faster                                              |
| pickle_pure_python   | 215 us                                                 | 209 us: 1.02x faster                                               |
| json_dumps           | 6.47 ms                                                | 6.63 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.3 ms: 1.04x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.8 ms: 1.14x faster                                              |
| mako            | 7.75 ms                                                | 6.92 ms: 1.12x faster                                              |
| genshi_xml      | 34.1 ms                                                | 31.6 ms: 1.08x faster                                              |
| django_template | 20.5 ms                                                | 21.8 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 755 ms: 1.99x faster                                               |
| deepcopy                         | 236 us                                                 | 156 us: 1.51x faster                                               |
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                               |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                               |
| deepcopy_memo                    | 27.4 us                                                | 19.6 us: 1.40x faster                                              |
| async_tree_memoization           | 268 ms                                                 | 193 ms: 1.39x faster                                               |
| async_tree_io                    | 508 ms                                                 | 374 ms: 1.36x faster                                               |
| go                               | 117 ms                                                 | 87.3 ms: 1.34x faster                                              |
| generators                       | 31.9 ms                                                | 24.1 ms: 1.33x faster                                              |
| async_tree_io_tg                 | 500 ms                                                 | 379 ms: 1.32x faster                                               |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.30x faster                                               |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                               |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                               |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                             |
| deepcopy_reduce                  | 2.09 us                                                | 1.67 us: 1.26x faster                                              |
| unpickle_pure_python             | 165 us                                                 | 135 us: 1.23x faster                                               |
| pyflate                          | 352 ms                                                 | 288 ms: 1.22x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.20x faster                                               |
| scimark_sor                      | 106 ms                                                 | 89.0 ms: 1.19x faster                                              |
| coroutines                       | 20.0 ms                                                | 17.1 ms: 1.17x faster                                              |
| html5lib                         | 36.7 ms                                                | 31.6 ms: 1.16x faster                                              |
| xml_etree_process                | 41.3 ms                                                | 35.7 ms: 1.16x faster                                              |
| dulwich_log                      | 28.7 ms                                                | 25.1 ms: 1.14x faster                                              |
| genshi_text                      | 16.9 ms                                                | 14.8 ms: 1.14x faster                                              |
| spectral_norm                    | 76.5 ms                                                | 67.2 ms: 1.14x faster                                              |
| xml_etree_generate               | 57.1 ms                                                | 50.3 ms: 1.13x faster                                              |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.13x faster                                              |
| mako                             | 7.75 ms                                                | 6.92 ms: 1.12x faster                                              |
| float                            | 55.8 ms                                                | 49.9 ms: 1.12x faster                                              |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                               |
| regex_compile                    | 78.3 ms                                                | 71.2 ms: 1.10x faster                                              |
| scimark_monte_carlo              | 50.4 ms                                                | 45.9 ms: 1.10x faster                                              |
| async_tree_eager                 | 69.9 ms                                                | 64.1 ms: 1.09x faster                                              |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                               |
| genshi_xml                       | 34.1 ms                                                | 31.6 ms: 1.08x faster                                              |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                               |
| regex_v8                         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                              |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                             |
| json                             | 3.04 ms                                                | 2.88 ms: 1.06x faster                                              |
| bpe_tokeniser                    | 3.26 sec                                               | 3.08 sec: 1.06x faster                                             |
| telco                            | 4.84 ms                                                | 4.60 ms: 1.05x faster                                              |
| async_generators                 | 294 ms                                                 | 280 ms: 1.05x faster                                               |
| thrift                           | 466 us                                                 | 445 us: 1.05x faster                                               |
| chaos                            | 41.1 ms                                                | 39.3 ms: 1.04x faster                                              |
| pathlib                          | 23.2 ms                                                | 22.2 ms: 1.04x faster                                              |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                               |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                              |
| logging_simple                   | 3.56 us                                                | 3.43 us: 1.04x faster                                              |
| logging_format                   | 3.85 us                                                | 3.72 us: 1.03x faster                                              |
| typing_runtime_protocols         | 101 us                                                 | 97.3 us: 1.03x faster                                              |
| 2to3                             | 179 ms                                                 | 174 ms: 1.03x faster                                               |
| sphinx                           | 602 ms                                                 | 586 ms: 1.03x faster                                               |
| xml_etree_iterparse              | 74.2 ms                                                | 72.3 ms: 1.03x faster                                              |
| pprint_pformat                   | 1.10 sec                                               | 1.07 sec: 1.03x faster                                             |
| connected_components             | 319 ms                                                 | 311 ms: 1.02x faster                                               |
| pickle_pure_python               | 215 us                                                 | 209 us: 1.02x faster                                               |
| shortest_path                    | 345 ms                                                 | 338 ms: 1.02x faster                                               |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                              |
| hexiom                           | 4.87 ms                                                | 4.77 ms: 1.02x faster                                              |
| deltablue                        | 2.65 ms                                                | 2.60 ms: 1.02x faster                                              |
| sympy_expand                     | 248 ms                                                 | 243 ms: 1.02x faster                                               |
| pprint_safe_repr                 | 541 ms                                                 | 532 ms: 1.02x faster                                               |
| sympy_str                        | 146 ms                                                 | 144 ms: 1.01x faster                                               |
| raytrace                         | 181 ms                                                 | 179 ms: 1.01x faster                                               |
| richards                         | 36.2 ms                                                | 35.9 ms: 1.01x faster                                              |
| scimark_fft                      | 200 ms                                                 | 198 ms: 1.01x faster                                               |
| crypto_pyaes                     | 55.3 ms                                                | 55.8 ms: 1.01x slower                                              |
| pycparser                        | 701 ms                                                 | 708 ms: 1.01x slower                                               |
| logging_silent                   | 71.0 ns                                                | 72.1 ns: 1.02x slower                                              |
| comprehensions                   | 12.0 us                                                | 12.2 us: 1.02x slower                                              |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                             |
| json_dumps                       | 6.47 ms                                                | 6.63 ms: 1.03x slower                                              |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                              |
| nbody                            | 73.6 ms                                                | 75.6 ms: 1.03x slower                                              |
| richards_super                   | 39.2 ms                                                | 40.5 ms: 1.03x slower                                              |
| python_startup_no_site           | 13.7 ms                                                | 14.3 ms: 1.04x slower                                              |
| meteor_contest                   | 74.0 ms                                                | 77.8 ms: 1.05x slower                                              |
| coverage                         | 46.2 ms                                                | 48.7 ms: 1.05x slower                                              |
| django_template                  | 20.5 ms                                                | 21.8 ms: 1.06x slower                                              |
| scimark_lu                       | 75.9 ms                                                | 82.1 ms: 1.08x slower                                              |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                              |
| fannkuch                         | 279 ms                                                 | 306 ms: 1.10x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                               |
| create_gc_cycles                 | 1.19 ms                                                | 1.37 ms: 1.15x slower                                              |
| many_optionals                   | 409 us                                                 | 476 us: 1.17x slower                                               |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.54 ms: 1.19x slower                                              |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                               |
| subparsers                       | 9.44 ms                                                | 13.7 ms: 1.46x slower                                              |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (6): dask, nqueens, asyncio_websockets, python_startup, pidigits, sympy_sum
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x