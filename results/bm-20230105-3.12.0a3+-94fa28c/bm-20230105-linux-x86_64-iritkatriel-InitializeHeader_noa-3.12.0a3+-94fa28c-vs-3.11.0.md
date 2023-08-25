
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader_noa
- machine: linux-x86_64
- commit hash: 94fa28c
- commit date: 2023-01-05
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.15 ms: 1.05x faster                                                       |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                      |
| html5lib       | 64.5 ms                                                | 60.0 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.0 ms: 1.06x faster                                                       |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| nbody          | 93.1 ms                                                | 95.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                       |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                                        |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.28 ms: 1.36x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                        |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.06x faster                                                        |
| unpickle             | 13.7 us                                                | 12.9 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| pickle_list          | 4.11 us                                                | 4.04 us: 1.02x faster                                                       |
| xml_etree_process    | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                       |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.00x faster                                                       |
| xml_etree_generate   | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                       |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.49 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.08 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.9 ms: 1.10x faster                                                       |
| mako           | 10.1 ms                                                | 9.38 ms: 1.08x faster                                                       |
| genshi_text    | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.28 ms: 1.36x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                        |
| json_loads              | 26.5 us                                                | 23.7 us: 1.12x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.29 ms: 1.11x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 46.9 ms: 1.10x faster                                                       |
| logging_silent          | 101 ns                                                 | 92.5 ns: 1.09x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 33.9 us: 1.09x faster                                                       |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                                        |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                                       |
| mako                    | 10.1 ms                                                | 9.38 ms: 1.08x faster                                                       |
| html5lib                | 64.5 ms                                                | 60.0 ms: 1.08x faster                                                       |
| json                    | 4.94 ms                                                | 4.60 ms: 1.07x faster                                                       |
| nqueens                 | 83.4 ms                                                | 77.8 ms: 1.07x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                        |
| pyflate                 | 418 ms                                                 | 392 ms: 1.07x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.06x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 64.1 ms: 1.06x faster                                                       |
| genshi_text             | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                       |
| unpickle                | 13.7 us                                                | 12.9 us: 1.06x faster                                                       |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                                        |
| float                   | 77.2 ms                                                | 73.0 ms: 1.06x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.15 ms: 1.05x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 779 us: 1.05x faster                                                        |
| unpack_sequence         | 43.1 ns                                                | 41.2 ns: 1.05x faster                                                       |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                      |
| async_generators        | 368 ms                                                 | 352 ms: 1.05x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 671 ms: 1.05x faster                                                        |
| telco                   | 6.58 ms                                                | 6.30 ms: 1.04x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.04x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 50.9 ms: 1.04x faster                                                       |
| logging_format          | 6.68 us                                                | 6.42 us: 1.04x faster                                                       |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                        |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                        |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                        |
| raytrace                | 297 ms                                                 | 287 ms: 1.04x faster                                                        |
| go                      | 140 ms                                                 | 135 ms: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                       |
| scimark_fft             | 328 ms                                                 | 318 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.36 ms: 1.03x faster                                                       |
| spectral_norm           | 100 ms                                                 | 97.1 ms: 1.03x faster                                                       |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                        |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                        |
| chaos                   | 69.2 ms                                                | 67.4 ms: 1.03x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                        |
| pickle_list             | 4.11 us                                                | 4.04 us: 1.02x faster                                                       |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.01x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                       |
| coverage                | 100 ms                                                 | 98.8 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                       |
| thrift                  | 756 us                                                 | 750 us: 1.01x faster                                                        |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                       |
| coroutines              | 25.5 ms                                                | 25.4 ms: 1.01x faster                                                       |
| python_startup          | 8.52 ms                                                | 8.49 ms: 1.00x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 74.4 ms: 1.00x faster                                                       |
| pickle_dict             | 31.1 us                                                | 31.0 us: 1.00x faster                                                       |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| xml_etree_generate      | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                       |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.08 ms: 1.01x slower                                                       |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 755 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| nbody                   | 93.1 ms                                                | 95.7 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                       |
| async_tree_memoization  | 627 ms                                                 | 647 ms: 1.03x slower                                                        |
| mdp                     | 2.62 sec                                               | 2.72 sec: 1.04x slower                                                      |
| generators              | 73.5 ms                                                | 76.8 ms: 1.04x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (8): deepcopy_reduce, djangocms, sqlglot_transpile, bench_mp_pool, scimark_lu, pickle, async_tree_none, django_template
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230105-3.12.0a3+-94fa28c/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
