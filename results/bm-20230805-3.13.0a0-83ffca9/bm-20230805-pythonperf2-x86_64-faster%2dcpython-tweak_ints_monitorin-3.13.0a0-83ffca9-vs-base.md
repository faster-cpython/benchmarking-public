
# Results vs. base

- fork: faster-cpython
- ref: tweak_ints_monitorin
- machine: linux-x86_64
- commit hash: 83ffca9
- commit date: 2023-08-05
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 2.93 sec: 1.01x slower                                                                |
| tornado_http   | 120 ms                                                                      | 122 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 260 ms                                                                      | 261 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 252 ms                                                                      | 237 ms: 1.06x faster                                                                  |
| regex_effbot   | 3.67 ms                                                                     | 3.47 ms: 1.06x faster                                                                 |
| regex_v8       | 24.0 ms                                                                     | 23.9 ms: 1.00x faster                                                                 |
| regex_compile  | 151 ms                                                                      | 151 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 236 us                                                                      | 223 us: 1.06x faster                                                                  |
| pickle_list          | 4.54 us                                                                     | 4.34 us: 1.04x faster                                                                 |
| unpickle             | 15.1 us                                                                     | 14.7 us: 1.03x faster                                                                 |
| pickle_dict          | 32.7 us                                                                     | 31.9 us: 1.02x faster                                                                 |
| pickle               | 10.2 us                                                                     | 9.99 us: 1.02x faster                                                                 |
| json_loads           | 25.7 us                                                                     | 25.5 us: 1.01x faster                                                                 |
| json_dumps           | 10.2 ms                                                                     | 10.3 ms: 1.00x slower                                                                 |
| xml_etree_generate   | 84.9 ms                                                                     | 85.8 ms: 1.01x slower                                                                 |
| unpickle_list        | 4.79 us                                                                     | 4.85 us: 1.01x slower                                                                 |
| xml_etree_process    | 59.6 ms                                                                     | 60.8 ms: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, tomli_loads, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                                     | 11.6 ms: 1.00x faster                                                                 |
| python_startup_no_site | 8.63 ms                                                                     | 8.64 ms: 1.00x slower                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| coverage                 | 89.4 ms                                                                     | 83.9 ms: 1.07x faster                                                                 |
| regex_dna                | 252 ms                                                                      | 237 ms: 1.06x faster                                                                  |
| unpickle_pure_python     | 236 us                                                                      | 223 us: 1.06x faster                                                                  |
| regex_effbot             | 3.67 ms                                                                     | 3.47 ms: 1.06x faster                                                                 |
| pickle_list              | 4.54 us                                                                     | 4.34 us: 1.04x faster                                                                 |
| richards                 | 55.5 ms                                                                     | 53.7 ms: 1.03x faster                                                                 |
| unpickle                 | 15.1 us                                                                     | 14.7 us: 1.03x faster                                                                 |
| scimark_sparse_mat_mult  | 4.34 ms                                                                     | 4.23 ms: 1.03x faster                                                                 |
| pickle_dict              | 32.7 us                                                                     | 31.9 us: 1.02x faster                                                                 |
| scimark_fft              | 308 ms                                                                      | 301 ms: 1.02x faster                                                                  |
| richards_super           | 62.0 ms                                                                     | 60.8 ms: 1.02x faster                                                                 |
| pickle                   | 10.2 us                                                                     | 9.99 us: 1.02x faster                                                                 |
| coroutines               | 23.7 ms                                                                     | 23.3 ms: 1.02x faster                                                                 |
| sqlite_synth             | 2.76 us                                                                     | 2.71 us: 1.02x faster                                                                 |
| spectral_norm            | 94.8 ms                                                                     | 93.4 ms: 1.02x faster                                                                 |
| json                     | 5.22 ms                                                                     | 5.15 ms: 1.01x faster                                                                 |
| telco                    | 8.15 ms                                                                     | 8.05 ms: 1.01x faster                                                                 |
| fannkuch                 | 394 ms                                                                      | 389 ms: 1.01x faster                                                                  |
| typing_runtime_protocols | 156 us                                                                      | 155 us: 1.01x faster                                                                  |
| meteor_contest           | 130 ms                                                                      | 129 ms: 1.01x faster                                                                  |
| deltablue                | 3.67 ms                                                                     | 3.64 ms: 1.01x faster                                                                 |
| json_loads               | 25.7 us                                                                     | 25.5 us: 1.01x faster                                                                 |
| nqueens                  | 91.9 ms                                                                     | 91.3 ms: 1.01x faster                                                                 |
| regex_v8                 | 24.0 ms                                                                     | 23.9 ms: 1.00x faster                                                                 |
| python_startup           | 11.6 ms                                                                     | 11.6 ms: 1.00x faster                                                                 |
| python_startup_no_site   | 8.63 ms                                                                     | 8.64 ms: 1.00x slower                                                                 |
| pidigits                 | 260 ms                                                                      | 261 ms: 1.00x slower                                                                  |
| dulwich_log              | 68.2 ms                                                                     | 68.4 ms: 1.00x slower                                                                 |
| async_generators         | 395 ms                                                                      | 397 ms: 1.00x slower                                                                  |
| regex_compile            | 151 ms                                                                      | 151 ms: 1.00x slower                                                                  |
| scimark_monte_carlo      | 68.7 ms                                                                     | 69.0 ms: 1.00x slower                                                                 |
| json_dumps               | 10.2 ms                                                                     | 10.3 ms: 1.00x slower                                                                 |
| docutils                 | 2.92 sec                                                                    | 2.93 sec: 1.01x slower                                                                |
| comprehensions           | 22.1 us                                                                     | 22.3 us: 1.01x slower                                                                 |
| hexiom                   | 6.53 ms                                                                     | 6.58 ms: 1.01x slower                                                                 |
| sqlglot_parse            | 1.43 ms                                                                     | 1.44 ms: 1.01x slower                                                                 |
| sqlglot_optimize         | 58.8 ms                                                                     | 59.4 ms: 1.01x slower                                                                 |
| deepcopy_reduce          | 3.44 us                                                                     | 3.47 us: 1.01x slower                                                                 |
| xml_etree_generate       | 84.9 ms                                                                     | 85.8 ms: 1.01x slower                                                                 |
| sqlglot_transpile        | 1.83 ms                                                                     | 1.85 ms: 1.01x slower                                                                 |
| mdp                      | 2.55 sec                                                                    | 2.57 sec: 1.01x slower                                                                |
| scimark_lu               | 99.0 ms                                                                     | 100 ms: 1.01x slower                                                                  |
| tornado_http             | 120 ms                                                                      | 122 ms: 1.01x slower                                                                  |
| gc_traversal             | 3.52 ms                                                                     | 3.56 ms: 1.01x slower                                                                 |
| unpickle_list            | 4.79 us                                                                     | 4.85 us: 1.01x slower                                                                 |
| scimark_sor              | 144 ms                                                                      | 146 ms: 1.01x slower                                                                  |
| deepcopy_memo            | 37.7 us                                                                     | 38.2 us: 1.01x slower                                                                 |
| pathlib                  | 19.5 ms                                                                     | 19.8 ms: 1.02x slower                                                                 |
| xml_etree_process        | 59.6 ms                                                                     | 60.8 ms: 1.02x slower                                                                 |
| pprint_safe_repr         | 808 ms                                                                      | 826 ms: 1.02x slower                                                                  |
| unpack_sequence          | 48.4 ns                                                                     | 49.6 ns: 1.02x slower                                                                 |
| pycparser                | 1.32 sec                                                                    | 1.35 sec: 1.03x slower                                                                |
| pprint_pformat           | 1.65 sec                                                                    | 1.69 sec: 1.03x slower                                                                |
| go                       | 174 ms                                                                      | 179 ms: 1.03x slower                                                                  |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (28): bench_thread_pool, logging_format, raytrace, nbody, asyncio_tcp, crypto_pyaes, async_tree_cpu_io_mixed, mypy2, asyncio_tcp_ssl, pyflate, xml_etree_iterparse, float, generators, async_tree_io, bench_mp_pool, deepcopy, async_tree_none, chaos, logging_silent, dask, logging_simple, sqlglot_normalize, async_tree_memoization, tomli_loads, mako, xml_etree_parse, create_gc_cycles, pickle_pure_python
