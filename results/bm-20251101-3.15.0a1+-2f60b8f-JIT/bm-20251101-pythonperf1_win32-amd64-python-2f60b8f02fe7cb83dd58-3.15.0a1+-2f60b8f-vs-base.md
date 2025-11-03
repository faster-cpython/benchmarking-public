# Results vs. base

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 216 ms                                                                                                                       | 213 ms: 1.01x faster                                                                                                             |
| docutils       | 1.59 sec                                                                                                                     | 1.60 sec: 1.01x slower                                                                                                           |
| html5lib       | 36.6 ms                                                                                                                      | 35.6 ms: 1.03x faster                                                                                                            |
| Geometric mean | (ref)                                                                                                                        | 1.01x faster                                                                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp               | 504 ms                                                                                                                       | 458 ms: 1.10x faster                                                                                                             |
| async_tree_none_tg        | 157 ms                                                                                                                       | 152 ms: 1.03x faster                                                                                                             |
| asyncio_websockets        | 149 ms                                                                                                                       | 145 ms: 1.03x faster                                                                                                             |
| async_tree_io_tg          | 370 ms                                                                                                                       | 361 ms: 1.02x faster                                                                                                             |
| async_tree_io             | 366 ms                                                                                                                       | 358 ms: 1.02x faster                                                                                                             |
| asyncio_tcp_ssl           | 1.36 sec                                                                                                                     | 1.34 sec: 1.02x faster                                                                                                           |
| async_tree_memoization_tg | 189 ms                                                                                                                       | 192 ms: 1.02x slower                                                                                                             |
| coroutines                | 14.1 ms                                                                                                                      | 14.5 ms: 1.03x slower                                                                                                            |
| async_generators          | 229 ms                                                                                                                       | 241 ms: 1.05x slower                                                                                                             |
| Geometric mean            | (ref)                                                                                                                        | 1.01x faster                                                                                                                     |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                                                                                      | 53.4 ms: 1.23x faster                                                                                                            |
| float          | 43.3 ms                                                                                                                      | 38.8 ms: 1.11x faster                                                                                                            |
| pidigits       | 145 ms                                                                                                                       | 143 ms: 1.02x faster                                                                                                             |
| Geometric mean | (ref)                                                                                                                        | 1.12x faster                                                                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 79.9 ms                                                                                                                      | 77.0 ms: 1.04x faster                                                                                                            |
| regex_dna      | 116 ms                                                                                                                       | 117 ms: 1.01x slower                                                                                                             |
| regex_effbot   | 1.46 ms                                                                                                                      | 1.54 ms: 1.06x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                                        | 1.01x slower                                                                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                                                                       | 105 us: 1.28x faster                                                                                                             |
| tomli_loads          | 1.37 sec                                                                                                                     | 1.09 sec: 1.26x faster                                                                                                           |
| xml_etree_generate   | 55.3 ms                                                                                                                      | 48.6 ms: 1.14x faster                                                                                                            |
| xml_etree_process    | 38.6 ms                                                                                                                      | 35.0 ms: 1.10x faster                                                                                                            |
| pickle_pure_python   | 210 us                                                                                                                       | 196 us: 1.08x faster                                                                                                             |
| pickle               | 7.84 us                                                                                                                      | 7.48 us: 1.05x faster                                                                                                            |
| xml_etree_iterparse  | 58.6 ms                                                                                                                      | 56.5 ms: 1.04x faster                                                                                                            |
| xml_etree_parse      | 86.6 ms                                                                                                                      | 85.6 ms: 1.01x faster                                                                                                            |
| pickle_list          | 3.20 us                                                                                                                      | 3.18 us: 1.01x faster                                                                                                            |
| json_dumps           | 5.43 ms                                                                                                                      | 5.47 ms: 1.01x slower                                                                                                            |
| pickle_dict          | 19.4 us                                                                                                                      | 19.8 us: 1.02x slower                                                                                                            |
| unpickle             | 8.28 us                                                                                                                      | 8.47 us: 1.02x slower                                                                                                            |
| Geometric mean       | (ref)                                                                                                                        | 1.06x faster                                                                                                                     |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                                                                      | 19.0 ms: 1.02x faster                                                                                                            |
| Geometric mean         | (ref)                                                                                                                        | 1.01x faster                                                                                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.72 ms                                                                                                                      | 5.23 ms: 1.29x faster                                                                                                            |
| genshi_xml     | 34.3 ms                                                                                                                      | 34.7 ms: 1.01x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                                        | 1.06x faster                                                                                                                     |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                 | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| fannkuch                  | 267 ms                                                                                                                       | 204 ms: 1.31x faster                                                                                                             |
| mako                      | 6.72 ms                                                                                                                      | 5.23 ms: 1.29x faster                                                                                                            |
| unpickle_pure_python      | 134 us                                                                                                                       | 105 us: 1.28x faster                                                                                                             |
| scimark_fft               | 169 ms                                                                                                                       | 133 ms: 1.27x faster                                                                                                             |
| tomli_loads               | 1.37 sec                                                                                                                     | 1.09 sec: 1.26x faster                                                                                                           |
| nbody                     | 65.6 ms                                                                                                                      | 53.4 ms: 1.23x faster                                                                                                            |
| bpe_tokeniser             | 2.98 sec                                                                                                                     | 2.49 sec: 1.19x faster                                                                                                           |
| pprint_safe_repr          | 497 ms                                                                                                                       | 418 ms: 1.19x faster                                                                                                             |
| pprint_pformat            | 1.00 sec                                                                                                                     | 852 ms: 1.17x faster                                                                                                             |
| scimark_sparse_mat_mult   | 2.47 ms                                                                                                                      | 2.12 ms: 1.17x faster                                                                                                            |
| pyflate                   | 283 ms                                                                                                                       | 248 ms: 1.14x faster                                                                                                             |
| sqlglot_v2_parse          | 844 us                                                                                                                       | 741 us: 1.14x faster                                                                                                             |
| xml_etree_generate        | 55.3 ms                                                                                                                      | 48.6 ms: 1.14x faster                                                                                                            |
| float                     | 43.3 ms                                                                                                                      | 38.8 ms: 1.11x faster                                                                                                            |
| xml_etree_process         | 38.6 ms                                                                                                                      | 35.0 ms: 1.10x faster                                                                                                            |
| comprehensions            | 11.2 us                                                                                                                      | 10.2 us: 1.10x faster                                                                                                            |
| asyncio_tcp               | 504 ms                                                                                                                       | 458 ms: 1.10x faster                                                                                                             |
| sqlglot_v2_transpile      | 1.03 ms                                                                                                                      | 944 us: 1.09x faster                                                                                                             |
| pickle_pure_python        | 210 us                                                                                                                       | 196 us: 1.08x faster                                                                                                             |
| k_core                    | 1.56 sec                                                                                                                     | 1.46 sec: 1.07x faster                                                                                                           |
| crypto_pyaes              | 47.9 ms                                                                                                                      | 44.9 ms: 1.07x faster                                                                                                            |
| telco                     | 4.17 ms                                                                                                                      | 3.90 ms: 1.07x faster                                                                                                            |
| chaos                     | 41.1 ms                                                                                                                      | 38.5 ms: 1.07x faster                                                                                                            |
| richards                  | 27.7 ms                                                                                                                      | 26.1 ms: 1.06x faster                                                                                                            |
| richards_super            | 31.4 ms                                                                                                                      | 29.7 ms: 1.06x faster                                                                                                            |
| raytrace                  | 178 ms                                                                                                                       | 169 ms: 1.05x faster                                                                                                             |
| nqueens                   | 63.3 ms                                                                                                                      | 60.1 ms: 1.05x faster                                                                                                            |
| hexiom                    | 4.12 ms                                                                                                                      | 3.91 ms: 1.05x faster                                                                                                            |
| pickle                    | 7.84 us                                                                                                                      | 7.48 us: 1.05x faster                                                                                                            |
| scimark_sor               | 76.6 ms                                                                                                                      | 73.0 ms: 1.05x faster                                                                                                            |
| pycparser                 | 684 ms                                                                                                                       | 653 ms: 1.05x faster                                                                                                             |
| connected_components      | 327 ms                                                                                                                       | 313 ms: 1.05x faster                                                                                                             |
| deepcopy_memo             | 17.8 us                                                                                                                      | 17.1 us: 1.04x faster                                                                                                            |
| mdp                       | 812 ms                                                                                                                       | 779 ms: 1.04x faster                                                                                                             |
| regex_compile             | 79.9 ms                                                                                                                      | 77.0 ms: 1.04x faster                                                                                                            |
| xml_etree_iterparse       | 58.6 ms                                                                                                                      | 56.5 ms: 1.04x faster                                                                                                            |
| async_tree_none_tg        | 157 ms                                                                                                                       | 152 ms: 1.03x faster                                                                                                             |
| deepcopy_reduce           | 1.77 us                                                                                                                      | 1.71 us: 1.03x faster                                                                                                            |
| subparsers                | 30.7 ms                                                                                                                      | 29.7 ms: 1.03x faster                                                                                                            |
| meteor_contest            | 72.0 ms                                                                                                                      | 69.8 ms: 1.03x faster                                                                                                            |
| asyncio_websockets        | 149 ms                                                                                                                       | 145 ms: 1.03x faster                                                                                                             |
| go                        | 76.6 ms                                                                                                                      | 74.3 ms: 1.03x faster                                                                                                            |
| html5lib                  | 36.6 ms                                                                                                                      | 35.6 ms: 1.03x faster                                                                                                            |
| deltablue                 | 2.23 ms                                                                                                                      | 2.17 ms: 1.03x faster                                                                                                            |
| deepcopy                  | 165 us                                                                                                                       | 161 us: 1.02x faster                                                                                                             |
| async_tree_io_tg          | 370 ms                                                                                                                       | 361 ms: 1.02x faster                                                                                                             |
| async_tree_io             | 366 ms                                                                                                                       | 358 ms: 1.02x faster                                                                                                             |
| logging_simple            | 6.01 us                                                                                                                      | 5.91 us: 1.02x faster                                                                                                            |
| pidigits                  | 145 ms                                                                                                                       | 143 ms: 1.02x faster                                                                                                             |
| python_startup_no_site    | 19.4 ms                                                                                                                      | 19.0 ms: 1.02x faster                                                                                                            |
| asyncio_tcp_ssl           | 1.36 sec                                                                                                                     | 1.34 sec: 1.02x faster                                                                                                           |
| dulwich_log               | 39.3 ms                                                                                                                      | 38.7 ms: 1.02x faster                                                                                                            |
| logging_silent            | 55.2 ns                                                                                                                      | 54.4 ns: 1.01x faster                                                                                                            |
| sqlite_synth              | 1.57 us                                                                                                                      | 1.55 us: 1.01x faster                                                                                                            |
| 2to3                      | 216 ms                                                                                                                       | 213 ms: 1.01x faster                                                                                                             |
| shortest_path             | 352 ms                                                                                                                       | 348 ms: 1.01x faster                                                                                                             |
| xml_etree_parse           | 86.6 ms                                                                                                                      | 85.6 ms: 1.01x faster                                                                                                            |
| pickle_list               | 3.20 us                                                                                                                      | 3.18 us: 1.01x faster                                                                                                            |
| spectral_norm             | 65.1 ms                                                                                                                      | 64.8 ms: 1.01x faster                                                                                                            |
| docutils                  | 1.59 sec                                                                                                                     | 1.60 sec: 1.01x slower                                                                                                           |
| sqlglot_v2_optimize       | 33.9 ms                                                                                                                      | 34.2 ms: 1.01x slower                                                                                                            |
| json_dumps                | 5.43 ms                                                                                                                      | 5.47 ms: 1.01x slower                                                                                                            |
| regex_dna                 | 116 ms                                                                                                                       | 117 ms: 1.01x slower                                                                                                             |
| genshi_xml                | 34.3 ms                                                                                                                      | 34.7 ms: 1.01x slower                                                                                                            |
| typing_runtime_protocols  | 103 us                                                                                                                       | 104 us: 1.01x slower                                                                                                             |
| create_gc_cycles          | 1.28 ms                                                                                                                      | 1.30 ms: 1.01x slower                                                                                                            |
| async_tree_memoization_tg | 189 ms                                                                                                                       | 192 ms: 1.02x slower                                                                                                             |
| pathlib                   | 28.3 ms                                                                                                                      | 28.7 ms: 1.02x slower                                                                                                            |
| coverage                  | 48.0 ms                                                                                                                      | 48.8 ms: 1.02x slower                                                                                                            |
| sympy_expand              | 283 ms                                                                                                                       | 287 ms: 1.02x slower                                                                                                             |
| pickle_dict               | 19.4 us                                                                                                                      | 19.8 us: 1.02x slower                                                                                                            |
| sympy_integrate           | 12.2 ms                                                                                                                      | 12.5 ms: 1.02x slower                                                                                                            |
| unpickle                  | 8.28 us                                                                                                                      | 8.47 us: 1.02x slower                                                                                                            |
| json                      | 2.83 ms                                                                                                                      | 2.91 ms: 1.03x slower                                                                                                            |
| scimark_lu                | 56.2 ms                                                                                                                      | 57.8 ms: 1.03x slower                                                                                                            |
| scimark_monte_carlo       | 41.0 ms                                                                                                                      | 42.2 ms: 1.03x slower                                                                                                            |
| coroutines                | 14.1 ms                                                                                                                      | 14.5 ms: 1.03x slower                                                                                                            |
| async_generators          | 229 ms                                                                                                                       | 241 ms: 1.05x slower                                                                                                             |
| regex_effbot              | 1.46 ms                                                                                                                      | 1.54 ms: 1.06x slower                                                                                                            |
| Geometric mean            | (ref)                                                                                                                        | 1.04x faster                                                                                                                     |

Benchmark hidden because not significant (23): async_tree_memoization, async_tree_none, sqlglot_v2_normalize, thrift, python_startup, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, unpickle_list, json_loads, gc_traversal, sympy_sum, sphinx, many_optionals, bench_mp_pool, generators, bench_thread_pool, sympy_str, django_template, logging_format, genshi_text, pylint, unpack_sequence, regex_v8

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown