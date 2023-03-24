
# Results vs. base

- fork: faster-cpython
- ref: distinct_cases_for_d
- machine: windows-amd64
- commit hash: 5059fc6
- commit date: 2023-03-23
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 194 ms                                                                      | 194 ms: 1.00x faster                                                                  |
| docutils       | 1.51 sec                                                                    | 1.49 sec: 1.02x faster                                                                |
| html5lib       | 35.5 ms                                                                     | 34.9 ms: 1.02x faster                                                                 |
| tornado_http   | 86.7 ms                                                                     | 84.1 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 55.6 ms                                                                     | 51.1 ms: 1.09x faster                                                                 |
| pidigits       | 146 ms                                                                      | 144 ms: 1.01x faster                                                                  |
| float          | 46.0 ms                                                                     | 45.6 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                      | 118 ms: 1.03x faster                                                                  |
| regex_v8       | 13.8 ms                                                                     | 13.5 ms: 1.02x faster                                                                 |
| regex_compile  | 79.6 ms                                                                     | 78.3 ms: 1.02x faster                                                                 |
| regex_effbot   | 1.83 ms                                                                     | 1.82 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads           | 13.4 us                                                                     | 13.3 us: 1.01x faster                                                                 |
| pickle_pure_python   | 168 us                                                                      | 168 us: 1.00x faster                                                                  |
| xml_etree_generate   | 50.0 ms                                                                     | 50.2 ms: 1.00x slower                                                                 |
| unpickle_list        | 2.70 us                                                                     | 2.72 us: 1.01x slower                                                                 |
| unpickle_pure_python | 117 us                                                                      | 118 us: 1.01x slower                                                                  |
| xml_etree_process    | 33.9 ms                                                                     | 34.3 ms: 1.01x slower                                                                 |
| unpickle             | 7.96 us                                                                     | 8.06 us: 1.01x slower                                                                 |
| xml_etree_parse      | 87.3 ms                                                                     | 88.7 ms: 1.02x slower                                                                 |
| xml_etree_iterparse  | 59.2 ms                                                                     | 60.4 ms: 1.02x slower                                                                 |
| pickle               | 6.65 us                                                                     | 7.12 us: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (3): pickle_dict, json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup | 18.2 ms                                                                     | 18.1 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 13.8 ms                                                                     | 13.1 ms: 1.06x faster                                                                 |
| genshi_xml      | 30.5 ms                                                                     | 29.5 ms: 1.04x faster                                                                 |
| django_template | 19.9 ms                                                                     | 20.1 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody                   | 55.6 ms                                                                     | 51.1 ms: 1.09x faster                                                                 |
| genshi_text             | 13.8 ms                                                                     | 13.1 ms: 1.06x faster                                                                 |
| deltablue               | 1.91 ms                                                                     | 1.82 ms: 1.05x faster                                                                 |
| scimark_monte_carlo     | 39.3 ms                                                                     | 37.7 ms: 1.04x faster                                                                 |
| genshi_xml              | 30.5 ms                                                                     | 29.5 ms: 1.04x faster                                                                 |
| sympy_sum               | 95.6 ms                                                                     | 92.3 ms: 1.04x faster                                                                 |
| richards                | 24.3 ms                                                                     | 23.5 ms: 1.04x faster                                                                 |
| mypy2                   | 209 ms                                                                      | 202 ms: 1.04x faster                                                                  |
| sympy_integrate         | 12.8 ms                                                                     | 12.4 ms: 1.03x faster                                                                 |
| dulwich_log             | 42.1 ms                                                                     | 40.7 ms: 1.03x faster                                                                 |
| deepcopy_memo           | 19.6 us                                                                     | 19.0 us: 1.03x faster                                                                 |
| meteor_contest          | 70.4 ms                                                                     | 68.3 ms: 1.03x faster                                                                 |
| deepcopy                | 204 us                                                                      | 198 us: 1.03x faster                                                                  |
| regex_dna               | 122 ms                                                                      | 118 ms: 1.03x faster                                                                  |
| tornado_http            | 86.7 ms                                                                     | 84.1 ms: 1.03x faster                                                                 |
| chaos                   | 39.6 ms                                                                     | 38.4 ms: 1.03x faster                                                                 |
| spectral_norm           | 61.1 ms                                                                     | 59.4 ms: 1.03x faster                                                                 |
| sqlglot_transpile       | 1.03 ms                                                                     | 1.01 ms: 1.02x faster                                                                 |
| mdp                     | 1.36 sec                                                                    | 1.33 sec: 1.02x faster                                                                |
| sqlglot_optimize        | 30.8 ms                                                                     | 30.1 ms: 1.02x faster                                                                 |
| regex_v8                | 13.8 ms                                                                     | 13.5 ms: 1.02x faster                                                                 |
| hexiom                  | 3.66 ms                                                                     | 3.59 ms: 1.02x faster                                                                 |
| scimark_sor             | 70.6 ms                                                                     | 69.1 ms: 1.02x faster                                                                 |
| gc_traversal            | 1.47 ms                                                                     | 1.44 ms: 1.02x faster                                                                 |
| sympy_expand            | 271 ms                                                                      | 266 ms: 1.02x faster                                                                  |
| coverage                | 50.1 ms                                                                     | 49.2 ms: 1.02x faster                                                                 |
| deepcopy_reduce         | 1.82 us                                                                     | 1.79 us: 1.02x faster                                                                 |
| html5lib                | 35.5 ms                                                                     | 34.9 ms: 1.02x faster                                                                 |
| scimark_sparse_mat_mult | 2.20 ms                                                                     | 2.16 ms: 1.02x faster                                                                 |
| scimark_fft             | 159 ms                                                                      | 156 ms: 1.02x faster                                                                  |
| sympy_str               | 169 ms                                                                      | 166 ms: 1.02x faster                                                                  |
| docutils                | 1.51 sec                                                                    | 1.49 sec: 1.02x faster                                                                |
| regex_compile           | 79.6 ms                                                                     | 78.3 ms: 1.02x faster                                                                 |
| sqlglot_parse           | 843 us                                                                      | 829 us: 1.02x faster                                                                  |
| go                      | 80.6 ms                                                                     | 79.4 ms: 1.02x faster                                                                 |
| crypto_pyaes            | 44.3 ms                                                                     | 43.6 ms: 1.01x faster                                                                 |
| comprehensions          | 14.8 us                                                                     | 14.6 us: 1.01x faster                                                                 |
| logging_silent          | 54.5 ns                                                                     | 53.8 ns: 1.01x faster                                                                 |
| raytrace                | 164 ms                                                                      | 162 ms: 1.01x faster                                                                  |
| bench_mp_pool           | 64.8 ms                                                                     | 64.0 ms: 1.01x faster                                                                 |
| sqlglot_normalize       | 166 ms                                                                      | 164 ms: 1.01x faster                                                                  |
| pidigits                | 146 ms                                                                      | 144 ms: 1.01x faster                                                                  |
| float                   | 46.0 ms                                                                     | 45.6 ms: 1.01x faster                                                                 |
| create_gc_cycles        | 698 us                                                                      | 693 us: 1.01x faster                                                                  |
| generators              | 20.9 ms                                                                     | 20.7 ms: 1.01x faster                                                                 |
| regex_effbot            | 1.83 ms                                                                     | 1.82 ms: 1.01x faster                                                                 |
| bench_thread_pool       | 818 us                                                                      | 813 us: 1.01x faster                                                                  |
| json_loads              | 13.4 us                                                                     | 13.3 us: 1.01x faster                                                                 |
| 2to3                    | 194 ms                                                                      | 194 ms: 1.00x faster                                                                  |
| python_startup          | 18.2 ms                                                                     | 18.1 ms: 1.00x faster                                                                 |
| pickle_pure_python      | 168 us                                                                      | 168 us: 1.00x faster                                                                  |
| xml_etree_generate      | 50.0 ms                                                                     | 50.2 ms: 1.00x slower                                                                 |
| logging_format          | 6.41 us                                                                     | 6.44 us: 1.00x slower                                                                 |
| async_generators        | 202 ms                                                                      | 203 ms: 1.00x slower                                                                  |
| pyflate                 | 271 ms                                                                      | 273 ms: 1.01x slower                                                                  |
| pprint_pformat          | 902 ms                                                                      | 909 ms: 1.01x slower                                                                  |
| unpickle_list           | 2.70 us                                                                     | 2.72 us: 1.01x slower                                                                 |
| pathlib                 | 82.2 ms                                                                     | 82.9 ms: 1.01x slower                                                                 |
| unpickle_pure_python    | 117 us                                                                      | 118 us: 1.01x slower                                                                  |
| django_template         | 19.9 ms                                                                     | 20.1 ms: 1.01x slower                                                                 |
| thrift                  | 459 us                                                                      | 464 us: 1.01x slower                                                                  |
| xml_etree_process       | 33.9 ms                                                                     | 34.3 ms: 1.01x slower                                                                 |
| unpickle                | 7.96 us                                                                     | 8.06 us: 1.01x slower                                                                 |
| json                    | 2.71 ms                                                                     | 2.75 ms: 1.02x slower                                                                 |
| xml_etree_parse         | 87.3 ms                                                                     | 88.7 ms: 1.02x slower                                                                 |
| nqueens                 | 54.1 ms                                                                     | 55.1 ms: 1.02x slower                                                                 |
| xml_etree_iterparse     | 59.2 ms                                                                     | 60.4 ms: 1.02x slower                                                                 |
| pprint_safe_repr        | 443 ms                                                                      | 452 ms: 1.02x slower                                                                  |
| scimark_lu              | 50.5 ms                                                                     | 51.6 ms: 1.02x slower                                                                 |
| coroutines              | 13.9 ms                                                                     | 14.3 ms: 1.03x slower                                                                 |
| logging_simple          | 5.91 us                                                                     | 6.07 us: 1.03x slower                                                                 |
| pickle                  | 6.65 us                                                                     | 7.12 us: 1.07x slower                                                                 |
| fannkuch                | 222 ms                                                                      | 238 ms: 1.07x slower                                                                  |
| Geometric mean          | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (16): asyncio_tcp, unpack_sequence, dask, async_tree_cpu_io_mixed, sqlite_synth, pycparser, pickle_dict, async_tree_memoization, mako, json_dumps, telco, python_startup_no_site, chameleon, async_tree_none, pickle_list, async_tree_io
