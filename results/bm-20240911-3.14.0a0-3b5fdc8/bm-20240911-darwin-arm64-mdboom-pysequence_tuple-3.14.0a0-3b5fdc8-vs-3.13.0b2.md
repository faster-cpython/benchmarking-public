# Results vs. 3.13.0b2

- fork: mdboom
- ref: pysequence_tuple
- machine: darwin-arm64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.01x faster
- HPT reliability: 75.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 158 ms: 1.02x faster                                              |
| docutils       | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                            |
| html5lib       | 31.2 ms                                                    | 30.3 ms: 1.03x faster                                             |
| tornado_http   | 66.7 ms                                                    | 81.7 ms: 1.23x slower                                             |
| Geometric mean | (ref)                                                      | 1.04x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 682 ms: 1.12x faster                                              |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                              |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                              |
| async_tree_none_tg               | 198 ms                                                     | 188 ms: 1.05x faster                                              |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                              |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                              |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                              |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 463 ms: 1.03x slower                                              |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.5 ms: 1.03x slower                                             |
| async_tree_io                    | 563 ms                                                     | 581 ms: 1.03x slower                                              |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                              |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                      |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 49.2 ms: 1.01x slower                                             |
| nbody          | 59.6 ms                                                    | 60.7 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                             |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                             |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                              |
| regex_compile  | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                      | 1.03x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.38 us: 1.01x faster                                             |
| unpickle_pure_python | 141 us                                                     | 141 us: 1.00x slower                                              |
| xml_etree_generate   | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                             |
| unpickle_list        | 2.88 us                                                    | 2.91 us: 1.01x slower                                             |
| unpickle             | 9.12 us                                                    | 9.21 us: 1.01x slower                                             |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                             |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                             |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                              |
| tomli_loads          | 1.47 sec                                                   | 1.50 sec: 1.03x slower                                            |
| json_dumps           | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                             |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                              |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.8 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (2): pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                             |
| python_startup         | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                             |
| django_template | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                             |
| genshi_xml      | 29.9 ms                                                    | 30.5 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.41x faster                                              |
| deepcopy_memo                    | 22.6 us                                                    | 16.5 us: 1.37x faster                                             |
| go                               | 101 ms                                                     | 79.2 ms: 1.27x faster                                             |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                             |
| generators                       | 22.9 ms                                                    | 20.4 ms: 1.12x faster                                             |
| async_tree_eager_io              | 766 ms                                                     | 682 ms: 1.12x faster                                              |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                              |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                            |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                              |
| async_tree_none_tg               | 198 ms                                                     | 188 ms: 1.05x faster                                              |
| richards                         | 31.8 ms                                                    | 30.3 ms: 1.05x faster                                             |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                             |
| richards_super                   | 35.2 ms                                                    | 33.5 ms: 1.05x faster                                             |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                              |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                             |
| pprint_safe_repr                 | 465 ms                                                     | 448 ms: 1.04x faster                                              |
| pprint_pformat                   | 947 ms                                                     | 919 ms: 1.03x faster                                              |
| html5lib                         | 31.2 ms                                                    | 30.3 ms: 1.03x faster                                             |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                              |
| thrift                           | 435 us                                                     | 425 us: 1.02x faster                                              |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                              |
| regex_compile                    | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                             |
| 2to3                             | 161 ms                                                     | 158 ms: 1.02x faster                                              |
| scimark_sor                      | 94.9 ms                                                    | 93.2 ms: 1.02x faster                                             |
| dulwich_log                      | 27.6 ms                                                    | 27.1 ms: 1.02x faster                                             |
| comprehensions                   | 10.2 us                                                    | 10.0 us: 1.02x faster                                             |
| coverage                         | 45.0 ms                                                    | 44.4 ms: 1.01x faster                                             |
| pickle                           | 7.48 us                                                    | 7.38 us: 1.01x faster                                             |
| logging_simple                   | 3.04 us                                                    | 3.01 us: 1.01x faster                                             |
| async_generators                 | 281 ms                                                     | 279 ms: 1.01x faster                                              |
| docutils                         | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                            |
| deltablue                        | 2.14 ms                                                    | 2.13 ms: 1.01x faster                                             |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.01x faster                                             |
| create_gc_cycles                 | 897 us                                                     | 892 us: 1.01x faster                                              |
| gc_traversal                     | 2.45 ms                                                    | 2.45 ms: 1.00x slower                                             |
| sympy_expand                     | 226 ms                                                     | 226 ms: 1.00x slower                                              |
| sqlite_synth                     | 1.55 us                                                    | 1.56 us: 1.00x slower                                             |
| bench_thread_pool                | 447 us                                                     | 449 us: 1.00x slower                                              |
| unpickle_pure_python             | 141 us                                                     | 141 us: 1.00x slower                                              |
| logging_format                   | 3.31 us                                                    | 3.32 us: 1.00x slower                                             |
| logging_silent                   | 60.1 ns                                                    | 60.5 ns: 1.01x slower                                             |
| genshi_text                      | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                             |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                              |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                              |
| xml_etree_generate               | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                             |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                             |
| django_template                  | 19.4 ms                                                    | 19.6 ms: 1.01x slower                                             |
| unpickle_list                    | 2.88 us                                                    | 2.91 us: 1.01x slower                                             |
| unpickle                         | 9.12 us                                                    | 9.21 us: 1.01x slower                                             |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                             |
| raytrace                         | 147 ms                                                     | 148 ms: 1.01x slower                                              |
| hexiom                           | 4.06 ms                                                    | 4.11 ms: 1.01x slower                                             |
| float                            | 48.6 ms                                                    | 49.2 ms: 1.01x slower                                             |
| scimark_lu                       | 66.9 ms                                                    | 67.7 ms: 1.01x slower                                             |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                             |
| json                             | 2.93 ms                                                    | 2.97 ms: 1.01x slower                                             |
| spectral_norm                    | 66.4 ms                                                    | 67.3 ms: 1.01x slower                                             |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                             |
| crypto_pyaes                     | 49.5 ms                                                    | 50.2 ms: 1.01x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                              |
| sqlglot_parse                    | 732 us                                                     | 744 us: 1.02x slower                                              |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.82 ms: 1.02x slower                                             |
| meteor_contest                   | 70.3 ms                                                    | 71.5 ms: 1.02x slower                                             |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.02x slower                                             |
| sqlglot_transpile                | 891 us                                                     | 907 us: 1.02x slower                                              |
| nbody                            | 59.6 ms                                                    | 60.7 ms: 1.02x slower                                             |
| genshi_xml                       | 29.9 ms                                                    | 30.5 ms: 1.02x slower                                             |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                              |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.4 ms: 1.02x slower                                             |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                             |
| pathlib                          | 23.3 ms                                                    | 23.8 ms: 1.02x slower                                             |
| chaos                            | 34.0 ms                                                    | 34.9 ms: 1.03x slower                                             |
| tomli_loads                      | 1.47 sec                                                   | 1.50 sec: 1.03x slower                                            |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 463 ms: 1.03x slower                                              |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.5 ms: 1.03x slower                                             |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.14 sec: 1.03x slower                                            |
| json_dumps                       | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                             |
| scimark_fft                      | 181 ms                                                     | 186 ms: 1.03x slower                                              |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                              |
| async_tree_io                    | 563 ms                                                     | 581 ms: 1.03x slower                                              |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.8 ms: 1.03x slower                                             |
| bench_mp_pool                    | 47.2 ms                                                    | 49.2 ms: 1.04x slower                                             |
| telco                            | 4.60 ms                                                    | 4.81 ms: 1.05x slower                                             |
| typing_runtime_protocols         | 87.6 us                                                    | 91.7 us: 1.05x slower                                             |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                              |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                              |
| python_startup_no_site           | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                             |
| python_startup                   | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                             |
| tornado_http                     | 66.7 ms                                                    | 81.7 ms: 1.23x slower                                             |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                      |

Benchmark hidden because not significant (15): async_tree_io_tg, async_tree_cpu_io_mixed, sympy_sum, asyncio_websockets, asyncio_tcp_ssl, sympy_str, pickle_list, pidigits, pickle_dict, mako, pyflate, async_tree_eager_memoization, pycparser, asyncio_tcp, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: unpack_sequence

# HPT report

- Reliability score: 75.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.59x