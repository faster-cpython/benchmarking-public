
# Results vs. 3.10.4

- fork: python
- ref: 42429d3b9adb8af1eadc
- machine: linux-x86_64
- commit hash: 42429d3
- commit date: 2023-08-16
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.62 sec: 1.21x faster                                                |
| tornado_http   | 127 ms                                                 | 95.3 ms: 1.34x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.7 ms: 1.54x faster                                                 |
| float          | 111 ms                                                 | 80.6 ms: 1.37x faster                                                 |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.30x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.09x faster                                                 |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 298 us: 1.53x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.69 ms: 1.40x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.11 sec: 1.38x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 58.5 ms: 1.28x faster                                                 |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                                 |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                                 |
| pickle               | 10.3 us                                                | 10.8 us: 1.04x slower                                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                                 |
| pickle_dict          | 27.3 us                                                | 33.0 us: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.35 ms: 1.51x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.84 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.57x faster                                                  |
| generators               | 76.8 ms                                                | 29.0 ms: 2.65x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.27 ms: 2.27x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 486 ms: 1.90x faster                                                  |
| chaos                    | 106 ms                                                 | 59.8 ms: 1.78x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 68.5 ms: 1.73x faster                                                 |
| logging_silent           | 175 ns                                                 | 102 ns: 1.71x faster                                                  |
| raytrace                 | 464 ms                                                 | 274 ms: 1.69x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| richards_super           | 90.7 ms                                                | 54.2 ms: 1.68x faster                                                 |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                  |
| async_tree_none          | 717 ms                                                 | 435 ms: 1.65x faster                                                  |
| scimark_monte_carlo      | 108 ms                                                 | 66.2 ms: 1.64x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.60x faster                                                 |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.59x faster                                                  |
| richards                 | 74.9 ms                                                | 47.1 ms: 1.59x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                 |
| nbody                    | 142 ms                                                 | 91.7 ms: 1.54x faster                                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                 |
| pickle_pure_python       | 455 us                                                 | 298 us: 1.53x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 563 ms: 1.52x faster                                                  |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                                  |
| python_startup           | 14.2 ms                                                | 9.35 ms: 1.51x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.49x faster                                                  |
| unpack_sequence          | 64.7 ns                                                | 43.9 ns: 1.47x faster                                                 |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                 |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.69 ms: 1.40x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                                 |
| tomli_loads              | 2.92 sec                                               | 2.11 sec: 1.38x faster                                                |
| float                    | 111 ms                                                 | 80.6 ms: 1.37x faster                                                 |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                 |
| logging_simple           | 8.07 us                                                | 5.91 us: 1.36x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 701 ms: 1.36x faster                                                  |
| logging_format           | 8.91 us                                                | 6.57 us: 1.36x faster                                                 |
| tornado_http             | 127 ms                                                 | 95.3 ms: 1.34x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                                |
| pprint_safe_repr         | 955 ms                                                 | 732 ms: 1.30x faster                                                  |
| regex_compile            | 177 ms                                                 | 137 ms: 1.30x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 58.5 ms: 1.28x faster                                                 |
| deepcopy                 | 442 us                                                 | 352 us: 1.26x faster                                                  |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.25x faster                                                |
| nqueens                  | 100 ms                                                 | 80.3 ms: 1.25x faster                                                 |
| fannkuch                 | 486 ms                                                 | 392 ms: 1.24x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.1 ms: 1.23x faster                                                 |
| scimark_fft              | 424 ms                                                 | 349 ms: 1.22x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.62 sec: 1.21x faster                                                |
| deepcopy_reduce          | 3.82 us                                                | 3.17 us: 1.21x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 65.6 ms: 1.16x faster                                                 |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.85 ms: 1.12x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                 |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 22.9 ms: 1.09x faster                                                 |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                 |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                  |
| mdp                      | 2.82 sec                                               | 2.73 sec: 1.03x faster                                                |
| regex_dna                | 222 ms                                                 | 217 ms: 1.02x faster                                                  |
| gc_traversal             | 3.84 ms                                                | 3.89 ms: 1.01x slower                                                 |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                                 |
| unpickle_list            | 4.82 us                                                | 4.92 us: 1.02x slower                                                 |
| pickle                   | 10.3 us                                                | 10.8 us: 1.04x slower                                                 |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                                 |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                  |
| async_generators         | 425 ms                                                 | 457 ms: 1.07x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                 |
| coverage                 | 72.8 ms                                                | 85.1 ms: 1.17x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.84 ms: 1.18x slower                                                 |
| pickle_dict              | 27.3 us                                                | 33.0 us: 1.21x slower                                                 |
| telco                    | 6.54 ms                                                | 8.05 ms: 1.23x slower                                                 |
| dask                     | 423 ms                                                 | 520 ms: 1.23x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x
