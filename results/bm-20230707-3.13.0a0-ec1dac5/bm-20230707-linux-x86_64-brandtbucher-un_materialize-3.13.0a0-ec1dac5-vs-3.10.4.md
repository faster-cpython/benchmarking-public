
# Results vs. 3.10.4

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: ec1dac5
- commit date: 2023-07-07
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.19x faster                                                |
| tornado_http   | 127 ms                                                 | 96.2 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.3 ms: 1.55x faster                                                 |
| float          | 111 ms                                                 | 79.7 ms: 1.39x faster                                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                 |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 300 us: 1.52x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.41x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.69 ms: 1.40x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 57.5 ms: 1.30x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.28 sec: 1.28x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 83.5 ms: 1.13x faster                                                 |
| json_loads           | 28.8 us                                                | 25.6 us: 1.12x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                 |
| unpickle_list        | 4.82 us                                                | 5.10 us: 1.06x slower                                                 |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                 |
| pickle_list          | 4.56 us                                                | 4.93 us: 1.08x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.19 ms: 1.54x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                                  |
| generators               | 76.8 ms                                                | 28.7 ms: 2.68x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.30 ms: 2.25x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 510 ms: 1.81x faster                                                  |
| chaos                    | 106 ms                                                 | 59.4 ms: 1.79x faster                                                 |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                                  |
| richards_super           | 90.7 ms                                                | 52.8 ms: 1.72x faster                                                 |
| raytrace                 | 464 ms                                                 | 275 ms: 1.69x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                  |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.63x faster                                                  |
| richards                 | 74.9 ms                                                | 46.7 ms: 1.61x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 75.9 ms: 1.56x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.13 ms: 1.55x faster                                                 |
| nbody                    | 142 ms                                                 | 91.3 ms: 1.55x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.54x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.19 ms: 1.54x faster                                                 |
| pickle_pure_python       | 455 us                                                 | 300 us: 1.52x faster                                                  |
| pyflate                  | 673 ms                                                 | 445 ms: 1.51x faster                                                  |
| unpack_sequence          | 64.7 ns                                                | 42.9 ns: 1.51x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 72.1 ms: 1.50x faster                                                 |
| async_tree_none          | 717 ms                                                 | 482 ms: 1.49x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.49x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 587 ms: 1.45x faster                                                  |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.42x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.41x faster                                                  |
| coroutines               | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.69 ms: 1.40x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 37.5 us: 1.40x faster                                                 |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                 |
| float                    | 111 ms                                                 | 79.7 ms: 1.39x faster                                                 |
| logging_format           | 8.91 us                                                | 6.48 us: 1.38x faster                                                 |
| logging_simple           | 8.07 us                                                | 5.90 us: 1.37x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                                |
| pprint_safe_repr         | 955 ms                                                 | 711 ms: 1.34x faster                                                  |
| tornado_http             | 127 ms                                                 | 96.2 ms: 1.32x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 718 ms: 1.32x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 57.5 ms: 1.30x faster                                                 |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                                 |
| tomli_loads              | 2.92 sec                                               | 2.28 sec: 1.28x faster                                                |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                                  |
| deepcopy                 | 442 us                                                 | 347 us: 1.27x faster                                                  |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                                |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                                  |
| nqueens                  | 100 ms                                                 | 79.9 ms: 1.25x faster                                                 |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.13 us: 1.22x faster                                                 |
| scimark_fft              | 424 ms                                                 | 352 ms: 1.21x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.19x faster                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.61 ms: 1.18x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 818 us: 1.16x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 65.6 ms: 1.16x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.5 ms: 1.13x faster                                                 |
| json_loads               | 28.8 us                                                | 25.6 us: 1.12x faster                                                 |
| json                     | 5.42 ms                                                | 4.84 ms: 1.12x faster                                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                 |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| mdp                      | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                |
| regex_dna                | 222 ms                                                 | 213 ms: 1.04x faster                                                  |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                                  |
| unpickle_list            | 4.82 us                                                | 5.10 us: 1.06x slower                                                 |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                                 |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                 |
| pickle_list              | 4.56 us                                                | 4.93 us: 1.08x slower                                                 |
| telco                    | 6.54 ms                                                | 7.11 ms: 1.09x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                                 |
| dask                     | 423 ms                                                 | 520 ms: 1.23x slower                                                  |
| coverage                 | 72.8 ms                                                | 93.8 ms: 1.29x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
