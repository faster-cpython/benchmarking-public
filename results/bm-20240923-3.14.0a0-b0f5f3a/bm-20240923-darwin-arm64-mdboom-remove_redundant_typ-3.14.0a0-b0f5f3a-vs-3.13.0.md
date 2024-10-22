# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: darwin-arm64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 162 ms: 1.10x faster                                                  |
| html5lib       | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 60.8 ms: 1.16x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 256 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 416 ms: 1.10x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                                  |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 548 ms: 1.10x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 675 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.0 ms: 1.23x faster                                                 |
| float          | 56.2 ms                                                | 48.5 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 67.0 ms: 1.17x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 180 us: 1.18x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 140 us: 1.16x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.5 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 52.9 ms: 1.07x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.30 ms: 1.04x faster                                                 |
| pickle_list          | 2.99 us                                                | 2.96 us: 1.01x faster                                                 |
| unpickle_list        | 2.93 us                                                | 2.90 us: 1.01x faster                                                 |
| unpickle             | 9.15 us                                                | 9.07 us: 1.01x faster                                                 |
| pickle               | 7.36 us                                                | 7.34 us: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.1 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| mako            | 7.68 ms                                                | 7.12 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.6 us: 1.64x faster                                                 |
| deepcopy                         | 232 us                                                 | 144 us: 1.61x faster                                                  |
| generators                       | 31.5 ms                                                | 21.1 ms: 1.49x faster                                                 |
| go                               | 115 ms                                                 | 79.2 ms: 1.45x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.38x faster                                                 |
| unpack_sequence                  | 36.1 ns                                                | 26.4 ns: 1.37x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.13 ms: 1.26x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| nbody                            | 73.9 ms                                                | 60.0 ms: 1.23x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.04 ms: 1.20x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.00 us: 1.19x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 42.4 ms: 1.19x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 64.6 ms: 1.19x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 180 us: 1.18x faster                                                  |
| nqueens                          | 62.9 ms                                                | 53.2 ms: 1.18x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.28 us: 1.18x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 67.0 ms: 1.17x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 66.0 ms: 1.17x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 736 us: 1.16x faster                                                  |
| unpickle_pure_python             | 163 us                                                 | 140 us: 1.16x faster                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 457 ms: 1.16x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 930 ms: 1.16x faster                                                  |
| float                            | 56.2 ms                                                | 48.5 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| chaos                            | 41.3 ms                                                | 35.6 ms: 1.16x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 60.8 ms: 1.16x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 60.8 ns: 1.15x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 898 us: 1.14x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 92.7 ms: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 256 ms: 1.13x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 448 us: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.1 ms: 1.12x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 179 ms: 1.12x faster                                                  |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| pycparser                        | 706 ms                                                 | 637 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.70 ms: 1.11x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 68.7 ms: 1.10x faster                                                 |
| 2to3                             | 178 ms                                                 | 162 ms: 1.10x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 416 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 320 ms: 1.10x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                                  |
| richards                         | 35.4 ms                                                | 32.4 ms: 1.09x faster                                                 |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.5 ms: 1.09x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.08x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 50.0 ms: 1.08x faster                                                 |
| richards_super                   | 39.1 ms                                                | 36.2 ms: 1.08x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 93.6 us: 1.08x faster                                                 |
| fannkuch                         | 282 ms                                                 | 261 ms: 1.08x faster                                                  |
| mako                             | 7.68 ms                                                | 7.12 ms: 1.08x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 52.9 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                                  |
| python_startup                   | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 48.0 ms: 1.06x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                |
| python_startup_no_site           | 13.7 ms                                                | 13.1 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.30 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| coverage                         | 46.1 ms                                                | 44.4 ms: 1.04x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.13 sec: 1.04x faster                                                |
| meteor_contest                   | 73.8 ms                                                | 71.3 ms: 1.03x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| json                             | 2.94 ms                                                | 2.91 ms: 1.01x faster                                                 |
| pickle_list                      | 2.99 us                                                | 2.96 us: 1.01x faster                                                 |
| unpickle_list                    | 2.93 us                                                | 2.90 us: 1.01x faster                                                 |
| unpickle                         | 9.15 us                                                | 9.07 us: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.00x faster                                                 |
| pickle                           | 7.36 us                                                | 7.34 us: 1.00x faster                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| pathlib                          | 22.8 ms                                                | 23.5 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 548 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 892 us: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 675 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (9): pylint, xml_etree_iterparse, json_loads, async_tree_cpu_io_mixed, pickle_dict, xml_etree_parse, telco, docutils, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.99x