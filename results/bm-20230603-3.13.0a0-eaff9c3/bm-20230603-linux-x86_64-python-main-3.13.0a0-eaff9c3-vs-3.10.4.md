
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                |
| tornado_http   | 127 ms                                                 | 102 ms: 1.25x faster                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.0 ms: 1.59x faster                                 |
| float          | 111 ms                                                 | 81.4 ms: 1.36x faster                                 |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                  |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                 |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 312 us: 1.46x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                 |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.22 sec: 1.32x faster                                |
| xml_etree_process    | 74.9 ms                                                | 59.0 ms: 1.27x faster                                 |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.5 ms: 1.11x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| pickle_list          | 4.56 us                                                | 4.66 us: 1.02x slower                                 |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                 |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                 |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.30 ms: 1.52x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.77 ms: 1.16x slower                                 |
| Geometric mean         | (ref)                                                  | 1.14x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.56x faster                                  |
| generators               | 76.8 ms                                                | 30.5 ms: 2.51x faster                                 |
| deltablue                | 7.42 ms                                                | 3.49 ms: 2.12x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 511 ms: 1.81x faster                                  |
| richards_super           | 90.7 ms                                                | 50.5 ms: 1.80x faster                                 |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                  |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                  |
| richards                 | 74.9 ms                                                | 44.5 ms: 1.68x faster                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                |
| chaos                    | 106 ms                                                 | 64.5 ms: 1.65x faster                                 |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                  |
| nbody                    | 142 ms                                                 | 89.0 ms: 1.59x faster                                 |
| raytrace                 | 464 ms                                                 | 297 ms: 1.56x faster                                  |
| hexiom                   | 9.53 ms                                                | 6.21 ms: 1.53x faster                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.53x faster                                 |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                  |
| python_startup           | 14.2 ms                                                | 9.30 ms: 1.52x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 71.7 ms: 1.51x faster                                 |
| crypto_pyaes             | 118 ms                                                 | 78.7 ms: 1.51x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.48x faster                                 |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.47x faster                                |
| unpack_sequence          | 64.7 ns                                                | 44.2 ns: 1.46x faster                                 |
| pickle_pure_python       | 455 us                                                 | 312 us: 1.46x faster                                  |
| async_tree_none          | 717 ms                                                 | 496 ms: 1.44x faster                                  |
| scimark_lu               | 163 ms                                                 | 114 ms: 1.44x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 595 ms: 1.44x faster                                  |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.41x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.78 ms: 1.38x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                 |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                 |
| float                    | 111 ms                                                 | 81.4 ms: 1.36x faster                                 |
| coroutines               | 31.8 ms                                                | 23.7 ms: 1.34x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.33x faster                                |
| tomli_loads              | 2.92 sec                                               | 2.22 sec: 1.32x faster                                |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 733 ms: 1.30x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 735 ms: 1.29x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.0 ms: 1.27x faster                                 |
| logging_simple           | 8.07 us                                                | 6.37 us: 1.27x faster                                 |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.27x faster                                |
| logging_format           | 8.91 us                                                | 7.05 us: 1.26x faster                                 |
| fannkuch                 | 486 ms                                                 | 386 ms: 1.26x faster                                  |
| tornado_http             | 127 ms                                                 | 102 ms: 1.25x faster                                  |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                  |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                  |
| mypy2                    | 428 ms                                                 | 345 ms: 1.24x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.12 us: 1.23x faster                                 |
| nqueens                  | 100 ms                                                 | 81.6 ms: 1.23x faster                                 |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 54.0 ms: 1.21x faster                                 |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                  |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.15x faster                                 |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                 |
| bench_thread_pool        | 947 us                                                 | 831 us: 1.14x faster                                  |
| json                     | 5.42 ms                                                | 4.77 ms: 1.13x faster                                 |
| dulwich_log              | 75.9 ms                                                | 67.7 ms: 1.12x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.5 ms: 1.11x faster                                 |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.95 ms: 1.10x faster                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                  |
| regex_dna                | 222 ms                                                 | 205 ms: 1.08x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| sqlite_synth             | 2.93 us                                                | 2.72 us: 1.08x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                  |
| gc_traversal             | 3.84 ms                                                | 3.91 ms: 1.02x slower                                 |
| pickle_list              | 4.56 us                                                | 4.66 us: 1.02x slower                                 |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                 |
| telco                    | 6.54 ms                                                | 6.82 ms: 1.04x slower                                 |
| async_generators         | 425 ms                                                 | 450 ms: 1.06x slower                                  |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.56 ms: 1.10x slower                                 |
| pickle_dict              | 27.3 us                                                | 31.6 us: 1.16x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.77 ms: 1.16x slower                                 |
| dask                     | 423 ms                                                 | 538 ms: 1.27x slower                                  |
| coverage                 | 72.8 ms                                                | 96.3 ms: 1.32x slower                                 |
| Geometric mean           | (ref)                                                  | 1.28x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
