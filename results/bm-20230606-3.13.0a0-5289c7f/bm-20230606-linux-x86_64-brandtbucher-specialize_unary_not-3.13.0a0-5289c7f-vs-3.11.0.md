
# Results vs. 3.11.0

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 5289c7f
- commit date: 2023-06-06
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                      |
| tornado_http   | 96.3 ms                                                | 103 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                        |
| nbody          | 93.1 ms                                                | 92.2 ms: 1.01x faster                                                       |
| float          | 77.2 ms                                                | 83.0 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.55 ms: 1.12x faster                                                       |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                       |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| regex_compile  | 138 ms                                                 | 146 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.96 ms: 1.26x faster                                                       |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 224 us: 1.02x faster                                                        |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                        |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                       |
| tomli_loads          | 2.22 sec                                               | 2.26 sec: 1.02x slower                                                      |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                       |
| pickle_pure_python   | 306 us                                                 | 320 us: 1.05x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.45 us: 1.08x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                                       |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 85.3 ms: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.36 ms: 1.10x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.81 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.35x faster                                                        |
| generators               | 73.5 ms                                                | 30.1 ms: 2.44x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                                        |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.96 ms: 1.26x faster                                                       |
| mypy2                    | 420 ms                                                 | 349 ms: 1.20x faster                                                        |
| regex_effbot             | 3.99 ms                                                | 3.55 ms: 1.12x faster                                                       |
| richards_super           | 56.8 ms                                                | 51.2 ms: 1.11x faster                                                       |
| coroutines               | 25.5 ms                                                | 23.2 ms: 1.10x faster                                                       |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.07x faster                                                       |
| async_tree_none          | 526 ms                                                 | 501 ms: 1.05x faster                                                        |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                       |
| chaos                    | 69.2 ms                                                | 66.1 ms: 1.05x faster                                                       |
| async_tree_io            | 1.30 sec                                               | 1.24 sec: 1.04x faster                                                      |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                        |
| coverage                 | 100 ms                                                 | 96.8 ms: 1.03x faster                                                       |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                                        |
| async_tree_memoization   | 627 ms                                                 | 609 ms: 1.03x faster                                                        |
| json                     | 4.94 ms                                                | 4.80 ms: 1.03x faster                                                       |
| unpickle_pure_python     | 228 us                                                 | 224 us: 1.02x faster                                                        |
| sqlglot_parse            | 1.40 ms                                                | 1.38 ms: 1.02x faster                                                       |
| deltablue                | 3.67 ms                                                | 3.61 ms: 1.02x faster                                                       |
| pickle_dict              | 31.1 us                                                | 30.8 us: 1.01x faster                                                       |
| nbody                    | 93.1 ms                                                | 92.2 ms: 1.01x faster                                                       |
| richards                 | 45.7 ms                                                | 45.3 ms: 1.01x faster                                                       |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                       |
| go                       | 140 ms                                                 | 140 ms: 1.00x faster                                                        |
| hexiom                   | 6.37 ms                                                | 6.36 ms: 1.00x faster                                                       |
| mdp                      | 2.62 sec                                               | 2.63 sec: 1.00x slower                                                      |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                       |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 104 ms                                                 | 105 ms: 1.01x slower                                                        |
| unpickle_list            | 4.91 us                                                | 4.97 us: 1.01x slower                                                       |
| bench_thread_pool        | 819 us                                                 | 831 us: 1.01x slower                                                        |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                                        |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| tomli_loads              | 2.22 sec                                               | 2.26 sec: 1.02x slower                                                      |
| logging_silent           | 101 ns                                                 | 104 ns: 1.03x slower                                                        |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                                       |
| raytrace                 | 297 ms                                                 | 305 ms: 1.03x slower                                                        |
| pycparser                | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                      |
| telco                    | 6.58 ms                                                | 6.80 ms: 1.03x slower                                                       |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                                       |
| deepcopy_memo            | 37.0 us                                                | 38.4 us: 1.04x slower                                                       |
| sqlglot_optimize         | 53.1 ms                                                | 55.5 ms: 1.05x slower                                                       |
| pickle_pure_python       | 306 us                                                 | 320 us: 1.05x slower                                                        |
| docutils                 | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                      |
| scimark_lu               | 110 ms                                                 | 115 ms: 1.05x slower                                                        |
| sqlglot_normalize        | 108 ms                                                 | 114 ms: 1.05x slower                                                        |
| regex_compile            | 138 ms                                                 | 146 ms: 1.05x slower                                                        |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                        |
| crypto_pyaes             | 74.7 ms                                                | 79.4 ms: 1.06x slower                                                       |
| pprint_pformat           | 1.46 sec                                               | 1.55 sec: 1.06x slower                                                      |
| deepcopy                 | 342 us                                                 | 366 us: 1.07x slower                                                        |
| tornado_http             | 96.3 ms                                                | 103 ms: 1.07x slower                                                        |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                       |
| float                    | 77.2 ms                                                | 83.0 ms: 1.07x slower                                                       |
| dulwich_log              | 63.7 ms                                                | 68.6 ms: 1.08x slower                                                       |
| pickle_list              | 4.11 us                                                | 4.45 us: 1.08x slower                                                       |
| pprint_safe_repr         | 701 ms                                                 | 762 ms: 1.09x slower                                                        |
| logging_format           | 6.68 us                                                | 7.27 us: 1.09x slower                                                       |
| logging_simple           | 6.03 us                                                | 6.60 us: 1.09x slower                                                       |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                                       |
| python_startup           | 8.52 ms                                                | 9.36 ms: 1.10x slower                                                       |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.94 ms: 1.10x slower                                                       |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                                       |
| scimark_monte_carlo      | 68.1 ms                                                | 74.9 ms: 1.10x slower                                                       |
| deepcopy_reduce          | 2.94 us                                                | 3.24 us: 1.10x slower                                                       |
| scimark_fft              | 328 ms                                                 | 363 ms: 1.10x slower                                                        |
| pyflate                  | 418 ms                                                 | 463 ms: 1.11x slower                                                        |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                       |
| xml_etree_generate       | 76.2 ms                                                | 85.3 ms: 1.12x slower                                                       |
| python_startup_no_site   | 6.01 ms                                                | 6.81 ms: 1.13x slower                                                       |
| scimark_sor              | 118 ms                                                 | 139 ms: 1.18x slower                                                        |
| unpack_sequence          | 43.1 ns                                                | 52.8 ns: 1.23x slower                                                       |
| async_generators         | 368 ms                                                 | 459 ms: 1.25x slower                                                        |
| dask                     | 360 ms                                                 | 547 ms: 1.52x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (5): nqueens, meteor_contest, bench_mp_pool, sqlglot_transpile, async_tree_cpu_io_mixed
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
