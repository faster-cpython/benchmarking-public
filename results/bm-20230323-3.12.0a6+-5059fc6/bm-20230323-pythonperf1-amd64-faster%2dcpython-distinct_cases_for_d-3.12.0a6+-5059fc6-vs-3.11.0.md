
# Results vs. 3.11.0

- fork: faster-cpython
- ref: distinct_cases_for_d
- machine: windows-amd64
- commit hash: 5059fc6
- commit date: 2023-03-23
- overall geometric mean: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 194 ms: 1.05x faster                                                                  |
| chameleon      | 5.15 ms                                                                  | 4.31 ms: 1.20x faster                                                                 |
| docutils       | 1.59 sec                                                                 | 1.49 sec: 1.07x faster                                                                |
| html5lib       | 38.5 ms                                                                  | 34.9 ms: 1.10x faster                                                                 |
| tornado_http   | 91.8 ms                                                                  | 84.1 ms: 1.09x faster                                                                 |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 51.1 ms: 1.39x faster                                                                 |
| float          | 53.3 ms                                                                  | 45.6 ms: 1.17x faster                                                                 |
| pidigits       | 147 ms                                                                   | 144 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.18x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 78.3 ms: 1.15x faster                                                                 |
| regex_v8       | 13.5 ms                                                                  | 13.5 ms: 1.00x slower                                                                 |
| regex_dna      | 115 ms                                                                   | 118 ms: 1.03x slower                                                                  |
| regex_effbot   | 1.63 ms                                                                  | 1.82 ms: 1.12x slower                                                                 |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.44 ms: 1.42x faster                                                                 |
| unpickle_pure_python | 150 us                                                                   | 118 us: 1.27x faster                                                                  |
| pickle_pure_python   | 203 us                                                                   | 168 us: 1.21x faster                                                                  |
| xml_etree_process    | 36.6 ms                                                                  | 34.3 ms: 1.07x faster                                                                 |
| xml_etree_generate   | 52.3 ms                                                                  | 50.2 ms: 1.04x faster                                                                 |
| xml_etree_parse      | 92.1 ms                                                                  | 88.7 ms: 1.04x faster                                                                 |
| unpickle_list        | 2.80 us                                                                  | 2.72 us: 1.03x faster                                                                 |
| xml_etree_iterparse  | 61.8 ms                                                                  | 60.4 ms: 1.02x faster                                                                 |
| json_loads           | 13.5 us                                                                  | 13.3 us: 1.02x faster                                                                 |
| pickle_dict          | 18.6 us                                                                  | 18.5 us: 1.00x faster                                                                 |
| unpickle             | 8.01 us                                                                  | 8.06 us: 1.01x slower                                                                 |
| pickle_list          | 2.70 us                                                                  | 2.80 us: 1.04x slower                                                                 |
| pickle               | 6.47 us                                                                  | 7.12 us: 1.10x slower                                                                 |
| Geometric mean       | (ref)                                                                    | 1.07x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup | 18.4 ms                                                                  | 18.1 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 13.1 ms: 1.32x faster                                                                 |
| genshi_xml      | 38.0 ms                                                                  | 29.5 ms: 1.29x faster                                                                 |
| django_template | 23.9 ms                                                                  | 20.1 ms: 1.19x faster                                                                 |
| mako            | 7.20 ms                                                                  | 6.10 ms: 1.18x faster                                                                 |
| Geometric mean  | (ref)                                                                    | 1.24x faster                                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 20.7 ms: 1.62x faster                                                                 |
| unpack_sequence         | 43.1 ns                                                                  | 27.2 ns: 1.58x faster                                                                 |
| deltablue               | 2.68 ms                                                                  | 1.82 ms: 1.47x faster                                                                 |
| asyncio_tcp             | 674 ms                                                                   | 465 ms: 1.45x faster                                                                  |
| json_dumps              | 7.71 ms                                                                  | 5.44 ms: 1.42x faster                                                                 |
| nbody                   | 70.9 ms                                                                  | 51.1 ms: 1.39x faster                                                                 |
| richards                | 32.1 ms                                                                  | 23.5 ms: 1.37x faster                                                                 |
| mypy2                   | 276 ms                                                                   | 202 ms: 1.37x faster                                                                  |
| deepcopy_memo           | 25.3 us                                                                  | 19.0 us: 1.33x faster                                                                 |
| logging_silent          | 71.0 ns                                                                  | 53.8 ns: 1.32x faster                                                                 |
| genshi_text             | 17.3 ms                                                                  | 13.1 ms: 1.32x faster                                                                 |
| genshi_xml              | 38.0 ms                                                                  | 29.5 ms: 1.29x faster                                                                 |
| raytrace                | 206 ms                                                                   | 162 ms: 1.27x faster                                                                  |
| unpickle_pure_python    | 150 us                                                                   | 118 us: 1.27x faster                                                                  |
| mdp                     | 1.67 sec                                                                 | 1.33 sec: 1.26x faster                                                                |
| hexiom                  | 4.46 ms                                                                  | 3.59 ms: 1.24x faster                                                                 |
| chaos                   | 47.3 ms                                                                  | 38.4 ms: 1.23x faster                                                                 |
| go                      | 97.5 ms                                                                  | 79.4 ms: 1.23x faster                                                                 |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.16 ms: 1.22x faster                                                                 |
| scimark_lu              | 62.8 ms                                                                  | 51.6 ms: 1.22x faster                                                                 |
| scimark_monte_carlo     | 45.8 ms                                                                  | 37.7 ms: 1.21x faster                                                                 |
| pickle_pure_python      | 203 us                                                                   | 168 us: 1.21x faster                                                                  |
| deepcopy                | 240 us                                                                   | 198 us: 1.21x faster                                                                  |
| spectral_norm           | 71.8 ms                                                                  | 59.4 ms: 1.21x faster                                                                 |
| chameleon               | 5.15 ms                                                                  | 4.31 ms: 1.20x faster                                                                 |
| django_template         | 23.9 ms                                                                  | 20.1 ms: 1.19x faster                                                                 |
| nqueens                 | 65.1 ms                                                                  | 55.1 ms: 1.18x faster                                                                 |
| mako                    | 7.20 ms                                                                  | 6.10 ms: 1.18x faster                                                                 |
| scimark_fft             | 183 ms                                                                   | 156 ms: 1.17x faster                                                                  |
| float                   | 53.3 ms                                                                  | 45.6 ms: 1.17x faster                                                                 |
| json                    | 3.20 ms                                                                  | 2.75 ms: 1.17x faster                                                                 |
| pprint_pformat          | 1.05 sec                                                                 | 909 ms: 1.15x faster                                                                  |
| sqlglot_normalize       | 189 ms                                                                   | 164 ms: 1.15x faster                                                                  |
| deepcopy_reduce         | 2.06 us                                                                  | 1.79 us: 1.15x faster                                                                 |
| sqlglot_optimize        | 34.5 ms                                                                  | 30.1 ms: 1.15x faster                                                                 |
| regex_compile           | 89.7 ms                                                                  | 78.3 ms: 1.15x faster                                                                 |
| pprint_safe_repr        | 512 ms                                                                   | 452 ms: 1.13x faster                                                                  |
| coverage                | 55.3 ms                                                                  | 49.2 ms: 1.13x faster                                                                 |
| scimark_sor             | 77.7 ms                                                                  | 69.1 ms: 1.12x faster                                                                 |
| sympy_expand            | 298 ms                                                                   | 266 ms: 1.12x faster                                                                  |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.01 ms: 1.12x faster                                                                 |
| sqlglot_parse           | 929 us                                                                   | 829 us: 1.12x faster                                                                  |
| logging_format          | 7.13 us                                                                  | 6.44 us: 1.11x faster                                                                 |
| pyflate                 | 302 ms                                                                   | 273 ms: 1.11x faster                                                                  |
| crypto_pyaes            | 48.3 ms                                                                  | 43.6 ms: 1.11x faster                                                                 |
| sympy_str               | 184 ms                                                                   | 166 ms: 1.11x faster                                                                  |
| sympy_integrate         | 13.7 ms                                                                  | 12.4 ms: 1.10x faster                                                                 |
| html5lib                | 38.5 ms                                                                  | 34.9 ms: 1.10x faster                                                                 |
| tornado_http            | 91.8 ms                                                                  | 84.1 ms: 1.09x faster                                                                 |
| meteor_contest          | 74.4 ms                                                                  | 68.3 ms: 1.09x faster                                                                 |
| logging_simple          | 6.60 us                                                                  | 6.07 us: 1.09x faster                                                                 |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 473 ms: 1.08x faster                                                                  |
| docutils                | 1.59 sec                                                                 | 1.49 sec: 1.07x faster                                                                |
| fannkuch                | 255 ms                                                                   | 238 ms: 1.07x faster                                                                  |
| pycparser               | 686 ms                                                                   | 640 ms: 1.07x faster                                                                  |
| async_tree_memoization  | 374 ms                                                                   | 349 ms: 1.07x faster                                                                  |
| sympy_sum               | 98.9 ms                                                                  | 92.3 ms: 1.07x faster                                                                 |
| dulwich_log             | 43.4 ms                                                                  | 40.7 ms: 1.07x faster                                                                 |
| xml_etree_process       | 36.6 ms                                                                  | 34.3 ms: 1.07x faster                                                                 |
| async_tree_none         | 313 ms                                                                   | 297 ms: 1.06x faster                                                                  |
| comprehensions          | 15.4 us                                                                  | 14.6 us: 1.05x faster                                                                 |
| 2to3                    | 204 ms                                                                   | 194 ms: 1.05x faster                                                                  |
| bench_thread_pool       | 856 us                                                                   | 813 us: 1.05x faster                                                                  |
| thrift                  | 487 us                                                                   | 464 us: 1.05x faster                                                                  |
| xml_etree_generate      | 52.3 ms                                                                  | 50.2 ms: 1.04x faster                                                                 |
| xml_etree_parse         | 92.1 ms                                                                  | 88.7 ms: 1.04x faster                                                                 |
| coroutines              | 14.8 ms                                                                  | 14.3 ms: 1.04x faster                                                                 |
| unpickle_list           | 2.80 us                                                                  | 2.72 us: 1.03x faster                                                                 |
| xml_etree_iterparse     | 61.8 ms                                                                  | 60.4 ms: 1.02x faster                                                                 |
| telco                   | 3.93 ms                                                                  | 3.85 ms: 1.02x faster                                                                 |
| async_tree_io           | 744 ms                                                                   | 731 ms: 1.02x faster                                                                  |
| json_loads              | 13.5 us                                                                  | 13.3 us: 1.02x faster                                                                 |
| pidigits                | 147 ms                                                                   | 144 ms: 1.02x faster                                                                  |
| python_startup          | 18.4 ms                                                                  | 18.1 ms: 1.01x faster                                                                 |
| pickle_dict             | 18.6 us                                                                  | 18.5 us: 1.00x faster                                                                 |
| regex_v8                | 13.5 ms                                                                  | 13.5 ms: 1.00x slower                                                                 |
| unpickle                | 8.01 us                                                                  | 8.06 us: 1.01x slower                                                                 |
| regex_dna               | 115 ms                                                                   | 118 ms: 1.03x slower                                                                  |
| gc_traversal            | 1.40 ms                                                                  | 1.44 ms: 1.03x slower                                                                 |
| pickle_list             | 2.70 us                                                                  | 2.80 us: 1.04x slower                                                                 |
| create_gc_cycles        | 666 us                                                                   | 693 us: 1.04x slower                                                                  |
| bench_mp_pool           | 61.2 ms                                                                  | 64.0 ms: 1.05x slower                                                                 |
| sqlite_synth            | 1.67 us                                                                  | 1.76 us: 1.05x slower                                                                 |
| pickle                  | 6.47 us                                                                  | 7.12 us: 1.10x slower                                                                 |
| regex_effbot            | 1.63 ms                                                                  | 1.82 ms: 1.12x slower                                                                 |
| async_generators        | 180 ms                                                                   | 203 ms: 1.13x slower                                                                  |
| pathlib                 | 72.9 ms                                                                  | 82.9 ms: 1.14x slower                                                                 |
| dask                    | 267 ms                                                                   | 352 ms: 1.32x slower                                                                  |
| Geometric mean          | (ref)                                                                    | 1.12x faster                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
