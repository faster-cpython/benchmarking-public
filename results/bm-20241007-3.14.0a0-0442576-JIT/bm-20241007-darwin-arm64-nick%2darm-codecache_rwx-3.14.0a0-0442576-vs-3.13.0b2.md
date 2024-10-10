# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 95.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 168 ms: 1.05x slower                                               |
| docutils       | 1.44 sec                                                   | 1.49 sec: 1.04x slower                                             |
| html5lib       | 31.2 ms                                                    | 32.6 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                      | 1.06x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 676 ms: 1.13x faster                                               |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.10x faster                                               |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                               |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                               |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                               |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.2 ms: 1.00x faster                                              |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                               |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                              |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                               |
| async_tree_memoization_tg        | 240 ms                                                     | 259 ms: 1.08x slower                                               |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                       |

Benchmark hidden because not significant (4): async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.4 ms: 1.05x faster                                              |
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                               |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                      | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.0 ms: 1.02x faster                                              |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                               |
| regex_effbot   | 2.58 ms                                                    | 2.61 ms: 1.01x slower                                              |
| regex_compile  | 68.5 ms                                                    | 71.8 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                      | 1.01x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                             |
| xml_etree_process    | 37.1 ms                                                    | 33.8 ms: 1.10x faster                                              |
| unpickle_pure_python | 141 us                                                     | 130 us: 1.08x faster                                               |
| xml_etree_generate   | 52.7 ms                                                    | 49.2 ms: 1.07x faster                                              |
| json_loads           | 16.8 us                                                    | 16.3 us: 1.04x faster                                              |
| pickle_pure_python   | 179 us                                                     | 175 us: 1.02x faster                                               |
| json_dumps           | 6.23 ms                                                    | 6.14 ms: 1.01x faster                                              |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                              |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.9 ms: 1.01x faster                                              |
| unpickle             | 9.12 us                                                    | 9.06 us: 1.01x faster                                              |
| pickle_list          | 2.96 us                                                    | 2.94 us: 1.01x faster                                              |
| pickle               | 7.48 us                                                    | 7.44 us: 1.01x faster                                              |
| unpickle_list        | 2.88 us                                                    | 2.99 us: 1.04x slower                                              |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.9 ms: 1.11x slower                                              |
| python_startup_no_site | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.39 ms: 1.09x faster                                              |
| django_template | 19.4 ms                                                    | 20.2 ms: 1.04x slower                                              |
| genshi_text     | 13.9 ms                                                    | 14.6 ms: 1.05x slower                                              |
| genshi_xml      | 29.9 ms                                                    | 31.8 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.69x faster                                               |
| deepcopy_memo                    | 22.6 us                                                    | 16.2 us: 1.39x faster                                              |
| deepcopy                         | 204 us                                                     | 148 us: 1.38x faster                                               |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                              |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                             |
| async_tree_eager_io              | 766 ms                                                     | 676 ms: 1.13x faster                                               |
| xml_etree_process                | 37.1 ms                                                    | 33.8 ms: 1.10x faster                                              |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.10x faster                                               |
| mako                             | 6.99 ms                                                    | 6.39 ms: 1.09x faster                                              |
| scimark_sor                      | 94.9 ms                                                    | 87.4 ms: 1.09x faster                                              |
| unpickle_pure_python             | 141 us                                                     | 130 us: 1.08x faster                                               |
| go                               | 101 ms                                                     | 93.4 ms: 1.08x faster                                              |
| xml_etree_generate               | 52.7 ms                                                    | 49.2 ms: 1.07x faster                                              |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                               |
| pathlib                          | 23.3 ms                                                    | 21.9 ms: 1.06x faster                                              |
| mdp                              | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                             |
| float                            | 48.6 ms                                                    | 46.4 ms: 1.05x faster                                              |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                               |
| thrift                           | 435 us                                                     | 417 us: 1.04x faster                                               |
| scimark_lu                       | 66.9 ms                                                    | 64.1 ms: 1.04x faster                                              |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                               |
| richards                         | 31.8 ms                                                    | 30.7 ms: 1.04x faster                                              |
| json_loads                       | 16.8 us                                                    | 16.3 us: 1.04x faster                                              |
| coverage                         | 45.0 ms                                                    | 43.6 ms: 1.03x faster                                              |
| richards_super                   | 35.2 ms                                                    | 34.1 ms: 1.03x faster                                              |
| json                             | 2.93 ms                                                    | 2.85 ms: 1.03x faster                                              |
| pickle_pure_python               | 179 us                                                     | 175 us: 1.02x faster                                               |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 460 ms: 1.02x faster                                               |
| regex_v8                         | 17.3 ms                                                    | 17.0 ms: 1.02x faster                                              |
| json_dumps                       | 6.23 ms                                                    | 6.14 ms: 1.01x faster                                              |
| sqlite_synth                     | 1.55 us                                                    | 1.53 us: 1.01x faster                                              |
| pyflate                          | 321 ms                                                     | 317 ms: 1.01x faster                                               |
| pickle_dict                      | 18.3 us                                                    | 18.1 us: 1.01x faster                                              |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                               |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.9 ms: 1.01x faster                                              |
| unpickle                         | 9.12 us                                                    | 9.06 us: 1.01x faster                                              |
| pickle_list                      | 2.96 us                                                    | 2.94 us: 1.01x faster                                              |
| telco                            | 4.60 ms                                                    | 4.57 ms: 1.01x faster                                              |
| pickle                           | 7.48 us                                                    | 7.44 us: 1.01x faster                                              |
| logging_format                   | 3.31 us                                                    | 3.30 us: 1.00x faster                                              |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.2 ms: 1.00x faster                                              |
| logging_simple                   | 3.04 us                                                    | 3.03 us: 1.00x faster                                              |
| create_gc_cycles                 | 897 us                                                     | 894 us: 1.00x faster                                               |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                               |
| pprint_safe_repr                 | 465 ms                                                     | 467 ms: 1.00x slower                                               |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.07 sec: 1.01x slower                                             |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                               |
| spectral_norm                    | 66.4 ms                                                    | 66.9 ms: 1.01x slower                                              |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                              |
| regex_effbot                     | 2.58 ms                                                    | 2.61 ms: 1.01x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                               |
| logging_silent                   | 60.1 ns                                                    | 60.9 ns: 1.01x slower                                              |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                              |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                               |
| pycparser                        | 632 ms                                                     | 649 ms: 1.03x slower                                               |
| async_generators                 | 281 ms                                                     | 289 ms: 1.03x slower                                               |
| coroutines                       | 15.8 ms                                                    | 16.3 ms: 1.03x slower                                              |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                               |
| docutils                         | 1.44 sec                                                   | 1.49 sec: 1.04x slower                                             |
| unpickle_list                    | 2.88 us                                                    | 2.99 us: 1.04x slower                                              |
| pprint_pformat                   | 947 ms                                                     | 985 ms: 1.04x slower                                               |
| dulwich_log                      | 27.6 ms                                                    | 28.7 ms: 1.04x slower                                              |
| django_template                  | 19.4 ms                                                    | 20.2 ms: 1.04x slower                                              |
| 2to3                             | 161 ms                                                     | 168 ms: 1.05x slower                                               |
| sympy_expand                     | 226 ms                                                     | 236 ms: 1.05x slower                                               |
| html5lib                         | 31.2 ms                                                    | 32.6 ms: 1.05x slower                                              |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                               |
| meteor_contest                   | 70.3 ms                                                    | 73.6 ms: 1.05x slower                                              |
| regex_compile                    | 68.5 ms                                                    | 71.8 ms: 1.05x slower                                              |
| crypto_pyaes                     | 49.5 ms                                                    | 52.0 ms: 1.05x slower                                              |
| genshi_text                      | 13.9 ms                                                    | 14.6 ms: 1.05x slower                                              |
| generators                       | 22.9 ms                                                    | 24.2 ms: 1.05x slower                                              |
| sqlglot_normalize                | 166 ms                                                     | 175 ms: 1.06x slower                                               |
| genshi_xml                       | 29.9 ms                                                    | 31.8 ms: 1.06x slower                                              |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.06x slower                                              |
| bench_thread_pool                | 447 us                                                     | 476 us: 1.07x slower                                               |
| bench_mp_pool                    | 47.2 ms                                                    | 50.7 ms: 1.08x slower                                              |
| sympy_sum                        | 69.2 ms                                                    | 74.5 ms: 1.08x slower                                              |
| sympy_str                        | 131 ms                                                     | 142 ms: 1.08x slower                                               |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.99 ms: 1.08x slower                                              |
| async_tree_memoization_tg        | 240 ms                                                     | 259 ms: 1.08x slower                                               |
| scimark_monte_carlo              | 42.5 ms                                                    | 46.2 ms: 1.09x slower                                              |
| hexiom                           | 4.06 ms                                                    | 4.42 ms: 1.09x slower                                              |
| typing_runtime_protocols         | 87.6 us                                                    | 95.8 us: 1.09x slower                                              |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.9 ms: 1.10x slower                                              |
| deltablue                        | 2.14 ms                                                    | 2.36 ms: 1.10x slower                                              |
| sqlglot_parse                    | 732 us                                                     | 808 us: 1.10x slower                                               |
| nqueens                          | 52.2 ms                                                    | 57.7 ms: 1.10x slower                                              |
| sqlglot_transpile                | 891 us                                                     | 986 us: 1.11x slower                                               |
| asyncio_tcp                      | 402 ms                                                     | 445 ms: 1.11x slower                                               |
| python_startup                   | 15.2 ms                                                    | 16.9 ms: 1.11x slower                                              |
| python_startup_no_site           | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                              |
| sympy_integrate                  | 10.3 ms                                                    | 11.8 ms: 1.14x slower                                              |
| pylint                           | 170 ms                                                     | 195 ms: 1.15x slower                                               |
| raytrace                         | 147 ms                                                     | 171 ms: 1.17x slower                                               |
| chaos                            | 34.0 ms                                                    | 39.8 ms: 1.17x slower                                              |
| comprehensions                   | 10.2 us                                                    | 12.5 us: 1.23x slower                                              |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (7): async_tree_eager_memoization_tg, async_tree_io_tg, asyncio_tcp_ssl, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: unpack_sequence

# HPT report

- Reliability score: 95.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.91x