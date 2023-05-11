
# Results vs. base

- fork: faster-cpython
- ref: instrument_all_possi
- machine: linux-x86_64
- commit hash: 5418580
- commit date: 2023-05-10
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 283 ms                                                                       | 285 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 79.9 ms                                                                      | 79.0 ms: 1.01x faster                                                                  |
| pidigits       | 260 ms                                                                       | 261 ms: 1.00x slower                                                                   |
| nbody          | 84.2 ms                                                                      | 84.7 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.55 ms                                                                      | 3.41 ms: 1.04x faster                                                                  |
| regex_v8       | 24.3 ms                                                                      | 23.4 ms: 1.04x faster                                                                  |
| regex_dna      | 234 ms                                                                       | 227 ms: 1.03x faster                                                                   |
| regex_compile  | 145 ms                                                                       | 144 ms: 1.01x faster                                                                   |
| Geometric mean | (ref)                                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                                       | 104 ms: 1.03x faster                                                                   |
| unpickle_list        | 4.81 us                                                                      | 4.72 us: 1.02x faster                                                                  |
| pickle_pure_python   | 323 us                                                                       | 320 us: 1.01x faster                                                                   |
| json_dumps           | 10.3 ms                                                                      | 10.2 ms: 1.01x faster                                                                  |
| xml_etree_process    | 59.0 ms                                                                      | 58.7 ms: 1.01x faster                                                                  |
| xml_etree_generate   | 86.0 ms                                                                      | 85.6 ms: 1.00x faster                                                                  |
| unpickle_pure_python | 206 us                                                                       | 205 us: 1.00x faster                                                                   |
| unpickle             | 14.8 us                                                                      | 14.9 us: 1.01x slower                                                                  |
| pickle_dict          | 31.9 us                                                                      | 32.6 us: 1.02x slower                                                                  |
| pickle_list          | 4.33 us                                                                      | 4.45 us: 1.03x slower                                                                  |
| pickle               | 10.0 us                                                                      | 10.3 us: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.43 ms                                                                      | 8.38 ms: 1.01x faster                                                                  |
| python_startup         | 11.3 ms                                                                      | 11.3 ms: 1.00x faster                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-----------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 9.84 ms                                                                      | 10.2 ms: 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpack_sequence         | 52.9 ns                                                                      | 44.8 ns: 1.18x faster                                                                  |
| scimark_monte_carlo     | 73.6 ms                                                                      | 68.1 ms: 1.08x faster                                                                  |
| coverage                | 94.6 ms                                                                      | 88.5 ms: 1.07x faster                                                                  |
| go                      | 152 ms                                                                       | 144 ms: 1.06x faster                                                                   |
| logging_silent          | 96.0 ns                                                                      | 91.1 ns: 1.05x faster                                                                  |
| regex_effbot            | 3.55 ms                                                                      | 3.41 ms: 1.04x faster                                                                  |
| scimark_sparse_mat_mult | 4.41 ms                                                                      | 4.23 ms: 1.04x faster                                                                  |
| regex_v8                | 24.3 ms                                                                      | 23.4 ms: 1.04x faster                                                                  |
| richards                | 44.9 ms                                                                      | 43.5 ms: 1.03x faster                                                                  |
| regex_dna               | 234 ms                                                                       | 227 ms: 1.03x faster                                                                   |
| nqueens                 | 92.8 ms                                                                      | 90.1 ms: 1.03x faster                                                                  |
| pathlib                 | 20.7 ms                                                                      | 20.1 ms: 1.03x faster                                                                  |
| xml_etree_iterparse     | 107 ms                                                                       | 104 ms: 1.03x faster                                                                   |
| mdp                     | 2.58 sec                                                                     | 2.53 sec: 1.02x faster                                                                 |
| pycparser               | 1.28 sec                                                                     | 1.25 sec: 1.02x faster                                                                 |
| pprint_safe_repr        | 813 ms                                                                       | 798 ms: 1.02x faster                                                                   |
| unpickle_list           | 4.81 us                                                                      | 4.72 us: 1.02x faster                                                                  |
| pprint_pformat          | 1.66 sec                                                                     | 1.64 sec: 1.02x faster                                                                 |
| scimark_sor             | 111 ms                                                                       | 109 ms: 1.02x faster                                                                   |
| async_generators        | 385 ms                                                                       | 380 ms: 1.01x faster                                                                   |
| crypto_pyaes            | 80.2 ms                                                                      | 79.2 ms: 1.01x faster                                                                  |
| scimark_fft             | 302 ms                                                                       | 298 ms: 1.01x faster                                                                   |
| float                   | 79.9 ms                                                                      | 79.0 ms: 1.01x faster                                                                  |
| meteor_contest          | 129 ms                                                                       | 128 ms: 1.01x faster                                                                   |
| deltablue               | 3.25 ms                                                                      | 3.22 ms: 1.01x faster                                                                  |
| dask                    | 562 ms                                                                       | 556 ms: 1.01x faster                                                                   |
| hexiom                  | 5.85 ms                                                                      | 5.79 ms: 1.01x faster                                                                  |
| pickle_pure_python      | 323 us                                                                       | 320 us: 1.01x faster                                                                   |
| json_dumps              | 10.3 ms                                                                      | 10.2 ms: 1.01x faster                                                                  |
| coroutines              | 22.8 ms                                                                      | 22.6 ms: 1.01x faster                                                                  |
| chaos                   | 64.8 ms                                                                      | 64.3 ms: 1.01x faster                                                                  |
| regex_compile           | 145 ms                                                                       | 144 ms: 1.01x faster                                                                   |
| python_startup_no_site  | 8.43 ms                                                                      | 8.38 ms: 1.01x faster                                                                  |
| xml_etree_process       | 59.0 ms                                                                      | 58.7 ms: 1.01x faster                                                                  |
| xml_etree_generate      | 86.0 ms                                                                      | 85.6 ms: 1.00x faster                                                                  |
| fannkuch                | 345 ms                                                                       | 343 ms: 1.00x faster                                                                   |
| unpickle_pure_python    | 206 us                                                                       | 205 us: 1.00x faster                                                                   |
| generators              | 36.5 ms                                                                      | 36.4 ms: 1.00x faster                                                                  |
| async_tree_io           | 1.05 sec                                                                     | 1.05 sec: 1.00x faster                                                                 |
| python_startup          | 11.3 ms                                                                      | 11.3 ms: 1.00x faster                                                                  |
| mypy2                   | 367 ms                                                                       | 369 ms: 1.00x slower                                                                   |
| pidigits                | 260 ms                                                                       | 261 ms: 1.00x slower                                                                   |
| sqlite_synth            | 2.64 us                                                                      | 2.66 us: 1.00x slower                                                                  |
| 2to3                    | 283 ms                                                                       | 285 ms: 1.01x slower                                                                   |
| unpickle                | 14.8 us                                                                      | 14.9 us: 1.01x slower                                                                  |
| nbody                   | 84.2 ms                                                                      | 84.7 ms: 1.01x slower                                                                  |
| sqlglot_transpile       | 1.78 ms                                                                      | 1.79 ms: 1.01x slower                                                                  |
| raytrace                | 297 ms                                                                       | 299 ms: 1.01x slower                                                                   |
| deepcopy_reduce         | 3.42 us                                                                      | 3.45 us: 1.01x slower                                                                  |
| sqlglot_parse           | 1.38 ms                                                                      | 1.39 ms: 1.01x slower                                                                  |
| telco                   | 7.11 ms                                                                      | 7.23 ms: 1.02x slower                                                                  |
| logging_simple          | 6.66 us                                                                      | 6.80 us: 1.02x slower                                                                  |
| spectral_norm           | 90.5 ms                                                                      | 92.6 ms: 1.02x slower                                                                  |
| pickle_dict             | 31.9 us                                                                      | 32.6 us: 1.02x slower                                                                  |
| deepcopy_memo           | 36.4 us                                                                      | 37.2 us: 1.02x slower                                                                  |
| pickle_list             | 4.33 us                                                                      | 4.45 us: 1.03x slower                                                                  |
| pickle                  | 10.0 us                                                                      | 10.3 us: 1.03x slower                                                                  |
| logging_format          | 7.30 us                                                                      | 7.51 us: 1.03x slower                                                                  |
| mako                    | 9.84 ms                                                                      | 10.2 ms: 1.03x slower                                                                  |
| pyflate                 | 444 ms                                                                       | 461 ms: 1.04x slower                                                                   |
| bench_mp_pool           | 5.93 ms                                                                      | 7.35 ms: 1.24x slower                                                                  |
| Geometric mean          | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (18): async_tree_memoization, xml_etree_parse, tornado_http, docutils, deepcopy, async_tree_none, json_loads, bench_thread_pool, create_gc_cycles, sqlglot_optimize, json, asyncio_tcp, comprehensions, gc_traversal, scimark_lu, async_tree_cpu_io_mixed, sqlglot_normalize, dulwich_log
