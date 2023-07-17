
# Results vs. 3.10.4

- fork: python
- ref: 601ae09f0c8eda213b90
- machine: darwin-arm64
- commit hash: 601ae09
- commit date: 2023-06-02
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                                |
| tornado_http   | 91.9 ms                                                | 70.3 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.0 ms: 1.36x faster                                                 |
| float          | 72.3 ms                                                | 57.1 ms: 1.27x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.4 ms: 1.28x faster                                                 |
| regex_v8       | 17.5 ms                                                | 15.6 ms: 1.12x faster                                                 |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 190 us: 1.49x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.41x faster                                                  |
| json_dumps           | 8.38 ms                                                | 6.33 ms: 1.32x faster                                                 |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                                |
| xml_etree_process    | 45.1 ms                                                | 39.0 ms: 1.16x faster                                                 |
| unpickle             | 9.77 us                                                | 9.27 us: 1.05x faster                                                 |
| pickle               | 7.36 us                                                | 7.42 us: 1.01x slower                                                 |
| pickle_list          | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| pickle_dict          | 17.8 us                                                | 18.2 us: 1.02x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 75.1 ms: 1.03x slower                                                 |
| xml_etree_generate   | 54.3 ms                                                | 56.2 ms: 1.04x slower                                                 |
| json_loads           | 16.9 us                                                | 17.5 us: 1.04x slower                                                 |
| unpickle_list        | 2.66 us                                                | 3.19 us: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.3 ms: 1.03x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.54 ms: 1.39x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 89.3 us: 3.85x faster                                                 |
| deltablue                | 5.15 ms                                                | 2.40 ms: 2.14x faster                                                 |
| richards_super           | 60.7 ms                                                | 34.1 ms: 1.78x faster                                                 |
| go                       | 165 ms                                                 | 94.0 ms: 1.75x faster                                                 |
| logging_silent           | 119 ns                                                 | 69.7 ns: 1.71x faster                                                 |
| richards                 | 51.4 ms                                                | 30.2 ms: 1.70x faster                                                 |
| scimark_monte_carlo      | 72.2 ms                                                | 43.2 ms: 1.67x faster                                                 |
| sqlglot_parse            | 1.33 ms                                                | 829 us: 1.61x faster                                                  |
| chaos                    | 66.8 ms                                                | 41.9 ms: 1.60x faster                                                 |
| raytrace                 | 328 ms                                                 | 207 ms: 1.58x faster                                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.00 ms: 1.53x faster                                                 |
| asyncio_tcp              | 673 ms                                                 | 444 ms: 1.52x faster                                                  |
| crypto_pyaes             | 78.0 ms                                                | 51.6 ms: 1.51x faster                                                 |
| scimark_lu               | 110 ms                                                 | 72.9 ms: 1.51x faster                                                 |
| async_tree_memoization   | 493 ms                                                 | 327 ms: 1.51x faster                                                  |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.49x faster                                                 |
| pickle_pure_python       | 284 us                                                 | 190 us: 1.49x faster                                                  |
| scimark_sor              | 127 ms                                                 | 85.4 ms: 1.48x faster                                                 |
| async_tree_io            | 1.02 sec                                               | 701 ms: 1.46x faster                                                  |
| pyflate                  | 453 ms                                                 | 313 ms: 1.45x faster                                                  |
| async_tree_none          | 402 ms                                                 | 280 ms: 1.43x faster                                                  |
| unpickle_pure_python     | 203 us                                                 | 145 us: 1.41x faster                                                  |
| mako                     | 10.5 ms                                                | 7.54 ms: 1.39x faster                                                 |
| deepcopy_memo            | 34.5 us                                                | 25.0 us: 1.38x faster                                                 |
| unpack_sequence          | 38.7 ns                                                | 28.3 ns: 1.37x faster                                                 |
| nbody                    | 94.1 ms                                                | 69.0 ms: 1.36x faster                                                 |
| pycparser                | 915 ms                                                 | 672 ms: 1.36x faster                                                  |
| json_dumps               | 8.38 ms                                                | 6.33 ms: 1.32x faster                                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.31x faster                                                |
| tornado_http             | 91.9 ms                                                | 70.3 ms: 1.31x faster                                                 |
| logging_format           | 5.01 us                                                | 3.85 us: 1.30x faster                                                 |
| logging_simple           | 4.63 us                                                | 3.58 us: 1.29x faster                                                 |
| spectral_norm            | 96.4 ms                                                | 74.7 ms: 1.29x faster                                                 |
| regex_compile            | 96.6 ms                                                | 75.4 ms: 1.28x faster                                                 |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                                |
| float                    | 72.3 ms                                                | 57.1 ms: 1.27x faster                                                 |
| create_gc_cycles         | 876 us                                                 | 697 us: 1.26x faster                                                  |
| dulwich_log              | 37.1 ms                                                | 30.0 ms: 1.24x faster                                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 543 ms: 1.23x faster                                                  |
| pprint_pformat           | 1.24 sec                                               | 1.01 sec: 1.23x faster                                                |
| generators               | 32.9 ms                                                | 26.7 ms: 1.23x faster                                                 |
| pprint_safe_repr         | 609 ms                                                 | 494 ms: 1.23x faster                                                  |
| deepcopy                 | 278 us                                                 | 227 us: 1.22x faster                                                  |
| fannkuch                 | 317 ms                                                 | 266 ms: 1.20x faster                                                  |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                                  |
| comprehensions           | 17.7 us                                                | 14.9 us: 1.18x faster                                                 |
| docutils                 | 1.78 sec                                               | 1.51 sec: 1.18x faster                                                |
| scimark_fft              | 232 ms                                                 | 199 ms: 1.16x faster                                                  |
| xml_etree_process        | 45.1 ms                                                | 39.0 ms: 1.16x faster                                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.06 us: 1.16x faster                                                 |
| nqueens                  | 68.1 ms                                                | 59.7 ms: 1.14x faster                                                 |
| coroutines               | 20.2 ms                                                | 17.7 ms: 1.14x faster                                                 |
| bench_thread_pool        | 548 us                                                 | 483 us: 1.14x faster                                                  |
| regex_v8                 | 17.5 ms                                                | 15.6 ms: 1.12x faster                                                 |
| sqlglot_optimize         | 38.0 ms                                                | 34.3 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.15 ms: 1.10x faster                                                 |
| meteor_contest           | 78.6 ms                                                | 73.2 ms: 1.07x faster                                                 |
| sqlglot_normalize        | 197 ms                                                 | 184 ms: 1.07x faster                                                  |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                                  |
| unpickle                 | 9.77 us                                                | 9.27 us: 1.05x faster                                                 |
| json                     | 3.10 ms                                                | 2.99 ms: 1.04x faster                                                 |
| python_startup           | 12.6 ms                                                | 12.3 ms: 1.03x faster                                                 |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                                |
| pickle                   | 7.36 us                                                | 7.42 us: 1.01x slower                                                 |
| pickle_list              | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| telco                    | 3.68 ms                                                | 3.74 ms: 1.02x slower                                                 |
| pickle_dict              | 17.8 us                                                | 18.2 us: 1.02x slower                                                 |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 75.1 ms: 1.03x slower                                                 |
| xml_etree_generate       | 54.3 ms                                                | 56.2 ms: 1.04x slower                                                 |
| json_loads               | 16.9 us                                                | 17.5 us: 1.04x slower                                                 |
| python_startup_no_site   | 9.73 ms                                                | 10.2 ms: 1.04x slower                                                 |
| regex_effbot             | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| sqlite_synth             | 1.47 us                                                | 1.57 us: 1.06x slower                                                 |
| bench_mp_pool            | 41.0 ms                                                | 46.3 ms: 1.13x slower                                                 |
| pathlib                  | 28.8 ms                                                | 33.7 ms: 1.17x slower                                                 |
| unpickle_list            | 2.66 us                                                | 3.19 us: 1.20x slower                                                 |
| dask                     | 258 ms                                                 | 319 ms: 1.24x slower                                                  |
| coverage                 | 40.8 ms                                                | 50.8 ms: 1.24x slower                                                 |
| async_generators         | 233 ms                                                 | 311 ms: 1.33x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (2): pidigits, gc_traversal
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
