
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_symbols
- machine: linux-x86_64
- commit hash: e4c97dd
- commit date: 2023-07-05
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                |
| tornado_http   | 127 ms                                                 | 98.9 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 99.0 ms: 1.43x faster                                                 |
| float          | 111 ms                                                 | 92.8 ms: 1.19x faster                                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 140 ms: 1.26x faster                                                  |
| regex_v8       | 25.0 ms                                                | 23.3 ms: 1.07x faster                                                 |
| regex_dna      | 222 ms                                                 | 215 ms: 1.03x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.81 ms: 1.18x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 305 us: 1.49x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.43x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.89 ms: 1.37x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 57.9 ms: 1.29x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.48 sec: 1.18x faster                                                |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 85.2 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.39 us: 1.04x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.87 us: 1.01x slower                                                 |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.06x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.53 ms: 1.49x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.94 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 13.7 ms: 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                                  |
| generators               | 76.8 ms                                                | 28.8 ms: 2.67x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.74 ms: 1.99x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                                  |
| richards_super           | 90.7 ms                                                | 50.7 ms: 1.79x faster                                                 |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                                  |
| richards                 | 74.9 ms                                                | 44.5 ms: 1.68x faster                                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| chaos                    | 106 ms                                                 | 64.0 ms: 1.66x faster                                                 |
| go                       | 229 ms                                                 | 140 ms: 1.63x faster                                                  |
| scimark_sor              | 197 ms                                                 | 125 ms: 1.58x faster                                                  |
| raytrace                 | 464 ms                                                 | 296 ms: 1.57x faster                                                  |
| scimark_monte_carlo      | 108 ms                                                 | 71.9 ms: 1.51x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.37 ms: 1.50x faster                                                 |
| pickle_pure_python       | 455 us                                                 | 305 us: 1.49x faster                                                  |
| python_startup           | 14.2 ms                                                | 9.53 ms: 1.49x faster                                                 |
| async_tree_none          | 717 ms                                                 | 496 ms: 1.45x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                |
| sqlglot_transpile        | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                 |
| nbody                    | 142 ms                                                 | 99.0 ms: 1.43x faster                                                 |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.43x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 601 ms: 1.42x faster                                                  |
| hexiom                   | 9.53 ms                                                | 6.72 ms: 1.42x faster                                                 |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                 |
| pyflate                  | 673 ms                                                 | 480 ms: 1.40x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.89 ms: 1.37x faster                                                 |
| logging_format           | 8.91 us                                                | 6.51 us: 1.37x faster                                                 |
| spectral_norm            | 150 ms                                                 | 111 ms: 1.35x faster                                                  |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                |
| logging_simple           | 8.07 us                                                | 6.04 us: 1.34x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 722 ms: 1.32x faster                                                  |
| crypto_pyaes             | 118 ms                                                 | 90.1 ms: 1.31x faster                                                 |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                |
| xml_etree_process        | 74.9 ms                                                | 57.9 ms: 1.29x faster                                                 |
| tornado_http             | 127 ms                                                 | 98.9 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 740 ms: 1.29x faster                                                  |
| regex_compile            | 177 ms                                                 | 140 ms: 1.26x faster                                                  |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                                  |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                                  |
| mypy2                    | 428 ms                                                 | 343 ms: 1.25x faster                                                  |
| unpack_sequence          | 64.7 ns                                                | 52.3 ns: 1.24x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.12 us: 1.22x faster                                                 |
| sqlglot_optimize         | 65.3 ms                                                | 53.7 ms: 1.22x faster                                                 |
| float                    | 111 ms                                                 | 92.8 ms: 1.19x faster                                                 |
| tomli_loads              | 2.92 sec                                               | 2.48 sec: 1.18x faster                                                |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                |
| dulwich_log              | 75.9 ms                                                | 65.7 ms: 1.16x faster                                                 |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                                 |
| nqueens                  | 100 ms                                                 | 88.2 ms: 1.13x faster                                                 |
| scimark_fft              | 424 ms                                                 | 374 ms: 1.13x faster                                                  |
| scimark_lu               | 163 ms                                                 | 144 ms: 1.13x faster                                                  |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 839 us: 1.13x faster                                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 85.2 ms: 1.11x faster                                                 |
| comprehensions           | 26.8 us                                                | 24.6 us: 1.09x faster                                                 |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.09x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 23.3 ms: 1.07x faster                                                 |
| mako                     | 14.8 ms                                                | 13.7 ms: 1.07x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                  |
| fannkuch                 | 486 ms                                                 | 456 ms: 1.07x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.06x faster                                                 |
| gc_traversal             | 3.84 ms                                                | 3.61 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.14 ms: 1.06x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.71 sec: 1.04x faster                                                |
| pickle_list              | 4.56 us                                                | 4.39 us: 1.04x faster                                                 |
| sqlite_synth             | 2.93 us                                                | 2.83 us: 1.04x faster                                                 |
| regex_dna                | 222 ms                                                 | 215 ms: 1.03x faster                                                  |
| unpickle_list            | 4.82 us                                                | 4.87 us: 1.01x slower                                                 |
| deepcopy_memo            | 52.3 us                                                | 53.0 us: 1.01x slower                                                 |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| async_generators         | 425 ms                                                 | 448 ms: 1.05x slower                                                  |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.06x slower                                                 |
| telco                    | 6.54 ms                                                | 6.91 ms: 1.06x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.7 us: 1.16x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.81 ms: 1.18x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.94 ms: 1.19x slower                                                 |
| dask                     | 423 ms                                                 | 525 ms: 1.24x slower                                                  |
| coverage                 | 72.8 ms                                                | 94.9 ms: 1.30x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
