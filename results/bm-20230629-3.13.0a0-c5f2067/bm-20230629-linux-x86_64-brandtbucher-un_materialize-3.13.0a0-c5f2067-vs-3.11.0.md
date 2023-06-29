
# Results vs. 3.11.0

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: c5f2067
- commit date: 2023-06-29
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 90.2 ms: 1.03x faster                                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| float          | 77.2 ms                                                | 78.8 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                                  |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.61 ms: 1.31x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                                  |
| json_loads           | 26.5 us                                                | 25.5 us: 1.04x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                                  |
| tomli_loads          | 2.22 sec                                               | 2.19 sec: 1.01x faster                                                |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.00x faster                                                 |
| unpickle_list        | 4.91 us                                                | 4.93 us: 1.01x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 57.1 ms: 1.06x slower                                                 |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 82.8 ms: 1.09x slower                                                 |
| unpickle             | 13.7 us                                                | 15.5 us: 1.13x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.75 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.70 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 142 us: 3.41x faster                                                  |
| generators               | 73.5 ms                                                | 28.9 ms: 2.54x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.61 ms: 1.31x faster                                                 |
| chaos                    | 69.2 ms                                                | 59.0 ms: 1.17x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| richards_super           | 56.8 ms                                                | 49.9 ms: 1.14x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                                 |
| async_tree_none          | 526 ms                                                 | 477 ms: 1.10x faster                                                  |
| raytrace                 | 297 ms                                                 | 273 ms: 1.09x faster                                                  |
| coverage                 | 100 ms                                                 | 92.0 ms: 1.09x faster                                                 |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.09x faster                                                 |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.08x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                                  |
| async_tree_memoization   | 627 ms                                                 | 585 ms: 1.07x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.06x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.01 ms: 1.06x faster                                                 |
| logging_format           | 6.68 us                                                | 6.39 us: 1.05x faster                                                 |
| richards                 | 45.7 ms                                                | 43.8 ms: 1.05x faster                                                 |
| nqueens                  | 83.4 ms                                                | 80.1 ms: 1.04x faster                                                 |
| json_loads               | 26.5 us                                                | 25.5 us: 1.04x faster                                                 |
| logging_silent           | 101 ns                                                 | 97.7 ns: 1.03x faster                                                 |
| nbody                    | 93.1 ms                                                | 90.2 ms: 1.03x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                                  |
| meteor_contest           | 107 ms                                                 | 103 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 718 ms: 1.03x faster                                                  |
| gc_traversal             | 4.02 ms                                                | 3.91 ms: 1.03x faster                                                 |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                                  |
| regex_compile            | 138 ms                                                 | 135 ms: 1.03x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                 |
| logging_simple           | 6.03 us                                                | 5.93 us: 1.02x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                 | 102 ms: 1.01x faster                                                  |
| sqlglot_optimize         | 53.1 ms                                                | 52.4 ms: 1.01x faster                                                 |
| tomli_loads              | 2.22 sec                                               | 2.19 sec: 1.01x faster                                                |
| scimark_lu               | 110 ms                                                 | 109 ms: 1.01x faster                                                  |
| bench_thread_pool        | 819 us                                                 | 814 us: 1.01x faster                                                  |
| pickle_dict              | 31.1 us                                                | 31.0 us: 1.00x faster                                                 |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| docutils                 | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                |
| unpickle_list            | 4.91 us                                                | 4.93 us: 1.01x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 37.3 us: 1.01x slower                                                 |
| fannkuch                 | 388 ms                                                 | 393 ms: 1.01x slower                                                  |
| pprint_safe_repr         | 701 ms                                                 | 711 ms: 1.01x slower                                                  |
| regex_dna                | 204 ms                                                 | 207 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.57 ms: 1.02x slower                                                 |
| crypto_pyaes             | 74.7 ms                                                | 76.0 ms: 1.02x slower                                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                                 |
| float                    | 77.2 ms                                                | 78.8 ms: 1.02x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 65.4 ms: 1.03x slower                                                 |
| mdp                      | 2.62 sec                                               | 2.70 sec: 1.03x slower                                                |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                  |
| mako                     | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 72.0 ms: 1.06x slower                                                 |
| pathlib                  | 18.2 ms                                                | 19.3 ms: 1.06x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 57.1 ms: 1.06x slower                                                 |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                                 |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                                  |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 82.8 ms: 1.09x slower                                                 |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                                  |
| telco                    | 6.58 ms                                                | 7.31 ms: 1.11x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 47.9 ns: 1.11x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.70 ms: 1.12x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.5 us: 1.13x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.75 us: 1.16x slower                                                 |
| async_generators         | 368 ms                                                 | 437 ms: 1.19x slower                                                  |
| dask                     | 360 ms                                                 | 512 ms: 1.42x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (8): pprint_pformat, bench_mp_pool, pickle_pure_python, regex_v8, tornado_http, pycparser, scimark_sor, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
