
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| chameleon      | 7.67 ms                                                      | 7.03 ms: 1.09x faster                                        |
| docutils       | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                       |
| html5lib       | 72.9 ms                                                      | 67.1 ms: 1.09x faster                                        |
| tornado_http   | 122 ms                                                       | 115 ms: 1.06x faster                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.0 ms: 1.08x faster                                        |
| float          | 74.2 ms                                                      | 72.6 ms: 1.02x faster                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.06x faster                                         |
| regex_v8       | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.48 ms: 1.01x faster                                        |
| regex_dna      | 227 ms                                                       | 235 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                        |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.18x faster                                        |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.17x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| pickle_list          | 3.83 us                                                      | 3.76 us: 1.02x faster                                        |
| pickle_pure_python   | 319 us                                                       | 314 us: 1.02x faster                                         |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.01x faster                                         |
| pickle_dict          | 30.8 us                                                      | 30.5 us: 1.01x faster                                        |
| xml_etree_process    | 56.5 ms                                                      | 56.8 ms: 1.01x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.59 us: 1.01x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 82.6 ms: 1.03x slower                                        |
| pickle               | 9.64 us                                                      | 9.92 us: 1.03x slower                                        |
| unpickle             | 13.4 us                                                      | 14.0 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.29 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 52.7 ms: 1.11x faster                                        |
| mako            | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| genshi_text     | 26.1 ms                                                      | 24.8 ms: 1.05x faster                                        |
| django_template | 40.2 ms                                                      | 38.9 ms: 1.04x faster                                        |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 384 ms: 1.96x faster                                         |
| generators              | 56.0 ms                                                      | 37.6 ms: 1.49x faster                                        |
| json_dumps              | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                        |
| mypy2                   | 451 ms                                                       | 378 ms: 1.19x faster                                         |
| json_loads              | 28.7 us                                                      | 24.2 us: 1.18x faster                                        |
| deltablue               | 4.00 ms                                                      | 3.40 ms: 1.17x faster                                        |
| unpickle_pure_python    | 241 us                                                       | 205 us: 1.17x faster                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.35 ms: 1.14x faster                                        |
| chaos                   | 80.9 ms                                                      | 72.0 ms: 1.12x faster                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.71 ms: 1.12x faster                                        |
| logging_format          | 8.11 us                                                      | 7.26 us: 1.12x faster                                        |
| deepcopy_memo           | 38.8 us                                                      | 34.8 us: 1.12x faster                                        |
| genshi_xml              | 58.5 ms                                                      | 52.7 ms: 1.11x faster                                        |
| json                    | 5.65 ms                                                      | 5.13 ms: 1.10x faster                                        |
| scimark_lu              | 115 ms                                                       | 104 ms: 1.10x faster                                         |
| raytrace                | 317 ms                                                       | 288 ms: 1.10x faster                                         |
| logging_simple          | 7.19 us                                                      | 6.58 us: 1.09x faster                                        |
| coroutines              | 27.6 ms                                                      | 25.2 ms: 1.09x faster                                        |
| chameleon               | 7.67 ms                                                      | 7.03 ms: 1.09x faster                                        |
| mako                    | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| xml_etree_parse         | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| html5lib                | 72.9 ms                                                      | 67.1 ms: 1.09x faster                                        |
| hexiom                  | 7.13 ms                                                      | 6.60 ms: 1.08x faster                                        |
| mdp                     | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                       |
| nbody                   | 90.7 ms                                                      | 84.0 ms: 1.08x faster                                        |
| pycparser               | 1.32 sec                                                     | 1.24 sec: 1.07x faster                                       |
| sqlglot_normalize       | 126 ms                                                       | 118 ms: 1.07x faster                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.30 us: 1.06x faster                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.81 ms: 1.06x faster                                        |
| deepcopy                | 399 us                                                       | 376 us: 1.06x faster                                         |
| regex_compile           | 158 ms                                                       | 149 ms: 1.06x faster                                         |
| bench_thread_pool       | 1.01 ms                                                      | 955 us: 1.06x faster                                         |
| dulwich_log             | 68.4 ms                                                      | 64.7 ms: 1.06x faster                                        |
| tornado_http            | 122 ms                                                       | 115 ms: 1.06x faster                                         |
| genshi_text             | 26.1 ms                                                      | 24.8 ms: 1.05x faster                                        |
| scimark_fft             | 285 ms                                                       | 271 ms: 1.05x faster                                         |
| logging_silent          | 101 ns                                                       | 96.0 ns: 1.05x faster                                        |
| async_tree_memoization  | 630 ms                                                       | 601 ms: 1.05x faster                                         |
| coverage                | 84.8 ms                                                      | 81.2 ms: 1.04x faster                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 57.5 ms: 1.04x faster                                        |
| thrift                  | 925 us                                                       | 891 us: 1.04x faster                                         |
| django_template         | 40.2 ms                                                      | 38.9 ms: 1.04x faster                                        |
| async_tree_none         | 519 ms                                                       | 503 ms: 1.03x faster                                         |
| async_tree_io           | 1.17 sec                                                     | 1.14 sec: 1.03x faster                                       |
| sympy_integrate         | 25.8 ms                                                      | 25.0 ms: 1.03x faster                                        |
| sympy_expand            | 555 ms                                                       | 538 ms: 1.03x faster                                         |
| unpack_sequence         | 45.6 ns                                                      | 44.4 ns: 1.03x faster                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.59 sec: 1.03x faster                                       |
| go                      | 164 ms                                                       | 160 ms: 1.03x faster                                         |
| spectral_norm           | 93.3 ms                                                      | 91.2 ms: 1.02x faster                                        |
| float                   | 74.2 ms                                                      | 72.6 ms: 1.02x faster                                        |
| sympy_str               | 337 ms                                                       | 330 ms: 1.02x faster                                         |
| gc_traversal            | 3.85 ms                                                      | 3.77 ms: 1.02x faster                                        |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 735 ms: 1.02x faster                                         |
| regex_v8                | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| richards                | 48.3 ms                                                      | 47.4 ms: 1.02x faster                                        |
| pickle_list             | 3.83 us                                                      | 3.76 us: 1.02x faster                                        |
| docutils                | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                       |
| pickle_pure_python      | 319 us                                                       | 314 us: 1.02x faster                                         |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 67.4 ms: 1.01x faster                                        |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.01x faster                                         |
| nqueens                 | 103 ms                                                       | 102 ms: 1.01x faster                                         |
| pickle_dict             | 30.8 us                                                      | 30.5 us: 1.01x faster                                        |
| sympy_sum               | 185 ms                                                       | 183 ms: 1.01x faster                                         |
| regex_effbot            | 3.50 ms                                                      | 3.48 ms: 1.01x faster                                        |
| telco                   | 6.86 ms                                                      | 6.82 ms: 1.01x faster                                        |
| comprehensions          | 24.6 us                                                      | 24.7 us: 1.00x slower                                        |
| xml_etree_process       | 56.5 ms                                                      | 56.8 ms: 1.01x slower                                        |
| scimark_sor             | 111 ms                                                       | 113 ms: 1.01x slower                                         |
| unpickle_list           | 4.53 us                                                      | 4.59 us: 1.01x slower                                        |
| python_startup          | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                        |
| xml_etree_generate      | 80.5 ms                                                      | 82.6 ms: 1.03x slower                                        |
| pickle                  | 9.64 us                                                      | 9.92 us: 1.03x slower                                        |
| crypto_pyaes            | 83.4 ms                                                      | 85.9 ms: 1.03x slower                                        |
| pidigits                | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| regex_dna               | 227 ms                                                       | 235 ms: 1.04x slower                                         |
| pathlib                 | 19.1 ms                                                      | 19.8 ms: 1.04x slower                                        |
| bench_mp_pool           | 4.62 ms                                                      | 4.82 ms: 1.04x slower                                        |
| unpickle                | 13.4 us                                                      | 14.0 us: 1.04x slower                                        |
| sqlite_synth            | 2.50 us                                                      | 2.62 us: 1.05x slower                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.29 ms: 1.07x slower                                        |
| async_generators        | 316 ms                                                       | 381 ms: 1.21x slower                                         |
| dask                    | 410 ms                                                       | 566 ms: 1.38x slower                                         |
| Geometric mean          | (ref)                                                        | 1.05x faster                                                 |

Benchmark hidden because not significant (4): create_gc_cycles, pyflate, pprint_safe_repr, fannkuch
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
