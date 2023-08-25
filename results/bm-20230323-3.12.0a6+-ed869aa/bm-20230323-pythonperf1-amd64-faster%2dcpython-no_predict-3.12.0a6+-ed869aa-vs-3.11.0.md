
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: ed869aa
- commit date: 2023-03-23
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 196 ms: 1.06x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.54 ms: 1.13x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.52 sec: 1.05x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 87.2 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 56.6 ms: 1.24x faster                                                       |
| float          | 54.6 ms                                                     | 47.2 ms: 1.16x faster                                                       |
| pidigits       | 148 ms                                                      | 145 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.5 ms: 1.03x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.41 ms: 1.40x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 127 us: 1.19x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 175 us: 1.14x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 90.4 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.7 ms: 1.01x faster                                                       |
| unpickle             | 8.09 us                                                     | 8.01 us: 1.01x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.8 ms: 1.01x faster                                                       |
| pickle               | 6.61 us                                                     | 6.78 us: 1.03x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.82 us: 1.05x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.72 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                       |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.5 ms: 1.25x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                       |
| django_template | 24.1 ms                                                     | 20.5 ms: 1.18x faster                                                       |
| mako            | 7.26 ms                                                     | 6.21 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 28.1 ns: 1.64x faster                                                       |
| generators              | 33.8 ms                                                     | 21.2 ms: 1.60x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 471 ms: 1.48x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.41 ms: 1.40x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.98 ms: 1.32x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.5 ms: 1.25x faster                                                       |
| nbody                   | 70.0 ms                                                     | 56.6 ms: 1.24x faster                                                       |
| raytrace                | 211 ms                                                      | 172 ms: 1.23x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 57.7 ns: 1.21x faster                                                       |
| json                    | 3.25 ms                                                     | 2.70 ms: 1.21x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 127 us: 1.19x faster                                                        |
| django_template         | 24.1 ms                                                     | 20.5 ms: 1.18x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.21 ms: 1.17x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.90 ms: 1.17x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 54.4 ms: 1.17x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| float                   | 54.6 ms                                                     | 47.2 ms: 1.16x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.9 us: 1.15x faster                                                       |
| richards                | 30.6 ms                                                     | 26.7 ms: 1.14x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 175 us: 1.14x faster                                                        |
| chaos                   | 47.1 ms                                                     | 41.2 ms: 1.14x faster                                                       |
| deepcopy                | 246 us                                                      | 215 us: 1.14x faster                                                        |
| sqlglot_normalize       | 190 ms                                                      | 168 ms: 1.13x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 57.5 ms: 1.13x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.54 ms: 1.13x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.86 us: 1.12x faster                                                       |
| go                      | 97.3 ms                                                     | 87.3 ms: 1.11x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 31.4 ms: 1.11x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 936 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.32 ms: 1.11x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 462 ms: 1.11x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 871 us: 1.09x faster                                                        |
| sympy_expand            | 295 ms                                                      | 270 ms: 1.09x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.46 us: 1.09x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.1 ms: 1.09x faster                                                       |
| mypy2                   | 229 ms                                                      | 211 ms: 1.09x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.10 us: 1.08x faster                                                       |
| fannkuch                | 252 ms                                                      | 233 ms: 1.08x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 12.8 ms: 1.08x faster                                                       |
| async_tree_none         | 320 ms                                                      | 296 ms: 1.08x faster                                                        |
| pyflate                 | 304 ms                                                      | 282 ms: 1.08x faster                                                        |
| thrift                  | 491 us                                                      | 457 us: 1.07x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 69.8 ms: 1.07x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 63.6 ms: 1.07x faster                                                       |
| scimark_fft             | 178 ms                                                      | 167 ms: 1.07x faster                                                        |
| sympy_str               | 182 ms                                                      | 171 ms: 1.07x faster                                                        |
| 2to3                    | 209 ms                                                      | 196 ms: 1.06x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 90.4 ms: 1.06x faster                                                       |
| pycparser               | 691 ms                                                      | 653 ms: 1.06x faster                                                        |
| coverage                | 55.9 ms                                                     | 52.9 ms: 1.06x faster                                                       |
| async_tree_io           | 779 ms                                                      | 736 ms: 1.06x faster                                                        |
| tornado_http            | 91.8 ms                                                     | 87.2 ms: 1.05x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.52 sec: 1.05x faster                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 45.2 ms: 1.05x faster                                                       |
| async_tree_memoization  | 371 ms                                                      | 353 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 478 ms: 1.05x faster                                                        |
| html5lib                | 37.5 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.2 us: 1.05x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 96.3 ms: 1.04x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 825 us: 1.03x faster                                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 43.2 ms: 1.03x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.5 ms: 1.03x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.80 ms: 1.03x faster                                                       |
| pidigits                | 148 ms                                                      | 145 ms: 1.03x faster                                                        |
| coroutines              | 14.6 ms                                                     | 14.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.7 ms: 1.01x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 74.8 ms: 1.01x faster                                                       |
| unpickle                | 8.09 us                                                     | 8.01 us: 1.01x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.8 ms: 1.01x faster                                                       |
| pickle                  | 6.61 us                                                     | 6.78 us: 1.03x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| json_loads              | 12.9 us                                                     | 13.5 us: 1.05x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.82 us: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.72 us: 1.07x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 82.7 ms: 1.16x slower                                                       |
| async_generators        | 178 ms                                                      | 208 ms: 1.17x slower                                                        |
| dask                    | 264 ms                                                      | 355 ms: 1.34x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (3): gc_traversal, pickle_dict, create_gc_cycles
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x
