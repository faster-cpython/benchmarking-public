
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: ed869aa
- commit date: 2023-03-23
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 196 ms: 1.21x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.54 ms: 1.31x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.52 sec: 1.24x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.8 ms: 1.30x faster                                                       |
| tornado_http   | 109 ms                                                      | 87.2 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 47.2 ms: 1.27x faster                                                       |
| nbody          | 69.3 ms                                                     | 56.6 ms: 1.23x faster                                                       |
| pidigits       | 145 ms                                                      | 145 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 82.3 ms: 1.26x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.5 ms: 1.12x faster                                                       |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.41 ms: 1.57x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 175 us: 1.47x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 127 us: 1.35x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.7 ms: 1.22x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.01 us: 1.15x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.4 ms: 1.13x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.8 ms: 1.05x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.72 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.7 ms: 1.03x faster                                                       |
| pickle_list          | 2.59 us                                                     | 2.82 us: 1.09x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.21 ms: 1.42x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.5 ms: 1.41x faster                                                       |
| django_template | 28.2 ms                                                     | 20.5 ms: 1.38x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.38x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.98 ms: 2.10x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 57.7 ns: 1.67x faster                                                       |
| mypy2                   | 352 ms                                                      | 211 ms: 1.67x faster                                                        |
| raytrace                | 271 ms                                                      | 172 ms: 1.58x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.41 ms: 1.57x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 54.4 ms: 1.57x faster                                                       |
| go                      | 136 ms                                                      | 87.3 ms: 1.56x faster                                                       |
| richards                | 41.2 ms                                                     | 26.7 ms: 1.54x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 471 ms: 1.51x faster                                                        |
| generators              | 31.6 ms                                                     | 21.2 ms: 1.49x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 175 us: 1.47x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 736 ms: 1.45x faster                                                        |
| chaos                   | 58.9 ms                                                     | 41.2 ms: 1.43x faster                                                       |
| async_tree_none         | 420 ms                                                      | 296 ms: 1.42x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.21 ms: 1.42x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.90 ms: 1.42x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 353 ms: 1.41x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 13.5 ms: 1.41x faster                                                       |
| scimark_sor             | 105 ms                                                      | 74.8 ms: 1.40x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 871 us: 1.40x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.06 ms: 1.38x faster                                                       |
| django_template         | 28.2 ms                                                     | 20.5 ms: 1.38x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 45.2 ms: 1.38x faster                                                       |
| pyflate                 | 387 ms                                                      | 282 ms: 1.37x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.1 ms: 1.36x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 28.1 ns: 1.35x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 127 us: 1.35x faster                                                        |
| thrift                  | 615 us                                                      | 457 us: 1.35x faster                                                        |
| pycparser               | 868 ms                                                      | 653 ms: 1.33x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.54 ms: 1.31x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 21.9 us: 1.30x faster                                                       |
| html5lib                | 46.5 ms                                                     | 35.8 ms: 1.30x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 936 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 478 ms: 1.28x faster                                                        |
| float                   | 60.2 ms                                                     | 47.2 ms: 1.27x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 462 ms: 1.27x faster                                                        |
| regex_compile           | 103 ms                                                      | 82.3 ms: 1.26x faster                                                       |
| tornado_http            | 109 ms                                                      | 87.2 ms: 1.25x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.52 sec: 1.24x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 31.4 ms: 1.24x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 63.6 ms: 1.23x faster                                                       |
| nbody                   | 69.3 ms                                                     | 56.6 ms: 1.23x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 35.7 ms: 1.22x faster                                                       |
| 2to3                    | 237 ms                                                      | 196 ms: 1.21x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 168 ms: 1.20x faster                                                        |
| deepcopy                | 255 us                                                      | 215 us: 1.19x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.44 sec: 1.19x faster                                                      |
| sympy_expand            | 315 ms                                                      | 270 ms: 1.17x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 57.5 ms: 1.17x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.8 ms: 1.16x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.86 us: 1.16x faster                                                       |
| scimark_fft             | 193 ms                                                      | 167 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.32 ms: 1.15x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 825 us: 1.15x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.01 us: 1.15x faster                                                       |
| json                    | 3.05 ms                                                     | 2.70 ms: 1.13x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 90.4 ms: 1.13x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 698 us: 1.12x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.5 ms: 1.12x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.3 ms: 1.11x faster                                                       |
| fannkuch                | 258 ms                                                      | 233 ms: 1.11x faster                                                        |
| sympy_str               | 188 ms                                                      | 171 ms: 1.10x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 43.2 ms: 1.10x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                       |
| regex_dna               | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| sympy_sum               | 104 ms                                                      | 96.3 ms: 1.08x faster                                                       |
| async_generators        | 224 ms                                                      | 208 ms: 1.08x faster                                                        |
| xml_etree_generate      | 54.5 ms                                                     | 51.8 ms: 1.05x faster                                                       |
| json_loads              | 14.2 us                                                     | 13.5 us: 1.05x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.2 us: 1.05x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 69.8 ms: 1.04x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.72 us: 1.04x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.78 us: 1.03x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.46 us: 1.03x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.7 ms: 1.03x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.10 us: 1.02x faster                                                       |
| pidigits                | 145 ms                                                      | 145 ms: 1.00x faster                                                        |
| telco                   | 3.78 ms                                                     | 3.80 ms: 1.00x slower                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 64.5 ms: 1.06x slower                                                       |
| pathlib                 | 77.4 ms                                                     | 82.7 ms: 1.07x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.46 ms: 1.08x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.82 us: 1.09x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| dask                    | 305 ms                                                      | 355 ms: 1.16x slower                                                        |
| coverage                | 40.0 ms                                                     | 52.9 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (2): python_startup_no_site, pickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
