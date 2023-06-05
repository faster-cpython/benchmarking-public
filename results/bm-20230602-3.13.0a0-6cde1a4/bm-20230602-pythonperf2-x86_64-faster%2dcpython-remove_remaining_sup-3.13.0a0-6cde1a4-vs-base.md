
# Results vs. base

- fork: faster-cpython
- ref: remove_remaining_sup
- machine: linux-x86_64
- commit hash: 6cde1a4
- commit date: 2023-06-02
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.88 sec                                                                    | 2.89 sec: 1.00x slower                                                                |
| tornado_http   | 115 ms                                                                      | 117 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 92.5 ms                                                                     | 87.9 ms: 1.05x faster                                                                 |
| pidigits       | 261 ms                                                                      | 261 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 146 ms                                                                      | 147 ms: 1.01x slower                                                                  |
| regex_effbot   | 3.51 ms                                                                     | 3.62 ms: 1.03x slower                                                                 |
| regex_dna      | 236 ms                                                                      | 245 ms: 1.04x slower                                                                  |
| regex_v8       | 22.9 ms                                                                     | 24.4 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|--------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_list        | 4.44 us                                                                     | 4.27 us: 1.04x faster                                                                 |
| pickle_dict        | 31.9 us                                                                     | 31.8 us: 1.00x faster                                                                 |
| json_dumps         | 10.1 ms                                                                     | 10.1 ms: 1.00x slower                                                                 |
| unpickle_list      | 4.59 us                                                                     | 4.64 us: 1.01x slower                                                                 |
| json_loads         | 24.3 us                                                                     | 24.5 us: 1.01x slower                                                                 |
| xml_etree_generate | 86.4 ms                                                                     | 87.4 ms: 1.01x slower                                                                 |
| unpickle           | 14.4 us                                                                     | 14.6 us: 1.01x slower                                                                 |
| xml_etree_parse    | 146 ms                                                                      | 148 ms: 1.01x slower                                                                  |
| tomli_loads        | 2.17 sec                                                                    | 2.22 sec: 1.02x slower                                                                |
| xml_etree_process  | 58.4 ms                                                                     | 59.9 ms: 1.03x slower                                                                 |
| Geometric mean     | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (4): pickle, pickle_pure_python, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.35 ms                                                                     | 8.33 ms: 1.00x faster                                                                 |
| python_startup         | 11.3 ms                                                                     | 11.2 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                                     | 10.2 ms: 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| gc_traversal             | 4.04 ms                                                                     | 3.56 ms: 1.14x faster                                                                 |
| nbody                    | 92.5 ms                                                                     | 87.9 ms: 1.05x faster                                                                 |
| pickle_list              | 4.44 us                                                                     | 4.27 us: 1.04x faster                                                                 |
| scimark_monte_carlo      | 70.9 ms                                                                     | 68.8 ms: 1.03x faster                                                                 |
| comprehensions           | 22.2 us                                                                     | 21.9 us: 1.02x faster                                                                 |
| hexiom                   | 6.02 ms                                                                     | 5.95 ms: 1.01x faster                                                                 |
| mypy2                    | 369 ms                                                                      | 365 ms: 1.01x faster                                                                  |
| async_tree_none          | 470 ms                                                                      | 466 ms: 1.01x faster                                                                  |
| async_tree_memoization   | 564 ms                                                                      | 558 ms: 1.01x faster                                                                  |
| async_tree_io            | 1.08 sec                                                                    | 1.07 sec: 1.01x faster                                                                |
| nqueens                  | 92.1 ms                                                                     | 91.4 ms: 1.01x faster                                                                 |
| scimark_sor              | 110 ms                                                                      | 109 ms: 1.01x faster                                                                  |
| coroutines               | 22.3 ms                                                                     | 22.1 ms: 1.00x faster                                                                 |
| dulwich_log              | 65.9 ms                                                                     | 65.6 ms: 1.00x faster                                                                 |
| python_startup_no_site   | 8.35 ms                                                                     | 8.33 ms: 1.00x faster                                                                 |
| pickle_dict              | 31.9 us                                                                     | 31.8 us: 1.00x faster                                                                 |
| python_startup           | 11.3 ms                                                                     | 11.2 ms: 1.00x faster                                                                 |
| pidigits                 | 261 ms                                                                      | 261 ms: 1.00x slower                                                                  |
| spectral_norm            | 87.6 ms                                                                     | 88.0 ms: 1.00x slower                                                                 |
| json_dumps               | 10.1 ms                                                                     | 10.1 ms: 1.00x slower                                                                 |
| docutils                 | 2.88 sec                                                                    | 2.89 sec: 1.00x slower                                                                |
| sqlite_synth             | 2.68 us                                                                     | 2.70 us: 1.01x slower                                                                 |
| crypto_pyaes             | 80.7 ms                                                                     | 81.1 ms: 1.01x slower                                                                 |
| telco                    | 7.20 ms                                                                     | 7.24 ms: 1.01x slower                                                                 |
| sqlglot_normalize        | 115 ms                                                                      | 116 ms: 1.01x slower                                                                  |
| generators               | 35.5 ms                                                                     | 35.8 ms: 1.01x slower                                                                 |
| typing_runtime_protocols | 148 us                                                                      | 150 us: 1.01x slower                                                                  |
| chaos                    | 62.9 ms                                                                     | 63.6 ms: 1.01x slower                                                                 |
| unpickle_list            | 4.59 us                                                                     | 4.64 us: 1.01x slower                                                                 |
| json_loads               | 24.3 us                                                                     | 24.5 us: 1.01x slower                                                                 |
| regex_compile            | 146 ms                                                                      | 147 ms: 1.01x slower                                                                  |
| deepcopy_reduce          | 3.39 us                                                                     | 3.43 us: 1.01x slower                                                                 |
| mako                     | 10.1 ms                                                                     | 10.2 ms: 1.01x slower                                                                 |
| xml_etree_generate       | 86.4 ms                                                                     | 87.4 ms: 1.01x slower                                                                 |
| unpickle                 | 14.4 us                                                                     | 14.6 us: 1.01x slower                                                                 |
| json                     | 5.06 ms                                                                     | 5.13 ms: 1.01x slower                                                                 |
| logging_simple           | 6.74 us                                                                     | 6.83 us: 1.01x slower                                                                 |
| xml_etree_parse          | 146 ms                                                                      | 148 ms: 1.01x slower                                                                  |
| pyflate                  | 444 ms                                                                      | 451 ms: 1.01x slower                                                                  |
| scimark_sparse_mat_mult  | 4.23 ms                                                                     | 4.29 ms: 1.01x slower                                                                 |
| meteor_contest           | 127 ms                                                                      | 129 ms: 1.02x slower                                                                  |
| raytrace                 | 303 ms                                                                      | 308 ms: 1.02x slower                                                                  |
| pprint_pformat           | 1.65 sec                                                                    | 1.68 sec: 1.02x slower                                                                |
| pycparser                | 1.26 sec                                                                    | 1.28 sec: 1.02x slower                                                                |
| deepcopy                 | 370 us                                                                      | 377 us: 1.02x slower                                                                  |
| logging_format           | 7.23 us                                                                     | 7.37 us: 1.02x slower                                                                 |
| tornado_http             | 115 ms                                                                      | 117 ms: 1.02x slower                                                                  |
| logging_silent           | 94.7 ns                                                                     | 96.7 ns: 1.02x slower                                                                 |
| pprint_safe_repr         | 810 ms                                                                      | 827 ms: 1.02x slower                                                                  |
| tomli_loads              | 2.17 sec                                                                    | 2.22 sec: 1.02x slower                                                                |
| coverage                 | 87.1 ms                                                                     | 89.1 ms: 1.02x slower                                                                 |
| go                       | 149 ms                                                                      | 153 ms: 1.03x slower                                                                  |
| xml_etree_process        | 58.4 ms                                                                     | 59.9 ms: 1.03x slower                                                                 |
| deepcopy_memo            | 37.2 us                                                                     | 38.4 us: 1.03x slower                                                                 |
| regex_effbot             | 3.51 ms                                                                     | 3.62 ms: 1.03x slower                                                                 |
| richards_super           | 51.6 ms                                                                     | 53.3 ms: 1.03x slower                                                                 |
| richards                 | 45.7 ms                                                                     | 47.4 ms: 1.04x slower                                                                 |
| fannkuch                 | 344 ms                                                                      | 358 ms: 1.04x slower                                                                  |
| regex_dna                | 236 ms                                                                      | 245 ms: 1.04x slower                                                                  |
| regex_v8                 | 22.9 ms                                                                     | 24.4 ms: 1.07x slower                                                                 |
| unpack_sequence          | 44.9 ns                                                                     | 48.3 ns: 1.08x slower                                                                 |
| bench_mp_pool            | 7.92 ms                                                                     | 9.37 ms: 1.18x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (19): create_gc_cycles, pickle, sqlglot_transpile, pickle_pure_python, scimark_lu, async_tree_cpu_io_mixed, asyncio_tcp, asyncio_tcp_ssl, mdp, pathlib, float, unpickle_pure_python, scimark_fft, sqlglot_parse, sqlglot_optimize, deltablue, async_generators, xml_etree_iterparse, bench_thread_pool
