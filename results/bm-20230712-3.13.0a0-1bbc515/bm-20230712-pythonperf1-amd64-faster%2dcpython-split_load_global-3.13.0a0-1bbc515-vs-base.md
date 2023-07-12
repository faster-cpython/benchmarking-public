
# Results vs. base

- fork: faster-cpython
- ref: split_load_global
- machine: windows-amd64
- commit hash: 1bbc515
- commit date: 2023-07-12
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 1.67 sec                                                                   | 1.64 sec: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 56.9 ms                                                                    | 56.1 ms: 1.02x faster                                                             |
| nbody          | 80.4 ms                                                                    | 81.2 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                                    | 13.7 ms: 1.18x faster                                                             |
| regex_dna      | 120 ms                                                                     | 117 ms: 1.03x faster                                                              |
| regex_effbot   | 1.59 ms                                                                    | 1.58 ms: 1.01x faster                                                             |
| regex_compile  | 93.7 ms                                                                    | 93.0 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                      | 1.05x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_dict          | 18.8 us                                                                    | 18.2 us: 1.03x faster                                                             |
| pickle               | 7.27 us                                                                    | 7.11 us: 1.02x faster                                                             |
| unpickle_list        | 2.82 us                                                                    | 2.76 us: 1.02x faster                                                             |
| pickle_list          | 2.82 us                                                                    | 2.83 us: 1.00x slower                                                             |
| unpickle             | 8.13 us                                                                    | 8.18 us: 1.01x slower                                                             |
| xml_etree_process    | 39.3 ms                                                                    | 39.7 ms: 1.01x slower                                                             |
| unpickle_pure_python | 146 us                                                                     | 148 us: 1.01x slower                                                              |
| xml_etree_iterparse  | 65.1 ms                                                                    | 65.9 ms: 1.01x slower                                                             |
| tomli_loads          | 1.59 sec                                                                   | 1.61 sec: 1.02x slower                                                            |
| xml_etree_parse      | 90.6 ms                                                                    | 93.0 ms: 1.03x slower                                                             |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                      |

Benchmark hidden because not significant (4): xml_etree_generate, json_loads, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|-----------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 7.68 ms                                                                    | 7.51 ms: 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|--------------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8                 | 16.2 ms                                                                    | 13.7 ms: 1.18x faster                                                             |
| generators               | 25.5 ms                                                                    | 24.2 ms: 1.05x faster                                                             |
| pycparser                | 787 ms                                                                     | 758 ms: 1.04x faster                                                              |
| typing_runtime_protocols | 98.7 us                                                                    | 95.1 us: 1.04x faster                                                             |
| pickle_dict              | 18.8 us                                                                    | 18.2 us: 1.03x faster                                                             |
| regex_dna                | 120 ms                                                                     | 117 ms: 1.03x faster                                                              |
| crypto_pyaes             | 47.1 ms                                                                    | 46.0 ms: 1.02x faster                                                             |
| pickle                   | 7.27 us                                                                    | 7.11 us: 1.02x faster                                                             |
| mako                     | 7.68 ms                                                                    | 7.51 ms: 1.02x faster                                                             |
| unpickle_list            | 2.82 us                                                                    | 2.76 us: 1.02x faster                                                             |
| docutils                 | 1.67 sec                                                                   | 1.64 sec: 1.02x faster                                                            |
| deepcopy_reduce          | 2.22 us                                                                    | 2.18 us: 1.02x faster                                                             |
| float                    | 56.9 ms                                                                    | 56.1 ms: 1.02x faster                                                             |
| mdp                      | 1.46 sec                                                                   | 1.44 sec: 1.01x faster                                                            |
| coroutines               | 15.4 ms                                                                    | 15.2 ms: 1.01x faster                                                             |
| meteor_contest           | 75.8 ms                                                                    | 75.1 ms: 1.01x faster                                                             |
| deepcopy                 | 250 us                                                                     | 248 us: 1.01x faster                                                              |
| regex_effbot             | 1.59 ms                                                                    | 1.58 ms: 1.01x faster                                                             |
| regex_compile            | 93.7 ms                                                                    | 93.0 ms: 1.01x faster                                                             |
| async_generators         | 244 ms                                                                     | 242 ms: 1.01x faster                                                              |
| mypy2                    | 221 ms                                                                     | 220 ms: 1.01x faster                                                              |
| chaos                    | 44.3 ms                                                                    | 44.1 ms: 1.01x faster                                                             |
| sqlite_synth             | 1.77 us                                                                    | 1.77 us: 1.00x faster                                                             |
| fannkuch                 | 267 ms                                                                     | 266 ms: 1.00x faster                                                              |
| logging_silent           | 65.7 ns                                                                    | 65.4 ns: 1.00x faster                                                             |
| scimark_sor              | 89.3 ms                                                                    | 88.9 ms: 1.00x faster                                                             |
| pprint_safe_repr         | 545 ms                                                                     | 542 ms: 1.00x faster                                                              |
| scimark_fft              | 191 ms                                                                     | 190 ms: 1.00x faster                                                              |
| coverage                 | 52.7 ms                                                                    | 52.5 ms: 1.00x faster                                                             |
| scimark_monte_carlo      | 45.3 ms                                                                    | 45.2 ms: 1.00x faster                                                             |
| sqlglot_optimize         | 36.0 ms                                                                    | 36.1 ms: 1.00x slower                                                             |
| pickle_list              | 2.82 us                                                                    | 2.83 us: 1.00x slower                                                             |
| sqlglot_normalize        | 192 ms                                                                     | 193 ms: 1.01x slower                                                              |
| unpickle                 | 8.13 us                                                                    | 8.18 us: 1.01x slower                                                             |
| nqueens                  | 63.3 ms                                                                    | 63.7 ms: 1.01x slower                                                             |
| sqlglot_parse            | 870 us                                                                     | 876 us: 1.01x slower                                                              |
| nbody                    | 80.4 ms                                                                    | 81.2 ms: 1.01x slower                                                             |
| spectral_norm            | 69.9 ms                                                                    | 70.6 ms: 1.01x slower                                                             |
| xml_etree_process        | 39.3 ms                                                                    | 39.7 ms: 1.01x slower                                                             |
| scimark_lu               | 62.9 ms                                                                    | 63.6 ms: 1.01x slower                                                             |
| unpickle_pure_python     | 146 us                                                                     | 148 us: 1.01x slower                                                              |
| go                       | 99.6 ms                                                                    | 101 ms: 1.01x slower                                                              |
| xml_etree_iterparse      | 65.1 ms                                                                    | 65.9 ms: 1.01x slower                                                             |
| raytrace                 | 184 ms                                                                     | 187 ms: 1.01x slower                                                              |
| tomli_loads              | 1.59 sec                                                                   | 1.61 sec: 1.02x slower                                                            |
| logging_simple           | 6.88 us                                                                    | 7.00 us: 1.02x slower                                                             |
| logging_format           | 7.38 us                                                                    | 7.53 us: 1.02x slower                                                             |
| json                     | 2.85 ms                                                                    | 2.91 ms: 1.02x slower                                                             |
| hexiom                   | 4.49 ms                                                                    | 4.58 ms: 1.02x slower                                                             |
| deltablue                | 2.28 ms                                                                    | 2.33 ms: 1.02x slower                                                             |
| xml_etree_parse          | 90.6 ms                                                                    | 93.0 ms: 1.03x slower                                                             |
| telco                    | 4.34 ms                                                                    | 4.46 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult  | 2.59 ms                                                                    | 2.68 ms: 1.03x slower                                                             |
| unpack_sequence          | 42.6 ns                                                                    | 45.9 ns: 1.08x slower                                                             |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                                      |

Benchmark hidden because not significant (28): asyncio_tcp_ssl, async_tree_none, deepcopy_memo, dask, create_gc_cycles, async_tree_cpu_io_mixed, bench_mp_pool, pathlib, pidigits, richards, dulwich_log, sqlglot_transpile, pprint_pformat, async_tree_memoization, xml_etree_generate, richards_super, pyflate, json_loads, tornado_http, comprehensions, pickle_pure_python, json_dumps, asyncio_tcp, python_startup, gc_traversal, async_tree_io, bench_thread_pool, python_startup_no_site
