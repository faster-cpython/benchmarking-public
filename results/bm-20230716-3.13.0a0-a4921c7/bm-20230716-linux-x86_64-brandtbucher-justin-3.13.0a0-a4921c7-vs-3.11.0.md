
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                        |
| tornado_http   | 96.3 ms                                                | 98.7 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                          |
| nbody          | 93.1 ms                                                | 96.3 ms: 1.03x slower                                         |
| float          | 77.2 ms                                                | 91.2 ms: 1.18x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.41 ms: 1.17x faster                                         |
| regex_dna      | 204 ms                                                 | 201 ms: 1.02x faster                                          |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                         |
| regex_compile  | 138 ms                                                 | 142 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                         |
| json_loads           | 26.5 us                                                | 24.9 us: 1.06x faster                                         |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                          |
| unpickle_pure_python | 228 us                                                 | 221 us: 1.03x faster                                          |
| unpickle_list        | 4.91 us                                                | 4.86 us: 1.01x faster                                         |
| pickle_dict          | 31.1 us                                                | 31.1 us: 1.00x faster                                         |
| pickle_pure_python   | 306 us                                                 | 317 us: 1.04x slower                                          |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                         |
| xml_etree_process    | 53.9 ms                                                | 58.8 ms: 1.09x slower                                         |
| tomli_loads          | 2.22 sec                                               | 2.47 sec: 1.11x slower                                        |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                         |
| pickle_list          | 4.11 us                                                | 4.62 us: 1.12x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 86.8 ms: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.48 ms: 1.11x slower                                         |
| python_startup_no_site | 6.01 ms                                                | 6.90 ms: 1.15x slower                                         |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 13.4 ms: 1.33x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                          |
| generators               | 73.5 ms                                                | 29.4 ms: 2.50x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                          |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                        |
| json_dumps               | 12.6 ms                                                | 9.76 ms: 1.29x faster                                         |
| mypy2                    | 420 ms                                                 | 343 ms: 1.22x faster                                          |
| regex_effbot             | 3.99 ms                                                | 3.41 ms: 1.17x faster                                         |
| coroutines               | 25.5 ms                                                | 22.7 ms: 1.12x faster                                         |
| richards_super           | 56.8 ms                                                | 51.2 ms: 1.11x faster                                         |
| chaos                    | 69.2 ms                                                | 64.6 ms: 1.07x faster                                         |
| coverage                 | 100 ms                                                 | 93.8 ms: 1.07x faster                                         |
| json_loads               | 26.5 us                                                | 24.9 us: 1.06x faster                                         |
| async_tree_none          | 526 ms                                                 | 499 ms: 1.05x faster                                          |
| async_tree_io            | 1.30 sec                                               | 1.24 sec: 1.05x faster                                        |
| json                     | 4.94 ms                                                | 4.77 ms: 1.04x faster                                         |
| async_tree_memoization   | 627 ms                                                 | 606 ms: 1.03x faster                                          |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                          |
| unpickle_pure_python     | 228 us                                                 | 221 us: 1.03x faster                                          |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                          |
| logging_format           | 6.68 us                                                | 6.55 us: 1.02x faster                                         |
| mdp                      | 2.62 sec                                               | 2.57 sec: 1.02x faster                                        |
| regex_dna                | 204 ms                                                 | 201 ms: 1.02x faster                                          |
| richards                 | 45.7 ms                                                | 45.0 ms: 1.02x faster                                         |
| sqlglot_parse            | 1.40 ms                                                | 1.38 ms: 1.02x faster                                         |
| meteor_contest           | 107 ms                                                 | 106 ms: 1.01x faster                                          |
| unpickle_list            | 4.91 us                                                | 4.86 us: 1.01x faster                                         |
| logging_simple           | 6.03 us                                                | 5.99 us: 1.01x faster                                         |
| pickle_dict              | 31.1 us                                                | 31.1 us: 1.00x faster                                         |
| sqlglot_normalize        | 108 ms                                                 | 108 ms: 1.00x slower                                          |
| raytrace                 | 297 ms                                                 | 299 ms: 1.01x slower                                          |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                         |
| sqlglot_optimize         | 53.1 ms                                                | 54.1 ms: 1.02x slower                                         |
| bench_thread_pool        | 819 us                                                 | 839 us: 1.02x slower                                          |
| tornado_http             | 96.3 ms                                                | 98.7 ms: 1.03x slower                                         |
| go                       | 140 ms                                                 | 144 ms: 1.03x slower                                          |
| dulwich_log              | 63.7 ms                                                | 65.5 ms: 1.03x slower                                         |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                        |
| regex_compile            | 138 ms                                                 | 142 ms: 1.03x slower                                          |
| deltablue                | 3.67 ms                                                | 3.79 ms: 1.03x slower                                         |
| nbody                    | 93.1 ms                                                | 96.3 ms: 1.03x slower                                         |
| pickle_pure_python       | 306 us                                                 | 317 us: 1.04x slower                                          |
| pathlib                  | 18.2 ms                                                | 18.9 ms: 1.04x slower                                         |
| nqueens                  | 83.4 ms                                                | 86.7 ms: 1.04x slower                                         |
| pprint_pformat           | 1.46 sec                                               | 1.52 sec: 1.04x slower                                        |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                         |
| deepcopy                 | 342 us                                                 | 362 us: 1.06x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 742 ms: 1.06x slower                                          |
| telco                    | 6.58 ms                                                | 6.98 ms: 1.06x slower                                         |
| scimark_monte_carlo      | 68.1 ms                                                | 72.6 ms: 1.07x slower                                         |
| hexiom                   | 6.37 ms                                                | 6.82 ms: 1.07x slower                                         |
| gc_traversal             | 4.02 ms                                                | 4.32 ms: 1.07x slower                                         |
| scimark_sor              | 118 ms                                                 | 128 ms: 1.08x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.09x slower                                         |
| logging_silent           | 101 ns                                                 | 110 ns: 1.09x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 58.8 ms: 1.09x slower                                         |
| sqlite_synth             | 2.52 us                                                | 2.77 us: 1.10x slower                                         |
| comprehensions           | 22.4 us                                                | 24.7 us: 1.10x slower                                         |
| spectral_norm            | 100 ms                                                 | 111 ms: 1.11x slower                                          |
| tomli_loads              | 2.22 sec                                               | 2.47 sec: 1.11x slower                                        |
| python_startup           | 8.52 ms                                                | 9.48 ms: 1.11x slower                                         |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                         |
| pickle_list              | 4.11 us                                                | 4.62 us: 1.12x slower                                         |
| scimark_fft              | 328 ms                                                 | 371 ms: 1.13x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.10 ms: 1.13x slower                                         |
| xml_etree_generate       | 76.2 ms                                                | 86.8 ms: 1.14x slower                                         |
| pyflate                  | 418 ms                                                 | 480 ms: 1.15x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.90 ms: 1.15x slower                                         |
| fannkuch                 | 388 ms                                                 | 448 ms: 1.16x slower                                          |
| float                    | 77.2 ms                                                | 91.2 ms: 1.18x slower                                         |
| crypto_pyaes             | 74.7 ms                                                | 88.5 ms: 1.18x slower                                         |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                          |
| scimark_lu               | 110 ms                                                 | 142 ms: 1.30x slower                                          |
| mako                     | 10.1 ms                                                | 13.4 ms: 1.33x slower                                         |
| deepcopy_memo            | 37.0 us                                                | 53.6 us: 1.45x slower                                         |
| dask                     | 360 ms                                                 | 529 ms: 1.47x slower                                          |
| Geometric mean           | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (7): pycparser, xml_etree_iterparse, bench_mp_pool, create_gc_cycles, async_tree_cpu_io_mixed, unpack_sequence, sqlglot_transpile
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
