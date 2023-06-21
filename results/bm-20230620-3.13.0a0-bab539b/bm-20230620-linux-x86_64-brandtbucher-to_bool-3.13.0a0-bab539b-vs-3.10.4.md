
# Results vs. 3.10.4

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: bab539b
- commit date: 2023-06-20
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| tornado_http   | 127 ms                                                 | 96.9 ms: 1.32x faster                                          |
| Geometric mean | (ref)                                                  | 1.25x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.8 ms: 1.51x faster                                          |
| float          | 111 ms                                                 | 79.2 ms: 1.40x faster                                          |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                  | 1.27x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                           |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                          |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 307 us: 1.48x faster                                           |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.40x faster                                           |
| json_dumps           | 13.5 ms                                                | 10.0 ms: 1.35x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 57.9 ms: 1.29x faster                                          |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                         |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 83.7 ms: 1.12x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                           |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                          |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                          |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                          |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.17 ms: 1.54x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.40x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                           |
| generators               | 76.8 ms                                                | 28.9 ms: 2.66x faster                                          |
| deltablue                | 7.42 ms                                                | 3.29 ms: 2.25x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                           |
| chaos                    | 106 ms                                                 | 61.6 ms: 1.72x faster                                          |
| richards_super           | 90.7 ms                                                | 52.8 ms: 1.72x faster                                          |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                         |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                           |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                           |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                           |
| richards                 | 74.9 ms                                                | 47.1 ms: 1.59x faster                                          |
| raytrace                 | 464 ms                                                 | 296 ms: 1.57x faster                                           |
| crypto_pyaes             | 118 ms                                                 | 75.9 ms: 1.56x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.11 ms: 1.56x faster                                          |
| python_startup           | 14.2 ms                                                | 9.17 ms: 1.54x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.54x faster                                          |
| pyflate                  | 673 ms                                                 | 445 ms: 1.51x faster                                           |
| nbody                    | 142 ms                                                 | 93.8 ms: 1.51x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 72.3 ms: 1.50x faster                                          |
| async_tree_none          | 717 ms                                                 | 482 ms: 1.49x faster                                           |
| pickle_pure_python       | 455 us                                                 | 307 us: 1.48x faster                                           |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                         |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.48x faster                                          |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                           |
| spectral_norm            | 150 ms                                                 | 102 ms: 1.47x faster                                           |
| async_tree_memoization   | 854 ms                                                 | 588 ms: 1.45x faster                                           |
| coroutines               | 31.8 ms                                                | 22.1 ms: 1.44x faster                                          |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.40x faster                                           |
| float                    | 111 ms                                                 | 79.2 ms: 1.40x faster                                          |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.40x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                          |
| logging_format           | 8.91 us                                                | 6.57 us: 1.36x faster                                          |
| json_dumps               | 13.5 ms                                                | 10.0 ms: 1.35x faster                                          |
| logging_simple           | 8.07 us                                                | 6.06 us: 1.33x faster                                          |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                         |
| unpack_sequence          | 64.7 ns                                                | 48.9 ns: 1.32x faster                                          |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 722 ms: 1.32x faster                                           |
| tornado_http             | 127 ms                                                 | 96.9 ms: 1.32x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.31x faster                                         |
| pprint_safe_repr         | 955 ms                                                 | 736 ms: 1.30x faster                                           |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                           |
| xml_etree_process        | 74.9 ms                                                | 57.9 ms: 1.29x faster                                          |
| nqueens                  | 100 ms                                                 | 78.0 ms: 1.28x faster                                          |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                           |
| mypy2                    | 428 ms                                                 | 336 ms: 1.27x faster                                           |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                         |
| deepcopy                 | 442 us                                                 | 349 us: 1.26x faster                                           |
| fannkuch                 | 486 ms                                                 | 385 ms: 1.26x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                          |
| scimark_fft              | 424 ms                                                 | 352 ms: 1.20x faster                                           |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| bench_thread_pool        | 947 us                                                 | 821 us: 1.15x faster                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.74 ms: 1.15x faster                                          |
| dulwich_log              | 75.9 ms                                                | 66.1 ms: 1.15x faster                                          |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                          |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.14x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 83.7 ms: 1.12x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                          |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                          |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.10x faster                                         |
| regex_dna                | 222 ms                                                 | 203 ms: 1.09x faster                                           |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                           |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                           |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                           |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                          |
| unpickle_list            | 4.82 us                                                | 4.91 us: 1.02x slower                                          |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                           |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                          |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                           |
| telco                    | 6.54 ms                                                | 6.89 ms: 1.05x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.51 ms: 1.09x slower                                          |
| gc_traversal             | 3.84 ms                                                | 4.32 ms: 1.13x slower                                          |
| pickle_dict              | 27.3 us                                                | 30.8 us: 1.13x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                          |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                           |
| coverage                 | 72.8 ms                                                | 93.2 ms: 1.28x slower                                          |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                   |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
