
# Results vs. 3.10.4

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: windows-amd64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 205 ms: 1.16x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.59 ms: 1.29x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.56 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 36.5 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.3 ms: 1.20x faster                                                       |
| nbody          | 69.3 ms                                                     | 66.2 ms: 1.05x faster                                                       |
| pidigits       | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.2 ms: 1.20x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.12x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.21 ms: 1.63x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 181 us: 1.42x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 129 us: 1.32x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.3 ms: 1.23x faster                                                       |
| unpickle             | 9.17 us                                                     | 7.94 us: 1.16x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 89.5 ms: 1.14x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 50.5 ms: 1.08x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.72 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.4 ms: 1.02x faster                                                       |
| pickle               | 6.80 us                                                     | 6.71 us: 1.01x faster                                                       |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.88 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.34 ms: 1.39x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.6 ms: 1.30x faster                                                       |
| django_template | 28.2 ms                                                     | 22.7 ms: 1.24x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 34.4 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.21 ms: 1.88x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 59.0 ns: 1.63x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.21 ms: 1.63x faster                                                       |
| mypy2                   | 352 ms                                                      | 224 ms: 1.57x faster                                                        |
| scimark_sor             | 105 ms                                                      | 66.9 ms: 1.57x faster                                                       |
| go                      | 136 ms                                                      | 87.9 ms: 1.55x faster                                                       |
| raytrace                | 271 ms                                                      | 181 ms: 1.50x faster                                                        |
| richards                | 41.2 ms                                                     | 28.1 ms: 1.46x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 58.8 ms: 1.45x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 497 ms: 1.43x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.4 ms: 1.42x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 181 us: 1.42x faster                                                        |
| pyflate                 | 387 ms                                                      | 278 ms: 1.39x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.34 ms: 1.39x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 789 ms: 1.35x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 47.1 ms: 1.32x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 129 us: 1.32x faster                                                        |
| chaos                   | 58.9 ms                                                     | 44.5 ms: 1.32x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 923 us: 1.32x faster                                                        |
| async_tree_none         | 420 ms                                                      | 318 ms: 1.32x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 4.21 ms: 1.31x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.12 ms: 1.31x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 21.8 us: 1.31x faster                                                       |
| pycparser               | 868 ms                                                      | 662 ms: 1.31x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 14.6 ms: 1.30x faster                                                       |
| async_generators        | 224 ms                                                      | 173 ms: 1.30x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.59 ms: 1.29x faster                                                       |
| thrift                  | 615 us                                                      | 479 us: 1.28x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 388 ms: 1.28x faster                                                        |
| html5lib                | 46.5 ms                                                     | 36.5 ms: 1.27x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 29.8 ns: 1.27x faster                                                       |
| django_template         | 28.2 ms                                                     | 22.7 ms: 1.24x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 63.3 ms: 1.23x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 35.3 ms: 1.23x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 990 ms: 1.22x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.56 sec: 1.22x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 504 ms: 1.21x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 490 ms: 1.20x faster                                                        |
| regex_compile           | 103 ms                                                      | 86.2 ms: 1.20x faster                                                       |
| float                   | 60.2 ms                                                     | 50.3 ms: 1.20x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 34.4 ms: 1.18x faster                                                       |
| dask                    | 305 ms                                                      | 260 ms: 1.17x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 33.4 ms: 1.17x faster                                                       |
| deepcopy                | 255 us                                                      | 220 us: 1.16x faster                                                        |
| unpickle                | 9.17 us                                                     | 7.94 us: 1.16x faster                                                       |
| 2to3                    | 237 ms                                                      | 205 ms: 1.16x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.88 us: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.32 ms: 1.15x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 41.7 ms: 1.14x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 89.5 ms: 1.14x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 690 us: 1.13x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                                       |
| regex_dna               | 132 ms                                                      | 117 ms: 1.12x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 180 ms: 1.12x faster                                                        |
| json                    | 3.05 ms                                                     | 2.73 ms: 1.12x faster                                                       |
| fannkuch                | 258 ms                                                      | 232 ms: 1.11x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 853 us: 1.11x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 60.6 ms: 1.11x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.4 ms: 1.10x faster                                                       |
| sympy_expand            | 315 ms                                                      | 285 ms: 1.10x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.55 sec: 1.10x faster                                                      |
| coroutines              | 15.9 ms                                                     | 14.5 ms: 1.10x faster                                                       |
| json_loads              | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| scimark_fft             | 193 ms                                                      | 177 ms: 1.09x faster                                                        |
| regex_effbot            | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 50.5 ms: 1.08x faster                                                       |
| sympy_str               | 188 ms                                                      | 176 ms: 1.07x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| nbody                   | 69.3 ms                                                     | 66.2 ms: 1.05x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.76 us: 1.05x faster                                                       |
| sympy_sum               | 104 ms                                                      | 99.5 ms: 1.05x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.72 us: 1.03x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 62.4 ms: 1.02x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 71.5 ms: 1.01x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.71 us: 1.01x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| comprehensions          | 16.0 us                                                     | 16.3 us: 1.02x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.83 us: 1.03x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 62.6 ms: 1.03x slower                                                       |
| logging_simple          | 6.20 us                                                     | 6.47 us: 1.04x slower                                                       |
| pidigits                | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| gc_traversal            | 1.34 ms                                                     | 1.45 ms: 1.08x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.5 us: 1.09x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.88 us: 1.11x slower                                                       |
| generators              | 31.6 ms                                                     | 36.8 ms: 1.16x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.2 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
