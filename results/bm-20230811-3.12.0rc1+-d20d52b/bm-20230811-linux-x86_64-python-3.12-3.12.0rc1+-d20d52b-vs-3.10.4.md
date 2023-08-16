
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: d20d52b
- commit date: 2023-08-11
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.25x faster                                    |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.17x faster                                  |
| tornado_http   | 127 ms                                                 | 99.3 ms: 1.28x faster                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.7 ms: 1.58x faster                                   |
| float          | 111 ms                                                 | 79.9 ms: 1.38x faster                                   |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                    |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                   |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                    |
| regex_effbot   | 3.23 ms                                                | 3.46 ms: 1.07x slower                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 307 us: 1.48x faster                                    |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                    |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                   |
| tomli_loads          | 2.92 sec                                               | 2.22 sec: 1.32x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 59.8 ms: 1.25x faster                                   |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                   |
| xml_etree_generate   | 94.2 ms                                                | 85.8 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                    |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                    |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                   |
| pickle_list          | 4.56 us                                                | 4.81 us: 1.06x slower                                   |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                   |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                   |
| pickle_dict          | 27.3 us                                                | 32.3 us: 1.19x slower                                   |
| Geometric mean       | (ref)                                                  | 1.12x faster                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.34 ms: 1.52x faster                                   |
| python_startup_no_site | 5.82 ms                                                | 6.78 ms: 1.17x slower                                   |
| Geometric mean         | (ref)                                                  | 1.14x faster                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.40x faster                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 149 us: 3.42x faster                                    |
| generators               | 76.8 ms                                                | 30.6 ms: 2.51x faster                                   |
| deltablue                | 7.42 ms                                                | 3.50 ms: 2.12x faster                                   |
| richards_super           | 90.7 ms                                                | 49.3 ms: 1.84x faster                                   |
| asyncio_tcp              | 925 ms                                                 | 512 ms: 1.81x faster                                    |
| logging_silent           | 175 ns                                                 | 98.0 ns: 1.79x faster                                   |
| richards                 | 74.9 ms                                                | 43.8 ms: 1.71x faster                                   |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                    |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                  |
| chaos                    | 106 ms                                                 | 63.7 ms: 1.67x faster                                   |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                    |
| nbody                    | 142 ms                                                 | 89.7 ms: 1.58x faster                                   |
| hexiom                   | 9.53 ms                                                | 6.07 ms: 1.57x faster                                   |
| raytrace                 | 464 ms                                                 | 298 ms: 1.55x faster                                    |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.54x faster                                   |
| async_tree_io            | 1.77 sec                                               | 1.15 sec: 1.54x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 77.0 ms: 1.54x faster                                   |
| async_tree_none          | 717 ms                                                 | 467 ms: 1.54x faster                                    |
| pyflate                  | 673 ms                                                 | 443 ms: 1.52x faster                                    |
| python_startup           | 14.2 ms                                                | 9.34 ms: 1.52x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 71.8 ms: 1.51x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 572 ms: 1.49x faster                                    |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.49x faster                                   |
| pickle_pure_python       | 455 us                                                 | 307 us: 1.48x faster                                    |
| spectral_norm            | 150 ms                                                 | 103 ms: 1.45x faster                                    |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.45x faster                                   |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.44x faster                                    |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.40x faster                                   |
| unpack_sequence          | 64.7 ns                                                | 46.4 ns: 1.40x faster                                   |
| unpickle_pure_python     | 300 us                                                 | 216 us: 1.39x faster                                    |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                   |
| deepcopy_memo            | 52.3 us                                                | 37.9 us: 1.38x faster                                   |
| float                    | 111 ms                                                 | 79.9 ms: 1.38x faster                                   |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 709 ms: 1.34x faster                                    |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.22 sec: 1.32x faster                                  |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 733 ms: 1.30x faster                                    |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                   |
| logging_simple           | 8.07 us                                                | 6.25 us: 1.29x faster                                   |
| logging_format           | 8.91 us                                                | 6.93 us: 1.28x faster                                   |
| tornado_http             | 127 ms                                                 | 99.3 ms: 1.28x faster                                   |
| 2to3                     | 336 ms                                                 | 268 ms: 1.25x faster                                    |
| xml_etree_process        | 74.9 ms                                                | 59.8 ms: 1.25x faster                                   |
| fannkuch                 | 486 ms                                                 | 390 ms: 1.25x faster                                    |
| mypy2                    | 428 ms                                                 | 345 ms: 1.24x faster                                    |
| nqueens                  | 100 ms                                                 | 80.6 ms: 1.24x faster                                   |
| deepcopy                 | 442 us                                                 | 357 us: 1.24x faster                                    |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                    |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                    |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 54.0 ms: 1.21x faster                                   |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                    |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.17x faster                                  |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                   |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.5 ms: 1.15x faster                                   |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.14x faster                                    |
| bench_thread_pool        | 947 us                                                 | 829 us: 1.14x faster                                    |
| json                     | 5.42 ms                                                | 4.81 ms: 1.13x faster                                   |
| dulwich_log              | 75.9 ms                                                | 68.1 ms: 1.12x faster                                   |
| regex_v8                 | 25.0 ms                                                | 22.5 ms: 1.11x faster                                   |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                   |
| xml_etree_generate       | 94.2 ms                                                | 85.8 ms: 1.10x faster                                   |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                    |
| regex_dna                | 222 ms                                                 | 202 ms: 1.10x faster                                    |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.01 ms: 1.09x faster                                   |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                   |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                    |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                   |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                    |
| pidigits                 | 190 ms                                                 | 189 ms: 1.00x faster                                    |
| gc_traversal             | 3.84 ms                                                | 3.84 ms: 1.00x faster                                   |
| unpickle_list            | 4.82 us                                                | 5.02 us: 1.04x slower                                   |
| telco                    | 6.54 ms                                                | 6.87 ms: 1.05x slower                                   |
| async_generators         | 425 ms                                                 | 449 ms: 1.06x slower                                    |
| pickle_list              | 4.56 us                                                | 4.81 us: 1.06x slower                                   |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                   |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                   |
| regex_effbot             | 3.23 ms                                                | 3.46 ms: 1.07x slower                                   |
| python_startup_no_site   | 5.82 ms                                                | 6.78 ms: 1.17x slower                                   |
| pickle_dict              | 27.3 us                                                | 32.3 us: 1.19x slower                                   |
| dask                     | 423 ms                                                 | 536 ms: 1.27x slower                                    |
| coverage                 | 72.8 ms                                                | 93.5 ms: 1.28x slower                                   |
| Geometric mean           | (ref)                                                  | 1.28x faster                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
