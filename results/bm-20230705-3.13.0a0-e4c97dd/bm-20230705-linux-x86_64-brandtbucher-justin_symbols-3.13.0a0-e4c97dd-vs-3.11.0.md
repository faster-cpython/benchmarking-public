
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_symbols
- machine: linux-x86_64
- commit hash: e4c97dd
- commit date: 2023-07-05
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                |
| tornado_http   | 96.3 ms                                                | 98.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                                  |
| nbody          | 93.1 ms                                                | 99.0 ms: 1.06x slower                                                 |
| float          | 77.2 ms                                                | 92.8 ms: 1.20x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.81 ms: 1.05x faster                                                 |
| regex_compile  | 138 ms                                                 | 140 ms: 1.02x slower                                                  |
| regex_dna      | 204 ms                                                 | 215 ms: 1.05x slower                                                  |
| regex_v8       | 22.0 ms                                                | 23.3 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.89 ms: 1.27x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 211 us: 1.08x faster                                                  |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| unpickle_list        | 4.91 us                                                | 4.87 us: 1.01x faster                                                 |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                                 |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.39 us: 1.07x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 57.9 ms: 1.08x slower                                                 |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| tomli_loads          | 2.22 sec                                               | 2.48 sec: 1.12x slower                                                |
| xml_etree_generate   | 76.2 ms                                                | 85.2 ms: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.53 ms: 1.12x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.94 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 13.7 ms: 1.36x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                                  |
| generators               | 73.5 ms                                                | 28.8 ms: 2.55x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.89 ms: 1.27x faster                                                 |
| mypy2                    | 420 ms                                                 | 343 ms: 1.22x faster                                                  |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                                 |
| richards_super           | 56.8 ms                                                | 50.7 ms: 1.12x faster                                                 |
| gc_traversal             | 4.02 ms                                                | 3.61 ms: 1.11x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 211 us: 1.08x faster                                                  |
| chaos                    | 69.2 ms                                                | 64.0 ms: 1.08x faster                                                 |
| async_tree_none          | 526 ms                                                 | 496 ms: 1.06x faster                                                  |
| json_loads               | 26.5 us                                                | 25.1 us: 1.06x faster                                                 |
| coverage                 | 100 ms                                                 | 94.9 ms: 1.05x faster                                                 |
| async_tree_io            | 1.30 sec                                               | 1.23 sec: 1.05x faster                                                |
| regex_effbot             | 3.99 ms                                                | 3.81 ms: 1.05x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 601 ms: 1.04x faster                                                  |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                  |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                 |
| richards                 | 45.7 ms                                                | 44.5 ms: 1.03x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| logging_format           | 6.68 us                                                | 6.51 us: 1.03x faster                                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.37 ms: 1.02x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| meteor_contest           | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| unpickle_list            | 4.91 us                                                | 4.87 us: 1.01x faster                                                 |
| pidigits                 | 198 ms                                                 | 197 ms: 1.01x faster                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                |
| sqlglot_optimize         | 53.1 ms                                                | 53.7 ms: 1.01x slower                                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                                 |
| regex_compile            | 138 ms                                                 | 140 ms: 1.02x slower                                                  |
| deltablue                | 3.67 ms                                                | 3.74 ms: 1.02x slower                                                 |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                  |
| pickle_dict              | 31.1 us                                                | 31.7 us: 1.02x slower                                                 |
| bench_thread_pool        | 819 us                                                 | 839 us: 1.02x slower                                                  |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                                  |
| tornado_http             | 96.3 ms                                                | 98.9 ms: 1.03x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 722 ms: 1.03x slower                                                  |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 65.7 ms: 1.03x slower                                                 |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                |
| mdp                      | 2.62 sec                                               | 2.71 sec: 1.04x slower                                                |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                                 |
| telco                    | 6.58 ms                                                | 6.91 ms: 1.05x slower                                                 |
| regex_dna                | 204 ms                                                 | 215 ms: 1.05x slower                                                  |
| hexiom                   | 6.37 ms                                                | 6.72 ms: 1.05x slower                                                 |
| scimark_sor              | 118 ms                                                 | 125 ms: 1.06x slower                                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 71.9 ms: 1.06x slower                                                 |
| regex_v8                 | 22.0 ms                                                | 23.3 ms: 1.06x slower                                                 |
| nqueens                  | 83.4 ms                                                | 88.2 ms: 1.06x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.12 us: 1.06x slower                                                 |
| nbody                    | 93.1 ms                                                | 99.0 ms: 1.06x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.39 us: 1.07x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 57.9 ms: 1.08x slower                                                 |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| comprehensions           | 22.4 us                                                | 24.6 us: 1.09x slower                                                 |
| spectral_norm            | 100 ms                                                 | 111 ms: 1.11x slower                                                  |
| tomli_loads              | 2.22 sec                                               | 2.48 sec: 1.12x slower                                                |
| python_startup           | 8.52 ms                                                | 9.53 ms: 1.12x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 85.2 ms: 1.12x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.83 us: 1.12x slower                                                 |
| scimark_fft              | 328 ms                                                 | 374 ms: 1.14x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.14 ms: 1.14x slower                                                 |
| pyflate                  | 418 ms                                                 | 480 ms: 1.15x slower                                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.94 ms: 1.16x slower                                                 |
| fannkuch                 | 388 ms                                                 | 456 ms: 1.18x slower                                                  |
| float                    | 77.2 ms                                                | 92.8 ms: 1.20x slower                                                 |
| crypto_pyaes             | 74.7 ms                                                | 90.1 ms: 1.21x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 52.3 ns: 1.21x slower                                                 |
| async_generators         | 368 ms                                                 | 448 ms: 1.22x slower                                                  |
| scimark_lu               | 110 ms                                                 | 144 ms: 1.31x slower                                                  |
| mako                     | 10.1 ms                                                | 13.7 ms: 1.36x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 53.0 us: 1.43x slower                                                 |
| dask                     | 360 ms                                                 | 525 ms: 1.46x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (8): raytrace, pickle_pure_python, bench_mp_pool, sqlglot_transpile, logging_simple, sqlglot_normalize, async_tree_cpu_io_mixed, go
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
