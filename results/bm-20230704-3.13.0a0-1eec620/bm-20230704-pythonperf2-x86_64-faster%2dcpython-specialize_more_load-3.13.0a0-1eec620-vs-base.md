
# Results vs. base

- fork: faster-cpython
- ref: specialize_more_load
- machine: linux-x86_64
- commit hash: 1eec620
- commit date: 2023-07-04
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tornado_http   | 123 ms                                                                      | 122 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                                     | 80.3 ms: 1.02x faster                                                                 |
| pidigits       | 260 ms                                                                      | 260 ms: 1.00x faster                                                                  |
| nbody          | 85.6 ms                                                                     | 89.6 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 151 ms                                                                      | 149 ms: 1.02x faster                                                                  |
| regex_dna      | 237 ms                                                                      | 246 ms: 1.04x slower                                                                  |
| regex_v8       | 23.2 ms                                                                     | 24.9 ms: 1.08x slower                                                                 |
| regex_effbot   | 3.38 ms                                                                     | 3.65 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|--------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python | 330 us                                                                      | 314 us: 1.05x faster                                                                  |
| json_dumps         | 10.4 ms                                                                     | 10.0 ms: 1.03x faster                                                                 |
| xml_etree_process  | 59.7 ms                                                                     | 58.4 ms: 1.02x faster                                                                 |
| xml_etree_parse    | 148 ms                                                                      | 146 ms: 1.01x faster                                                                  |
| unpickle_list      | 4.71 us                                                                     | 4.65 us: 1.01x faster                                                                 |
| xml_etree_generate | 86.9 ms                                                                     | 85.8 ms: 1.01x faster                                                                 |
| tomli_loads        | 2.32 sec                                                                    | 2.34 sec: 1.01x slower                                                                |
| pickle_list        | 4.33 us                                                                     | 4.36 us: 1.01x slower                                                                 |
| json_loads         | 24.5 us                                                                     | 24.7 us: 1.01x slower                                                                 |
| unpickle           | 14.4 us                                                                     | 14.6 us: 1.01x slower                                                                 |
| pickle_dict        | 31.2 us                                                                     | 31.9 us: 1.02x slower                                                                 |
| Geometric mean     | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup | 11.3 ms                                                                     | 11.3 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 10.3 ms                                                                     | 10.1 ms: 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpack_sequence          | 56.7 ns                                                                     | 46.9 ns: 1.21x faster                                                                 |
| crypto_pyaes             | 82.6 ms                                                                     | 73.6 ms: 1.12x faster                                                                 |
| pickle_pure_python       | 330 us                                                                      | 314 us: 1.05x faster                                                                  |
| deepcopy_memo            | 38.4 us                                                                     | 36.8 us: 1.04x faster                                                                 |
| scimark_monte_carlo      | 74.0 ms                                                                     | 71.5 ms: 1.04x faster                                                                 |
| sqlglot_parse            | 1.48 ms                                                                     | 1.43 ms: 1.03x faster                                                                 |
| json_dumps               | 10.4 ms                                                                     | 10.0 ms: 1.03x faster                                                                 |
| telco                    | 7.79 ms                                                                     | 7.57 ms: 1.03x faster                                                                 |
| sqlglot_transpile        | 1.90 ms                                                                     | 1.85 ms: 1.03x faster                                                                 |
| deepcopy                 | 382 us                                                                      | 373 us: 1.02x faster                                                                  |
| scimark_sparse_mat_mult  | 4.47 ms                                                                     | 4.37 ms: 1.02x faster                                                                 |
| go                       | 176 ms                                                                      | 172 ms: 1.02x faster                                                                  |
| xml_etree_process        | 59.7 ms                                                                     | 58.4 ms: 1.02x faster                                                                 |
| async_generators         | 400 ms                                                                      | 392 ms: 1.02x faster                                                                  |
| mako                     | 10.3 ms                                                                     | 10.1 ms: 1.02x faster                                                                 |
| float                    | 81.9 ms                                                                     | 80.3 ms: 1.02x faster                                                                 |
| deepcopy_reduce          | 3.47 us                                                                     | 3.42 us: 1.02x faster                                                                 |
| regex_compile            | 151 ms                                                                      | 149 ms: 1.02x faster                                                                  |
| tornado_http             | 123 ms                                                                      | 122 ms: 1.02x faster                                                                  |
| pyflate                  | 520 ms                                                                      | 513 ms: 1.01x faster                                                                  |
| xml_etree_parse          | 148 ms                                                                      | 146 ms: 1.01x faster                                                                  |
| unpickle_list            | 4.71 us                                                                     | 4.65 us: 1.01x faster                                                                 |
| sqlglot_normalize        | 119 ms                                                                      | 118 ms: 1.01x faster                                                                  |
| xml_etree_generate       | 86.9 ms                                                                     | 85.8 ms: 1.01x faster                                                                 |
| raytrace                 | 278 ms                                                                      | 275 ms: 1.01x faster                                                                  |
| hexiom                   | 6.57 ms                                                                     | 6.49 ms: 1.01x faster                                                                 |
| comprehensions           | 22.2 us                                                                     | 22.0 us: 1.01x faster                                                                 |
| scimark_sor              | 147 ms                                                                      | 145 ms: 1.01x faster                                                                  |
| sqlite_synth             | 2.74 us                                                                     | 2.72 us: 1.01x faster                                                                 |
| dask                     | 593 ms                                                                      | 588 ms: 1.01x faster                                                                  |
| sqlglot_optimize         | 59.5 ms                                                                     | 59.2 ms: 1.01x faster                                                                 |
| dulwich_log              | 68.0 ms                                                                     | 67.6 ms: 1.01x faster                                                                 |
| pidigits                 | 260 ms                                                                      | 260 ms: 1.00x faster                                                                  |
| python_startup           | 11.3 ms                                                                     | 11.3 ms: 1.00x faster                                                                 |
| mdp                      | 2.55 sec                                                                    | 2.55 sec: 1.00x slower                                                                |
| mypy2                    | 370 ms                                                                      | 371 ms: 1.00x slower                                                                  |
| asyncio_tcp              | 382 ms                                                                      | 383 ms: 1.00x slower                                                                  |
| pprint_safe_repr         | 836 ms                                                                      | 840 ms: 1.00x slower                                                                  |
| tomli_loads              | 2.32 sec                                                                    | 2.34 sec: 1.01x slower                                                                |
| pickle_list              | 4.33 us                                                                     | 4.36 us: 1.01x slower                                                                 |
| json                     | 5.13 ms                                                                     | 5.17 ms: 1.01x slower                                                                 |
| pprint_pformat           | 1.70 sec                                                                    | 1.71 sec: 1.01x slower                                                                |
| json_loads               | 24.5 us                                                                     | 24.7 us: 1.01x slower                                                                 |
| fannkuch                 | 394 ms                                                                      | 397 ms: 1.01x slower                                                                  |
| unpickle                 | 14.4 us                                                                     | 14.6 us: 1.01x slower                                                                 |
| scimark_fft              | 313 ms                                                                      | 317 ms: 1.01x slower                                                                  |
| logging_format           | 7.51 us                                                                     | 7.59 us: 1.01x slower                                                                 |
| typing_runtime_protocols | 149 us                                                                      | 151 us: 1.01x slower                                                                  |
| coroutines               | 22.9 ms                                                                     | 23.2 ms: 1.01x slower                                                                 |
| logging_silent           | 96.0 ns                                                                     | 97.5 ns: 1.02x slower                                                                 |
| richards                 | 52.6 ms                                                                     | 53.5 ms: 1.02x slower                                                                 |
| meteor_contest           | 129 ms                                                                      | 131 ms: 1.02x slower                                                                  |
| nqueens                  | 91.2 ms                                                                     | 92.9 ms: 1.02x slower                                                                 |
| richards_super           | 58.5 ms                                                                     | 59.7 ms: 1.02x slower                                                                 |
| pickle_dict              | 31.2 us                                                                     | 31.9 us: 1.02x slower                                                                 |
| generators               | 36.4 ms                                                                     | 37.6 ms: 1.03x slower                                                                 |
| regex_dna                | 237 ms                                                                      | 246 ms: 1.04x slower                                                                  |
| nbody                    | 85.6 ms                                                                     | 89.6 ms: 1.05x slower                                                                 |
| gc_traversal             | 3.59 ms                                                                     | 3.77 ms: 1.05x slower                                                                 |
| coverage                 | 87.5 ms                                                                     | 92.8 ms: 1.06x slower                                                                 |
| regex_v8                 | 23.2 ms                                                                     | 24.9 ms: 1.08x slower                                                                 |
| regex_effbot             | 3.38 ms                                                                     | 3.65 ms: 1.08x slower                                                                 |
| bench_mp_pool            | 5.29 ms                                                                     | 5.86 ms: 1.11x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (19): scimark_lu, async_tree_cpu_io_mixed, bench_thread_pool, pycparser, xml_etree_iterparse, pathlib, python_startup_no_site, pickle, asyncio_tcp_ssl, async_tree_io, docutils, spectral_norm, chaos, unpickle_pure_python, async_tree_none, logging_simple, async_tree_memoization, create_gc_cycles, deltablue
