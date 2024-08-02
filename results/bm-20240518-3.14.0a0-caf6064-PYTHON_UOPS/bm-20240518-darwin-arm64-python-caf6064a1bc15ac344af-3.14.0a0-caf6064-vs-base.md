# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| chameleon      | 4.29 ms                                                                                                         | 4.94 ms: 1.15x slower                                                                                                       |
| docutils       | 1.44 sec                                                                                                        | 1.66 sec: 1.16x slower                                                                                                      |
| html5lib       | 31.0 ms                                                                                                         | 32.9 ms: 1.06x slower                                                                                                       |
| tornado_http   | 66.2 ms                                                                                                         | 70.6 ms: 1.07x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                           | 1.09x slower                                                                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                                                          | 335 ms: 1.01x slower                                                                                                        |
| async_tree_eager_cpu_io_mixed    | 361 ms                                                                                                          | 367 ms: 1.02x slower                                                                                                        |
| async_tree_cpu_io_mixed          | 468 ms                                                                                                          | 480 ms: 1.03x slower                                                                                                        |
| async_tree_eager_memoization_tg  | 125 ms                                                                                                          | 129 ms: 1.03x slower                                                                                                        |
| async_tree_none_tg               | 197 ms                                                                                                          | 206 ms: 1.05x slower                                                                                                        |
| async_tree_memoization           | 258 ms                                                                                                          | 272 ms: 1.05x slower                                                                                                        |
| async_tree_none                  | 209 ms                                                                                                          | 221 ms: 1.06x slower                                                                                                        |
| async_tree_eager_tg              | 41.4 ms                                                                                                         | 44.4 ms: 1.07x slower                                                                                                       |
| async_tree_memoization_tg        | 239 ms                                                                                                          | 259 ms: 1.08x slower                                                                                                        |
| async_tree_eager                 | 61.0 ms                                                                                                         | 68.7 ms: 1.13x slower                                                                                                       |
| Geometric mean                   | (ref)                                                                                                           | 1.04x slower                                                                                                                |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_io, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                        |
| float          | 48.2 ms                                                                                                         | 60.5 ms: 1.25x slower                                                                                                       |
| nbody          | 60.3 ms                                                                                                         | 77.3 ms: 1.28x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                           | 1.17x slower                                                                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.56 ms                                                                                                         | 2.59 ms: 1.01x slower                                                                                                       |
| regex_v8       | 17.3 ms                                                                                                         | 17.6 ms: 1.02x slower                                                                                                       |
| regex_compile  | 68.2 ms                                                                                                         | 95.7 ms: 1.40x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                           | 1.10x slower                                                                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| pickle_list          | 3.00 us                                                                                                         | 2.97 us: 1.01x faster                                                                                                       |
| pickle_dict          | 18.3 us                                                                                                         | 18.2 us: 1.01x faster                                                                                                       |
| unpickle_list        | 2.90 us                                                                                                         | 2.88 us: 1.01x faster                                                                                                       |
| xml_etree_parse      | 104 ms                                                                                                          | 106 ms: 1.02x slower                                                                                                        |
| json_dumps           | 6.29 ms                                                                                                         | 6.53 ms: 1.04x slower                                                                                                       |
| xml_etree_iterparse  | 71.6 ms                                                                                                         | 76.5 ms: 1.07x slower                                                                                                       |
| xml_etree_process    | 36.9 ms                                                                                                         | 41.1 ms: 1.11x slower                                                                                                       |
| tomli_loads          | 1.46 sec                                                                                                        | 1.64 sec: 1.12x slower                                                                                                      |
| xml_etree_generate   | 52.2 ms                                                                                                         | 58.7 ms: 1.13x slower                                                                                                       |
| unpickle_pure_python | 140 us                                                                                                          | 176 us: 1.26x slower                                                                                                        |
| pickle_pure_python   | 178 us                                                                                                          | 228 us: 1.28x slower                                                                                                        |
| Geometric mean       | (ref)                                                                                                           | 1.07x slower                                                                                                                |

Benchmark hidden because not significant (3): json_loads, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 11.5 ms                                                                                                         | 11.7 ms: 1.02x slower                                                                                                       |
| Geometric mean         | (ref)                                                                                                           | 1.02x slower                                                                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 29.7 ms                                                                                                         | 36.0 ms: 1.21x slower                                                                                                       |
| django_template | 19.4 ms                                                                                                         | 23.8 ms: 1.23x slower                                                                                                       |
| genshi_text     | 13.7 ms                                                                                                         | 17.3 ms: 1.26x slower                                                                                                       |
| mako            | 6.91 ms                                                                                                         | 9.09 ms: 1.32x slower                                                                                                       |
| Geometric mean  | (ref)                                                                                                           | 1.25x slower                                                                                                                |

All benchmarks:
===============

| Benchmark                        | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| pickle_list                      | 3.00 us                                                                                                         | 2.97 us: 1.01x faster                                                                                                       |
| pickle_dict                      | 18.3 us                                                                                                         | 18.2 us: 1.01x faster                                                                                                       |
| unpickle_list                    | 2.90 us                                                                                                         | 2.88 us: 1.01x faster                                                                                                       |
| gc_traversal                     | 2.46 ms                                                                                                         | 2.46 ms: 1.00x slower                                                                                                       |
| pidigits                         | 281 ms                                                                                                          | 282 ms: 1.00x slower                                                                                                        |
| create_gc_cycles                 | 910 us                                                                                                          | 914 us: 1.00x slower                                                                                                        |
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                                                          | 335 ms: 1.01x slower                                                                                                        |
| regex_effbot                     | 2.56 ms                                                                                                         | 2.59 ms: 1.01x slower                                                                                                       |
| coroutines                       | 15.9 ms                                                                                                         | 16.1 ms: 1.01x slower                                                                                                       |
| asyncio_tcp_ssl                  | 1.28 sec                                                                                                        | 1.30 sec: 1.01x slower                                                                                                      |
| json                             | 2.95 ms                                                                                                         | 3.00 ms: 1.01x slower                                                                                                       |
| xml_etree_parse                  | 104 ms                                                                                                          | 106 ms: 1.02x slower                                                                                                        |
| regex_v8                         | 17.3 ms                                                                                                         | 17.6 ms: 1.02x slower                                                                                                       |
| async_tree_eager_cpu_io_mixed    | 361 ms                                                                                                          | 367 ms: 1.02x slower                                                                                                        |
| python_startup_no_site           | 11.5 ms                                                                                                         | 11.7 ms: 1.02x slower                                                                                                       |
| thrift                           | 428 us                                                                                                          | 439 us: 1.02x slower                                                                                                        |
| async_tree_cpu_io_mixed          | 468 ms                                                                                                          | 480 ms: 1.03x slower                                                                                                        |
| logging_format                   | 3.35 us                                                                                                         | 3.45 us: 1.03x slower                                                                                                       |
| async_tree_eager_memoization_tg  | 125 ms                                                                                                          | 129 ms: 1.03x slower                                                                                                        |
| generators                       | 22.9 ms                                                                                                         | 23.6 ms: 1.03x slower                                                                                                       |
| bench_mp_pool                    | 45.7 ms                                                                                                         | 47.1 ms: 1.03x slower                                                                                                       |
| dask                             | 220 ms                                                                                                          | 227 ms: 1.03x slower                                                                                                        |
| logging_simple                   | 3.07 us                                                                                                         | 3.18 us: 1.04x slower                                                                                                       |
| json_dumps                       | 6.29 ms                                                                                                         | 6.53 ms: 1.04x slower                                                                                                       |
| sqlite_synth                     | 1.54 us                                                                                                         | 1.61 us: 1.04x slower                                                                                                       |
| async_tree_none_tg               | 197 ms                                                                                                          | 206 ms: 1.05x slower                                                                                                        |
| flaskblogging                    | 3.40 ms                                                                                                         | 3.57 ms: 1.05x slower                                                                                                       |
| async_tree_memoization           | 258 ms                                                                                                          | 272 ms: 1.05x slower                                                                                                        |
| async_tree_none                  | 209 ms                                                                                                          | 221 ms: 1.06x slower                                                                                                        |
| async_generators                 | 279 ms                                                                                                          | 296 ms: 1.06x slower                                                                                                        |
| html5lib                         | 31.0 ms                                                                                                         | 32.9 ms: 1.06x slower                                                                                                       |
| tornado_http                     | 66.2 ms                                                                                                         | 70.6 ms: 1.07x slower                                                                                                       |
| xml_etree_iterparse              | 71.6 ms                                                                                                         | 76.5 ms: 1.07x slower                                                                                                       |
| async_tree_eager_tg              | 41.4 ms                                                                                                         | 44.4 ms: 1.07x slower                                                                                                       |
| async_tree_memoization_tg        | 239 ms                                                                                                          | 259 ms: 1.08x slower                                                                                                        |
| mdp                              | 1.49 sec                                                                                                        | 1.64 sec: 1.10x slower                                                                                                      |
| telco                            | 4.61 ms                                                                                                         | 5.12 ms: 1.11x slower                                                                                                       |
| xml_etree_process                | 36.9 ms                                                                                                         | 41.1 ms: 1.11x slower                                                                                                       |
| tomli_loads                      | 1.46 sec                                                                                                        | 1.64 sec: 1.12x slower                                                                                                      |
| async_tree_eager                 | 61.0 ms                                                                                                         | 68.7 ms: 1.13x slower                                                                                                       |
| xml_etree_generate               | 52.2 ms                                                                                                         | 58.7 ms: 1.13x slower                                                                                                       |
| bench_thread_pool                | 463 us                                                                                                          | 525 us: 1.13x slower                                                                                                        |
| pylint                           | 172 ms                                                                                                          | 195 ms: 1.14x slower                                                                                                        |
| pycparser                        | 632 ms                                                                                                          | 723 ms: 1.14x slower                                                                                                        |
| scimark_sor                      | 94.0 ms                                                                                                         | 108 ms: 1.15x slower                                                                                                        |
| meteor_contest                   | 69.8 ms                                                                                                         | 80.1 ms: 1.15x slower                                                                                                       |
| chameleon                        | 4.29 ms                                                                                                         | 4.94 ms: 1.15x slower                                                                                                       |
| docutils                         | 1.44 sec                                                                                                        | 1.66 sec: 1.16x slower                                                                                                      |
| go                               | 100 ms                                                                                                          | 117 ms: 1.17x slower                                                                                                        |
| sympy_expand                     | 227 ms                                                                                                          | 266 ms: 1.17x slower                                                                                                        |
| typing_runtime_protocols         | 91.7 us                                                                                                         | 108 us: 1.17x slower                                                                                                        |
| deepcopy_reduce                  | 1.79 us                                                                                                         | 2.11 us: 1.18x slower                                                                                                       |
| raytrace                         | 147 ms                                                                                                          | 175 ms: 1.19x slower                                                                                                        |
| sqlglot_optimize                 | 31.0 ms                                                                                                         | 37.2 ms: 1.20x slower                                                                                                       |
| richards_super                   | 34.3 ms                                                                                                         | 41.2 ms: 1.20x slower                                                                                                       |
| richards                         | 31.1 ms                                                                                                         | 37.6 ms: 1.21x slower                                                                                                       |
| genshi_xml                       | 29.7 ms                                                                                                         | 36.0 ms: 1.21x slower                                                                                                       |
| sympy_integrate                  | 10.3 ms                                                                                                         | 12.6 ms: 1.22x slower                                                                                                       |
| django_template                  | 19.4 ms                                                                                                         | 23.8 ms: 1.23x slower                                                                                                       |
| sympy_sum                        | 69.9 ms                                                                                                         | 85.9 ms: 1.23x slower                                                                                                       |
| crypto_pyaes                     | 49.6 ms                                                                                                         | 61.2 ms: 1.23x slower                                                                                                       |
| deepcopy                         | 200 us                                                                                                          | 248 us: 1.24x slower                                                                                                        |
| sympy_str                        | 132 ms                                                                                                          | 164 ms: 1.24x slower                                                                                                        |
| pyflate                          | 320 ms                                                                                                          | 399 ms: 1.25x slower                                                                                                        |
| pprint_pformat                   | 943 ms                                                                                                          | 1.18 sec: 1.25x slower                                                                                                      |
| pprint_safe_repr                 | 462 ms                                                                                                          | 578 ms: 1.25x slower                                                                                                        |
| float                            | 48.2 ms                                                                                                         | 60.5 ms: 1.25x slower                                                                                                       |
| unpickle_pure_python             | 140 us                                                                                                          | 176 us: 1.26x slower                                                                                                        |
| genshi_text                      | 13.7 ms                                                                                                         | 17.3 ms: 1.26x slower                                                                                                       |
| fannkuch                         | 249 ms                                                                                                          | 318 ms: 1.27x slower                                                                                                        |
| pickle_pure_python               | 178 us                                                                                                          | 228 us: 1.28x slower                                                                                                        |
| scimark_fft                      | 180 ms                                                                                                          | 232 ms: 1.28x slower                                                                                                        |
| nbody                            | 60.3 ms                                                                                                         | 77.3 ms: 1.28x slower                                                                                                       |
| sqlglot_transpile                | 892 us                                                                                                          | 1.15 ms: 1.29x slower                                                                                                       |
| sqlglot_parse                    | 733 us                                                                                                          | 957 us: 1.31x slower                                                                                                        |
| nqueens                          | 52.6 ms                                                                                                         | 69.1 ms: 1.31x slower                                                                                                       |
| mako                             | 6.91 ms                                                                                                         | 9.09 ms: 1.32x slower                                                                                                       |
| chaos                            | 34.3 ms                                                                                                         | 47.0 ms: 1.37x slower                                                                                                       |
| deltablue                        | 2.14 ms                                                                                                         | 2.94 ms: 1.38x slower                                                                                                       |
| spectral_norm                    | 67.2 ms                                                                                                         | 94.2 ms: 1.40x slower                                                                                                       |
| regex_compile                    | 68.2 ms                                                                                                         | 95.7 ms: 1.40x slower                                                                                                       |
| deepcopy_memo                    | 22.6 us                                                                                                         | 32.4 us: 1.43x slower                                                                                                       |
| scimark_monte_carlo              | 42.2 ms                                                                                                         | 61.1 ms: 1.45x slower                                                                                                       |
| scimark_sparse_mat_mult          | 2.77 ms                                                                                                         | 4.01 ms: 1.45x slower                                                                                                       |
| scimark_lu                       | 66.8 ms                                                                                                         | 98.1 ms: 1.47x slower                                                                                                       |
| hexiom                           | 4.08 ms                                                                                                         | 6.00 ms: 1.47x slower                                                                                                       |
| logging_silent                   | 60.0 ns                                                                                                         | 95.4 ns: 1.59x slower                                                                                                       |
| comprehensions                   | 10.7 us                                                                                                         | 17.3 us: 1.62x slower                                                                                                       |
| Geometric mean                   | (ref)                                                                                                           | 1.13x slower                                                                                                                |

Benchmark hidden because not significant (16): asyncio_tcp, coverage, json_loads, async_tree_io_tg, 2to3, asyncio_websockets, regex_dna, pathlib, pickle, unpickle, python_startup, async_tree_io, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_memoization
Ignored benchmarks (1) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.02x