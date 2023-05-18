
# Results vs. base

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: f190abf
- commit date: 2023-05-12
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 211 ms                                                                      | 206 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.3 ms                                                                     | 51.6 ms: 1.05x faster                                                       |
| nbody          | 69.1 ms                                                                     | 68.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 14.3 ms                                                                     | 14.1 ms: 1.02x faster                                                       |
| regex_compile  | 85.5 ms                                                                     | 84.2 ms: 1.02x faster                                                       |
| regex_effbot   | 1.60 ms                                                                     | 1.59 ms: 1.01x faster                                                       |
| regex_dna      | 117 ms                                                                      | 120 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 56.7 ms                                                                     | 54.8 ms: 1.03x faster                                                       |
| pickle_pure_python   | 191 us                                                                      | 187 us: 1.02x faster                                                        |
| pickle_dict          | 18.6 us                                                                     | 18.3 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 63.6 ms                                                                     | 62.7 ms: 1.01x faster                                                       |
| tomli_loads          | 1.33 sec                                                                    | 1.32 sec: 1.01x faster                                                      |
| xml_etree_process    | 38.1 ms                                                                     | 37.6 ms: 1.01x faster                                                       |
| xml_etree_parse      | 91.5 ms                                                                     | 90.3 ms: 1.01x faster                                                       |
| unpickle             | 8.13 us                                                                     | 8.04 us: 1.01x faster                                                       |
| unpickle_pure_python | 131 us                                                                      | 130 us: 1.01x faster                                                        |
| pickle               | 7.12 us                                                                     | 7.18 us: 1.01x slower                                                       |
| json_loads           | 13.3 us                                                                     | 13.7 us: 1.03x slower                                                       |
| json_dumps           | 5.51 ms                                                                     | 5.69 ms: 1.03x slower                                                       |
| unpickle_list        | 2.78 us                                                                     | 2.90 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                                     | 19.2 ms: 1.02x faster                                                       |
| python_startup_no_site | 16.4 ms                                                                     | 16.2 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|-----------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 6.61 ms                                                                     | 6.53 ms: 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence          | 40.8 ns                                                                     | 37.5 ns: 1.09x faster                                                       |
| scimark_monte_carlo      | 43.6 ms                                                                     | 41.3 ms: 1.06x faster                                                       |
| float                    | 54.3 ms                                                                     | 51.6 ms: 1.05x faster                                                       |
| scimark_sor              | 81.6 ms                                                                     | 77.6 ms: 1.05x faster                                                       |
| asyncio_tcp_ssl          | 2.03 sec                                                                    | 1.94 sec: 1.05x faster                                                      |
| scimark_fft              | 178 ms                                                                      | 170 ms: 1.05x faster                                                        |
| typing_runtime_protocols | 99.4 us                                                                     | 95.3 us: 1.04x faster                                                       |
| fannkuch                 | 245 ms                                                                      | 235 ms: 1.04x faster                                                        |
| logging_silent           | 60.7 ns                                                                     | 58.6 ns: 1.04x faster                                                       |
| xml_etree_generate       | 56.7 ms                                                                     | 54.8 ms: 1.03x faster                                                       |
| spectral_norm            | 64.3 ms                                                                     | 62.1 ms: 1.03x faster                                                       |
| richards_super           | 29.4 ms                                                                     | 28.6 ms: 1.03x faster                                                       |
| 2to3                     | 211 ms                                                                      | 206 ms: 1.02x faster                                                        |
| sqlglot_transpile        | 1.01 ms                                                                     | 983 us: 1.02x faster                                                        |
| async_tree_memoization   | 336 ms                                                                      | 329 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 2.46 ms                                                                     | 2.41 ms: 1.02x faster                                                       |
| pickle_pure_python       | 191 us                                                                      | 187 us: 1.02x faster                                                        |
| pickle_dict              | 18.6 us                                                                     | 18.3 us: 1.02x faster                                                       |
| go                       | 86.8 ms                                                                     | 85.0 ms: 1.02x faster                                                       |
| async_tree_none          | 288 ms                                                                      | 282 ms: 1.02x faster                                                        |
| pprint_safe_repr         | 512 ms                                                                      | 501 ms: 1.02x faster                                                        |
| raytrace                 | 188 ms                                                                      | 184 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed  | 478 ms                                                                      | 470 ms: 1.02x faster                                                        |
| hexiom                   | 3.93 ms                                                                     | 3.86 ms: 1.02x faster                                                       |
| regex_v8                 | 14.3 ms                                                                     | 14.1 ms: 1.02x faster                                                       |
| python_startup           | 19.5 ms                                                                     | 19.2 ms: 1.02x faster                                                       |
| regex_compile            | 85.5 ms                                                                     | 84.2 ms: 1.02x faster                                                       |
| bench_thread_pool        | 838 us                                                                      | 826 us: 1.02x faster                                                        |
| python_startup_no_site   | 16.4 ms                                                                     | 16.2 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 63.6 ms                                                                     | 62.7 ms: 1.01x faster                                                       |
| pathlib                  | 83.0 ms                                                                     | 81.8 ms: 1.01x faster                                                       |
| tomli_loads              | 1.33 sec                                                                    | 1.32 sec: 1.01x faster                                                      |
| chaos                    | 43.7 ms                                                                     | 43.1 ms: 1.01x faster                                                       |
| xml_etree_process        | 38.1 ms                                                                     | 37.6 ms: 1.01x faster                                                       |
| meteor_contest           | 73.3 ms                                                                     | 72.3 ms: 1.01x faster                                                       |
| xml_etree_parse          | 91.5 ms                                                                     | 90.3 ms: 1.01x faster                                                       |
| mako                     | 6.61 ms                                                                     | 6.53 ms: 1.01x faster                                                       |
| logging_simple           | 6.52 us                                                                     | 6.44 us: 1.01x faster                                                       |
| sqlglot_parse            | 794 us                                                                      | 784 us: 1.01x faster                                                        |
| nbody                    | 69.1 ms                                                                     | 68.3 ms: 1.01x faster                                                       |
| deepcopy_memo            | 23.1 us                                                                     | 22.8 us: 1.01x faster                                                       |
| unpickle                 | 8.13 us                                                                     | 8.04 us: 1.01x faster                                                       |
| mdp                      | 1.43 sec                                                                    | 1.42 sec: 1.01x faster                                                      |
| gc_traversal             | 1.49 ms                                                                     | 1.47 ms: 1.01x faster                                                       |
| richards                 | 25.5 ms                                                                     | 25.2 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 33.9 ms                                                                     | 33.6 ms: 1.01x faster                                                       |
| deepcopy                 | 231 us                                                                      | 229 us: 1.01x faster                                                        |
| unpickle_pure_python     | 131 us                                                                      | 130 us: 1.01x faster                                                        |
| pprint_pformat           | 1.04 sec                                                                    | 1.03 sec: 1.01x faster                                                      |
| dask                     | 364 ms                                                                      | 361 ms: 1.01x faster                                                        |
| pyflate                  | 289 ms                                                                      | 286 ms: 1.01x faster                                                        |
| regex_effbot             | 1.60 ms                                                                     | 1.59 ms: 1.01x faster                                                       |
| bench_mp_pool            | 67.5 ms                                                                     | 67.0 ms: 1.01x faster                                                       |
| nqueens                  | 60.4 ms                                                                     | 60.1 ms: 1.01x faster                                                       |
| pickle                   | 7.12 us                                                                     | 7.18 us: 1.01x slower                                                       |
| coroutines               | 13.8 ms                                                                     | 14.0 ms: 1.02x slower                                                       |
| json                     | 2.92 ms                                                                     | 2.97 ms: 1.02x slower                                                       |
| dulwich_log              | 41.8 ms                                                                     | 42.7 ms: 1.02x slower                                                       |
| logging_format           | 6.85 us                                                                     | 7.00 us: 1.02x slower                                                       |
| regex_dna                | 117 ms                                                                      | 120 ms: 1.03x slower                                                        |
| json_loads               | 13.3 us                                                                     | 13.7 us: 1.03x slower                                                       |
| asyncio_tcp              | 470 ms                                                                      | 483 ms: 1.03x slower                                                        |
| json_dumps               | 5.51 ms                                                                     | 5.69 ms: 1.03x slower                                                       |
| coverage                 | 50.3 ms                                                                     | 52.0 ms: 1.03x slower                                                       |
| async_generators         | 225 ms                                                                      | 234 ms: 1.04x slower                                                        |
| unpickle_list            | 2.78 us                                                                     | 2.90 us: 1.04x slower                                                       |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (18): docutils, pickle_list, sqlglot_normalize, aiohttp, pidigits, mypy2, async_tree_io, deltablue, tornado_http, generators, telco, sqlite_synth, comprehensions, crypto_pyaes, scimark_lu, deepcopy_reduce, create_gc_cycles, pycparser
