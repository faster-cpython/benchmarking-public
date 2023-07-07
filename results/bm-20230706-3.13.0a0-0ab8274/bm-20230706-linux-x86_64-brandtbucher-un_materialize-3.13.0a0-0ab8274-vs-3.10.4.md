
# Results vs. 3.10.4

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: 0ab8274
- commit date: 2023-07-06
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                |
| tornado_http   | 127 ms                                                 | 96.1 ms: 1.33x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.8 ms: 1.59x faster                                                 |
| float          | 111 ms                                                 | 80.4 ms: 1.38x faster                                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                 |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 300 us: 1.52x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.89 ms: 1.37x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 57.9 ms: 1.29x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.31 sec: 1.27x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 84.0 ms: 1.12x faster                                                 |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                                 |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                 |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.72 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.4 ms: 1.42x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                                  |
| generators               | 76.8 ms                                                | 28.5 ms: 2.70x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.26 ms: 2.28x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 512 ms: 1.81x faster                                                  |
| chaos                    | 106 ms                                                 | 59.6 ms: 1.78x faster                                                 |
| logging_silent           | 175 ns                                                 | 102 ns: 1.71x faster                                                  |
| richards_super           | 90.7 ms                                                | 53.0 ms: 1.71x faster                                                 |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                                  |
| scimark_sor              | 197 ms                                                 | 118 ms: 1.66x faster                                                  |
| nbody                    | 142 ms                                                 | 88.8 ms: 1.59x faster                                                 |
| richards                 | 74.9 ms                                                | 47.1 ms: 1.59x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.01 ms: 1.58x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.53x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 77.5 ms: 1.53x faster                                                 |
| pyflate                  | 673 ms                                                 | 441 ms: 1.53x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 300 us: 1.52x faster                                                  |
| scimark_monte_carlo      | 108 ms                                                 | 71.7 ms: 1.51x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                |
| async_tree_none          | 717 ms                                                 | 482 ms: 1.49x faster                                                  |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.48x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.47x faster                                                 |
| async_tree_memoization   | 854 ms                                                 | 589 ms: 1.45x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                  |
| mako                     | 14.8 ms                                                | 10.4 ms: 1.42x faster                                                 |
| coroutines               | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                 |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.41x faster                                                  |
| deepcopy_memo            | 52.3 us                                                | 37.2 us: 1.41x faster                                                 |
| logging_format           | 8.91 us                                                | 6.40 us: 1.39x faster                                                 |
| logging_simple           | 8.07 us                                                | 5.83 us: 1.38x faster                                                 |
| float                    | 111 ms                                                 | 80.4 ms: 1.38x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.89 ms: 1.37x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                                |
| unpack_sequence          | 64.7 ns                                                | 48.1 ns: 1.35x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 716 ms: 1.33x faster                                                  |
| tornado_http             | 127 ms                                                 | 96.1 ms: 1.33x faster                                                 |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 727 ms: 1.31x faster                                                  |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 57.9 ms: 1.29x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.29x faster                                                 |
| deepcopy                 | 442 us                                                 | 348 us: 1.27x faster                                                  |
| nqueens                  | 100 ms                                                 | 79.0 ms: 1.27x faster                                                 |
| tomli_loads              | 2.92 sec                                               | 2.31 sec: 1.27x faster                                                |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.10 us: 1.23x faster                                                 |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                |
| scimark_fft              | 424 ms                                                 | 355 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.62 ms: 1.18x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 814 us: 1.16x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 65.5 ms: 1.16x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.0 ms: 1.12x faster                                                 |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                                 |
| json                     | 5.42 ms                                                | 4.92 ms: 1.10x faster                                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.65 sec: 1.06x faster                                                |
| sqlite_synth             | 2.93 us                                                | 2.77 us: 1.06x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| regex_dna                | 222 ms                                                 | 211 ms: 1.05x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                 |
| pickle_list              | 4.56 us                                                | 4.64 us: 1.02x slower                                                 |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| async_generators         | 425 ms                                                 | 448 ms: 1.05x slower                                                  |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| telco                    | 6.54 ms                                                | 7.26 ms: 1.11x slower                                                 |
| gc_traversal             | 3.84 ms                                                | 4.33 ms: 1.13x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.72 ms: 1.15x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                                 |
| dask                     | 423 ms                                                 | 516 ms: 1.22x slower                                                  |
| coverage                 | 72.8 ms                                                | 91.3 ms: 1.25x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
