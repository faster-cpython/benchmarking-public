
# Results vs. 3.11.0

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: f9fa498
- commit date: 2023-06-21
- overall geometric mean: 1.04x faster
- HPT reliability: 89.27%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.3 ms: 1.05x faster                                          |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                           |
| float          | 77.2 ms                                                | 79.8 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                          |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                           |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                          |
| regex_dna      | 204 ms                                                 | 207 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.91 ms: 1.27x faster                                          |
| unpickle_pure_python | 228 us                                                 | 209 us: 1.09x faster                                           |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                          |
| pickle_pure_python   | 306 us                                                 | 301 us: 1.02x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                           |
| tomli_loads          | 2.22 sec                                               | 2.24 sec: 1.01x slower                                         |
| pickle_dict          | 31.1 us                                                | 32.0 us: 1.03x slower                                          |
| pickle               | 10.1 us                                                | 10.7 us: 1.07x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 58.4 ms: 1.08x slower                                          |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 84.4 ms: 1.11x slower                                          |
| pickle_list          | 4.11 us                                                | 4.67 us: 1.14x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.19 ms: 1.08x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.67 ms: 1.11x slower                                          |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.29x faster                                           |
| generators               | 73.5 ms                                                | 29.1 ms: 2.53x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.75x faster                                         |
| json_dumps               | 12.6 ms                                                | 9.91 ms: 1.27x faster                                          |
| mypy2                    | 420 ms                                                 | 335 ms: 1.25x faster                                           |
| coroutines               | 25.5 ms                                                | 22.1 ms: 1.15x faster                                          |
| regex_effbot             | 3.99 ms                                                | 3.50 ms: 1.14x faster                                          |
| deltablue                | 3.67 ms                                                | 3.29 ms: 1.12x faster                                          |
| chaos                    | 69.2 ms                                                | 62.2 ms: 1.11x faster                                          |
| comprehensions           | 22.4 us                                                | 20.3 us: 1.11x faster                                          |
| unpickle_pure_python     | 228 us                                                 | 209 us: 1.09x faster                                           |
| richards_super           | 56.8 ms                                                | 52.4 ms: 1.08x faster                                          |
| async_tree_none          | 526 ms                                                 | 487 ms: 1.08x faster                                           |
| coverage                 | 100 ms                                                 | 92.6 ms: 1.08x faster                                          |
| hexiom                   | 6.37 ms                                                | 5.90 ms: 1.08x faster                                          |
| async_tree_io            | 1.30 sec                                               | 1.21 sec: 1.07x faster                                         |
| sqlglot_parse            | 1.40 ms                                                | 1.32 ms: 1.06x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 592 ms: 1.06x faster                                           |
| nbody                    | 93.1 ms                                                | 88.3 ms: 1.05x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.82 ms: 1.05x faster                                          |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                          |
| logging_format           | 6.68 us                                                | 6.41 us: 1.04x faster                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                          |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                          |
| mdp                      | 2.62 sec                                               | 2.53 sec: 1.03x faster                                         |
| logging_simple           | 6.03 us                                                | 5.85 us: 1.03x faster                                          |
| regex_compile            | 138 ms                                                 | 135 ms: 1.03x faster                                           |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                         |
| fannkuch                 | 388 ms                                                 | 380 ms: 1.02x faster                                           |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                           |
| pickle_pure_python       | 306 us                                                 | 301 us: 1.02x faster                                           |
| scimark_sor              | 118 ms                                                 | 116 ms: 1.02x faster                                           |
| logging_silent           | 101 ns                                                 | 99.5 ns: 1.02x faster                                          |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 728 ms: 1.02x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 156 ms: 1.01x faster                                           |
| nqueens                  | 83.4 ms                                                | 82.3 ms: 1.01x faster                                          |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                           |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.01x faster                                           |
| raytrace                 | 297 ms                                                 | 294 ms: 1.01x faster                                           |
| regex_v8                 | 22.0 ms                                                | 21.8 ms: 1.01x faster                                          |
| scimark_lu               | 110 ms                                                 | 109 ms: 1.01x faster                                           |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                           |
| deepcopy_memo            | 37.0 us                                                | 37.2 us: 1.01x slower                                          |
| richards                 | 45.7 ms                                                | 46.1 ms: 1.01x slower                                          |
| tomli_loads              | 2.22 sec                                               | 2.24 sec: 1.01x slower                                         |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                         |
| deepcopy                 | 342 us                                                 | 346 us: 1.01x slower                                           |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                          |
| regex_dna                | 204 ms                                                 | 207 ms: 1.01x slower                                           |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                         |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.60 ms: 1.02x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 719 ms: 1.03x slower                                           |
| pickle_dict              | 31.1 us                                                | 32.0 us: 1.03x slower                                          |
| telco                    | 6.58 ms                                                | 6.80 ms: 1.03x slower                                          |
| dulwich_log              | 63.7 ms                                                | 65.7 ms: 1.03x slower                                          |
| float                    | 77.2 ms                                                | 79.8 ms: 1.03x slower                                          |
| crypto_pyaes             | 74.7 ms                                                | 77.3 ms: 1.04x slower                                          |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 71.5 ms: 1.05x slower                                          |
| pathlib                  | 18.2 ms                                                | 19.2 ms: 1.05x slower                                          |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.10 us: 1.05x slower                                          |
| scimark_fft              | 328 ms                                                 | 346 ms: 1.05x slower                                           |
| pyflate                  | 418 ms                                                 | 441 ms: 1.06x slower                                           |
| unpack_sequence          | 43.1 ns                                                | 45.8 ns: 1.06x slower                                          |
| pickle                   | 10.1 us                                                | 10.7 us: 1.07x slower                                          |
| python_startup           | 8.52 ms                                                | 9.19 ms: 1.08x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 58.4 ms: 1.08x slower                                          |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                          |
| sqlite_synth             | 2.52 us                                                | 2.77 us: 1.10x slower                                          |
| xml_etree_generate       | 76.2 ms                                                | 84.4 ms: 1.11x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.67 ms: 1.11x slower                                          |
| pickle_list              | 4.11 us                                                | 4.67 us: 1.14x slower                                          |
| async_generators         | 368 ms                                                 | 451 ms: 1.22x slower                                           |
| dask                     | 360 ms                                                 | 521 ms: 1.45x slower                                           |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (6): unpickle_list, xml_etree_iterparse, bench_mp_pool, bench_thread_pool, tornado_http, sqlglot_optimize
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 89.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
