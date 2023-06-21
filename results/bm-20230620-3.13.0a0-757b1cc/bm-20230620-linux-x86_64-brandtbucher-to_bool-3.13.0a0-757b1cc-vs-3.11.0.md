
# Results vs. 3.11.0

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: 757b1cc
- commit date: 2023-06-20
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.67 sec: 1.01x slower                                         |
| tornado_http   | 96.3 ms                                                | 97.0 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                           |
| nbody          | 93.1 ms                                                | 92.2 ms: 1.01x faster                                          |
| float          | 77.2 ms                                                | 80.0 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                          |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                           |
| regex_v8       | 22.0 ms                                                | 22.6 ms: 1.02x slower                                          |
| regex_dna      | 204 ms                                                 | 217 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.95 ms: 1.27x faster                                          |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                           |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                           |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                           |
| pickle_pure_python   | 306 us                                                 | 308 us: 1.01x slower                                           |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                          |
| tomli_loads          | 2.22 sec                                               | 2.27 sec: 1.02x slower                                         |
| pickle_dict          | 31.1 us                                                | 32.1 us: 1.03x slower                                          |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                          |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 58.4 ms: 1.08x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 84.3 ms: 1.11x slower                                          |
| pickle_list          | 4.11 us                                                | 4.62 us: 1.12x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.17 ms: 1.08x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                          |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.32x faster                                           |
| generators               | 73.5 ms                                                | 29.4 ms: 2.50x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.75x faster                                         |
| json_dumps               | 12.6 ms                                                | 9.95 ms: 1.27x faster                                          |
| mypy2                    | 420 ms                                                 | 337 ms: 1.25x faster                                           |
| regex_effbot             | 3.99 ms                                                | 3.56 ms: 1.12x faster                                          |
| chaos                    | 69.2 ms                                                | 62.1 ms: 1.11x faster                                          |
| deltablue                | 3.67 ms                                                | 3.32 ms: 1.11x faster                                          |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.68 ms: 1.09x faster                                          |
| coroutines               | 25.5 ms                                                | 23.6 ms: 1.08x faster                                          |
| async_tree_none          | 526 ms                                                 | 487 ms: 1.08x faster                                           |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                         |
| coverage                 | 100 ms                                                 | 92.9 ms: 1.08x faster                                          |
| nqueens                  | 83.4 ms                                                | 77.7 ms: 1.07x faster                                          |
| richards_super           | 56.8 ms                                                | 53.4 ms: 1.06x faster                                          |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                           |
| async_tree_memoization   | 627 ms                                                 | 594 ms: 1.06x faster                                           |
| json_loads               | 26.5 us                                                | 25.1 us: 1.06x faster                                          |
| hexiom                   | 6.37 ms                                                | 6.07 ms: 1.05x faster                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.35 ms: 1.04x faster                                          |
| json                     | 4.94 ms                                                | 4.78 ms: 1.03x faster                                          |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                           |
| logging_format           | 6.68 us                                                | 6.53 us: 1.02x faster                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                          |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                           |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 729 ms: 1.01x faster                                           |
| nbody                    | 93.1 ms                                                | 92.2 ms: 1.01x faster                                          |
| sqlglot_normalize        | 108 ms                                                 | 107 ms: 1.01x faster                                           |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                           |
| raytrace                 | 297 ms                                                 | 295 ms: 1.00x faster                                           |
| go                       | 140 ms                                                 | 141 ms: 1.00x slower                                           |
| tornado_http             | 96.3 ms                                                | 97.0 ms: 1.01x slower                                          |
| sqlglot_optimize         | 53.1 ms                                                | 53.5 ms: 1.01x slower                                          |
| pickle_pure_python       | 306 us                                                 | 308 us: 1.01x slower                                           |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                          |
| unpickle_list            | 4.91 us                                                | 4.96 us: 1.01x slower                                          |
| pycparser                | 1.18 sec                                               | 1.19 sec: 1.01x slower                                         |
| deepcopy_memo            | 37.0 us                                                | 37.5 us: 1.01x slower                                          |
| docutils                 | 2.63 sec                                               | 2.67 sec: 1.01x slower                                         |
| fannkuch                 | 388 ms                                                 | 395 ms: 1.02x slower                                           |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                           |
| tomli_loads              | 2.22 sec                                               | 2.27 sec: 1.02x slower                                         |
| regex_v8                 | 22.0 ms                                                | 22.6 ms: 1.02x slower                                          |
| deepcopy                 | 342 us                                                 | 351 us: 1.02x slower                                           |
| telco                    | 6.58 ms                                                | 6.75 ms: 1.03x slower                                          |
| mdp                      | 2.62 sec                                               | 2.69 sec: 1.03x slower                                         |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                         |
| dulwich_log              | 63.7 ms                                                | 65.5 ms: 1.03x slower                                          |
| logging_silent           | 101 ns                                                 | 104 ns: 1.03x slower                                           |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                          |
| pickle_dict              | 31.1 us                                                | 32.1 us: 1.03x slower                                          |
| pickle                   | 10.1 us                                                | 10.4 us: 1.03x slower                                          |
| crypto_pyaes             | 74.7 ms                                                | 77.3 ms: 1.04x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.66 ms: 1.04x slower                                          |
| float                    | 77.2 ms                                                | 80.0 ms: 1.04x slower                                          |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                           |
| richards                 | 45.7 ms                                                | 47.5 ms: 1.04x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 735 ms: 1.05x slower                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 72.0 ms: 1.06x slower                                          |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                          |
| scimark_fft              | 328 ms                                                 | 349 ms: 1.06x slower                                           |
| regex_dna                | 204 ms                                                 | 217 ms: 1.07x slower                                           |
| python_startup           | 8.52 ms                                                | 9.17 ms: 1.08x slower                                          |
| unpack_sequence          | 43.1 ns                                                | 46.3 ns: 1.08x slower                                          |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 58.4 ms: 1.08x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.20 us: 1.09x slower                                          |
| pyflate                  | 418 ms                                                 | 456 ms: 1.09x slower                                           |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.10x slower                                          |
| xml_etree_generate       | 76.2 ms                                                | 84.3 ms: 1.11x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.68 ms: 1.11x slower                                          |
| pickle_list              | 4.11 us                                                | 4.62 us: 1.12x slower                                          |
| async_generators         | 368 ms                                                 | 448 ms: 1.22x slower                                           |
| dask                     | 360 ms                                                 | 526 ms: 1.46x slower                                           |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (4): bench_thread_pool, logging_simple, bench_mp_pool, scimark_sor
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
