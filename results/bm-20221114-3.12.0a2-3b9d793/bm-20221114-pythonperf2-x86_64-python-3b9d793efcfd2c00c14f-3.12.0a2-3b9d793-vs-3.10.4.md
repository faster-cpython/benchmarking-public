
# Results vs. 3.10.4

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: linux-x86_64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| chameleon      | 9.72 ms                                                      | 7.19 ms: 1.35x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.77 sec: 1.23x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.7 ms: 1.42x faster                                                       |
| tornado_http   | 152 ms                                                       | 115 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 90.9 ms: 1.51x faster                                                       |
| float          | 110 ms                                                       | 73.2 ms: 1.51x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 147 ms: 1.32x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                                       |
| regex_dna      | 259 ms                                                       | 227 ms: 1.14x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.45 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 209 us: 1.53x faster                                                        |
| pickle_pure_python   | 457 us                                                       | 314 us: 1.46x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 54.8 ms: 1.39x faster                                                       |
| json_loads           | 30.0 us                                                      | 23.7 us: 1.26x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 79.3 ms: 1.19x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 143 ms: 1.13x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.65 us: 1.13x faster                                                       |
| unpickle             | 14.2 us                                                      | 12.6 us: 1.12x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 108 ms: 1.03x faster                                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.01x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 33.4 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.87 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                       |
| django_template | 51.5 ms                                                      | 39.7 ms: 1.30x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 25.2 ms: 1.25x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 54.0 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.64 ms: 2.05x faster                                                       |
| logging_silent          | 166 ns                                                       | 99.2 ns: 1.67x faster                                                       |
| scimark_sor             | 177 ms                                                       | 106 ms: 1.66x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 66.4 ms: 1.65x faster                                                       |
| richards                | 74.1 ms                                                      | 45.4 ms: 1.63x faster                                                       |
| go                      | 259 ms                                                       | 160 ms: 1.61x faster                                                        |
| pyflate                 | 697 ms                                                       | 436 ms: 1.60x faster                                                        |
| raytrace                | 488 ms                                                       | 305 ms: 1.60x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.59 ms: 1.56x faster                                                       |
| unpickle_pure_python    | 321 us                                                       | 209 us: 1.53x faster                                                        |
| nbody                   | 137 ms                                                       | 90.9 ms: 1.51x faster                                                       |
| float                   | 110 ms                                                       | 73.2 ms: 1.51x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 1.50 ms: 1.50x faster                                                       |
| scimark_lu              | 164 ms                                                       | 111 ms: 1.47x faster                                                        |
| chaos                   | 107 ms                                                       | 72.9 ms: 1.47x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 80.7 ms: 1.46x faster                                                       |
| spectral_norm           | 136 ms                                                       | 93.2 ms: 1.46x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 314 us: 1.46x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.87 ms: 1.45x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                       |
| html5lib                | 94.6 ms                                                      | 66.7 ms: 1.42x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 6.76 ms: 1.41x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 752 ms: 1.40x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.74 ms: 1.39x faster                                                       |
| pprint_pformat          | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                      |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 54.8 ms: 1.39x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                                      |
| chameleon               | 9.72 ms                                                      | 7.19 ms: 1.35x faster                                                       |
| async_tree_none         | 700 ms                                                       | 520 ms: 1.34x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                                      |
| aiohttp                 | 1.21 ms                                                      | 904 us: 1.34x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 36.7 us: 1.33x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 621 ms: 1.33x faster                                                        |
| gunicorn                | 1.17 ms                                                      | 886 us: 1.32x faster                                                        |
| regex_compile           | 194 ms                                                       | 147 ms: 1.32x faster                                                        |
| tornado_http            | 152 ms                                                       | 115 ms: 1.32x faster                                                        |
| scimark_fft             | 359 ms                                                       | 273 ms: 1.32x faster                                                        |
| async_generators        | 422 ms                                                       | 321 ms: 1.31x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.78 us: 1.31x faster                                                       |
| unpack_sequence         | 59.5 ns                                                      | 45.8 ns: 1.30x faster                                                       |
| django_template         | 51.5 ms                                                      | 39.7 ms: 1.30x faster                                                       |
| thrift                  | 1.16 ms                                                      | 913 us: 1.28x faster                                                        |
| fannkuch                | 496 ms                                                       | 391 ms: 1.27x faster                                                        |
| json_loads              | 30.0 us                                                      | 23.7 us: 1.26x faster                                                       |
| logging_format          | 9.57 us                                                      | 7.60 us: 1.26x faster                                                       |
| genshi_text             | 31.5 ms                                                      | 25.2 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed | 952 ms                                                       | 762 ms: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 374 ms: 1.25x faster                                                        |
| 2to3                    | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.77 sec: 1.23x faster                                                      |
| sqlglot_optimize        | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                                       |
| json                    | 5.96 ms                                                      | 4.95 ms: 1.20x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 54.0 ms: 1.20x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 79.3 ms: 1.19x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 67.2 ms: 1.19x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.39 us: 1.19x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 122 ms: 1.18x faster                                                        |
| deepcopy                | 454 us                                                       | 387 us: 1.17x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 969 us: 1.17x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.57 us: 1.15x faster                                                       |
| regex_v8                | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                                       |
| regex_dna               | 259 ms                                                       | 227 ms: 1.14x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.60 ms: 1.14x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 143 ms: 1.13x faster                                                        |
| dask                    | 463 ms                                                       | 410 ms: 1.13x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.65 us: 1.13x faster                                                       |
| pathlib                 | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                                       |
| unpickle                | 14.2 us                                                      | 12.6 us: 1.12x faster                                                       |
| mdp                     | 3.03 sec                                                     | 2.73 sec: 1.11x faster                                                      |
| sympy_integrate         | 28.1 ms                                                      | 25.5 ms: 1.10x faster                                                       |
| nqueens                 | 112 ms                                                       | 103 ms: 1.10x faster                                                        |
| coroutines              | 30.4 ms                                                      | 27.9 ms: 1.09x faster                                                       |
| sympy_expand            | 599 ms                                                       | 550 ms: 1.09x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.58 ms: 1.09x faster                                                       |
| pidigits                | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| sympy_str               | 358 ms                                                       | 337 ms: 1.06x faster                                                        |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 749 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 108 ms: 1.03x faster                                                        |
| pickle                  | 9.94 us                                                      | 10.1 us: 1.01x slower                                                       |
| generators              | 58.0 ms                                                      | 61.2 ms: 1.06x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.87 ms: 1.08x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 33.4 us: 1.11x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.92 ms: 1.14x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.45 ms: 1.15x slower                                                       |
| coverage                | 64.0 ms                                                      | 86.9 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                |

Benchmark hidden because not significant (2): comprehensions, unpickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x
