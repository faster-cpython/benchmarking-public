
# Results vs. 3.10.4

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: 47205b2
- commit date: 2023-06-16
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                |
| tornado_http   | 127 ms                                                 | 96.8 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.3 ms: 1.55x faster                                                 |
| float          | 111 ms                                                 | 81.2 ms: 1.36x faster                                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                 |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 4.09 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 316 us: 1.44x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.86 ms: 1.37x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 58.1 ms: 1.29x faster                                                 |
| json_loads           | 28.8 us                                                | 24.9 us: 1.15x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.3 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.61 us: 1.01x slower                                                 |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| unpickle_list        | 4.82 us                                                | 5.09 us: 1.06x slower                                                 |
| unpickle             | 14.1 us                                                | 15.3 us: 1.08x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.16 ms: 1.55x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.65 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 141 us: 3.62x faster                                                  |
| generators               | 76.8 ms                                                | 29.0 ms: 2.65x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.29 ms: 2.25x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 507 ms: 1.82x faster                                                  |
| richards_super           | 90.7 ms                                                | 51.8 ms: 1.75x faster                                                 |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                                  |
| chaos                    | 106 ms                                                 | 62.0 ms: 1.71x faster                                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                                  |
| richards                 | 74.9 ms                                                | 45.0 ms: 1.66x faster                                                 |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                                  |
| hexiom                   | 9.53 ms                                                | 6.04 ms: 1.58x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                                 |
| raytrace                 | 464 ms                                                 | 297 ms: 1.56x faster                                                  |
| nbody                    | 142 ms                                                 | 91.3 ms: 1.55x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.16 ms: 1.55x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 77.6 ms: 1.53x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 71.4 ms: 1.52x faster                                                 |
| pyflate                  | 673 ms                                                 | 447 ms: 1.51x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                |
| async_tree_none          | 717 ms                                                 | 482 ms: 1.49x faster                                                  |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                  |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.45x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 590 ms: 1.45x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 316 us: 1.44x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.86 ms: 1.37x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 38.3 us: 1.37x faster                                                 |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                 |
| float                    | 111 ms                                                 | 81.2 ms: 1.36x faster                                                 |
| logging_format           | 8.91 us                                                | 6.56 us: 1.36x faster                                                 |
| unpack_sequence          | 64.7 ns                                                | 47.7 ns: 1.36x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                |
| logging_simple           | 8.07 us                                                | 6.06 us: 1.33x faster                                                 |
| coroutines               | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 720 ms: 1.32x faster                                                  |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.32x faster                                                 |
| tornado_http             | 127 ms                                                 | 96.8 ms: 1.32x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 730 ms: 1.31x faster                                                  |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 58.1 ms: 1.29x faster                                                 |
| mypy2                    | 428 ms                                                 | 339 ms: 1.27x faster                                                  |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.26x faster                                                  |
| nqueens                  | 100 ms                                                 | 79.4 ms: 1.26x faster                                                 |
| fannkuch                 | 486 ms                                                 | 393 ms: 1.24x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.23x faster                                                 |
| deepcopy                 | 442 us                                                 | 363 us: 1.22x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                |
| deepcopy_reduce          | 3.82 us                                                | 3.25 us: 1.18x faster                                                 |
| scimark_fft              | 424 ms                                                 | 360 ms: 1.18x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 65.5 ms: 1.16x faster                                                 |
| json_loads               | 28.8 us                                                | 24.9 us: 1.15x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 822 us: 1.15x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                 |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.3 ms: 1.12x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.01 ms: 1.09x faster                                                 |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                                  |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                                  |
| gc_traversal             | 3.84 ms                                                | 3.69 ms: 1.04x faster                                                 |
| pickle_list              | 4.56 us                                                | 4.61 us: 1.01x slower                                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| telco                    | 6.54 ms                                                | 6.87 ms: 1.05x slower                                                 |
| unpickle_list            | 4.82 us                                                | 5.09 us: 1.06x slower                                                 |
| async_generators         | 425 ms                                                 | 459 ms: 1.08x slower                                                  |
| unpickle                 | 14.1 us                                                | 15.3 us: 1.08x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.65 ms: 1.14x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                                 |
| dask                     | 423 ms                                                 | 526 ms: 1.25x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 4.09 ms: 1.27x slower                                                 |
| coverage                 | 72.8 ms                                                | 95.5 ms: 1.31x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
