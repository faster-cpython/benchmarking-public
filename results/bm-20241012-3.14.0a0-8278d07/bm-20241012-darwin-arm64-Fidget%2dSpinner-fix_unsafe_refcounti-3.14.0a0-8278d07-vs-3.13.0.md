# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: darwin-arm64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 196 ms: 1.10x slower                                                            |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                          |
| html5lib       | 36.6 ms                                                | 32.0 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 245 ms: 1.19x faster                                                            |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.19x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 59.7 ms: 1.18x faster                                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.15x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 192 ms: 1.10x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                            |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                                            |
| async_tree_eager_memoization     | 169 ms                                                 | 158 ms: 1.07x faster                                                            |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 459 ms: 1.03x slower                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 563 ms: 1.13x slower                                                            |
| async_tree_io                    | 507 ms                                                 | 593 ms: 1.17x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 711 ms: 1.49x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 49.0 ms: 1.15x faster                                                           |
| nbody          | 73.9 ms                                                | 65.6 ms: 1.13x faster                                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.3 ms: 1.15x faster                                                           |
| regex_v8       | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                           |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                           |
| regex_dna      | 148 ms                                                 | 146 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 183 us: 1.16x faster                                                            |
| unpickle_pure_python | 163 us                                                 | 142 us: 1.15x faster                                                            |
| xml_etree_process    | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                           |
| xml_etree_generate   | 56.6 ms                                                | 52.4 ms: 1.08x faster                                                           |
| tomli_loads          | 1.56 sec                                               | 1.49 sec: 1.04x faster                                                          |
| pickle_list          | 2.99 us                                                | 2.91 us: 1.03x faster                                                           |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 73.1 ms: 1.01x faster                                                           |
| pickle               | 7.36 us                                                | 7.34 us: 1.00x faster                                                           |
| unpickle_list        | 2.93 us                                                | 2.99 us: 1.02x slower                                                           |
| json_dumps           | 6.56 ms                                                | 7.25 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 19.0 ms: 1.12x slower                                                           |
| python_startup_no_site | 13.7 ms                                                | 15.9 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                           |
| genshi_xml      | 34.4 ms                                                | 29.9 ms: 1.15x faster                                                           |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                           |
| mako            | 7.68 ms                                                | 7.00 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                         | 232 us                                                 | 147 us: 1.58x faster                                                            |
| deepcopy_memo                    | 27.2 us                                                | 17.3 us: 1.58x faster                                                           |
| generators                       | 31.5 ms                                                | 20.3 ms: 1.55x faster                                                           |
| go                               | 115 ms                                                 | 81.8 ms: 1.41x faster                                                           |
| unpack_sequence                  | 36.1 ns                                                | 26.4 ns: 1.37x faster                                                           |
| deepcopy_reduce                  | 2.06 us                                                | 1.53 us: 1.34x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                           |
| deltablue                        | 2.68 ms                                                | 2.22 ms: 1.21x faster                                                           |
| async_tree_memoization_tg        | 291 ms                                                 | 245 ms: 1.19x faster                                                            |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.19x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 59.7 ms: 1.18x faster                                                           |
| raytrace                         | 182 ms                                                 | 154 ms: 1.18x faster                                                            |
| hexiom                           | 4.85 ms                                                | 4.14 ms: 1.17x faster                                                           |
| logging_simple                   | 3.57 us                                                | 3.05 us: 1.17x faster                                                           |
| pickle_pure_python               | 213 us                                                 | 183 us: 1.16x faster                                                            |
| nqueens                          | 62.9 ms                                                | 54.2 ms: 1.16x faster                                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.15x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 43.7 ms: 1.15x faster                                                           |
| logging_silent                   | 69.9 ns                                                | 60.6 ns: 1.15x faster                                                           |
| sqlglot_parse                    | 856 us                                                 | 743 us: 1.15x faster                                                            |
| logging_format                   | 3.85 us                                                | 3.34 us: 1.15x faster                                                           |
| pprint_safe_repr                 | 531 ms                                                 | 461 ms: 1.15x faster                                                            |
| regex_compile                    | 78.5 ms                                                | 68.3 ms: 1.15x faster                                                           |
| genshi_xml                       | 34.4 ms                                                | 29.9 ms: 1.15x faster                                                           |
| float                            | 56.2 ms                                                | 49.0 ms: 1.15x faster                                                           |
| unpickle_pure_python             | 163 us                                                 | 142 us: 1.15x faster                                                            |
| html5lib                         | 36.6 ms                                                | 32.0 ms: 1.14x faster                                                           |
| pprint_pformat                   | 1.08 sec                                               | 943 ms: 1.14x faster                                                            |
| scimark_lu                       | 76.5 ms                                                | 67.0 ms: 1.14x faster                                                           |
| sqlglot_transpile                | 1.02 ms                                                | 898 us: 1.14x faster                                                            |
| richards                         | 35.4 ms                                                | 31.2 ms: 1.14x faster                                                           |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.13x faster                                                            |
| nbody                            | 73.9 ms                                                | 65.6 ms: 1.13x faster                                                           |
| sqlglot_optimize                 | 34.9 ms                                                | 31.0 ms: 1.13x faster                                                           |
| richards_super                   | 39.1 ms                                                | 34.8 ms: 1.12x faster                                                           |
| thrift                           | 466 us                                                 | 419 us: 1.11x faster                                                            |
| bench_thread_pool                | 506 us                                                 | 455 us: 1.11x faster                                                            |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                           |
| pycparser                        | 706 ms                                                 | 638 ms: 1.11x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 192 ms: 1.10x faster                                                            |
| chaos                            | 41.3 ms                                                | 37.4 ms: 1.10x faster                                                           |
| comprehensions                   | 12.2 us                                                | 11.0 us: 1.10x faster                                                           |
| scimark_sor                      | 106 ms                                                 | 95.9 ms: 1.10x faster                                                           |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                            |
| mako                             | 7.68 ms                                                | 7.00 ms: 1.10x faster                                                           |
| sympy_expand                     | 246 ms                                                 | 225 ms: 1.09x faster                                                            |
| xml_etree_process                | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                           |
| spectral_norm                    | 77.3 ms                                                | 70.8 ms: 1.09x faster                                                           |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.09x faster                                                            |
| sympy_sum                        | 75.6 ms                                                | 69.3 ms: 1.09x faster                                                           |
| typing_runtime_protocols         | 101 us                                                 | 92.9 us: 1.09x faster                                                           |
| xml_etree_generate               | 56.6 ms                                                | 52.4 ms: 1.08x faster                                                           |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                                            |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                            |
| async_tree_eager_memoization     | 169 ms                                                 | 158 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.82 ms: 1.06x faster                                                           |
| fannkuch                         | 282 ms                                                 | 266 ms: 1.06x faster                                                            |
| coverage                         | 46.1 ms                                                | 43.6 ms: 1.06x faster                                                           |
| crypto_pyaes                     | 54.0 ms                                                | 51.2 ms: 1.05x faster                                                           |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.05x faster                                                            |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                            |
| bpe_tokeniser                    | 3.24 sec                                               | 3.08 sec: 1.05x faster                                                          |
| telco                            | 4.80 ms                                                | 4.57 ms: 1.05x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                                           |
| tomli_loads                      | 1.56 sec                                               | 1.49 sec: 1.04x faster                                                          |
| json                             | 2.94 ms                                                | 2.82 ms: 1.04x faster                                                           |
| pathlib                          | 22.8 ms                                                | 22.0 ms: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 362 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                            |
| meteor_contest                   | 73.8 ms                                                | 71.5 ms: 1.03x faster                                                           |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                           |
| regex_v8                         | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                           |
| pickle_list                      | 2.99 us                                                | 2.91 us: 1.03x faster                                                           |
| json_loads                       | 16.9 us                                                | 16.4 us: 1.03x faster                                                           |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                          |
| mdp                              | 1.50 sec                                               | 1.47 sec: 1.02x faster                                                          |
| sqlite_synth                     | 1.54 us                                                | 1.52 us: 1.02x faster                                                           |
| xml_etree_iterparse              | 74.2 ms                                                | 73.1 ms: 1.01x faster                                                           |
| regex_effbot                     | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                           |
| regex_dna                        | 148 ms                                                 | 146 ms: 1.01x faster                                                            |
| pickle                           | 7.36 us                                                | 7.34 us: 1.00x faster                                                           |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| gc_traversal                     | 2.48 ms                                                | 2.50 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                          |
| unpickle_list                    | 2.93 us                                                | 2.99 us: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 459 ms: 1.03x slower                                                            |
| 2to3                             | 178 ms                                                 | 196 ms: 1.10x slower                                                            |
| json_dumps                       | 6.56 ms                                                | 7.25 ms: 1.10x slower                                                           |
| python_startup                   | 17.0 ms                                                | 19.0 ms: 1.12x slower                                                           |
| async_tree_io_tg                 | 500 ms                                                 | 563 ms: 1.13x slower                                                            |
| create_gc_cycles                 | 803 us                                                 | 929 us: 1.16x slower                                                            |
| python_startup_no_site           | 13.7 ms                                                | 15.9 ms: 1.16x slower                                                           |
| async_tree_io                    | 507 ms                                                 | 593 ms: 1.17x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 711 ms: 1.49x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (10): tornado_http, asyncio_tcp, pylint, bench_mp_pool, async_tree_none_tg, xml_etree_parse, unpickle, asyncio_websockets, pickle_dict, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x