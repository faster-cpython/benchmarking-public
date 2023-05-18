
# Results vs. base

- fork: adr26
- ref: condvar
- machine: windows-amd64
- commit hash: 4f0355f
- commit date: 2023-05-16
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.61 sec                                                                    | 1.63 sec: 1.01x slower                                        |
| tornado_http   | 88.4 ms                                                                     | 87.4 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                  |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 76.5 ms                                                                     | 72.7 ms: 1.05x faster                                         |
| float          | 55.9 ms                                                                     | 55.2 ms: 1.01x faster                                         |
| pidigits       | 149 ms                                                                      | 151 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 87.4 ms                                                                     | 85.8 ms: 1.02x faster                                         |
| regex_dna      | 118 ms                                                                      | 117 ms: 1.01x faster                                          |
| regex_effbot   | 1.59 ms                                                                     | 1.58 ms: 1.01x faster                                         |
| regex_v8       | 13.7 ms                                                                     | 13.8 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_list        | 2.88 us                                                                     | 2.77 us: 1.04x faster                                         |
| xml_etree_process    | 40.2 ms                                                                     | 38.9 ms: 1.03x faster                                         |
| tomli_loads          | 1.43 sec                                                                    | 1.39 sec: 1.03x faster                                        |
| pickle_pure_python   | 198 us                                                                      | 193 us: 1.03x faster                                          |
| xml_etree_iterparse  | 65.8 ms                                                                     | 64.2 ms: 1.02x faster                                         |
| unpickle_pure_python | 138 us                                                                      | 136 us: 1.02x faster                                          |
| json_dumps           | 5.82 ms                                                                     | 5.71 ms: 1.02x faster                                         |
| json_loads           | 13.7 us                                                                     | 13.6 us: 1.01x faster                                         |
| xml_etree_generate   | 57.2 ms                                                                     | 57.7 ms: 1.01x slower                                         |
| unpickle             | 8.33 us                                                                     | 8.45 us: 1.01x slower                                         |
| pickle_dict          | 18.1 us                                                                     | 18.6 us: 1.03x slower                                         |
| pickle               | 7.15 us                                                                     | 7.44 us: 1.04x slower                                         |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                  |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 6.92 ms                                                                     | 6.87 ms: 1.01x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpack_sequence          | 41.4 ns                                                                     | 36.5 ns: 1.13x faster                                         |
| hexiom                   | 4.31 ms                                                                     | 4.05 ms: 1.06x faster                                         |
| scimark_sor              | 85.1 ms                                                                     | 80.2 ms: 1.06x faster                                         |
| fannkuch                 | 245 ms                                                                      | 233 ms: 1.06x faster                                          |
| typing_runtime_protocols | 105 us                                                                      | 99.4 us: 1.05x faster                                         |
| nbody                    | 76.5 ms                                                                     | 72.7 ms: 1.05x faster                                         |
| scimark_fft              | 187 ms                                                                      | 178 ms: 1.05x faster                                          |
| deepcopy_memo            | 25.1 us                                                                     | 23.9 us: 1.05x faster                                         |
| bench_thread_pool        | 853 us                                                                      | 814 us: 1.05x faster                                          |
| pprint_pformat           | 1.10 sec                                                                    | 1.05 sec: 1.05x faster                                        |
| unpickle_list            | 2.88 us                                                                     | 2.77 us: 1.04x faster                                         |
| pprint_safe_repr         | 539 ms                                                                      | 519 ms: 1.04x faster                                          |
| chaos                    | 44.4 ms                                                                     | 42.8 ms: 1.04x faster                                         |
| nqueens                  | 62.2 ms                                                                     | 60.1 ms: 1.03x faster                                         |
| xml_etree_process        | 40.2 ms                                                                     | 38.9 ms: 1.03x faster                                         |
| tomli_loads              | 1.43 sec                                                                    | 1.39 sec: 1.03x faster                                        |
| sqlglot_parse            | 834 us                                                                      | 810 us: 1.03x faster                                          |
| comprehensions           | 14.6 us                                                                     | 14.2 us: 1.03x faster                                         |
| crypto_pyaes             | 48.0 ms                                                                     | 46.7 ms: 1.03x faster                                         |
| pyflate                  | 305 ms                                                                      | 297 ms: 1.03x faster                                          |
| logging_format           | 7.11 us                                                                     | 6.92 us: 1.03x faster                                         |
| async_generators         | 235 ms                                                                      | 229 ms: 1.03x faster                                          |
| pickle_pure_python       | 198 us                                                                      | 193 us: 1.03x faster                                          |
| sqlglot_transpile        | 1.05 ms                                                                     | 1.02 ms: 1.03x faster                                         |
| logging_simple           | 6.65 us                                                                     | 6.49 us: 1.03x faster                                         |
| richards_super           | 31.2 ms                                                                     | 30.4 ms: 1.02x faster                                         |
| xml_etree_iterparse      | 65.8 ms                                                                     | 64.2 ms: 1.02x faster                                         |
| go                       | 89.4 ms                                                                     | 87.6 ms: 1.02x faster                                         |
| unpickle_pure_python     | 138 us                                                                      | 136 us: 1.02x faster                                          |
| json_dumps               | 5.82 ms                                                                     | 5.71 ms: 1.02x faster                                         |
| aiohttp                  | 904 us                                                                      | 886 us: 1.02x faster                                          |
| regex_compile            | 87.4 ms                                                                     | 85.8 ms: 1.02x faster                                         |
| scimark_monte_carlo      | 44.7 ms                                                                     | 43.8 ms: 1.02x faster                                         |
| deltablue                | 2.21 ms                                                                     | 2.17 ms: 1.02x faster                                         |
| mypy2                    | 215 ms                                                                      | 212 ms: 1.02x faster                                          |
| async_tree_none          | 286 ms                                                                      | 281 ms: 1.02x faster                                          |
| dulwich_log              | 42.4 ms                                                                     | 41.6 ms: 1.02x faster                                         |
| richards                 | 27.4 ms                                                                     | 27.0 ms: 1.01x faster                                         |
| float                    | 55.9 ms                                                                     | 55.2 ms: 1.01x faster                                         |
| tornado_http             | 88.4 ms                                                                     | 87.4 ms: 1.01x faster                                         |
| raytrace                 | 191 ms                                                                      | 189 ms: 1.01x faster                                          |
| regex_dna                | 118 ms                                                                      | 117 ms: 1.01x faster                                          |
| spectral_norm            | 65.0 ms                                                                     | 64.3 ms: 1.01x faster                                         |
| regex_effbot             | 1.59 ms                                                                     | 1.58 ms: 1.01x faster                                         |
| sqlglot_optimize         | 34.7 ms                                                                     | 34.4 ms: 1.01x faster                                         |
| json_loads               | 13.7 us                                                                     | 13.6 us: 1.01x faster                                         |
| gc_traversal             | 1.47 ms                                                                     | 1.46 ms: 1.01x faster                                         |
| mako                     | 6.92 ms                                                                     | 6.87 ms: 1.01x faster                                         |
| mdp                      | 1.45 sec                                                                    | 1.44 sec: 1.01x faster                                        |
| coroutines               | 14.5 ms                                                                     | 14.4 ms: 1.01x faster                                         |
| sqlite_synth             | 1.70 us                                                                     | 1.69 us: 1.01x faster                                         |
| logging_silent           | 60.9 ns                                                                     | 61.2 ns: 1.01x slower                                         |
| docutils                 | 1.61 sec                                                                    | 1.63 sec: 1.01x slower                                        |
| regex_v8                 | 13.7 ms                                                                     | 13.8 ms: 1.01x slower                                         |
| xml_etree_generate       | 57.2 ms                                                                     | 57.7 ms: 1.01x slower                                         |
| generators               | 22.9 ms                                                                     | 23.1 ms: 1.01x slower                                         |
| coverage                 | 50.4 ms                                                                     | 50.9 ms: 1.01x slower                                         |
| pathlib                  | 82.0 ms                                                                     | 82.9 ms: 1.01x slower                                         |
| json                     | 3.02 ms                                                                     | 3.05 ms: 1.01x slower                                         |
| scimark_sparse_mat_mult  | 2.50 ms                                                                     | 2.54 ms: 1.01x slower                                         |
| unpickle                 | 8.33 us                                                                     | 8.45 us: 1.01x slower                                         |
| pidigits                 | 149 ms                                                                      | 151 ms: 1.02x slower                                          |
| dask                     | 364 ms                                                                      | 371 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed  | 471 ms                                                                      | 481 ms: 1.02x slower                                          |
| pickle_dict              | 18.1 us                                                                     | 18.6 us: 1.03x slower                                         |
| telco                    | 4.02 ms                                                                     | 4.16 ms: 1.03x slower                                         |
| pickle                   | 7.15 us                                                                     | 7.44 us: 1.04x slower                                         |
| asyncio_tcp_ssl          | 1.89 sec                                                                    | 2.02 sec: 1.07x slower                                        |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                  |

Benchmark hidden because not significant (16): pickle_list, deepcopy, pycparser, asyncio_tcp, python_startup, python_startup_no_site, 2to3, xml_etree_parse, sqlglot_normalize, deepcopy_reduce, meteor_contest, async_tree_memoization, bench_mp_pool, scimark_lu, create_gc_cycles, async_tree_io
