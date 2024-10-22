# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: darwin-arm64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.03x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 176 ms: 1.01x faster                                                    |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.08x slower                                                  |
| html5lib       | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.13x faster                                                    |
| async_tree_eager_tg              | 48.4 ms                                                | 43.0 ms: 1.13x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                    |
| async_tree_eager                 | 70.5 ms                                                | 64.7 ms: 1.09x faster                                                   |
| async_tree_memoization           | 270 ms                                                 | 249 ms: 1.09x faster                                                    |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.08x faster                                                    |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                                    |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                    |
| async_tree_none                  | 212 ms                                                 | 202 ms: 1.05x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                                    |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 462 ms: 1.03x slower                                                    |
| async_tree_io_tg                 | 500 ms                                                 | 545 ms: 1.09x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                    |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                    |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 45.8 ms: 1.23x faster                                                   |
| nbody          | 73.9 ms                                                | 64.2 ms: 1.15x faster                                                   |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.13x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.48 ms: 1.06x faster                                                   |
| regex_compile  | 78.5 ms                                                | 76.0 ms: 1.03x faster                                                   |
| regex_v8       | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                   |
| regex_dna      | 148 ms                                                 | 146 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 131 us: 1.25x faster                                                    |
| pickle_pure_python   | 213 us                                                 | 176 us: 1.21x faster                                                    |
| xml_etree_process    | 40.9 ms                                                | 34.2 ms: 1.20x faster                                                   |
| xml_etree_generate   | 56.6 ms                                                | 50.5 ms: 1.12x faster                                                   |
| json_dumps           | 6.56 ms                                                | 6.18 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 71.4 ms: 1.04x faster                                                   |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                                    |
| unpickle_list        | 2.93 us                                                | 2.90 us: 1.01x faster                                                   |
| unpickle             | 9.15 us                                                | 9.18 us: 1.00x slower                                                   |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                                   |
| pickle               | 7.36 us                                                | 7.44 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                            |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.43 ms: 1.19x faster                                                   |
| genshi_text     | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                   |
| django_template | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                   |
| genshi_xml      | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.0 us: 1.70x faster                                                   |
| deepcopy                         | 232 us                                                 | 154 us: 1.51x faster                                                    |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.36x faster                                                   |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                                   |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                  |
| unpickle_pure_python             | 163 us                                                 | 131 us: 1.25x faster                                                    |
| float                            | 56.2 ms                                                | 45.8 ms: 1.23x faster                                                   |
| scimark_lu                       | 76.5 ms                                                | 63.2 ms: 1.21x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 87.4 ms: 1.21x faster                                                   |
| pickle_pure_python               | 213 us                                                 | 176 us: 1.21x faster                                                    |
| xml_etree_process                | 40.9 ms                                                | 34.2 ms: 1.20x faster                                                   |
| mako                             | 7.68 ms                                                | 6.43 ms: 1.19x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| logging_simple                   | 3.57 us                                                | 3.01 us: 1.19x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.29 us: 1.17x faster                                                   |
| spectral_norm                    | 77.3 ms                                                | 66.7 ms: 1.16x faster                                                   |
| nbody                            | 73.9 ms                                                | 64.2 ms: 1.15x faster                                                   |
| deltablue                        | 2.68 ms                                                | 2.35 ms: 1.14x faster                                                   |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.13x faster                                                    |
| async_tree_eager_tg              | 48.4 ms                                                | 43.0 ms: 1.13x faster                                                   |
| xml_etree_generate               | 56.6 ms                                                | 50.5 ms: 1.12x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                    |
| logging_silent                   | 69.9 ns                                                | 63.0 ns: 1.11x faster                                                   |
| html5lib                         | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                   |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                    |
| nqueens                          | 62.9 ms                                                | 57.7 ms: 1.09x faster                                                   |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                    |
| async_tree_eager                 | 70.5 ms                                                | 64.7 ms: 1.09x faster                                                   |
| async_tree_memoization           | 270 ms                                                 | 249 ms: 1.09x faster                                                    |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.08x faster                                                    |
| typing_runtime_protocols         | 101 us                                                 | 93.6 us: 1.08x faster                                                   |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                                    |
| bench_thread_pool                | 506 us                                                 | 474 us: 1.07x faster                                                    |
| pyflate                          | 351 ms                                                 | 330 ms: 1.06x faster                                                    |
| json_dumps                       | 6.56 ms                                                | 6.18 ms: 1.06x faster                                                   |
| fannkuch                         | 282 ms                                                 | 266 ms: 1.06x faster                                                    |
| regex_effbot                     | 2.63 ms                                                | 2.48 ms: 1.06x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                    |
| bpe_tokeniser                    | 3.24 sec                                               | 3.07 sec: 1.06x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 202 ms: 1.05x faster                                                    |
| raytrace                         | 182 ms                                                 | 173 ms: 1.05x faster                                                    |
| scimark_monte_carlo              | 50.4 ms                                                | 48.0 ms: 1.05x faster                                                   |
| pprint_safe_repr                 | 531 ms                                                 | 509 ms: 1.04x faster                                                    |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.04x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 52.0 ms: 1.04x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 71.4 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                    |
| sqlglot_normalize                | 189 ms                                                 | 182 ms: 1.03x faster                                                    |
| regex_compile                    | 78.5 ms                                                | 76.0 ms: 1.03x faster                                                   |
| telco                            | 4.80 ms                                                | 4.65 ms: 1.03x faster                                                   |
| coverage                         | 46.1 ms                                                | 44.7 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                                    |
| chaos                            | 41.3 ms                                                | 40.1 ms: 1.03x faster                                                   |
| pycparser                        | 706 ms                                                 | 688 ms: 1.03x faster                                                    |
| regex_v8                         | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                   |
| hexiom                           | 4.85 ms                                                | 4.75 ms: 1.02x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.47 sec: 1.02x faster                                                  |
| python_startup                   | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                   |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                                    |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                   |
| 2to3                             | 178 ms                                                 | 176 ms: 1.01x faster                                                    |
| unpickle_list                    | 2.93 us                                                | 2.90 us: 1.01x faster                                                   |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                    |
| regex_dna                        | 148 ms                                                 | 146 ms: 1.01x faster                                                    |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                    |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                    |
| unpickle                         | 9.15 us                                                | 9.18 us: 1.00x slower                                                   |
| sympy_expand                     | 246 ms                                                 | 248 ms: 1.01x slower                                                    |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                                   |
| meteor_contest                   | 73.8 ms                                                | 74.4 ms: 1.01x slower                                                   |
| django_template                  | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                   |
| pickle                           | 7.36 us                                                | 7.44 us: 1.01x slower                                                   |
| dulwich_log                      | 28.7 ms                                                | 29.1 ms: 1.01x slower                                                   |
| sympy_sum                        | 75.6 ms                                                | 76.4 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 35.4 ms: 1.01x slower                                                   |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                   |
| sqlite_synth                     | 1.54 us                                                | 1.57 us: 1.02x slower                                                   |
| pathlib                          | 22.8 ms                                                | 23.3 ms: 1.02x slower                                                   |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 462 ms: 1.03x slower                                                    |
| comprehensions                   | 12.2 us                                                | 12.8 us: 1.05x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.08x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 545 ms: 1.09x slower                                                    |
| create_gc_cycles                 | 803 us                                                 | 898 us: 1.12x slower                                                    |
| pylint                           | 181 ms                                                 | 206 ms: 1.14x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                    |
| richards_super                   | 39.1 ms                                                | 46.7 ms: 1.19x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                   |
| richards                         | 35.4 ms                                                | 44.6 ms: 1.26x slower                                                   |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                    |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                    |
| unpack_sequence                  | 36.1 ns                                                | 76.3 ns: 2.11x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (9): json, scimark_sparse_mat_mult, pickle_list, sqlglot_parse, json_loads, python_startup_no_site, async_tree_cpu_io_mixed, bench_mp_pool, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x