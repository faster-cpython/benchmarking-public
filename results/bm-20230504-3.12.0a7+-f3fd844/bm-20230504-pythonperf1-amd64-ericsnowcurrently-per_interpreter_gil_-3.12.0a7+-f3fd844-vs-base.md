
# Results vs. base

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: windows-amd64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 206 ms                                                                      | 208 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                                      | 150 ms: 1.01x faster                                                                   |
| float          | 51.6 ms                                                                     | 52.1 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                      | 116 ms: 1.01x faster                                                                   |
| regex_v8       | 13.9 ms                                                                     | 14.1 ms: 1.01x slower                                                                  |
| regex_compile  | 84.3 ms                                                                     | 85.1 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pickle_list          | 2.85 us                                                                     | 2.76 us: 1.03x faster                                                                  |
| unpickle             | 8.63 us                                                                     | 8.46 us: 1.02x faster                                                                  |
| xml_etree_iterparse  | 62.2 ms                                                                     | 61.1 ms: 1.02x faster                                                                  |
| xml_etree_parse      | 92.7 ms                                                                     | 91.3 ms: 1.01x faster                                                                  |
| pickle               | 7.00 us                                                                     | 6.95 us: 1.01x faster                                                                  |
| xml_etree_generate   | 54.1 ms                                                                     | 54.6 ms: 1.01x slower                                                                  |
| json_dumps           | 5.53 ms                                                                     | 5.60 ms: 1.01x slower                                                                  |
| pickle_pure_python   | 186 us                                                                      | 191 us: 1.03x slower                                                                   |
| unpickle_pure_python | 131 us                                                                      | 136 us: 1.03x slower                                                                   |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                           |

Benchmark hidden because not significant (4): unpickle_list, json_loads, pickle_dict, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                     | 18.8 ms: 1.02x slower                                                                  |
| python_startup_no_site | 15.5 ms                                                                     | 15.9 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                                       | 1.02x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 6.42 ms                                                                     | 6.60 ms: 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pickle_list             | 2.85 us                                                                     | 2.76 us: 1.03x faster                                                                  |
| unpickle                | 8.63 us                                                                     | 8.46 us: 1.02x faster                                                                  |
| create_gc_cycles        | 689 us                                                                      | 676 us: 1.02x faster                                                                   |
| async_tree_none         | 295 ms                                                                      | 289 ms: 1.02x faster                                                                   |
| coverage                | 53.3 ms                                                                     | 52.3 ms: 1.02x faster                                                                  |
| xml_etree_iterparse     | 62.2 ms                                                                     | 61.1 ms: 1.02x faster                                                                  |
| xml_etree_parse         | 92.7 ms                                                                     | 91.3 ms: 1.01x faster                                                                  |
| scimark_sparse_mat_mult | 2.45 ms                                                                     | 2.42 ms: 1.01x faster                                                                  |
| scimark_lu              | 57.5 ms                                                                     | 56.8 ms: 1.01x faster                                                                  |
| pidigits                | 152 ms                                                                      | 150 ms: 1.01x faster                                                                   |
| regex_dna               | 117 ms                                                                      | 116 ms: 1.01x faster                                                                   |
| pickle                  | 7.00 us                                                                     | 6.95 us: 1.01x faster                                                                  |
| gc_traversal            | 1.44 ms                                                                     | 1.43 ms: 1.01x faster                                                                  |
| raytrace                | 186 ms                                                                      | 185 ms: 1.01x faster                                                                   |
| bench_mp_pool           | 67.4 ms                                                                     | 67.1 ms: 1.01x faster                                                                  |
| mypy2                   | 215 ms                                                                      | 214 ms: 1.00x faster                                                                   |
| meteor_contest          | 78.7 ms                                                                     | 79.0 ms: 1.00x slower                                                                  |
| 2to3                    | 206 ms                                                                      | 208 ms: 1.01x slower                                                                   |
| sqlglot_optimize        | 33.8 ms                                                                     | 34.0 ms: 1.01x slower                                                                  |
| logging_silent          | 57.6 ns                                                                     | 58.1 ns: 1.01x slower                                                                  |
| xml_etree_generate      | 54.1 ms                                                                     | 54.6 ms: 1.01x slower                                                                  |
| float                   | 51.6 ms                                                                     | 52.1 ms: 1.01x slower                                                                  |
| deltablue               | 2.03 ms                                                                     | 2.05 ms: 1.01x slower                                                                  |
| regex_v8                | 13.9 ms                                                                     | 14.1 ms: 1.01x slower                                                                  |
| regex_compile           | 84.3 ms                                                                     | 85.1 ms: 1.01x slower                                                                  |
| json_dumps              | 5.53 ms                                                                     | 5.60 ms: 1.01x slower                                                                  |
| pycparser               | 658 ms                                                                      | 666 ms: 1.01x slower                                                                   |
| dulwich_log             | 42.4 ms                                                                     | 43.1 ms: 1.02x slower                                                                  |
| scimark_fft             | 172 ms                                                                      | 174 ms: 1.02x slower                                                                   |
| async_tree_io           | 715 ms                                                                      | 727 ms: 1.02x slower                                                                   |
| sqlglot_normalize       | 182 ms                                                                      | 185 ms: 1.02x slower                                                                   |
| async_generators        | 224 ms                                                                      | 228 ms: 1.02x slower                                                                   |
| mdp                     | 1.39 sec                                                                    | 1.42 sec: 1.02x slower                                                                 |
| crypto_pyaes            | 46.5 ms                                                                     | 47.4 ms: 1.02x slower                                                                  |
| python_startup          | 18.4 ms                                                                     | 18.8 ms: 1.02x slower                                                                  |
| pprint_safe_repr        | 500 ms                                                                      | 511 ms: 1.02x slower                                                                   |
| sqlglot_transpile       | 977 us                                                                      | 999 us: 1.02x slower                                                                   |
| comprehensions          | 15.5 us                                                                     | 15.9 us: 1.02x slower                                                                  |
| hexiom                  | 3.90 ms                                                                     | 3.99 ms: 1.02x slower                                                                  |
| python_startup_no_site  | 15.5 ms                                                                     | 15.9 ms: 1.02x slower                                                                  |
| pyflate                 | 282 ms                                                                      | 289 ms: 1.02x slower                                                                   |
| dask                    | 357 ms                                                                      | 366 ms: 1.03x slower                                                                   |
| json                    | 2.88 ms                                                                     | 2.96 ms: 1.03x slower                                                                  |
| chaos                   | 43.5 ms                                                                     | 44.8 ms: 1.03x slower                                                                  |
| mako                    | 6.42 ms                                                                     | 6.60 ms: 1.03x slower                                                                  |
| pickle_pure_python      | 186 us                                                                      | 191 us: 1.03x slower                                                                   |
| sqlglot_parse           | 768 us                                                                      | 791 us: 1.03x slower                                                                   |
| deepcopy_reduce         | 2.00 us                                                                     | 2.07 us: 1.03x slower                                                                  |
| logging_format          | 6.81 us                                                                     | 7.03 us: 1.03x slower                                                                  |
| generators              | 20.0 ms                                                                     | 20.7 ms: 1.03x slower                                                                  |
| unpickle_pure_python    | 131 us                                                                      | 136 us: 1.03x slower                                                                   |
| deepcopy_memo           | 23.1 us                                                                     | 23.9 us: 1.04x slower                                                                  |
| go                      | 84.7 ms                                                                     | 87.9 ms: 1.04x slower                                                                  |
| spectral_norm           | 61.8 ms                                                                     | 64.3 ms: 1.04x slower                                                                  |
| logging_simple          | 6.24 us                                                                     | 6.51 us: 1.04x slower                                                                  |
| richards                | 24.6 ms                                                                     | 25.7 ms: 1.04x slower                                                                  |
| scimark_sor             | 74.5 ms                                                                     | 78.1 ms: 1.05x slower                                                                  |
| nqueens                 | 57.0 ms                                                                     | 59.9 ms: 1.05x slower                                                                  |
| fannkuch                | 232 ms                                                                      | 244 ms: 1.05x slower                                                                   |
| scimark_monte_carlo     | 41.0 ms                                                                     | 43.3 ms: 1.05x slower                                                                  |
| unpack_sequence         | 33.8 ns                                                                     | 42.2 ns: 1.25x slower                                                                  |
| Geometric mean          | (ref)                                                                       | 1.01x slower                                                                           |

Benchmark hidden because not significant (18): unpickle_list, asyncio_tcp, json_loads, async_tree_memoization, async_tree_cpu_io_mixed, docutils, pathlib, regex_effbot, telco, deepcopy, pickle_dict, coroutines, pprint_pformat, tornado_http, sqlite_synth, xml_etree_process, bench_thread_pool, nbody
