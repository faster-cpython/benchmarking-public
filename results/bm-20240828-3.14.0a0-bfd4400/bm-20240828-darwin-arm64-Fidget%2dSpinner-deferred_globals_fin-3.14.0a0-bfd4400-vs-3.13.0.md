# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: darwin-arm64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 163 ms: 1.09x faster                                                            |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                          |
| html5lib       | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 229 ms: 1.27x faster                                                            |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 62.8 ms: 1.12x faster                                                           |
| async_tree_memoization           | 270 ms                                                 | 242 ms: 1.12x faster                                                            |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                            |
| asyncio_tcp                      | 457 ms                                                 | 418 ms: 1.09x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 184 ms: 1.08x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 196 ms: 1.08x faster                                                            |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                          |
| async_tree_io                    | 507 ms                                                 | 547 ms: 1.08x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.4 ms: 1.24x faster                                                           |
| float          | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                           |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.5 ms: 1.15x faster                                                           |
| regex_effbot   | 2.63 ms                                                | 2.50 ms: 1.05x faster                                                           |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                           |
| regex_dna      | 148 ms                                                 | 146 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 184 us: 1.16x faster                                                            |
| unpickle_pure_python | 163 us                                                 | 144 us: 1.14x faster                                                            |
| xml_etree_process    | 40.9 ms                                                | 38.3 ms: 1.07x faster                                                           |
| xml_etree_generate   | 56.6 ms                                                | 53.4 ms: 1.06x faster                                                           |
| tomli_loads          | 1.56 sec                                               | 1.50 sec: 1.04x faster                                                          |
| json_dumps           | 6.56 ms                                                | 6.52 ms: 1.01x faster                                                           |
| json_loads           | 16.9 us                                                | 17.3 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.2 ms: 1.19x faster                                                           |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                           |
| genshi_xml      | 34.4 ms                                                | 30.7 ms: 1.12x faster                                                           |
| mako            | 7.68 ms                                                | 7.16 ms: 1.07x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 17.1 us: 1.59x faster                                                           |
| deepcopy                         | 232 us                                                 | 146 us: 1.59x faster                                                            |
| generators                       | 31.5 ms                                                | 20.6 ms: 1.53x faster                                                           |
| deepcopy_reduce                  | 2.06 us                                                | 1.52 us: 1.35x faster                                                           |
| async_tree_memoization_tg        | 291 ms                                                 | 229 ms: 1.27x faster                                                            |
| deltablue                        | 2.68 ms                                                | 2.12 ms: 1.26x faster                                                           |
| nbody                            | 73.9 ms                                                | 59.4 ms: 1.24x faster                                                           |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                           |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                            |
| hexiom                           | 4.85 ms                                                | 4.06 ms: 1.20x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 14.2 ms: 1.19x faster                                                           |
| nqueens                          | 62.9 ms                                                | 53.1 ms: 1.18x faster                                                           |
| go                               | 115 ms                                                 | 97.2 ms: 1.18x faster                                                           |
| logging_simple                   | 3.57 us                                                | 3.06 us: 1.17x faster                                                           |
| float                            | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                           |
| spectral_norm                    | 77.3 ms                                                | 66.5 ms: 1.16x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 43.5 ms: 1.16x faster                                                           |
| html5lib                         | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                           |
| logging_silent                   | 69.9 ns                                                | 60.4 ns: 1.16x faster                                                           |
| pickle_pure_python               | 213 us                                                 | 184 us: 1.16x faster                                                            |
| sqlglot_parse                    | 856 us                                                 | 744 us: 1.15x faster                                                            |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                           |
| regex_compile                    | 78.5 ms                                                | 68.5 ms: 1.15x faster                                                           |
| logging_format                   | 3.85 us                                                | 3.37 us: 1.14x faster                                                           |
| chaos                            | 41.3 ms                                                | 36.2 ms: 1.14x faster                                                           |
| unpickle_pure_python             | 163 us                                                 | 144 us: 1.14x faster                                                            |
| scimark_lu                       | 76.5 ms                                                | 67.5 ms: 1.13x faster                                                           |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                                           |
| sqlglot_transpile                | 1.02 ms                                                | 907 us: 1.13x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 93.7 ms: 1.13x faster                                                           |
| bench_thread_pool                | 506 us                                                 | 449 us: 1.13x faster                                                            |
| richards                         | 35.4 ms                                                | 31.4 ms: 1.13x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 62.8 ms: 1.12x faster                                                           |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                           |
| genshi_xml                       | 34.4 ms                                                | 30.7 ms: 1.12x faster                                                           |
| pprint_safe_repr                 | 531 ms                                                 | 475 ms: 1.12x faster                                                            |
| async_tree_memoization           | 270 ms                                                 | 242 ms: 1.12x faster                                                            |
| pprint_pformat                   | 1.08 sec                                               | 969 ms: 1.11x faster                                                            |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                            |
| pycparser                        | 706 ms                                                 | 639 ms: 1.10x faster                                                            |
| comprehensions                   | 12.2 us                                                | 11.0 us: 1.10x faster                                                           |
| sqlglot_optimize                 | 34.9 ms                                                | 31.8 ms: 1.10x faster                                                           |
| sqlglot_normalize                | 189 ms                                                 | 172 ms: 1.10x faster                                                            |
| asyncio_tcp                      | 457 ms                                                 | 418 ms: 1.09x faster                                                            |
| pyflate                          | 351 ms                                                 | 322 ms: 1.09x faster                                                            |
| 2to3                             | 178 ms                                                 | 163 ms: 1.09x faster                                                            |
| thrift                           | 466 us                                                 | 430 us: 1.08x faster                                                            |
| sympy_integrate                  | 11.3 ms                                                | 10.5 ms: 1.08x faster                                                           |
| async_tree_none_tg               | 198 ms                                                 | 184 ms: 1.08x faster                                                            |
| scimark_fft                      | 201 ms                                                 | 186 ms: 1.08x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 196 ms: 1.08x faster                                                            |
| sympy_str                        | 145 ms                                                 | 135 ms: 1.08x faster                                                            |
| fannkuch                         | 282 ms                                                 | 262 ms: 1.07x faster                                                            |
| mako                             | 7.68 ms                                                | 7.16 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.80 ms: 1.07x faster                                                           |
| sympy_sum                        | 75.6 ms                                                | 70.8 ms: 1.07x faster                                                           |
| xml_etree_process                | 40.9 ms                                                | 38.3 ms: 1.07x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 26.9 ms: 1.07x faster                                                           |
| sympy_expand                     | 246 ms                                                 | 231 ms: 1.07x faster                                                            |
| xml_etree_generate               | 56.6 ms                                                | 53.4 ms: 1.06x faster                                                           |
| crypto_pyaes                     | 54.0 ms                                                | 51.1 ms: 1.06x faster                                                           |
| typing_runtime_protocols         | 101 us                                                 | 95.6 us: 1.06x faster                                                           |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.50 ms: 1.05x faster                                                           |
| bench_mp_pool                    | 50.9 ms                                                | 48.6 ms: 1.05x faster                                                           |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                          |
| bpe_tokeniser                    | 3.24 sec                                               | 3.11 sec: 1.04x faster                                                          |
| tomli_loads                      | 1.56 sec                                               | 1.50 sec: 1.04x faster                                                          |
| python_startup                   | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                            |
| telco                            | 4.80 ms                                                | 4.67 ms: 1.03x faster                                                           |
| meteor_contest                   | 73.8 ms                                                | 71.8 ms: 1.03x faster                                                           |
| coverage                         | 46.1 ms                                                | 44.9 ms: 1.03x faster                                                           |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                           |
| python_startup_no_site           | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                            |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                           |
| regex_dna                        | 148 ms                                                 | 146 ms: 1.01x faster                                                            |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                            |
| json_dumps                       | 6.56 ms                                                | 6.52 ms: 1.01x faster                                                           |
| pathlib                          | 22.8 ms                                                | 23.3 ms: 1.02x slower                                                           |
| json                             | 2.94 ms                                                | 3.01 ms: 1.02x slower                                                           |
| docutils                         | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                          |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.03x slower                                                           |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                          |
| async_tree_io                    | 507 ms                                                 | 547 ms: 1.08x slower                                                            |
| create_gc_cycles                 | 803 us                                                 | 886 us: 1.10x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, xml_etree_parse, xml_etree_iterparse, pylint, async_tree_io_tg, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.99x