
# Results vs. 3.10.4

- fork: faster-cpython
- ref: distinct_cases_for_d
- machine: windows-amd64
- commit hash: 5059fc6
- commit date: 2023-03-23
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 194 ms: 1.19x faster                                                                  |
| chameleon      | 5.77 ms                                                                  | 4.31 ms: 1.34x faster                                                                 |
| docutils       | 1.83 sec                                                                 | 1.49 sec: 1.23x faster                                                                |
| html5lib       | 47.3 ms                                                                  | 34.9 ms: 1.36x faster                                                                 |
| tornado_http   | 106 ms                                                                   | 84.1 ms: 1.27x faster                                                                 |
| Geometric mean | (ref)                                                                    | 1.27x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 71.5 ms                                                                  | 51.1 ms: 1.40x faster                                                                 |
| float          | 59.5 ms                                                                  | 45.6 ms: 1.31x faster                                                                 |
| pidigits       | 145 ms                                                                   | 144 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.22x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 78.3 ms: 1.32x faster                                                                 |
| regex_v8       | 15.1 ms                                                                  | 13.5 ms: 1.11x faster                                                                 |
| regex_dna      | 131 ms                                                                   | 118 ms: 1.11x faster                                                                  |
| regex_effbot   | 1.64 ms                                                                  | 1.82 ms: 1.11x slower                                                                 |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.44 ms: 1.65x faster                                                                 |
| pickle_pure_python   | 264 us                                                                   | 168 us: 1.57x faster                                                                  |
| unpickle_pure_python | 179 us                                                                   | 118 us: 1.52x faster                                                                  |
| xml_etree_process    | 43.0 ms                                                                  | 34.3 ms: 1.25x faster                                                                 |
| unpickle             | 8.88 us                                                                  | 8.06 us: 1.10x faster                                                                 |
| xml_etree_parse      | 95.6 ms                                                                  | 88.7 ms: 1.08x faster                                                                 |
| xml_etree_generate   | 53.8 ms                                                                  | 50.2 ms: 1.07x faster                                                                 |
| json_loads           | 14.2 us                                                                  | 13.3 us: 1.06x faster                                                                 |
| xml_etree_iterparse  | 62.5 ms                                                                  | 60.4 ms: 1.04x faster                                                                 |
| pickle               | 6.67 us                                                                  | 7.12 us: 1.07x slower                                                                 |
| pickle_list          | 2.57 us                                                                  | 2.80 us: 1.09x slower                                                                 |
| pickle_dict          | 16.7 us                                                                  | 18.5 us: 1.11x slower                                                                 |
| Geometric mean       | (ref)                                                                    | 1.14x faster                                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.1 ms: 1.06x faster                                                                 |
| python_startup_no_site | 14.8 ms                                                                  | 15.4 ms: 1.03x slower                                                                 |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 29.2 ms                                                                  | 20.1 ms: 1.45x faster                                                                 |
| mako            | 8.69 ms                                                                  | 6.10 ms: 1.43x faster                                                                 |
| genshi_text     | 18.5 ms                                                                  | 13.1 ms: 1.41x faster                                                                 |
| genshi_xml      | 38.8 ms                                                                  | 29.5 ms: 1.32x faster                                                                 |
| Geometric mean  | (ref)                                                                    | 1.40x faster                                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 1.82 ms: 2.28x faster                                                                 |
| go                      | 143 ms                                                                   | 79.4 ms: 1.80x faster                                                                 |
| logging_silent          | 94.6 ns                                                                  | 53.8 ns: 1.76x faster                                                                 |
| richards                | 41.0 ms                                                                  | 23.5 ms: 1.75x faster                                                                 |
| mypy2                   | 337 ms                                                                   | 202 ms: 1.67x faster                                                                  |
| json_dumps              | 9.00 ms                                                                  | 5.44 ms: 1.65x faster                                                                 |
| raytrace                | 267 ms                                                                   | 162 ms: 1.65x faster                                                                  |
| scimark_lu              | 83.9 ms                                                                  | 51.6 ms: 1.63x faster                                                                 |
| pickle_pure_python      | 264 us                                                                   | 168 us: 1.57x faster                                                                  |
| hexiom                  | 5.45 ms                                                                  | 3.59 ms: 1.52x faster                                                                 |
| unpickle_pure_python    | 179 us                                                                   | 118 us: 1.52x faster                                                                  |
| chaos                   | 58.4 ms                                                                  | 38.4 ms: 1.52x faster                                                                 |
| generators              | 31.4 ms                                                                  | 20.7 ms: 1.52x faster                                                                 |
| scimark_sor             | 104 ms                                                                   | 69.1 ms: 1.50x faster                                                                 |
| deepcopy_memo           | 28.4 us                                                                  | 19.0 us: 1.49x faster                                                                 |
| scimark_monte_carlo     | 56.0 ms                                                                  | 37.7 ms: 1.49x faster                                                                 |
| sqlglot_parse           | 1.22 ms                                                                  | 829 us: 1.47x faster                                                                  |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.01 ms: 1.46x faster                                                                 |
| django_template         | 29.2 ms                                                                  | 20.1 ms: 1.45x faster                                                                 |
| unpack_sequence         | 39.4 ns                                                                  | 27.2 ns: 1.45x faster                                                                 |
| asyncio_tcp             | 664 ms                                                                   | 465 ms: 1.43x faster                                                                  |
| mako                    | 8.69 ms                                                                  | 6.10 ms: 1.43x faster                                                                 |
| pyflate                 | 388 ms                                                                   | 273 ms: 1.42x faster                                                                  |
| genshi_text             | 18.5 ms                                                                  | 13.1 ms: 1.41x faster                                                                 |
| crypto_pyaes            | 61.4 ms                                                                  | 43.6 ms: 1.41x faster                                                                 |
| async_tree_io           | 1.02 sec                                                                 | 731 ms: 1.40x faster                                                                  |
| nbody                   | 71.5 ms                                                                  | 51.1 ms: 1.40x faster                                                                 |
| async_tree_none         | 414 ms                                                                   | 297 ms: 1.40x faster                                                                  |
| async_tree_memoization  | 485 ms                                                                   | 349 ms: 1.39x faster                                                                  |
| pycparser               | 873 ms                                                                   | 640 ms: 1.37x faster                                                                  |
| thrift                  | 632 us                                                                   | 464 us: 1.36x faster                                                                  |
| html5lib                | 47.3 ms                                                                  | 34.9 ms: 1.36x faster                                                                 |
| pprint_pformat          | 1.23 sec                                                                 | 909 ms: 1.35x faster                                                                  |
| chameleon               | 5.77 ms                                                                  | 4.31 ms: 1.34x faster                                                                 |
| regex_compile           | 103 ms                                                                   | 78.3 ms: 1.32x faster                                                                 |
| genshi_xml              | 38.8 ms                                                                  | 29.5 ms: 1.32x faster                                                                 |
| pprint_safe_repr        | 593 ms                                                                   | 452 ms: 1.31x faster                                                                  |
| float                   | 59.5 ms                                                                  | 45.6 ms: 1.31x faster                                                                 |
| deepcopy                | 256 us                                                                   | 198 us: 1.29x faster                                                                  |
| sqlglot_optimize        | 38.7 ms                                                                  | 30.1 ms: 1.29x faster                                                                 |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 473 ms: 1.28x faster                                                                  |
| tornado_http            | 106 ms                                                                   | 84.1 ms: 1.27x faster                                                                 |
| xml_etree_process       | 43.0 ms                                                                  | 34.3 ms: 1.25x faster                                                                 |
| spectral_norm           | 74.3 ms                                                                  | 59.4 ms: 1.25x faster                                                                 |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.16 ms: 1.24x faster                                                                 |
| docutils                | 1.83 sec                                                                 | 1.49 sec: 1.23x faster                                                                |
| sqlglot_normalize       | 201 ms                                                                   | 164 ms: 1.23x faster                                                                  |
| deepcopy_reduce         | 2.18 us                                                                  | 1.79 us: 1.22x faster                                                                 |
| mdp                     | 1.60 sec                                                                 | 1.33 sec: 1.21x faster                                                                |
| scimark_fft             | 187 ms                                                                   | 156 ms: 1.20x faster                                                                  |
| 2to3                    | 229 ms                                                                   | 194 ms: 1.19x faster                                                                  |
| sympy_integrate         | 14.7 ms                                                                  | 12.4 ms: 1.18x faster                                                                 |
| nqueens                 | 64.8 ms                                                                  | 55.1 ms: 1.18x faster                                                                 |
| sympy_expand            | 313 ms                                                                   | 266 ms: 1.18x faster                                                                  |
| bench_thread_pool       | 953 us                                                                   | 813 us: 1.17x faster                                                                  |
| json                    | 3.18 ms                                                                  | 2.75 ms: 1.16x faster                                                                 |
| dulwich_log             | 47.0 ms                                                                  | 40.7 ms: 1.15x faster                                                                 |
| sympy_str               | 189 ms                                                                   | 166 ms: 1.13x faster                                                                  |
| regex_v8                | 15.1 ms                                                                  | 13.5 ms: 1.11x faster                                                                 |
| regex_dna               | 131 ms                                                                   | 118 ms: 1.11x faster                                                                  |
| sympy_sum               | 102 ms                                                                   | 92.3 ms: 1.11x faster                                                                 |
| create_gc_cycles        | 764 us                                                                   | 693 us: 1.10x faster                                                                  |
| unpickle                | 8.88 us                                                                  | 8.06 us: 1.10x faster                                                                 |
| comprehensions          | 16.0 us                                                                  | 14.6 us: 1.10x faster                                                                 |
| coroutines              | 15.6 ms                                                                  | 14.3 ms: 1.09x faster                                                                 |
| meteor_contest          | 74.3 ms                                                                  | 68.3 ms: 1.09x faster                                                                 |
| xml_etree_parse         | 95.6 ms                                                                  | 88.7 ms: 1.08x faster                                                                 |
| xml_etree_generate      | 53.8 ms                                                                  | 50.2 ms: 1.07x faster                                                                 |
| json_loads              | 14.2 us                                                                  | 13.3 us: 1.06x faster                                                                 |
| python_startup          | 19.3 ms                                                                  | 18.1 ms: 1.06x faster                                                                 |
| fannkuch                | 252 ms                                                                   | 238 ms: 1.06x faster                                                                  |
| async_generators        | 214 ms                                                                   | 203 ms: 1.06x faster                                                                  |
| sqlite_synth            | 1.85 us                                                                  | 1.76 us: 1.05x faster                                                                 |
| xml_etree_iterparse     | 62.5 ms                                                                  | 60.4 ms: 1.04x faster                                                                 |
| logging_format          | 6.53 us                                                                  | 6.44 us: 1.01x faster                                                                 |
| logging_simple          | 6.12 us                                                                  | 6.07 us: 1.01x faster                                                                 |
| pidigits                | 145 ms                                                                   | 144 ms: 1.01x faster                                                                  |
| telco                   | 3.77 ms                                                                  | 3.85 ms: 1.02x slower                                                                 |
| python_startup_no_site  | 14.8 ms                                                                  | 15.4 ms: 1.03x slower                                                                 |
| pickle                  | 6.67 us                                                                  | 7.12 us: 1.07x slower                                                                 |
| bench_mp_pool           | 59.2 ms                                                                  | 64.0 ms: 1.08x slower                                                                 |
| gc_traversal            | 1.33 ms                                                                  | 1.44 ms: 1.08x slower                                                                 |
| pickle_list             | 2.57 us                                                                  | 2.80 us: 1.09x slower                                                                 |
| pathlib                 | 75.2 ms                                                                  | 82.9 ms: 1.10x slower                                                                 |
| regex_effbot            | 1.64 ms                                                                  | 1.82 ms: 1.11x slower                                                                 |
| pickle_dict             | 16.7 us                                                                  | 18.5 us: 1.11x slower                                                                 |
| dask                    | 310 ms                                                                   | 352 ms: 1.13x slower                                                                  |
| coverage                | 37.5 ms                                                                  | 49.2 ms: 1.31x slower                                                                 |
| Geometric mean          | (ref)                                                                    | 1.24x faster                                                                          |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
