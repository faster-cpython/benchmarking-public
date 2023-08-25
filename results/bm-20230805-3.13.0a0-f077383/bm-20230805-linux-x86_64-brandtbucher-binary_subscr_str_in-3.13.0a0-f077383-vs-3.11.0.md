
# Results vs. 3.11.0

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: f077383
- commit date: 2023-08-05
- overall geometric mean: 1.05x faster
- HPT reliability: 92.95%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.64 sec: 1.01x slower                                                      |
| tornado_http   | 96.3 ms                                                | 95.4 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 92.3 ms: 1.01x faster                                                       |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                        |
| float          | 77.2 ms                                                | 79.2 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                       |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                       |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                       |
| tomli_loads          | 2.22 sec                                               | 2.08 sec: 1.07x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.06x faster                                                        |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.05x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                        |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                       |
| pickle_dict          | 31.1 us                                                | 32.1 us: 1.03x slower                                                       |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                       |
| unpickle             | 13.7 us                                                | 14.8 us: 1.09x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.51 us: 1.10x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.40 ms: 1.10x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.87 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 149 us: 3.26x faster                                                        |
| generators               | 73.5 ms                                                | 28.5 ms: 2.57x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                                        |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                       |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                                        |
| coroutines               | 25.5 ms                                                | 21.4 ms: 1.19x faster                                                       |
| chaos                    | 69.2 ms                                                | 59.0 ms: 1.17x faster                                                       |
| regex_effbot             | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                       |
| deltablue                | 3.67 ms                                                | 3.18 ms: 1.15x faster                                                       |
| sqlglot_parse            | 1.40 ms                                                | 1.26 ms: 1.12x faster                                                       |
| raytrace                 | 297 ms                                                 | 267 ms: 1.11x faster                                                        |
| async_tree_io            | 1.30 sec                                               | 1.17 sec: 1.11x faster                                                      |
| comprehensions           | 22.4 us                                                | 20.3 us: 1.11x faster                                                       |
| async_tree_none          | 526 ms                                                 | 478 ms: 1.10x faster                                                        |
| gc_traversal             | 4.02 ms                                                | 3.67 ms: 1.10x faster                                                       |
| sqlglot_transpile        | 1.70 ms                                                | 1.58 ms: 1.08x faster                                                       |
| async_tree_memoization   | 627 ms                                                 | 582 ms: 1.08x faster                                                        |
| tomli_loads              | 2.22 sec                                               | 2.08 sec: 1.07x faster                                                      |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.06x faster                                                        |
| coverage                 | 100 ms                                                 | 94.2 ms: 1.06x faster                                                       |
| crypto_pyaes             | 74.7 ms                                                | 70.6 ms: 1.06x faster                                                       |
| hexiom                   | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                       |
| richards_super           | 56.8 ms                                                | 53.8 ms: 1.05x faster                                                       |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                       |
| pickle_pure_python       | 306 us                                                 | 293 us: 1.05x faster                                                        |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                        |
| json                     | 4.94 ms                                                | 4.76 ms: 1.04x faster                                                       |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                       |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 715 ms: 1.03x faster                                                        |
| logging_simple           | 6.03 us                                                | 5.89 us: 1.02x faster                                                       |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 66.9 ms: 1.02x faster                                                       |
| nqueens                  | 83.4 ms                                                | 82.2 ms: 1.01x faster                                                       |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                        |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                                        |
| nbody                    | 93.1 ms                                                | 92.3 ms: 1.01x faster                                                       |
| tornado_http             | 96.3 ms                                                | 95.4 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 53.1 ms                                                | 52.7 ms: 1.01x faster                                                       |
| pprint_pformat           | 1.46 sec                                               | 1.45 sec: 1.01x faster                                                      |
| go                       | 140 ms                                                 | 139 ms: 1.01x faster                                                        |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                       |
| fannkuch                 | 388 ms                                                 | 386 ms: 1.00x faster                                                        |
| bench_thread_pool        | 819 us                                                 | 824 us: 1.01x slower                                                        |
| docutils                 | 2.63 sec                                               | 2.64 sec: 1.01x slower                                                      |
| mdp                      | 2.62 sec                                               | 2.64 sec: 1.01x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 710 ms: 1.01x slower                                                        |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                        |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.01x slower                                                        |
| regex_dna                | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                                       |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                                       |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                                       |
| logging_silent           | 101 ns                                                 | 104 ns: 1.02x slower                                                        |
| float                    | 77.2 ms                                                | 79.2 ms: 1.03x slower                                                       |
| pickle_dict              | 31.1 us                                                | 32.1 us: 1.03x slower                                                       |
| deepcopy                 | 342 us                                                 | 353 us: 1.03x slower                                                        |
| dulwich_log              | 63.7 ms                                                | 65.9 ms: 1.03x slower                                                       |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                        |
| unpack_sequence          | 43.1 ns                                                | 44.7 ns: 1.04x slower                                                       |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                                       |
| richards                 | 45.7 ms                                                | 47.6 ms: 1.04x slower                                                       |
| pyflate                  | 418 ms                                                 | 443 ms: 1.06x slower                                                        |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                       |
| deepcopy_reduce          | 2.94 us                                                | 3.16 us: 1.07x slower                                                       |
| xml_etree_process        | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                       |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                       |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.09x slower                                                       |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                                        |
| pickle_list              | 4.11 us                                                | 4.51 us: 1.10x slower                                                       |
| python_startup           | 8.52 ms                                                | 9.40 ms: 1.10x slower                                                       |
| xml_etree_generate       | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                       |
| python_startup_no_site   | 6.01 ms                                                | 6.87 ms: 1.14x slower                                                       |
| telco                    | 6.58 ms                                                | 7.76 ms: 1.18x slower                                                       |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                                        |
| dask                     | 360 ms                                                 | 518 ms: 1.44x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (5): xml_etree_iterparse, bench_mp_pool, create_gc_cycles, scimark_sparse_mat_mult, scimark_lu
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 92.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
