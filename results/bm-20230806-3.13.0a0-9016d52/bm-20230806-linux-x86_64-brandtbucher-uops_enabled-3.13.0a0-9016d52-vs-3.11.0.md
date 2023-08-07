
# Results vs. 3.11.0

- fork: brandtbucher
- ref: uops_enabled
- machine: linux-x86_64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.75 sec: 1.05x slower                                              |
| tornado_http   | 96.3 ms                                                | 97.3 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 201 ms: 1.02x slower                                                |
| nbody          | 93.1 ms                                                | 96.6 ms: 1.04x slower                                               |
| float          | 77.2 ms                                                | 84.5 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                               |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                               |
| regex_dna      | 204 ms                                                 | 211 ms: 1.03x slower                                                |
| regex_compile  | 138 ms                                                 | 152 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.98 ms: 1.26x faster                                               |
| json_loads           | 26.5 us                                                | 25.5 us: 1.04x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                |
| pickle_pure_python   | 306 us                                                 | 300 us: 1.02x faster                                                |
| unpickle_pure_python | 228 us                                                 | 224 us: 1.02x faster                                                |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                               |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                |
| pickle_dict          | 31.1 us                                                | 32.1 us: 1.03x slower                                               |
| pickle               | 10.1 us                                                | 10.6 us: 1.06x slower                                               |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                               |
| xml_etree_process    | 53.9 ms                                                | 59.7 ms: 1.11x slower                                               |
| pickle_list          | 4.11 us                                                | 4.60 us: 1.12x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 86.6 ms: 1.14x slower                                               |
| tomli_loads          | 2.22 sec                                               | 2.66 sec: 1.20x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.42 ms: 1.10x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.88 ms: 1.15x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 12.0 ms: 1.19x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 150 us: 3.25x faster                                                |
| generators               | 73.5 ms                                                | 29.0 ms: 2.53x faster                                               |
| asyncio_tcp              | 922 ms                                                 | 489 ms: 1.88x faster                                                |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                              |
| json_dumps               | 12.6 ms                                                | 9.98 ms: 1.26x faster                                               |
| mypy2                    | 420 ms                                                 | 346 ms: 1.21x faster                                                |
| regex_effbot             | 3.99 ms                                                | 3.51 ms: 1.14x faster                                               |
| coroutines               | 25.5 ms                                                | 23.0 ms: 1.11x faster                                               |
| coverage                 | 100 ms                                                 | 92.3 ms: 1.08x faster                                               |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                              |
| async_tree_none          | 526 ms                                                 | 489 ms: 1.08x faster                                                |
| async_tree_memoization   | 627 ms                                                 | 594 ms: 1.06x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                               |
| raytrace                 | 297 ms                                                 | 283 ms: 1.05x faster                                                |
| chaos                    | 69.2 ms                                                | 66.3 ms: 1.04x faster                                               |
| json_loads               | 26.5 us                                                | 25.5 us: 1.04x faster                                               |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                               |
| json                     | 4.94 ms                                                | 4.83 ms: 1.02x faster                                               |
| gc_traversal             | 4.02 ms                                                | 3.93 ms: 1.02x faster                                               |
| pickle_pure_python       | 306 us                                                 | 300 us: 1.02x faster                                                |
| richards_super           | 56.8 ms                                                | 55.8 ms: 1.02x faster                                               |
| unpickle_pure_python     | 228 us                                                 | 224 us: 1.02x faster                                                |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 729 ms: 1.01x faster                                                |
| crypto_pyaes             | 74.7 ms                                                | 74.9 ms: 1.00x slower                                               |
| tornado_http             | 96.3 ms                                                | 97.3 ms: 1.01x slower                                               |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                               |
| scimark_monte_carlo      | 68.1 ms                                                | 68.9 ms: 1.01x slower                                               |
| pidigits                 | 198 ms                                                 | 201 ms: 1.02x slower                                                |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                               |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                               |
| sqlglot_normalize        | 108 ms                                                 | 110 ms: 1.02x slower                                                |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                |
| xml_etree_iterparse      | 104 ms                                                 | 106 ms: 1.02x slower                                                |
| pycparser                | 1.18 sec                                               | 1.21 sec: 1.03x slower                                              |
| pickle_dict              | 31.1 us                                                | 32.1 us: 1.03x slower                                               |
| regex_dna                | 204 ms                                                 | 211 ms: 1.03x slower                                                |
| nbody                    | 93.1 ms                                                | 96.6 ms: 1.04x slower                                               |
| sqlglot_optimize         | 53.1 ms                                                | 55.2 ms: 1.04x slower                                               |
| mdp                      | 2.62 sec                                               | 2.73 sec: 1.04x slower                                              |
| docutils                 | 2.63 sec                                               | 2.75 sec: 1.05x slower                                              |
| bench_thread_pool        | 819 us                                                 | 859 us: 1.05x slower                                                |
| pprint_pformat           | 1.46 sec                                               | 1.53 sec: 1.05x slower                                              |
| deepcopy                 | 342 us                                                 | 360 us: 1.05x slower                                                |
| pathlib                  | 18.2 ms                                                | 19.2 ms: 1.05x slower                                               |
| scimark_sor              | 118 ms                                                 | 125 ms: 1.05x slower                                                |
| pickle                   | 10.1 us                                                | 10.6 us: 1.06x slower                                               |
| pprint_safe_repr         | 701 ms                                                 | 744 ms: 1.06x slower                                                |
| dulwich_log              | 63.7 ms                                                | 67.6 ms: 1.06x slower                                               |
| scimark_lu               | 110 ms                                                 | 117 ms: 1.07x slower                                                |
| go                       | 140 ms                                                 | 149 ms: 1.07x slower                                                |
| richards                 | 45.7 ms                                                | 48.9 ms: 1.07x slower                                               |
| deepcopy_reduce          | 2.94 us                                                | 3.20 us: 1.09x slower                                               |
| meteor_contest           | 107 ms                                                 | 116 ms: 1.09x slower                                                |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                               |
| float                    | 77.2 ms                                                | 84.5 ms: 1.09x slower                                               |
| comprehensions           | 22.4 us                                                | 24.6 us: 1.10x slower                                               |
| regex_compile            | 138 ms                                                 | 152 ms: 1.10x slower                                                |
| spectral_norm            | 100 ms                                                 | 110 ms: 1.10x slower                                                |
| python_startup           | 8.52 ms                                                | 9.42 ms: 1.10x slower                                               |
| xml_etree_process        | 53.9 ms                                                | 59.7 ms: 1.11x slower                                               |
| sqlite_synth             | 2.52 us                                                | 2.81 us: 1.11x slower                                               |
| pickle_list              | 4.11 us                                                | 4.60 us: 1.12x slower                                               |
| deepcopy_memo            | 37.0 us                                                | 41.8 us: 1.13x slower                                               |
| xml_etree_generate       | 76.2 ms                                                | 86.6 ms: 1.14x slower                                               |
| python_startup_no_site   | 6.01 ms                                                | 6.88 ms: 1.15x slower                                               |
| unpack_sequence          | 43.1 ns                                                | 49.8 ns: 1.16x slower                                               |
| scimark_fft              | 328 ms                                                 | 382 ms: 1.16x slower                                                |
| fannkuch                 | 388 ms                                                 | 455 ms: 1.17x slower                                                |
| nqueens                  | 83.4 ms                                                | 98.8 ms: 1.19x slower                                               |
| mako                     | 10.1 ms                                                | 12.0 ms: 1.19x slower                                               |
| pyflate                  | 418 ms                                                 | 498 ms: 1.19x slower                                                |
| hexiom                   | 6.37 ms                                                | 7.60 ms: 1.19x slower                                               |
| tomli_loads              | 2.22 sec                                               | 2.66 sec: 1.20x slower                                              |
| telco                    | 6.58 ms                                                | 7.93 ms: 1.20x slower                                               |
| async_generators         | 368 ms                                                 | 462 ms: 1.25x slower                                                |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.84 ms: 1.30x slower                                               |
| dask                     | 360 ms                                                 | 532 ms: 1.48x slower                                                |
| Geometric mean           | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (4): deltablue, logging_format, bench_mp_pool, logging_simple
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
