
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 6996b40
- commit date: 2023-08-05
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                |
| tornado_http   | 127 ms                                                 | 95.6 ms: 1.33x faster                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.6 ms: 1.54x faster                                 |
| float          | 111 ms                                                 | 78.8 ms: 1.40x faster                                 |
| pidigits       | 190 ms                                                 | 200 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                  |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.13x faster                                 |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.48 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 296 us: 1.54x faster                                  |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 57.9 ms: 1.29x faster                                 |
| tomli_loads          | 2.92 sec                                               | 2.29 sec: 1.27x faster                                |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.6 ms: 1.13x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                 |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.02x slower                                 |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                 |
| pickle_dict          | 27.3 us                                                | 32.4 us: 1.19x slower                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.39 ms: 1.51x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.87 ms: 1.18x slower                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 144 us: 3.54x faster                                  |
| generators               | 76.8 ms                                                | 27.8 ms: 2.77x faster                                 |
| deltablue                | 7.42 ms                                                | 3.17 ms: 2.34x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 483 ms: 1.92x faster                                  |
| chaos                    | 106 ms                                                 | 59.3 ms: 1.79x faster                                 |
| richards_super           | 90.7 ms                                                | 51.7 ms: 1.76x faster                                 |
| raytrace                 | 464 ms                                                 | 267 ms: 1.74x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 69.3 ms: 1.71x faster                                 |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.68x faster                                |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                  |
| richards                 | 74.9 ms                                                | 44.9 ms: 1.67x faster                                 |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.63x faster                                  |
| hexiom                   | 9.53 ms                                                | 5.95 ms: 1.60x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 68.3 ms: 1.59x faster                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.59x faster                                 |
| nbody                    | 142 ms                                                 | 91.6 ms: 1.54x faster                                 |
| pickle_pure_python       | 455 us                                                 | 296 us: 1.54x faster                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                 |
| python_startup           | 14.2 ms                                                | 9.39 ms: 1.51x faster                                 |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.50x faster                                |
| pyflate                  | 673 ms                                                 | 449 ms: 1.50x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 43.4 ns: 1.49x faster                                 |
| async_tree_none          | 717 ms                                                 | 481 ms: 1.49x faster                                  |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                  |
| coroutines               | 31.8 ms                                                | 21.7 ms: 1.46x faster                                 |
| async_tree_memoization   | 854 ms                                                 | 584 ms: 1.46x faster                                  |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                  |
| float                    | 111 ms                                                 | 78.8 ms: 1.40x faster                                 |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                 |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                 |
| deepcopy_memo            | 52.3 us                                                | 37.9 us: 1.38x faster                                 |
| logging_simple           | 8.07 us                                                | 5.90 us: 1.37x faster                                 |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                |
| tornado_http             | 127 ms                                                 | 95.6 ms: 1.33x faster                                 |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 720 ms: 1.32x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 723 ms: 1.32x faster                                  |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 57.9 ms: 1.29x faster                                 |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                  |
| mypy2                    | 428 ms                                                 | 336 ms: 1.28x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.29 sec: 1.27x faster                                |
| nqueens                  | 100 ms                                                 | 80.3 ms: 1.25x faster                                 |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                 |
| deepcopy                 | 442 us                                                 | 357 us: 1.24x faster                                  |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                  |
| scimark_fft              | 424 ms                                                 | 349 ms: 1.21x faster                                  |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.68 ms: 1.16x faster                                 |
| bench_thread_pool        | 947 us                                                 | 822 us: 1.15x faster                                  |
| dulwich_log              | 75.9 ms                                                | 66.0 ms: 1.15x faster                                 |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.6 ms: 1.13x faster                                 |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.13x faster                                 |
| json                     | 5.42 ms                                                | 4.83 ms: 1.12x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.08x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                 |
| regex_dna                | 222 ms                                                 | 211 ms: 1.05x faster                                  |
| mdp                      | 2.82 sec                                               | 2.73 sec: 1.03x faster                                |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                 |
| pickle_list              | 4.56 us                                                | 4.64 us: 1.02x slower                                 |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.02x slower                                 |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                  |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                 |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                 |
| pidigits                 | 190 ms                                                 | 200 ms: 1.06x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.48 ms: 1.08x slower                                 |
| gc_traversal             | 3.84 ms                                                | 4.19 ms: 1.09x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.87 ms: 1.18x slower                                 |
| pickle_dict              | 27.3 us                                                | 32.4 us: 1.19x slower                                 |
| telco                    | 6.54 ms                                                | 7.88 ms: 1.20x slower                                 |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                  |
| coverage                 | 72.8 ms                                                | 92.9 ms: 1.28x slower                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                          |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
