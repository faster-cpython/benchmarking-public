
# Results vs. base

- fork: faster-cpython
- ref: micro_op_jump_if_non
- machine: linux-x86_64
- commit hash: 66a6bc3
- commit date: 2023-07-10
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                                    | 2.93 sec: 1.00x slower                                                                |
| tornado_http   | 122 ms                                                                      | 124 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 82.5 ms                                                                     | 82.2 ms: 1.00x faster                                                                 |
| pidigits       | 262 ms                                                                      | 261 ms: 1.00x faster                                                                  |
| nbody          | 89.0 ms                                                                     | 92.7 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                      | 242 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.54 ms                                                                     | 3.56 ms: 1.01x slower                                                                 |
| regex_compile  | 151 ms                                                                      | 152 ms: 1.01x slower                                                                  |
| regex_v8       | 23.7 ms                                                                     | 23.8 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle             | 14.7 us                                                                     | 14.4 us: 1.03x faster                                                                 |
| pickle_list          | 4.47 us                                                                     | 4.38 us: 1.02x faster                                                                 |
| unpickle_list        | 4.79 us                                                                     | 4.71 us: 1.02x faster                                                                 |
| xml_etree_process    | 59.5 ms                                                                     | 59.2 ms: 1.00x faster                                                                 |
| json_loads           | 25.4 us                                                                     | 25.6 us: 1.01x slower                                                                 |
| pickle_pure_python   | 315 us                                                                      | 319 us: 1.01x slower                                                                  |
| json_dumps           | 10.1 ms                                                                     | 10.3 ms: 1.02x slower                                                                 |
| pickle_dict          | 32.1 us                                                                     | 32.7 us: 1.02x slower                                                                 |
| pickle               | 10.1 us                                                                     | 10.4 us: 1.02x slower                                                                 |
| unpickle_pure_python | 218 us                                                                      | 224 us: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.41 ms                                                                     | 8.38 ms: 1.00x faster                                                                 |
| python_startup         | 11.4 ms                                                                     | 11.3 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 10.3 ms                                                                     | 10.2 ms: 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| gc_traversal             | 4.04 ms                                                                     | 3.57 ms: 1.13x faster                                                                 |
| coroutines               | 24.6 ms                                                                     | 22.9 ms: 1.07x faster                                                                 |
| create_gc_cycles         | 1.70 ms                                                                     | 1.61 ms: 1.06x faster                                                                 |
| scimark_sparse_mat_mult  | 4.38 ms                                                                     | 4.16 ms: 1.05x faster                                                                 |
| spectral_norm            | 99.9 ms                                                                     | 95.3 ms: 1.05x faster                                                                 |
| deepcopy_memo            | 38.4 us                                                                     | 37.3 us: 1.03x faster                                                                 |
| unpack_sequence          | 54.0 ns                                                                     | 52.5 ns: 1.03x faster                                                                 |
| pycparser                | 1.36 sec                                                                    | 1.32 sec: 1.03x faster                                                                |
| unpickle                 | 14.7 us                                                                     | 14.4 us: 1.03x faster                                                                 |
| regex_dna                | 247 ms                                                                      | 242 ms: 1.02x faster                                                                  |
| coverage                 | 88.9 ms                                                                     | 86.9 ms: 1.02x faster                                                                 |
| generators               | 36.7 ms                                                                     | 35.9 ms: 1.02x faster                                                                 |
| pickle_list              | 4.47 us                                                                     | 4.38 us: 1.02x faster                                                                 |
| unpickle_list            | 4.79 us                                                                     | 4.71 us: 1.02x faster                                                                 |
| scimark_fft              | 318 ms                                                                      | 313 ms: 1.02x faster                                                                  |
| scimark_sor              | 149 ms                                                                      | 146 ms: 1.01x faster                                                                  |
| mako                     | 10.3 ms                                                                     | 10.2 ms: 1.01x faster                                                                 |
| scimark_monte_carlo      | 73.7 ms                                                                     | 73.1 ms: 1.01x faster                                                                 |
| scimark_lu               | 98.5 ms                                                                     | 97.9 ms: 1.01x faster                                                                 |
| async_tree_io            | 1.09 sec                                                                    | 1.08 sec: 1.01x faster                                                                |
| raytrace                 | 285 ms                                                                      | 284 ms: 1.00x faster                                                                  |
| async_tree_none          | 467 ms                                                                      | 465 ms: 1.00x faster                                                                  |
| float                    | 82.5 ms                                                                     | 82.2 ms: 1.00x faster                                                                 |
| xml_etree_process        | 59.5 ms                                                                     | 59.2 ms: 1.00x faster                                                                 |
| meteor_contest           | 130 ms                                                                      | 129 ms: 1.00x faster                                                                  |
| pprint_safe_repr         | 849 ms                                                                      | 846 ms: 1.00x faster                                                                  |
| python_startup_no_site   | 8.41 ms                                                                     | 8.38 ms: 1.00x faster                                                                 |
| python_startup           | 11.4 ms                                                                     | 11.3 ms: 1.00x faster                                                                 |
| pidigits                 | 262 ms                                                                      | 261 ms: 1.00x faster                                                                  |
| asyncio_tcp              | 384 ms                                                                      | 385 ms: 1.00x slower                                                                  |
| docutils                 | 2.91 sec                                                                    | 2.93 sec: 1.00x slower                                                                |
| regex_effbot             | 3.54 ms                                                                     | 3.56 ms: 1.01x slower                                                                 |
| regex_compile            | 151 ms                                                                      | 152 ms: 1.01x slower                                                                  |
| regex_v8                 | 23.7 ms                                                                     | 23.8 ms: 1.01x slower                                                                 |
| json                     | 5.14 ms                                                                     | 5.19 ms: 1.01x slower                                                                 |
| pyflate                  | 513 ms                                                                      | 518 ms: 1.01x slower                                                                  |
| sqlite_synth             | 2.74 us                                                                     | 2.77 us: 1.01x slower                                                                 |
| mdp                      | 2.54 sec                                                                    | 2.56 sec: 1.01x slower                                                                |
| typing_runtime_protocols | 154 us                                                                      | 155 us: 1.01x slower                                                                  |
| json_loads               | 25.4 us                                                                     | 25.6 us: 1.01x slower                                                                 |
| deltablue                | 3.67 ms                                                                     | 3.71 ms: 1.01x slower                                                                 |
| async_generators         | 389 ms                                                                      | 393 ms: 1.01x slower                                                                  |
| logging_format           | 7.47 us                                                                     | 7.55 us: 1.01x slower                                                                 |
| pickle_pure_python       | 315 us                                                                      | 319 us: 1.01x slower                                                                  |
| deepcopy_reduce          | 3.41 us                                                                     | 3.46 us: 1.01x slower                                                                 |
| go                       | 175 ms                                                                      | 177 ms: 1.01x slower                                                                  |
| tornado_http             | 122 ms                                                                      | 124 ms: 1.02x slower                                                                  |
| json_dumps               | 10.1 ms                                                                     | 10.3 ms: 1.02x slower                                                                 |
| telco                    | 7.62 ms                                                                     | 7.76 ms: 1.02x slower                                                                 |
| pathlib                  | 19.3 ms                                                                     | 19.6 ms: 1.02x slower                                                                 |
| nqueens                  | 92.1 ms                                                                     | 93.9 ms: 1.02x slower                                                                 |
| pickle_dict              | 32.1 us                                                                     | 32.7 us: 1.02x slower                                                                 |
| deepcopy                 | 375 us                                                                      | 384 us: 1.02x slower                                                                  |
| pickle                   | 10.1 us                                                                     | 10.4 us: 1.02x slower                                                                 |
| sqlglot_transpile        | 1.84 ms                                                                     | 1.89 ms: 1.03x slower                                                                 |
| unpickle_pure_python     | 218 us                                                                      | 224 us: 1.03x slower                                                                  |
| chaos                    | 61.2 ms                                                                     | 62.8 ms: 1.03x slower                                                                 |
| sqlglot_parse            | 1.43 ms                                                                     | 1.48 ms: 1.03x slower                                                                 |
| richards_super           | 58.9 ms                                                                     | 61.0 ms: 1.04x slower                                                                 |
| richards                 | 52.8 ms                                                                     | 55.0 ms: 1.04x slower                                                                 |
| nbody                    | 89.0 ms                                                                     | 92.7 ms: 1.04x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (21): bench_mp_pool, bench_thread_pool, async_tree_cpu_io_mixed, xml_etree_parse, fannkuch, pprint_pformat, async_tree_memoization, comprehensions, logging_silent, xml_etree_iterparse, dask, crypto_pyaes, sqlglot_normalize, asyncio_tcp_ssl, sqlglot_optimize, tomli_loads, hexiom, xml_etree_generate, mypy2, logging_simple, dulwich_log
