
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 82d43ba
- commit date: 2023-08-11
- overall geometric mean: 1.03x slower
- HPT reliability: 88.84%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 2.78 sec: 1.05x faster                                                          |
| tornado_http   | 120 ms                                                                      | 129 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 89.1 ms                                                                     | 85.8 ms: 1.04x faster                                                           |
| float          | 81.3 ms                                                                     | 116 ms: 1.42x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.11x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                                     | 3.37 ms: 1.09x faster                                                           |
| regex_dna      | 252 ms                                                                      | 236 ms: 1.07x faster                                                            |
| regex_v8       | 24.0 ms                                                                     | 23.8 ms: 1.01x faster                                                           |
| regex_compile  | 151 ms                                                                      | 151 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 236 us                                                                      | 218 us: 1.09x faster                                                            |
| pickle_list          | 4.54 us                                                                     | 4.22 us: 1.08x faster                                                           |
| pickle               | 10.2 us                                                                     | 9.78 us: 1.04x faster                                                           |
| unpickle_list        | 4.79 us                                                                     | 4.64 us: 1.03x faster                                                           |
| pickle_dict          | 32.7 us                                                                     | 31.8 us: 1.03x faster                                                           |
| pickle_pure_python   | 321 us                                                                      | 315 us: 1.02x faster                                                            |
| tomli_loads          | 2.41 sec                                                                    | 2.38 sec: 1.01x faster                                                          |
| unpickle             | 15.1 us                                                                     | 15.0 us: 1.01x faster                                                           |
| json_dumps           | 10.2 ms                                                                     | 10.2 ms: 1.00x faster                                                           |
| json_loads           | 25.7 us                                                                     | 26.0 us: 1.01x slower                                                           |
| xml_etree_generate   | 84.9 ms                                                                     | 96.4 ms: 1.13x slower                                                           |
| xml_etree_parse      | 147 ms                                                                      | 543 ms: 3.68x slower                                                            |
| xml_etree_iterparse  | 106 ms                                                                      | 515 ms: 4.86x slower                                                            |
| Geometric mean       | (ref)                                                                       | 1.22x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.63 ms                                                                     | 8.75 ms: 1.01x slower                                                           |
| python_startup         | 11.6 ms                                                                     | 11.8 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|-------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.08 sec                                                                    | 726 ms: 1.49x faster                                                            |
| async_tree_none         | 470 ms                                                                      | 352 ms: 1.33x faster                                                            |
| async_tree_memoization  | 567 ms                                                                      | 434 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed | 717 ms                                                                      | 611 ms: 1.17x faster                                                            |
| regex_effbot            | 3.67 ms                                                                     | 3.37 ms: 1.09x faster                                                           |
| unpickle_pure_python    | 236 us                                                                      | 218 us: 1.09x faster                                                            |
| pickle_list             | 4.54 us                                                                     | 4.22 us: 1.08x faster                                                           |
| regex_dna               | 252 ms                                                                      | 236 ms: 1.07x faster                                                            |
| docutils                | 2.92 sec                                                                    | 2.78 sec: 1.05x faster                                                          |
| richards                | 55.5 ms                                                                     | 53.0 ms: 1.05x faster                                                           |
| richards_super          | 62.0 ms                                                                     | 59.5 ms: 1.04x faster                                                           |
| pickle                  | 10.2 us                                                                     | 9.78 us: 1.04x faster                                                           |
| nbody                   | 89.1 ms                                                                     | 85.8 ms: 1.04x faster                                                           |
| pycparser               | 1.32 sec                                                                    | 1.27 sec: 1.04x faster                                                          |
| unpickle_list           | 4.79 us                                                                     | 4.64 us: 1.03x faster                                                           |
| pickle_dict             | 32.7 us                                                                     | 31.8 us: 1.03x faster                                                           |
| meteor_contest          | 130 ms                                                                      | 127 ms: 1.02x faster                                                            |
| sqlite_synth            | 2.76 us                                                                     | 2.70 us: 1.02x faster                                                           |
| pickle_pure_python      | 321 us                                                                      | 315 us: 1.02x faster                                                            |
| fannkuch                | 394 ms                                                                      | 387 ms: 1.02x faster                                                            |
| deepcopy_memo           | 37.7 us                                                                     | 37.0 us: 1.02x faster                                                           |
| spectral_norm           | 94.8 ms                                                                     | 93.2 ms: 1.02x faster                                                           |
| generators              | 37.4 ms                                                                     | 36.7 ms: 1.02x faster                                                           |
| chaos                   | 62.7 ms                                                                     | 61.7 ms: 1.02x faster                                                           |
| scimark_sor             | 144 ms                                                                      | 142 ms: 1.01x faster                                                            |
| tomli_loads             | 2.41 sec                                                                    | 2.38 sec: 1.01x faster                                                          |
| unpack_sequence         | 48.4 ns                                                                     | 47.8 ns: 1.01x faster                                                           |
| crypto_pyaes            | 74.4 ms                                                                     | 73.5 ms: 1.01x faster                                                           |
| coroutines              | 23.7 ms                                                                     | 23.5 ms: 1.01x faster                                                           |
| scimark_monte_carlo     | 68.7 ms                                                                     | 68.0 ms: 1.01x faster                                                           |
| deepcopy                | 384 us                                                                      | 380 us: 1.01x faster                                                            |
| comprehensions          | 22.1 us                                                                     | 22.0 us: 1.01x faster                                                           |
| json                    | 5.22 ms                                                                     | 5.19 ms: 1.01x faster                                                           |
| pyflate                 | 514 ms                                                                      | 511 ms: 1.01x faster                                                            |
| regex_v8                | 24.0 ms                                                                     | 23.8 ms: 1.01x faster                                                           |
| pprint_safe_repr        | 808 ms                                                                      | 803 ms: 1.01x faster                                                            |
| unpickle                | 15.1 us                                                                     | 15.0 us: 1.01x faster                                                           |
| nqueens                 | 91.9 ms                                                                     | 91.4 ms: 1.01x faster                                                           |
| pprint_pformat          | 1.65 sec                                                                    | 1.64 sec: 1.00x faster                                                          |
| json_dumps              | 10.2 ms                                                                     | 10.2 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl         | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                          |
| regex_compile           | 151 ms                                                                      | 151 ms: 1.00x slower                                                            |
| go                      | 174 ms                                                                      | 175 ms: 1.00x slower                                                            |
| deepcopy_reduce         | 3.44 us                                                                     | 3.46 us: 1.01x slower                                                           |
| pathlib                 | 19.5 ms                                                                     | 19.6 ms: 1.01x slower                                                           |
| dulwich_log             | 68.2 ms                                                                     | 68.6 ms: 1.01x slower                                                           |
| hexiom                  | 6.53 ms                                                                     | 6.58 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult | 4.34 ms                                                                     | 4.38 ms: 1.01x slower                                                           |
| json_loads              | 25.7 us                                                                     | 26.0 us: 1.01x slower                                                           |
| python_startup_no_site  | 8.63 ms                                                                     | 8.75 ms: 1.01x slower                                                           |
| sqlglot_normalize       | 118 ms                                                                      | 119 ms: 1.02x slower                                                            |
| python_startup          | 11.6 ms                                                                     | 11.8 ms: 1.02x slower                                                           |
| sqlglot_optimize        | 58.8 ms                                                                     | 59.9 ms: 1.02x slower                                                           |
| create_gc_cycles        | 1.64 ms                                                                     | 1.67 ms: 1.02x slower                                                           |
| mdp                     | 2.55 sec                                                                    | 2.60 sec: 1.02x slower                                                          |
| scimark_lu              | 99.0 ms                                                                     | 101 ms: 1.02x slower                                                            |
| async_generators        | 395 ms                                                                      | 405 ms: 1.02x slower                                                            |
| deltablue               | 3.67 ms                                                                     | 3.80 ms: 1.03x slower                                                           |
| sqlglot_parse           | 1.43 ms                                                                     | 1.48 ms: 1.04x slower                                                           |
| bench_mp_pool           | 4.83 ms                                                                     | 5.14 ms: 1.06x slower                                                           |
| coverage                | 89.4 ms                                                                     | 95.1 ms: 1.06x slower                                                           |
| sqlglot_transpile       | 1.83 ms                                                                     | 1.95 ms: 1.07x slower                                                           |
| tornado_http            | 120 ms                                                                      | 129 ms: 1.07x slower                                                            |
| xml_etree_generate      | 84.9 ms                                                                     | 96.4 ms: 1.13x slower                                                           |
| mypy2                   | 372 ms                                                                      | 457 ms: 1.23x slower                                                            |
| gc_traversal            | 3.52 ms                                                                     | 4.37 ms: 1.24x slower                                                           |
| float                   | 81.3 ms                                                                     | 116 ms: 1.42x slower                                                            |
| xml_etree_parse         | 147 ms                                                                      | 543 ms: 3.68x slower                                                            |
| xml_etree_iterparse     | 106 ms                                                                      | 515 ms: 4.86x slower                                                            |
| Geometric mean          | (ref)                                                                       | 1.03x slower                                                                    |

Benchmark hidden because not significant (13): typing_runtime_protocols, raytrace, mako, asyncio_tcp, scimark_fft, pidigits, telco, xml_etree_process, logging_silent, logging_format, dask, logging_simple, bench_thread_pool


# HPT report

- Reliability score: 88.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
