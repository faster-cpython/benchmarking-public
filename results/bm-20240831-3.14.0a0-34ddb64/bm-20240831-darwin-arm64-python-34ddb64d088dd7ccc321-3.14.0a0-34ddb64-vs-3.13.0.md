# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 160 ms: 1.11x faster                                                  |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| html5lib       | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 244 ms: 1.19x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 61.0 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 407 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 193 ms: 1.10x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                                  |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 459 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 568 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 679 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 720 ms: 1.51x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.3 ms: 1.25x faster                                                 |
| float          | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 67.7 ms: 1.16x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 181 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 53.2 ms: 1.07x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.38 ms: 1.03x faster                                                 |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                 |
| mako            | 7.68 ms                                                | 7.03 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.7 us: 1.63x faster                                                 |
| deepcopy                         | 232 us                                                 | 146 us: 1.59x faster                                                  |
| generators                       | 31.5 ms                                                | 20.4 ms: 1.54x faster                                                 |
| go                               | 115 ms                                                 | 79.0 ms: 1.46x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.52 us: 1.36x faster                                                 |
| nbody                            | 73.9 ms                                                | 59.3 ms: 1.25x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.18 ms: 1.23x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| comprehensions                   | 12.2 us                                                | 9.96 us: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.06 ms: 1.20x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 244 ms: 1.19x faster                                                  |
| nqueens                          | 62.9 ms                                                | 53.2 ms: 1.18x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 181 us: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 456 ms: 1.16x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 67.7 ms: 1.16x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 930 ms: 1.16x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 437 us: 1.16x faster                                                  |
| float                            | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                 |
| chaos                            | 41.3 ms                                                | 35.7 ms: 1.16x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 61.0 ms: 1.16x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.10 us: 1.15x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 67.1 ms: 1.15x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 66.6 ms: 1.15x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 60.9 ns: 1.15x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 898 us: 1.14x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 92.9 ms: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.40 us: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.0 ms: 1.13x faster                                                 |
| richards                         | 35.4 ms                                                | 31.6 ms: 1.12x faster                                                 |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 407 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 90.9 us: 1.11x faster                                                 |
| richards_super                   | 39.1 ms                                                | 35.3 ms: 1.11x faster                                                 |
| 2to3                             | 178 ms                                                 | 160 ms: 1.11x faster                                                  |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                                  |
| pycparser                        | 706 ms                                                 | 642 ms: 1.10x faster                                                  |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 193 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 69.1 ms: 1.09x faster                                                 |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| mako                             | 7.68 ms                                                | 7.03 ms: 1.09x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                                  |
| fannkuch                         | 282 ms                                                 | 261 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.79 ms: 1.07x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 50.6 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.07x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 53.2 ms: 1.07x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 48.6 ms: 1.05x faster                                                 |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.38 ms: 1.03x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.9 ms: 1.03x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 72.2 ms: 1.02x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| python_startup                   | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 459 ms: 1.03x slower                                                  |
| pathlib                          | 22.8 ms                                                | 24.2 ms: 1.06x slower                                                 |
| create_gc_cycles                 | 803 us                                                 | 896 us: 1.12x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 568 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 679 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 720 ms: 1.51x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (9): bpe_tokeniser, telco, async_tree_cpu_io_mixed, xml_etree_parse, xml_etree_iterparse, json, pylint, async_tree_none_tg, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.99x