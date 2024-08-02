# Results vs. 3.13.0b2

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: darwin-arm64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.01x slower
- HPT reliability: 54.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 159 ms: 1.01x faster                                                       |
| chameleon      | 4.27 ms                                                    | 4.38 ms: 1.03x slower                                                      |
| docutils       | 1.44 sec                                                   | 1.46 sec: 1.01x slower                                                     |
| tornado_http   | 66.7 ms                                                    | 72.4 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 742 ms: 1.03x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 355 ms: 1.01x faster                                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 328 ms: 1.01x faster                                                       |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.0 ms: 1.02x slower                                                      |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (12): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_io, async_tree_eager, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 59.3 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 139 ms: 1.08x faster                                                       |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                      |
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                      | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 98.1 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 67.7 ms: 1.06x faster                                                      |
| json_dumps           | 6.23 ms                                                    | 6.14 ms: 1.01x faster                                                      |
| tomli_loads          | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                                     |
| pickle               | 7.48 us                                                    | 7.44 us: 1.00x faster                                                      |
| xml_etree_generate   | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                      |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                       |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                                      |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.01x slower                                                       |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                      |
| unpickle             | 9.12 us                                                    | 9.67 us: 1.06x slower                                                      |
| unpickle_list        | 2.88 us                                                    | 3.26 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 10.9 ms: 1.13x faster                                                      |
| python_startup         | 15.2 ms                                                    | 13.7 ms: 1.11x faster                                                      |
| Geometric mean         | (ref)                                                      | 1.12x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 6.99 ms                                                    | 6.89 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site           | 12.3 ms                                                    | 10.9 ms: 1.13x faster                                                      |
| python_startup                   | 15.2 ms                                                    | 13.7 ms: 1.11x faster                                                      |
| crypto_pyaes                     | 49.5 ms                                                    | 45.8 ms: 1.08x faster                                                      |
| xml_etree_parse                  | 106 ms                                                     | 98.1 ms: 1.08x faster                                                      |
| regex_dna                        | 149 ms                                                     | 139 ms: 1.08x faster                                                       |
| xml_etree_iterparse              | 71.5 ms                                                    | 67.7 ms: 1.06x faster                                                      |
| telco                            | 4.60 ms                                                    | 4.40 ms: 1.05x faster                                                      |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 45.7 ms: 1.03x faster                                                      |
| async_tree_eager_io              | 766 ms                                                     | 742 ms: 1.03x faster                                                       |
| deepcopy_reduce                  | 1.82 us                                                    | 1.78 us: 1.02x faster                                                      |
| mdp                              | 1.53 sec                                                   | 1.50 sec: 1.02x faster                                                     |
| pathlib                          | 23.3 ms                                                    | 22.8 ms: 1.02x faster                                                      |
| mako                             | 6.99 ms                                                    | 6.89 ms: 1.01x faster                                                      |
| json_dumps                       | 6.23 ms                                                    | 6.14 ms: 1.01x faster                                                      |
| generators                       | 22.9 ms                                                    | 22.6 ms: 1.01x faster                                                      |
| 2to3                             | 161 ms                                                     | 159 ms: 1.01x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 355 ms: 1.01x faster                                                       |
| deepcopy                         | 204 us                                                     | 202 us: 1.01x faster                                                       |
| go                               | 101 ms                                                     | 99.7 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 328 ms: 1.01x faster                                                       |
| dulwich_log                      | 27.6 ms                                                    | 27.3 ms: 1.01x faster                                                      |
| tomli_loads                      | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                                     |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                      |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.01x faster                                                      |
| async_generators                 | 281 ms                                                     | 279 ms: 1.01x faster                                                       |
| nbody                            | 59.6 ms                                                    | 59.3 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.76 ms: 1.00x faster                                                      |
| pickle                           | 7.48 us                                                    | 7.44 us: 1.00x faster                                                      |
| sqlite_synth                     | 1.55 us                                                    | 1.55 us: 1.00x faster                                                      |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                       |
| richards_super                   | 35.2 ms                                                    | 35.3 ms: 1.00x slower                                                      |
| spectral_norm                    | 66.4 ms                                                    | 66.5 ms: 1.00x slower                                                      |
| scimark_sor                      | 94.9 ms                                                    | 95.1 ms: 1.00x slower                                                      |
| deltablue                        | 2.14 ms                                                    | 2.15 ms: 1.00x slower                                                      |
| sympy_str                        | 131 ms                                                     | 132 ms: 1.00x slower                                                       |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.00x slower                                                       |
| logging_silent                   | 60.1 ns                                                    | 60.5 ns: 1.01x slower                                                      |
| logging_format                   | 3.31 us                                                    | 3.33 us: 1.01x slower                                                      |
| sqlglot_parse                    | 732 us                                                     | 737 us: 1.01x slower                                                       |
| raytrace                         | 147 ms                                                     | 148 ms: 1.01x slower                                                       |
| xml_etree_generate               | 52.7 ms                                                    | 53.1 ms: 1.01x slower                                                      |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                       |
| pprint_safe_repr                 | 465 ms                                                     | 469 ms: 1.01x slower                                                       |
| coverage                         | 45.0 ms                                                    | 45.4 ms: 1.01x slower                                                      |
| thrift                           | 435 us                                                     | 440 us: 1.01x slower                                                       |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                                      |
| sqlglot_transpile                | 891 us                                                     | 900 us: 1.01x slower                                                       |
| richards                         | 31.8 ms                                                    | 32.2 ms: 1.01x slower                                                      |
| hexiom                           | 4.06 ms                                                    | 4.10 ms: 1.01x slower                                                      |
| nqueens                          | 52.2 ms                                                    | 52.8 ms: 1.01x slower                                                      |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.01x slower                                                       |
| scimark_lu                       | 66.9 ms                                                    | 67.8 ms: 1.01x slower                                                      |
| deepcopy_memo                    | 22.6 us                                                    | 22.9 us: 1.01x slower                                                      |
| docutils                         | 1.44 sec                                                   | 1.46 sec: 1.01x slower                                                     |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.0 ms: 1.02x slower                                                      |
| typing_runtime_protocols         | 87.6 us                                                    | 88.9 us: 1.02x slower                                                      |
| meteor_contest                   | 70.3 ms                                                    | 71.5 ms: 1.02x slower                                                      |
| gc_traversal                     | 2.45 ms                                                    | 2.49 ms: 1.02x slower                                                      |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                       |
| chaos                            | 34.0 ms                                                    | 34.7 ms: 1.02x slower                                                      |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                      |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.32 sec: 1.02x slower                                                     |
| chameleon                        | 4.27 ms                                                    | 4.38 ms: 1.03x slower                                                      |
| bench_thread_pool                | 447 us                                                     | 461 us: 1.03x slower                                                       |
| json                             | 2.93 ms                                                    | 3.03 ms: 1.04x slower                                                      |
| coroutines                       | 15.8 ms                                                    | 16.4 ms: 1.04x slower                                                      |
| fannkuch                         | 248 ms                                                     | 258 ms: 1.04x slower                                                       |
| comprehensions                   | 10.2 us                                                    | 10.6 us: 1.05x slower                                                      |
| create_gc_cycles                 | 897 us                                                     | 946 us: 1.05x slower                                                       |
| unpickle                         | 9.12 us                                                    | 9.67 us: 1.06x slower                                                      |
| aiohttp                          | 997 us                                                     | 1.08 ms: 1.08x slower                                                      |
| tornado_http                     | 66.7 ms                                                    | 72.4 ms: 1.09x slower                                                      |
| gunicorn                         | 1.04 ms                                                    | 1.13 ms: 1.09x slower                                                      |
| unpickle_list                    | 2.88 us                                                    | 3.26 us: 1.13x slower                                                      |
| mypy2                            | 379 ms                                                     | 458 ms: 1.21x slower                                                       |
| flaskblogging                    | 3.61 ms                                                    | 5.18 ms: 1.44x slower                                                      |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (32): async_tree_memoization, async_tree_none_tg, dask, asyncio_tcp, pylint, async_tree_cpu_io_mixed, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_io, pickle_dict, logging_simple, genshi_text, scimark_monte_carlo, pyflate, float, pidigits, xml_etree_process, genshi_xml, sqlglot_normalize, django_template, async_tree_eager, pprint_pformat, pycparser, html5lib, regex_compile, sympy_sum, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_none, sqlglot_optimize, async_tree_cpu_io_mixed_tg, async_tree_io_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 54.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x