
# Results vs. 3.11.0

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: ec1dac5
- commit date: 2023-07-07
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 91.3 ms: 1.02x faster                                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                                  |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                 |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.69 ms: 1.30x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.07x faster                                                  |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 300 us: 1.02x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                                 |
| tomli_loads          | 2.22 sec                                               | 2.28 sec: 1.03x slower                                                |
| unpickle_list        | 4.91 us                                                | 5.10 us: 1.04x slower                                                 |
| pickle               | 10.1 us                                                | 10.5 us: 1.05x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 57.5 ms: 1.07x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 83.5 ms: 1.10x slower                                                 |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.93 us: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.19 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.67 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                                  |
| generators               | 73.5 ms                                                | 28.7 ms: 2.56x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.69 ms: 1.30x faster                                                 |
| chaos                    | 69.2 ms                                                | 59.4 ms: 1.16x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.7 ms: 1.12x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.30 ms: 1.11x faster                                                 |
| async_tree_none          | 526 ms                                                 | 482 ms: 1.09x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.09x faster                                                 |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                                |
| raytrace                 | 297 ms                                                 | 275 ms: 1.08x faster                                                  |
| richards_super           | 56.8 ms                                                | 52.8 ms: 1.07x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.07x faster                                                  |
| async_tree_memoization   | 627 ms                                                 | 587 ms: 1.07x faster                                                  |
| coverage                 | 100 ms                                                 | 93.8 ms: 1.07x faster                                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                                 |
| nqueens                  | 83.4 ms                                                | 79.9 ms: 1.04x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.13 ms: 1.04x faster                                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                                 |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                                 |
| logging_format           | 6.68 us                                                | 6.48 us: 1.03x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 718 ms: 1.03x faster                                                  |
| logging_simple           | 6.03 us                                                | 5.90 us: 1.02x faster                                                 |
| json                     | 4.94 ms                                                | 4.84 ms: 1.02x faster                                                 |
| pickle_pure_python       | 306 us                                                 | 300 us: 1.02x faster                                                  |
| nbody                    | 93.1 ms                                                | 91.3 ms: 1.02x faster                                                 |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| go                       | 140 ms                                                 | 138 ms: 1.02x faster                                                  |
| regex_compile            | 138 ms                                                 | 136 ms: 1.02x faster                                                  |
| regex_v8                 | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.48 ms: 1.00x faster                                                 |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.46 sec: 1.00x slower                                                |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                                  |
| docutils                 | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 37.5 us: 1.01x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 711 ms: 1.01x slower                                                  |
| deepcopy                 | 342 us                                                 | 347 us: 1.02x slower                                                  |
| crypto_pyaes             | 74.7 ms                                                | 75.9 ms: 1.02x slower                                                 |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.02x slower                                                  |
| richards                 | 45.7 ms                                                | 46.7 ms: 1.02x slower                                                 |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                  |
| pickle_dict              | 31.1 us                                                | 31.8 us: 1.02x slower                                                 |
| mdp                      | 2.62 sec                                               | 2.68 sec: 1.02x slower                                                |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.61 ms: 1.03x slower                                                 |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.03x slower                                                 |
| tomli_loads              | 2.22 sec                                               | 2.28 sec: 1.03x slower                                                |
| dulwich_log              | 63.7 ms                                                | 65.6 ms: 1.03x slower                                                 |
| float                    | 77.2 ms                                                | 79.7 ms: 1.03x slower                                                 |
| unpickle_list            | 4.91 us                                                | 5.10 us: 1.04x slower                                                 |
| regex_dna                | 204 ms                                                 | 213 ms: 1.04x slower                                                  |
| pickle                   | 10.1 us                                                | 10.5 us: 1.05x slower                                                 |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 72.1 ms: 1.06x slower                                                 |
| pyflate                  | 418 ms                                                 | 445 ms: 1.06x slower                                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.13 us: 1.07x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 57.5 ms: 1.07x slower                                                 |
| scimark_fft              | 328 ms                                                 | 352 ms: 1.07x slower                                                  |
| python_startup           | 8.52 ms                                                | 9.19 ms: 1.08x slower                                                 |
| telco                    | 6.58 ms                                                | 7.11 ms: 1.08x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 83.5 ms: 1.10x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.67 ms: 1.11x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.93 us: 1.20x slower                                                 |
| async_generators         | 368 ms                                                 | 446 ms: 1.21x slower                                                  |
| dask                     | 360 ms                                                 | 520 ms: 1.44x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (9): xml_etree_iterparse, unpack_sequence, sqlglot_optimize, tornado_http, bench_thread_pool, fannkuch, bench_mp_pool, pycparser, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
