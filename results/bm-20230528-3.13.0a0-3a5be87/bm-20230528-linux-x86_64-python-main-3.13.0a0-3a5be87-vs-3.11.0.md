
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.72 sec: 1.03x slower                                |
| tornado_http   | 96.3 ms                                                | 102 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.2 ms: 1.04x faster                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                  |
| float          | 77.2 ms                                                | 82.2 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                 |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                  |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.89 ms: 1.27x faster                                 |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                  |
| unpickle_pure_python | 228 us                                                 | 223 us: 1.02x faster                                  |
| tomli_loads          | 2.22 sec                                               | 2.21 sec: 1.01x faster                                |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                 |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                 |
| pickle_dict          | 31.1 us                                                | 32.6 us: 1.05x slower                                 |
| pickle_pure_python   | 306 us                                                 | 322 us: 1.05x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.0 ms: 1.10x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.8 ms: 1.11x slower                                 |
| unpickle             | 13.7 us                                                | 15.3 us: 1.12x slower                                 |
| pickle_list          | 4.11 us                                                | 4.66 us: 1.13x slower                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.29 ms: 1.09x slower                                 |
| python_startup_no_site | 6.01 ms                                                | 6.75 ms: 1.12x slower                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.1 ms                                                | 11.0 ms: 1.09x slower                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.39x faster                                  |
| generators               | 73.5 ms                                                | 31.3 ms: 2.34x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 514 ms: 1.79x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                |
| json_dumps               | 12.6 ms                                                | 9.89 ms: 1.27x faster                                 |
| mypy2                    | 420 ms                                                 | 347 ms: 1.21x faster                                  |
| coroutines               | 25.5 ms                                                | 22.3 ms: 1.14x faster                                 |
| richards_super           | 56.8 ms                                                | 50.1 ms: 1.13x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.56 ms: 1.12x faster                                 |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.08x faster                                 |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                 |
| async_tree_none          | 526 ms                                                 | 500 ms: 1.05x faster                                  |
| deltablue                | 3.67 ms                                                | 3.50 ms: 1.05x faster                                 |
| chaos                    | 69.2 ms                                                | 66.1 ms: 1.05x faster                                 |
| nbody                    | 93.1 ms                                                | 89.2 ms: 1.04x faster                                 |
| async_tree_io            | 1.30 sec                                               | 1.24 sec: 1.04x faster                                |
| sqlglot_parse            | 1.40 ms                                                | 1.35 ms: 1.04x faster                                 |
| async_tree_memoization   | 627 ms                                                 | 606 ms: 1.03x faster                                  |
| json                     | 4.94 ms                                                | 4.78 ms: 1.03x faster                                 |
| coverage                 | 100 ms                                                 | 97.0 ms: 1.03x faster                                 |
| richards                 | 45.7 ms                                                | 44.4 ms: 1.03x faster                                 |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 223 us: 1.02x faster                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.68 ms: 1.02x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.29 ms: 1.01x faster                                 |
| nqueens                  | 83.4 ms                                                | 82.4 ms: 1.01x faster                                 |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                  |
| tomli_loads              | 2.22 sec                                               | 2.21 sec: 1.01x faster                                |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                  |
| sqlglot_normalize        | 108 ms                                                 | 108 ms: 1.01x slower                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                 |
| pycparser                | 1.18 sec                                               | 1.19 sec: 1.01x slower                                |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                 |
| unpickle_list            | 4.91 us                                                | 4.98 us: 1.01x slower                                 |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                  |
| raytrace                 | 297 ms                                                 | 302 ms: 1.02x slower                                  |
| sqlglot_optimize         | 53.1 ms                                                | 54.1 ms: 1.02x slower                                 |
| bench_thread_pool        | 819 us                                                 | 834 us: 1.02x slower                                  |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                  |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.03x slower                                |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                 |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.04x slower                                |
| scimark_lu               | 110 ms                                                 | 115 ms: 1.05x slower                                  |
| pickle_dict              | 31.1 us                                                | 32.6 us: 1.05x slower                                 |
| telco                    | 6.58 ms                                                | 6.91 ms: 1.05x slower                                 |
| pickle_pure_python       | 306 us                                                 | 322 us: 1.05x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 739 ms: 1.05x slower                                  |
| regex_compile            | 138 ms                                                 | 146 ms: 1.06x slower                                  |
| scimark_sor              | 118 ms                                                 | 125 ms: 1.06x slower                                  |
| crypto_pyaes             | 74.7 ms                                                | 79.3 ms: 1.06x slower                                 |
| logging_silent           | 101 ns                                                 | 107 ns: 1.06x slower                                  |
| tornado_http             | 96.3 ms                                                | 102 ms: 1.06x slower                                  |
| logging_format           | 6.68 us                                                | 7.10 us: 1.06x slower                                 |
| float                    | 77.2 ms                                                | 82.2 ms: 1.06x slower                                 |
| deepcopy                 | 342 us                                                 | 364 us: 1.06x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 39.4 us: 1.07x slower                                 |
| scimark_fft              | 328 ms                                                 | 350 ms: 1.07x slower                                  |
| dulwich_log              | 63.7 ms                                                | 68.0 ms: 1.07x slower                                 |
| logging_simple           | 6.03 us                                                | 6.47 us: 1.07x slower                                 |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.84 ms: 1.08x slower                                 |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 73.6 ms: 1.08x slower                                 |
| pathlib                  | 18.2 ms                                                | 19.7 ms: 1.08x slower                                 |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                 |
| mako                     | 10.1 ms                                                | 11.0 ms: 1.09x slower                                 |
| python_startup           | 8.52 ms                                                | 9.29 ms: 1.09x slower                                 |
| xml_etree_process        | 53.9 ms                                                | 59.0 ms: 1.10x slower                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.25 us: 1.11x slower                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.8 ms: 1.11x slower                                 |
| unpickle                 | 13.7 us                                                | 15.3 us: 1.12x slower                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.75 ms: 1.12x slower                                 |
| pickle_list              | 4.11 us                                                | 4.66 us: 1.13x slower                                 |
| unpack_sequence          | 43.1 ns                                                | 51.6 ns: 1.20x slower                                 |
| async_generators         | 368 ms                                                 | 454 ms: 1.23x slower                                  |
| dask                     | 360 ms                                                 | 537 ms: 1.49x slower                                  |
| Geometric mean           | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (6): meteor_contest, xml_etree_iterparse, mdp, regex_v8, bench_mp_pool, async_tree_cpu_io_mixed
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
