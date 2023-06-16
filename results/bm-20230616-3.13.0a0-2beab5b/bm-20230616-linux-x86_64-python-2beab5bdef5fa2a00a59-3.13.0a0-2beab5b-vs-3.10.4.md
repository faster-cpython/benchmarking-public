
# Results vs. 3.10.4

- fork: python
- ref: 2beab5bdef5fa2a00a59
- machine: linux-x86_64
- commit hash: 2beab5b
- commit date: 2023-06-16
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                |
| tornado_http   | 127 ms                                                 | 96.7 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.7 ms: 1.56x faster                                                 |
| float          | 111 ms                                                 | 79.9 ms: 1.38x faster                                                 |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.13x faster                                                 |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 4.12 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 309 us: 1.47x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.70 ms: 1.40x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 57.3 ms: 1.31x faster                                                 |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.6 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                                 |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                                 |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                                 |
| pickle_dict          | 27.3 us                                                | 32.2 us: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.63 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.46x faster                                                  |
| generators               | 76.8 ms                                                | 29.0 ms: 2.65x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                                  |
| richards_super           | 90.7 ms                                                | 50.2 ms: 1.81x faster                                                 |
| logging_silent           | 175 ns                                                 | 98.7 ns: 1.77x faster                                                 |
| chaos                    | 106 ms                                                 | 60.7 ms: 1.75x faster                                                 |
| go                       | 229 ms                                                 | 134 ms: 1.71x faster                                                  |
| richards                 | 74.9 ms                                                | 43.9 ms: 1.71x faster                                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| scimark_sor              | 197 ms                                                 | 117 ms: 1.68x faster                                                  |
| raytrace                 | 464 ms                                                 | 290 ms: 1.60x faster                                                  |
| hexiom                   | 9.53 ms                                                | 5.97 ms: 1.60x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                                 |
| nbody                    | 142 ms                                                 | 90.7 ms: 1.56x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 76.3 ms: 1.55x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                 |
| pyflate                  | 673 ms                                                 | 440 ms: 1.53x faster                                                  |
| scimark_monte_carlo      | 108 ms                                                 | 70.8 ms: 1.53x faster                                                 |
| scimark_lu               | 163 ms                                                 | 108 ms: 1.51x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                                 |
| async_tree_none          | 717 ms                                                 | 479 ms: 1.50x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                |
| pickle_pure_python       | 455 us                                                 | 309 us: 1.47x faster                                                  |
| coroutines               | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                 |
| async_tree_memoization   | 854 ms                                                 | 586 ms: 1.46x faster                                                  |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.45x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                  |
| unpack_sequence          | 64.7 ns                                                | 45.7 ns: 1.42x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.70 ms: 1.40x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                                 |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                 |
| float                    | 111 ms                                                 | 79.9 ms: 1.38x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.44 sec: 1.38x faster                                                |
| logging_simple           | 8.07 us                                                | 5.96 us: 1.35x faster                                                 |
| logging_format           | 8.91 us                                                | 6.59 us: 1.35x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 711 ms: 1.34x faster                                                  |
| tomli_loads              | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                                 |
| tornado_http             | 127 ms                                                 | 96.7 ms: 1.32x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 722 ms: 1.32x faster                                                  |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.31x faster                                                |
| xml_etree_process        | 74.9 ms                                                | 57.3 ms: 1.31x faster                                                 |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                  |
| nqueens                  | 100 ms                                                 | 78.2 ms: 1.28x faster                                                 |
| mypy2                    | 428 ms                                                 | 335 ms: 1.28x faster                                                  |
| fannkuch                 | 486 ms                                                 | 382 ms: 1.27x faster                                                  |
| deepcopy                 | 442 us                                                 | 348 us: 1.27x faster                                                  |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.27x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.3 ms: 1.23x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.13 us: 1.22x faster                                                 |
| scimark_fft              | 424 ms                                                 | 348 ms: 1.22x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.58 ms: 1.19x faster                                                 |
| dulwich_log              | 75.9 ms                                                | 64.7 ms: 1.17x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 816 us: 1.16x faster                                                  |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                                 |
| json                     | 5.42 ms                                                | 4.73 ms: 1.15x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.6 ms: 1.13x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.13x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                 |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| regex_dna                | 222 ms                                                 | 204 ms: 1.09x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                                  |
| pickle_list              | 4.56 us                                                | 4.62 us: 1.01x slower                                                 |
| gc_traversal             | 3.84 ms                                                | 3.90 ms: 1.01x slower                                                 |
| telco                    | 6.54 ms                                                | 6.72 ms: 1.03x slower                                                 |
| unpickle_list            | 4.82 us                                                | 5.00 us: 1.04x slower                                                 |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                                 |
| async_generators         | 425 ms                                                 | 458 ms: 1.08x slower                                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.63 ms: 1.14x slower                                                 |
| pickle_dict              | 27.3 us                                                | 32.2 us: 1.18x slower                                                 |
| dask                     | 423 ms                                                 | 515 ms: 1.22x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 4.12 ms: 1.27x slower                                                 |
| coverage                 | 72.8 ms                                                | 93.3 ms: 1.28x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
