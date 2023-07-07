
# Results vs. 3.11.0

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: 0ab8274
- commit date: 2023-07-06
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| float          | 77.2 ms                                                | 80.4 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                 |
| regex_dna      | 204 ms                                                 | 211 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.89 ms: 1.27x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                                  |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 300 us: 1.02x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                 |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                 |
| tomli_loads          | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.0 ms: 1.10x slower                                                 |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.64 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.72 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.4 ms: 1.03x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.34x faster                                                  |
| generators               | 73.5 ms                                                | 28.5 ms: 2.58x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 512 ms: 1.80x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.89 ms: 1.27x faster                                                 |
| chaos                    | 69.2 ms                                                | 59.6 ms: 1.16x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.6 ms: 1.13x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.26 ms: 1.13x faster                                                 |
| coverage                 | 100 ms                                                 | 91.3 ms: 1.10x faster                                                 |
| async_tree_none          | 526 ms                                                 | 482 ms: 1.09x faster                                                  |
| raytrace                 | 297 ms                                                 | 273 ms: 1.09x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.08x faster                                                 |
| richards_super           | 56.8 ms                                                | 53.0 ms: 1.07x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 589 ms: 1.07x faster                                                  |
| hexiom                   | 6.37 ms                                                | 6.01 ms: 1.06x faster                                                 |
| nqueens                  | 83.4 ms                                                | 79.0 ms: 1.06x faster                                                 |
| nbody                    | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                 |
| logging_format           | 6.68 us                                                | 6.40 us: 1.04x faster                                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.04x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                |
| logging_simple           | 6.03 us                                                | 5.83 us: 1.03x faster                                                 |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.02x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                                 |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                  |
| pickle_pure_python       | 306 us                                                 | 300 us: 1.02x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 727 ms: 1.02x faster                                                  |
| regex_compile            | 138 ms                                                 | 136 ms: 1.02x faster                                                  |
| bench_thread_pool        | 819 us                                                 | 814 us: 1.01x faster                                                  |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                                 |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| deepcopy_memo            | 37.0 us                                                | 37.2 us: 1.01x slower                                                 |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                                  |
| docutils                 | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                                  |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                 |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                                 |
| mdp                      | 2.62 sec                                               | 2.65 sec: 1.01x slower                                                |
| deepcopy                 | 342 us                                                 | 348 us: 1.02x slower                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                                 |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 716 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.62 ms: 1.03x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 65.5 ms: 1.03x slower                                                 |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                                 |
| richards                 | 45.7 ms                                                | 47.1 ms: 1.03x slower                                                 |
| mako                     | 10.1 ms                                                | 10.4 ms: 1.03x slower                                                 |
| regex_dna                | 204 ms                                                 | 211 ms: 1.04x slower                                                  |
| crypto_pyaes             | 74.7 ms                                                | 77.5 ms: 1.04x slower                                                 |
| tomli_loads              | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                |
| float                    | 77.2 ms                                                | 80.4 ms: 1.04x slower                                                 |
| pyflate                  | 418 ms                                                 | 441 ms: 1.05x slower                                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 71.7 ms: 1.05x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.10 us: 1.06x slower                                                 |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                 |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                  |
| xml_etree_process        | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                 |
| gc_traversal             | 4.02 ms                                                | 4.33 ms: 1.08x slower                                                 |
| scimark_fft              | 328 ms                                                 | 355 ms: 1.08x slower                                                  |
| python_startup           | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.77 us: 1.10x slower                                                 |
| telco                    | 6.58 ms                                                | 7.26 ms: 1.10x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.0 ms: 1.10x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 48.1 ns: 1.12x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.72 ms: 1.12x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.64 us: 1.13x slower                                                 |
| async_generators         | 368 ms                                                 | 448 ms: 1.21x slower                                                  |
| dask                     | 360 ms                                                 | 516 ms: 1.43x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (8): json, xml_etree_iterparse, tornado_http, fannkuch, bench_mp_pool, pprint_pformat, scimark_sor, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
