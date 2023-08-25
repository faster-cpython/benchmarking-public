
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.02x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 280 ms: 1.03x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.42 ms: 1.03x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                       |
| html5lib       | 72.9 ms                                                      | 67.3 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 73.6 ms: 1.01x faster                                                        |
| nbody          | 90.7 ms                                                      | 93.5 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                                         |
| regex_v8       | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.3 us: 1.18x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 208 us: 1.15x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 138 ms: 1.14x faster                                                         |
| xml_etree_process    | 56.5 ms                                                      | 55.2 ms: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 102 ms: 1.02x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 315 us: 1.01x faster                                                         |
| xml_etree_generate   | 80.5 ms                                                      | 79.5 ms: 1.01x faster                                                        |
| pickle_list          | 3.83 us                                                      | 3.88 us: 1.02x slower                                                        |
| pickle               | 9.64 us                                                      | 9.96 us: 1.03x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 32.3 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 7.85 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                        |
| genshi_xml      | 58.5 ms                                                      | 55.4 ms: 1.06x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 26.3 ms: 1.01x slower                                                        |
| django_template | 40.2 ms                                                      | 41.0 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                        |
| mypy2                   | 451 ms                                                       | 374 ms: 1.21x faster                                                         |
| json_loads              | 28.7 us                                                      | 24.3 us: 1.18x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 208 us: 1.15x faster                                                         |
| xml_etree_parse         | 158 ms                                                       | 138 ms: 1.14x faster                                                         |
| json                    | 5.65 ms                                                      | 5.07 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.65 ms: 1.11x faster                                                        |
| aiohttp                 | 985 us                                                       | 898 us: 1.10x faster                                                         |
| gunicorn                | 973 us                                                       | 889 us: 1.09x faster                                                         |
| deltablue               | 4.00 ms                                                      | 3.67 ms: 1.09x faster                                                        |
| html5lib                | 72.9 ms                                                      | 67.3 ms: 1.08x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                        |
| chaos                   | 80.9 ms                                                      | 75.3 ms: 1.07x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.61 ms: 1.07x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.65 us: 1.06x faster                                                        |
| deepcopy_memo           | 38.8 us                                                      | 36.6 us: 1.06x faster                                                        |
| raytrace                | 317 ms                                                       | 299 ms: 1.06x faster                                                         |
| genshi_xml              | 58.5 ms                                                      | 55.4 ms: 1.06x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 957 us: 1.06x faster                                                         |
| regex_compile           | 158 ms                                                       | 150 ms: 1.05x faster                                                         |
| thrift                  | 925 us                                                       | 880 us: 1.05x faster                                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.35 us: 1.05x faster                                                        |
| bench_mp_pool           | 4.62 ms                                                      | 4.42 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 122 ms: 1.03x faster                                                         |
| chameleon               | 7.67 ms                                                      | 7.42 ms: 1.03x faster                                                        |
| fannkuch                | 429 ms                                                       | 416 ms: 1.03x faster                                                         |
| nqueens                 | 103 ms                                                       | 99.6 ms: 1.03x faster                                                        |
| deepcopy                | 399 us                                                       | 388 us: 1.03x faster                                                         |
| docutils                | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                       |
| 2to3                    | 288 ms                                                       | 280 ms: 1.03x faster                                                         |
| go                      | 164 ms                                                       | 159 ms: 1.03x faster                                                         |
| meteor_contest          | 131 ms                                                       | 127 ms: 1.03x faster                                                         |
| async_tree_memoization  | 630 ms                                                       | 614 ms: 1.03x faster                                                         |
| scimark_sor             | 111 ms                                                       | 109 ms: 1.02x faster                                                         |
| xml_etree_process       | 56.5 ms                                                      | 55.2 ms: 1.02x faster                                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 58.5 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 102 ms: 1.02x faster                                                         |
| telco                   | 6.86 ms                                                      | 6.74 ms: 1.02x faster                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.89 ms: 1.02x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 67.4 ms: 1.02x faster                                                        |
| logging_simple          | 7.19 us                                                      | 7.08 us: 1.02x faster                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                                       |
| richards                | 48.3 ms                                                      | 47.6 ms: 1.01x faster                                                        |
| sympy_expand            | 555 ms                                                       | 547 ms: 1.01x faster                                                         |
| pickle_pure_python      | 319 us                                                       | 315 us: 1.01x faster                                                         |
| xml_etree_generate      | 80.5 ms                                                      | 79.5 ms: 1.01x faster                                                        |
| logging_silent          | 101 ns                                                       | 99.6 ns: 1.01x faster                                                        |
| asyncio_tcp             | 753 ms                                                       | 744 ms: 1.01x faster                                                         |
| regex_v8                | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                                        |
| scimark_fft             | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| float                   | 74.2 ms                                                      | 73.6 ms: 1.01x faster                                                        |
| scimark_lu              | 115 ms                                                       | 114 ms: 1.01x faster                                                         |
| sympy_integrate         | 25.8 ms                                                      | 25.6 ms: 1.01x faster                                                        |
| async_tree_none         | 519 ms                                                       | 515 ms: 1.01x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 7.08 ms: 1.01x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.62 sec: 1.01x faster                                                       |
| sympy_str               | 337 ms                                                       | 335 ms: 1.01x faster                                                         |
| sympy_sum               | 185 ms                                                       | 185 ms: 1.00x slower                                                         |
| python_startup          | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 788 ms: 1.01x slower                                                         |
| genshi_text             | 26.1 ms                                                      | 26.3 ms: 1.01x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 7.85 ms: 1.01x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 94.6 ms: 1.01x slower                                                        |
| dask                    | 410 ms                                                       | 416 ms: 1.01x slower                                                         |
| mdp                     | 2.75 sec                                                     | 2.78 sec: 1.01x slower                                                       |
| pickle_list             | 3.83 us                                                      | 3.88 us: 1.02x slower                                                        |
| django_template         | 40.2 ms                                                      | 41.0 ms: 1.02x slower                                                        |
| coverage                | 84.8 ms                                                      | 86.9 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.56 us: 1.03x slower                                                        |
| nbody                   | 90.7 ms                                                      | 93.5 ms: 1.03x slower                                                        |
| pickle                  | 9.64 us                                                      | 9.96 us: 1.03x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 32.3 us: 1.05x slower                                                        |
| async_generators        | 316 ms                                                       | 333 ms: 1.05x slower                                                         |
| generators              | 56.0 ms                                                      | 60.8 ms: 1.09x slower                                                        |
| comprehensions          | 24.6 us                                                      | 27.5 us: 1.12x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (14): create_gc_cycles, pycparser, tornado_http, sqlglot_parse, unpickle, unpack_sequence, async_tree_cpu_io_mixed, pidigits, coroutines, regex_dna, crypto_pyaes, scimark_monte_carlo, pyflate, unpickle_list
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
