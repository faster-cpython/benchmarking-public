
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: immortalize_empty_ke
- machine: linux-x86_64
- commit hash: e472d94
- commit date: 2023-05-06
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 270 ms: 1.05x slower                                                              |
| docutils       | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                            |
| tornado_http   | 96.7 ms                                                             | 103 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 93.1 ms: 1.04x faster                                                             |
| pidigits       | 197 ms                                                              | 197 ms: 1.00x slower                                                              |
| float          | 76.0 ms                                                             | 82.0 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.8 ms: 1.04x slower                                                             |
| regex_compile  | 137 ms                                                              | 146 ms: 1.07x slower                                                              |
| regex_dna      | 196 ms                                                              | 211 ms: 1.08x slower                                                              |
| regex_effbot   | 3.32 ms                                                             | 3.74 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                               | 1.08x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.99 ms: 1.25x faster                                                             |
| unpickle_pure_python | 228 us                                                              | 218 us: 1.05x faster                                                              |
| xml_etree_parse      | 162 ms                                                              | 156 ms: 1.04x faster                                                              |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                                              |
| json_loads           | 26.2 us                                                             | 25.5 us: 1.03x faster                                                             |
| pickle_dict          | 30.9 us                                                             | 31.4 us: 1.01x slower                                                             |
| pickle_pure_python   | 307 us                                                              | 318 us: 1.04x slower                                                              |
| pickle               | 9.79 us                                                             | 10.7 us: 1.10x slower                                                             |
| xml_etree_process    | 54.1 ms                                                             | 59.9 ms: 1.11x slower                                                             |
| xml_etree_generate   | 76.5 ms                                                             | 85.9 ms: 1.12x slower                                                             |
| pickle_list          | 4.03 us                                                             | 4.58 us: 1.14x slower                                                             |
| unpickle             | 13.2 us                                                             | 15.7 us: 1.18x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.19 ms: 1.08x slower                                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.70 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.1 ms: 2.36x faster                                                             |
| asyncio_tcp             | 888 ms                                                              | 513 ms: 1.73x faster                                                              |
| json_dumps              | 12.5 ms                                                             | 9.99 ms: 1.25x faster                                                             |
| mypy2                   | 422 ms                                                              | 354 ms: 1.19x faster                                                              |
| coroutines              | 26.3 ms                                                             | 22.4 ms: 1.17x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 218 us: 1.05x faster                                                              |
| nqueens                 | 84.0 ms                                                             | 80.1 ms: 1.05x faster                                                             |
| hexiom                  | 6.48 ms                                                             | 6.21 ms: 1.04x faster                                                             |
| async_tree_none         | 525 ms                                                              | 504 ms: 1.04x faster                                                              |
| async_tree_io           | 1.28 sec                                                            | 1.23 sec: 1.04x faster                                                            |
| xml_etree_parse         | 162 ms                                                              | 156 ms: 1.04x faster                                                              |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                                              |
| nbody                   | 96.7 ms                                                             | 93.1 ms: 1.04x faster                                                             |
| unpack_sequence         | 49.5 ns                                                             | 47.9 ns: 1.03x faster                                                             |
| fannkuch                | 384 ms                                                              | 372 ms: 1.03x faster                                                              |
| richards                | 45.7 ms                                                             | 44.3 ms: 1.03x faster                                                             |
| mdp                     | 2.64 sec                                                            | 2.56 sec: 1.03x faster                                                            |
| json_loads              | 26.2 us                                                             | 25.5 us: 1.03x faster                                                             |
| deltablue               | 3.66 ms                                                             | 3.58 ms: 1.02x faster                                                             |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                              | 725 ms: 1.01x faster                                                              |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.01x faster                                                              |
| json                    | 4.86 ms                                                             | 4.81 ms: 1.01x faster                                                             |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                                              |
| pidigits                | 197 ms                                                              | 197 ms: 1.00x slower                                                              |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.01x slower                                                             |
| chaos                   | 68.0 ms                                                             | 68.6 ms: 1.01x slower                                                             |
| pickle_dict             | 30.9 us                                                             | 31.4 us: 1.01x slower                                                             |
| spectral_norm           | 99.5 ms                                                             | 101 ms: 1.02x slower                                                              |
| bench_thread_pool       | 820 us                                                              | 834 us: 1.02x slower                                                              |
| sqlglot_optimize        | 53.4 ms                                                             | 55.1 ms: 1.03x slower                                                             |
| pickle_pure_python      | 307 us                                                              | 318 us: 1.04x slower                                                              |
| regex_v8                | 22.0 ms                                                             | 22.8 ms: 1.04x slower                                                             |
| sqlglot_normalize       | 108 ms                                                              | 112 ms: 1.04x slower                                                              |
| deepcopy_memo           | 36.4 us                                                             | 37.8 us: 1.04x slower                                                             |
| comprehensions          | 22.2 us                                                             | 23.2 us: 1.04x slower                                                             |
| sqlalchemy_imperative   | 18.0 ms                                                             | 18.9 ms: 1.05x slower                                                             |
| 2to3                    | 257 ms                                                              | 270 ms: 1.05x slower                                                              |
| docutils                | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                            |
| pprint_pformat          | 1.45 sec                                                            | 1.53 sec: 1.05x slower                                                            |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.06x slower                                                              |
| pathlib                 | 18.2 ms                                                             | 19.3 ms: 1.06x slower                                                             |
| scimark_lu              | 108 ms                                                              | 115 ms: 1.06x slower                                                              |
| pycparser               | 1.14 sec                                                            | 1.21 sec: 1.06x slower                                                            |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.74 ms: 1.06x slower                                                             |
| raytrace                | 292 ms                                                              | 310 ms: 1.06x slower                                                              |
| pprint_safe_repr        | 701 ms                                                              | 744 ms: 1.06x slower                                                              |
| telco                   | 6.59 ms                                                             | 7.00 ms: 1.06x slower                                                             |
| tornado_http            | 96.7 ms                                                             | 103 ms: 1.06x slower                                                              |
| deepcopy                | 339 us                                                              | 361 us: 1.07x slower                                                              |
| scimark_sor             | 115 ms                                                              | 123 ms: 1.07x slower                                                              |
| regex_compile           | 137 ms                                                              | 146 ms: 1.07x slower                                                              |
| deepcopy_reduce         | 2.96 us                                                             | 3.17 us: 1.07x slower                                                             |
| pyflate                 | 414 ms                                                              | 443 ms: 1.07x slower                                                              |
| regex_dna               | 196 ms                                                              | 211 ms: 1.08x slower                                                              |
| logging_silent          | 98.7 ns                                                             | 106 ns: 1.08x slower                                                              |
| dulwich_log             | 63.6 ms                                                             | 68.4 ms: 1.08x slower                                                             |
| mako                    | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                                             |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.0 ms: 1.08x slower                                                             |
| crypto_pyaes            | 73.8 ms                                                             | 79.6 ms: 1.08x slower                                                             |
| float                   | 76.0 ms                                                             | 82.0 ms: 1.08x slower                                                             |
| python_startup          | 8.49 ms                                                             | 9.19 ms: 1.08x slower                                                             |
| scimark_fft             | 328 ms                                                              | 355 ms: 1.08x slower                                                              |
| logging_simple          | 6.09 us                                                             | 6.61 us: 1.09x slower                                                             |
| gc_traversal            | 3.63 ms                                                             | 3.97 ms: 1.09x slower                                                             |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.10x slower                                                             |
| logging_format          | 6.64 us                                                             | 7.31 us: 1.10x slower                                                             |
| sqlite_synth            | 2.51 us                                                             | 2.78 us: 1.11x slower                                                             |
| xml_etree_process       | 54.1 ms                                                             | 59.9 ms: 1.11x slower                                                             |
| python_startup_no_site  | 5.98 ms                                                             | 6.70 ms: 1.12x slower                                                             |
| xml_etree_generate      | 76.5 ms                                                             | 85.9 ms: 1.12x slower                                                             |
| regex_effbot            | 3.32 ms                                                             | 3.74 ms: 1.13x slower                                                             |
| pickle_list             | 4.03 us                                                             | 4.58 us: 1.14x slower                                                             |
| unpickle                | 13.2 us                                                             | 15.7 us: 1.18x slower                                                             |
| async_generators        | 361 ms                                                              | 449 ms: 1.24x slower                                                              |
| dask                    | 368 ms                                                              | 538 ms: 1.46x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                                      |

Benchmark hidden because not significant (5): async_tree_memoization, unpickle_list, bench_mp_pool, coverage, sqlglot_transpile
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
