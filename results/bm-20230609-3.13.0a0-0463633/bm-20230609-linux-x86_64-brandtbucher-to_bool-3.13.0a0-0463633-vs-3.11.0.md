
# Results vs. 3.11.0

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: 0463633
- commit date: 2023-06-09
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.76 sec: 1.05x slower                                         |
| tornado_http   | 96.3 ms                                                | 104 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                           |
| nbody          | 93.1 ms                                                | 94.2 ms: 1.01x slower                                          |
| float          | 77.2 ms                                                | 82.2 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                          |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                          |
| regex_dna      | 204 ms                                                 | 212 ms: 1.04x slower                                           |
| regex_compile  | 138 ms                                                 | 148 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.86 ms: 1.28x faster                                          |
| json_loads           | 26.5 us                                                | 24.9 us: 1.06x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                           |
| unpickle_pure_python | 228 us                                                 | 226 us: 1.01x faster                                           |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                           |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                          |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                          |
| tomli_loads          | 2.22 sec                                               | 2.31 sec: 1.04x slower                                         |
| pickle               | 10.1 us                                                | 10.5 us: 1.05x slower                                          |
| pickle_pure_python   | 306 us                                                 | 321 us: 1.05x slower                                           |
| xml_etree_process    | 53.9 ms                                                | 59.5 ms: 1.10x slower                                          |
| unpickle             | 13.7 us                                                | 15.1 us: 1.11x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 85.5 ms: 1.12x slower                                          |
| pickle_list          | 4.11 us                                                | 4.63 us: 1.13x slower                                          |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.35 ms: 1.10x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.80 ms: 1.13x slower                                          |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.06x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 144 us: 3.38x faster                                           |
| generators               | 73.5 ms                                                | 32.6 ms: 2.26x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                         |
| json_dumps               | 12.6 ms                                                | 9.86 ms: 1.28x faster                                          |
| mypy2                    | 420 ms                                                 | 350 ms: 1.20x faster                                           |
| regex_effbot             | 3.99 ms                                                | 3.63 ms: 1.10x faster                                          |
| richards_super           | 56.8 ms                                                | 52.5 ms: 1.08x faster                                          |
| coroutines               | 25.5 ms                                                | 23.6 ms: 1.08x faster                                          |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.07x faster                                          |
| async_tree_io            | 1.30 sec                                               | 1.21 sec: 1.07x faster                                         |
| async_tree_none          | 526 ms                                                 | 493 ms: 1.07x faster                                           |
| json_loads               | 26.5 us                                                | 24.9 us: 1.06x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.82 ms: 1.05x faster                                          |
| chaos                    | 69.2 ms                                                | 65.9 ms: 1.05x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 599 ms: 1.05x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                           |
| coverage                 | 100 ms                                                 | 97.5 ms: 1.03x faster                                          |
| json                     | 4.94 ms                                                | 4.83 ms: 1.02x faster                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.38 ms: 1.01x faster                                          |
| deltablue                | 3.67 ms                                                | 3.63 ms: 1.01x faster                                          |
| unpickle_pure_python     | 228 us                                                 | 226 us: 1.01x faster                                           |
| hexiom                   | 6.37 ms                                                | 6.35 ms: 1.00x faster                                          |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                           |
| go                       | 140 ms                                                 | 141 ms: 1.00x slower                                           |
| nqueens                  | 83.4 ms                                                | 83.9 ms: 1.01x slower                                          |
| fannkuch                 | 388 ms                                                 | 392 ms: 1.01x slower                                           |
| xml_etree_iterparse      | 104 ms                                                 | 105 ms: 1.01x slower                                           |
| nbody                    | 93.1 ms                                                | 94.2 ms: 1.01x slower                                          |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                          |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                          |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.02x slower                                          |
| unpickle_list            | 4.91 us                                                | 5.00 us: 1.02x slower                                          |
| bench_thread_pool        | 819 us                                                 | 834 us: 1.02x slower                                           |
| mdp                      | 2.62 sec                                               | 2.67 sec: 1.02x slower                                         |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                          |
| raytrace                 | 297 ms                                                 | 307 ms: 1.03x slower                                           |
| sqlglot_normalize        | 108 ms                                                 | 112 ms: 1.04x slower                                           |
| sqlglot_optimize         | 53.1 ms                                                | 55.2 ms: 1.04x slower                                          |
| tomli_loads              | 2.22 sec                                               | 2.31 sec: 1.04x slower                                         |
| regex_dna                | 204 ms                                                 | 212 ms: 1.04x slower                                           |
| deepcopy_memo            | 37.0 us                                                | 38.6 us: 1.04x slower                                          |
| pickle                   | 10.1 us                                                | 10.5 us: 1.05x slower                                          |
| pickle_pure_python       | 306 us                                                 | 321 us: 1.05x slower                                           |
| crypto_pyaes             | 74.7 ms                                                | 78.4 ms: 1.05x slower                                          |
| telco                    | 6.58 ms                                                | 6.92 ms: 1.05x slower                                          |
| docutils                 | 2.63 sec                                               | 2.76 sec: 1.05x slower                                         |
| pprint_pformat           | 1.46 sec                                               | 1.53 sec: 1.05x slower                                         |
| logging_silent           | 101 ns                                                 | 107 ns: 1.05x slower                                           |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.06x slower                                          |
| deepcopy                 | 342 us                                                 | 363 us: 1.06x slower                                           |
| float                    | 77.2 ms                                                | 82.2 ms: 1.06x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 748 ms: 1.07x slower                                           |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                           |
| scimark_lu               | 110 ms                                                 | 118 ms: 1.07x slower                                           |
| regex_compile            | 138 ms                                                 | 148 ms: 1.07x slower                                           |
| tornado_http             | 96.3 ms                                                | 104 ms: 1.08x slower                                           |
| dulwich_log              | 63.7 ms                                                | 68.9 ms: 1.08x slower                                          |
| logging_format           | 6.68 us                                                | 7.28 us: 1.09x slower                                          |
| logging_simple           | 6.03 us                                                | 6.61 us: 1.09x slower                                          |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.10x slower                                          |
| python_startup           | 8.52 ms                                                | 9.35 ms: 1.10x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.23 us: 1.10x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 59.5 ms: 1.10x slower                                          |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.11x slower                                          |
| scimark_fft              | 328 ms                                                 | 364 ms: 1.11x slower                                           |
| pyflate                  | 418 ms                                                 | 465 ms: 1.11x slower                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.02 ms: 1.12x slower                                          |
| scimark_monte_carlo      | 68.1 ms                                                | 76.2 ms: 1.12x slower                                          |
| xml_etree_generate       | 76.2 ms                                                | 85.5 ms: 1.12x slower                                          |
| pickle_list              | 4.11 us                                                | 4.63 us: 1.13x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.80 ms: 1.13x slower                                          |
| scimark_sor              | 118 ms                                                 | 141 ms: 1.19x slower                                           |
| async_generators         | 368 ms                                                 | 455 ms: 1.24x slower                                           |
| unpack_sequence          | 43.1 ns                                                | 53.6 ns: 1.24x slower                                          |
| dask                     | 360 ms                                                 | 546 ms: 1.52x slower                                           |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, richards, bench_mp_pool, sqlglot_transpile, meteor_contest, pycparser
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
