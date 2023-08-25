
# Results vs. 3.11.0

- fork: faster-cpython
- ref: check_refcnt_in_bina
- machine: linux-x86_64
- commit hash: c29d369
- commit date: 2023-02-27
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                                             |
| chameleon      | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                            |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                           |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                            |
| tornado_http   | 96.3 ms                                                | 94.3 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                            |
| nbody          | 93.1 ms                                                | 89.7 ms: 1.04x faster                                                            |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.36 ms: 1.19x faster                                                            |
| regex_compile  | 138 ms                                                 | 132 ms: 1.05x faster                                                             |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                            |
| regex_dna      | 204 ms                                                 | 209 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                            |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.16x faster                                                             |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                            |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 98.7 ms: 1.05x faster                                                            |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                                            |
| xml_etree_process    | 53.9 ms                                                | 54.9 ms: 1.02x slower                                                            |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                            |
| xml_etree_generate   | 76.2 ms                                                | 79.7 ms: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (3): unpickle, pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.98 ms: 1.05x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.8 ms: 1.11x faster                                                            |
| genshi_text     | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                            |
| mako            | 10.1 ms                                                | 9.92 ms: 1.02x faster                                                            |
| django_template | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.7 ms: 2.47x faster                                                            |
| asyncio_tcp             | 922 ms                                                 | 503 ms: 1.83x faster                                                             |
| json_dumps              | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                            |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.36 ms: 1.19x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.11 ms: 1.18x faster                                                            |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.16x faster                                                             |
| scimark_sor             | 118 ms                                                 | 103 ms: 1.15x faster                                                             |
| spectral_norm           | 100 ms                                                 | 87.7 ms: 1.14x faster                                                            |
| coroutines              | 25.5 ms                                                | 22.7 ms: 1.12x faster                                                            |
| richards                | 45.7 ms                                                | 40.9 ms: 1.12x faster                                                            |
| genshi_xml              | 51.8 ms                                                | 46.8 ms: 1.11x faster                                                            |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                            |
| scimark_fft             | 328 ms                                                 | 300 ms: 1.10x faster                                                             |
| logging_silent          | 101 ns                                                 | 92.6 ns: 1.09x faster                                                            |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                            |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.09x faster                                                            |
| json                    | 4.94 ms                                                | 4.57 ms: 1.08x faster                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.17 ms: 1.08x faster                                                            |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                                           |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                            |
| fannkuch                | 388 ms                                                 | 361 ms: 1.07x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                            |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                                             |
| nqueens                 | 83.4 ms                                                | 78.6 ms: 1.06x faster                                                            |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                                            |
| xml_etree_iterparse     | 104 ms                                                 | 98.7 ms: 1.05x faster                                                            |
| sqlglot_optimize        | 53.1 ms                                                | 50.5 ms: 1.05x faster                                                            |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                            |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                                            |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                            |
| regex_compile           | 138 ms                                                 | 132 ms: 1.05x faster                                                             |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                                             |
| bench_thread_pool       | 819 us                                                 | 784 us: 1.05x faster                                                             |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                             |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                                             |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                             |
| logging_simple          | 6.03 us                                                | 5.81 us: 1.04x faster                                                            |
| nbody                   | 93.1 ms                                                | 89.7 ms: 1.04x faster                                                            |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                           |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                           |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                            |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                            |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                                             |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                             |
| coverage                | 100 ms                                                 | 97.5 ms: 1.03x faster                                                            |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                                             |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                            |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                                           |
| tornado_http            | 96.3 ms                                                | 94.3 ms: 1.02x faster                                                            |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                             |
| mako                    | 10.1 ms                                                | 9.92 ms: 1.02x faster                                                            |
| crypto_pyaes            | 74.7 ms                                                | 73.5 ms: 1.02x faster                                                            |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                                            |
| chaos                   | 69.2 ms                                                | 68.4 ms: 1.01x faster                                                            |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 732 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                            |
| telco                   | 6.58 ms                                                | 6.53 ms: 1.01x faster                                                            |
| dulwich_log             | 63.7 ms                                                | 63.2 ms: 1.01x faster                                                            |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                           |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                             |
| chameleon               | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                            |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                            |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                            |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                                            |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                            |
| xml_etree_process       | 53.9 ms                                                | 54.9 ms: 1.02x slower                                                            |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                            |
| regex_dna               | 204 ms                                                 | 209 ms: 1.03x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 44.3 ns: 1.03x slower                                                            |
| async_tree_memoization  | 627 ms                                                 | 645 ms: 1.03x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.03x slower                                                            |
| xml_etree_generate      | 76.2 ms                                                | 79.7 ms: 1.05x slower                                                            |
| python_startup          | 8.52 ms                                                | 8.98 ms: 1.05x slower                                                            |
| python_startup_no_site  | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                            |
| async_generators        | 368 ms                                                 | 410 ms: 1.11x slower                                                             |
| dask                    | 360 ms                                                 | 498 ms: 1.38x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (11): unpickle, djangocms, thrift, scimark_monte_carlo, bench_mp_pool, sympy_sum, sqlglot_transpile, pickle_list, sqlalchemy_imperative, sqlalchemy_declarative, unpickle_list
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
