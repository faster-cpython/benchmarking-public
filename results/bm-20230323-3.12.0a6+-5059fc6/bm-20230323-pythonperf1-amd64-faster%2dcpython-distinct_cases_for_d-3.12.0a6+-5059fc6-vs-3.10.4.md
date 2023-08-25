
# Results vs. 3.10.4

- fork: faster-cpython
- ref: distinct_cases_for_d
- machine: windows-amd64
- commit hash: 5059fc6
- commit date: 2023-03-23
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 194 ms: 1.22x faster                                                                  |
| chameleon      | 5.92 ms                                                     | 4.31 ms: 1.37x faster                                                                 |
| docutils       | 1.89 sec                                                    | 1.49 sec: 1.27x faster                                                                |
| html5lib       | 46.5 ms                                                     | 34.9 ms: 1.33x faster                                                                 |
| tornado_http   | 109 ms                                                      | 84.1 ms: 1.30x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.30x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 69.3 ms                                                     | 51.1 ms: 1.36x faster                                                                 |
| float          | 60.2 ms                                                     | 45.6 ms: 1.32x faster                                                                 |
| pidigits       | 145 ms                                                      | 144 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 78.3 ms: 1.32x faster                                                                 |
| regex_dna      | 132 ms                                                      | 118 ms: 1.12x faster                                                                  |
| regex_v8       | 15.0 ms                                                     | 13.5 ms: 1.11x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.82 ms: 1.09x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.44 ms: 1.56x faster                                                                 |
| pickle_pure_python   | 257 us                                                      | 168 us: 1.53x faster                                                                  |
| unpickle_pure_python | 171 us                                                      | 118 us: 1.45x faster                                                                  |
| xml_etree_process    | 43.4 ms                                                     | 34.3 ms: 1.27x faster                                                                 |
| xml_etree_parse      | 102 ms                                                      | 88.7 ms: 1.15x faster                                                                 |
| unpickle             | 9.17 us                                                     | 8.06 us: 1.14x faster                                                                 |
| xml_etree_generate   | 54.5 ms                                                     | 50.2 ms: 1.09x faster                                                                 |
| json_loads           | 14.2 us                                                     | 13.3 us: 1.06x faster                                                                 |
| xml_etree_iterparse  | 63.5 ms                                                     | 60.4 ms: 1.05x faster                                                                 |
| unpickle_list        | 2.81 us                                                     | 2.72 us: 1.03x faster                                                                 |
| pickle               | 6.80 us                                                     | 7.12 us: 1.05x slower                                                                 |
| pickle_list          | 2.59 us                                                     | 2.80 us: 1.08x slower                                                                 |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.10x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.1 ms: 1.10x faster                                                                 |
| python_startup_no_site | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                                 |
| Geometric mean         | (ref)                                                       | 1.06x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 19.0 ms                                                     | 13.1 ms: 1.45x faster                                                                 |
| mako            | 8.80 ms                                                     | 6.10 ms: 1.44x faster                                                                 |
| django_template | 28.2 ms                                                     | 20.1 ms: 1.40x faster                                                                 |
| genshi_xml      | 40.5 ms                                                     | 29.5 ms: 1.38x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.42x faster                                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-distinct_cases_for_d-3.12.0a6+-5059fc6 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.82 ms: 2.29x faster                                                                 |
| logging_silent          | 96.4 ns                                                     | 53.8 ns: 1.79x faster                                                                 |
| richards                | 41.2 ms                                                     | 23.5 ms: 1.75x faster                                                                 |
| mypy2                   | 352 ms                                                      | 202 ms: 1.74x faster                                                                  |
| go                      | 136 ms                                                      | 79.4 ms: 1.71x faster                                                                 |
| raytrace                | 271 ms                                                      | 162 ms: 1.67x faster                                                                  |
| scimark_lu              | 85.4 ms                                                     | 51.6 ms: 1.66x faster                                                                 |
| json_dumps              | 8.50 ms                                                     | 5.44 ms: 1.56x faster                                                                 |
| hexiom                  | 5.52 ms                                                     | 3.59 ms: 1.54x faster                                                                 |
| asyncio_tcp             | 712 ms                                                      | 465 ms: 1.53x faster                                                                  |
| chaos                   | 58.9 ms                                                     | 38.4 ms: 1.53x faster                                                                 |
| pickle_pure_python      | 257 us                                                      | 168 us: 1.53x faster                                                                  |
| generators              | 31.6 ms                                                     | 20.7 ms: 1.52x faster                                                                 |
| scimark_sor             | 105 ms                                                      | 69.1 ms: 1.52x faster                                                                 |
| deepcopy_memo           | 28.5 us                                                     | 19.0 us: 1.50x faster                                                                 |
| scimark_monte_carlo     | 55.9 ms                                                     | 37.7 ms: 1.48x faster                                                                 |
| sqlglot_parse           | 1.22 ms                                                     | 829 us: 1.47x faster                                                                  |
| async_tree_io           | 1.07 sec                                                    | 731 ms: 1.46x faster                                                                  |
| genshi_text             | 19.0 ms                                                     | 13.1 ms: 1.45x faster                                                                 |
| unpickle_pure_python    | 171 us                                                      | 118 us: 1.45x faster                                                                  |
| sqlglot_transpile       | 1.46 ms                                                     | 1.01 ms: 1.45x faster                                                                 |
| mako                    | 8.80 ms                                                     | 6.10 ms: 1.44x faster                                                                 |
| crypto_pyaes            | 62.3 ms                                                     | 43.6 ms: 1.43x faster                                                                 |
| async_tree_memoization  | 497 ms                                                      | 349 ms: 1.43x faster                                                                  |
| pyflate                 | 387 ms                                                      | 273 ms: 1.42x faster                                                                  |
| async_tree_none         | 420 ms                                                      | 297 ms: 1.42x faster                                                                  |
| django_template         | 28.2 ms                                                     | 20.1 ms: 1.40x faster                                                                 |
| unpack_sequence         | 37.8 ns                                                     | 27.2 ns: 1.39x faster                                                                 |
| genshi_xml              | 40.5 ms                                                     | 29.5 ms: 1.38x faster                                                                 |
| chameleon               | 5.92 ms                                                     | 4.31 ms: 1.37x faster                                                                 |
| nbody                   | 69.3 ms                                                     | 51.1 ms: 1.36x faster                                                                 |
| pycparser               | 868 ms                                                      | 640 ms: 1.36x faster                                                                  |
| html5lib                | 46.5 ms                                                     | 34.9 ms: 1.33x faster                                                                 |
| pprint_pformat          | 1.21 sec                                                    | 909 ms: 1.33x faster                                                                  |
| thrift                  | 615 us                                                      | 464 us: 1.32x faster                                                                  |
| float                   | 60.2 ms                                                     | 45.6 ms: 1.32x faster                                                                 |
| regex_compile           | 103 ms                                                      | 78.3 ms: 1.32x faster                                                                 |
| spectral_norm           | 78.0 ms                                                     | 59.4 ms: 1.31x faster                                                                 |
| pprint_safe_repr        | 589 ms                                                      | 452 ms: 1.30x faster                                                                  |
| tornado_http            | 109 ms                                                      | 84.1 ms: 1.30x faster                                                                 |
| sqlglot_optimize        | 39.0 ms                                                     | 30.1 ms: 1.30x faster                                                                 |
| mdp                     | 1.71 sec                                                    | 1.33 sec: 1.29x faster                                                                |
| async_tree_cpu_io_mixed | 609 ms                                                      | 473 ms: 1.29x faster                                                                  |
| deepcopy                | 255 us                                                      | 198 us: 1.29x faster                                                                  |
| docutils                | 1.89 sec                                                    | 1.49 sec: 1.27x faster                                                                |
| xml_etree_process       | 43.4 ms                                                     | 34.3 ms: 1.27x faster                                                                 |
| scimark_fft             | 193 ms                                                      | 156 ms: 1.24x faster                                                                  |
| sqlglot_normalize       | 202 ms                                                      | 164 ms: 1.24x faster                                                                  |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.16 ms: 1.23x faster                                                                 |
| 2to3                    | 237 ms                                                      | 194 ms: 1.22x faster                                                                  |
| nqueens                 | 67.0 ms                                                     | 55.1 ms: 1.22x faster                                                                 |
| deepcopy_reduce         | 2.16 us                                                     | 1.79 us: 1.21x faster                                                                 |
| sympy_integrate         | 14.8 ms                                                     | 12.4 ms: 1.20x faster                                                                 |
| sympy_expand            | 315 ms                                                      | 266 ms: 1.19x faster                                                                  |
| dulwich_log             | 47.6 ms                                                     | 40.7 ms: 1.17x faster                                                                 |
| bench_thread_pool       | 946 us                                                      | 813 us: 1.16x faster                                                                  |
| xml_etree_parse         | 102 ms                                                      | 88.7 ms: 1.15x faster                                                                 |
| unpickle                | 9.17 us                                                     | 8.06 us: 1.14x faster                                                                 |
| sympy_str               | 188 ms                                                      | 166 ms: 1.13x faster                                                                  |
| sympy_sum               | 104 ms                                                      | 92.3 ms: 1.13x faster                                                                 |
| create_gc_cycles        | 782 us                                                      | 693 us: 1.13x faster                                                                  |
| regex_dna               | 132 ms                                                      | 118 ms: 1.12x faster                                                                  |
| coroutines              | 15.9 ms                                                     | 14.3 ms: 1.12x faster                                                                 |
| regex_v8                | 15.0 ms                                                     | 13.5 ms: 1.11x faster                                                                 |
| json                    | 3.05 ms                                                     | 2.75 ms: 1.11x faster                                                                 |
| python_startup          | 20.0 ms                                                     | 18.1 ms: 1.10x faster                                                                 |
| async_generators        | 224 ms                                                      | 203 ms: 1.10x faster                                                                  |
| comprehensions          | 16.0 us                                                     | 14.6 us: 1.10x faster                                                                 |
| xml_etree_generate      | 54.5 ms                                                     | 50.2 ms: 1.09x faster                                                                 |
| fannkuch                | 258 ms                                                      | 238 ms: 1.08x faster                                                                  |
| json_loads              | 14.2 us                                                     | 13.3 us: 1.06x faster                                                                 |
| meteor_contest          | 72.5 ms                                                     | 68.3 ms: 1.06x faster                                                                 |
| xml_etree_iterparse     | 63.5 ms                                                     | 60.4 ms: 1.05x faster                                                                 |
| sqlite_synth            | 1.84 us                                                     | 1.76 us: 1.04x faster                                                                 |
| logging_format          | 6.66 us                                                     | 6.44 us: 1.04x faster                                                                 |
| unpickle_list           | 2.81 us                                                     | 2.72 us: 1.03x faster                                                                 |
| logging_simple          | 6.20 us                                                     | 6.07 us: 1.02x faster                                                                 |
| python_startup_no_site  | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                                 |
| pidigits                | 145 ms                                                      | 144 ms: 1.01x faster                                                                  |
| telco                   | 3.78 ms                                                     | 3.85 ms: 1.02x slower                                                                 |
| pickle                  | 6.80 us                                                     | 7.12 us: 1.05x slower                                                                 |
| bench_mp_pool           | 60.7 ms                                                     | 64.0 ms: 1.05x slower                                                                 |
| pathlib                 | 77.4 ms                                                     | 82.9 ms: 1.07x slower                                                                 |
| gc_traversal            | 1.34 ms                                                     | 1.44 ms: 1.07x slower                                                                 |
| pickle_list             | 2.59 us                                                     | 2.80 us: 1.08x slower                                                                 |
| regex_effbot            | 1.66 ms                                                     | 1.82 ms: 1.09x slower                                                                 |
| pickle_dict             | 16.9 us                                                     | 18.5 us: 1.10x slower                                                                 |
| dask                    | 305 ms                                                      | 352 ms: 1.15x slower                                                                  |
| coverage                | 40.0 ms                                                     | 49.2 ms: 1.23x slower                                                                 |
| Geometric mean          | (ref)                                                       | 1.25x faster                                                                          |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
