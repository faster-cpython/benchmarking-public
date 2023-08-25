
# Results vs. 3.11.0

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: linux-x86_64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 278 ms: 1.04x faster                                                        |
| chameleon      | 7.67 ms                                                      | 7.62 ms: 1.01x faster                                                       |
| docutils       | 2.86 sec                                                     | 2.79 sec: 1.02x faster                                                      |
| html5lib       | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                       |
| tornado_http   | 122 ms                                                       | 114 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 73.2 ms: 1.01x faster                                                       |
| nbody          | 90.7 ms                                                      | 98.1 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 146 ms: 1.08x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.34 ms: 1.05x faster                                                       |
| regex_v8       | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                       |
| regex_dna      | 227 ms                                                       | 232 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                       |
| json_loads           | 28.7 us                                                      | 24.3 us: 1.18x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 208 us: 1.16x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 138 ms: 1.14x faster                                                        |
| xml_etree_process    | 56.5 ms                                                      | 54.1 ms: 1.04x faster                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 77.6 ms: 1.04x faster                                                       |
| pickle_pure_python   | 319 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.02x faster                                                        |
| unpickle_list        | 4.53 us                                                      | 4.47 us: 1.01x faster                                                       |
| unpickle             | 13.4 us                                                      | 13.3 us: 1.01x faster                                                       |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                                       |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.62 ms: 1.02x faster                                                       |
| python_startup         | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 26.1 ms                                                      | 24.7 ms: 1.06x faster                                                       |
| genshi_xml     | 58.5 ms                                                      | 55.5 ms: 1.06x faster                                                       |
| mako           | 11.0 ms                                                      | 10.4 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                       |
| mypy2                   | 451 ms                                                       | 372 ms: 1.21x faster                                                        |
| json_loads              | 28.7 us                                                      | 24.3 us: 1.18x faster                                                       |
| unpickle_pure_python    | 241 us                                                       | 208 us: 1.16x faster                                                        |
| xml_etree_parse         | 158 ms                                                       | 138 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.58 ms: 1.13x faster                                                       |
| json                    | 5.65 ms                                                      | 5.05 ms: 1.12x faster                                                       |
| aiohttp                 | 985 us                                                       | 894 us: 1.10x faster                                                        |
| chaos                   | 80.9 ms                                                      | 73.4 ms: 1.10x faster                                                       |
| html5lib                | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                       |
| gunicorn                | 973 us                                                       | 888 us: 1.09x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.65 ms: 1.09x faster                                                       |
| gc_traversal            | 3.85 ms                                                      | 3.54 ms: 1.09x faster                                                       |
| regex_compile           | 158 ms                                                       | 146 ms: 1.08x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.61 ms: 1.08x faster                                                       |
| deepcopy_memo           | 38.8 us                                                      | 36.4 us: 1.07x faster                                                       |
| tornado_http            | 122 ms                                                       | 114 ms: 1.06x faster                                                        |
| raytrace                | 317 ms                                                       | 298 ms: 1.06x faster                                                        |
| go                      | 164 ms                                                       | 155 ms: 1.06x faster                                                        |
| fannkuch                | 429 ms                                                       | 405 ms: 1.06x faster                                                        |
| nqueens                 | 103 ms                                                       | 97.1 ms: 1.06x faster                                                       |
| pycparser               | 1.32 sec                                                     | 1.25 sec: 1.06x faster                                                      |
| genshi_text             | 26.1 ms                                                      | 24.7 ms: 1.06x faster                                                       |
| genshi_xml              | 58.5 ms                                                      | 55.5 ms: 1.06x faster                                                       |
| logging_silent          | 101 ns                                                       | 95.5 ns: 1.06x faster                                                       |
| mako                    | 11.0 ms                                                      | 10.4 ms: 1.05x faster                                                       |
| sympy_expand            | 555 ms                                                       | 527 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.35 us: 1.05x faster                                                       |
| bench_thread_pool       | 1.01 ms                                                      | 966 us: 1.05x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.34 ms: 1.05x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.77 us: 1.04x faster                                                       |
| regex_v8                | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                       |
| xml_etree_process       | 56.5 ms                                                      | 54.1 ms: 1.04x faster                                                       |
| pyflate                 | 449 ms                                                       | 431 ms: 1.04x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.57 sec: 1.04x faster                                                      |
| coverage                | 84.8 ms                                                      | 81.5 ms: 1.04x faster                                                       |
| pylint                  | 515 ms                                                       | 496 ms: 1.04x faster                                                        |
| meteor_contest          | 131 ms                                                       | 126 ms: 1.04x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 65.9 ms: 1.04x faster                                                       |
| xml_etree_generate      | 80.5 ms                                                      | 77.6 ms: 1.04x faster                                                       |
| 2to3                    | 288 ms                                                       | 278 ms: 1.04x faster                                                        |
| sympy_str               | 337 ms                                                       | 326 ms: 1.04x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.64 ms: 1.03x faster                                                       |
| scimark_lu              | 115 ms                                                       | 111 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 761 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                       |
| generators              | 56.0 ms                                                      | 54.6 ms: 1.03x faster                                                       |
| scimark_sor             | 111 ms                                                       | 108 ms: 1.03x faster                                                        |
| docutils                | 2.86 sec                                                     | 2.79 sec: 1.02x faster                                                      |
| sympy_sum               | 185 ms                                                       | 181 ms: 1.02x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 618 ms: 1.02x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 313 us: 1.02x faster                                                        |
| logging_simple          | 7.19 us                                                      | 7.06 us: 1.02x faster                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.62 ms: 1.02x faster                                                       |
| comprehensions          | 24.6 us                                                      | 24.2 us: 1.02x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.02x faster                                                        |
| python_startup          | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| richards                | 48.3 ms                                                      | 47.6 ms: 1.02x faster                                                       |
| sympy_integrate         | 25.8 ms                                                      | 25.4 ms: 1.02x faster                                                       |
| unpickle_list           | 4.53 us                                                      | 4.47 us: 1.01x faster                                                       |
| mdp                     | 2.75 sec                                                     | 2.71 sec: 1.01x faster                                                      |
| unpack_sequence         | 45.6 ns                                                      | 45.0 ns: 1.01x faster                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 1.51 ms: 1.01x faster                                                       |
| float                   | 74.2 ms                                                      | 73.2 ms: 1.01x faster                                                       |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                                      |
| deepcopy                | 399 us                                                       | 394 us: 1.01x faster                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.90 ms: 1.01x faster                                                       |
| unpickle                | 13.4 us                                                      | 13.3 us: 1.01x faster                                                       |
| asyncio_tcp             | 753 ms                                                       | 747 ms: 1.01x faster                                                        |
| chameleon               | 7.67 ms                                                      | 7.62 ms: 1.01x faster                                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 67.8 ms: 1.01x faster                                                       |
| pathlib                 | 19.1 ms                                                      | 19.0 ms: 1.00x faster                                                       |
| coroutines              | 27.6 ms                                                      | 27.4 ms: 1.00x faster                                                       |
| async_tree_cpu_io_mixed | 749 ms                                                       | 756 ms: 1.01x slower                                                        |
| scimark_fft             | 285 ms                                                       | 288 ms: 1.01x slower                                                        |
| async_generators        | 316 ms                                                       | 321 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.54 us: 1.02x slower                                                       |
| regex_dna               | 227 ms                                                       | 232 ms: 1.02x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 96.1 ms: 1.03x slower                                                       |
| thrift                  | 925 us                                                       | 953 us: 1.03x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 31.9 us: 1.04x slower                                                       |
| pickle                  | 9.64 us                                                      | 10.1 us: 1.05x slower                                                       |
| nbody                   | 90.7 ms                                                      | 98.1 ms: 1.08x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (8): bench_mp_pool, async_tree_none, crypto_pyaes, dask, create_gc_cycles, pidigits, pickle_list, django_template
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
