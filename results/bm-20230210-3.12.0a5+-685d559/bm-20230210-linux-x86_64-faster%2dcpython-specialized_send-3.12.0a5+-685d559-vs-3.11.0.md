
# Results vs. 3.11.0

- fork: faster-cpython
- ref: specialized_send
- machine: linux-x86_64
- commit hash: 685d559
- commit date: 2023-02-10
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                        |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| tornado_http   | 96.3 ms                                                | 95.1 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.9 ms: 1.05x faster                                                        |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                        |
| regex_compile  | 138 ms                                                 | 131 ms: 1.06x faster                                                         |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                        |
| regex_dna      | 204 ms                                                 | 211 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                         |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                         |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                                        |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (3): pickle, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 48.1 ms: 1.08x faster                                                        |
| genshi_text    | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                        |
| mako           | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.1 ms: 2.36x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 495 ms: 1.86x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                        |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.87 ms: 1.16x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                         |
| coroutines              | 25.5 ms                                                | 22.3 ms: 1.15x faster                                                        |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                        |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.09x faster                                                         |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                         |
| logging_silent          | 101 ns                                                 | 94.0 ns: 1.08x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| genshi_xml              | 51.8 ms                                                | 48.1 ms: 1.08x faster                                                        |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                         |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                                        |
| deepcopy_memo           | 37.0 us                                                | 34.5 us: 1.07x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                       |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                                        |
| richards                | 45.7 ms                                                | 42.9 ms: 1.06x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.67 us: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                        |
| regex_compile           | 138 ms                                                 | 131 ms: 1.06x faster                                                         |
| sympy_sum               | 167 ms                                                 | 158 ms: 1.06x faster                                                         |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                                         |
| html5lib                | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                        |
| scimark_fft             | 328 ms                                                 | 313 ms: 1.05x faster                                                         |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                         |
| chaos                   | 69.2 ms                                                | 66.1 ms: 1.05x faster                                                        |
| float                   | 77.2 ms                                                | 73.9 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                         |
| spectral_norm           | 100 ms                                                 | 95.8 ms: 1.04x faster                                                        |
| telco                   | 6.58 ms                                                | 6.32 ms: 1.04x faster                                                        |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                         |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                         |
| bench_thread_pool       | 819 us                                                 | 789 us: 1.04x faster                                                         |
| hexiom                  | 6.37 ms                                                | 6.14 ms: 1.04x faster                                                        |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                        |
| pyflate                 | 418 ms                                                 | 403 ms: 1.04x faster                                                         |
| mako                    | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                       |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                       |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                                         |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 66.1 ms: 1.03x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.91 ms: 1.03x faster                                                        |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                         |
| nqueens                 | 83.4 ms                                                | 81.2 ms: 1.03x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                         |
| coverage                | 100 ms                                                 | 98.1 ms: 1.02x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 690 ms: 1.02x faster                                                         |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                                        |
| tornado_http            | 96.3 ms                                                | 95.1 ms: 1.01x faster                                                        |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.7 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                                        |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 63.4 ms: 1.00x faster                                                        |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                         |
| chameleon               | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                        |
| unpack_sequence         | 43.1 ns                                                | 43.4 ns: 1.01x slower                                                        |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                        |
| thrift                  | 756 us                                                 | 766 us: 1.01x slower                                                         |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 750 ms: 1.01x slower                                                         |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                        |
| regex_dna               | 204 ms                                                 | 211 ms: 1.03x slower                                                         |
| xml_etree_process       | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                        |
| mdp                     | 2.62 sec                                               | 2.75 sec: 1.05x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                        |
| async_generators        | 368 ms                                                 | 410 ms: 1.11x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (11): meteor_contest, sqlalchemy_declarative, async_tree_none, django_template, nbody, pickle, bench_mp_pool, pickle_list, djangocms, unpickle, async_tree_memoization
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
