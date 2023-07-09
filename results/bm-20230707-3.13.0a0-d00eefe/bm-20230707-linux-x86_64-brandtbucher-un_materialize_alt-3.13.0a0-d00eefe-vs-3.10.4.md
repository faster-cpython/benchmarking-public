
# Results vs. 3.10.4

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: d00eefe
- commit date: 2023-07-07
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                    |
| tornado_http   | 127 ms                                                 | 96.0 ms: 1.33x faster                                                     |
| Geometric mean | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.4 ms: 1.58x faster                                                     |
| float          | 111 ms                                                 | 79.3 ms: 1.39x faster                                                     |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                     |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 302 us: 1.51x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 57.5 ms: 1.30x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                     |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                      |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                                     |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                                     |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.26 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.73 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.5 ms: 1.40x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 144 us: 3.54x faster                                                      |
| generators               | 76.8 ms                                                | 28.6 ms: 2.69x faster                                                     |
| deltablue                | 7.42 ms                                                | 3.29 ms: 2.26x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                                      |
| chaos                    | 106 ms                                                 | 58.9 ms: 1.81x faster                                                     |
| richards_super           | 90.7 ms                                                | 52.5 ms: 1.73x faster                                                     |
| raytrace                 | 464 ms                                                 | 271 ms: 1.71x faster                                                      |
| logging_silent           | 175 ns                                                 | 104 ns: 1.68x faster                                                      |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 139 ms: 1.65x faster                                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.63x faster                                                      |
| richards                 | 74.9 ms                                                | 47.1 ms: 1.59x faster                                                     |
| nbody                    | 142 ms                                                 | 89.4 ms: 1.58x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.06 ms: 1.57x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.26 ms: 1.53x faster                                                     |
| crypto_pyaes             | 118 ms                                                 | 77.9 ms: 1.52x faster                                                     |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                                      |
| pickle_pure_python       | 455 us                                                 | 302 us: 1.51x faster                                                      |
| scimark_monte_carlo      | 108 ms                                                 | 72.1 ms: 1.50x faster                                                     |
| unpack_sequence          | 64.7 ns                                                | 43.1 ns: 1.50x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                    |
| async_tree_none          | 717 ms                                                 | 484 ms: 1.48x faster                                                      |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 588 ms: 1.45x faster                                                      |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                      |
| mako                     | 14.8 ms                                                | 10.5 ms: 1.40x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 37.3 us: 1.40x faster                                                     |
| float                    | 111 ms                                                 | 79.3 ms: 1.39x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                     |
| logging_format           | 8.91 us                                                | 6.50 us: 1.37x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.90 us: 1.37x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                    |
| tornado_http             | 127 ms                                                 | 96.0 ms: 1.33x faster                                                     |
| pprint_safe_repr         | 955 ms                                                 | 720 ms: 1.33x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 729 ms: 1.30x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.6 us: 1.30x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 57.5 ms: 1.30x faster                                                     |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                                    |
| fannkuch                 | 486 ms                                                 | 391 ms: 1.24x faster                                                      |
| nqueens                  | 100 ms                                                 | 81.6 ms: 1.23x faster                                                     |
| sqlglot_optimize         | 65.3 ms                                                | 53.3 ms: 1.23x faster                                                     |
| scimark_fft              | 424 ms                                                 | 351 ms: 1.21x faster                                                      |
| docutils                 | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                    |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.70 ms: 1.16x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 817 us: 1.16x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 65.6 ms: 1.16x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                     |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                     |
| json                     | 5.42 ms                                                | 4.91 ms: 1.10x faster                                                     |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| gc_traversal             | 3.84 ms                                                | 3.56 ms: 1.08x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                     |
| pathlib                  | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.70 sec: 1.05x faster                                                    |
| regex_dna                | 222 ms                                                 | 213 ms: 1.04x faster                                                      |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                     |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                      |
| unpickle_list            | 4.82 us                                                | 5.00 us: 1.04x slower                                                     |
| async_generators         | 425 ms                                                 | 447 ms: 1.05x slower                                                      |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                                     |
| telco                    | 6.54 ms                                                | 7.10 ms: 1.09x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                     |
| pickle_dict              | 27.3 us                                                | 30.8 us: 1.13x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.73 ms: 1.16x slower                                                     |
| dask                     | 423 ms                                                 | 517 ms: 1.22x slower                                                      |
| coverage                 | 72.8 ms                                                | 95.6 ms: 1.31x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (2): pickle_list, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
