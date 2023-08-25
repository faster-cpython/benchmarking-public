
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| chameleon      | 9.72 ms                                                      | 7.03 ms: 1.38x faster                                        |
| docutils       | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                       |
| html5lib       | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                        |
| tornado_http   | 152 ms                                                       | 115 ms: 1.32x faster                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 84.0 ms: 1.63x faster                                        |
| float          | 110 ms                                                       | 72.6 ms: 1.52x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.37x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.5 ms: 1.13x faster                                        |
| regex_dna      | 259 ms                                                       | 235 ms: 1.10x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.56x faster                                         |
| pickle_pure_python   | 457 us                                                       | 314 us: 1.46x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                        |
| xml_etree_process    | 76.0 ms                                                      | 56.8 ms: 1.34x faster                                        |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 82.6 ms: 1.14x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 145 ms: 1.12x faster                                         |
| pickle_list          | 4.11 us                                                      | 3.76 us: 1.09x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| pickle_dict          | 30.0 us                                                      | 30.5 us: 1.02x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.59 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                 |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.29 ms: 1.13x slower                                        |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| django_template | 51.5 ms                                                      | 38.9 ms: 1.33x faster                                        |
| genshi_text     | 31.5 ms                                                      | 24.8 ms: 1.27x faster                                        |
| genshi_xml      | 64.7 ms                                                      | 52.7 ms: 1.23x faster                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.40 ms: 2.19x faster                                        |
| asyncio_tcp             | 782 ms                                                       | 384 ms: 2.04x faster                                         |
| logging_silent          | 166 ns                                                       | 96.0 ns: 1.73x faster                                        |
| raytrace                | 488 ms                                                       | 288 ms: 1.70x faster                                         |
| sqlglot_parse           | 2.26 ms                                                      | 1.35 ms: 1.67x faster                                        |
| nbody                   | 137 ms                                                       | 84.0 ms: 1.63x faster                                        |
| scimark_monte_carlo     | 109 ms                                                       | 67.4 ms: 1.62x faster                                        |
| go                      | 259 ms                                                       | 160 ms: 1.62x faster                                         |
| sqlglot_transpile       | 2.71 ms                                                      | 1.71 ms: 1.58x faster                                        |
| scimark_sor             | 177 ms                                                       | 113 ms: 1.57x faster                                         |
| scimark_lu              | 164 ms                                                       | 104 ms: 1.57x faster                                         |
| pyflate                 | 697 ms                                                       | 446 ms: 1.56x faster                                         |
| richards                | 74.1 ms                                                      | 47.4 ms: 1.56x faster                                        |
| unpickle_pure_python    | 321 us                                                       | 205 us: 1.56x faster                                         |
| generators              | 58.0 ms                                                      | 37.6 ms: 1.54x faster                                        |
| float                   | 110 ms                                                       | 72.6 ms: 1.52x faster                                        |
| spectral_norm           | 136 ms                                                       | 91.2 ms: 1.49x faster                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.82 ms: 1.49x faster                                        |
| chaos                   | 107 ms                                                       | 72.0 ms: 1.49x faster                                        |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| pickle_pure_python      | 457 us                                                       | 314 us: 1.46x faster                                         |
| hexiom                  | 9.52 ms                                                      | 6.60 ms: 1.44x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.14 sec: 1.41x faster                                       |
| html5lib                | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                        |
| deepcopy_memo           | 48.9 us                                                      | 34.8 us: 1.41x faster                                        |
| async_tree_none         | 700 ms                                                       | 503 ms: 1.39x faster                                         |
| chameleon               | 9.72 ms                                                      | 7.03 ms: 1.38x faster                                        |
| crypto_pyaes            | 118 ms                                                       | 85.9 ms: 1.38x faster                                        |
| async_tree_memoization  | 824 ms                                                       | 601 ms: 1.37x faster                                         |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.81 ms: 1.36x faster                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.59 sec: 1.36x faster                                       |
| json_dumps              | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                        |
| logging_simple          | 8.90 us                                                      | 6.58 us: 1.35x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.24 sec: 1.35x faster                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 780 ms: 1.35x faster                                         |
| unpack_sequence         | 59.5 ns                                                      | 44.4 ns: 1.34x faster                                        |
| xml_etree_process       | 76.0 ms                                                      | 56.8 ms: 1.34x faster                                        |
| django_template         | 51.5 ms                                                      | 38.9 ms: 1.33x faster                                        |
| scimark_fft             | 359 ms                                                       | 271 ms: 1.33x faster                                         |
| tornado_http            | 152 ms                                                       | 115 ms: 1.32x faster                                         |
| logging_format          | 9.57 us                                                      | 7.26 us: 1.32x faster                                        |
| thrift                  | 1.16 ms                                                      | 891 us: 1.31x faster                                         |
| regex_compile           | 194 ms                                                       | 149 ms: 1.30x faster                                         |
| async_tree_cpu_io_mixed | 952 ms                                                       | 735 ms: 1.29x faster                                         |
| genshi_text             | 31.5 ms                                                      | 24.8 ms: 1.27x faster                                        |
| json_loads              | 30.0 us                                                      | 24.2 us: 1.24x faster                                        |
| dulwich_log             | 80.1 ms                                                      | 64.7 ms: 1.24x faster                                        |
| mypy2                   | 466 ms                                                       | 378 ms: 1.23x faster                                         |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| genshi_xml              | 64.7 ms                                                      | 52.7 ms: 1.23x faster                                        |
| sqlglot_normalize       | 144 ms                                                       | 118 ms: 1.22x faster                                         |
| deepcopy_reduce         | 4.03 us                                                      | 3.30 us: 1.22x faster                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 57.5 ms: 1.22x faster                                        |
| docutils                | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                       |
| deepcopy                | 454 us                                                       | 376 us: 1.21x faster                                         |
| coroutines              | 30.4 ms                                                      | 25.2 ms: 1.21x faster                                        |
| mdp                     | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                       |
| bench_thread_pool       | 1.14 ms                                                      | 955 us: 1.19x faster                                         |
| json                    | 5.96 ms                                                      | 5.13 ms: 1.16x faster                                        |
| fannkuch                | 496 ms                                                       | 432 ms: 1.15x faster                                         |
| xml_etree_generate      | 94.6 ms                                                      | 82.6 ms: 1.14x faster                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.59 ms: 1.14x faster                                        |
| regex_v8                | 26.6 ms                                                      | 23.5 ms: 1.13x faster                                        |
| sqlite_synth            | 2.97 us                                                      | 2.62 us: 1.13x faster                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.0 ms: 1.12x faster                                        |
| xml_etree_parse         | 162 ms                                                       | 145 ms: 1.12x faster                                         |
| sympy_expand            | 599 ms                                                       | 538 ms: 1.11x faster                                         |
| async_generators        | 422 ms                                                       | 381 ms: 1.11x faster                                         |
| nqueens                 | 112 ms                                                       | 102 ms: 1.10x faster                                         |
| regex_dna               | 259 ms                                                       | 235 ms: 1.10x faster                                         |
| pathlib                 | 21.7 ms                                                      | 19.8 ms: 1.09x faster                                        |
| pickle_list             | 4.11 us                                                      | 3.76 us: 1.09x faster                                        |
| comprehensions          | 26.9 us                                                      | 24.7 us: 1.09x faster                                        |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                         |
| xml_etree_iterparse     | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                         |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                         |
| telco                   | 7.14 ms                                                      | 6.82 ms: 1.05x faster                                        |
| python_startup          | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| pickle_dict             | 30.0 us                                                      | 30.5 us: 1.02x slower                                        |
| unpickle_list           | 4.49 us                                                      | 4.59 us: 1.02x slower                                        |
| gc_traversal            | 3.45 ms                                                      | 3.77 ms: 1.09x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.29 ms: 1.13x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                        |
| dask                    | 463 ms                                                       | 566 ms: 1.22x slower                                         |
| coverage                | 64.0 ms                                                      | 81.2 ms: 1.27x slower                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                 |

Benchmark hidden because not significant (2): unpickle, pickle
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
