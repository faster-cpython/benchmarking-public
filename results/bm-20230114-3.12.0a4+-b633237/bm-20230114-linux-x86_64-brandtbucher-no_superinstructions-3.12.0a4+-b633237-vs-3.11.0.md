
# Results vs. 3.11.0

- fork: brandtbucher
- ref: no_superinstructions
- machine: linux-x86_64
- commit hash: b633237
- commit date: 2023-01-14
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.01x faster                                                         |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                       |
| html5lib       | 64.5 ms                                                | 60.6 ms: 1.06x faster                                                        |
| tornado_http   | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                        |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                         |
| nbody          | 93.1 ms                                                | 94.2 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                        |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                         |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.38 ms: 1.34x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.14x faster                                                         |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                         |
| unpickle             | 13.7 us                                                | 12.9 us: 1.06x faster                                                        |
| pickle_dict          | 31.1 us                                                | 29.5 us: 1.06x faster                                                        |
| pickle_list          | 4.11 us                                                | 4.02 us: 1.02x faster                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.0 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (3): pickle, xml_etree_process, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.74 ms: 1.03x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.30 ms: 1.05x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                        |
| genshi_text    | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                        |
| mako           | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.38 ms: 1.34x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.50 ms: 1.15x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.14x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                        |
| logging_silent          | 101 ns                                                 | 91.7 ns: 1.10x faster                                                        |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                         |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.13 ms: 1.09x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                        |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                         |
| html5lib                | 64.5 ms                                                | 60.6 ms: 1.06x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                       |
| unpickle                | 13.7 us                                                | 12.9 us: 1.06x faster                                                        |
| pickle_dict             | 31.1 us                                                | 29.5 us: 1.06x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                       |
| pyflate                 | 418 ms                                                 | 398 ms: 1.05x faster                                                         |
| json                    | 4.94 ms                                                | 4.71 ms: 1.05x faster                                                        |
| nqueens                 | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                        |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                        |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 784 us: 1.04x faster                                                         |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                        |
| coverage                | 100 ms                                                 | 96.2 ms: 1.04x faster                                                        |
| richards                | 45.7 ms                                                | 44.0 ms: 1.04x faster                                                        |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                         |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                         |
| scimark_fft             | 328 ms                                                 | 317 ms: 1.04x faster                                                         |
| logging_simple          | 6.03 us                                                | 5.82 us: 1.04x faster                                                        |
| fannkuch                | 388 ms                                                 | 374 ms: 1.04x faster                                                         |
| async_generators        | 368 ms                                                 | 356 ms: 1.04x faster                                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                                        |
| hexiom                  | 6.37 ms                                                | 6.18 ms: 1.03x faster                                                        |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                                         |
| raytrace                | 297 ms                                                 | 288 ms: 1.03x faster                                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 66.1 ms: 1.03x faster                                                        |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                         |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                         |
| logging_format          | 6.68 us                                                | 6.52 us: 1.02x faster                                                        |
| deepcopy_memo           | 37.0 us                                                | 36.1 us: 1.02x faster                                                        |
| pickle_list             | 4.11 us                                                | 4.02 us: 1.02x faster                                                        |
| telco                   | 6.58 ms                                                | 6.43 ms: 1.02x faster                                                        |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.4 ms: 1.02x faster                                                        |
| spectral_norm           | 100 ms                                                 | 98.0 ms: 1.02x faster                                                        |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                         |
| mako                    | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| coroutines              | 25.5 ms                                                | 25.0 ms: 1.02x faster                                                        |
| deepcopy                | 342 us                                                 | 336 us: 1.02x faster                                                         |
| tornado_http            | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                        |
| 2to3                    | 259 ms                                                 | 255 ms: 1.01x faster                                                         |
| thrift                  | 756 us                                                 | 750 us: 1.01x faster                                                         |
| sympy_str               | 290 ms                                                 | 288 ms: 1.01x faster                                                         |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                       |
| xml_etree_generate      | 76.2 ms                                                | 77.0 ms: 1.01x slower                                                        |
| nbody                   | 93.1 ms                                                | 94.2 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed | 739 ms                                                 | 749 ms: 1.01x slower                                                         |
| generators              | 73.5 ms                                                | 74.6 ms: 1.01x slower                                                        |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                                         |
| chaos                   | 69.2 ms                                                | 70.4 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.74 ms: 1.03x slower                                                        |
| crypto_pyaes            | 74.7 ms                                                | 77.7 ms: 1.04x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.30 ms: 1.05x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 658 ms: 1.05x slower                                                         |
| unpack_sequence         | 43.1 ns                                                | 49.0 ns: 1.14x slower                                                        |
| dask                    | 360 ms                                                 | 507 ms: 1.41x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (12): pickle, xml_etree_process, bench_mp_pool, unpickle_list, sqlglot_transpile, pathlib, sqlglot_parse, chameleon, django_template, deepcopy_reduce, async_tree_none, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230114-3.12.0a4+-b633237/bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
