
# Results vs. 3.11.0

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: linux-x86_64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 282 ms: 1.02x faster                                                        |
| chameleon      | 7.67 ms                                                      | 7.19 ms: 1.07x faster                                                       |
| docutils       | 2.86 sec                                                     | 2.77 sec: 1.03x faster                                                      |
| html5lib       | 72.9 ms                                                      | 66.7 ms: 1.09x faster                                                       |
| tornado_http   | 122 ms                                                       | 115 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 73.2 ms: 1.01x faster                                                       |
| pidigits       | 251 ms                                                       | 252 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 147 ms: 1.08x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                       |
| regex_effbot   | 3.50 ms                                                      | 3.45 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                       |
| json_loads           | 28.7 us                                                      | 23.7 us: 1.21x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 209 us: 1.15x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 143 ms: 1.11x faster                                                        |
| unpickle             | 13.4 us                                                      | 12.6 us: 1.06x faster                                                       |
| pickle_list          | 3.83 us                                                      | 3.65 us: 1.05x faster                                                       |
| xml_etree_process    | 56.5 ms                                                      | 54.8 ms: 1.03x faster                                                       |
| pickle_pure_python   | 319 us                                                       | 314 us: 1.02x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 79.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 108 ms: 1.03x slower                                                        |
| pickle               | 9.64 us                                                      | 10.1 us: 1.04x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 33.4 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 7.87 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 54.0 ms: 1.08x faster                                                       |
| mako           | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                       |
| genshi_text    | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                       |
| json_loads              | 28.7 us                                                      | 23.7 us: 1.21x faster                                                       |
| mypy2                   | 451 ms                                                       | 374 ms: 1.21x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 209 us: 1.15x faster                                                        |
| json                    | 5.65 ms                                                      | 4.95 ms: 1.14x faster                                                       |
| chaos                   | 80.9 ms                                                      | 72.9 ms: 1.11x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 143 ms: 1.11x faster                                                        |
| gunicorn                | 973 us                                                       | 886 us: 1.10x faster                                                        |
| fannkuch                | 429 ms                                                       | 391 ms: 1.10x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.64 ms: 1.10x faster                                                       |
| html5lib                | 72.9 ms                                                      | 66.7 ms: 1.09x faster                                                       |
| aiohttp                 | 985 us                                                       | 904 us: 1.09x faster                                                        |
| genshi_xml              | 58.5 ms                                                      | 54.0 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.74 ms: 1.08x faster                                                       |
| regex_compile           | 158 ms                                                       | 147 ms: 1.08x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                       |
| chameleon               | 7.67 ms                                                      | 7.19 ms: 1.07x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.60 us: 1.07x faster                                                       |
| pycparser               | 1.32 sec                                                     | 1.24 sec: 1.07x faster                                                      |
| richards                | 48.3 ms                                                      | 45.4 ms: 1.06x faster                                                       |
| unpickle                | 13.4 us                                                      | 12.6 us: 1.06x faster                                                       |
| logging_simple          | 7.19 us                                                      | 6.78 us: 1.06x faster                                                       |
| deepcopy_memo           | 38.8 us                                                      | 36.7 us: 1.06x faster                                                       |
| tornado_http            | 122 ms                                                       | 115 ms: 1.05x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.76 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.63 sec                                                     | 1.55 sec: 1.05x faster                                                      |
| pickle_list             | 3.83 us                                                      | 3.65 us: 1.05x faster                                                       |
| scimark_sor             | 111 ms                                                       | 106 ms: 1.04x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 969 us: 1.04x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.58 ms: 1.04x faster                                                       |
| scimark_fft             | 285 ms                                                       | 273 ms: 1.04x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 752 ms: 1.04x faster                                                        |
| genshi_text             | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                       |
| raytrace                | 317 ms                                                       | 305 ms: 1.04x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.39 us: 1.04x faster                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 80.7 ms: 1.03x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.77 sec: 1.03x faster                                                      |
| regex_v8                | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                       |
| deepcopy                | 399 us                                                       | 387 us: 1.03x faster                                                        |
| xml_etree_process       | 56.5 ms                                                      | 54.8 ms: 1.03x faster                                                       |
| scimark_lu              | 115 ms                                                       | 111 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 122 ms: 1.03x faster                                                        |
| pyflate                 | 449 ms                                                       | 436 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 66.4 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 1.87 ms: 1.03x faster                                                       |
| go                      | 164 ms                                                       | 160 ms: 1.02x faster                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.50 ms: 1.02x faster                                                       |
| dulwich_log             | 68.4 ms                                                      | 67.2 ms: 1.02x faster                                                       |
| 2to3                    | 288 ms                                                       | 282 ms: 1.02x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 314 us: 1.02x faster                                                        |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.02x faster                                                        |
| logging_silent          | 101 ns                                                       | 99.2 ns: 1.02x faster                                                       |
| async_tree_memoization  | 630 ms                                                       | 621 ms: 1.02x faster                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 79.3 ms: 1.02x faster                                                       |
| regex_effbot            | 3.50 ms                                                      | 3.45 ms: 1.01x faster                                                       |
| float                   | 74.2 ms                                                      | 73.2 ms: 1.01x faster                                                       |
| thrift                  | 925 us                                                       | 913 us: 1.01x faster                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.5 ms: 1.01x faster                                                       |
| sympy_expand            | 555 ms                                                       | 550 ms: 1.01x faster                                                        |
| asyncio_tcp             | 753 ms                                                       | 749 ms: 1.01x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.73 sec: 1.00x faster                                                      |
| pidigits                | 251 ms                                                       | 252 ms: 1.00x slower                                                        |
| python_startup          | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                       |
| coroutines              | 27.6 ms                                                      | 27.9 ms: 1.01x slower                                                       |
| pathlib                 | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.87 ms: 1.02x slower                                                       |
| async_generators        | 316 ms                                                       | 321 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 762 ms: 1.02x slower                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.92 ms: 1.02x slower                                                       |
| coverage                | 84.8 ms                                                      | 86.9 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.50 us                                                      | 2.57 us: 1.03x slower                                                       |
| xml_etree_iterparse     | 104 ms                                                       | 108 ms: 1.03x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.1 us: 1.04x slower                                                       |
| pickle_dict             | 30.8 us                                                      | 33.4 us: 1.09x slower                                                       |
| generators              | 56.0 ms                                                      | 61.2 ms: 1.09x slower                                                       |
| comprehensions          | 24.6 us                                                      | 26.9 us: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (14): django_template, bench_mp_pool, create_gc_cycles, unpickle_list, nqueens, async_tree_io, sympy_sum, regex_dna, spectral_norm, sympy_str, dask, async_tree_none, nbody, unpack_sequence
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
