
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0fd3891
- commit date: 2023-04-22
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| chameleon      | 7.67 ms                                                      | 7.48 ms: 1.03x faster                                        |
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                       |
| html5lib       | 72.9 ms                                                      | 67.8 ms: 1.08x faster                                        |
| tornado_http   | 122 ms                                                       | 119 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 86.6 ms: 1.05x faster                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| float          | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| regex_v8       | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                        |
| regex_effbot   | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                        |
| regex_dna      | 227 ms                                                       | 232 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                        |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.17x faster                                         |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| pickle_pure_python   | 319 us                                                       | 315 us: 1.01x faster                                         |
| pickle_dict          | 30.8 us                                                      | 30.9 us: 1.00x slower                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.2 ms: 1.03x slower                                        |
| pickle_list          | 3.83 us                                                      | 3.96 us: 1.04x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.72 us: 1.04x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 84.5 ms: 1.05x slower                                        |
| unpickle             | 13.4 us                                                      | 14.2 us: 1.05x slower                                        |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                        |
| genshi_xml      | 58.5 ms                                                      | 54.1 ms: 1.08x faster                                        |
| genshi_text     | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                        |
| django_template | 40.2 ms                                                      | 38.6 ms: 1.04x faster                                        |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-main-3.12.0a7+-0fd3891 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 376 ms: 2.00x faster                                         |
| generators              | 56.0 ms                                                      | 36.4 ms: 1.54x faster                                        |
| json_dumps              | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                        |
| fannkuch                | 429 ms                                                       | 341 ms: 1.26x faster                                         |
| hexiom                  | 7.13 ms                                                      | 5.84 ms: 1.22x faster                                        |
| chaos                   | 80.9 ms                                                      | 66.4 ms: 1.22x faster                                        |
| coroutines              | 27.6 ms                                                      | 22.6 ms: 1.22x faster                                        |
| deltablue               | 4.00 ms                                                      | 3.30 ms: 1.21x faster                                        |
| scimark_lu              | 115 ms                                                       | 94.7 ms: 1.21x faster                                        |
| unpickle_pure_python    | 241 us                                                       | 205 us: 1.17x faster                                         |
| json_loads              | 28.7 us                                                      | 24.5 us: 1.17x faster                                        |
| mypy2                   | 451 ms                                                       | 387 ms: 1.16x faster                                         |
| nqueens                 | 103 ms                                                       | 89.0 ms: 1.16x faster                                        |
| logging_format          | 8.11 us                                                      | 7.15 us: 1.14x faster                                        |
| go                      | 164 ms                                                       | 145 ms: 1.13x faster                                         |
| json                    | 5.65 ms                                                      | 5.05 ms: 1.12x faster                                        |
| richards                | 48.3 ms                                                      | 43.3 ms: 1.11x faster                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                        |
| mako                    | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                        |
| logging_simple          | 7.19 us                                                      | 6.49 us: 1.11x faster                                        |
| regex_compile           | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| xml_etree_parse         | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| gc_traversal            | 3.85 ms                                                      | 3.56 ms: 1.08x faster                                        |
| genshi_xml              | 58.5 ms                                                      | 54.1 ms: 1.08x faster                                        |
| spectral_norm           | 93.3 ms                                                      | 86.5 ms: 1.08x faster                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                        |
| html5lib                | 72.9 ms                                                      | 67.8 ms: 1.08x faster                                        |
| async_tree_memoization  | 630 ms                                                       | 587 ms: 1.07x faster                                         |
| logging_silent          | 101 ns                                                       | 94.2 ns: 1.07x faster                                        |
| mdp                     | 2.75 sec                                                     | 2.57 sec: 1.07x faster                                       |
| sympy_expand            | 555 ms                                                       | 524 ms: 1.06x faster                                         |
| deepcopy_memo           | 38.8 us                                                      | 36.7 us: 1.06x faster                                        |
| dulwich_log             | 68.4 ms                                                      | 64.9 ms: 1.05x faster                                        |
| raytrace                | 317 ms                                                       | 300 ms: 1.05x faster                                         |
| genshi_text             | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                        |
| pylint                  | 515 ms                                                       | 491 ms: 1.05x faster                                         |
| bench_thread_pool       | 1.01 ms                                                      | 964 us: 1.05x faster                                         |
| pycparser               | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                       |
| nbody                   | 90.7 ms                                                      | 86.6 ms: 1.05x faster                                        |
| async_tree_none         | 519 ms                                                       | 498 ms: 1.04x faster                                         |
| django_template         | 40.2 ms                                                      | 38.6 ms: 1.04x faster                                        |
| sympy_str               | 337 ms                                                       | 324 ms: 1.04x faster                                         |
| crypto_pyaes            | 83.4 ms                                                      | 80.4 ms: 1.04x faster                                        |
| pathlib                 | 19.1 ms                                                      | 18.4 ms: 1.03x faster                                        |
| sqlglot_normalize       | 126 ms                                                       | 122 ms: 1.03x faster                                         |
| deepcopy                | 399 us                                                       | 388 us: 1.03x faster                                         |
| pyflate                 | 449 ms                                                       | 437 ms: 1.03x faster                                         |
| async_tree_io           | 1.17 sec                                                     | 1.14 sec: 1.03x faster                                       |
| chameleon               | 7.67 ms                                                      | 7.48 ms: 1.03x faster                                        |
| scimark_sor             | 111 ms                                                       | 109 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 733 ms: 1.02x faster                                         |
| thrift                  | 925 us                                                       | 906 us: 1.02x faster                                         |
| tornado_http            | 122 ms                                                       | 119 ms: 1.02x faster                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.45 us: 1.02x faster                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.3 ms: 1.02x faster                                        |
| sympy_sum               | 185 ms                                                       | 182 ms: 1.01x faster                                         |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| pickle_pure_python      | 319 us                                                       | 315 us: 1.01x faster                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 59.6 ms: 1.00x faster                                        |
| docutils                | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                       |
| pickle_dict             | 30.8 us                                                      | 30.9 us: 1.00x slower                                        |
| regex_v8                | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                        |
| regex_effbot            | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                        |
| scimark_fft             | 285 ms                                                       | 288 ms: 1.01x slower                                         |
| comprehensions          | 24.6 us                                                      | 25.0 us: 1.01x slower                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.66 sec: 1.02x slower                                       |
| regex_dna               | 227 ms                                                       | 232 ms: 1.02x slower                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.8 ms: 1.02x slower                                        |
| telco                   | 6.86 ms                                                      | 7.05 ms: 1.03x slower                                        |
| xml_etree_process       | 56.5 ms                                                      | 58.2 ms: 1.03x slower                                        |
| python_startup          | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                        |
| pidigits                | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| pickle_list             | 3.83 us                                                      | 3.96 us: 1.04x slower                                        |
| pprint_safe_repr        | 784 ms                                                       | 815 ms: 1.04x slower                                         |
| unpickle_list           | 4.53 us                                                      | 4.72 us: 1.04x slower                                        |
| meteor_contest          | 131 ms                                                       | 137 ms: 1.05x slower                                         |
| xml_etree_generate      | 80.5 ms                                                      | 84.5 ms: 1.05x slower                                        |
| unpickle                | 13.4 us                                                      | 14.2 us: 1.05x slower                                        |
| pickle                  | 9.64 us                                                      | 10.2 us: 1.06x slower                                        |
| sqlite_synth            | 2.50 us                                                      | 2.65 us: 1.06x slower                                        |
| float                   | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                        |
| coverage                | 84.8 ms                                                      | 90.9 ms: 1.07x slower                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.35 ms: 1.07x slower                                        |
| unpack_sequence         | 45.6 ns                                                      | 52.6 ns: 1.15x slower                                        |
| async_generators        | 316 ms                                                       | 386 ms: 1.22x slower                                         |
| dask                    | 410 ms                                                       | 560 ms: 1.37x slower                                         |
| bench_mp_pool           | 4.62 ms                                                      | 7.21 ms: 1.56x slower                                        |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, create_gc_cycles
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
