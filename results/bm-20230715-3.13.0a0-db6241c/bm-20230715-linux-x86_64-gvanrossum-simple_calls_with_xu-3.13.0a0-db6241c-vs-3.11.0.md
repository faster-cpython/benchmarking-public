
# Results vs. 3.11.0

- fork: gvanrossum
- ref: simple_calls_with_xu
- machine: linux-x86_64
- commit hash: db6241c
- commit date: 2023-07-15
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                    |
| tornado_http   | 96.3 ms                                                | 98.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                      |
| nbody          | 93.1 ms                                                | 100 ms: 1.07x slower                                                      |
| float          | 77.2 ms                                                | 85.6 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                     |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| regex_compile  | 138 ms                                                 | 151 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 26.0 us: 1.02x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 302 us: 1.01x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 226 us: 1.01x faster                                                      |
| unpickle_list        | 4.91 us                                                | 4.93 us: 1.01x slower                                                     |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                      |
| pickle               | 10.1 us                                                | 11.0 us: 1.09x slower                                                     |
| unpickle             | 13.7 us                                                | 15.0 us: 1.09x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 86.7 ms: 1.14x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.73 us: 1.15x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.68 sec: 1.21x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 152 us: 3.20x faster                                                      |
| generators               | 73.5 ms                                                | 28.5 ms: 2.58x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                                    |
| json_dumps               | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                     |
| mypy2                    | 420 ms                                                 | 347 ms: 1.21x faster                                                      |
| coroutines               | 25.5 ms                                                | 21.8 ms: 1.17x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                     |
| chaos                    | 69.2 ms                                                | 63.4 ms: 1.09x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                    |
| async_tree_none          | 526 ms                                                 | 485 ms: 1.09x faster                                                      |
| gc_traversal             | 4.02 ms                                                | 3.73 ms: 1.08x faster                                                     |
| coverage                 | 100 ms                                                 | 93.9 ms: 1.07x faster                                                     |
| async_tree_memoization   | 627 ms                                                 | 592 ms: 1.06x faster                                                      |
| raytrace                 | 297 ms                                                 | 280 ms: 1.06x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                      |
| richards_super           | 56.8 ms                                                | 54.9 ms: 1.03x faster                                                     |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 725 ms: 1.02x faster                                                      |
| json_loads               | 26.5 us                                                | 26.0 us: 1.02x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 302 us: 1.01x faster                                                      |
| unpickle_pure_python     | 228 us                                                 | 226 us: 1.01x faster                                                      |
| unpickle_list            | 4.91 us                                                | 4.93 us: 1.01x slower                                                     |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.01x slower                                                     |
| crypto_pyaes             | 74.7 ms                                                | 75.4 ms: 1.01x slower                                                     |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                                      |
| json                     | 4.94 ms                                                | 5.02 ms: 1.01x slower                                                     |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.02x slower                                                      |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                    |
| scimark_monte_carlo      | 68.1 ms                                                | 69.2 ms: 1.02x slower                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                                     |
| tornado_http             | 96.3 ms                                                | 98.2 ms: 1.02x slower                                                     |
| xml_etree_iterparse      | 104 ms                                                 | 106 ms: 1.02x slower                                                      |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| bench_thread_pool        | 819 us                                                 | 848 us: 1.04x slower                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 55.3 ms: 1.04x slower                                                     |
| go                       | 140 ms                                                 | 146 ms: 1.04x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 66.6 ms: 1.05x slower                                                     |
| docutils                 | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                    |
| pprint_pformat           | 1.46 sec                                               | 1.53 sec: 1.05x slower                                                    |
| pathlib                  | 18.2 ms                                                | 19.1 ms: 1.05x slower                                                     |
| scimark_sor              | 118 ms                                                 | 124 ms: 1.05x slower                                                      |
| deepcopy                 | 342 us                                                 | 364 us: 1.06x slower                                                      |
| richards                 | 45.7 ms                                                | 48.8 ms: 1.07x slower                                                     |
| pprint_safe_repr         | 701 ms                                                 | 752 ms: 1.07x slower                                                      |
| scimark_lu               | 110 ms                                                 | 118 ms: 1.07x slower                                                      |
| nbody                    | 93.1 ms                                                | 100 ms: 1.07x slower                                                      |
| mdp                      | 2.62 sec                                               | 2.83 sec: 1.08x slower                                                    |
| python_startup           | 8.52 ms                                                | 9.24 ms: 1.08x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 46.9 ns: 1.09x slower                                                     |
| pickle                   | 10.1 us                                                | 11.0 us: 1.09x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                                     |
| meteor_contest           | 107 ms                                                 | 117 ms: 1.09x slower                                                      |
| regex_compile            | 138 ms                                                 | 151 ms: 1.09x slower                                                      |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.09x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                                     |
| float                    | 77.2 ms                                                | 85.6 ms: 1.11x slower                                                     |
| telco                    | 6.58 ms                                                | 7.31 ms: 1.11x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.80 us: 1.11x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                     |
| comprehensions           | 22.4 us                                                | 25.1 us: 1.12x slower                                                     |
| spectral_norm            | 100 ms                                                 | 113 ms: 1.13x slower                                                      |
| xml_etree_generate       | 76.2 ms                                                | 86.7 ms: 1.14x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.73 us: 1.15x slower                                                     |
| pyflate                  | 418 ms                                                 | 482 ms: 1.15x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 43.1 us: 1.17x slower                                                     |
| scimark_fft              | 328 ms                                                 | 390 ms: 1.19x slower                                                      |
| hexiom                   | 6.37 ms                                                | 7.57 ms: 1.19x slower                                                     |
| mako                     | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.68 sec: 1.21x slower                                                    |
| nqueens                  | 83.4 ms                                                | 101 ms: 1.21x slower                                                      |
| fannkuch                 | 388 ms                                                 | 477 ms: 1.23x slower                                                      |
| async_generators         | 368 ms                                                 | 465 ms: 1.26x slower                                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 6.45 ms: 1.43x slower                                                     |
| dask                     | 360 ms                                                 | 531 ms: 1.48x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (4): logging_simple, bench_mp_pool, logging_format, deltablue
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
