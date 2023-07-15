
# Results vs. 3.10.4

- fork: gvanrossum
- ref: simple_calls_with_xu
- machine: linux-x86_64
- commit hash: db6241c
- commit date: 2023-07-15
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.75 sec: 1.15x faster                                                    |
| tornado_http   | 127 ms                                                 | 98.2 ms: 1.30x faster                                                     |
| Geometric mean | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 100 ms: 1.42x faster                                                      |
| float          | 111 ms                                                 | 85.6 ms: 1.29x faster                                                     |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 151 ms: 1.17x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 302 us: 1.51x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 226 us: 1.33x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.27x faster                                                     |
| json_loads           | 28.8 us                                                | 26.0 us: 1.11x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.68 sec: 1.09x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 86.7 ms: 1.09x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                      |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                                     |
| pickle_list          | 4.56 us                                                | 4.73 us: 1.04x slower                                                     |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| pickle               | 10.3 us                                                | 11.0 us: 1.07x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 12.2 ms: 1.21x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 152 us: 3.36x faster                                                      |
| generators               | 76.8 ms                                                | 28.5 ms: 2.69x faster                                                     |
| deltablue                | 7.42 ms                                                | 3.70 ms: 2.00x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 511 ms: 1.81x faster                                                      |
| logging_silent           | 175 ns                                                 | 102 ns: 1.71x faster                                                      |
| chaos                    | 106 ms                                                 | 63.4 ms: 1.68x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                                    |
| raytrace                 | 464 ms                                                 | 280 ms: 1.66x faster                                                      |
| richards_super           | 90.7 ms                                                | 54.9 ms: 1.65x faster                                                     |
| scimark_sor              | 197 ms                                                 | 124 ms: 1.58x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 75.4 ms: 1.57x faster                                                     |
| go                       | 229 ms                                                 | 146 ms: 1.57x faster                                                      |
| scimark_monte_carlo      | 108 ms                                                 | 69.2 ms: 1.56x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                                     |
| richards                 | 74.9 ms                                                | 48.8 ms: 1.53x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 302 us: 1.51x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                    |
| async_tree_none          | 717 ms                                                 | 485 ms: 1.48x faster                                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.48x faster                                                     |
| coroutines               | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                     |
| async_tree_memoization   | 854 ms                                                 | 592 ms: 1.44x faster                                                      |
| nbody                    | 142 ms                                                 | 100 ms: 1.42x faster                                                      |
| pyflate                  | 673 ms                                                 | 482 ms: 1.40x faster                                                      |
| scimark_lu               | 163 ms                                                 | 118 ms: 1.39x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 46.9 ns: 1.38x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                     |
| logging_simple           | 8.07 us                                                | 6.03 us: 1.34x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 226 us: 1.33x faster                                                      |
| spectral_norm            | 150 ms                                                 | 113 ms: 1.33x faster                                                      |
| logging_format           | 8.91 us                                                | 6.73 us: 1.32x faster                                                     |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 725 ms: 1.31x faster                                                      |
| pprint_pformat           | 1.99 sec                                               | 1.53 sec: 1.30x faster                                                    |
| tornado_http             | 127 ms                                                 | 98.2 ms: 1.30x faster                                                     |
| float                    | 111 ms                                                 | 85.6 ms: 1.29x faster                                                     |
| pprint_safe_repr         | 955 ms                                                 | 752 ms: 1.27x faster                                                      |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.27x faster                                                     |
| hexiom                   | 9.53 ms                                                | 7.57 ms: 1.26x faster                                                     |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.25x faster                                                    |
| mypy2                    | 428 ms                                                 | 347 ms: 1.24x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                                      |
| deepcopy                 | 442 us                                                 | 364 us: 1.21x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 43.1 us: 1.21x faster                                                     |
| mako                     | 14.8 ms                                                | 12.2 ms: 1.21x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                                     |
| sqlglot_optimize         | 65.3 ms                                                | 55.3 ms: 1.18x faster                                                     |
| regex_compile            | 177 ms                                                 | 151 ms: 1.17x faster                                                      |
| docutils                 | 3.17 sec                                               | 2.75 sec: 1.15x faster                                                    |
| dulwich_log              | 75.9 ms                                                | 66.6 ms: 1.14x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 848 us: 1.12x faster                                                      |
| json_loads               | 28.8 us                                                | 26.0 us: 1.11x faster                                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                                     |
| tomli_loads              | 2.92 sec                                               | 2.68 sec: 1.09x faster                                                    |
| scimark_fft              | 424 ms                                                 | 390 ms: 1.09x faster                                                      |
| xml_etree_generate       | 94.2 ms                                                | 86.7 ms: 1.09x faster                                                     |
| json                     | 5.42 ms                                                | 5.02 ms: 1.08x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                      |
| comprehensions           | 26.8 us                                                | 25.1 us: 1.07x faster                                                     |
| regex_dna                | 222 ms                                                 | 210 ms: 1.06x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.80 us: 1.05x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 106 ms: 1.05x faster                                                      |
| pathlib                  | 20.0 ms                                                | 19.1 ms: 1.05x faster                                                     |
| gc_traversal             | 3.84 ms                                                | 3.73 ms: 1.03x faster                                                     |
| fannkuch                 | 486 ms                                                 | 477 ms: 1.02x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.83 sec: 1.00x slower                                                    |
| nqueens                  | 100 ms                                                 | 101 ms: 1.01x slower                                                      |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| meteor_contest           | 115 ms                                                 | 117 ms: 1.01x slower                                                      |
| unpickle_list            | 4.82 us                                                | 4.93 us: 1.02x slower                                                     |
| pickle_list              | 4.56 us                                                | 4.73 us: 1.04x slower                                                     |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| pickle                   | 10.3 us                                                | 11.0 us: 1.07x slower                                                     |
| async_generators         | 425 ms                                                 | 465 ms: 1.09x slower                                                      |
| regex_effbot             | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                     |
| telco                    | 6.54 ms                                                | 7.31 ms: 1.12x slower                                                     |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 6.45 ms: 1.18x slower                                                     |
| dask                     | 423 ms                                                 | 531 ms: 1.26x slower                                                      |
| coverage                 | 72.8 ms                                                | 93.9 ms: 1.29x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
