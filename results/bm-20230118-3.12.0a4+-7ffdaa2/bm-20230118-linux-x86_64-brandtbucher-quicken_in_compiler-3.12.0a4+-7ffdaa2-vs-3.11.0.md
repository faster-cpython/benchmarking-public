
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 7ffdaa2
- commit date: 2023-01-18
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                       |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                      |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                       |
| tornado_http   | 96.3 ms                                                | 93.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.0 ms: 1.07x faster                                                       |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                        |
| nbody          | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                       |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                       |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.45 ms: 1.33x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.16x faster                                                        |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 280 us: 1.09x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                       |
| pickle_list          | 4.11 us                                                | 4.04 us: 1.02x faster                                                       |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.11 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (2): pickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.39 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                       |
| genshi_text    | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                       |
| mako           | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 489 ms: 1.88x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.45 ms: 1.33x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.16x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.93 ms: 1.14x faster                                                       |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.13x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.28 ms: 1.12x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                       |
| scimark_fft             | 328 ms                                                 | 296 ms: 1.11x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 992 us: 1.11x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                       |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| logging_silent          | 101 ns                                                 | 92.1 ns: 1.10x faster                                                       |
| nqueens                 | 83.4 ms                                                | 76.3 ms: 1.09x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 280 us: 1.09x faster                                                        |
| richards                | 45.7 ms                                                | 42.1 ms: 1.08x faster                                                       |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                       |
| sympy_str               | 290 ms                                                 | 269 ms: 1.08x faster                                                        |
| json                    | 4.94 ms                                                | 4.58 ms: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| chaos                   | 69.2 ms                                                | 64.4 ms: 1.07x faster                                                       |
| float                   | 77.2 ms                                                | 72.0 ms: 1.07x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.5 us: 1.07x faster                                                       |
| hexiom                  | 6.37 ms                                                | 5.95 ms: 1.07x faster                                                       |
| pyflate                 | 418 ms                                                 | 391 ms: 1.07x faster                                                        |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                       |
| genshi_text             | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                       |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                        |
| spectral_norm           | 100 ms                                                 | 94.4 ms: 1.06x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                      |
| gc_traversal            | 4.02 ms                                                | 3.81 ms: 1.06x faster                                                       |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 780 us: 1.05x faster                                                        |
| coverage                | 100 ms                                                 | 95.3 ms: 1.05x faster                                                       |
| logging_format          | 6.68 us                                                | 6.37 us: 1.05x faster                                                       |
| async_generators        | 368 ms                                                 | 351 ms: 1.05x faster                                                        |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                                       |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                                        |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                                       |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                        |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                        |
| coroutines              | 25.5 ms                                                | 24.6 ms: 1.04x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                      |
| mako                    | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                       |
| telco                   | 6.58 ms                                                | 6.37 ms: 1.03x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                       |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.1 ms                                                | 66.0 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                       |
| tornado_http            | 96.3 ms                                                | 93.9 ms: 1.03x faster                                                       |
| dulwich_log             | 63.7 ms                                                | 62.1 ms: 1.02x faster                                                       |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.2 ms: 1.02x faster                                                       |
| pickle_list             | 4.11 us                                                | 4.04 us: 1.02x faster                                                       |
| thrift                  | 756 us                                                 | 747 us: 1.01x faster                                                        |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 696 ms: 1.01x faster                                                        |
| pickle_dict             | 31.1 us                                                | 31.0 us: 1.01x faster                                                       |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                                       |
| nbody                   | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                       |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                                      |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.57 us: 1.02x slower                                                       |
| generators              | 73.5 ms                                                | 75.0 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 755 ms: 1.02x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                       |
| unpack_sequence         | 43.1 ns                                                | 44.3 ns: 1.03x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                       |
| async_tree_memoization  | 627 ms                                                 | 653 ms: 1.04x slower                                                        |
| unpickle_list           | 4.91 us                                                | 5.11 us: 1.04x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.39 ms: 1.06x slower                                                       |
| dask                    | 360 ms                                                 | 492 ms: 1.37x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (7): django_template, async_tree_none, bench_mp_pool, pickle, sqlglot_parse, xml_etree_process, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-7ffdaa2/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
