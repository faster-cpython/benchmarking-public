# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: darwin-arm64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.03x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 6.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 182 ms: 1.02x slower                                                      |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| html5lib       | 36.6 ms                                                | 33.8 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 235 ms: 1.24x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                     |
| async_tree_eager_tg              | 48.4 ms                                                | 43.3 ms: 1.12x faster                                                     |
| async_tree_eager                 | 70.5 ms                                                | 63.8 ms: 1.10x faster                                                     |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 154 ms: 1.10x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 200 ms: 1.06x faster                                                      |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 131 ms: 1.06x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 365 ms: 1.03x faster                                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 471 ms: 1.05x slower                                                      |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 613 ms: 1.23x slower                                                      |
| async_tree_eager_io              | 513 ms                                                 | 672 ms: 1.31x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_cpu_io_mixed, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 47.7 ms: 1.18x faster                                                     |
| nbody          | 73.9 ms                                                | 63.2 ms: 1.17x faster                                                     |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 74.0 ms: 1.06x faster                                                     |
| regex_v8       | 16.9 ms                                                | 16.9 ms: 1.01x faster                                                     |
| regex_effbot   | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                     |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.23 sec: 1.27x faster                                                    |
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                                      |
| xml_etree_process    | 40.9 ms                                                | 34.3 ms: 1.19x faster                                                     |
| pickle_pure_python   | 213 us                                                 | 179 us: 1.19x faster                                                      |
| xml_etree_generate   | 56.6 ms                                                | 49.8 ms: 1.14x faster                                                     |
| json_loads           | 16.9 us                                                | 16.5 us: 1.02x faster                                                     |
| xml_etree_iterparse  | 74.2 ms                                                | 73.2 ms: 1.01x faster                                                     |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                                      |
| unpickle             | 9.15 us                                                | 9.04 us: 1.01x faster                                                     |
| pickle_list          | 2.99 us                                                | 2.97 us: 1.01x faster                                                     |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                                     |
| unpickle_list        | 2.93 us                                                | 2.97 us: 1.01x slower                                                     |
| json_dumps           | 6.56 ms                                                | 7.23 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.08x slower                                                     |
| python_startup         | 17.0 ms                                                | 19.0 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.30 ms: 1.22x faster                                                     |
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                     |
| django_template | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                     |
| genshi_xml      | 34.4 ms                                                | 38.4 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                                     |
| deepcopy                         | 232 us                                                 | 155 us: 1.49x faster                                                      |
| deepcopy_reduce                  | 2.06 us                                                | 1.53 us: 1.35x faster                                                     |
| scimark_sor                      | 106 ms                                                 | 82.4 ms: 1.28x faster                                                     |
| tomli_loads                      | 1.56 sec                                               | 1.23 sec: 1.27x faster                                                    |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                     |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 235 ms: 1.24x faster                                                      |
| mako                             | 7.68 ms                                                | 6.30 ms: 1.22x faster                                                     |
| xml_etree_process                | 40.9 ms                                                | 34.3 ms: 1.19x faster                                                     |
| pickle_pure_python               | 213 us                                                 | 179 us: 1.19x faster                                                      |
| go                               | 115 ms                                                 | 96.8 ms: 1.19x faster                                                     |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                     |
| float                            | 56.2 ms                                                | 47.7 ms: 1.18x faster                                                     |
| nbody                            | 73.9 ms                                                | 63.2 ms: 1.17x faster                                                     |
| scimark_lu                       | 76.5 ms                                                | 65.7 ms: 1.16x faster                                                     |
| logging_simple                   | 3.57 us                                                | 3.09 us: 1.16x faster                                                     |
| logging_format                   | 3.85 us                                                | 3.37 us: 1.14x faster                                                     |
| xml_etree_generate               | 56.6 ms                                                | 49.8 ms: 1.14x faster                                                     |
| spectral_norm                    | 77.3 ms                                                | 68.1 ms: 1.13x faster                                                     |
| pprint_safe_repr                 | 531 ms                                                 | 470 ms: 1.13x faster                                                      |
| pprint_pformat                   | 1.08 sec                                               | 961 ms: 1.12x faster                                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 45.0 ms: 1.12x faster                                                     |
| async_tree_eager_tg              | 48.4 ms                                                | 43.3 ms: 1.12x faster                                                     |
| deltablue                        | 2.68 ms                                                | 2.42 ms: 1.11x faster                                                     |
| pyflate                          | 351 ms                                                 | 318 ms: 1.10x faster                                                      |
| async_tree_eager                 | 70.5 ms                                                | 63.8 ms: 1.10x faster                                                     |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 154 ms: 1.10x faster                                                      |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                      |
| bpe_tokeniser                    | 3.24 sec                                               | 2.98 sec: 1.09x faster                                                    |
| html5lib                         | 36.6 ms                                                | 33.8 ms: 1.09x faster                                                     |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                      |
| raytrace                         | 182 ms                                                 | 169 ms: 1.08x faster                                                      |
| bench_thread_pool                | 506 us                                                 | 474 us: 1.07x faster                                                      |
| fannkuch                         | 282 ms                                                 | 265 ms: 1.07x faster                                                      |
| regex_compile                    | 78.5 ms                                                | 74.0 ms: 1.06x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 200 ms: 1.06x faster                                                      |
| typing_runtime_protocols         | 101 us                                                 | 95.3 us: 1.06x faster                                                     |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 131 ms: 1.06x faster                                                      |
| telco                            | 4.80 ms                                                | 4.55 ms: 1.05x faster                                                     |
| nqueens                          | 62.9 ms                                                | 59.9 ms: 1.05x faster                                                     |
| pycparser                        | 706 ms                                                 | 673 ms: 1.05x faster                                                      |
| coverage                         | 46.1 ms                                                | 44.1 ms: 1.05x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 365 ms: 1.03x faster                                                      |
| richards                         | 35.4 ms                                                | 34.5 ms: 1.03x faster                                                     |
| json                             | 2.94 ms                                                | 2.87 ms: 1.02x faster                                                     |
| richards_super                   | 39.1 ms                                                | 38.3 ms: 1.02x faster                                                     |
| json_loads                       | 16.9 us                                                | 16.5 us: 1.02x faster                                                     |
| crypto_pyaes                     | 54.0 ms                                                | 53.1 ms: 1.02x faster                                                     |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.01x faster                                                      |
| pathlib                          | 22.8 ms                                                | 22.5 ms: 1.01x faster                                                     |
| xml_etree_iterparse              | 74.2 ms                                                | 73.2 ms: 1.01x faster                                                     |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                                      |
| unpickle                         | 9.15 us                                                | 9.04 us: 1.01x faster                                                     |
| meteor_contest                   | 73.8 ms                                                | 73.1 ms: 1.01x faster                                                     |
| sqlglot_parse                    | 856 us                                                 | 849 us: 1.01x faster                                                      |
| pickle_list                      | 2.99 us                                                | 2.97 us: 1.01x faster                                                     |
| dulwich_log                      | 28.7 ms                                                | 28.5 ms: 1.01x faster                                                     |
| regex_v8                         | 16.9 ms                                                | 16.9 ms: 1.01x faster                                                     |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                     |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                                     |
| sympy_expand                     | 246 ms                                                 | 249 ms: 1.01x slower                                                      |
| django_template                  | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                     |
| logging_silent                   | 69.9 ns                                                | 70.7 ns: 1.01x slower                                                     |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                      |
| chaos                            | 41.3 ms                                                | 41.8 ms: 1.01x slower                                                     |
| unpickle_list                    | 2.93 us                                                | 2.97 us: 1.01x slower                                                     |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                     |
| hexiom                           | 4.85 ms                                                | 4.95 ms: 1.02x slower                                                     |
| 2to3                             | 178 ms                                                 | 182 ms: 1.02x slower                                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                    |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.11 ms: 1.04x slower                                                     |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                    |
| sympy_sum                        | 75.6 ms                                                | 79.2 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 471 ms: 1.05x slower                                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 36.9 ms: 1.06x slower                                                     |
| comprehensions                   | 12.2 us                                                | 13.0 us: 1.07x slower                                                     |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.08x slower                                                     |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.10x slower                                                     |
| json_dumps                       | 6.56 ms                                                | 7.23 ms: 1.10x slower                                                     |
| python_startup                   | 17.0 ms                                                | 19.0 ms: 1.12x slower                                                     |
| genshi_xml                       | 34.4 ms                                                | 38.4 ms: 1.12x slower                                                     |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                                      |
| pylint                           | 181 ms                                                 | 210 ms: 1.16x slower                                                      |
| gc_traversal                     | 2.48 ms                                                | 2.95 ms: 1.19x slower                                                     |
| bench_mp_pool                    | 50.9 ms                                                | 61.7 ms: 1.21x slower                                                     |
| async_tree_io_tg                 | 500 ms                                                 | 613 ms: 1.23x slower                                                      |
| async_tree_eager_io              | 513 ms                                                 | 672 ms: 1.31x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                      |
| create_gc_cycles                 | 803 us                                                 | 1.32 ms: 1.65x slower                                                     |
| unpack_sequence                  | 36.1 ns                                                | 62.2 ns: 1.72x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (7): asyncio_tcp, async_tree_cpu_io_mixed, sqlite_synth, tornado_http, pickle, asyncio_websockets, async_generators
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: sphinx

# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 6.53x