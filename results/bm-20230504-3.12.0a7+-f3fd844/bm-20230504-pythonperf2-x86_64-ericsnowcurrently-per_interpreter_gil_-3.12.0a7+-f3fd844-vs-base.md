
# Results vs. base

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                       | 286 ms: 1.00x slower                                                                    |
| docutils       | 2.90 sec                                                                     | 2.88 sec: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                                      | 78.5 ms: 1.00x faster                                                                   |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                                      | 23.4 ms: 1.02x faster                                                                   |
| regex_effbot   | 3.47 ms                                                                      | 3.41 ms: 1.02x faster                                                                   |
| regex_dna      | 232 ms                                                                       | 228 ms: 1.02x faster                                                                    |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| pickle               | 10.5 us                                                                      | 9.94 us: 1.05x faster                                                                   |
| json_loads           | 25.2 us                                                                      | 24.3 us: 1.04x faster                                                                   |
| pickle_dict          | 33.3 us                                                                      | 32.5 us: 1.03x faster                                                                   |
| xml_etree_parse      | 148 ms                                                                       | 144 ms: 1.02x faster                                                                    |
| json_dumps           | 10.5 ms                                                                      | 10.3 ms: 1.01x faster                                                                   |
| unpickle             | 15.0 us                                                                      | 14.8 us: 1.01x faster                                                                   |
| xml_etree_iterparse  | 105 ms                                                                       | 103 ms: 1.01x faster                                                                    |
| xml_etree_process    | 58.8 ms                                                                      | 59.1 ms: 1.00x slower                                                                   |
| xml_etree_generate   | 85.6 ms                                                                      | 86.1 ms: 1.01x slower                                                                   |
| unpickle_pure_python | 205 us                                                                       | 206 us: 1.01x slower                                                                    |
| unpickle_list        | 4.61 us                                                                      | 4.86 us: 1.06x slower                                                                   |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                            |

Benchmark hidden because not significant (2): pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.39 ms                                                                      | 8.44 ms: 1.01x slower                                                                   |
| python_startup         | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                                   |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| mako      | 9.92 ms                                                                      | 10.0 ms: 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark               | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| bench_mp_pool           | 7.84 ms                                                                      | 4.87 ms: 1.61x faster                                                                   |
| unpack_sequence         | 52.7 ns                                                                      | 46.0 ns: 1.15x faster                                                                   |
| gc_traversal            | 3.76 ms                                                                      | 3.53 ms: 1.07x faster                                                                   |
| pickle                  | 10.5 us                                                                      | 9.94 us: 1.05x faster                                                                   |
| deepcopy_memo           | 37.2 us                                                                      | 35.5 us: 1.05x faster                                                                   |
| json_loads              | 25.2 us                                                                      | 24.3 us: 1.04x faster                                                                   |
| fannkuch                | 357 ms                                                                       | 347 ms: 1.03x faster                                                                    |
| pickle_dict             | 33.3 us                                                                      | 32.5 us: 1.03x faster                                                                   |
| logging_simple          | 6.78 us                                                                      | 6.60 us: 1.03x faster                                                                   |
| raytrace                | 316 ms                                                                       | 308 ms: 1.03x faster                                                                    |
| pprint_pformat          | 1.65 sec                                                                     | 1.61 sec: 1.03x faster                                                                  |
| xml_etree_parse         | 148 ms                                                                       | 144 ms: 1.02x faster                                                                    |
| deepcopy_reduce         | 3.46 us                                                                      | 3.38 us: 1.02x faster                                                                   |
| scimark_monte_carlo     | 72.3 ms                                                                      | 70.7 ms: 1.02x faster                                                                   |
| telco                   | 7.26 ms                                                                      | 7.11 ms: 1.02x faster                                                                   |
| pprint_safe_repr        | 808 ms                                                                       | 793 ms: 1.02x faster                                                                    |
| deepcopy                | 383 us                                                                       | 376 us: 1.02x faster                                                                    |
| richards                | 44.5 ms                                                                      | 43.8 ms: 1.02x faster                                                                   |
| chaos                   | 67.8 ms                                                                      | 66.6 ms: 1.02x faster                                                                   |
| regex_v8                | 23.8 ms                                                                      | 23.4 ms: 1.02x faster                                                                   |
| regex_effbot            | 3.47 ms                                                                      | 3.41 ms: 1.02x faster                                                                   |
| go                      | 146 ms                                                                       | 144 ms: 1.02x faster                                                                    |
| logging_format          | 7.51 us                                                                      | 7.39 us: 1.02x faster                                                                   |
| regex_dna               | 232 ms                                                                       | 228 ms: 1.02x faster                                                                    |
| json_dumps              | 10.5 ms                                                                      | 10.3 ms: 1.01x faster                                                                   |
| unpickle                | 15.0 us                                                                      | 14.8 us: 1.01x faster                                                                   |
| xml_etree_iterparse     | 105 ms                                                                       | 103 ms: 1.01x faster                                                                    |
| json                    | 5.18 ms                                                                      | 5.12 ms: 1.01x faster                                                                   |
| deltablue               | 3.25 ms                                                                      | 3.23 ms: 1.01x faster                                                                   |
| docutils                | 2.90 sec                                                                     | 2.88 sec: 1.01x faster                                                                  |
| comprehensions          | 24.5 us                                                                      | 24.4 us: 1.01x faster                                                                   |
| float                   | 78.9 ms                                                                      | 78.5 ms: 1.00x faster                                                                   |
| mypy2                   | 377 ms                                                                       | 378 ms: 1.00x slower                                                                    |
| 2to3                    | 284 ms                                                                       | 286 ms: 1.00x slower                                                                    |
| pathlib                 | 19.4 ms                                                                      | 19.4 ms: 1.00x slower                                                                   |
| logging_silent          | 92.4 ns                                                                      | 92.8 ns: 1.00x slower                                                                   |
| xml_etree_process       | 58.8 ms                                                                      | 59.1 ms: 1.00x slower                                                                   |
| scimark_fft             | 298 ms                                                                       | 299 ms: 1.01x slower                                                                    |
| async_tree_memoization  | 572 ms                                                                       | 575 ms: 1.01x slower                                                                    |
| xml_etree_generate      | 85.6 ms                                                                      | 86.1 ms: 1.01x slower                                                                   |
| sqlglot_normalize       | 120 ms                                                                       | 121 ms: 1.01x slower                                                                    |
| mdp                     | 2.53 sec                                                                     | 2.55 sec: 1.01x slower                                                                  |
| python_startup_no_site  | 8.39 ms                                                                      | 8.44 ms: 1.01x slower                                                                   |
| unpickle_pure_python    | 205 us                                                                       | 206 us: 1.01x slower                                                                    |
| hexiom                  | 5.86 ms                                                                      | 5.90 ms: 1.01x slower                                                                   |
| scimark_sparse_mat_mult | 4.44 ms                                                                      | 4.47 ms: 1.01x slower                                                                   |
| python_startup          | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                                   |
| async_tree_io           | 1.09 sec                                                                     | 1.10 sec: 1.01x slower                                                                  |
| mako                    | 9.92 ms                                                                      | 10.0 ms: 1.01x slower                                                                   |
| dulwich_log             | 64.8 ms                                                                      | 65.6 ms: 1.01x slower                                                                   |
| sqlite_synth            | 2.62 us                                                                      | 2.65 us: 1.01x slower                                                                   |
| pyflate                 | 437 ms                                                                       | 443 ms: 1.01x slower                                                                    |
| async_tree_cpu_io_mixed | 703 ms                                                                       | 712 ms: 1.01x slower                                                                    |
| generators              | 36.0 ms                                                                      | 36.6 ms: 1.02x slower                                                                   |
| scimark_sor             | 111 ms                                                                       | 113 ms: 1.02x slower                                                                    |
| nqueens                 | 88.9 ms                                                                      | 90.7 ms: 1.02x slower                                                                   |
| unpickle_list           | 4.61 us                                                                      | 4.86 us: 1.06x slower                                                                   |
| coverage                | 90.6 ms                                                                      | 98.7 ms: 1.09x slower                                                                   |
| Geometric mean          | (ref)                                                                        | 1.01x faster                                                                            |

Benchmark hidden because not significant (21): sqlglot_transpile, create_gc_cycles, tornado_http, scimark_lu, crypto_pyaes, nbody, meteor_contest, pidigits, regex_compile, pickle_pure_python, coroutines, pickle_list, sqlglot_optimize, pycparser, dask, asyncio_tcp, async_generators, sqlglot_parse, async_tree_none, spectral_norm, bench_thread_pool
