
# Results vs. 3.10.4

- fork: python
- ref: 601ae09f0c8eda213b90
- machine: darwin-arm64
- commit hash: 601ae09
- commit date: 2023-06-02
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                                |
| tornado_http   | 91.9 ms                                                | 70.7 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.0 ms: 1.37x faster                                                 |
| float          | 72.3 ms                                                | 57.0 ms: 1.27x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.5 ms: 1.28x faster                                                 |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                 |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 189 us: 1.50x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                                  |
| json_dumps           | 8.38 ms                                                | 6.31 ms: 1.33x faster                                                 |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                                |
| xml_etree_process    | 45.1 ms                                                | 39.0 ms: 1.16x faster                                                 |
| unpickle             | 9.77 us                                                | 9.27 us: 1.05x faster                                                 |
| pickle               | 7.36 us                                                | 7.44 us: 1.01x slower                                                 |
| pickle_list          | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| pickle_dict          | 17.8 us                                                | 18.1 us: 1.02x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 74.5 ms: 1.03x slower                                                 |
| xml_etree_generate   | 54.3 ms                                                | 56.1 ms: 1.03x slower                                                 |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                                 |
| unpickle_list        | 2.66 us                                                | 3.19 us: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.4 ms: 1.02x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.53 ms: 1.39x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 89.3 us: 3.85x faster                                                 |
| deltablue                | 5.15 ms                                                | 2.41 ms: 2.14x faster                                                 |
| richards_super           | 60.7 ms                                                | 34.0 ms: 1.78x faster                                                 |
| go                       | 165 ms                                                 | 94.0 ms: 1.75x faster                                                 |
| logging_silent           | 119 ns                                                 | 69.4 ns: 1.72x faster                                                 |
| richards                 | 51.4 ms                                                | 30.1 ms: 1.70x faster                                                 |
| scimark_monte_carlo      | 72.2 ms                                                | 43.4 ms: 1.67x faster                                                 |
| sqlglot_parse            | 1.33 ms                                                | 830 us: 1.61x faster                                                  |
| chaos                    | 66.8 ms                                                | 41.7 ms: 1.60x faster                                                 |
| raytrace                 | 328 ms                                                 | 207 ms: 1.58x faster                                                  |
| asyncio_tcp              | 673 ms                                                 | 433 ms: 1.55x faster                                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.00 ms: 1.53x faster                                                 |
| crypto_pyaes             | 78.0 ms                                                | 51.5 ms: 1.51x faster                                                 |
| async_tree_memoization   | 493 ms                                                 | 328 ms: 1.50x faster                                                  |
| scimark_lu               | 110 ms                                                 | 73.1 ms: 1.50x faster                                                 |
| pickle_pure_python       | 284 us                                                 | 189 us: 1.50x faster                                                  |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.49x faster                                                 |
| scimark_sor              | 127 ms                                                 | 85.5 ms: 1.48x faster                                                 |
| async_tree_io            | 1.02 sec                                               | 702 ms: 1.45x faster                                                  |
| pyflate                  | 453 ms                                                 | 313 ms: 1.45x faster                                                  |
| async_tree_none          | 402 ms                                                 | 280 ms: 1.43x faster                                                  |
| unpickle_pure_python     | 203 us                                                 | 145 us: 1.40x faster                                                  |
| mako                     | 10.5 ms                                                | 7.53 ms: 1.39x faster                                                 |
| deepcopy_memo            | 34.5 us                                                | 25.1 us: 1.37x faster                                                 |
| nbody                    | 94.1 ms                                                | 69.0 ms: 1.37x faster                                                 |
| unpack_sequence          | 38.7 ns                                                | 28.4 ns: 1.36x faster                                                 |
| pycparser                | 915 ms                                                 | 674 ms: 1.36x faster                                                  |
| json_dumps               | 8.38 ms                                                | 6.31 ms: 1.33x faster                                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.31x faster                                                |
| tornado_http             | 91.9 ms                                                | 70.7 ms: 1.30x faster                                                 |
| logging_format           | 5.01 us                                                | 3.86 us: 1.30x faster                                                 |
| logging_simple           | 4.63 us                                                | 3.58 us: 1.29x faster                                                 |
| spectral_norm            | 96.4 ms                                                | 74.8 ms: 1.29x faster                                                 |
| regex_compile            | 96.6 ms                                                | 75.5 ms: 1.28x faster                                                 |
| float                    | 72.3 ms                                                | 57.0 ms: 1.27x faster                                                 |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                                |
| create_gc_cycles         | 876 us                                                 | 698 us: 1.25x faster                                                  |
| generators               | 32.9 ms                                                | 26.7 ms: 1.24x faster                                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 543 ms: 1.23x faster                                                  |
| dulwich_log              | 37.1 ms                                                | 30.1 ms: 1.23x faster                                                 |
| pprint_pformat           | 1.24 sec                                               | 1.01 sec: 1.23x faster                                                |
| pprint_safe_repr         | 609 ms                                                 | 497 ms: 1.22x faster                                                  |
| deepcopy                 | 278 us                                                 | 228 us: 1.22x faster                                                  |
| fannkuch                 | 317 ms                                                 | 265 ms: 1.20x faster                                                  |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                                  |
| comprehensions           | 17.7 us                                                | 15.0 us: 1.18x faster                                                 |
| docutils                 | 1.78 sec                                               | 1.51 sec: 1.18x faster                                                |
| scimark_fft              | 232 ms                                                 | 199 ms: 1.17x faster                                                  |
| xml_etree_process        | 45.1 ms                                                | 39.0 ms: 1.16x faster                                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.07 us: 1.15x faster                                                 |
| nqueens                  | 68.1 ms                                                | 59.7 ms: 1.14x faster                                                 |
| bench_thread_pool        | 548 us                                                 | 482 us: 1.14x faster                                                  |
| coroutines               | 20.2 ms                                                | 17.8 ms: 1.13x faster                                                 |
| sqlglot_optimize         | 38.0 ms                                                | 34.2 ms: 1.11x faster                                                 |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.16 ms: 1.10x faster                                                 |
| meteor_contest           | 78.6 ms                                                | 73.4 ms: 1.07x faster                                                 |
| sqlglot_normalize        | 197 ms                                                 | 184 ms: 1.07x faster                                                  |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                                  |
| unpickle                 | 9.77 us                                                | 9.27 us: 1.05x faster                                                 |
| json                     | 3.10 ms                                                | 2.96 ms: 1.05x faster                                                 |
| python_startup           | 12.6 ms                                                | 12.4 ms: 1.02x faster                                                 |
| mdp                      | 1.67 sec                                               | 1.65 sec: 1.01x faster                                                |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| pickle                   | 7.36 us                                                | 7.44 us: 1.01x slower                                                 |
| pickle_list              | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| telco                    | 3.68 ms                                                | 3.74 ms: 1.02x slower                                                 |
| pickle_dict              | 17.8 us                                                | 18.1 us: 1.02x slower                                                 |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 74.5 ms: 1.03x slower                                                 |
| xml_etree_generate       | 54.3 ms                                                | 56.1 ms: 1.03x slower                                                 |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                                 |
| python_startup_no_site   | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| sqlite_synth             | 1.47 us                                                | 1.56 us: 1.06x slower                                                 |
| regex_effbot             | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| bench_mp_pool            | 41.0 ms                                                | 46.3 ms: 1.13x slower                                                 |
| pathlib                  | 28.8 ms                                                | 33.6 ms: 1.16x slower                                                 |
| unpickle_list            | 2.66 us                                                | 3.19 us: 1.20x slower                                                 |
| dask                     | 258 ms                                                 | 320 ms: 1.24x slower                                                  |
| coverage                 | 40.8 ms                                                | 51.1 ms: 1.25x slower                                                 |
| async_generators         | 233 ms                                                 | 311 ms: 1.33x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
