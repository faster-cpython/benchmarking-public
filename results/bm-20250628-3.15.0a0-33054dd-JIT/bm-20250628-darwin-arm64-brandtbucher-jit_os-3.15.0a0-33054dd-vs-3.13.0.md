# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_os
- machine: darwin-arm64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 174 ms: 1.03x faster                                          |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                        |
| html5lib       | 36.7 ms                                                | 31.7 ms: 1.16x faster                                         |
| sphinx         | 602 ms                                                 | 587 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                          |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.42x faster                                          |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                          |
| async_tree_io                    | 508 ms                                                 | 376 ms: 1.35x faster                                          |
| async_tree_io_tg                 | 500 ms                                                 | 379 ms: 1.32x faster                                          |
| async_tree_none                  | 212 ms                                                 | 162 ms: 1.30x faster                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                          |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.20x faster                                          |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                          |
| async_tree_eager                 | 69.9 ms                                                | 64.5 ms: 1.08x faster                                         |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.9 ms: 1.12x faster                                         |
| nbody          | 73.6 ms                                                | 75.7 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                         |
| regex_compile  | 78.3 ms                                                | 71.4 ms: 1.10x faster                                         |
| regex_v8       | 17.0 ms                                                | 16.1 ms: 1.05x faster                                         |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                        |
| unpickle_pure_python | 165 us                                                 | 134 us: 1.23x faster                                          |
| xml_etree_process    | 41.3 ms                                                | 35.8 ms: 1.15x faster                                         |
| xml_etree_generate   | 57.1 ms                                                | 51.0 ms: 1.12x faster                                         |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                          |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                         |
| xml_etree_iterparse  | 74.2 ms                                                | 72.3 ms: 1.03x faster                                         |
| pickle_pure_python   | 215 us                                                 | 211 us: 1.02x faster                                          |
| json_dumps           | 6.47 ms                                                | 6.57 ms: 1.02x slower                                         |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.7 ms: 1.00x faster                                         |
| python_startup_no_site | 13.7 ms                                                | 14.2 ms: 1.03x slower                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.9 ms: 1.14x faster                                         |
| mako            | 7.75 ms                                                | 6.99 ms: 1.11x faster                                         |
| genshi_xml      | 34.1 ms                                                | 31.3 ms: 1.09x faster                                         |
| django_template | 20.5 ms                                                | 22.0 ms: 1.07x slower                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 759 ms: 1.97x faster                                          |
| deepcopy                         | 236 us                                                 | 156 us: 1.52x faster                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                          |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.42x faster                                          |
| deepcopy_memo                    | 27.4 us                                                | 19.5 us: 1.40x faster                                         |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                          |
| async_tree_io                    | 508 ms                                                 | 376 ms: 1.35x faster                                          |
| generators                       | 31.9 ms                                                | 24.1 ms: 1.33x faster                                         |
| go                               | 117 ms                                                 | 88.1 ms: 1.32x faster                                         |
| async_tree_io_tg                 | 500 ms                                                 | 379 ms: 1.32x faster                                          |
| async_tree_none                  | 212 ms                                                 | 162 ms: 1.30x faster                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                          |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                          |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                        |
| deepcopy_reduce                  | 2.09 us                                                | 1.67 us: 1.25x faster                                         |
| unpickle_pure_python             | 165 us                                                 | 134 us: 1.23x faster                                          |
| pyflate                          | 352 ms                                                 | 292 ms: 1.20x faster                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.20x faster                                          |
| scimark_sor                      | 106 ms                                                 | 88.9 ms: 1.19x faster                                         |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                         |
| html5lib                         | 36.7 ms                                                | 31.7 ms: 1.16x faster                                         |
| xml_etree_process                | 41.3 ms                                                | 35.8 ms: 1.15x faster                                         |
| dulwich_log                      | 28.7 ms                                                | 25.0 ms: 1.15x faster                                         |
| genshi_text                      | 16.9 ms                                                | 14.9 ms: 1.14x faster                                         |
| spectral_norm                    | 76.5 ms                                                | 67.8 ms: 1.13x faster                                         |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                         |
| xml_etree_generate               | 57.1 ms                                                | 51.0 ms: 1.12x faster                                         |
| float                            | 55.8 ms                                                | 49.9 ms: 1.12x faster                                         |
| mako                             | 7.75 ms                                                | 6.99 ms: 1.11x faster                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                          |
| pylint                           | 180 ms                                                 | 163 ms: 1.10x faster                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 46.0 ms: 1.10x faster                                         |
| regex_compile                    | 78.3 ms                                                | 71.4 ms: 1.10x faster                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                          |
| genshi_xml                       | 34.1 ms                                                | 31.3 ms: 1.09x faster                                         |
| async_tree_eager                 | 69.9 ms                                                | 64.5 ms: 1.08x faster                                         |
| telco                            | 4.84 ms                                                | 4.55 ms: 1.06x faster                                         |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                          |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.05x faster                                        |
| regex_v8                         | 17.0 ms                                                | 16.1 ms: 1.05x faster                                         |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                          |
| thrift                           | 466 us                                                 | 443 us: 1.05x faster                                          |
| bpe_tokeniser                    | 3.26 sec                                               | 3.10 sec: 1.05x faster                                        |
| json                             | 3.04 ms                                                | 2.91 ms: 1.05x faster                                         |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                          |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                          |
| chaos                            | 41.1 ms                                                | 39.7 ms: 1.03x faster                                         |
| pathlib                          | 23.2 ms                                                | 22.5 ms: 1.03x faster                                         |
| connected_components             | 319 ms                                                 | 310 ms: 1.03x faster                                          |
| typing_runtime_protocols         | 101 us                                                 | 98.0 us: 1.03x faster                                         |
| shortest_path                    | 345 ms                                                 | 337 ms: 1.03x faster                                          |
| logging_simple                   | 3.56 us                                                | 3.47 us: 1.03x faster                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 72.3 ms: 1.03x faster                                         |
| 2to3                             | 179 ms                                                 | 174 ms: 1.03x faster                                          |
| sphinx                           | 602 ms                                                 | 587 ms: 1.03x faster                                          |
| hexiom                           | 4.87 ms                                                | 4.75 ms: 1.02x faster                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                         |
| pickle_pure_python               | 215 us                                                 | 211 us: 1.02x faster                                          |
| logging_format                   | 3.85 us                                                | 3.79 us: 1.02x faster                                         |
| sympy_expand                     | 248 ms                                                 | 245 ms: 1.01x faster                                          |
| sympy_str                        | 146 ms                                                 | 144 ms: 1.01x faster                                          |
| raytrace                         | 181 ms                                                 | 179 ms: 1.01x faster                                          |
| scimark_fft                      | 200 ms                                                 | 198 ms: 1.01x faster                                          |
| pprint_safe_repr                 | 541 ms                                                 | 537 ms: 1.01x faster                                          |
| dask                             | 771 ms                                                 | 766 ms: 1.01x faster                                          |
| python_startup                   | 18.8 ms                                                | 18.7 ms: 1.00x faster                                         |
| deltablue                        | 2.65 ms                                                | 2.67 ms: 1.01x slower                                         |
| richards                         | 36.2 ms                                                | 36.5 ms: 1.01x slower                                         |
| sympy_sum                        | 75.1 ms                                                | 76.0 ms: 1.01x slower                                         |
| pycparser                        | 701 ms                                                 | 710 ms: 1.01x slower                                          |
| crypto_pyaes                     | 55.3 ms                                                | 56.1 ms: 1.01x slower                                         |
| json_dumps                       | 6.47 ms                                                | 6.57 ms: 1.02x slower                                         |
| logging_silent                   | 71.0 ns                                                | 72.3 ns: 1.02x slower                                         |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.02x slower                                         |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                        |
| comprehensions                   | 12.0 us                                                | 12.2 us: 1.02x slower                                         |
| nbody                            | 73.6 ms                                                | 75.7 ms: 1.03x slower                                         |
| python_startup_no_site           | 13.7 ms                                                | 14.2 ms: 1.03x slower                                         |
| meteor_contest                   | 74.0 ms                                                | 76.5 ms: 1.03x slower                                         |
| coverage                         | 46.2 ms                                                | 47.9 ms: 1.04x slower                                         |
| richards_super                   | 39.2 ms                                                | 41.2 ms: 1.05x slower                                         |
| fannkuch                         | 279 ms                                                 | 299 ms: 1.07x slower                                          |
| django_template                  | 20.5 ms                                                | 22.0 ms: 1.07x slower                                         |
| scimark_lu                       | 75.9 ms                                                | 82.8 ms: 1.09x slower                                         |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                         |
| many_optionals                   | 409 us                                                 | 481 us: 1.18x slower                                          |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.51 ms: 1.18x slower                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                          |
| subparsers                       | 9.44 ms                                                | 13.8 ms: 1.46x slower                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                  |

Benchmark hidden because not significant (4): asyncio_websockets, nqueens, pidigits, pprint_pformat
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x