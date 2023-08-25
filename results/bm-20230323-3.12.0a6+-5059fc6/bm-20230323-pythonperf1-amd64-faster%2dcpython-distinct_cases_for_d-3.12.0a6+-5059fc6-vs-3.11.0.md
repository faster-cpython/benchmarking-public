
# Results vs. 3.11.0

- fork: faster-cpython
- ref: distinct_cases_for_d
- machine: windows-amd64
- commit hash: 5059fc6
- commit date: 2023-03-23
- overall geometric mean: 1.12x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 194 ms: 1.08x faster                                                                  |
| chameleon      | 5.11 ms                                                     | 4.31 ms: 1.19x faster                                                                 |
| docutils       | 1.60 sec                                                    | 1.49 sec: 1.08x faster                                                                |
| html5lib       | 37.5 ms                                                     | 34.9 ms: 1.07x faster                                                                 |
| tornado_http   | 91.8 ms                                                     | 84.1 ms: 1.09x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 51.1 ms: 1.37x faster                                                                 |
| float          | 54.6 ms                                                     | 45.6 ms: 1.20x faster                                                                 |
| pidigits       | 148 ms                                                      | 144 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 78.3 ms: 1.16x faster                                                                 |
| regex_v8       | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                                                 |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                                  |
| regex_effbot   | 1.50 ms                                                     | 1.82 ms: 1.22x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.44 ms: 1.39x faster                                                                 |
| unpickle_pure_python | 152 us                                                      | 118 us: 1.29x faster                                                                  |
| pickle_pure_python   | 200 us                                                      | 168 us: 1.19x faster                                                                  |
| xml_etree_parse      | 95.9 ms                                                     | 88.7 ms: 1.08x faster                                                                 |
| xml_etree_process    | 37.1 ms                                                     | 34.3 ms: 1.08x faster                                                                 |
| xml_etree_generate   | 52.2 ms                                                     | 50.2 ms: 1.04x faster                                                                 |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.4 ms: 1.04x faster                                                                 |
| json_loads           | 12.9 us                                                     | 13.3 us: 1.03x slower                                                                 |
| pickle_list          | 2.68 us                                                     | 2.80 us: 1.04x slower                                                                 |
| unpickle_list        | 2.55 us                                                     | 2.72 us: 1.07x slower                                                                 |
| pickle               | 6.61 us                                                     | 7.12 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                                 |
| python_startup         | 18.7 ms                                                     | 18.1 ms: 1.03x faster                                                                 |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.1 ms: 1.29x faster                                                                 |
| genshi_xml      | 37.3 ms                                                     | 29.5 ms: 1.27x faster                                                                 |
| django_template | 24.1 ms                                                     | 20.1 ms: 1.20x faster                                                                 |
| mako            | 7.26 ms                                                     | 6.10 ms: 1.19x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 27.2 ns: 1.69x faster                                                                 |
| generators              | 33.8 ms                                                     | 20.7 ms: 1.63x faster                                                                 |
| asyncio_tcp             | 699 ms                                                      | 465 ms: 1.50x faster                                                                  |
| deltablue               | 2.61 ms                                                     | 1.82 ms: 1.43x faster                                                                 |
| json_dumps              | 7.56 ms                                                     | 5.44 ms: 1.39x faster                                                                 |
| nbody                   | 70.0 ms                                                     | 51.1 ms: 1.37x faster                                                                 |
| deepcopy_memo           | 25.2 us                                                     | 19.0 us: 1.32x faster                                                                 |
| richards                | 30.6 ms                                                     | 23.5 ms: 1.30x faster                                                                 |
| raytrace                | 211 ms                                                      | 162 ms: 1.30x faster                                                                  |
| logging_silent          | 69.8 ns                                                     | 53.8 ns: 1.30x faster                                                                 |
| genshi_text             | 17.0 ms                                                     | 13.1 ms: 1.29x faster                                                                 |
| unpickle_pure_python    | 152 us                                                      | 118 us: 1.29x faster                                                                  |
| hexiom                  | 4.55 ms                                                     | 3.59 ms: 1.27x faster                                                                 |
| genshi_xml              | 37.3 ms                                                     | 29.5 ms: 1.27x faster                                                                 |
| mdp                     | 1.67 sec                                                    | 1.33 sec: 1.26x faster                                                                |
| deepcopy                | 246 us                                                      | 198 us: 1.24x faster                                                                  |
| scimark_lu              | 63.5 ms                                                     | 51.6 ms: 1.23x faster                                                                 |
| chaos                   | 47.1 ms                                                     | 38.4 ms: 1.23x faster                                                                 |
| go                      | 97.3 ms                                                     | 79.4 ms: 1.23x faster                                                                 |
| django_template         | 24.1 ms                                                     | 20.1 ms: 1.20x faster                                                                 |
| float                   | 54.6 ms                                                     | 45.6 ms: 1.20x faster                                                                 |
| mako                    | 7.26 ms                                                     | 6.10 ms: 1.19x faster                                                                 |
| pickle_pure_python      | 200 us                                                      | 168 us: 1.19x faster                                                                  |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.16 ms: 1.19x faster                                                                 |
| chameleon               | 5.11 ms                                                     | 4.31 ms: 1.19x faster                                                                 |
| json                    | 3.25 ms                                                     | 2.75 ms: 1.18x faster                                                                 |
| scimark_monte_carlo     | 44.6 ms                                                     | 37.7 ms: 1.18x faster                                                                 |
| nqueens                 | 64.9 ms                                                     | 55.1 ms: 1.18x faster                                                                 |
| sqlglot_normalize       | 190 ms                                                      | 164 ms: 1.16x faster                                                                  |
| sqlglot_optimize        | 34.9 ms                                                     | 30.1 ms: 1.16x faster                                                                 |
| deepcopy_reduce         | 2.07 us                                                     | 1.79 us: 1.16x faster                                                                 |
| regex_compile           | 90.6 ms                                                     | 78.3 ms: 1.16x faster                                                                 |
| sqlglot_transpile       | 1.16 ms                                                     | 1.01 ms: 1.15x faster                                                                 |
| sqlglot_parse           | 952 us                                                      | 829 us: 1.15x faster                                                                  |
| spectral_norm           | 67.9 ms                                                     | 59.4 ms: 1.14x faster                                                                 |
| pprint_pformat          | 1.04 sec                                                    | 909 ms: 1.14x faster                                                                  |
| scimark_fft             | 178 ms                                                      | 156 ms: 1.14x faster                                                                  |
| coverage                | 55.9 ms                                                     | 49.2 ms: 1.14x faster                                                                 |
| mypy2                   | 229 ms                                                      | 202 ms: 1.13x faster                                                                  |
| pprint_safe_repr        | 512 ms                                                      | 452 ms: 1.13x faster                                                                  |
| sympy_integrate         | 13.8 ms                                                     | 12.4 ms: 1.11x faster                                                                 |
| pyflate                 | 304 ms                                                      | 273 ms: 1.11x faster                                                                  |
| sympy_expand            | 295 ms                                                      | 266 ms: 1.11x faster                                                                  |
| meteor_contest          | 74.7 ms                                                     | 68.3 ms: 1.09x faster                                                                 |
| scimark_sor             | 75.6 ms                                                     | 69.1 ms: 1.09x faster                                                                 |
| sympy_str               | 182 ms                                                      | 166 ms: 1.09x faster                                                                  |
| dulwich_log             | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                                 |
| tornado_http            | 91.8 ms                                                     | 84.1 ms: 1.09x faster                                                                 |
| comprehensions          | 15.9 us                                                     | 14.6 us: 1.09x faster                                                                 |
| logging_format          | 7.01 us                                                     | 6.44 us: 1.09x faster                                                                 |
| crypto_pyaes            | 47.6 ms                                                     | 43.6 ms: 1.09x faster                                                                 |
| logging_simple          | 6.61 us                                                     | 6.07 us: 1.09x faster                                                                 |
| sympy_sum               | 99.9 ms                                                     | 92.3 ms: 1.08x faster                                                                 |
| xml_etree_parse         | 95.9 ms                                                     | 88.7 ms: 1.08x faster                                                                 |
| xml_etree_process       | 37.1 ms                                                     | 34.3 ms: 1.08x faster                                                                 |
| pycparser               | 691 ms                                                      | 640 ms: 1.08x faster                                                                  |
| async_tree_none         | 320 ms                                                      | 297 ms: 1.08x faster                                                                  |
| 2to3                    | 209 ms                                                      | 194 ms: 1.08x faster                                                                  |
| docutils                | 1.60 sec                                                    | 1.49 sec: 1.08x faster                                                                |
| html5lib                | 37.5 ms                                                     | 34.9 ms: 1.07x faster                                                                 |
| async_tree_io           | 779 ms                                                      | 731 ms: 1.07x faster                                                                  |
| async_tree_memoization  | 371 ms                                                      | 349 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed | 501 ms                                                      | 473 ms: 1.06x faster                                                                  |
| fannkuch                | 252 ms                                                      | 238 ms: 1.06x faster                                                                  |
| thrift                  | 491 us                                                      | 464 us: 1.06x faster                                                                  |
| bench_thread_pool       | 852 us                                                      | 813 us: 1.05x faster                                                                  |
| xml_etree_generate      | 52.2 ms                                                     | 50.2 ms: 1.04x faster                                                                 |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.4 ms: 1.04x faster                                                                 |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                                 |
| python_startup          | 18.7 ms                                                     | 18.1 ms: 1.03x faster                                                                 |
| pidigits                | 148 ms                                                      | 144 ms: 1.03x faster                                                                  |
| coroutines              | 14.6 ms                                                     | 14.3 ms: 1.02x faster                                                                 |
| regex_v8                | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                                                 |
| telco                   | 3.90 ms                                                     | 3.85 ms: 1.01x faster                                                                 |
| gc_traversal            | 1.46 ms                                                     | 1.44 ms: 1.01x faster                                                                 |
| bench_mp_pool           | 62.5 ms                                                     | 64.0 ms: 1.02x slower                                                                 |
| regex_dna               | 115 ms                                                      | 118 ms: 1.02x slower                                                                  |
| json_loads              | 12.9 us                                                     | 13.3 us: 1.03x slower                                                                 |
| pickle_list             | 2.68 us                                                     | 2.80 us: 1.04x slower                                                                 |
| sqlite_synth            | 1.68 us                                                     | 1.76 us: 1.05x slower                                                                 |
| unpickle_list           | 2.55 us                                                     | 2.72 us: 1.07x slower                                                                 |
| pickle                  | 6.61 us                                                     | 7.12 us: 1.08x slower                                                                 |
| async_generators        | 178 ms                                                      | 203 ms: 1.14x slower                                                                  |
| pathlib                 | 71.4 ms                                                     | 82.9 ms: 1.16x slower                                                                 |
| regex_effbot            | 1.50 ms                                                     | 1.82 ms: 1.22x slower                                                                 |
| dask                    | 264 ms                                                      | 352 ms: 1.33x slower                                                                  |
| Geometric mean          | (ref)                                                       | 1.12x faster                                                                          |

Benchmark hidden because not significant (3): unpickle, create_gc_cycles, pickle_dict
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.08x
