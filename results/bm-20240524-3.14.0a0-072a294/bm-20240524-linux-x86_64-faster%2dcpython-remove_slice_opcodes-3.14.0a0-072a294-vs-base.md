# Results vs. base

- fork: faster-cpython
- ref: remove_slice_opcodes
- machine: linux-x86_64
- commit hash: 072a294
- commit date: 2024-05-24
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                | 271 ms: 1.01x slower                                                            |
| chameleon      | 7.14 ms                                                               | 7.05 ms: 1.01x faster                                                           |
| html5lib       | 67.2 ms                                                               | 67.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg | 356 ms                                                                | 340 ms: 1.05x faster                                                            |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 85.2 ms                                                               | 86.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.71 ms                                                               | 3.78 ms: 1.02x slower                                                           |
| regex_v8       | 25.2 ms                                                               | 25.9 ms: 1.03x slower                                                           |
| regex_dna      | 222 ms                                                                | 230 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle              | 12.0 us                                                               | 11.6 us: 1.03x faster                                                           |
| json_loads          | 28.9 us                                                               | 29.0 us: 1.00x slower                                                           |
| pickle_dict         | 34.8 us                                                               | 34.9 us: 1.00x slower                                                           |
| xml_etree_process   | 60.0 ms                                                               | 60.3 ms: 1.00x slower                                                           |
| pickle_pure_python  | 302 us                                                                | 304 us: 1.01x slower                                                            |
| xml_etree_parse     | 158 ms                                                                | 161 ms: 1.02x slower                                                            |
| xml_etree_iterparse | 105 ms                                                                | 107 ms: 1.02x slower                                                            |
| tomli_loads         | 2.12 sec                                                              | 2.16 sec: 1.02x slower                                                          |
| json_dumps          | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                           |
| unpickle_list       | 5.36 us                                                               | 5.60 us: 1.04x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): unpickle, unpickle_pure_python, pickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.14 ms: 1.01x slower                                                           |
| python_startup         | 10.4 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                               | 52.1 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg      | 356 ms                                                                | 340 ms: 1.05x faster                                                            |
| pickle                  | 12.0 us                                                               | 11.6 us: 1.03x faster                                                           |
| meteor_contest          | 111 ms                                                                | 109 ms: 1.02x faster                                                            |
| richards                | 48.6 ms                                                               | 47.5 ms: 1.02x faster                                                           |
| richards_super          | 55.2 ms                                                               | 54.3 ms: 1.02x faster                                                           |
| chameleon               | 7.14 ms                                                               | 7.05 ms: 1.01x faster                                                           |
| telco                   | 8.49 ms                                                               | 8.40 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult | 5.09 ms                                                               | 5.05 ms: 1.01x faster                                                           |
| crypto_pyaes            | 75.5 ms                                                               | 75.0 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl         | 1.85 sec                                                              | 1.85 sec: 1.00x faster                                                          |
| bench_thread_pool       | 838 us                                                                | 835 us: 1.00x faster                                                            |
| dulwich_log             | 65.5 ms                                                               | 65.4 ms: 1.00x faster                                                           |
| hexiom                  | 6.10 ms                                                               | 6.12 ms: 1.00x slower                                                           |
| json_loads              | 28.9 us                                                               | 29.0 us: 1.00x slower                                                           |
| async_generators        | 445 ms                                                                | 447 ms: 1.00x slower                                                            |
| sqlglot_normalize       | 109 ms                                                                | 110 ms: 1.00x slower                                                            |
| go                      | 144 ms                                                                | 144 ms: 1.00x slower                                                            |
| pickle_dict             | 34.8 us                                                               | 34.9 us: 1.00x slower                                                           |
| deepcopy_reduce         | 3.26 us                                                               | 3.27 us: 1.00x slower                                                           |
| xml_etree_process       | 60.0 ms                                                               | 60.3 ms: 1.00x slower                                                           |
| chaos                   | 59.6 ms                                                               | 60.0 ms: 1.01x slower                                                           |
| python_startup_no_site  | 7.10 ms                                                               | 7.14 ms: 1.01x slower                                                           |
| sympy_expand            | 469 ms                                                                | 472 ms: 1.01x slower                                                            |
| python_startup          | 10.4 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| sqlglot_optimize        | 54.5 ms                                                               | 54.9 ms: 1.01x slower                                                           |
| pathlib                 | 16.6 ms                                                               | 16.7 ms: 1.01x slower                                                           |
| generators              | 29.3 ms                                                               | 29.5 ms: 1.01x slower                                                           |
| pprint_pformat          | 1.54 sec                                                              | 1.55 sec: 1.01x slower                                                          |
| deepcopy                | 363 us                                                                | 366 us: 1.01x slower                                                            |
| pickle_pure_python      | 302 us                                                                | 304 us: 1.01x slower                                                            |
| html5lib                | 67.2 ms                                                               | 67.8 ms: 1.01x slower                                                           |
| pprint_safe_repr        | 747 ms                                                                | 753 ms: 1.01x slower                                                            |
| 2to3                    | 269 ms                                                                | 271 ms: 1.01x slower                                                            |
| logging_format          | 6.42 us                                                               | 6.49 us: 1.01x slower                                                           |
| nbody                   | 85.2 ms                                                               | 86.0 ms: 1.01x slower                                                           |
| logging_silent          | 103 ns                                                                | 104 ns: 1.01x slower                                                            |
| deltablue               | 3.28 ms                                                               | 3.32 ms: 1.01x slower                                                           |
| sqlglot_transpile       | 1.61 ms                                                               | 1.63 ms: 1.01x slower                                                           |
| genshi_xml              | 51.4 ms                                                               | 52.1 ms: 1.02x slower                                                           |
| scimark_fft             | 360 ms                                                                | 365 ms: 1.02x slower                                                            |
| pyflate                 | 483 ms                                                                | 491 ms: 1.02x slower                                                            |
| raytrace                | 265 ms                                                                | 269 ms: 1.02x slower                                                            |
| xml_etree_parse         | 158 ms                                                                | 161 ms: 1.02x slower                                                            |
| xml_etree_iterparse     | 105 ms                                                                | 107 ms: 1.02x slower                                                            |
| tomli_loads             | 2.12 sec                                                              | 2.16 sec: 1.02x slower                                                          |
| nqueens                 | 81.4 ms                                                               | 82.9 ms: 1.02x slower                                                           |
| json                    | 5.27 ms                                                               | 5.37 ms: 1.02x slower                                                           |
| gc_traversal            | 3.79 ms                                                               | 3.87 ms: 1.02x slower                                                           |
| sqlglot_parse           | 1.30 ms                                                               | 1.33 ms: 1.02x slower                                                           |
| regex_effbot            | 3.71 ms                                                               | 3.78 ms: 1.02x slower                                                           |
| logging_simple          | 5.77 us                                                               | 5.90 us: 1.02x slower                                                           |
| deepcopy_memo           | 38.9 us                                                               | 39.8 us: 1.02x slower                                                           |
| scimark_lu              | 114 ms                                                                | 117 ms: 1.02x slower                                                            |
| json_dumps              | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                           |
| regex_v8                | 25.2 ms                                                               | 25.9 ms: 1.03x slower                                                           |
| fannkuch                | 403 ms                                                                | 416 ms: 1.03x slower                                                            |
| regex_dna               | 222 ms                                                                | 230 ms: 1.04x slower                                                            |
| unpickle_list           | 5.36 us                                                               | 5.60 us: 1.04x slower                                                           |
| create_gc_cycles        | 1.77 ms                                                               | 1.87 ms: 1.05x slower                                                           |
| pycparser               | 1.17 sec                                                              | 1.25 sec: 1.06x slower                                                          |
| mdp                     | 2.53 sec                                                              | 2.78 sec: 1.10x slower                                                          |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (37): async_tree_io_tg, flaskblogging, async_tree_memoization_tg, regex_compile, typing_runtime_protocols, thrift, django_template, coverage, comprehensions, tornado_http, pylint, coroutines, async_tree_none, docutils, unpickle, bench_mp_pool, unpickle_pure_python, pidigits, dask, sympy_integrate, mako, asyncio_websockets, pickle_list, scimark_monte_carlo, sympy_str, asyncio_tcp, float, xml_etree_generate, sympy_sum, scimark_sor, spectral_norm, genshi_text, sqlite_synth, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x