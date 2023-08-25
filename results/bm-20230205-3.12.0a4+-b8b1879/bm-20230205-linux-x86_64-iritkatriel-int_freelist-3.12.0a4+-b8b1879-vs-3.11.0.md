
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b8b1879
- commit date: 2023-02-05
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.34 ms: 1.02x faster                                               |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| html5lib       | 64.5 ms                                                | 60.2 ms: 1.07x faster                                               |
| tornado_http   | 96.3 ms                                                | 94.3 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.9 ms: 1.06x faster                                               |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                |
| nbody          | 93.1 ms                                                | 99.5 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.62 ms: 1.10x faster                                               |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                               |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                               |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                |
| json_loads           | 26.5 us                                                | 23.5 us: 1.13x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| pickle_dict          | 31.1 us                                                | 30.1 us: 1.03x faster                                               |
| pickle_list          | 4.11 us                                                | 4.00 us: 1.03x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| unpickle_list        | 4.91 us                                                | 4.84 us: 1.01x faster                                               |
| pickle               | 10.1 us                                                | 9.98 us: 1.01x faster                                               |
| xml_etree_generate   | 76.2 ms                                                | 78.1 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.92 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.46 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.7 ms: 1.09x faster                                               |
| mako           | 10.1 ms                                                | 9.62 ms: 1.05x faster                                               |
| genshi_text    | 21.6 ms                                                | 21.2 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 493 ms: 1.87x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.92 ms: 1.15x faster                                               |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                               |
| json_loads              | 26.5 us                                                | 23.5 us: 1.13x faster                                               |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.62 ms: 1.10x faster                                               |
| aiohttp                 | 1.10 ms                                                | 999 us: 1.10x faster                                                |
| chaos                   | 69.2 ms                                                | 63.2 ms: 1.09x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                               |
| logging_silent          | 101 ns                                                 | 92.6 ns: 1.09x faster                                               |
| json                    | 4.94 ms                                                | 4.55 ms: 1.09x faster                                               |
| genshi_xml              | 51.8 ms                                                | 47.7 ms: 1.09x faster                                               |
| nqueens                 | 83.4 ms                                                | 77.0 ms: 1.08x faster                                               |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| html5lib                | 64.5 ms                                                | 60.2 ms: 1.07x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.76 ms: 1.07x faster                                               |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                |
| sympy_str               | 290 ms                                                 | 272 ms: 1.07x faster                                                |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                               |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| float                   | 77.2 ms                                                | 72.9 ms: 1.06x faster                                               |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                                |
| async_generators        | 368 ms                                                 | 349 ms: 1.05x faster                                                |
| spectral_norm           | 100 ms                                                 | 95.0 ms: 1.05x faster                                               |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                              |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                              |
| bench_thread_pool       | 819 us                                                 | 780 us: 1.05x faster                                                |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                |
| mako                    | 10.1 ms                                                | 9.62 ms: 1.05x faster                                               |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.05x faster                                              |
| logging_format          | 6.68 us                                                | 6.38 us: 1.05x faster                                               |
| logging_simple          | 6.03 us                                                | 5.76 us: 1.05x faster                                               |
| pyflate                 | 418 ms                                                 | 401 ms: 1.04x faster                                                |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| sqlglot_optimize        | 53.1 ms                                                | 51.3 ms: 1.04x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                              |
| raytrace                | 297 ms                                                 | 287 ms: 1.04x faster                                                |
| pickle_dict             | 31.1 us                                                | 30.1 us: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| pickle_list             | 4.11 us                                                | 4.00 us: 1.03x faster                                               |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.03x faster                                               |
| telco                   | 6.58 ms                                                | 6.42 ms: 1.03x faster                                               |
| coroutines              | 25.5 ms                                                | 24.9 ms: 1.03x faster                                               |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| tornado_http            | 96.3 ms                                                | 94.3 ms: 1.02x faster                                               |
| dulwich_log             | 63.7 ms                                                | 62.4 ms: 1.02x faster                                               |
| thrift                  | 756 us                                                 | 741 us: 1.02x faster                                                |
| chameleon               | 6.47 ms                                                | 6.34 ms: 1.02x faster                                               |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                               |
| deepcopy                | 342 us                                                 | 336 us: 1.02x faster                                                |
| unpickle_list           | 4.91 us                                                | 4.84 us: 1.01x faster                                               |
| coverage                | 100 ms                                                 | 98.9 ms: 1.01x faster                                               |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                               |
| pickle                  | 10.1 us                                                | 9.98 us: 1.01x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 67.7 ms: 1.00x faster                                               |
| crypto_pyaes            | 74.7 ms                                                | 75.2 ms: 1.01x slower                                               |
| sqlite_synth            | 2.52 us                                                | 2.55 us: 1.01x slower                                               |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                               |
| deepcopy_reduce         | 2.94 us                                                | 3.01 us: 1.02x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 78.1 ms: 1.02x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 762 ms: 1.03x slower                                                |
| generators              | 73.5 ms                                                | 76.8 ms: 1.04x slower                                               |
| python_startup          | 8.52 ms                                                | 8.92 ms: 1.05x slower                                               |
| regex_dna               | 204 ms                                                 | 214 ms: 1.05x slower                                                |
| async_tree_memoization  | 627 ms                                                 | 659 ms: 1.05x slower                                                |
| nbody                   | 93.1 ms                                                | 99.5 ms: 1.07x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.46 ms: 1.08x slower                                               |
| dask                    | 360 ms                                                 | 497 ms: 1.38x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (9): scimark_lu, django_template, xml_etree_process, bench_mp_pool, sqlglot_transpile, async_tree_none, unpack_sequence, sqlglot_parse, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230205-3.12.0a4+-b8b1879/bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
