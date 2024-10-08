# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc2
- machine: darwin-arm64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 162 ms: 1.01x slower                                         |
| chameleon      | 4.27 ms                                                    | 4.37 ms: 1.02x slower                                        |
| docutils       | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                       |
| html5lib       | 31.2 ms                                                    | 31.9 ms: 1.02x slower                                        |
| tornado_http   | 66.7 ms                                                    | 85.1 ms: 1.28x slower                                        |
| Geometric mean | (ref)                                                      | 1.07x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                         |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                        |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.02x slower                                         |
| async_tree_eager                 | 60.3 ms                                                    | 61.9 ms: 1.03x slower                                        |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                 |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                        |
| nbody          | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                      | 1.00x slower                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                         |
| regex_compile  | 68.5 ms                                                    | 68.8 ms: 1.00x slower                                        |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                        |
| regex_effbot   | 2.58 ms                                                    | 2.61 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                      | 1.00x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 16.8 us                                                    | 16.7 us: 1.01x faster                                        |
| tomli_loads          | 1.47 sec                                                   | 1.46 sec: 1.01x faster                                       |
| xml_etree_generate   | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                        |
| pickle_dict          | 18.3 us                                                    | 18.4 us: 1.01x slower                                        |
| unpickle_list        | 2.88 us                                                    | 2.91 us: 1.01x slower                                        |
| unpickle             | 9.12 us                                                    | 9.21 us: 1.01x slower                                        |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                         |
| json_dumps           | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                        |
| xml_etree_process    | 37.1 ms                                                    | 37.6 ms: 1.02x slower                                        |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                         |
| pickle_list          | 2.96 us                                                    | 3.01 us: 1.02x slower                                        |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                         |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.0 ms: 1.02x slower                                        |
| pickle               | 7.48 us                                                    | 7.70 us: 1.03x slower                                        |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.7 ms: 1.12x slower                                        |
| python_startup         | 15.2 ms                                                    | 17.2 ms: 1.13x slower                                        |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                        |
| mako            | 6.99 ms                                                    | 7.08 ms: 1.01x slower                                        |
| genshi_text     | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                        |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                       |
| richards_super                   | 35.2 ms                                                    | 34.6 ms: 1.02x faster                                        |
| richards                         | 31.8 ms                                                    | 31.5 ms: 1.01x faster                                        |
| dulwich_log                      | 27.6 ms                                                    | 27.3 ms: 1.01x faster                                        |
| coverage                         | 45.0 ms                                                    | 44.7 ms: 1.01x faster                                        |
| json_loads                       | 16.8 us                                                    | 16.7 us: 1.01x faster                                        |
| tomli_loads                      | 1.47 sec                                                   | 1.46 sec: 1.01x faster                                       |
| float                            | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                        |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                        |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                         |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                         |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                        |
| regex_compile                    | 68.5 ms                                                    | 68.8 ms: 1.00x slower                                        |
| sympy_integrate                  | 10.3 ms                                                    | 10.4 ms: 1.00x slower                                        |
| pyflate                          | 321 ms                                                     | 322 ms: 1.00x slower                                         |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.07 sec: 1.01x slower                                       |
| pprint_pformat                   | 947 ms                                                     | 953 ms: 1.01x slower                                         |
| scimark_sor                      | 94.9 ms                                                    | 95.5 ms: 1.01x slower                                        |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                        |
| genshi_xml                       | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                        |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                        |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.8 ms: 1.01x slower                                        |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                        |
| pprint_safe_repr                 | 465 ms                                                     | 468 ms: 1.01x slower                                         |
| xml_etree_generate               | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                        |
| 2to3                             | 161 ms                                                     | 162 ms: 1.01x slower                                         |
| pickle_dict                      | 18.3 us                                                    | 18.4 us: 1.01x slower                                        |
| sympy_sum                        | 69.2 ms                                                    | 69.8 ms: 1.01x slower                                        |
| unpickle_list                    | 2.88 us                                                    | 2.91 us: 1.01x slower                                        |
| crypto_pyaes                     | 49.5 ms                                                    | 49.9 ms: 1.01x slower                                        |
| unpickle                         | 9.12 us                                                    | 9.21 us: 1.01x slower                                        |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                         |
| logging_silent                   | 60.1 ns                                                    | 60.7 ns: 1.01x slower                                        |
| spectral_norm                    | 66.4 ms                                                    | 67.0 ms: 1.01x slower                                        |
| deltablue                        | 2.14 ms                                                    | 2.16 ms: 1.01x slower                                        |
| sqlglot_transpile                | 891 us                                                     | 899 us: 1.01x slower                                         |
| regex_effbot                     | 2.58 ms                                                    | 2.61 ms: 1.01x slower                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                         |
| sqlglot_parse                    | 732 us                                                     | 739 us: 1.01x slower                                         |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                         |
| sympy_str                        | 131 ms                                                     | 133 ms: 1.01x slower                                         |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                         |
| chaos                            | 34.0 ms                                                    | 34.4 ms: 1.01x slower                                        |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                        |
| scimark_lu                       | 66.9 ms                                                    | 67.6 ms: 1.01x slower                                        |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                        |
| json_dumps                       | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                        |
| mako                             | 6.99 ms                                                    | 7.08 ms: 1.01x slower                                        |
| async_generators                 | 281 ms                                                     | 285 ms: 1.01x slower                                         |
| sqlglot_normalize                | 166 ms                                                     | 168 ms: 1.01x slower                                         |
| pycparser                        | 632 ms                                                     | 641 ms: 1.01x slower                                         |
| nqueens                          | 52.2 ms                                                    | 52.9 ms: 1.01x slower                                        |
| genshi_text                      | 13.9 ms                                                    | 14.1 ms: 1.01x slower                                        |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.81 ms: 1.01x slower                                        |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.02x slower                                         |
| xml_etree_process                | 37.1 ms                                                    | 37.6 ms: 1.02x slower                                        |
| deepcopy_memo                    | 22.6 us                                                    | 23.0 us: 1.02x slower                                        |
| nbody                            | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                        |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                         |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                         |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                        |
| pickle_list                      | 2.96 us                                                    | 3.01 us: 1.02x slower                                        |
| telco                            | 4.60 ms                                                    | 4.69 ms: 1.02x slower                                        |
| django_template                  | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                        |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                         |
| docutils                         | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                       |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.0 ms: 1.02x slower                                        |
| chameleon                        | 4.27 ms                                                    | 4.37 ms: 1.02x slower                                        |
| typing_runtime_protocols         | 87.6 us                                                    | 89.7 us: 1.02x slower                                        |
| html5lib                         | 31.2 ms                                                    | 31.9 ms: 1.02x slower                                        |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.03x slower                                        |
| hexiom                           | 4.06 ms                                                    | 4.16 ms: 1.03x slower                                        |
| logging_simple                   | 3.04 us                                                    | 3.12 us: 1.03x slower                                        |
| async_tree_eager                 | 60.3 ms                                                    | 61.9 ms: 1.03x slower                                        |
| bench_thread_pool                | 447 us                                                     | 460 us: 1.03x slower                                         |
| pickle                           | 7.48 us                                                    | 7.70 us: 1.03x slower                                        |
| fannkuch                         | 248 ms                                                     | 257 ms: 1.03x slower                                         |
| bench_mp_pool                    | 47.2 ms                                                    | 49.0 ms: 1.04x slower                                        |
| comprehensions                   | 10.2 us                                                    | 10.6 us: 1.05x slower                                        |
| pathlib                          | 23.3 ms                                                    | 24.6 ms: 1.05x slower                                        |
| dask                             | 221 ms                                                     | 234 ms: 1.06x slower                                         |
| flaskblogging                    | 3.61 ms                                                    | 3.96 ms: 1.10x slower                                        |
| gunicorn                         | 1.04 ms                                                    | 1.14 ms: 1.10x slower                                        |
| python_startup_no_site           | 12.3 ms                                                    | 13.7 ms: 1.12x slower                                        |
| python_startup                   | 15.2 ms                                                    | 17.2 ms: 1.13x slower                                        |
| aiohttp                          | 997 us                                                     | 1.16 ms: 1.16x slower                                        |
| mypy2                            | 379 ms                                                     | 479 ms: 1.26x slower                                         |
| tornado_http                     | 66.7 ms                                                    | 85.1 ms: 1.28x slower                                        |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                 |

Benchmark hidden because not significant (22): async_tree_io_tg, async_tree_io, async_tree_none_tg, deepcopy_reduce, thrift, async_tree_eager_io, asyncio_tcp_ssl, pidigits, create_gc_cycles, async_tree_cpu_io_mixed_tg, generators, go, async_tree_memoization_tg, deepcopy, async_tree_eager_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_memoization, pylint
Ignored benchmarks (1) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.32x