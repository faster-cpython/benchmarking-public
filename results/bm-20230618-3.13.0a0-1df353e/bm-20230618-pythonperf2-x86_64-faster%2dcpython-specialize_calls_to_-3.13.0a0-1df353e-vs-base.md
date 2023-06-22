
# Results vs. base

- fork: faster-cpython
- ref: specialize_calls_to_
- machine: linux-x86_64
- commit hash: 1df353e
- commit date: 2023-06-18
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                                    | 2.89 sec: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 88.6 ms                                                                     | 86.9 ms: 1.02x faster                                                                 |
| pidigits       | 259 ms                                                                      | 261 ms: 1.01x slower                                                                  |
| float          | 77.5 ms                                                                     | 78.6 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                                     | 23.6 ms: 1.02x faster                                                                 |
| regex_compile  | 146 ms                                                                      | 143 ms: 1.02x faster                                                                  |
| regex_dna      | 243 ms                                                                      | 250 ms: 1.03x slower                                                                  |
| regex_effbot   | 3.47 ms                                                                     | 3.63 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle             | 15.1 us                                                                     | 14.5 us: 1.05x faster                                                                 |
| xml_etree_process    | 60.5 ms                                                                     | 58.5 ms: 1.03x faster                                                                 |
| unpickle_list        | 4.82 us                                                                     | 4.68 us: 1.03x faster                                                                 |
| tomli_loads          | 2.26 sec                                                                    | 2.21 sec: 1.02x faster                                                                |
| xml_etree_generate   | 87.3 ms                                                                     | 85.5 ms: 1.02x faster                                                                 |
| xml_etree_iterparse  | 106 ms                                                                      | 105 ms: 1.01x faster                                                                  |
| pickle_dict          | 32.3 us                                                                     | 32.0 us: 1.01x faster                                                                 |
| json_dumps           | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                                 |
| pickle_pure_python   | 319 us                                                                      | 322 us: 1.01x slower                                                                  |
| xml_etree_parse      | 149 ms                                                                      | 151 ms: 1.01x slower                                                                  |
| unpickle_pure_python | 211 us                                                                      | 214 us: 1.01x slower                                                                  |
| json_loads           | 24.5 us                                                                     | 24.9 us: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup | 11.2 ms                                                                     | 11.3 ms: 1.00x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpack_sequence          | 56.5 ns                                                                     | 51.2 ns: 1.10x faster                                                                 |
| raytrace                 | 304 ms                                                                      | 278 ms: 1.10x faster                                                                  |
| coverage                 | 91.3 ms                                                                     | 85.3 ms: 1.07x faster                                                                 |
| chaos                    | 63.4 ms                                                                     | 60.3 ms: 1.05x faster                                                                 |
| logging_silent           | 97.3 ns                                                                     | 92.7 ns: 1.05x faster                                                                 |
| unpickle                 | 15.1 us                                                                     | 14.5 us: 1.05x faster                                                                 |
| spectral_norm            | 91.4 ms                                                                     | 88.0 ms: 1.04x faster                                                                 |
| xml_etree_process        | 60.5 ms                                                                     | 58.5 ms: 1.03x faster                                                                 |
| dulwich_log              | 67.7 ms                                                                     | 65.6 ms: 1.03x faster                                                                 |
| unpickle_list            | 4.82 us                                                                     | 4.68 us: 1.03x faster                                                                 |
| scimark_sor              | 111 ms                                                                      | 108 ms: 1.02x faster                                                                  |
| regex_v8                 | 24.2 ms                                                                     | 23.6 ms: 1.02x faster                                                                 |
| tomli_loads              | 2.26 sec                                                                    | 2.21 sec: 1.02x faster                                                                |
| regex_compile            | 146 ms                                                                      | 143 ms: 1.02x faster                                                                  |
| xml_etree_generate       | 87.3 ms                                                                     | 85.5 ms: 1.02x faster                                                                 |
| nbody                    | 88.6 ms                                                                     | 86.9 ms: 1.02x faster                                                                 |
| meteor_contest           | 127 ms                                                                      | 125 ms: 1.01x faster                                                                  |
| logging_simple           | 6.91 us                                                                     | 6.82 us: 1.01x faster                                                                 |
| pyflate                  | 451 ms                                                                      | 446 ms: 1.01x faster                                                                  |
| xml_etree_iterparse      | 106 ms                                                                      | 105 ms: 1.01x faster                                                                  |
| hexiom                   | 5.87 ms                                                                     | 5.81 ms: 1.01x faster                                                                 |
| go                       | 149 ms                                                                      | 148 ms: 1.01x faster                                                                  |
| deepcopy                 | 379 us                                                                      | 376 us: 1.01x faster                                                                  |
| pickle_dict              | 32.3 us                                                                     | 32.0 us: 1.01x faster                                                                 |
| asyncio_tcp              | 380 ms                                                                      | 378 ms: 1.01x faster                                                                  |
| nqueens                  | 90.9 ms                                                                     | 90.4 ms: 1.01x faster                                                                 |
| crypto_pyaes             | 81.8 ms                                                                     | 81.3 ms: 1.01x faster                                                                 |
| mdp                      | 2.53 sec                                                                    | 2.52 sec: 1.00x faster                                                                |
| asyncio_tcp_ssl          | 1.56 sec                                                                    | 1.56 sec: 1.00x faster                                                                |
| python_startup           | 11.2 ms                                                                     | 11.3 ms: 1.00x slower                                                                 |
| async_generators         | 396 ms                                                                      | 397 ms: 1.00x slower                                                                  |
| fannkuch                 | 360 ms                                                                      | 361 ms: 1.00x slower                                                                  |
| json_dumps               | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                                 |
| coroutines               | 21.9 ms                                                                     | 22.1 ms: 1.01x slower                                                                 |
| docutils                 | 2.87 sec                                                                    | 2.89 sec: 1.01x slower                                                                |
| deepcopy_reduce          | 3.44 us                                                                     | 3.47 us: 1.01x slower                                                                 |
| pidigits                 | 259 ms                                                                      | 261 ms: 1.01x slower                                                                  |
| async_tree_io            | 1.06 sec                                                                    | 1.06 sec: 1.01x slower                                                                |
| telco                    | 7.17 ms                                                                     | 7.23 ms: 1.01x slower                                                                 |
| pickle_pure_python       | 319 us                                                                      | 322 us: 1.01x slower                                                                  |
| comprehensions           | 21.8 us                                                                     | 22.0 us: 1.01x slower                                                                 |
| pathlib                  | 19.7 ms                                                                     | 19.9 ms: 1.01x slower                                                                 |
| xml_etree_parse          | 149 ms                                                                      | 151 ms: 1.01x slower                                                                  |
| unpickle_pure_python     | 211 us                                                                      | 214 us: 1.01x slower                                                                  |
| scimark_fft              | 301 ms                                                                      | 305 ms: 1.01x slower                                                                  |
| async_tree_memoization   | 550 ms                                                                      | 557 ms: 1.01x slower                                                                  |
| pprint_safe_repr         | 804 ms                                                                      | 815 ms: 1.01x slower                                                                  |
| mypy2                    | 365 ms                                                                      | 370 ms: 1.01x slower                                                                  |
| richards_super           | 52.8 ms                                                                     | 53.5 ms: 1.01x slower                                                                 |
| float                    | 77.5 ms                                                                     | 78.6 ms: 1.01x slower                                                                 |
| pprint_pformat           | 1.64 sec                                                                    | 1.66 sec: 1.01x slower                                                                |
| sqlglot_normalize        | 116 ms                                                                      | 118 ms: 1.02x slower                                                                  |
| typing_runtime_protocols | 148 us                                                                      | 150 us: 1.02x slower                                                                  |
| json_loads               | 24.5 us                                                                     | 24.9 us: 1.02x slower                                                                 |
| sqlglot_transpile        | 1.79 ms                                                                     | 1.82 ms: 1.02x slower                                                                 |
| deepcopy_memo            | 37.5 us                                                                     | 38.3 us: 1.02x slower                                                                 |
| sqlglot_parse            | 1.39 ms                                                                     | 1.42 ms: 1.02x slower                                                                 |
| scimark_sparse_mat_mult  | 4.37 ms                                                                     | 4.47 ms: 1.02x slower                                                                 |
| regex_dna                | 243 ms                                                                      | 250 ms: 1.03x slower                                                                  |
| scimark_monte_carlo      | 68.3 ms                                                                     | 70.8 ms: 1.04x slower                                                                 |
| regex_effbot             | 3.47 ms                                                                     | 3.63 ms: 1.05x slower                                                                 |
| bench_mp_pool            | 8.43 ms                                                                     | 16.1 ms: 1.91x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (19): sqlite_synth, mako, richards, scimark_lu, pickle_list, deltablue, generators, python_startup_no_site, pickle, gc_traversal, sqlglot_optimize, json, async_tree_none, logging_format, pycparser, create_gc_cycles, async_tree_cpu_io_mixed, tornado_http, bench_thread_pool
