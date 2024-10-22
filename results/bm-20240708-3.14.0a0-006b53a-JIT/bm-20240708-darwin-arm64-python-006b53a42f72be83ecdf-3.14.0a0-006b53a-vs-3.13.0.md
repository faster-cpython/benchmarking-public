# Results vs. 3.13.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: darwin-arm64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 6.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 171 ms: 1.04x faster                                                  |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.18x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 241 ms: 1.21x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.18x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 232 ms: 1.16x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 398 ms: 1.15x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 63.6 ms: 1.11x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| async_tree_io                    | 507 ms                                                 | 519 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                |
| async_tree_eager_io              | 513 ms                                                 | 737 ms: 1.44x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 697 ms: 1.46x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_generators, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 47.2 ms: 1.19x faster                                                 |
| nbody          | 73.9 ms                                                | 64.1 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 73.5 ms: 1.07x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                 |
| regex_v8       | 16.9 ms                                                | 17.2 ms: 1.01x slower                                                 |
| regex_dna      | 148 ms                                                 | 150 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                |
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                                  |
| pickle_pure_python   | 213 us                                                 | 175 us: 1.22x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 36.5 ms: 1.12x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 52.5 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 71.3 ms: 1.04x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.39 ms: 1.03x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| json_loads           | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.50 ms: 1.18x faster                                                 |
| genshi_text     | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                 |
| django_template | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 39.9 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                                 |
| deepcopy                         | 232 us                                                 | 152 us: 1.53x faster                                                  |
| generators                       | 31.5 ms                                                | 23.2 ms: 1.36x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.56 us: 1.32x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 175 us: 1.22x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 241 ms: 1.21x faster                                                  |
| float                            | 56.2 ms                                                | 47.2 ms: 1.19x faster                                                 |
| mako                             | 7.68 ms                                                | 6.50 ms: 1.18x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.04 us: 1.18x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.18x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.18x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 232 ms: 1.16x faster                                                  |
| nbody                            | 73.9 ms                                                | 64.1 ms: 1.15x faster                                                 |
| fannkuch                         | 282 ms                                                 | 244 ms: 1.15x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.33 ms: 1.15x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 398 ms: 1.15x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.9 ms: 1.15x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.37 us: 1.14x faster                                                 |
| richards                         | 35.4 ms                                                | 31.1 ms: 1.14x faster                                                 |
| dask                             | 255 ms                                                 | 225 ms: 1.14x faster                                                  |
| go                               | 115 ms                                                 | 101 ms: 1.13x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 61.7 ns: 1.13x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| richards_super                   | 39.1 ms                                                | 34.7 ms: 1.13x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 68.7 ms: 1.12x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 36.5 ms: 1.12x faster                                                 |
| python_startup                   | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 63.6 ms: 1.11x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.40 ms: 1.10x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 481 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 319 ms: 1.10x faster                                                  |
| raytrace                         | 182 ms                                                 | 166 ms: 1.10x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 989 ms: 1.09x faster                                                  |
| nqueens                          | 62.9 ms                                                | 57.9 ms: 1.09x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 52.5 ms: 1.08x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                 |
| thrift                           | 466 us                                                 | 436 us: 1.07x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 73.5 ms: 1.07x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 476 us: 1.06x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 179 ms: 1.05x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 33.2 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                  |
| chaos                            | 41.3 ms                                                | 39.3 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| pycparser                        | 706 ms                                                 | 675 ms: 1.05x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 96.7 us: 1.04x faster                                                 |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.12 sec: 1.04x faster                                                |
| xml_etree_iterparse              | 74.2 ms                                                | 71.3 ms: 1.04x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| 2to3                             | 178 ms                                                 | 171 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 52.2 ms: 1.04x faster                                                 |
| telco                            | 4.80 ms                                                | 4.64 ms: 1.03x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                |
| sqlglot_parse                    | 856 us                                                 | 831 us: 1.03x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.39 ms: 1.03x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 73.7 ms: 1.03x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.00 ms: 1.02x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 241 ms: 1.02x faster                                                  |
| django_template                  | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 50.1 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| meteor_contest                   | 73.8 ms                                                | 72.7 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| coverage                         | 46.1 ms                                                | 45.9 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.03 ms: 1.01x slower                                                 |
| regex_v8                         | 16.9 ms                                                | 17.2 ms: 1.01x slower                                                 |
| comprehensions                   | 12.2 us                                                | 12.4 us: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                 | 150 ms: 1.02x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 519 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                                |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.5 ms: 1.03x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                |
| scimark_lu                       | 76.5 ms                                                | 82.6 ms: 1.08x slower                                                 |
| create_gc_cycles                 | 803 us                                                 | 913 us: 1.14x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 39.9 ms: 1.16x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 737 ms: 1.44x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 697 ms: 1.46x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (6): tornado_http, pylint, async_tree_cpu_io_mixed_tg, json, async_generators, async_tree_io_tg
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 6.23x