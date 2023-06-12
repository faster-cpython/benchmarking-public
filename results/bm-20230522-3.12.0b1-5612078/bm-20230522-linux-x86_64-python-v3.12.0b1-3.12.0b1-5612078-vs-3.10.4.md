
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b1
- machine: linux-x86_64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                       |
| docutils       | 3.17 sec                                               | 2.74 sec: 1.16x faster                                     |
| tornado_http   | 127 ms                                                 | 99.2 ms: 1.28x faster                                      |
| Geometric mean | (ref)                                                  | 1.23x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.4 ms: 1.58x faster                                      |
| float          | 111 ms                                                 | 81.5 ms: 1.36x faster                                      |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 143 ms: 1.24x faster                                       |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                      |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                       |
| regex_effbot   | 3.23 ms                                                | 3.76 ms: 1.16x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 312 us: 1.46x faster                                       |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.39x faster                                       |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                      |
| tomli_loads          | 2.92 sec                                               | 2.19 sec: 1.33x faster                                     |
| xml_etree_process    | 74.9 ms                                                | 58.9 ms: 1.27x faster                                      |
| json_loads           | 28.8 us                                                | 24.9 us: 1.16x faster                                      |
| xml_etree_generate   | 94.2 ms                                                | 85.2 ms: 1.11x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                       |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                       |
| pickle_list          | 4.56 us                                                | 4.47 us: 1.02x faster                                      |
| unpickle             | 14.1 us                                                | 14.6 us: 1.03x slower                                      |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                      |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                      |
| pickle_dict          | 27.3 us                                                | 32.0 us: 1.17x slower                                      |
| Geometric mean       | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.34 ms: 1.51x faster                                      |
| python_startup_no_site | 5.82 ms                                                | 6.79 ms: 1.17x slower                                      |
| Geometric mean         | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 140 us: 3.65x faster                                       |
| generators               | 76.8 ms                                                | 30.7 ms: 2.50x faster                                      |
| deltablue                | 7.42 ms                                                | 3.51 ms: 2.11x faster                                      |
| richards_super           | 90.7 ms                                                | 49.1 ms: 1.85x faster                                      |
| asyncio_tcp              | 925 ms                                                 | 507 ms: 1.82x faster                                       |
| logging_silent           | 175 ns                                                 | 99.8 ns: 1.75x faster                                      |
| richards                 | 74.9 ms                                                | 43.4 ms: 1.73x faster                                      |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                     |
| chaos                    | 106 ms                                                 | 64.7 ms: 1.64x faster                                      |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.63x faster                                       |
| nbody                    | 142 ms                                                 | 89.4 ms: 1.58x faster                                      |
| raytrace                 | 464 ms                                                 | 296 ms: 1.57x faster                                       |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                      |
| hexiom                   | 9.53 ms                                                | 6.17 ms: 1.54x faster                                      |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                     |
| async_tree_none          | 717 ms                                                 | 471 ms: 1.52x faster                                       |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                       |
| crypto_pyaes             | 118 ms                                                 | 78.1 ms: 1.52x faster                                      |
| python_startup           | 14.2 ms                                                | 9.34 ms: 1.51x faster                                      |
| scimark_monte_carlo      | 108 ms                                                 | 71.8 ms: 1.51x faster                                      |
| async_tree_memoization   | 854 ms                                                 | 567 ms: 1.51x faster                                       |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                       |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.50x faster                                      |
| pickle_pure_python       | 455 us                                                 | 312 us: 1.46x faster                                       |
| coroutines               | 31.8 ms                                                | 21.9 ms: 1.46x faster                                      |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.41x faster                                       |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                      |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.39x faster                                       |
| json_dumps               | 13.5 ms                                                | 9.78 ms: 1.38x faster                                      |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                      |
| float                    | 111 ms                                                 | 81.5 ms: 1.36x faster                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 710 ms: 1.34x faster                                       |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                     |
| tomli_loads              | 2.92 sec                                               | 2.19 sec: 1.33x faster                                     |
| pprint_safe_repr         | 955 ms                                                 | 728 ms: 1.31x faster                                       |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                     |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.29x faster                                      |
| tornado_http             | 127 ms                                                 | 99.2 ms: 1.28x faster                                      |
| unpack_sequence          | 64.7 ns                                                | 50.5 ns: 1.28x faster                                      |
| xml_etree_process        | 74.9 ms                                                | 58.9 ms: 1.27x faster                                      |
| fannkuch                 | 486 ms                                                 | 384 ms: 1.27x faster                                       |
| logging_format           | 8.91 us                                                | 7.12 us: 1.25x faster                                      |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                       |
| logging_simple           | 8.07 us                                                | 6.45 us: 1.25x faster                                      |
| 2to3                     | 336 ms                                                 | 269 ms: 1.25x faster                                       |
| deepcopy                 | 442 us                                                 | 357 us: 1.24x faster                                       |
| regex_compile            | 177 ms                                                 | 143 ms: 1.24x faster                                       |
| nqueens                  | 100 ms                                                 | 81.8 ms: 1.22x faster                                      |
| sqlglot_optimize         | 65.3 ms                                                | 53.6 ms: 1.22x faster                                      |
| scimark_fft              | 424 ms                                                 | 349 ms: 1.21x faster                                       |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                      |
| docutils                 | 3.17 sec                                               | 2.74 sec: 1.16x faster                                     |
| json_loads               | 28.8 us                                                | 24.9 us: 1.16x faster                                      |
| json                     | 5.42 ms                                                | 4.72 ms: 1.15x faster                                      |
| bench_thread_pool        | 947 us                                                 | 827 us: 1.15x faster                                       |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                       |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.7 ms: 1.13x faster                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.81 ms: 1.13x faster                                      |
| dulwich_log              | 75.9 ms                                                | 67.8 ms: 1.12x faster                                      |
| xml_etree_generate       | 94.2 ms                                                | 85.2 ms: 1.11x faster                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                      |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                       |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                      |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                      |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                       |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                       |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.07x faster                                      |
| mdp                      | 2.82 sec                                               | 2.71 sec: 1.04x faster                                     |
| regex_dna                | 222 ms                                                 | 214 ms: 1.04x faster                                       |
| pickle_list              | 4.56 us                                                | 4.47 us: 1.02x faster                                      |
| gc_traversal             | 3.84 ms                                                | 3.83 ms: 1.00x faster                                      |
| unpickle                 | 14.1 us                                                | 14.6 us: 1.03x slower                                      |
| unpickle_list            | 4.82 us                                                | 5.00 us: 1.04x slower                                      |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                       |
| async_generators         | 425 ms                                                 | 444 ms: 1.05x slower                                       |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                      |
| telco                    | 6.54 ms                                                | 6.95 ms: 1.06x slower                                      |
| regex_effbot             | 3.23 ms                                                | 3.76 ms: 1.16x slower                                      |
| python_startup_no_site   | 5.82 ms                                                | 6.79 ms: 1.17x slower                                      |
| pickle_dict              | 27.3 us                                                | 32.0 us: 1.17x slower                                      |
| dask                     | 423 ms                                                 | 534 ms: 1.26x slower                                       |
| coverage                 | 72.8 ms                                                | 95.9 ms: 1.32x slower                                      |
| Geometric mean           | (ref)                                                  | 1.28x faster                                               |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
