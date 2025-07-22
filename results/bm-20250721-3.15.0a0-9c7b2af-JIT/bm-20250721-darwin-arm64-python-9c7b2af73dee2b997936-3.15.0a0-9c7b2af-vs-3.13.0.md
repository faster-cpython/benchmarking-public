# Results vs. 3.13.0

- fork: python
- ref: 9c7b2af73dee2b997936
- machine: darwin-arm64
- commit hash: 9c7b2af
- commit date: 2025-07-21
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 169 ms: 1.06x faster                                                  |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                |
| html5lib       | 36.7 ms                                                | 32.8 ms: 1.12x faster                                                 |
| sphinx         | 602 ms                                                 | 573 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.50x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 368 ms: 1.36x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 370 ms: 1.30x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 165 ms: 1.29x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 418 ms: 1.10x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 63.9 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 284 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                 |
| nbody          | 73.6 ms                                                | 72.4 ms: 1.02x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.16 ms: 1.22x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| regex_compile  | 78.3 ms                                                | 72.3 ms: 1.08x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 127 us: 1.30x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.22 sec: 1.29x faster                                                |
| xml_etree_process    | 41.3 ms                                                | 34.3 ms: 1.20x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 49.3 ms: 1.16x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 206 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.6 ms: 1.02x faster                                                 |
| json_dumps           | 6.47 ms                                                | 6.55 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.2 ms: 1.09x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.9 ms: 1.06x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.57 ms: 1.18x faster                                                 |
| genshi_text     | 16.9 ms                                                | 15.3 ms: 1.11x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.0 ms: 1.03x faster                                                 |
| django_template | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 744 ms: 2.01x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.50x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                                  |
| deepcopy                         | 236 us                                                 | 172 us: 1.38x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 368 ms: 1.36x faster                                                  |
| go                               | 117 ms                                                 | 86.0 ms: 1.36x faster                                                 |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                  |
| generators                       | 31.9 ms                                                | 24.5 ms: 1.30x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 127 us: 1.30x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 370 ms: 1.30x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.22 sec: 1.29x faster                                                |
| async_tree_none                  | 212 ms                                                 | 165 ms: 1.29x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 21.5 us: 1.27x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 83.2 ms: 1.27x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                  |
| pyflate                          | 352 ms                                                 | 283 ms: 1.24x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.16 ms: 1.22x faster                                                 |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 63.4 ms: 1.21x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 34.3 ms: 1.20x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 457 ms: 1.18x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 931 ms: 1.18x faster                                                  |
| mako                             | 7.75 ms                                                | 6.57 ms: 1.18x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.18x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 49.3 ms: 1.16x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 25.0 ms: 1.15x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 2.90 sec: 1.12x faster                                                |
| fannkuch                         | 279 ms                                                 | 249 ms: 1.12x faster                                                  |
| html5lib                         | 36.7 ms                                                | 32.8 ms: 1.12x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 45.2 ms: 1.12x faster                                                 |
| pylint                           | 180 ms                                                 | 161 ms: 1.12x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.6 ms: 1.12x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.3 ms: 1.11x faster                                                 |
| telco                            | 4.84 ms                                                | 4.39 ms: 1.10x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.40 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 418 ms: 1.10x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 63.9 ms: 1.10x faster                                                 |
| python_startup                   | 18.8 ms                                                | 17.2 ms: 1.09x faster                                                 |
| float                            | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                 |
| richards                         | 36.2 ms                                                | 33.3 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 72.3 ms: 1.08x faster                                                 |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.53 ms: 1.07x faster                                                 |
| comprehensions                   | 12.0 us                                                | 11.2 us: 1.07x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 94.1 us: 1.07x faster                                                 |
| chaos                            | 41.1 ms                                                | 38.4 ms: 1.07x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 12.9 ms: 1.06x faster                                                 |
| logging_simple                   | 3.56 us                                                | 3.36 us: 1.06x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 188 ms: 1.06x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.64 us: 1.06x faster                                                 |
| 2to3                             | 179 ms                                                 | 169 ms: 1.06x faster                                                  |
| raytrace                         | 181 ms                                                 | 172 ms: 1.05x faster                                                  |
| sphinx                           | 602 ms                                                 | 573 ms: 1.05x faster                                                  |
| richards_super                   | 39.2 ms                                                | 37.4 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 206 us: 1.04x faster                                                  |
| thrift                           | 466 us                                                 | 448 us: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.03x faster                                                 |
| async_generators                 | 294 ms                                                 | 284 ms: 1.03x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 33.0 ms: 1.03x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 71.8 ms: 1.03x faster                                                 |
| pathlib                          | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.6 ms: 1.02x faster                                                 |
| nbody                            | 73.6 ms                                                | 72.4 ms: 1.02x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.59 sec: 1.02x faster                                                |
| scimark_lu                       | 75.9 ms                                                | 74.9 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| nqueens                          | 61.8 ms                                                | 61.0 ms: 1.01x faster                                                 |
| json                             | 3.04 ms                                                | 3.00 ms: 1.01x faster                                                 |
| sympy_expand                     | 248 ms                                                 | 245 ms: 1.01x faster                                                  |
| pycparser                        | 701 ms                                                 | 693 ms: 1.01x faster                                                  |
| sympy_str                        | 146 ms                                                 | 144 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                |
| connected_components             | 319 ms                                                 | 322 ms: 1.01x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 6.55 ms: 1.01x slower                                                 |
| shortest_path                    | 345 ms                                                 | 351 ms: 1.02x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 76.6 ms: 1.02x slower                                                 |
| coverage                         | 46.2 ms                                                | 47.4 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 73.3 ns: 1.03x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.30 ms: 1.11x slower                                                 |
| django_template                  | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                  |
| many_optionals                   | 409 us                                                 | 593 us: 1.45x slower                                                  |
| subparsers                       | 9.44 ms                                                | 25.4 ms: 2.69x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (3): json_loads, dask, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250721-3.15.0a0-9c7b2af-JIT/bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x