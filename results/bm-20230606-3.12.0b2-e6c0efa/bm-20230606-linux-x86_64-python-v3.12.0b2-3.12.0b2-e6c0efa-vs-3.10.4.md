
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b2
- machine: linux-x86_64
- commit hash: e6c0efa
- commit date: 2023-06-06
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                       |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                     |
| tornado_http   | 127 ms                                                 | 99.3 ms: 1.28x faster                                      |
| Geometric mean | (ref)                                                  | 1.23x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.7 ms: 1.58x faster                                      |
| float          | 111 ms                                                 | 80.3 ms: 1.38x faster                                      |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                       |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                       |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.09x faster                                      |
| regex_effbot   | 3.23 ms                                                | 3.83 ms: 1.19x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 314 us: 1.45x faster                                       |
| json_dumps           | 13.5 ms                                                | 9.69 ms: 1.40x faster                                      |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.39x faster                                       |
| tomli_loads          | 2.92 sec                                               | 2.24 sec: 1.30x faster                                     |
| xml_etree_process    | 74.9 ms                                                | 59.1 ms: 1.27x faster                                      |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                      |
| xml_etree_generate   | 94.2 ms                                                | 85.6 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                       |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                       |
| unpickle_list        | 4.82 us                                                | 4.90 us: 1.02x slower                                      |
| pickle_list          | 4.56 us                                                | 4.75 us: 1.04x slower                                      |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                      |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                      |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.30 ms: 1.52x faster                                      |
| python_startup_no_site | 5.82 ms                                                | 6.76 ms: 1.16x slower                                      |
| Geometric mean         | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                       |
| generators               | 76.8 ms                                                | 31.6 ms: 2.43x faster                                      |
| deltablue                | 7.42 ms                                                | 3.46 ms: 2.15x faster                                      |
| richards_super           | 90.7 ms                                                | 48.9 ms: 1.86x faster                                      |
| asyncio_tcp              | 925 ms                                                 | 511 ms: 1.81x faster                                       |
| richards                 | 74.9 ms                                                | 43.1 ms: 1.74x faster                                      |
| logging_silent           | 175 ns                                                 | 103 ns: 1.71x faster                                       |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                     |
| chaos                    | 106 ms                                                 | 63.6 ms: 1.67x faster                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.63x faster                                       |
| nbody                    | 142 ms                                                 | 89.7 ms: 1.58x faster                                      |
| raytrace                 | 464 ms                                                 | 296 ms: 1.57x faster                                       |
| hexiom                   | 9.53 ms                                                | 6.19 ms: 1.54x faster                                      |
| async_tree_io            | 1.77 sec                                               | 1.15 sec: 1.54x faster                                     |
| async_tree_none          | 717 ms                                                 | 468 ms: 1.53x faster                                       |
| sqlglot_parse            | 2.06 ms                                                | 1.35 ms: 1.52x faster                                      |
| python_startup           | 14.2 ms                                                | 9.30 ms: 1.52x faster                                      |
| crypto_pyaes             | 118 ms                                                 | 78.0 ms: 1.52x faster                                      |
| scimark_monte_carlo      | 108 ms                                                 | 71.3 ms: 1.52x faster                                      |
| pyflate                  | 673 ms                                                 | 448 ms: 1.50x faster                                       |
| async_tree_memoization   | 854 ms                                                 | 570 ms: 1.50x faster                                       |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.46x faster                                      |
| pickle_pure_python       | 455 us                                                 | 314 us: 1.45x faster                                       |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.44x faster                                       |
| coroutines               | 31.8 ms                                                | 22.1 ms: 1.44x faster                                      |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                       |
| json_dumps               | 13.5 ms                                                | 9.69 ms: 1.40x faster                                      |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                      |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.39x faster                                       |
| unpack_sequence          | 64.7 ns                                                | 46.7 ns: 1.39x faster                                      |
| float                    | 111 ms                                                 | 80.3 ms: 1.38x faster                                      |
| deepcopy_memo            | 52.3 us                                                | 38.1 us: 1.37x faster                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 708 ms: 1.34x faster                                       |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.32x faster                                     |
| tomli_loads              | 2.92 sec                                               | 2.24 sec: 1.30x faster                                     |
| pprint_safe_repr         | 955 ms                                                 | 735 ms: 1.30x faster                                       |
| logging_simple           | 8.07 us                                                | 6.24 us: 1.29x faster                                      |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.28x faster                                      |
| tornado_http             | 127 ms                                                 | 99.3 ms: 1.28x faster                                      |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.28x faster                                     |
| logging_format           | 8.91 us                                                | 6.96 us: 1.28x faster                                      |
| xml_etree_process        | 74.9 ms                                                | 59.1 ms: 1.27x faster                                      |
| 2to3                     | 336 ms                                                 | 269 ms: 1.25x faster                                       |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                       |
| deepcopy                 | 442 us                                                 | 359 us: 1.23x faster                                       |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                       |
| fannkuch                 | 486 ms                                                 | 398 ms: 1.22x faster                                       |
| nqueens                  | 100 ms                                                 | 82.6 ms: 1.21x faster                                      |
| sqlglot_optimize         | 65.3 ms                                                | 54.2 ms: 1.21x faster                                      |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                      |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                       |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.16x faster                                     |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                      |
| bench_thread_pool        | 947 us                                                 | 829 us: 1.14x faster                                       |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                       |
| json                     | 5.42 ms                                                | 4.76 ms: 1.14x faster                                      |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.8 ms: 1.13x faster                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.89 ms: 1.12x faster                                      |
| dulwich_log              | 75.9 ms                                                | 68.4 ms: 1.11x faster                                      |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                      |
| xml_etree_generate       | 94.2 ms                                                | 85.6 ms: 1.10x faster                                      |
| regex_dna                | 222 ms                                                 | 202 ms: 1.10x faster                                       |
| regex_v8                 | 25.0 ms                                                | 22.9 ms: 1.09x faster                                      |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                       |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.08x faster                                      |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                       |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.06x faster                                      |
| xml_etree_parse          | 163 ms                                                 | 156 ms: 1.04x faster                                       |
| unpickle_list            | 4.82 us                                                | 4.90 us: 1.02x slower                                      |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                       |
| pickle_list              | 4.56 us                                                | 4.75 us: 1.04x slower                                      |
| telco                    | 6.54 ms                                                | 6.83 ms: 1.04x slower                                      |
| async_generators         | 425 ms                                                 | 450 ms: 1.06x slower                                       |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                      |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                      |
| gc_traversal             | 3.84 ms                                                | 4.25 ms: 1.11x slower                                      |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                      |
| python_startup_no_site   | 5.82 ms                                                | 6.76 ms: 1.16x slower                                      |
| regex_effbot             | 3.23 ms                                                | 3.83 ms: 1.19x slower                                      |
| dask                     | 423 ms                                                 | 536 ms: 1.27x slower                                       |
| coverage                 | 72.8 ms                                                | 93.8 ms: 1.29x slower                                      |
| Geometric mean           | (ref)                                                  | 1.27x faster                                               |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
