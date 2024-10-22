# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.04x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 179 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                               | 1.62 sec: 1.12x slower                                                |
| html5lib       | 36.6 ms                                                | 34.5 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 229 ms: 1.27x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.16x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 242 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.8 ms: 1.09x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 338 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 367 ms: 1.02x faster                                                  |
| async_generators                 | 294 ms                                                 | 297 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.03x slower                                                |
| async_tree_io                    | 507 ms                                                 | 543 ms: 1.07x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 636 ms: 1.24x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 675 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                 |
| nbody          | 73.9 ms                                                | 63.8 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_compile  | 78.5 ms                                                | 74.8 ms: 1.05x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| regex_v8       | 16.9 ms                                                | 16.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.26 sec: 1.23x faster                                                |
| unpickle_pure_python | 163 us                                                 | 134 us: 1.22x faster                                                  |
| pickle_pure_python   | 213 us                                                 | 179 us: 1.19x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 34.4 ms: 1.19x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 50.3 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 71.7 ms: 1.03x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.50 ms: 1.01x faster                                                 |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 14.3 ms: 1.19x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 11.6 ms: 1.18x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.50 ms: 1.18x faster                                                 |
| genshi_text     | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                 |
| django_template | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 42.1 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.2 us: 1.68x faster                                                 |
| deepcopy                         | 232 us                                                 | 155 us: 1.50x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.37x faster                                                 |
| generators                       | 31.5 ms                                                | 24.5 ms: 1.29x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 229 ms: 1.27x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.26 sec: 1.23x faster                                                |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 134 us: 1.22x faster                                                  |
| float                            | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 88.0 ms: 1.20x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 179 us: 1.19x faster                                                  |
| python_startup                   | 17.0 ms                                                | 14.3 ms: 1.19x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 34.4 ms: 1.19x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.02 us: 1.18x faster                                                 |
| mako                             | 7.68 ms                                                | 6.50 ms: 1.18x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 11.6 ms: 1.18x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 65.6 ms: 1.17x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.8 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.16x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.32 ms: 1.16x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.33 us: 1.16x faster                                                 |
| go                               | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 62.1 ns: 1.13x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 50.3 ms: 1.13x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 242 ms: 1.12x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 69.7 ms: 1.11x faster                                                 |
| raytrace                         | 182 ms                                                 | 164 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 126 ms: 1.10x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.8 ms: 1.09x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 469 us: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                  |
| thrift                           | 466 us                                                 | 434 us: 1.07x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| html5lib                         | 36.6 ms                                                | 34.5 ms: 1.06x faster                                                 |
| nqueens                          | 62.9 ms                                                | 59.2 ms: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.07 sec: 1.06x faster                                                |
| typing_runtime_protocols         | 101 us                                                 | 95.8 us: 1.05x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 48.0 ms: 1.05x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 74.8 ms: 1.05x faster                                                 |
| fannkuch                         | 282 ms                                                 | 269 ms: 1.05x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 52.1 ms: 1.04x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 512 ms: 1.04x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 194 ms: 1.04x faster                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 49.1 ms: 1.04x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.6 ms: 1.03x faster                                                 |
| telco                            | 4.80 ms                                                | 4.64 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 71.7 ms: 1.03x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 338 ms: 1.03x faster                                                  |
| chaos                            | 41.3 ms                                                | 40.1 ms: 1.03x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 1.05 sec: 1.03x faster                                                |
| hexiom                           | 4.85 ms                                                | 4.72 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 367 ms: 1.02x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.2 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 185 ms: 1.02x faster                                                  |
| pycparser                        | 706 ms                                                 | 695 ms: 1.02x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.50 ms: 1.01x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| regex_v8                         | 16.9 ms                                                | 16.9 ms: 1.01x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                 |
| async_generators                 | 294 ms                                                 | 297 ms: 1.01x slower                                                  |
| 2to3                             | 178 ms                                                 | 179 ms: 1.01x slower                                                  |
| sympy_str                        | 145 ms                                                 | 147 ms: 1.01x slower                                                  |
| meteor_contest                   | 73.8 ms                                                | 74.6 ms: 1.01x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.2 us: 1.02x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 252 ms: 1.02x slower                                                  |
| sympy_sum                        | 75.6 ms                                                | 77.3 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.03x slower                                                |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.08 ms: 1.03x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 36.0 ms: 1.03x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.5 ms: 1.03x slower                                                 |
| django_template                  | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                 |
| comprehensions                   | 12.2 us                                                | 12.7 us: 1.04x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.9 ms: 1.05x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 543 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 893 us: 1.11x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.62 sec: 1.12x slower                                                |
| pylint                           | 181 ms                                                 | 205 ms: 1.13x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 42.1 ms: 1.23x slower                                                 |
| richards_super                   | 39.1 ms                                                | 48.1 ms: 1.23x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 636 ms: 1.24x slower                                                  |
| richards                         | 35.4 ms                                                | 45.9 ms: 1.29x slower                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 675 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (8): asyncio_tcp, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, json, sqlglot_parse, xml_etree_parse, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x