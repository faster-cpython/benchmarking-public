
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.02x faster \*
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.29 ms: 1.03x faster                                               |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                              |
| html5lib       | 64.5 ms                                                | 61.9 ms: 1.04x faster                                               |
| tornado_http   | 96.3 ms                                                | 95.0 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.8 ms: 1.06x faster                                               |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                |
| nbody          | 93.1 ms                                                | 97.9 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                               |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                               |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.35 ms: 1.35x faster                                               |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                |
| json_loads           | 26.5 us                                                | 24.6 us: 1.08x faster                                               |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_dict          | 31.1 us                                                | 30.5 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 53.2 ms: 1.01x faster                                               |
| pickle_list          | 4.11 us                                                | 4.09 us: 1.01x faster                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.7 ms: 1.02x slower                                               |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.94 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.47 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.0 ms: 1.10x faster                                               |
| genshi_text    | 21.6 ms                                                | 20.2 ms: 1.07x faster                                               |
| mako           | 10.1 ms                                                | 9.82 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 496 ms: 1.86x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.35 ms: 1.35x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                               |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                               |
| logging_silent          | 101 ns                                                 | 91.3 ns: 1.11x faster                                               |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                               |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                               |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                |
| json_loads              | 26.5 us                                                | 24.6 us: 1.08x faster                                               |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| genshi_text             | 21.6 ms                                                | 20.2 ms: 1.07x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                               |
| logging_format          | 6.68 us                                                | 6.29 us: 1.06x faster                                               |
| float                   | 77.2 ms                                                | 72.8 ms: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                               |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                              |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.06x faster                                               |
| coverage                | 100 ms                                                 | 95.1 ms: 1.05x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.82 ms: 1.05x faster                                               |
| nqueens                 | 83.4 ms                                                | 79.3 ms: 1.05x faster                                               |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                                |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                               |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.04x faster                                              |
| richards                | 45.7 ms                                                | 43.8 ms: 1.04x faster                                               |
| html5lib                | 64.5 ms                                                | 61.9 ms: 1.04x faster                                               |
| chaos                   | 69.2 ms                                                | 66.4 ms: 1.04x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 678 ms: 1.03x faster                                                |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                |
| telco                   | 6.58 ms                                                | 6.37 ms: 1.03x faster                                               |
| chameleon               | 6.47 ms                                                | 6.29 ms: 1.03x faster                                               |
| thrift                  | 756 us                                                 | 735 us: 1.03x faster                                                |
| mako                    | 10.1 ms                                                | 9.82 ms: 1.03x faster                                               |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                |
| bench_thread_pool       | 819 us                                                 | 800 us: 1.02x faster                                                |
| pickle_dict             | 31.1 us                                                | 30.5 us: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| raytrace                | 297 ms                                                 | 292 ms: 1.02x faster                                                |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                               |
| tornado_http            | 96.3 ms                                                | 95.0 ms: 1.01x faster                                               |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                |
| xml_etree_process       | 53.9 ms                                                | 53.2 ms: 1.01x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 67.6 ms: 1.01x faster                                               |
| pickle_list             | 4.11 us                                                | 4.09 us: 1.01x faster                                               |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                               |
| dulwich_log             | 63.7 ms                                                | 64.3 ms: 1.01x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                              |
| async_generators        | 368 ms                                                 | 372 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 739 ms                                                 | 752 ms: 1.02x slower                                                |
| xml_etree_generate      | 76.2 ms                                                | 77.7 ms: 1.02x slower                                               |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                               |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                |
| mdp                     | 2.62 sec                                               | 2.72 sec: 1.04x slower                                              |
| pathlib                 | 18.2 ms                                                | 19.0 ms: 1.04x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.78 ms: 1.04x slower                                               |
| python_startup          | 8.52 ms                                                | 8.94 ms: 1.05x slower                                               |
| nbody                   | 93.1 ms                                                | 97.9 ms: 1.05x slower                                               |
| sqlglot_parse           | 1.40 ms                                                | 1.48 ms: 1.05x slower                                               |
| scimark_sor             | 118 ms                                                 | 125 ms: 1.06x slower                                                |
| sqlite_synth            | 2.52 us                                                | 2.70 us: 1.07x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.47 ms: 1.08x slower                                               |
| generators              | 73.5 ms                                                | 81.0 ms: 1.10x slower                                               |
| pyflate                 | 418 ms                                                 | 467 ms: 1.12x slower                                                |
| crypto_pyaes            | 74.7 ms                                                | 89.5 ms: 1.20x slower                                               |
| scimark_fft             | 328 ms                                                 | 397 ms: 1.21x slower                                                |
| spectral_norm           | 100 ms                                                 | 141 ms: 1.41x slower                                                |
| dask                    | 360 ms                                                 | 526 ms: 1.46x slower                                                |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (10): unpickle, async_tree_none, scimark_sparse_mat_mult, unpack_sequence, unpickle_list, coroutines, bench_mp_pool, django_template, djangocms, async_tree_memoization
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: mypy


# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
