# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 163 ms: 1.10x faster                                                            |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                          |
| html5lib       | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                           |
| sphinx         | 602 ms                                                 | 568 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 185 ms: 1.44x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 365 ms: 1.39x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 364 ms: 1.37x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 157 ms: 1.35x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 362 ms: 1.32x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.31x faster                                                            |
| coroutines                       | 20.0 ms                                                | 16.0 ms: 1.25x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 60.5 ms: 1.16x faster                                                           |
| async_generators                 | 294 ms                                                 | 259 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 407 ms: 1.10x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 354 ms: 1.05x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 386 ms: 1.11x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.63x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.0 ms: 1.19x faster                                                           |
| nbody          | 73.6 ms                                                | 68.6 ms: 1.07x faster                                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 65.9 ms: 1.19x faster                                                           |
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                           |
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.07x faster                                                           |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                          |
| unpickle_pure_python | 165 us                                                 | 144 us: 1.15x faster                                                            |
| xml_etree_process    | 41.3 ms                                                | 37.3 ms: 1.11x faster                                                           |
| xml_etree_generate   | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                           |
| pickle_pure_python   | 215 us                                                 | 203 us: 1.06x faster                                                            |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                            |
| xml_etree_iterparse  | 74.2 ms                                                | 70.7 ms: 1.05x faster                                                           |
| json_loads           | 17.0 us                                                | 16.3 us: 1.04x faster                                                           |
| json_dumps           | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.7 ms: 1.18x faster                                                           |
| python_startup         | 18.8 ms                                                | 16.0 ms: 1.17x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.4 ms: 1.26x faster                                                           |
| genshi_xml      | 34.1 ms                                                | 28.6 ms: 1.19x faster                                                           |
| mako            | 7.75 ms                                                | 7.64 ms: 1.01x faster                                                           |
| django_template | 20.5 ms                                                | 20.9 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 725 ms: 2.07x faster                                                            |
| deepcopy                         | 236 us                                                 | 149 us: 1.59x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 17.8 us: 1.54x faster                                                           |
| go                               | 117 ms                                                 | 77.1 ms: 1.51x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 185 ms: 1.44x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 365 ms: 1.39x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 76.1 ms: 1.39x faster                                                           |
| generators                       | 31.9 ms                                                | 23.2 ms: 1.38x faster                                                           |
| async_tree_io_tg                 | 500 ms                                                 | 364 ms: 1.37x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 157 ms: 1.35x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 362 ms: 1.32x faster                                                            |
| tomli_loads                      | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.31x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.62 us: 1.30x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 13.4 ms: 1.26x faster                                                           |
| html5lib                         | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                           |
| coroutines                       | 20.0 ms                                                | 16.0 ms: 1.25x faster                                                           |
| pyflate                          | 352 ms                                                 | 284 ms: 1.24x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                            |
| genshi_xml                       | 34.1 ms                                                | 28.6 ms: 1.19x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 42.3 ms: 1.19x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 24.1 ms: 1.19x faster                                                           |
| float                            | 55.8 ms                                                | 47.0 ms: 1.19x faster                                                           |
| regex_compile                    | 78.3 ms                                                | 65.9 ms: 1.19x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 64.7 ms: 1.18x faster                                                           |
| python_startup_no_site           | 13.7 ms                                                | 11.7 ms: 1.18x faster                                                           |
| python_startup                   | 18.8 ms                                                | 16.0 ms: 1.17x faster                                                           |
| hexiom                           | 4.87 ms                                                | 4.15 ms: 1.17x faster                                                           |
| fannkuch                         | 279 ms                                                 | 241 ms: 1.16x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 60.5 ms: 1.16x faster                                                           |
| unpickle_pure_python             | 165 us                                                 | 144 us: 1.15x faster                                                            |
| pylint                           | 180 ms                                                 | 157 ms: 1.14x faster                                                            |
| async_generators                 | 294 ms                                                 | 259 ms: 1.13x faster                                                            |
| deltablue                        | 2.65 ms                                                | 2.34 ms: 1.13x faster                                                           |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                                            |
| richards                         | 36.2 ms                                                | 32.3 ms: 1.12x faster                                                           |
| k_core                           | 1.61 sec                                               | 1.44 sec: 1.12x faster                                                          |
| scimark_fft                      | 200 ms                                                 | 179 ms: 1.11x faster                                                            |
| bpe_tokeniser                    | 3.26 sec                                               | 2.93 sec: 1.11x faster                                                          |
| chaos                            | 41.1 ms                                                | 37.1 ms: 1.11x faster                                                           |
| xml_etree_process                | 41.3 ms                                                | 37.3 ms: 1.11x faster                                                           |
| typing_runtime_protocols         | 101 us                                                 | 90.9 us: 1.11x faster                                                           |
| richards_super                   | 39.2 ms                                                | 35.5 ms: 1.11x faster                                                           |
| xml_etree_generate               | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 407 ms: 1.10x faster                                                            |
| comprehensions                   | 12.0 us                                                | 10.9 us: 1.10x faster                                                           |
| 2to3                             | 179 ms                                                 | 163 ms: 1.10x faster                                                            |
| telco                            | 4.84 ms                                                | 4.42 ms: 1.10x faster                                                           |
| nqueens                          | 61.8 ms                                                | 57.0 ms: 1.08x faster                                                           |
| pycparser                        | 701 ms                                                 | 648 ms: 1.08x faster                                                            |
| sympy_integrate                  | 11.3 ms                                                | 10.5 ms: 1.08x faster                                                           |
| connected_components             | 319 ms                                                 | 295 ms: 1.08x faster                                                            |
| shortest_path                    | 345 ms                                                 | 320 ms: 1.08x faster                                                            |
| nbody                            | 73.6 ms                                                | 68.6 ms: 1.07x faster                                                           |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                                            |
| raytrace                         | 181 ms                                                 | 169 ms: 1.07x faster                                                            |
| sympy_expand                     | 248 ms                                                 | 231 ms: 1.07x faster                                                            |
| sympy_str                        | 146 ms                                                 | 137 ms: 1.07x faster                                                            |
| regex_v8                         | 17.0 ms                                                | 16.0 ms: 1.07x faster                                                           |
| json                             | 3.04 ms                                                | 2.87 ms: 1.06x faster                                                           |
| meteor_contest                   | 74.0 ms                                                | 69.7 ms: 1.06x faster                                                           |
| sphinx                           | 602 ms                                                 | 568 ms: 1.06x faster                                                            |
| pickle_pure_python               | 215 us                                                 | 203 us: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 354 ms: 1.05x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 70.7 ms: 1.05x faster                                                           |
| json_loads                       | 17.0 us                                                | 16.3 us: 1.04x faster                                                           |
| pathlib                          | 23.2 ms                                                | 22.3 ms: 1.04x faster                                                           |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| sympy_sum                        | 75.1 ms                                                | 72.9 ms: 1.03x faster                                                           |
| pprint_pformat                   | 1.10 sec                                               | 1.07 sec: 1.03x faster                                                          |
| logging_simple                   | 3.56 us                                                | 3.47 us: 1.02x faster                                                           |
| pprint_safe_repr                 | 541 ms                                                 | 528 ms: 1.02x faster                                                            |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                          |
| scimark_lu                       | 75.9 ms                                                | 74.4 ms: 1.02x faster                                                           |
| crypto_pyaes                     | 55.3 ms                                                | 54.2 ms: 1.02x faster                                                           |
| logging_format                   | 3.85 us                                                | 3.78 us: 1.02x faster                                                           |
| mako                             | 7.75 ms                                                | 7.64 ms: 1.01x faster                                                           |
| json_dumps                       | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                           |
| dask                             | 771 ms                                                 | 765 ms: 1.01x faster                                                            |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| django_template                  | 20.5 ms                                                | 20.9 ms: 1.02x slower                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.02x slower                                                           |
| coverage                         | 46.2 ms                                                | 47.5 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.09 ms: 1.04x slower                                                           |
| gc_traversal                     | 2.94 ms                                                | 3.18 ms: 1.08x slower                                                           |
| many_optionals                   | 409 us                                                 | 452 us: 1.11x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 386 ms: 1.11x slower                                                            |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                            |
| subparsers                       | 9.44 ms                                                | 13.1 ms: 1.39x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.63x slower                                                            |
| logging_silent                   | 71.0 ns                                                | 321 ns: 4.53x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x