
# Results vs. base

- fork: faster-cpython
- ref: gc_scan_roots
- machine: linux-x86_64
- commit hash: 3994224
- commit date: 2023-08-04
- overall geometric mean: 1.00x slower
- HPT reliability: 70.49%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 3.00 sec: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 89.2 ms                                                                     | 87.7 ms: 1.02x faster                                                          |
| pidigits       | 260 ms                                                                      | 260 ms: 1.00x faster                                                           |
| float          | 80.7 ms                                                                     | 82.4 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 149 ms                                                                      | 148 ms: 1.01x faster                                                           |
| regex_effbot   | 3.77 ms                                                                     | 3.74 ms: 1.01x faster                                                          |
| regex_v8       | 23.6 ms                                                                     | 23.9 ms: 1.01x slower                                                          |
| regex_dna      | 242 ms                                                                      | 248 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 152 ms                                                                      | 143 ms: 1.07x faster                                                           |
| pickle_list          | 4.54 us                                                                     | 4.36 us: 1.04x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                                      | 105 ms: 1.03x faster                                                           |
| pickle_dict          | 32.6 us                                                                     | 31.9 us: 1.02x faster                                                          |
| pickle_pure_python   | 323 us                                                                      | 318 us: 1.01x faster                                                           |
| json_dumps           | 10.4 ms                                                                     | 10.3 ms: 1.01x faster                                                          |
| xml_etree_generate   | 86.5 ms                                                                     | 85.6 ms: 1.01x faster                                                          |
| unpickle_pure_python | 233 us                                                                      | 232 us: 1.01x faster                                                           |
| unpickle             | 14.7 us                                                                     | 15.1 us: 1.03x slower                                                          |
| unpickle_list        | 4.69 us                                                                     | 4.83 us: 1.03x slower                                                          |
| json_loads           | 24.5 us                                                                     | 25.3 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): xml_etree_process, pickle, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.63 ms                                                                     | 8.64 ms: 1.00x slower                                                          |
| python_startup         | 11.6 ms                                                                     | 11.6 ms: 1.00x slower                                                          |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|-------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse         | 152 ms                                                                      | 143 ms: 1.07x faster                                                           |
| pickle_list             | 4.54 us                                                                     | 4.36 us: 1.04x faster                                                          |
| deepcopy                | 387 us                                                                      | 376 us: 1.03x faster                                                           |
| logging_silent          | 101 ns                                                                      | 98.3 ns: 1.03x faster                                                          |
| xml_etree_iterparse     | 107 ms                                                                      | 105 ms: 1.03x faster                                                           |
| bench_thread_pool       | 966 us                                                                      | 946 us: 1.02x faster                                                           |
| pickle_dict             | 32.6 us                                                                     | 31.9 us: 1.02x faster                                                          |
| deepcopy_memo           | 37.9 us                                                                     | 37.2 us: 1.02x faster                                                          |
| pprint_pformat          | 1.69 sec                                                                    | 1.65 sec: 1.02x faster                                                         |
| pprint_safe_repr        | 824 ms                                                                      | 809 ms: 1.02x faster                                                           |
| nbody                   | 89.2 ms                                                                     | 87.7 ms: 1.02x faster                                                          |
| go                      | 176 ms                                                                      | 174 ms: 1.02x faster                                                           |
| asyncio_tcp             | 373 ms                                                                      | 368 ms: 1.01x faster                                                           |
| mdp                     | 2.58 sec                                                                    | 2.54 sec: 1.01x faster                                                         |
| pickle_pure_python      | 323 us                                                                      | 318 us: 1.01x faster                                                           |
| sqlite_synth            | 2.76 us                                                                     | 2.72 us: 1.01x faster                                                          |
| json_dumps              | 10.4 ms                                                                     | 10.3 ms: 1.01x faster                                                          |
| sqlglot_parse           | 1.44 ms                                                                     | 1.42 ms: 1.01x faster                                                          |
| xml_etree_generate      | 86.5 ms                                                                     | 85.6 ms: 1.01x faster                                                          |
| nqueens                 | 91.2 ms                                                                     | 90.3 ms: 1.01x faster                                                          |
| spectral_norm           | 97.6 ms                                                                     | 96.7 ms: 1.01x faster                                                          |
| sqlglot_normalize       | 118 ms                                                                      | 118 ms: 1.01x faster                                                           |
| regex_compile           | 149 ms                                                                      | 148 ms: 1.01x faster                                                           |
| logging_simple          | 6.87 us                                                                     | 6.82 us: 1.01x faster                                                          |
| regex_effbot            | 3.77 ms                                                                     | 3.74 ms: 1.01x faster                                                          |
| scimark_lu              | 97.9 ms                                                                     | 97.3 ms: 1.01x faster                                                          |
| unpickle_pure_python    | 233 us                                                                      | 232 us: 1.01x faster                                                           |
| deepcopy_reduce         | 3.45 us                                                                     | 3.43 us: 1.01x faster                                                          |
| crypto_pyaes            | 73.6 ms                                                                     | 73.2 ms: 1.01x faster                                                          |
| sqlglot_optimize        | 59.0 ms                                                                     | 58.7 ms: 1.00x faster                                                          |
| scimark_fft             | 304 ms                                                                      | 303 ms: 1.00x faster                                                           |
| hexiom                  | 6.48 ms                                                                     | 6.46 ms: 1.00x faster                                                          |
| meteor_contest          | 131 ms                                                                      | 131 ms: 1.00x faster                                                           |
| pidigits                | 260 ms                                                                      | 260 ms: 1.00x faster                                                           |
| mypy2                   | 372 ms                                                                      | 372 ms: 1.00x faster                                                           |
| python_startup_no_site  | 8.63 ms                                                                     | 8.64 ms: 1.00x slower                                                          |
| python_startup          | 11.6 ms                                                                     | 11.6 ms: 1.00x slower                                                          |
| asyncio_tcp_ssl         | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                         |
| pyflate                 | 515 ms                                                                      | 517 ms: 1.00x slower                                                           |
| dulwich_log             | 69.1 ms                                                                     | 69.5 ms: 1.01x slower                                                          |
| coroutines              | 23.3 ms                                                                     | 23.5 ms: 1.01x slower                                                          |
| telco                   | 8.00 ms                                                                     | 8.06 ms: 1.01x slower                                                          |
| regex_v8                | 23.6 ms                                                                     | 23.9 ms: 1.01x slower                                                          |
| raytrace                | 275 ms                                                                      | 279 ms: 1.01x slower                                                           |
| coverage                | 88.4 ms                                                                     | 89.8 ms: 1.02x slower                                                          |
| async_generators        | 396 ms                                                                      | 404 ms: 1.02x slower                                                           |
| float                   | 80.7 ms                                                                     | 82.4 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed | 719 ms                                                                      | 735 ms: 1.02x slower                                                           |
| scimark_monte_carlo     | 68.2 ms                                                                     | 69.7 ms: 1.02x slower                                                          |
| regex_dna               | 242 ms                                                                      | 248 ms: 1.02x slower                                                           |
| json                    | 5.12 ms                                                                     | 5.25 ms: 1.03x slower                                                          |
| docutils                | 2.92 sec                                                                    | 3.00 sec: 1.03x slower                                                         |
| unpickle                | 14.7 us                                                                     | 15.1 us: 1.03x slower                                                          |
| create_gc_cycles        | 1.67 ms                                                                     | 1.72 ms: 1.03x slower                                                          |
| unpickle_list           | 4.69 us                                                                     | 4.83 us: 1.03x slower                                                          |
| json_loads              | 24.5 us                                                                     | 25.3 us: 1.03x slower                                                          |
| scimark_sor             | 144 ms                                                                      | 149 ms: 1.04x slower                                                           |
| async_tree_memoization  | 569 ms                                                                      | 589 ms: 1.04x slower                                                           |
| async_tree_none         | 474 ms                                                                      | 491 ms: 1.04x slower                                                           |
| async_tree_io           | 1.09 sec                                                                    | 1.13 sec: 1.04x slower                                                         |
| gc_traversal            | 3.54 ms                                                                     | 3.82 ms: 1.08x slower                                                          |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (21): richards, chaos, pycparser, xml_etree_process, pathlib, generators, typing_runtime_protocols, unpack_sequence, pickle, dask, fannkuch, sqlglot_transpile, comprehensions, mako, logging_format, tomli_loads, richards_super, scimark_sparse_mat_mult, deltablue, bench_mp_pool, tornado_http


# HPT report

- Reliability score: 70.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
