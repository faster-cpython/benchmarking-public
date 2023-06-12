
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
| 2to3           | 336 ms                                                 | 268 ms: 1.25x faster                                       |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                     |
| tornado_http   | 127 ms                                                 | 99.2 ms: 1.28x faster                                      |
| Geometric mean | (ref)                                                  | 1.23x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.9 ms: 1.59x faster                                      |
| float          | 111 ms                                                 | 80.7 ms: 1.37x faster                                      |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                       |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                      |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                       |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 312 us: 1.46x faster                                       |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                       |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                      |
| tomli_loads          | 2.92 sec                                               | 2.18 sec: 1.34x faster                                     |
| xml_etree_process    | 74.9 ms                                                | 59.0 ms: 1.27x faster                                      |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                      |
| xml_etree_generate   | 94.2 ms                                                | 85.6 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                       |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                       |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                      |
| pickle_list          | 4.56 us                                                | 4.73 us: 1.04x slower                                      |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                      |
| unpickle_list        | 4.82 us                                                | 5.17 us: 1.07x slower                                      |
| pickle_dict          | 27.3 us                                                | 33.3 us: 1.22x slower                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.34 ms: 1.52x faster                                      |
| python_startup_no_site | 5.82 ms                                                | 6.78 ms: 1.17x slower                                      |
| Geometric mean         | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 140 us: 3.64x faster                                       |
| generators               | 76.8 ms                                                | 31.4 ms: 2.44x faster                                      |
| deltablue                | 7.42 ms                                                | 3.44 ms: 2.15x faster                                      |
| richards_super           | 90.7 ms                                                | 49.8 ms: 1.82x faster                                      |
| asyncio_tcp              | 925 ms                                                 | 513 ms: 1.80x faster                                       |
| logging_silent           | 175 ns                                                 | 100 ns: 1.75x faster                                       |
| richards                 | 74.9 ms                                                | 43.6 ms: 1.72x faster                                      |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                     |
| chaos                    | 106 ms                                                 | 64.6 ms: 1.65x faster                                      |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                       |
| nbody                    | 142 ms                                                 | 88.9 ms: 1.59x faster                                      |
| hexiom                   | 9.53 ms                                                | 6.12 ms: 1.56x faster                                      |
| raytrace                 | 464 ms                                                 | 298 ms: 1.55x faster                                       |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                      |
| async_tree_none          | 717 ms                                                 | 469 ms: 1.53x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                     |
| crypto_pyaes             | 118 ms                                                 | 77.9 ms: 1.52x faster                                      |
| pyflate                  | 673 ms                                                 | 443 ms: 1.52x faster                                       |
| python_startup           | 14.2 ms                                                | 9.34 ms: 1.52x faster                                      |
| async_tree_memoization   | 854 ms                                                 | 572 ms: 1.49x faster                                       |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                      |
| scimark_monte_carlo      | 108 ms                                                 | 72.7 ms: 1.49x faster                                      |
| pickle_pure_python       | 455 us                                                 | 312 us: 1.46x faster                                       |
| coroutines               | 31.8 ms                                                | 21.9 ms: 1.45x faster                                      |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.44x faster                                       |
| unpickle_pure_python     | 300 us                                                 | 216 us: 1.39x faster                                       |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                      |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                      |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.39x faster                                       |
| float                    | 111 ms                                                 | 80.7 ms: 1.37x faster                                      |
| unpack_sequence          | 64.7 ns                                                | 47.3 ns: 1.37x faster                                      |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 708 ms: 1.34x faster                                       |
| tomli_loads              | 2.92 sec                                               | 2.18 sec: 1.34x faster                                     |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.33x faster                                     |
| comprehensions           | 26.8 us                                                | 20.6 us: 1.31x faster                                      |
| pprint_safe_repr         | 955 ms                                                 | 733 ms: 1.30x faster                                       |
| tornado_http             | 127 ms                                                 | 99.2 ms: 1.28x faster                                      |
| logging_simple           | 8.07 us                                                | 6.33 us: 1.28x faster                                      |
| fannkuch                 | 486 ms                                                 | 382 ms: 1.27x faster                                       |
| xml_etree_process        | 74.9 ms                                                | 59.0 ms: 1.27x faster                                      |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                     |
| logging_format           | 8.91 us                                                | 7.09 us: 1.26x faster                                      |
| 2to3                     | 336 ms                                                 | 268 ms: 1.25x faster                                       |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.25x faster                                       |
| regex_compile            | 177 ms                                                 | 144 ms: 1.23x faster                                       |
| nqueens                  | 100 ms                                                 | 81.4 ms: 1.23x faster                                      |
| deepcopy                 | 442 us                                                 | 361 us: 1.22x faster                                       |
| sqlglot_optimize         | 65.3 ms                                                | 54.1 ms: 1.21x faster                                      |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                      |
| scimark_fft              | 424 ms                                                 | 356 ms: 1.19x faster                                       |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                     |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                      |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                      |
| bench_thread_pool        | 947 us                                                 | 827 us: 1.15x faster                                       |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.6 ms: 1.14x faster                                      |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                       |
| json                     | 5.42 ms                                                | 4.77 ms: 1.13x faster                                      |
| dulwich_log              | 75.9 ms                                                | 67.7 ms: 1.12x faster                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                      |
| xml_etree_generate       | 94.2 ms                                                | 85.6 ms: 1.10x faster                                      |
| pathlib                  | 20.0 ms                                                | 18.3 ms: 1.09x faster                                      |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                       |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                       |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.05 ms: 1.08x faster                                      |
| sqlite_synth             | 2.93 us                                                | 2.72 us: 1.08x faster                                      |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                       |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                       |
| mdp                      | 2.82 sec                                               | 2.68 sec: 1.05x faster                                     |
| gc_traversal             | 3.84 ms                                                | 3.67 ms: 1.05x faster                                      |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                      |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                       |
| pickle_list              | 4.56 us                                                | 4.73 us: 1.04x slower                                      |
| telco                    | 6.54 ms                                                | 6.84 ms: 1.05x slower                                      |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                      |
| async_generators         | 425 ms                                                 | 449 ms: 1.06x slower                                       |
| unpickle_list            | 4.82 us                                                | 5.17 us: 1.07x slower                                      |
| regex_effbot             | 3.23 ms                                                | 3.54 ms: 1.09x slower                                      |
| python_startup_no_site   | 5.82 ms                                                | 6.78 ms: 1.17x slower                                      |
| pickle_dict              | 27.3 us                                                | 33.3 us: 1.22x slower                                      |
| dask                     | 423 ms                                                 | 535 ms: 1.27x slower                                       |
| coverage                 | 72.8 ms                                                | 96.8 ms: 1.33x slower                                      |
| Geometric mean           | (ref)                                                  | 1.28x faster                                               |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
