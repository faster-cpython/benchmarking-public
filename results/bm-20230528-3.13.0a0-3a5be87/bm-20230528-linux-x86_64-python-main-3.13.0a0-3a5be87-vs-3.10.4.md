
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.72 sec: 1.17x faster                                |
| tornado_http   | 127 ms                                                 | 102 ms: 1.25x faster                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.2 ms: 1.59x faster                                 |
| float          | 111 ms                                                 | 82.2 ms: 1.35x faster                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                  |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                 |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 322 us: 1.41x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.89 ms: 1.37x faster                                 |
| unpickle_pure_python | 300 us                                                 | 223 us: 1.34x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                |
| xml_etree_process    | 74.9 ms                                                | 59.0 ms: 1.27x faster                                 |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.8 ms: 1.11x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                 |
| pickle_list          | 4.56 us                                                | 4.66 us: 1.02x slower                                 |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                 |
| unpickle             | 14.1 us                                                | 15.3 us: 1.08x slower                                 |
| pickle_dict          | 27.3 us                                                | 32.6 us: 1.20x slower                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.29 ms: 1.52x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.75 ms: 1.16x slower                                 |
| Geometric mean         | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 11.0 ms: 1.34x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-linux-x86_64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.56x faster                                  |
| generators               | 76.8 ms                                                | 31.3 ms: 2.45x faster                                 |
| deltablue                | 7.42 ms                                                | 3.50 ms: 2.12x faster                                 |
| richards_super           | 90.7 ms                                                | 50.1 ms: 1.81x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 514 ms: 1.80x faster                                  |
| richards                 | 74.9 ms                                                | 44.4 ms: 1.69x faster                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                  |
| logging_silent           | 175 ns                                                 | 107 ns: 1.63x faster                                  |
| chaos                    | 106 ms                                                 | 66.1 ms: 1.61x faster                                 |
| nbody                    | 142 ms                                                 | 89.2 ms: 1.59x faster                                 |
| scimark_sor              | 197 ms                                                 | 125 ms: 1.57x faster                                  |
| raytrace                 | 464 ms                                                 | 302 ms: 1.54x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.35 ms: 1.52x faster                                 |
| python_startup           | 14.2 ms                                                | 9.29 ms: 1.52x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.29 ms: 1.51x faster                                 |
| pyflate                  | 673 ms                                                 | 448 ms: 1.50x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 79.3 ms: 1.49x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 73.6 ms: 1.47x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.68 ms: 1.46x faster                                 |
| async_tree_none          | 717 ms                                                 | 500 ms: 1.43x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.24 sec: 1.43x faster                                |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                 |
| scimark_lu               | 163 ms                                                 | 115 ms: 1.42x faster                                  |
| pickle_pure_python       | 455 us                                                 | 322 us: 1.41x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 606 ms: 1.41x faster                                  |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.39x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.89 ms: 1.37x faster                                 |
| float                    | 111 ms                                                 | 82.2 ms: 1.35x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 223 us: 1.34x faster                                  |
| mako                     | 14.8 ms                                                | 11.0 ms: 1.34x faster                                 |
| deepcopy_memo            | 52.3 us                                                | 39.4 us: 1.33x faster                                 |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.31x faster                                |
| pprint_safe_repr         | 955 ms                                                 | 739 ms: 1.29x faster                                  |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.29x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 742 ms: 1.28x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.0 ms: 1.27x faster                                 |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                |
| unpack_sequence          | 64.7 ns                                                | 51.6 ns: 1.26x faster                                 |
| logging_format           | 8.91 us                                                | 7.10 us: 1.25x faster                                 |
| logging_simple           | 8.07 us                                                | 6.47 us: 1.25x faster                                 |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                  |
| tornado_http             | 127 ms                                                 | 102 ms: 1.25x faster                                  |
| mypy2                    | 428 ms                                                 | 347 ms: 1.24x faster                                  |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                  |
| deepcopy                 | 442 us                                                 | 364 us: 1.21x faster                                  |
| nqueens                  | 100 ms                                                 | 82.4 ms: 1.21x faster                                 |
| scimark_fft              | 424 ms                                                 | 350 ms: 1.21x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 54.1 ms: 1.21x faster                                 |
| regex_compile            | 177 ms                                                 | 146 ms: 1.21x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.25 us: 1.18x faster                                 |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.17x faster                                |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                 |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                 |
| bench_thread_pool        | 947 us                                                 | 834 us: 1.14x faster                                  |
| json                     | 5.42 ms                                                | 4.78 ms: 1.13x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.84 ms: 1.13x faster                                 |
| dulwich_log              | 75.9 ms                                                | 68.0 ms: 1.12x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.8 ms: 1.11x faster                                 |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                  |
| mdp                      | 2.82 sec                                               | 2.61 sec: 1.08x faster                                |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                  |
| regex_dna                | 222 ms                                                 | 210 ms: 1.06x faster                                  |
| pathlib                  | 20.0 ms                                                | 19.7 ms: 1.01x faster                                 |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                 |
| pickle_list              | 4.56 us                                                | 4.66 us: 1.02x slower                                 |
| unpickle_list            | 4.82 us                                                | 4.98 us: 1.03x slower                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| telco                    | 6.54 ms                                                | 6.91 ms: 1.06x slower                                 |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                 |
| async_generators         | 425 ms                                                 | 454 ms: 1.07x slower                                  |
| unpickle                 | 14.1 us                                                | 15.3 us: 1.08x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.56 ms: 1.10x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.75 ms: 1.16x slower                                 |
| pickle_dict              | 27.3 us                                                | 32.6 us: 1.20x slower                                 |
| dask                     | 423 ms                                                 | 537 ms: 1.27x slower                                  |
| coverage                 | 72.8 ms                                                | 97.0 ms: 1.33x slower                                 |
| Geometric mean           | (ref)                                                  | 1.27x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
