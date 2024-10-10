# Results vs. base

- fork: faster-cpython
- ref: more_robust_immortal
- machine: windows-amd64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.73 sec                                                                   | 1.71 sec: 1.01x faster                                                               |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 268 ms                                                                     | 257 ms: 1.04x faster                                                                 |
| async_tree_none           | 219 ms                                                                     | 212 ms: 1.03x faster                                                                 |
| async_tree_memoization    | 269 ms                                                                     | 273 ms: 1.02x slower                                                                 |
| async_generators          | 248 ms                                                                     | 253 ms: 1.02x slower                                                                 |
| asyncio_tcp               | 652 ms                                                                     | 695 ms: 1.07x slower                                                                 |
| Geometric mean            | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed_tg, coroutines, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 85.6 ms                                                                    | 80.7 ms: 1.06x faster                                                                |
| float          | 56.5 ms                                                                    | 54.8 ms: 1.03x faster                                                                |
| pidigits       | 149 ms                                                                     | 147 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                                    | 14.9 ms: 1.09x faster                                                                |
| regex_compile  | 91.8 ms                                                                    | 90.1 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                                         |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 159 us                                                                     | 149 us: 1.07x faster                                                                 |
| xml_etree_process    | 42.5 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| tomli_loads          | 1.66 sec                                                                   | 1.62 sec: 1.02x faster                                                               |
| pickle_pure_python   | 220 us                                                                     | 215 us: 1.02x faster                                                                 |
| xml_etree_parse      | 95.9 ms                                                                    | 93.9 ms: 1.02x faster                                                                |
| json_dumps           | 6.41 ms                                                                    | 6.34 ms: 1.01x faster                                                                |
| xml_etree_generate   | 59.4 ms                                                                    | 58.7 ms: 1.01x faster                                                                |
| pickle_dict          | 19.0 us                                                                    | 19.2 us: 1.01x slower                                                                |
| xml_etree_iterparse  | 66.0 ms                                                                    | 66.9 ms: 1.01x slower                                                                |
| pickle               | 7.31 us                                                                    | 7.45 us: 1.02x slower                                                                |
| unpickle             | 9.17 us                                                                    | 9.35 us: 1.02x slower                                                                |
| unpickle_list        | 2.82 us                                                                    | 2.89 us: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.19 ms                                                                    | 6.85 ms: 1.05x faster                                                                |
| django_template | 26.3 ms                                                                    | 26.7 ms: 1.02x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| scimark_lu                | 65.3 ms                                                                    | 57.4 ms: 1.14x faster                                                                |
| logging_silent            | 65.4 ns                                                                    | 60.1 ns: 1.09x faster                                                                |
| regex_v8                  | 16.2 ms                                                                    | 14.9 ms: 1.09x faster                                                                |
| json                      | 4.52 ms                                                                    | 4.15 ms: 1.09x faster                                                                |
| deepcopy_memo             | 21.6 us                                                                    | 19.9 us: 1.08x faster                                                                |
| scimark_sor               | 94.8 ms                                                                    | 88.0 ms: 1.08x faster                                                                |
| spectral_norm             | 74.6 ms                                                                    | 69.3 ms: 1.08x faster                                                                |
| scimark_monte_carlo       | 50.4 ms                                                                    | 46.9 ms: 1.07x faster                                                                |
| unpickle_pure_python      | 159 us                                                                     | 149 us: 1.07x faster                                                                 |
| fannkuch                  | 297 ms                                                                     | 279 ms: 1.06x faster                                                                 |
| nbody                     | 85.6 ms                                                                    | 80.7 ms: 1.06x faster                                                                |
| scimark_fft               | 215 ms                                                                     | 202 ms: 1.06x faster                                                                 |
| mako                      | 7.19 ms                                                                    | 6.85 ms: 1.05x faster                                                                |
| go                        | 91.7 ms                                                                    | 87.4 ms: 1.05x faster                                                                |
| hexiom                    | 4.52 ms                                                                    | 4.32 ms: 1.05x faster                                                                |
| pprint_pformat            | 1.18 sec                                                                   | 1.13 sec: 1.04x faster                                                               |
| raytrace                  | 201 ms                                                                     | 192 ms: 1.04x faster                                                                 |
| pprint_safe_repr          | 575 ms                                                                     | 552 ms: 1.04x faster                                                                 |
| async_tree_memoization_tg | 268 ms                                                                     | 257 ms: 1.04x faster                                                                 |
| pyflate                   | 332 ms                                                                     | 319 ms: 1.04x faster                                                                 |
| richards_super            | 38.1 ms                                                                    | 36.6 ms: 1.04x faster                                                                |
| chaos                     | 45.5 ms                                                                    | 43.8 ms: 1.04x faster                                                                |
| crypto_pyaes              | 50.1 ms                                                                    | 48.3 ms: 1.04x faster                                                                |
| richards                  | 33.7 ms                                                                    | 32.5 ms: 1.04x faster                                                                |
| xml_etree_process         | 42.5 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| async_tree_none           | 219 ms                                                                     | 212 ms: 1.03x faster                                                                 |
| float                     | 56.5 ms                                                                    | 54.8 ms: 1.03x faster                                                                |
| logging_simple            | 6.62 us                                                                    | 6.45 us: 1.03x faster                                                                |
| sqlglot_parse             | 936 us                                                                     | 912 us: 1.03x faster                                                                 |
| tomli_loads               | 1.66 sec                                                                   | 1.62 sec: 1.02x faster                                                               |
| pickle_pure_python        | 220 us                                                                     | 215 us: 1.02x faster                                                                 |
| nqueens                   | 65.5 ms                                                                    | 64.1 ms: 1.02x faster                                                                |
| meteor_contest            | 78.1 ms                                                                    | 76.4 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult   | 2.72 ms                                                                    | 2.66 ms: 1.02x faster                                                                |
| xml_etree_parse           | 95.9 ms                                                                    | 93.9 ms: 1.02x faster                                                                |
| deltablue                 | 2.33 ms                                                                    | 2.29 ms: 1.02x faster                                                                |
| regex_compile             | 91.8 ms                                                                    | 90.1 ms: 1.02x faster                                                                |
| generators                | 22.1 ms                                                                    | 21.7 ms: 1.02x faster                                                                |
| sympy_expand              | 312 ms                                                                     | 308 ms: 1.02x faster                                                                 |
| logging_format            | 7.02 us                                                                    | 6.91 us: 1.02x faster                                                                |
| comprehensions            | 12.0 us                                                                    | 11.8 us: 1.01x faster                                                                |
| sympy_sum                 | 91.5 ms                                                                    | 90.2 ms: 1.01x faster                                                                |
| deepcopy_reduce           | 1.99 us                                                                    | 1.97 us: 1.01x faster                                                                |
| json_dumps                | 6.41 ms                                                                    | 6.34 ms: 1.01x faster                                                                |
| thrift                    | 528 us                                                                     | 522 us: 1.01x faster                                                                 |
| docutils                  | 1.73 sec                                                                   | 1.71 sec: 1.01x faster                                                               |
| xml_etree_generate        | 59.4 ms                                                                    | 58.7 ms: 1.01x faster                                                                |
| pidigits                  | 149 ms                                                                     | 147 ms: 1.01x faster                                                                 |
| sympy_integrate           | 13.7 ms                                                                    | 13.5 ms: 1.01x faster                                                                |
| sqlglot_optimize          | 37.9 ms                                                                    | 37.6 ms: 1.01x faster                                                                |
| deepcopy                  | 193 us                                                                     | 192 us: 1.01x faster                                                                 |
| sqlglot_transpile         | 1.15 ms                                                                    | 1.14 ms: 1.01x faster                                                                |
| bench_mp_pool             | 69.2 ms                                                                    | 69.6 ms: 1.01x slower                                                                |
| unpack_sequence           | 39.9 ns                                                                    | 40.2 ns: 1.01x slower                                                                |
| pickle_dict               | 19.0 us                                                                    | 19.2 us: 1.01x slower                                                                |
| xml_etree_iterparse       | 66.0 ms                                                                    | 66.9 ms: 1.01x slower                                                                |
| django_template           | 26.3 ms                                                                    | 26.7 ms: 1.02x slower                                                                |
| async_tree_memoization    | 269 ms                                                                     | 273 ms: 1.02x slower                                                                 |
| async_generators          | 248 ms                                                                     | 253 ms: 1.02x slower                                                                 |
| pickle                    | 7.31 us                                                                    | 7.45 us: 1.02x slower                                                                |
| unpickle                  | 9.17 us                                                                    | 9.35 us: 1.02x slower                                                                |
| unpickle_list             | 2.82 us                                                                    | 2.89 us: 1.03x slower                                                                |
| asyncio_tcp               | 652 ms                                                                     | 695 ms: 1.07x slower                                                                 |
| mdp                       | 1.47 sec                                                                   | 1.58 sec: 1.07x slower                                                               |
| Geometric mean            | (ref)                                                                      | 1.02x faster                                                                         |

Benchmark hidden because not significant (31): async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg, pylint, regex_effbot, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, genshi_xml, coroutines, sympy_str, gc_traversal, 2to3, pathlib, python_startup, genshi_text, sqlglot_normalize, dulwich_log, pickle_list, regex_dna, coverage, telco, asyncio_tcp_ssl, create_gc_cycles, html5lib, tornado_http, python_startup_no_site, sqlite_synth, pycparser, json_loads, bench_thread_pool

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown