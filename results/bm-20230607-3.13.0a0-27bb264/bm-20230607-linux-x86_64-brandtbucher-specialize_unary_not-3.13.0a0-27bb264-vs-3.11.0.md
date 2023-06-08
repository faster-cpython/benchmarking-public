
# Results vs. 3.11.0

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 27bb264
- commit date: 2023-06-07
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                      |
| tornado_http   | 96.3 ms                                                | 103 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 90.5 ms: 1.03x faster                                                       |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                                        |
| float          | 77.2 ms                                                | 80.9 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                       |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.89 ms: 1.27x faster                                                       |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                        |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 224 us: 1.02x faster                                                        |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| tomli_loads          | 2.22 sec                                               | 2.27 sec: 1.02x slower                                                      |
| pickle_pure_python   | 306 us                                                 | 315 us: 1.03x slower                                                        |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.51 us: 1.10x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 59.3 ms: 1.10x slower                                                       |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 85.1 ms: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.37 ms: 1.10x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.82 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                                        |
| generators               | 73.5 ms                                                | 31.9 ms: 2.30x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                                        |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.89 ms: 1.27x faster                                                       |
| mypy2                    | 420 ms                                                 | 348 ms: 1.21x faster                                                        |
| richards_super           | 56.8 ms                                                | 51.0 ms: 1.11x faster                                                       |
| regex_effbot             | 3.99 ms                                                | 3.61 ms: 1.11x faster                                                       |
| coroutines               | 25.5 ms                                                | 23.7 ms: 1.07x faster                                                       |
| comprehensions           | 22.4 us                                                | 21.2 us: 1.06x faster                                                       |
| chaos                    | 69.2 ms                                                | 65.6 ms: 1.06x faster                                                       |
| async_tree_none          | 526 ms                                                 | 500 ms: 1.05x faster                                                        |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                                       |
| async_tree_io            | 1.30 sec                                               | 1.24 sec: 1.05x faster                                                      |
| coverage                 | 100 ms                                                 | 96.4 ms: 1.04x faster                                                       |
| async_tree_memoization   | 627 ms                                                 | 607 ms: 1.03x faster                                                        |
| json                     | 4.94 ms                                                | 4.78 ms: 1.03x faster                                                       |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                        |
| nbody                    | 93.1 ms                                                | 90.5 ms: 1.03x faster                                                       |
| sqlglot_parse            | 1.40 ms                                                | 1.36 ms: 1.03x faster                                                       |
| pickle_dict              | 31.1 us                                                | 30.4 us: 1.02x faster                                                       |
| unpickle_pure_python     | 228 us                                                 | 224 us: 1.02x faster                                                        |
| richards                 | 45.7 ms                                                | 45.0 ms: 1.02x faster                                                       |
| mdp                      | 2.62 sec                                               | 2.59 sec: 1.01x faster                                                      |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                                        |
| gc_traversal             | 4.02 ms                                                | 3.99 ms: 1.01x faster                                                       |
| unpickle_list            | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| hexiom                   | 6.37 ms                                                | 6.42 ms: 1.01x slower                                                       |
| nqueens                  | 83.4 ms                                                | 84.9 ms: 1.02x slower                                                       |
| bench_thread_pool        | 819 us                                                 | 835 us: 1.02x slower                                                        |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| deepcopy_memo            | 37.0 us                                                | 37.8 us: 1.02x slower                                                       |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                                       |
| tomli_loads              | 2.22 sec                                               | 2.27 sec: 1.02x slower                                                      |
| pycparser                | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                      |
| pickle_pure_python       | 306 us                                                 | 315 us: 1.03x slower                                                        |
| fannkuch                 | 388 ms                                                 | 400 ms: 1.03x slower                                                        |
| scimark_lu               | 110 ms                                                 | 114 ms: 1.03x slower                                                        |
| sqlglot_optimize         | 53.1 ms                                                | 55.1 ms: 1.04x slower                                                       |
| sqlglot_normalize        | 108 ms                                                 | 113 ms: 1.04x slower                                                        |
| docutils                 | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                      |
| float                    | 77.2 ms                                                | 80.9 ms: 1.05x slower                                                       |
| deepcopy                 | 342 us                                                 | 359 us: 1.05x slower                                                        |
| pprint_pformat           | 1.46 sec                                               | 1.53 sec: 1.05x slower                                                      |
| regex_compile            | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.77 ms: 1.06x slower                                                       |
| telco                    | 6.58 ms                                                | 7.00 ms: 1.06x slower                                                       |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                        |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                                       |
| crypto_pyaes             | 74.7 ms                                                | 79.9 ms: 1.07x slower                                                       |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                       |
| pprint_safe_repr         | 701 ms                                                 | 752 ms: 1.07x slower                                                        |
| dulwich_log              | 63.7 ms                                                | 68.4 ms: 1.07x slower                                                       |
| tornado_http             | 96.3 ms                                                | 103 ms: 1.07x slower                                                        |
| scimark_monte_carlo      | 68.1 ms                                                | 73.5 ms: 1.08x slower                                                       |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.09x slower                                                       |
| scimark_fft              | 328 ms                                                 | 357 ms: 1.09x slower                                                        |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                       |
| logging_simple           | 6.03 us                                                | 6.61 us: 1.10x slower                                                       |
| pickle_list              | 4.11 us                                                | 4.51 us: 1.10x slower                                                       |
| python_startup           | 8.52 ms                                                | 9.37 ms: 1.10x slower                                                       |
| xml_etree_process        | 53.9 ms                                                | 59.3 ms: 1.10x slower                                                       |
| logging_format           | 6.68 us                                                | 7.36 us: 1.10x slower                                                       |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                       |
| pyflate                  | 418 ms                                                 | 465 ms: 1.11x slower                                                        |
| xml_etree_generate       | 76.2 ms                                                | 85.1 ms: 1.12x slower                                                       |
| python_startup_no_site   | 6.01 ms                                                | 6.82 ms: 1.14x slower                                                       |
| scimark_sor              | 118 ms                                                 | 137 ms: 1.16x slower                                                        |
| async_generators         | 368 ms                                                 | 457 ms: 1.24x slower                                                        |
| unpack_sequence          | 43.1 ns                                                | 54.8 ns: 1.27x slower                                                       |
| dask                     | 360 ms                                                 | 547 ms: 1.52x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (11): sqlglot_transpile, regex_v8, deltablue, bench_mp_pool, go, logging_silent, meteor_contest, pathlib, xml_etree_iterparse, raytrace, async_tree_cpu_io_mixed
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
