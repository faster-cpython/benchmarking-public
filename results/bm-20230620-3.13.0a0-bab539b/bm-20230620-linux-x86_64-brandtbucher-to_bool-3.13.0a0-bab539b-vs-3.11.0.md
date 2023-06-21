
# Results vs. 3.11.0

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: bab539b
- commit date: 2023-06-20
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                         |
| tornado_http   | 96.3 ms                                                | 96.9 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                           |
| nbody          | 93.1 ms                                                | 93.8 ms: 1.01x slower                                          |
| float          | 77.2 ms                                                | 79.2 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                          |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                           |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                          |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.0 ms: 1.26x faster                                          |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.06x faster                                           |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                           |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                          |
| pickle_pure_python   | 306 us                                                 | 307 us: 1.00x slower                                           |
| tomli_loads          | 2.22 sec                                               | 2.30 sec: 1.03x slower                                         |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 57.9 ms: 1.08x slower                                          |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 83.7 ms: 1.10x slower                                          |
| pickle_list          | 4.11 us                                                | 4.55 us: 1.11x slower                                          |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.17 ms: 1.08x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.67 ms: 1.11x slower                                          |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                           |
| generators               | 73.5 ms                                                | 28.9 ms: 2.54x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                         |
| json_dumps               | 12.6 ms                                                | 10.0 ms: 1.26x faster                                          |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                           |
| coroutines               | 25.5 ms                                                | 22.1 ms: 1.16x faster                                          |
| regex_effbot             | 3.99 ms                                                | 3.51 ms: 1.14x faster                                          |
| chaos                    | 69.2 ms                                                | 61.6 ms: 1.12x faster                                          |
| deltablue                | 3.67 ms                                                | 3.29 ms: 1.12x faster                                          |
| comprehensions           | 22.4 us                                                | 20.3 us: 1.10x faster                                          |
| async_tree_none          | 526 ms                                                 | 482 ms: 1.09x faster                                           |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                         |
| richards_super           | 56.8 ms                                                | 52.8 ms: 1.08x faster                                          |
| coverage                 | 100 ms                                                 | 93.2 ms: 1.07x faster                                          |
| nqueens                  | 83.4 ms                                                | 78.0 ms: 1.07x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 588 ms: 1.07x faster                                           |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.06x faster                                           |
| json_loads               | 26.5 us                                                | 25.1 us: 1.06x faster                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                          |
| hexiom                   | 6.37 ms                                                | 6.11 ms: 1.04x faster                                          |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.04x faster                                         |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                          |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.02x faster                                         |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 722 ms: 1.02x faster                                           |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                           |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                           |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                          |
| logging_format           | 6.68 us                                                | 6.57 us: 1.02x faster                                          |
| pickle_dict              | 31.1 us                                                | 30.8 us: 1.01x faster                                          |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                           |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                           |
| fannkuch                 | 388 ms                                                 | 385 ms: 1.01x faster                                           |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                          |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                          |
| regex_dna                | 204 ms                                                 | 203 ms: 1.00x faster                                           |
| bench_thread_pool        | 819 us                                                 | 821 us: 1.00x slower                                           |
| pickle_pure_python       | 306 us                                                 | 307 us: 1.00x slower                                           |
| create_gc_cycles         | 1.49 ms                                                | 1.49 ms: 1.00x slower                                          |
| tornado_http             | 96.3 ms                                                | 96.9 ms: 1.01x slower                                          |
| nbody                    | 93.1 ms                                                | 93.8 ms: 1.01x slower                                          |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                           |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                         |
| crypto_pyaes             | 74.7 ms                                                | 75.9 ms: 1.02x slower                                          |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                          |
| deepcopy                 | 342 us                                                 | 349 us: 1.02x slower                                           |
| spectral_norm            | 100 ms                                                 | 102 ms: 1.02x slower                                           |
| float                    | 77.2 ms                                                | 79.2 ms: 1.02x slower                                          |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.03x slower                                          |
| richards                 | 45.7 ms                                                | 47.1 ms: 1.03x slower                                          |
| tomli_loads              | 2.22 sec                                               | 2.30 sec: 1.03x slower                                         |
| logging_silent           | 101 ns                                                 | 105 ns: 1.04x slower                                           |
| dulwich_log              | 63.7 ms                                                | 66.1 ms: 1.04x slower                                          |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.04x slower                                         |
| telco                    | 6.58 ms                                                | 6.89 ms: 1.05x slower                                          |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 736 ms: 1.05x slower                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.74 ms: 1.05x slower                                          |
| scimark_monte_carlo      | 68.1 ms                                                | 72.3 ms: 1.06x slower                                          |
| pyflate                  | 418 ms                                                 | 445 ms: 1.06x slower                                           |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                          |
| scimark_fft              | 328 ms                                                 | 352 ms: 1.07x slower                                           |
| deepcopy_reduce          | 2.94 us                                                | 3.16 us: 1.07x slower                                          |
| gc_traversal             | 4.02 ms                                                | 4.32 ms: 1.07x slower                                          |
| python_startup           | 8.52 ms                                                | 9.17 ms: 1.08x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 57.9 ms: 1.08x slower                                          |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                          |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.10x slower                                          |
| xml_etree_generate       | 76.2 ms                                                | 83.7 ms: 1.10x slower                                          |
| pickle_list              | 4.11 us                                                | 4.55 us: 1.11x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.67 ms: 1.11x slower                                          |
| unpack_sequence          | 43.1 ns                                                | 48.9 ns: 1.14x slower                                          |
| async_generators         | 368 ms                                                 | 446 ms: 1.21x slower                                           |
| dask                     | 360 ms                                                 | 523 ms: 1.45x slower                                           |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (7): meteor_contest, xml_etree_iterparse, raytrace, unpickle_list, bench_mp_pool, logging_simple, scimark_sor
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
