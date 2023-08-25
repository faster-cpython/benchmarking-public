
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 9595e01
- commit date: 2023-02-07
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                             |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                            |
| html5lib       | 64.5 ms                                                | 61.1 ms: 1.06x faster                                             |
| tornado_http   | 96.3 ms                                                | 93.7 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.7 ms: 1.05x faster                                             |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                              |
| nbody          | 93.1 ms                                                | 96.0 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.62 ms: 1.10x faster                                             |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                              |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                             |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.53 ms: 1.32x faster                                             |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                              |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                             |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                              |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                             |
| xml_etree_process    | 53.9 ms                                                | 53.2 ms: 1.01x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| pickle_list          | 4.11 us                                                | 4.14 us: 1.01x slower                                             |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                             |
| xml_etree_generate   | 76.2 ms                                                | 77.4 ms: 1.02x slower                                             |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                             |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.91 ms: 1.05x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 6.47 ms: 1.08x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.5 ms: 1.11x faster                                             |
| genshi_text    | 21.6 ms                                                | 20.7 ms: 1.04x faster                                             |
| mako           | 10.1 ms                                                | 9.92 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 492 ms: 1.87x faster                                              |
| json_dumps              | 12.6 ms                                                | 9.53 ms: 1.32x faster                                             |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                              |
| deltablue               | 3.67 ms                                                | 3.16 ms: 1.16x faster                                             |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.04 ms: 1.11x faster                                             |
| genshi_xml              | 51.8 ms                                                | 46.5 ms: 1.11x faster                                             |
| regex_effbot            | 3.99 ms                                                | 3.62 ms: 1.10x faster                                             |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                             |
| fannkuch                | 388 ms                                                 | 355 ms: 1.09x faster                                              |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                             |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                              |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                             |
| logging_silent          | 101 ns                                                 | 93.3 ns: 1.08x faster                                             |
| richards                | 45.7 ms                                                | 42.2 ms: 1.08x faster                                             |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                              |
| sympy_str               | 290 ms                                                 | 270 ms: 1.08x faster                                              |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                              |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                              |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                             |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                              |
| async_generators        | 368 ms                                                 | 347 ms: 1.06x faster                                              |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                             |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                              |
| deepcopy_memo           | 37.0 us                                                | 35.0 us: 1.06x faster                                             |
| html5lib                | 64.5 ms                                                | 61.1 ms: 1.06x faster                                             |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                              |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                            |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                             |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                              |
| spectral_norm           | 100 ms                                                 | 95.4 ms: 1.05x faster                                             |
| bench_thread_pool       | 819 us                                                 | 781 us: 1.05x faster                                              |
| float                   | 77.2 ms                                                | 73.7 ms: 1.05x faster                                             |
| coverage                | 100 ms                                                 | 95.6 ms: 1.05x faster                                             |
| chaos                   | 69.2 ms                                                | 66.1 ms: 1.05x faster                                             |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                              |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                             |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                             |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                            |
| unpack_sequence         | 43.1 ns                                                | 41.6 ns: 1.04x faster                                             |
| pyflate                 | 418 ms                                                 | 404 ms: 1.04x faster                                              |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| logging_format          | 6.68 us                                                | 6.48 us: 1.03x faster                                             |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                             |
| thrift                  | 756 us                                                 | 735 us: 1.03x faster                                              |
| nqueens                 | 83.4 ms                                                | 81.0 ms: 1.03x faster                                             |
| gc_traversal            | 4.02 ms                                                | 3.91 ms: 1.03x faster                                             |
| crypto_pyaes            | 74.7 ms                                                | 72.6 ms: 1.03x faster                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 66.2 ms: 1.03x faster                                             |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                              |
| tornado_http            | 96.3 ms                                                | 93.7 ms: 1.03x faster                                             |
| logging_simple          | 6.03 us                                                | 5.89 us: 1.03x faster                                             |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.02x faster                                            |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                              |
| telco                   | 6.58 ms                                                | 6.45 ms: 1.02x faster                                             |
| deepcopy                | 342 us                                                 | 336 us: 1.02x faster                                              |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                             |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                             |
| pprint_safe_repr        | 701 ms                                                 | 689 ms: 1.02x faster                                              |
| mako                    | 10.1 ms                                                | 9.92 ms: 1.02x faster                                             |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                             |
| xml_etree_process       | 53.9 ms                                                | 53.2 ms: 1.01x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                             |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                            |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                             |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                              |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                              |
| pickle_list             | 4.11 us                                                | 4.14 us: 1.01x slower                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                             |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                            |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.01x slower                                             |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.02x slower                                             |
| xml_etree_generate      | 76.2 ms                                                | 77.4 ms: 1.02x slower                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                             |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                             |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 757 ms: 1.02x slower                                              |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                             |
| generators              | 73.5 ms                                                | 75.7 ms: 1.03x slower                                             |
| nbody                   | 93.1 ms                                                | 96.0 ms: 1.03x slower                                             |
| async_tree_memoization  | 627 ms                                                 | 647 ms: 1.03x slower                                              |
| python_startup          | 8.52 ms                                                | 8.91 ms: 1.05x slower                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.47 ms: 1.08x slower                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (7): djangocms, async_tree_none, sqlalchemy_imperative, sqlalchemy_declarative, bench_mp_pool, django_template, meteor_contest
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
