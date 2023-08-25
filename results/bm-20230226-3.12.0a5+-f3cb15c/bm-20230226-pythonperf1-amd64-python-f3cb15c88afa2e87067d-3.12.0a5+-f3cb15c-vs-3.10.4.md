
# Results vs. 3.10.4

- fork: python
- ref: f3cb15c88afa2e87067d
- machine: windows-amd64
- commit hash: f3cb15c
- commit date: 2023-02-26
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 200 ms: 1.18x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.45 ms: 1.33x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.1 ms: 1.33x faster                                                       |
| tornado_http   | 109 ms                                                      | 89.4 ms: 1.22x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 48.0 ms: 1.26x faster                                                       |
| nbody          | 69.3 ms                                                     | 58.7 ms: 1.18x faster                                                       |
| pidigits       | 145 ms                                                      | 149 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 81.3 ms: 1.27x faster                                                       |
| regex_dna      | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.38 ms: 1.58x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 167 us: 1.54x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 118 us: 1.45x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 34.6 ms: 1.26x faster                                                       |
| unpickle             | 9.17 us                                                     | 7.86 us: 1.17x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 92.2 ms: 1.10x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 52.9 ms: 1.03x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.73 us: 1.03x faster                                                       |
| pickle               | 6.80 us                                                     | 6.89 us: 1.01x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.22 ms: 1.41x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.7 ms: 1.39x faster                                                       |
| django_template | 28.2 ms                                                     | 20.8 ms: 1.36x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.8 ms: 1.31x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.37x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.94 ms: 2.15x faster                                                       |
| richards                | 41.2 ms                                                     | 23.2 ms: 1.78x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 54.5 ns: 1.77x faster                                                       |
| scimark_sor             | 105 ms                                                      | 61.6 ms: 1.70x faster                                                       |
| mypy2                   | 352 ms                                                      | 215 ms: 1.64x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.38 ms: 1.58x faster                                                       |
| raytrace                | 271 ms                                                      | 173 ms: 1.56x faster                                                        |
| go                      | 136 ms                                                      | 87.5 ms: 1.56x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 167 us: 1.54x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 57.4 ms: 1.49x faster                                                       |
| generators              | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 831 us: 1.47x faster                                                        |
| asyncio_tcp             | 712 ms                                                      | 486 ms: 1.47x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 118 us: 1.45x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 26.2 ns: 1.44x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.84 ms: 1.44x faster                                                       |
| pyflate                 | 387 ms                                                      | 270 ms: 1.43x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 20.0 us: 1.43x faster                                                       |
| chaos                   | 58.9 ms                                                     | 41.3 ms: 1.42x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.22 ms: 1.41x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 44.4 ms: 1.40x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.04 ms: 1.40x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 356 ms: 1.40x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 764 ms: 1.39x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 13.7 ms: 1.39x faster                                                       |
| async_tree_none         | 420 ms                                                      | 308 ms: 1.36x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.0 ms: 1.36x faster                                                       |
| django_template         | 28.2 ms                                                     | 20.8 ms: 1.36x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 58.4 ms: 1.34x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.45 ms: 1.33x faster                                                       |
| thrift                  | 615 us                                                      | 464 us: 1.33x faster                                                        |
| html5lib                | 46.5 ms                                                     | 35.1 ms: 1.33x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 30.8 ms: 1.31x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 938 ms: 1.29x faster                                                        |
| pycparser               | 868 ms                                                      | 677 ms: 1.28x faster                                                        |
| regex_compile           | 103 ms                                                      | 81.3 ms: 1.27x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 464 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 484 ms: 1.26x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 34.6 ms: 1.26x faster                                                       |
| float                   | 60.2 ms                                                     | 48.0 ms: 1.26x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 31.5 ms: 1.24x faster                                                       |
| deepcopy                | 255 us                                                      | 208 us: 1.23x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| tornado_http            | 109 ms                                                      | 89.4 ms: 1.22x faster                                                       |
| scimark_fft             | 193 ms                                                      | 162 ms: 1.19x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.81 us: 1.19x faster                                                       |
| fannkuch                | 258 ms                                                      | 216 ms: 1.19x faster                                                        |
| 2to3                    | 237 ms                                                      | 200 ms: 1.18x faster                                                        |
| nbody                   | 69.3 ms                                                     | 58.7 ms: 1.18x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 171 ms: 1.18x faster                                                        |
| sympy_expand            | 315 ms                                                      | 269 ms: 1.17x faster                                                        |
| unpickle                | 9.17 us                                                     | 7.86 us: 1.17x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.47 sec: 1.16x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 12.8 ms: 1.16x faster                                                       |
| coroutines              | 15.9 ms                                                     | 13.9 ms: 1.14x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 58.6 ms: 1.14x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 41.9 ms: 1.14x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 696 us: 1.12x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.38 ms: 1.12x faster                                                       |
| regex_dna               | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 852 us: 1.11x faster                                                        |
| json_loads              | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 92.2 ms: 1.10x faster                                                       |
| json                    | 3.05 ms                                                     | 2.79 ms: 1.09x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| sympy_sum               | 104 ms                                                      | 96.9 ms: 1.07x faster                                                       |
| sympy_str               | 188 ms                                                      | 176 ms: 1.07x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 73.4 ms: 1.05x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.2 us: 1.05x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.37 us: 1.05x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 52.9 ms: 1.03x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.73 us: 1.03x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 70.6 ms: 1.03x faster                                                       |
| async_generators        | 224 ms                                                      | 220 ms: 1.02x faster                                                        |
| logging_simple          | 6.20 us                                                     | 6.11 us: 1.01x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.86 us: 1.01x slower                                                       |
| pickle                  | 6.80 us                                                     | 6.89 us: 1.01x slower                                                       |
| telco                   | 3.78 ms                                                     | 3.85 ms: 1.02x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 149 ms: 1.03x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 65.8 ms: 1.08x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                                       |
| dask                    | 305 ms                                                      | 353 ms: 1.16x slower                                                        |
| coverage                | 40.0 ms                                                     | 51.0 ms: 1.28x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
