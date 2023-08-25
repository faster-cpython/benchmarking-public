
# Results vs. 3.11.0

- fork: python
- ref: 7b14c2ef194b6eed7967
- machine: linux-x86_64
- commit hash: 7b14c2e
- commit date: 2023-01-16
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 287 ms: 1.00x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.60 ms: 1.01x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                       |
| html5lib       | 72.9 ms                                                      | 66.6 ms: 1.10x faster                                                        |
| tornado_http   | 122 ms                                                       | 120 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 72.6 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.34 ms: 1.05x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                        |
| regex_compile  | 158 ms                                                       | 151 ms: 1.04x faster                                                         |
| regex_dna      | 227 ms                                                       | 226 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.3 us: 1.18x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 210 us: 1.15x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 143 ms: 1.10x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 304 us: 1.05x faster                                                         |
| xml_etree_process    | 56.5 ms                                                      | 54.8 ms: 1.03x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 79.0 ms: 1.02x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.3 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                                         |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 32.2 us: 1.05x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.12 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.18 ms: 1.05x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| genshi_xml     | 58.5 ms                                                      | 56.5 ms: 1.04x faster                                                        |
| genshi_text    | 26.1 ms                                                      | 25.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 393 ms: 1.92x faster                                                         |
| json_dumps              | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                        |
| mypy2                   | 451 ms                                                       | 379 ms: 1.19x faster                                                         |
| json_loads              | 28.7 us                                                      | 24.3 us: 1.18x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 210 us: 1.15x faster                                                         |
| chaos                   | 80.9 ms                                                      | 72.1 ms: 1.12x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.58 ms: 1.12x faster                                                        |
| scimark_lu              | 115 ms                                                       | 103 ms: 1.11x faster                                                         |
| json                    | 5.65 ms                                                      | 5.09 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.66 ms: 1.11x faster                                                        |
| xml_etree_parse         | 158 ms                                                       | 143 ms: 1.10x faster                                                         |
| html5lib                | 72.9 ms                                                      | 66.6 ms: 1.10x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.52 ms: 1.09x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.23 sec: 1.07x faster                                                       |
| nqueens                 | 103 ms                                                       | 95.8 ms: 1.07x faster                                                        |
| fannkuch                | 429 ms                                                       | 401 ms: 1.07x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 6.69 ms: 1.07x faster                                                        |
| gunicorn                | 973 us                                                       | 914 us: 1.06x faster                                                         |
| aiohttp                 | 985 us                                                       | 927 us: 1.06x faster                                                         |
| bench_thread_pool       | 1.01 ms                                                      | 955 us: 1.06x faster                                                         |
| raytrace                | 317 ms                                                       | 300 ms: 1.06x faster                                                         |
| richards                | 48.3 ms                                                      | 46.0 ms: 1.05x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 304 us: 1.05x faster                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.34 ms: 1.05x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                        |
| deepcopy_memo           | 38.8 us                                                      | 37.1 us: 1.05x faster                                                        |
| regex_compile           | 158 ms                                                       | 151 ms: 1.04x faster                                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 65.8 ms: 1.04x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 122 ms: 1.04x faster                                                         |
| genshi_xml              | 58.5 ms                                                      | 56.5 ms: 1.04x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 609 ms: 1.03x faster                                                         |
| sympy_expand            | 555 ms                                                       | 536 ms: 1.03x faster                                                         |
| xml_etree_process       | 56.5 ms                                                      | 54.8 ms: 1.03x faster                                                        |
| pyflate                 | 449 ms                                                       | 436 ms: 1.03x faster                                                         |
| docutils                | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.90 us: 1.03x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.59 sec: 1.03x faster                                                       |
| go                      | 164 ms                                                       | 160 ms: 1.02x faster                                                         |
| genshi_text             | 26.1 ms                                                      | 25.5 ms: 1.02x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 66.9 ms: 1.02x faster                                                        |
| unpack_sequence         | 45.6 ns                                                      | 44.7 ns: 1.02x faster                                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 58.5 ms: 1.02x faster                                                        |
| float                   | 74.2 ms                                                      | 72.6 ms: 1.02x faster                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 79.0 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.45 us: 1.02x faster                                                        |
| async_tree_none         | 519 ms                                                       | 510 ms: 1.02x faster                                                         |
| scimark_sor             | 111 ms                                                       | 109 ms: 1.02x faster                                                         |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.02x faster                                                         |
| sympy_integrate         | 25.8 ms                                                      | 25.4 ms: 1.01x faster                                                        |
| tornado_http            | 122 ms                                                       | 120 ms: 1.01x faster                                                         |
| unpickle                | 13.4 us                                                      | 13.3 us: 1.01x faster                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                                       |
| logging_silent          | 101 ns                                                       | 99.5 ns: 1.01x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.77 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 774 ms: 1.01x faster                                                         |
| sympy_str               | 337 ms                                                       | 333 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 741 ms: 1.01x faster                                                         |
| logging_simple          | 7.19 us                                                      | 7.12 us: 1.01x faster                                                        |
| thrift                  | 925 us                                                       | 916 us: 1.01x faster                                                         |
| chameleon               | 7.67 ms                                                      | 7.60 ms: 1.01x faster                                                        |
| regex_dna               | 227 ms                                                       | 226 ms: 1.01x faster                                                         |
| 2to3                    | 288 ms                                                       | 287 ms: 1.00x faster                                                         |
| scimark_fft             | 285 ms                                                       | 287 ms: 1.01x slower                                                         |
| mdp                     | 2.75 sec                                                     | 2.77 sec: 1.01x slower                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 84.3 ms: 1.01x slower                                                        |
| dask                    | 410 ms                                                       | 415 ms: 1.01x slower                                                         |
| pathlib                 | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 106 ms: 1.02x slower                                                         |
| coverage                | 84.8 ms                                                      | 86.4 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.96 ms: 1.02x slower                                                        |
| coroutines              | 27.6 ms                                                      | 28.3 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.57 us: 1.03x slower                                                        |
| python_startup          | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.59 ms: 1.04x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 96.9 ms: 1.04x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.0 us: 1.04x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 32.2 us: 1.05x slower                                                        |
| async_generators        | 316 ms                                                       | 333 ms: 1.05x slower                                                         |
| python_startup_no_site  | 7.76 ms                                                      | 8.18 ms: 1.05x slower                                                        |
| pickle_list             | 3.83 us                                                      | 4.12 us: 1.08x slower                                                        |
| generators              | 56.0 ms                                                      | 60.7 ms: 1.08x slower                                                        |
| comprehensions          | 24.6 us                                                      | 27.3 us: 1.11x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (8): nbody, create_gc_cycles, deepcopy, django_template, unpickle_list, pidigits, sympy_sum, bench_mp_pool
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
