# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 162 ms: 1.10x faster                                                  |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.01x slower                                                |
| html5lib       | 36.6 ms                                                | 31.4 ms: 1.17x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.27x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 62.0 ms: 1.14x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 192 ms: 1.11x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 413 ms: 1.11x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 438 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| async_tree_io                    | 507 ms                                                 | 539 ms: 1.06x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 617 ms: 1.20x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 653 ms: 1.37x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.8 ms: 1.22x faster                                                 |
| float          | 56.2 ms                                                | 48.7 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.0 ms: 1.15x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.3 ms: 1.10x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 53.1 ms: 1.07x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.38 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 74.8 ms: 1.01x slower                                                 |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| json_loads           | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 10.9 ms: 1.25x faster                                                 |
| python_startup         | 17.0 ms                                                | 13.8 ms: 1.24x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.4 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 19.6 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.96 ms: 1.10x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 17.1 us: 1.59x faster                                                 |
| deepcopy                         | 232 us                                                 | 146 us: 1.59x faster                                                  |
| generators                       | 31.5 ms                                                | 20.3 ms: 1.55x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.36x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.27x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.11 ms: 1.27x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 10.9 ms: 1.25x faster                                                 |
| python_startup                   | 17.0 ms                                                | 13.8 ms: 1.24x faster                                                 |
| raytrace                         | 182 ms                                                 | 147 ms: 1.23x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| nbody                            | 73.9 ms                                                | 60.8 ms: 1.22x faster                                                 |
| comprehensions                   | 12.2 us                                                | 10.0 us: 1.21x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                 |
| go                               | 115 ms                                                 | 96.6 ms: 1.19x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.10 ms: 1.18x faster                                                 |
| nqueens                          | 62.9 ms                                                | 53.3 ms: 1.18x faster                                                 |
| richards_super                   | 39.1 ms                                                | 33.3 ms: 1.17x faster                                                 |
| richards                         | 35.4 ms                                                | 30.3 ms: 1.17x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                                  |
| html5lib                         | 36.6 ms                                                | 31.4 ms: 1.17x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.07 us: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.5 ms: 1.16x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 60.4 ns: 1.16x faster                                                 |
| float                            | 56.2 ms                                                | 48.7 ms: 1.16x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 68.0 ms: 1.15x faster                                                 |
| chaos                            | 41.3 ms                                                | 35.8 ms: 1.15x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 744 us: 1.15x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 67.2 ms: 1.15x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 466 ms: 1.14x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 62.0 ms: 1.14x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 902 us: 1.13x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.40 us: 1.13x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 952 ms: 1.13x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 30.4 ms: 1.13x faster                                                 |
| django_template                  | 22.2 ms                                                | 19.6 ms: 1.13x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 67.8 ms: 1.13x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 93.8 ms: 1.13x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 450 us: 1.12x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 168 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.3 ms: 1.12x faster                                                 |
| pycparser                        | 706 ms                                                 | 638 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 192 ms: 1.11x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 413 ms: 1.11x faster                                                  |
| mako                             | 7.68 ms                                                | 6.96 ms: 1.10x faster                                                 |
| 2to3                             | 178 ms                                                 | 162 ms: 1.10x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.3 ms: 1.10x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 46.5 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| sympy_str                        | 145 ms                                                 | 134 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 93.2 us: 1.08x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.5 ms: 1.08x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                                  |
| thrift                           | 466 us                                                 | 432 us: 1.08x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 70.4 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.81 ms: 1.07x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 26.9 ms: 1.07x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 53.1 ms: 1.07x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 50.7 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| fannkuch                         | 282 ms                                                 | 265 ms: 1.06x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                |
| telco                            | 4.80 ms                                                | 4.58 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.05x faster                                                |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.38 ms: 1.03x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.9 ms: 1.03x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 438 ms: 1.02x faster                                                  |
| coverage                         | 46.1 ms                                                | 45.4 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 74.8 ms: 1.01x slower                                                 |
| json                             | 2.94 ms                                                | 2.98 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.01x slower                                                |
| xml_etree_parse                  | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| pathlib                          | 22.8 ms                                                | 23.4 ms: 1.02x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.54 sec: 1.03x slower                                                |
| async_tree_io                    | 507 ms                                                 | 539 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 895 us: 1.11x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 617 ms: 1.20x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 653 ms: 1.37x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.70x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (3): pylint, async_tree_io_tg, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.99x